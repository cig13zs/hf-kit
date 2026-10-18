"""Measure how a YouTube video is edited: cuts, pacing, on-screen text, speech, loudness.

    python measure.py <url> [--niche NAME] [--role outlier|control] [--ratio 4.2] [--keep]
    python measure.py --selftest

Numbers go to research/data/<id>.json. Contact sheets, captions and the transcript stay
in research/_local/<id>/ (never committed). The downloaded media is deleted afterwards
unless --keep. Needs ffmpeg, yt-dlp and Tesseract.
"""
import argparse
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pytesseract
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
DATA, LOCAL = HERE / "data", HERE / "_local"
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
YTDLP = shutil.which("yt-dlp") or "yt-dlp"
CUT = 0.30       # ffmpeg scene score counted as a hard cut
MIN_SHOT = 0.25  # s; detections closer than this are one cut (flashes, strobes)
pytesseract.pytesseract.tesseract_cmd = shutil.which("tesseract") or r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def download(url, d):
    d.mkdir(parents=True, exist_ok=True)
    # -i: a caption 429 must not abort the video; missing captions are retried later with --skip-download.
    r = run([YTDLP, "--remote-components", "ejs:github", "-i", "--sleep-subtitles", "3", "--sleep-requests", "1",
             "--no-playlist", "--write-info-json", "--write-auto-subs", "--write-subs",
             "--sub-langs", "en,en-orig,en-US,en-GB", "--sub-format", "json3",
             "-f", "bv*[height<=360]+ba/b[height<=360]/b", "--merge-output-format", "mp4",
             "-o", str(d / "video.%(ext)s"), url])
    video = next((p for p in d.glob("video.*") if p.suffix in {".mp4", ".webm", ".mkv"}), None)
    if not video:
        raise RuntimeError(f"yt-dlp wrote no video:\n{(r.stderr or r.stdout)[-1500:]}")
    return video, json.loads((d / "video.info.json").read_text(encoding="utf-8"))


def scene_scores(video):
    """Scene-change score of every frame (0 = identical to the previous frame, 1 = new shot)."""
    with tempfile.TemporaryDirectory() as t:
        run([FFMPEG, "-hide_banner", "-nostats", "-i", str(video), "-an", "-vf",
             "scale=160:-2,select='gte(scene\\,0)',metadata=print:key=lavfi.scene_score:file=s.txt",
             "-f", "null", "-"], cwd=t)
        times, scores = [], []
        for line in (Path(t) / "s.txt").read_text().splitlines():
            if "pts_time:" in line:
                times.append(float(line.split("pts_time:")[1].split()[0]))
            elif "scene_score=" in line:
                scores.append(float(line.split("=")[1]))
    n = min(len(times), len(scores))
    return np.array(times[:n]), np.array(scores[:n])


def find_cuts(times, scores):
    cuts = []
    for t, s in zip(times, scores):
        if s >= CUT and t > 0 and (not cuts or t - cuts[-1] >= MIN_SHOT):
            cuts.append(round(float(t), 2))
    return cuts


def segments(dur):
    # Shorts get their own opening windows; long-form gets hook / setup / body / ending.
    edges = [0, 3, 15, 60] if dur <= 180 else [0, 15, 60, 180] + ([dur - 60] if dur - 60 > 180 else [])
    edges = sorted({e for e in edges if e < dur} | {dur})
    return [(a, b) for a, b in zip(edges, edges[1:]) if b - a >= 1]


def per_min(events, a, b):
    return round(sum(a <= t < b for t in events) / ((b - a) / 60), 1)


def audio(video, dur):
    r = run([FFMPEG, "-hide_banner", "-nostats", "-i", str(video), "-vn", "-af",
             "ebur128=framelog=info,silencedetect=n=-35dB:d=0.4", "-f", "null", "-"])
    err = r.stderr
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", err)
    lra = re.findall(r"LRA:\s+([\d.]+) LU", err)
    curve = {}
    for m in re.finditer(r"t:\s*([\d.]+)\s+TARGET.*?S:\s*(-?[\d.]+|-inf)", err):
        curve[int(float(m.group(1)) // 2) * 2] = None if m.group(2) == "-inf" else round(float(m.group(2)), 1)
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    ends = re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", err)
    silences = [(round(float(s), 2), round(float(d), 2)) for s, (e, d) in zip(starts, ends)]
    return {
        "integrated_lufs": float(lufs[-1]) if lufs else None,
        "loudness_range_lu": float(lra[-1]) if lra else None,
        "shortterm_lufs_every_2s": [curve[k] for k in sorted(curve)],
        "silences": silences,
        "silences_per_min": round(len(silences) / (dur / 60), 2),
        "silence_share": round(sum(d for _, d in silences) / dur, 3),
        "onsets_per_min": onsets_per_min(video, dur),
    }


def onsets_per_min(video, dur, sr=11025, n=1024, hop=512):
    """Spectral-flux onsets: a rough proxy for sound-design density (hits, whooshes, beats)."""
    raw = subprocess.run([FFMPEG, "-v", "error", "-i", str(video), "-vn", "-ac", "1", "-ar", str(sr),
                          "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    if x.size < n * 4:
        return None
    # Whole signal in memory: fine to about 1 h at 11 kHz.
    frames = np.lib.stride_tricks.sliding_window_view(x, n)[::hop] * np.hanning(n).astype(np.float32)
    mag = np.log1p(10 * np.abs(np.fft.rfft(frames, axis=1)))
    flux = np.maximum(np.diff(mag, axis=0), 0).sum(1)
    w = sr // hop  # ~1 s window
    local = np.convolve(flux, np.ones(w) / w, mode="same")
    thr = local + 1.5 * flux.std()
    peaks = [i for i in range(3, len(flux) - 3)
             if flux[i] > thr[i] and flux[i] == flux[i - 3:i + 4].max()]
    kept, last = 0, -1e9
    for i in peaks:  # 100 ms refractory period
        if (i - last) * hop / sr >= 0.1:
            kept, last = kept + 1, i
    return round(kept / (dur / 60), 1)


def speech(d, dur):
    f = next(d.glob("video.*.json3"), None)
    if not f:
        return None, []
    words = []
    for e in json.loads(f.read_text(encoding="utf-8")).get("events", []):
        t0 = e.get("tStartMs", 0)
        for s in e.get("segs") or []:
            tok = s.get("utf8", "").strip()
            if tok and not re.fullmatch(r"\[.*\]", tok):
                words += [((t0 + s.get("tOffsetMs", 0)) / 1000, w) for w in tok.split()]
    if not words:
        return None, []
    head = [w for t, w in words if t < 30]
    return {
        "caption_track": f.name.split(".")[-2],
        "words": len(words),
        "wpm": round(len(words) / (dur / 60), 1),
        "wpm_first_30s": round(len(head) / (min(30, dur) / 60), 1),
        "first_word_s": round(words[0][0], 2),
    }, words


def grab(video, times, out, w=240):
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, t in enumerate(times):
        p = out / f"{i:03d}.jpg"
        run([FFMPEG, "-hide_banner", "-loglevel", "error", "-ss", f"{max(t, 0):.2f}", "-i", str(video),
             "-frames:v", "1", "-vf", f"scale={w}:-2", "-q:v", "4", "-y", str(p)])
        if p.exists():
            paths.append((t, p))
    return paths


def sheet(frames, cols, dest, labels=None, tw=240):
    if not frames:
        return
    ims = [Image.open(p) for _, p in frames]
    w = tw
    h = round(ims[0].size[1] * tw / ims[0].size[0])
    rows = -(-len(ims) // cols)
    canvas = Image.new("RGB", (cols * w, rows * h), "black")
    draw = ImageDraw.Draw(canvas)
    for i, (im, (t, _)) in enumerate(zip(ims, frames)):
        x, y = i % cols * w, i // cols * h
        canvas.paste(im.resize((w, h)), (x, y))
        label = labels[i] if labels else f"{int(t // 60)}:{t % 60:04.1f}"
        draw.rectangle([x, y, x + 7 * len(label) + 4, y + 13], fill="black")
        draw.text((x + 2, y + 1), label, fill="yellow")
    canvas.save(dest, quality=85)


def ocr_share(frames):
    hits, words = 0, 0
    for _, p in frames:
        data = pytesseract.image_to_data(Image.open(p), output_type=pytesseract.Output.DICT)
        n = sum(1 for w, c in zip(data["text"], data["conf"])
                if float(c) > 70 and len(w.strip()) >= 2 and any(ch.isalpha() for ch in w))
        words += n
        hits += n >= 2
    return {"frames_checked": len(frames), "text_share": round(hits / max(len(frames), 1), 2),
            "words_per_frame": round(words / max(len(frames), 1), 1)}


def measure(video, info, d, niche=None, role=None, ratio=None):
    dur = float(info.get("duration") or 0)
    times, scores = scene_scores(video)
    dur = dur or float(times[-1])
    cuts = find_cuts(times, scores)
    shots = np.diff([0.0] + cuts + [dur])
    energy = [round(float(scores[(times >= m * 60) & (times < m * 60 + 60)].mean() * 100), 2)
              for m in range(int(dur // 60) + 1) if ((times >= m * 60) & (times < m * 60 + 60)).any()]
    sp, words = speech(d, dur)

    sheets = d / "sheets"
    sheets.mkdir(exist_ok=True)
    hook = grab(video, [i / 2 for i in range(int(min(30, dur) * 2))], d / "tmp_hook")
    sheet(hook[:30], 10, sheets / "hook_00-15s.jpg")
    sheet(hook[30:], 10, sheets / "hook_15-30s.jpg")
    # 640 px so the same 40 frames serve the overview sheet and OCR.
    overview = grab(video, [dur * (i + 0.5) / 40 for i in range(40)], d / "tmp_over", w=640)
    sheet(overview, 8, sheets / "overview_40.jpg")
    pick = [cuts[int(i * len(cuts) / 12)] for i in range(min(12, len(cuts)))]
    pairs = grab(video, [t + o for t in pick for o in (-0.15, 0.1)], d / "tmp_cuts")
    sheet(pairs, 6, sheets / "cuts_before_after.jpg",
          labels=[f"{'pre' if i % 2 == 0 else 'post'} {int(t // 60)}:{t % 60:04.1f}" for i, (t, _) in enumerate(pairs)])
    text = ocr_share(overview)

    if words:  # transcript stays local
        lines, cur, start = [], [], None
        for t, w in words:
            start = t if start is None else start
            cur.append(w)
            if len(cur) >= 14:
                lines.append(f"[{int(start // 60):02d}:{start % 60:04.1f}] {' '.join(cur)}")
                cur, start = [], None
        if cur:
            lines.append(f"[{int(start // 60):02d}:{start % 60:04.1f}] {' '.join(cur)}")
        (d / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")

    return {
        "id": info.get("id"), "url": info.get("webpage_url"), "title": info.get("title"),
        "channel": info.get("channel"), "channel_followers": info.get("channel_follower_count"),
        "upload_date": info.get("upload_date"), "duration_s": round(dur, 1),
        "views": info.get("view_count"), "likes": info.get("like_count"), "comments": info.get("comment_count"),
        "vertical": (info.get("height") or 0) > (info.get("width") or 1),
        "niche": niche, "role": role, "outlier_ratio": ratio,
        "checked": __import__("datetime").date.today().isoformat(),
        "cuts": {
            "note": "hard cuts only (ffmpeg scene >= %.2f); dissolves and whip-pans undercount, so a floor" % CUT,
            "count": len(cuts), "per_min": round(len(cuts) / (dur / 60), 1),
            "per_min_by_segment": {f"{a:g}-{b:g}s": per_min(cuts, a, b) for a, b in segments(dur)},
            "avg_shot_s": round(float(shots.mean()), 2), "median_shot_s": round(float(np.median(shots)), 2),
            "shot_p10_p90_s": [round(float(np.percentile(shots, 10)), 2), round(float(np.percentile(shots, 90)), 2)],
            "times": cuts,
        },
        "visual_energy_per_min": energy,
        "on_screen_text": text,
        "speech": sp,
        "audio": audio(video, dur),
    }


def selftest():
    with tempfile.TemporaryDirectory() as t:
        v = Path(t) / "t.mp4"
        run([FFMPEG, "-y", "-f", "lavfi", "-i", "color=red:s=320x240:d=2", "-f", "lavfi", "-i", "color=blue:s=320x240:d=3",
             "-f", "lavfi", "-i", "color=green:s=320x240:d=1.5",
             "-f", "lavfi", "-i", "aevalsrc='if(between(t,3,4),0,0.4*sin(2*PI*440*t))':d=6.5",
             "-filter_complex", "[0][1][2]concat=n=3:v=1:a=0[v]", "-map", "[v]", "-map", "3", "-shortest", str(v)])
        times, scores = scene_scores(v)
        cuts = find_cuts(times, scores)
        assert len(cuts) == 2 and abs(cuts[0] - 2) < 0.1 and abs(cuts[1] - 5) < 0.1, cuts
        a = audio(v, 6.5)
        assert len(a["shortterm_lufs_every_2s"]) >= 3, "loudness curve empty"
        assert len(a["silences"]) == 1 and abs(a["silences"][0][0] - 3) < 0.2, a["silences"]
        assert segments(6.5) == [(0, 3), (3, 6.5)]
        assert segments(200) == [(0, 15), (15, 60), (60, 180), (180, 200)]
        assert segments(600) == [(0, 15), (15, 60), (60, 180), (180, 540), (540, 600)]
        print("selftest ok:", cuts, a["silences"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", nargs="?")
    ap.add_argument("--niche")
    ap.add_argument("--role", choices=["outlier", "control"])
    ap.add_argument("--ratio", type=float)
    ap.add_argument("--keep", action="store_true", help="keep the downloaded media")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest or not a.url:
        return selftest()
    vid = re.search(r"(?:v=|shorts/|youtu\.be/)([\w-]{11})", a.url)
    d = LOCAL / (vid.group(1) if vid else "unknown")
    video, info = download(a.url, d)
    result = measure(video, info, d, a.niche, a.role, a.ratio)
    DATA.mkdir(exist_ok=True)
    out = DATA / f"{result['id']}.json"
    out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    for p in d.glob("tmp_*"):
        shutil.rmtree(p)
    if not a.keep:
        video.unlink()
        (d / "video.info.json").unlink(missing_ok=True)
    c = result["cuts"]
    print(f"{out.name}: {result['title']!r} {result['duration_s']}s, {c['count']} cuts ({c['per_min']}/min), "
          f"median shot {c['median_shot_s']}s, {result['audio']['integrated_lufs']} LUFS, sheets in {d / 'sheets'}")


if __name__ == "__main__":
    main()
