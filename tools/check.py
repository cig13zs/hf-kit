"""Advisory measurements for a rendered HyperFrames video."""
import argparse
import json
import re
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT / "research"))
import measure as research  # noqa: E402


def compare(value, limits):
    if value is None or limits is None:
        return "n/a"
    low, high = limits
    return "low" if value < low else "high" if value > high else "ok"


def rows(result, style):
    ranges = style.get("ranges", {})
    cuts = result["cuts"]
    audio = result["audio"]
    values = [(f"cuts/min {name}", value, ranges.get("cuts_per_min", {}).get(name))
              for name, value in cuts["per_min_by_segment"].items()]
    values += [
        ("median shot s", cuts["median_shot_s"], ranges.get("median_shot_s")),
        ("loudness LUFS", audio["integrated_lufs"], None),  # judged by the master line (-14), not the reference mixes
        ("LRA LU", audio["loudness_range_lu"], ranges.get("lra_lu")),
        ("silences/min", audio["silences_per_min"], ranges.get("silences_per_min")),
    ]
    if result.get("first_word_s") is not None:
        values.append(("first word s", result["first_word_s"], ranges.get("first_word_s")))
    return [(name, value, limits, compare(value, limits)) for name, value, limits in values]


def first_word(video):
    for path in (video.with_suffix(".words.json"), video.parent / "words.json", video.parent / "transcript.json"):
        if path.is_file():
            from captions import read_words
            try:
                return read_words(path)[0]["start"]
            except (ValueError, KeyError, IndexError):
                pass
    for path in (video.with_suffix(".srt"), video.with_suffix(".vtt")):
        if path.is_file():
            m = re.search(r"(\d\d):([0-5]\d):([0-5]\d)[,.](\d+)\s*-->", path.read_text(encoding="utf-8-sig"))
            if m:
                h, minute, sec, milli = m.groups()
                return int(h) * 3600 + int(minute) * 60 + int(sec) + int(milli.ljust(3, "0")[:3]) / 1000
    return None


def duration_s(video):
    proc = research.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(video)])
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip() or "ffprobe failed")
    return float(proc.stdout.strip())


def true_peak(video):
    proc = research.run([research.FFMPEG, "-hide_banner", "-nostats", "-i", str(video), "-vn", "-filter_complex", "ebur128=peak=true", "-f", "null", "-"])
    found = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", proc.stderr)
    return float(found[-1]) if found else None


def inspect(video):
    video = Path(video).resolve()
    dur = duration_s(video)
    times, scores = research.scene_scores(video)
    cuts = research.find_cuts(times, scores)
    import numpy as np
    shots = np.diff([0.0] + cuts + [dur])
    segments = research.segments(dur)
    named = {}
    for i, (a, b) in enumerate(segments):
        if dur <= 180:
            key = "0-3s" if a < 3 else "3-15s" if a < 15 else "15-60s" if a < 60 else "60s+"
        else:
            key = "last_min" if i == len(segments) - 1 and a >= 180 else "body" if a >= 180 else f"{a:g}-{b:g}s"
        named[key] = research.per_min(cuts, a, b)
    return {
        "cuts": {"per_min_by_segment": named, "median_shot_s": round(float(np.median(shots)), 2)},
        "audio": research.audio(video, dur),
        "first_word_s": first_word(video),
        "true_peak_dbtp": true_peak(video),
    }


def display(result, style):
    print(f"{'measure':<26} {'value':>10} {'style range':>16}  status")
    for name, value, limits, status in rows(result, style):
        target = f"{limits[0]}..{limits[1]}" if limits else "-"
        print(f"{name:<26} {str(value):>10} {target:>16}  {status}")
    lufs = result["audio"]["integrated_lufs"]
    peak = result.get("true_peak_dbtp")
    delta = f"{lufs + 14:+.1f} LU" if lufs is not None else "n/a"
    peak_state = "ok" if peak is not None and peak <= -1 else "high" if peak is not None else "n/a"
    print(f"master: {lufs} LUFS (target -14, {delta}), {peak} dBTP (ceiling -1, {peak_state})")


def selftest():
    fake = {
        "cuts": {"per_min_by_segment": {"0-3s": 42}, "median_shot_s": 1.7},
        "audio": {"integrated_lufs": -14.2, "loudness_range_lu": 2.2, "silences_per_min": 0},
        "first_word_s": 0, "true_peak_dbtp": -1.1,
    }
    style = {"ranges": {"cuts_per_min": {"0-3s": [30, 50]}, "median_shot_s": [2, 3],
                        "lra_lu": [1, 3], "silences_per_min": [1, 2]}}
    actual = {name: state for name, _, _, state in rows(fake, style)}
    assert actual["cuts/min 0-3s"] == "ok"
    assert actual["median shot s"] == "low"
    assert actual["silences/min"] == "low"
    assert compare(4, [1, 3]) == "high" and compare(None, [1, 3]) == "n/a"
    print("check selftest ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("render", nargs="?")
    ap.add_argument("--style")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        if not args.render:
            ap.error("render is required")
        try:
            style = {}
            if args.style:
                if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.style):
                    raise ValueError("invalid style id")
                style = json.loads((KIT / "styles" / f"{args.style}.json").read_text(encoding="utf-8"))
            display(inspect(Path(args.render)), style)
        except Exception as exc:
            print(f"measurement unavailable: {exc}", file=sys.stderr)
