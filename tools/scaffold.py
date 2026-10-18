"""Create a small HyperFrames project from local hf-kit blocks."""
import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
TOKENS = {
    "--hk-bg": "#0b0f14", "--hk-ink": "#f5f5f0", "--hk-paper": "#f3efe4",
    "--hk-accent": "#ffd23f", "--hk-positive": "#39ff6a", "--hk-negative": "#ff4d4d",
    "--hk-side-a": "#3be8ff", "--hk-side-b": "#ff7a3b",
    "--hk-font-display": '"Inter", system-ui, sans-serif',
    "--hk-font-body": '"Inter", system-ui, sans-serif',
}
REGISTRY = "https://raw.githubusercontent.com/heygen-com/hyperframes/v0.8.77/registry"


def build(destination, fmt, duration, style=None, blocks=None):
    destination = Path(destination)
    if destination.exists() and any(destination.iterdir()):
        raise ValueError(f"destination is not empty: {destination}")
    if duration <= 0:
        raise ValueError("duration must be positive")
    width, height = (1920, 1080) if fmt == "16:9" else (1080, 1920)
    selected = {}
    if style:
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", style):
            raise ValueError("invalid style id")
        source = KIT / "styles" / f"{style}.json"
        selected = json.loads(source.read_text(encoding="utf-8"))
        if selected.get("format") != fmt:
            raise ValueError(f"style {style} uses {selected.get('format')}, not {fmt}")
    names = blocks if blocks is not None else selected.get("blocks", [])
    names = list(dict.fromkeys(names))
    for name in names:
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            raise ValueError(f"invalid block name: {name}")
        if not (KIT / "blocks" / f"{name}.html").is_file():
            raise FileNotFoundError(f"missing block: {name}")
    tokens = TOKENS | selected.get("tokens", {})
    for key, value in tokens.items():
        if not re.fullmatch(r"--hk-[a-z-]+", key) or not isinstance(value, str) or any(c in value for c in ";{}<>"):
            raise ValueError(f"invalid token: {key}")
    css = "\n".join(f"      {key}: {value};" for key, value in tokens.items())
    slots = "\n".join(
        f'    <div id="{name}" class="clip" data-composition-id="{name}" '
        f'data-composition-src="compositions/{name}.html" data-start="0" '
        f'data-duration="{duration:g}" data-track-index="1" '
        f'data-width="{width}" data-height="{height}"></div>' for name in names
    )
    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width={width}, height={height}">
  <title>HyperFrames project</title>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <style>
    :root {{
{css}
    }}
    body {{ margin: 0; background: var(--hk-bg); color: var(--hk-ink); font-family: var(--hk-font-body); }}
    #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; }}
    .clip {{ position: absolute; inset: 0; }}
  </style>
</head>
<body>
  <div id="root" data-composition-id="main" data-start="0" data-width="{width}" data-height="{height}" data-duration="{duration:g}">
{slots}
  </div>
  <script>window.__timelines["main"] = gsap.timeline({{ paused: true }});</script>
</body>
</html>
'''
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "index.html").write_text(page, encoding="utf-8")
    (destination / "hyperframes.json").write_text(json.dumps({"registry": REGISTRY}, indent=2) + "\n", encoding="utf-8")
    if names:
        target = destination / "compositions"
        target.mkdir()
        for name in names:
            shutil.copyfile(KIT / "blocks" / f"{name}.html", target / f"{name}.html")
    return destination


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "demo"
        build(p, "9:16", 4)
        page = (p / "index.html").read_text(encoding="utf-8")
        assert 'data-width="1080" data-height="1920" data-duration="4"' in page
        assert 'gsap.timeline({ paused: true })' in page
        assert json.loads((p / "hyperframes.json").read_text())["registry"] == REGISTRY
        try:
            build(p, "9:16", 4)
        except ValueError:
            pass
        else:
            raise AssertionError("non-empty destination overwritten")
    print("scaffold selftest ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--format", choices=["16:9", "9:16"], required=False)
    ap.add_argument("--duration", type=float)
    ap.add_argument("--style")
    ap.add_argument("--blocks", help="comma-separated block names")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        if not args.dir or not args.format or args.duration is None:
            ap.error("dir, --format and --duration are required")
        print(build(args.dir, args.format, args.duration, args.style,
                    args.blocks.split(",") if args.blocks is not None else None))
