"""Turn timed words into a HyperFrames caption sub-composition."""
import argparse
import html
import json
import math
import tempfile
from pathlib import Path


def read_words(path):
    data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    if isinstance(data, dict):
        if "transcription" in data:
            tokens = [token for segment in data["transcription"] for token in segment.get("tokens", [])]
            data = []
            for token in tokens:
                raw = token.get("text", "")
                word = raw.strip()
                if not word or word.startswith(("[_", "[BLANK")):
                    continue
                end = float(token.get("offsets", {}).get("to", 0)) / 1000
                if data and (not raw.startswith(" ") or word in ".,!?;:'\")]}>"):
                    data[-1]["text"] += word
                    data[-1]["end"] = end
                else:
                    data.append({"text": word, "start": float(token.get("offsets", {}).get("from", 0)) / 1000,
                                 "end": end})
            for i, item in enumerate(data):
                if item["end"] <= item["start"]:
                    item["end"] = data[i + 1]["start"] if i + 1 < len(data) else item["start"] + 0.1
        elif "words" in data:
            data = data["words"]
        elif "segments" in data:
            data = [word for segment in data["segments"] for word in segment.get("words", [segment])]
        else:
            raise ValueError("expected a word list or an object with words/segments")
    words = []
    for item in data:
        word = item.get("text", item.get("word"))
        if word is None or "start" not in item or "end" not in item:
            raise ValueError("each word needs text or word, start, and end")
        start, end = float(item["start"]), float(item["end"])
        if not word.strip() or not math.isfinite(start) or not math.isfinite(end) or start < 0 or end <= start:
            raise ValueError(f"invalid word timing: {item}")
        words.append({"text": word.strip(), "start": start, "end": end,
                      "speaker": str(item.get("speaker", "")), "class": str(item.get("class", ""))})
    if not words or any(a["start"] > b["start"] for a, b in zip(words, words[1:])):
        raise ValueError("words must be nonempty and sorted by start")
    return words


def groups(words, variant):
    limit = {"cards": 4, "karaoke": 4, "speaker": 5, "keyword": 4, "punch": 1}[variant]
    result, current = [], []
    for word in words:
        split = current and (len(current) >= limit or
                             (variant == "speaker" and word["speaker"] != current[0]["speaker"]) or
                             (variant == "cards" and word["start"] - current[0]["start"] >= 1.0))
        if split:
            result.append(current)
            current = []
        current.append(word)
    if current:
        result.append(current)
    return result


def make_html(words, variant, fmt):
    width, height = (1920, 1080) if fmt == "16:9" else (1080, 1920)
    duration = max(word["end"] for word in words) + (1.2 if variant == "punch" else 0.05)
    groups_ = groups(words, variant)
    speakers = list(dict.fromkeys(w["speaker"] for w in words))
    pieces, animations = [], []
    for i, group in enumerate(groups_):
        start = group[0]["start"]
        end = group[-1]["end"]
        if variant == "punch":
            end = max(end, start + 1.2)
        if i + 1 < len(groups_):
            end = min(end, groups_[i + 1][0]["start"])
        end = max(end, start + 0.04)
        spans = []
        for j, word in enumerate(group):
            classes = ["word"]
            if variant == "keyword" and word["class"] in {"kw", "money"}:
                classes.append(word["class"])
            if variant == "speaker":
                classes.append("speaker-a" if speakers.index(word["speaker"]) % 2 == 0 else "speaker-b")
            ident = f"w-{i}-{j}"
            spans.append(f'<span id="{ident}" class="{" ".join(classes)}">{html.escape(word["text"])}</span>')
            if variant == "karaoke":
                animations.append(f'tl.set("#{ident}", {{ color: "var(--hk-side-a, #3be8ff)" }}, {word["start"]:.3f});')
                animations.append(f'tl.set("#{ident}", {{ color: "var(--hk-ink, #f5f5f0)" }}, {word["end"]:.3f});')
            elif variant == "keyword":
                animations.append(f'tl.fromTo("#{ident}", {{ scale: 0.92 }}, {{ scale: 1, duration: 0.1, ease: "none" }}, {word["start"]:.3f});')
        contents = " ".join(spans)
        pieces.append(f'      <section id="cap-{i}" class="clip card" data-start="{start:.3f}" data-duration="{end-start:.3f}" data-track-index="5"><div class="line">{contents}</div></section>')
        if variant == "cards":
            animations.append(f'tl.fromTo("#cap-{i} .line", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.067, ease: "none" }}, {start:.3f});')
        elif variant == "punch":
            animations.append(f'tl.fromTo("#cap-{i} .line", {{ scale: 0.6 }}, {{ scale: 1, duration: 0.12, ease: "power4.out" }}, {start:.3f});')
    position = "78%" if variant == "cards" else "55%" if variant == "speaker" else "72%"
    css_extra = '''.kw { color: var(--hk-accent, #ffd23f); }
        .money { color: var(--hk-positive, #39ff6a); }''' if variant == "keyword" else '''.speaker-a { color: var(--hk-side-a, #3be8ff); }
        .speaker-b { color: var(--hk-side-b, #ff7a3b); }''' if variant == "speaker" else ""
    punch = 'font-style: italic; text-transform: uppercase; -webkit-text-stroke: 4px var(--hk-bg);' if variant == "punch" else ""
    font_size = "6.5vmin" if fmt == "16:9" else "8vmin"
    use = {"cards": "fast narrated facts", "karaoke": "fast gaming talk", "speaker": "two-speaker clips",
           "keyword": "selective cooking keywords and money", "punch": "one reaction or claim"}[variant]
    avoid = {"cards": "faces or products at 78% height", "karaoke": "slow emotional speech",
             "speaker": "more than three speaker colours", "keyword": "colouring every word",
             "punch": "continuous subtitles"}[variant]
    return f'''<!doctype html>
<html lang="en" data-composition-variables='[
  {{"id":"fontScale","type":"number","label":"Font scale","default":1,"min":0.5,"max":2}},
  {{"id":"accentOverride","type":"string","label":"Accent override","default":""}},
  {{"id":"sideAOverride","type":"string","label":"Speaker A override","default":""}},
  {{"id":"sideBOverride","type":"string","label":"Speaker B override","default":""}}
]'>
<body>
<template>
  <!-- {variant} captions; source: {dict(cards='shorts-facts',karaoke='shorts-gaming',speaker='shorts-podcast',keyword='cooking',punch='challenge-spectacle')[variant]} steal list. -->
  <!-- Works for {use}; backfires on {avoid}. Variables: fontScale, colour overrides. -->
  <style>
    #root {{ position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; color: var(--hk-ink, #f5f5f0); font-family: var(--hk-font-display, Inter, system-ui, sans-serif); }}
    .card {{ position: absolute; inset: 0; display: flex; justify-content: center; align-items: flex-start; pointer-events: none; }}
    .line {{ position: absolute; top: calc({position} - 0.5em); max-width: 90%; text-align: center; font-size: calc({font_size} * var(--caption-scale, 1)); font-weight: 800; line-height: 1.12; overflow-wrap: anywhere; {punch} }}
    .word {{ display: inline-block; }}
    {css_extra}
  </style>
  <div id="root" data-composition-id="captions" data-start="0" data-width="{width}" data-height="{height}" data-duration="{duration:.3f}">
{chr(10).join(pieces)}
  </div>
  <script>
    const {{ fontScale, accentOverride, sideAOverride, sideBOverride }} = window.__hyperframes.getVariables();
    const root = document.querySelector('[data-composition-id="captions"]');
    root.style.setProperty("--caption-scale", fontScale);
    if (accentOverride) root.style.setProperty("--hk-accent", accentOverride);
    if (sideAOverride) root.style.setProperty("--hk-side-a", sideAOverride);
    if (sideBOverride) root.style.setProperty("--hk-side-b", sideBOverride);
    const tl = gsap.timeline({{ paused: true }});
    {' '.join(animations)}
    window.__timelines["captions"] = tl;
  </script>
</template>
</body>
</html>
'''


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        path = tmp / "words.json"
        path.write_text(json.dumps({"segments": [{"words": [
            {"word": "Hello", "start": 0, "end": 0.4},
            {"word": "world", "start": 0.4, "end": 0.9, "speaker": "B", "class": "kw"}]}]}), encoding="utf-8")
        words = read_words(path)
        whisper = tmp / "transcript.json"
        whisper.write_text(json.dumps({"transcription": [{"tokens": [
            {"text": " Hello", "offsets": {"from": 0, "to": 400}},
            {"text": " world", "offsets": {"from": 400, "to": 800}},
            {"text": "!", "offsets": {"from": 800, "to": 900}}]}]}), encoding="utf-8")
        assert [w["text"] for w in read_words(whisper)] == ["Hello", "world!"]
        for variant in ("cards", "karaoke", "speaker", "keyword", "punch"):
            output = make_html(words, variant, "9:16")
            assert 'data-composition-id="captions"' in output and 'data-width="1080"' in output
            assert "Hello" in output and "world" in output
        assert 'duration: 0.067' in make_html(words, "cards", "9:16")
        assert 'duration: 0.12' in make_html(words, "punch", "9:16")
    print("captions selftest ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("words", nargs="?")
    ap.add_argument("--variant", choices=["cards", "karaoke", "speaker", "keyword", "punch"])
    ap.add_argument("--format", choices=["16:9", "9:16"])
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        if not all((args.words, args.variant, args.format, args.out)):
            ap.error("words, --variant, --format and --out are required")
        out = Path(args.out)
        if out.exists():
            ap.error(f"output exists: {out}")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(make_html(read_words(args.words), args.variant, args.format), encoding="utf-8")
        print(out)
