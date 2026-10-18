# hf-kit spec

hf-kit sits on top of HyperFrames 0.8.77. It holds measured styles, animation blocks, sound
presets and a render check, so a video gets HyperFrames motion and its in-render audio mix
instead of plain ffmpeg cuts. Every technique traces to the measured research in
`research/niches/*.md`, in the "Steal list" tables. New blocks should build what those rows
describe.

## Rules
- **HyperFrames version.** Target 0.8.77: `npx hyperframes@0.8.77 <command>` or a local install
  of that version. `lint`, `check`, `snapshot`, `compositions`, `timeline` and `render` are
  all the kit needs. Nothing in the kit calls the network-backed commands (`add`, `catalog`,
  `capture`, `tts`, `transcribe`, `remove-background`).
- **GSAP.** Load it only from `https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/<file>`, pinned, the
  same as the official examples. Use GSAP plugins only if they're in that CDN path, such as Flip.
- **Reference.** The composition contract lives in the HyperFrames skills: `hyperframes-core`
  (with its references on minimal compositions, sub-compositions, variables and media, data
  attributes and determinism), `hyperframes-animation`, and `hyperframes-audio` for sound. If
  this spec and those docs disagree on HyperFrames syntax, the docs win.
- **Determinism.** No `Math.random` without a seed, no wall-clock time, no network fetches in blocks.
  Visual state is a pure function of timeline time.
- **Code.** No build step and no npm installs. Python tools use the stdlib, numpy and Pillow
  (plus pytesseract for `research/measure.py`). Comments state constraints only.

## Layout
```
SPEC.md                  this file
blocks/<name>.html       sub-compositions (source of truth)
blocks/README.md         catalog: one row per block
examples/<name>/         one demo project per block
sound/MIX.md             mix presets as copyable HyperFrames audio attributes
sound/SFX.md             SFX events, files and levels
sound/gen_sfx.py         renders sound/sfx/*.wav
sound/gen_bed.py         renders sound/beds/*.wav (not committed; generate locally)
styles/<id>.json         measured style targets (schema below)
styles/README.md         niche → style id → blocks, captions, mix
tools/scaffold.py        new project from a style and a block list
tools/captions.py        word timings → caption sub-composition
tools/check.py           rendered MP4 → measured, compared against a style's ranges
tools/bg_source.py       licence gate for YouTube footage or music
research/                the 48-video study behind every number
skills/hf-kit/SKILL.md   the workflow as an agent skill
```

## Block contract
Each block is one sub-composition file: `<template>` transport, root `#root` with
`data-composition-id="<name>"`.

- **Scoping.** The runtime rewrites `#root` and `[data-composition-id]` per instance.
  - Style the block box as plain `#root { }`, or `#root.some-class` for a state, and every
    descendant with a plain selector (`.label { }`). The runtime prefixes the instance scope.
  - Never write the compound `#root[data-composition-id="x"]`. It passes lint and then renders
    the block completely unstyled.
  - In scripts, `document.querySelector('#root')` resolves to this instance's root.

- **Variables.** Declare every tunable on `<html>` with `data-composition-variables`: text, numbers,
  timings in seconds, and colour overrides. Read them once with
  `window.__hyperframes.getVariables()`. Defaults must render a sensible demo.
- **Tokens.** Colours and fonts come from inherited CSS custom properties with fallbacks, so a
  style can theme every block at once:
  - `--hk-bg` `#0b0f14`, `--hk-ink` `#f5f5f0`, `--hk-paper` `#f3efe4`;
  - `--hk-accent` `#ffd23f`, `--hk-positive` `#39ff6a`, `--hk-negative` `#ff4d4d`;
  - `--hk-side-a` `#3be8ff`, `--hk-side-b` `#ff7a3b`;
  - `--hk-font-display` `"Inter", system-ui, sans-serif` at weight 800, and
    `--hk-font-body` `"Inter", system-ui, sans-serif`.

  A colour variable, when set, overrides the token.
- **Aspect ratio.** Size with `%`, `vmin` or container units, so the same block works at 1920×1080
  and 1080×1920. Shorts-only blocks say so in the catalog.
- **Header comment,** at the top of `<template>`, in 4 lines at most: what it does; its source (the
  niche sheet and steal-list row); when it works and when it backfires, from that row; and its
  variables.
- **Timing** comes from the steal-list recipe: its ease, duration and stagger. Keep the numbers.
- **Example.** Each block has a demo project at `examples/<name>/`: `index.html` hosts the block
  through `data-composition-src="compositions/<name>.html"` with sample values, and a copy of the
  block sits in `examples/<name>/compositions/`. It runs 3-8 s at 1920×1080; Shorts blocks run at
  1080×1920. `npx hyperframes lint examples/<name>` must pass, and a snapshot should be checked by
  eye, since lint can't see a blank frame.

## Style JSON schema
```json
{
  "id": "archive-essay",
  "source_niche": "documentary",
  "format": "16:9",
  "measured_from": ["2r5eKpptixo", "GV8KGcFqeLc", "OMbV1rIPhCg"],
  "ranges": {
    "cuts_per_min": {"0-15s": [24, 48], "15-60s": [25, 32], "60-180s": [26, 43], "body": [13, 23], "last_min": [1, 4]},
    "median_shot_s": [1.6, 2.7],
    "text_share": [0.03, 0.23],
    "wpm": [144, 171],
    "first_word_s": [0, 10],
    "lra_lu": [5.9, 7.9],
    "silences_per_min": [0.2, 1.0]
  },
  "master": {"lufs": -14, "true_peak_db": -1},
  "tokens": {"--hk-accent": "#e63946"},
  "captions": "none",
  "blocks": ["doc-highlight", "film-gate", "progress-badge", "chapter-card"],
  "mix": ["silence-at-heaviest-line", "dip-before-clip"]
}
```
- For Shorts, the `cuts_per_min` keys are `0-3s`, `3-15s`, `15-60s` and `60s+`. They match
  `research/measure.py` `segments()`: under 180 s the edges are 0, 3, 15 and 60; otherwise they
  are 0, 15, 60, 180, and the last 60 s.
- Any range may be missing. The tools skip what's missing.

## Tools
Each tool has a `--selftest` that fails if its logic breaks.

- `tools/scaffold.py <dir> --format 16:9|9:16 --duration S [--style id] [--blocks a,b]` writes
  `index.html` (the root, the style's tokens or the defaults, a paused timeline registered),
  a `hyperframes.json` pinned to the v0.8.77 registry, and copies the listed blocks into
  `compositions/`. It refuses to overwrite a non-empty dir.
- `tools/captions.py words.json --variant cards|karaoke|speaker|keyword|punch --format 16:9|9:16 --out <file>`
  reads `[{"text", "start", "end", "speaker"?, "class"?}]` or the word-timestamp JSON that
  `hyperframes transcribe` writes, and outputs a caption sub-composition that follows the block
  contract. The variants come from the steal lists:

  | Variant | Source | Rule |
  |---|---|---|
  | cards | shorts-facts | 2-4 words, about 1 per second, about 78% height, in over 2 frames, no motion |
  | karaoke | shorts-gaming | the active word gets `--hk-side-a` |
  | speaker | shorts-podcast | a colour per speaker, 1-5 words, about 55% height |
  | keyword | cooking | `.kw` and `.money` classes, word pop `scale 0.92→1` over 3 frames |
  | punch | challenge-spectacle | single heavy italic caps with a stroke, `scale 0.6→1` 120 ms, hold 1.2 s |
- `tools/check.py render.mp4 [--style id]` imports `research/measure.py` for cuts by segment,
  median shot, loudness, LRA, silences and the first word where captions exist. It prints a
  table (measure, value, style range, ok/low/high) and a master line against -14 LUFS and
  -1 dBTP. It always exits 0: it's advice.
- `tools/bg_source.py <url> [--download --out assets/ --audio --min-height N]` accepts a YouTube
  source only when yt-dlp reports a Creative Commons licence, and logs every decision to
  `sources/provenance.jsonl`.
