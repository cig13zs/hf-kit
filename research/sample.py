"""Find a channel's outliers: uploads that beat the channel's own median views.

    python sample.py @MarkRober [--tab videos|shorts] [--n 80]
    python sample.py --search "minecraft shorts" [--n 20]     # YouTube search sorted by views

Median = the latest 30 uploads. Ratio = views / median. Writes _local/candidates/*.json.
"""
import argparse
import base64
import json
import re
import shutil
import statistics
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote_plus

OUT = Path(__file__).resolve().parent / "_local" / "candidates"
YTDLP = shutil.which("yt-dlp") or "yt-dlp"


def flat(url, n):
    r = subprocess.run([YTDLP, "--flat-playlist", "-J", "--playlist-end", str(n), url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(r.stderr[-800:])
    return json.loads(r.stdout)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", nargs="?")
    ap.add_argument("--tab", default="videos", choices=["videos", "shorts"])
    ap.add_argument("--search")
    ap.add_argument("--short", action="store_true", help="search: under 4 minutes")
    ap.add_argument("--this-year", action="store_true", help="search: uploaded this year")
    ap.add_argument("--n", type=int, default=80)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    if a.search:
        # sp is a base64 protobuf: 08 03 = sort by views; filter 12 <len>: 08 05 = this year, 18 01 = under 4 min.
        f = (b"\x08\x05" if a.this_year else b"") + (b"\x18\x01" if a.short else b"")
        sp = b"\x08\x03" + (b"\x12" + bytes([len(f)]) + f if f else b"")
        d = flat(f"https://www.youtube.com/results?search_query={quote_plus(a.search)}"
                 f"&sp={quote_plus(base64.b64encode(sp).decode())}&gl=US&hl=en", a.n)
        rows = [{"id": e["id"], "views": e.get("view_count"), "channel": e.get("channel"),
                 "duration": e.get("duration"), "title": e.get("title")} for e in d["entries"]]
        for r in rows:
            print(f"{r['id']}  {r['views'] or 0:>13,}  {str(r['duration']):>6}s  {r['channel']}: {r['title'][:60]}")
        name = re.sub(r"\W+", "-", a.search).strip("-")
        (OUT / f"search-{name}.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
        return

    handle = a.channel if a.channel.startswith("http") else f"https://www.youtube.com/{a.channel}"
    d = flat(f"{handle.rstrip('/')}/{a.tab}", a.n)
    entries = [e for e in d["entries"] if e.get("view_count")]
    median = statistics.median(e["view_count"] for e in entries[:30])
    rows = [{"rank_recent": i, "id": e["id"], "views": e["view_count"], "ratio": round(e["view_count"] / median, 2),
             "duration": e.get("duration"), "title": e.get("title")} for i, e in enumerate(entries)]
    print(f"{d.get('channel')}  followers={d.get('channel_follower_count')}  median(last 30)={median:,.0f}  n={len(rows)}")
    for r in sorted(rows, key=lambda r: -r["ratio"])[:8]:
        print(f"  #{r['rank_recent']:>3}  {r['id']}  {r['views']:>13,}  x{r['ratio']:<5}  {str(r['duration']):>6}s  {r['title'][:60]}")
    control = min(rows[:30], key=lambda r: abs(r["ratio"] - 1))
    print(f"  control  #{control['rank_recent']}  {control['id']}  {control['views']:,}  x{control['ratio']}  {control['title'][:60]}")
    out = {"channel": d.get("channel"), "followers": d.get("channel_follower_count"), "tab": a.tab,
           "median_last30": median, "rows": rows, "control": control}
    stem = re.sub(r"\W+", "", a.channel)
    (OUT / f"{stem}-{a.tab}.json").write_text(json.dumps(out, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
