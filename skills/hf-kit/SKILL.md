---
name: hf-kit
description: HyperFrames layer with 16 measured YouTube styles, 13 animation blocks, sound-mix presets, CC0 SFX and mood beds, a caption generator, a project scaffold, a licence gate for YouTube Creative Commons footage, and a render checker that measures a cut against the reference ranges. Use for a HyperFrames video that should follow a measured style (explainer, documentary, Shorts facts and so on), or when a brief names one. Read after the `hyperframes` skill.
---

# hf-kit

A layer on HyperFrames 0.8.77. Everything in it traces to measured research: 48 YouTube videos
across 16 niches, with the numbers in `research/`. Paths below are relative to the repo root.
Read `SPEC.md` for the contracts, and follow the `hyperframes-core` composition rules.

`hyperframes` below means `npx hyperframes@0.8.77` or a local install of 0.8.77. Python tools
need Python 3.10+ with numpy and Pillow, plus ffmpeg on PATH.

## Workflow
1. **Pick the style.** `styles/README.md` maps niche → style id → blocks, captions and mix
   presets. The style JSON holds the measured ranges (cuts/min by segment, shot length, wpm,
   LRA, silences) and the master target (-14 LUFS, -1 dBTP).
2. **Scaffold.** `python tools/scaffold.py <dir> --format 16:9|9:16 --duration S --style <id> [--blocks a,b]`.
   It writes `index.html` with the style's tokens, pins `hyperframes.json` to the v0.8.77
   registry, and copies the blocks into `compositions/`. It refuses to overwrite a non-empty dir.
3. **Blocks.** Catalog in `blocks/README.md`: pill-label, chapter-card, number-card (clean or
   money), progress-badge, question-card, doc-highlight, film-gate, world-camera, ui-window,
   tier-board, face-banner-stack (with a `topic-top` layout for a rounded 16:9 topic box),
   zoom-through, blur-swap. Each is a sub-composition with `data-composition-variables`; pass
   values with `data-variable-values`. `examples/<block>/` has a working demo of each.
   Style every block with plain `#root` and plain descendant selectors. Never the compound
   `#root[data-composition-id=...]`: it lints clean and renders blank.
4. **Captions.** `python tools/captions.py words.json --variant cards|karaoke|speaker|keyword|punch --format 9:16 --out compositions/captions.html`.
   Input is `[{text,start,end,speaker?,class?}]` or `hyperframes transcribe` JSON.
5. **Sound.** `sound/MIX.md` has 10 copyable `hyperframes-audio` presets (voice-first flat,
   pause at the turn, silence at the heaviest line, dip before a clip, and so on), each naming
   its source row. `sound/sfx/` has 11 generated effects and `sound/SFX.md` maps events to
   files and levels. The 7 mood beds are not committed: `python sound/gen_bed.py` renders all of
   them into `sound/beds/` at -20 LUFS, and `python sound/gen_bed.py --mood <name> --seconds N --out bed.wav`
   renders any length. Both generators are deterministic and the output is CC0.
6. **Background footage or music from YouTube.** `python tools/bg_source.py <url> [--download --out assets/ --audio]`.
   - ACCEPT (exit 0) only when yt-dlp reports a Creative Commons licence. It prints a credit
     line for the description. Video downloads need at least `--min-height` (default 1080);
     `--audio` has no height floor.
   - REVIEW (exit 3) when a standard-licence upload claims reuse in its title or description.
     A "no copyright" title is the uploader's word. Check that the uploader is the original
     creator and keep a screenshot of the terms.
   - REFUSE (exit 2) otherwise.

   Every decision is appended to `sources/provenance.jsonl` (`--log` to change it). Content ID
   can still claim a Creative Commons re-upload of someone else's work, so prefer the original
   channel. Keep downloads in the project's `assets/`, never in a public repo.
7. **Check before render.** `hyperframes lint <dir>` and `hyperframes check <dir>`; then
   `hyperframes snapshot <dir> --frames 6` and look at the contact sheet. Lint passing is not a
   visual pass.
8. **Render and measure.** `hyperframes render <dir> --output out.mp4`, then
   `python tools/check.py out.mp4 --style <id>`. It prints each measure against the style's
   range plus the master loudness line. It's advice: a miss says the cut drifted from the
   reference, and your own analytics decide whether that matters.

## What the research says (short version)
- Across all 16 niches, cut rate and loudness did not separate outliers from their controls. A
  person at stake, the stake stated in the first seconds, proof on screen, and a held answer did
  (hypotheses; see `research/TECHNIQUES.md`, "What didn't separate outliers from controls").
- Hard-cut counts are floors. Tempo is unreliable under narration. The audio was not listened
  to: the sound findings come from R128 numbers, spectra and caption tags.

## Where things are
| Need | Path |
|---|---|
| Contracts and rules | `SPEC.md` |
| Styles and their measured ranges | `styles/README.md`, `styles/<id>.json` |
| Block catalog and demos | `blocks/README.md`, `examples/<block>/` |
| Mix presets and the SFX map | `sound/MIX.md`, `sound/SFX.md` |
| Technique library, mood table | `research/TECHNIQUES.md` |
| Niche DNA sheets with steal lists | `research/niches/<niche>.md` |
| One card and one data file per video | `research/cards/<niche>/<id>.md`, `research/data/<id>.json` |
| Knowledge chapters (music and mood, sound design, VFX and motion) | `research/knowledge/` |
