# HyperFrames mix presets

The bed examples use the generated 32-second loops (`python sound/gen_bed.py` writes them to `sound/beds/`). For longer clips, repeat a loop or render the needed length with `python sound/gen_bed.py --mood calm-pad --seconds 60 --out sound/beds/calm-pad-60s.wav`. Replace the sample durations and event times. Automation `t` is seconds from that audio clip's `data-start`, and `v` is the absolute track gain, not a multiplier on `data-volume`. Keep each clip's `id` unique. The examples use the 0.8.77 `data-automation` object with a `version`, `lanes`, and `points`; an audio element needs its own `id`. Music under speech also needs a measured voice carve before a final render; volume settings here are starting recipes, and `-14 LUFS / -1 dBTP` is checked on the rendered mix.

## Voice-first flat mix

Source: `animated-explainer.md`, "Voice-first flat mix": VO `1`, bed `0.15` (about 16 dB lower); target LRA at most 3 LU. Use for dense narration.

```html
<audio id="voice" src="assets/voice.wav" data-start="0" data-duration="60" data-track-index="10" data-volume="1" data-fx-chain="{&quot;version&quot;:1,&quot;nodes&quot;:[{&quot;type&quot;:&quot;compressor&quot;,&quot;id&quot;:&quot;voice-compressor&quot;,&quot;label&quot;:&quot;Dense narration&quot;,&quot;params&quot;:{&quot;threshold&quot;:-24,&quot;ratio&quot;:4,&quot;attack&quot;:20,&quot;release&quot;:250,&quot;knee&quot;:2.83,&quot;makeup&quot;:0,&quot;mix&quot;:1}}]}"></audio>
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="60" data-track-index="11" data-volume="0.15"></audio>
```

## One pause at the turn

Source: `animated-explainer.md`, "One pause at the turn": one 0.4-0.74 s turn. Example pivot `T=20`; points are `T-0.3`, `T`, `T+0.7`, `T+1`.

```html
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="40" data-track-index="11" data-volume="0.15" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0.15},{&quot;t&quot;:19.7,&quot;v&quot;:0.15},{&quot;t&quot;:20,&quot;v&quot;:0.03},{&quot;t&quot;:20.7,&quot;v&quot;:0.03},{&quot;t&quot;:21,&quot;v&quot;:0.15}]}]}"></audio>
```

## Silence at the heaviest line

Source: `documentary.md`, "Silence at the heaviest line": one 0.4-1.5 s silence at a painful fact or thesis, about 0.7-1.0 per minute. Example line at 20 s; bring music back on the next section's first downbeat at 21.2 s.

```html
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="40" data-track-index="11" data-volume="0.15" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0.15},{&quot;t&quot;:19.5,&quot;v&quot;:0.15},{&quot;t&quot;:20,&quot;v&quot;:0},{&quot;t&quot;:21.2,&quot;v&quot;:0},{&quot;t&quot;:21.3,&quot;v&quot;:0.15}]}]}"></audio>
```

## Dip before a loud clip

Source: `documentary.md`, "Dip before a loud archive clip": take the bed near zero 0.5-1 s before the archive starts; let the archive play at full level. Example archive at 20 s.

```html
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="30" data-track-index="11" data-volume="0.15" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0.15},{&quot;t&quot;:19,&quot;v&quot;:0.15},{&quot;t&quot;:19.5,&quot;v&quot;:0.0075},{&quot;t&quot;:28,&quot;v&quot;:0.0075},{&quot;t&quot;:29,&quot;v&quot;:0.15}]}]}"></audio>
<audio id="archive" src="assets/archive.wav" data-start="20" data-duration="8" data-track-index="12" data-volume="1"></audio>
```

## Long fade under the end card

Source: `animated-explainer.md`, "Long fade under the end card": 14-16 s fade, about 31 LU in the measured videos. Example end card starts at 46 s in a 60 s piece.

```html
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="60" data-track-index="11" data-volume="0.15" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0.15},{&quot;t&quot;:46,&quot;v&quot;:0.15},{&quot;t&quot;:60,&quot;v&quot;:0}]}]}"></audio>
```

## Exhale tail

Source: `calm-faith.md`, "Exhale tail": 26-35 s of music alone, 6.8-10.4 LU under the body; end with 0.7-6.1 s silence. Use only on a long end screen. The sample music should be prepared to sit near -24 to -27 LUFS short term; the attribute alone cannot ensure that measurement.

```html
<audio id="outro-music" src="sound/beds/calm-pad.wav" data-start="60" data-duration="30" data-track-index="11" data-volume="0.15" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0},{&quot;t&quot;:1,&quot;v&quot;:0.15},{&quot;t&quot;:28,&quot;v&quot;:0.15},{&quot;t&quot;:29.3,&quot;v&quot;:0}]}]}"></audio>
```

## Gapless loud bed

Source: `shorts-facts.md`, "Gapless loud bed": bed throughout the Short, 18-22 LU under VO, 0 silences, LRA 2.0-2.3 LU. Render, then measure against about -14 LUFS and -1 dBTP; gain on the source determines the actual result.

```html
<audio id="voice" src="assets/voice.wav" data-start="0" data-duration="30" data-track-index="10" data-volume="1"></audio>
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="30" data-track-index="11" data-volume="0.1"></audio>
```

## Tension bed for one section

Source: `challenge-spectacle.md`, "Score the tension scene differently": one interrogation, vote, or reveal about 3 LU quieter. Example section 20-28 s; use a dark drone source only in that window.

```html
<audio id="tension" src="sound/beds/tension-drone.wav" data-start="20" data-duration="8" data-track-index="11" data-volume="0.708"></audio>
```

## Payoff montage lift

Source: `science-entertainment.md`, "Payoff montage: fewer cuts, louder music": 4-8 s music-only montage, about +4 LU, on bar lines, VO off. Here the lift is a 4 dB gain ratio (`1.585`) on a clip that has no simultaneous VO.

```html
<audio id="payoff-music" src="sound/beds/hype-pulse.wav" data-start="30" data-duration="6" data-track-index="11" data-volume="1.585"></audio>
```

## Thin bed lifted in pauses

Source: `animated-storytime.md`, "Voice-first thin bed": bed `0.08`, lifted to `0.25` (about +10 dB) over 0.8 s only where VO pauses. The sheet wrote the lift as `v:1`; absolute gain 1 would be about +22 dB, too loud against the next line. The example VO pause begins at 20 s and speech resumes at 22 s. High-pass keeps low mids free for the voice.

```html
<audio id="music" src="sound/beds/calm-pad.wav" data-start="0" data-duration="40" data-track-index="11" data-volume="0.08" data-fx-chain="{&quot;version&quot;:1,&quot;nodes&quot;:[{&quot;type&quot;:&quot;highpass&quot;,&quot;id&quot;:&quot;bed-highpass&quot;,&quot;label&quot;:&quot;Voice room&quot;,&quot;params&quot;:{&quot;frequency&quot;:150,&quot;q&quot;:0.707,&quot;poles&quot;:&quot;2&quot;}}]}" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0.08},{&quot;t&quot;:20,&quot;v&quot;:0.08},{&quot;t&quot;:20.8,&quot;v&quot;:0.25},{&quot;t&quot;:21.2,&quot;v&quot;:0.25},{&quot;t&quot;:22,&quot;v&quot;:0.08}]}]}"></audio>
```
