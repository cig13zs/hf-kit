"""Music and sound measurements for videos already run through measure.py.

    python audio_features.py <video-id> [...]      # or --all
    python audio_features.py --selftest

Downloads audio only, adds a "music" block to research/data/<id>.json, deletes the audio.
Nothing here listens, so these are proxies, each named for what it actually measures.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA, LOCAL = HERE / "data", HERE / "_local"
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
YTDLP = shutil.which("yt-dlp") or "yt-dlp"
SR, N, HOP = 22050, 2048, 512
FPS = SR / HOP  # onset-envelope frames per second


def decode(path):
    raw = subprocess.run([FFMPEG, "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(SR),
                          "-f", "s16le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def spectra(x):
    """Per-frame spectral flux, centroid (Hz) and share of energy below 150 Hz, in 60 s chunks to bound memory."""
    win = np.hanning(N).astype(np.float32)
    freqs = np.fft.rfftfreq(N, 1 / SR)
    low = freqs < 150
    flux, cent, bass, prev = [], [], [], None
    step = SR * 60
    for s in range(0, max(len(x) - N, 1), step):
        seg = x[s:s + step + N]
        if len(seg) < N:
            break
        fr = np.lib.stride_tricks.sliding_window_view(seg, N)[::HOP][: step // HOP] * win
        mag = np.abs(np.fft.rfft(fr, axis=1))
        power = mag ** 2 + 1e-12
        cent.append((power * freqs).sum(1) / power.sum(1))
        bass.append(power[:, low].sum(1) / power.sum(1))
        lm = np.log1p(10 * mag)
        d = np.diff(np.vstack([lm[:1] if prev is None else prev, lm]), axis=0)
        flux.append(np.maximum(d, 0).sum(1))
        prev = lm[-1:]
    return np.concatenate(flux), np.concatenate(cent), np.concatenate(bass)


def onsets(flux):
    w = int(FPS)
    local = np.convolve(flux, np.ones(w) / w, mode="same")
    thr = local + 1.5 * flux.std()
    peaks = [i for i in range(3, len(flux) - 3) if flux[i] > thr[i] and flux[i] == flux[i - 3:i + 4].max()]
    out, last = [], -1e9
    for i in peaks:
        if i - last >= 0.1 * FPS:
            out.append((i * HOP + N / 2) / SR)  # frame centre, not frame start
            last = i
    return np.array(out)


def tempo(flux, lo=60, hi=180):
    """BPM from onset-envelope autocorrelation; confidence = peak / mean autocorrelation in range."""
    e = np.convolve(flux, np.ones(3) / 3, mode="same")  # smoothing lets off-grid beat lags still line up
    e = e - e.mean()
    ac = np.correlate(e, e, mode="full")[len(e) - 1:]
    lags = np.arange(int(FPS * 60 / hi), int(FPS * 60 / lo) + 1)
    if len(ac) <= lags[-1]:
        return None, None
    seg = ac[lags]
    # Log-normal prior around 120 BPM (one-octave spread) breaks half/double-tempo ties, as beat trackers do.
    prior = np.exp(-0.5 * np.log2(60 * FPS / lags / 120) ** 2)
    # Only interior peaks count: narration's autocorrelation just decays, so its argmax sits on the range edge (184.6).
    peaks = [i for i in range(1, len(seg) - 1) if seg[i] > 0 and seg[i] >= seg[i - 1] and seg[i] >= seg[i + 1]]
    if not peaks:
        return None, None
    i = max(peaks, key=lambda i: seg[i] * prior[i])
    return round(60 * FPS / lags[i], 1), round(float(seg[i] / (np.abs(seg).mean() + 1e-9)), 2)


def cut_alignment(cuts, ons, dur, tol=0.06, trials=300, seed=7):
    """Share of cuts within ±tol s of an audio onset, against the same count of random times."""
    if len(cuts) < 5 or len(ons) < 5:
        return None
    near = lambda t: np.min(np.abs(ons[:, None] - np.asarray(t)[None, :]), axis=0) <= tol
    observed = float(near(cuts).mean())
    rng = np.random.default_rng(seed)
    chance = float(np.mean([near(rng.uniform(0, dur, len(cuts))).mean() for _ in range(trials)]))
    return {"within_s": tol, "observed": round(observed, 3), "chance": round(chance, 3),
            "lift": round(observed / chance, 2) if chance else None}


def windows(values, seconds, fn=np.mean):
    per = int(seconds * FPS)
    return [round(float(fn(values[i:i + per])), 3) for i in range(0, len(values) - per // 2, per)]


def caption_tags(d, dur):
    f = next(d.glob("video.*.json3"), None)
    if not f:
        return None
    tags = {}
    for e in json.loads(f.read_text(encoding="utf-8")).get("events", []):
        for s in e.get("segs") or []:
            m = re.fullmatch(r"\[(.+)\]", s.get("utf8", "").strip())
            if m:
                tags.setdefault(m.group(1).lower(), []).append(round(e.get("tStartMs", 0) / 1000, 1))
    return {k: {"count": len(v), "per_min": round(len(v) / (dur / 60), 2), "times": v[:60]} for k, v in tags.items()}


def loudness_curve(path):
    err = subprocess.run([FFMPEG, "-hide_banner", "-nostats", "-i", str(path), "-vn", "-af", "ebur128=framelog=info",
                          "-f", "null", "-"], capture_output=True, text=True, errors="replace").stderr
    curve = {}
    for m in re.finditer(r"t:\s*([\d.]+)\s+TARGET.*?S:\s*(-?[\d.]+|-inf)", err):
        curve[int(float(m.group(1)) // 2) * 2] = None if m.group(2) == "-inf" else round(float(m.group(2)), 1)
    return [curve[k] for k in sorted(curve)]


def analyze(x, cuts, dur):
    flux, cent, bass = spectra(x)
    ons = onsets(flux)
    bpm, conf = tempo(flux)
    per_min_bpm = [tempo(flux[i:i + int(60 * FPS)])[0] for i in range(0, len(flux) - int(30 * FPS), int(60 * FPS))]
    return {
        "note": "proxies: tempo from onset autocorrelation (speech-heavy audio lowers confidence); "
                "brightness = spectral centroid; bass = energy share under 150 Hz",
        "tempo_bpm": bpm, "tempo_confidence": conf, "tempo_by_minute": per_min_bpm,
        "onsets_per_min": round(len(ons) / (dur / 60), 1),
        "cuts_on_audio_onsets": cut_alignment(cuts, ons, dur),
        "brightness_hz_every_10s": windows(cent, 10),
        "bass_share_every_10s": windows(bass, 10),
    }


def run_one(vid):
    f = DATA / f"{vid}.json"
    data = json.loads(f.read_text(encoding="utf-8"))
    d = LOCAL / vid
    d.mkdir(parents=True, exist_ok=True)
    subprocess.run([YTDLP, "--remote-components", "ejs:github", "-f", "ba", "-o", str(d / "audio.%(ext)s"), "--no-playlist", data["url"]],
                   capture_output=True)
    audio = next((p for p in d.glob("audio.*")), None)
    if not audio:
        print(f"FAIL {vid}: no audio downloaded")
        return
    dur = data["duration_s"]
    music = analyze(decode(audio), data["cuts"]["times"], dur)
    music["caption_tags"] = caption_tags(d, dur)
    if not data["audio"].get("shortterm_lufs_every_2s"):
        data["audio"]["shortterm_lufs_every_2s"] = loudness_curve(audio)
    data["music"] = music
    f.write_text(json.dumps(data, indent=1), encoding="utf-8")
    audio.unlink()
    a = music["cuts_on_audio_onsets"] or {}
    print(f"{vid}: {music['tempo_bpm']} BPM (conf {music['tempo_confidence']}), cuts on onsets "
          f"{a.get('observed')} vs chance {a.get('chance')} (lift {a.get('lift')})")


def selftest():
    # 120 BPM click track, 20 s, with cuts placed exactly on beats: tempo ~120, lift well above 1.
    t = np.arange(20 * SR) / SR
    x = np.zeros_like(t, dtype=np.float32)
    for b in np.arange(0, 20, 0.5):
        i = int(b * SR)
        x[i:i + 400] += np.sin(2 * np.pi * 1000 * t[:400]) * np.exp(-np.arange(400) / 80)
    r = analyze(x, [round(b, 2) for b in np.arange(1, 19, 1.0)], 20)
    assert r["tempo_bpm"] and abs(r["tempo_bpm"] - 120) < 4, r["tempo_bpm"]
    assert r["cuts_on_audio_onsets"]["lift"] > 2, r["cuts_on_audio_onsets"]
    print("selftest ok:", r["tempo_bpm"], r["cuts_on_audio_onsets"])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args or args == ["--selftest"]:
        return selftest()
    ids = [p.stem for p in sorted(DATA.glob("*.json")) if "music" not in json.loads(p.read_text(encoding="utf-8"))] \
        if args == ["--all"] else args
    for vid in ids:
        try:
            run_one(vid)
        except Exception as e:  # one bad video shouldn't stop the batch
            print(f"FAIL {vid}: {e}")


if __name__ == "__main__":
    main()
