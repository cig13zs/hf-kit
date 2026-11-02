# Contributing

Thanks for taking a look. Bug reports, new blocks, style fixes and better measurements are all welcome.

## Getting set up

Follow the Install section in the README. You need Python 3.10+, Node (for HyperFrames 0.8.77), and ffmpeg/ffprobe on your PATH.

## Before you open a PR

Run the selftest for anything you touched:

```sh
python tools/scaffold.py --selftest
python tools/captions.py --selftest
python tools/bg_source.py --selftest
python tools/check.py --selftest
python sound/gen_sfx.py --selftest
python sound/gen_bed.py --selftest
```

If you change `sound/gen_sfx.py`, the files in `sound/sfx/` still have to match. CI checks that. Beds are generated when you need them and are not in the repo.

Keep PRs small and about one thing. A short note on why helps more than a long one on what.

## Research changes

If you add or re-measure a video, put the link and the date you read the views in `research/`. Don't commit frames, audio or transcripts from other people's videos.

## Not sure where to start?

Look for issues tagged `good first issue`, or open one and ask. Happy to help.
