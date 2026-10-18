# SFX event map

Levels are starting points relative to the voice at the same moment, from `../research/knowledge/sound-design.md` §3.4: designed effects usually sit 6-15 dB under speech. Set gain by listening and measurement. Sync points and durations below are that chapter's editing practice, not measured laws. Keep the master at or below -1 dBTP.

| Event | Category and placement | Starting level | Local candidate |
|---|---|---|---|
| Pop-in | Short UI pop, 50-250 ms; onset on first visible frame. | -12 dB under voice | `sound/sfx/pop.wav` |
| Whoosh on transition | Whoosh or swish, 0.3-1.2 s; start 4-10 frames early, peak on cut; high-pass 150-250 Hz. | -12 dB under voice | `sound/sfx/whoosh-short.wav` or `sound/sfx/whoosh-long.wav` |
| Impact on reveal | Transient plus mid thump, 0.2-2 s; transient on reveal frame, tail clear of the next line. | -6 dB under voice, brief peak may meet speech between lines | `sound/sfx/impact-soft.wav` or `sound/sfx/impact-hard.wav` |
| Riser into payoff | Riser, 1-4 s lead, ending exactly on payoff frame; optional impact at end. | Begin -15 dB under voice; keep the payoff transient below master ceiling | `sound/sfx/riser-2s.wav` or `sound/sfx/riser-4s.wav` |
| Tick for counter | UI tick/click, 20-200 ms; one tick per visible count change, vary pitch for repeats. | -15 dB under voice | `sound/sfx/tick.wav` or `sound/sfx/tick-high.wav` (15 ms) |
| Sub drop | Falling low hit, 0.5-2 s tail from payoff frame; include 100-200 Hz harmonic for phone audibility. | -12 dB under voice; check low-end headroom | `sound/sfx/sub-drop.wav` |
| Glitch | Short digital interruption on a screen glitch frame. | -15 dB under voice | `sound/sfx/glitch.wav` |

## Licence

The files in `sound/sfx/` and `sound/beds/` are procedurally generated, with no downloaded samples or models. These generated audio files are released under CC0 (Creative Commons Zero); attribution is optional. Regenerate with `python sound/gen_sfx.py` and `python sound/gen_bed.py`. The beds are not committed, so run `gen_bed.py` once before using the mix presets.

## Render measurements

EBU R128 and true peak measured from the rendered 48 kHz, 24-bit WAVs. Spectral centroid is the magnitude-weighted average of sampled FFT windows (mono sum for beds); it is a brightness proxy, not a listening test.

| File | Duration | Integrated LUFS | True peak dBTP | Centroid Hz |
|---|---:|---:|---:|---:|
| `sound/beds/calm-pad.wav` | 32.000 s | -20.0 | -12.6 | 224 |
| `sound/beds/hype-pulse.wav` | 32.000 s | -20.0 | -6.6 | 101 |
| `sound/beds/kids-bounce.wav` | 32.000 s | -20.0 | -9.2 | 651 |
| `sound/beds/news-tick.wav` | 32.000 s | -20.0 | -6.6 | 5990 |
| `sound/beds/story-noir.wav` | 32.000 s | -20.0 | -11.1 | 186 |
| `sound/beds/tension-drone.wav` | 32.000 s | -20.0 | -11.9 | 107 |
| `sound/beds/wonder-pad.wav` | 32.000 s | -20.0 | -12.3 | 364 |
| `sound/sfx/glitch.wav` | 0.150 s | -70.0* | -2.0 | 5627 |
| `sound/sfx/impact-hard.wav` | 0.800 s | -22.4 | -1.3 | 2378 |
| `sound/sfx/impact-soft.wav` | 0.650 s | -22.8 | -6.1 | 929 |
| `sound/sfx/pop.wav` | 0.060 s | -70.0* | -1.5 | 611 |
| `sound/sfx/riser-2s.wav` | 2.000 s | -17.2 | -2.1 | 2759 |
| `sound/sfx/riser-4s.wav` | 4.000 s | -16.3 | -1.6 | 2814 |
| `sound/sfx/sub-drop.wav` | 1.200 s | -16.0 | -1.5 | 103 |
| `sound/sfx/tick-high.wav` | 0.015 s | -70.0* | -1.5 | 1928 |
| `sound/sfx/tick.wav` | 0.015 s | -70.0* | -1.5 | 1415 |
| `sound/sfx/whoosh-long.wav` | 1.000 s | -13.2 | -1.5 | 2299 |
| `sound/sfx/whoosh-short.wav` | 0.350 s | -70.0* | -1.5 | 2459 |

* The clip is shorter than the EBU R128 integration window or contains too little gated material; `-70.0` is the meter floor, not a usable loudness estimate.
