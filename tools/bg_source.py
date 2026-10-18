"""Check a YouTube source's reuse licence before optionally downloading it."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import shutil
import subprocess


YTDLP = shutil.which("yt-dlp") or "yt-dlp"  # Same lookup as ../research/measure.py.
CLAIM = re.compile(r"no copyright|free to use|royalty[ -]free|copyright[ -]free|\bNCS\b", re.I)


def best_height(info):
    heights = [info.get("height")] + [fmt.get("height") for fmt in info.get("formats", [])]
    return max((h for h in heights if isinstance(h, (int, float)) and h > 0), default=None)


def decide(info, download=False, audio=False, min_height=1080):
    licence = str(info.get("license") or "")
    if "creative commons" in licence.casefold():
        height = best_height(info)
        if download and not audio and (height is None or height < min_height):
            return "REFUSE", f"Video download needs at least {min_height}p; best available is {height or 'unknown'}p.", []
        credit = (f'"{info.get("title") or "Untitled"}" by {info.get("channel") or "Unknown creator"} '
                  f'({info.get("webpage_url") or "unknown URL"}), licensed CC BY via YouTube')
        return "ACCEPT", credit, []
    title = str(info.get("title") or "")
    lines = [line.strip() for line in str(info.get("description") or "").splitlines()
             if CLAIM.search(line)]
    if CLAIM.search(title) or lines:
        return "REVIEW", "A claim in a title or description is the uploader's word, not a licence. Check that the uploader is the original creator, and keep a screenshot of the terms.", lines
    return "REFUSE", "No Creative Commons licence or reuse claim found.", []


def download_source(url, out, audio, min_height):
    out.mkdir(parents=True, exist_ok=True)
    fmt = "ba" if audio else f"bv[height>={min_height}]+ba/b[height>={min_height}]"
    cmd = [YTDLP, "--no-playlist", "--remote-components", "ejs:github", "-f", fmt,
           "--print", "after_move:filepath", "-o", str(out / "%(title).200B [%(id)s].%(ext)s"), url]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
    path = Path(result.stdout.strip().splitlines()[-1])
    if not path.is_file():
        raise RuntimeError(f"yt-dlp did not report an existing downloaded file: {path}")
    return str(path.resolve())


def selftest():
    base = {"title": "Quiet loop", "channel": "Creator", "webpage_url": "https://youtu.be/example",
            "license": "Creative Commons Attribution license (reuse allowed)", "height": 1080}
    assert decide(base)[0] == "ACCEPT"
    assert decide({**base, "license": "Standard YouTube License", "title": "No copyright loop"})[0] == "REVIEW"
    assert decide({**base, "license": "Standard YouTube License"})[0] == "REFUSE"
    assert decide({**base, "height": 720}, download=True, min_height=1080)[0] == "REFUSE"
    print("Self-test passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", nargs="?")
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--audio", action="store_true", help="Download the best audio only")
    parser.add_argument("--out", type=Path, default=Path("assets"))
    parser.add_argument("--min-height", type=int, default=1080)
    parser.add_argument("--log", type=Path, default=Path("sources/provenance.jsonl"))
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return 0
    if not args.url:
        parser.error("url is required unless --selftest is used")
    if args.min_height < 1:
        parser.error("--min-height must be positive")
    try:
        result = subprocess.run([YTDLP, "--dump-json", "--no-playlist", "--remote-components",
                                 "ejs:github", args.url], capture_output=True, text=True,
                                encoding="utf-8", errors="replace", check=True)
        info = json.loads(result.stdout.strip().splitlines()[-1])
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError) as exc:
        parser.exit(1, f"Could not read YouTube metadata: {exc}\n")

    decision, message, claim_lines = decide(info, args.download, args.audio, args.min_height)
    print(f"{decision}: {message}")
    if decision == "REVIEW":
        if CLAIM.search(str(info.get("title") or "")):
            print(f"Title claim: {info['title']}")
        for line in claim_lines:
            print(f"Description claim: {line}")
    file_path = None
    error = None
    if decision == "ACCEPT" and args.download:
        try:
            file_path = download_source(args.url, args.out, args.audio, args.min_height)
            print(f"Downloaded: {file_path}")
        except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
            error = str(exc)
    record = {"url": args.url, "title": info.get("title"), "channel": info.get("channel"),
              "channel_url": info.get("channel_url"), "licence": info.get("license"),
              "decision": decision, "credit_line": message if decision == "ACCEPT" else None,
              "date_checked": date.today().isoformat(), "file_path": file_path,
              "upload_date": info.get("upload_date"), "webpage_url": info.get("webpage_url"),
              "height": best_height(info), "duration": info.get("duration")}
    args.log.parent.mkdir(parents=True, exist_ok=True)
    with args.log.open("a", encoding="utf-8") as log:
        log.write(json.dumps(record, ensure_ascii=False) + "\n")
    if error:
        parser.exit(1, f"Download failed: {error}\n")
    return {"ACCEPT": 0, "REVIEW": 3, "REFUSE": 2}[decision]


if __name__ == "__main__":
    raise SystemExit(main())
