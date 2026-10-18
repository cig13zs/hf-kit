# Research brief: how the most-watched videos are edited, and why

The brief this folder's research was run against, written 2026-09-26. The ask: study YouTube
videos with millions of views across many niches. Analyse the audio, animation, VFX, editing
style, cuts per minute, the idea and the retention, and explain why they were edited that way,
so a video skill can reuse it.

## The question

For each kind of video, what editing decisions do the biggest videos share, what job
does each decision do for the viewer, and how do we reproduce it with our own assets in
HyperFrames?

"Millions of views" alone doesn't answer that. A creator with 30M subscribers gets
millions of views on an average upload, so their typical video reveals the
channel, not the edit. The brief therefore studies **outliers**: videos that beat their own
channel's typical views by a wide margin. It sets them against a typical upload from the same
channel where it can. Whatever the outlier does that the typical upload doesn't is a
candidate cause. Whatever both do is the house style.

## Sample

About 45 videos across 15 niches, 3 per niche. Each niche covers one long-form outlier, one
recent outlier (last 18 months), and one typical upload from the same channel as a control.
Shorts niches use 3 outliers from different creators instead, because Shorts views are too
noisy for a same-channel control.

| # | Niche | Format | Why it's in |
|---|---|---|---|
| 1 | Documentary / video essay | Long | Pacing across 20+ minutes, archival and map graphics |
| 2 | Animated explainer | Long | Motion-graphics grammar, the HyperFrames sweet spot |
| 3 | Science / engineering entertainment | Long | Story built around a build or test, payoff structure |
| 4 | Challenge / spectacle entertainment | Long | The most-studied retention machine on the platform |
| 5 | Tech review | Long | Clean product b-roll, typography, restraint |
| 6 | Tutorial / screen recording | Long | Keeping attention without a face or a story |
| 7 | Gaming story / commentary | Long | Gameplay as footage, narration over it |
| 8 | True crime / storytelling | Long | Tension, music, restraint, slow reveals |
| 9 | Cooking / food | Long | Process shots, sound design, speed ramps |
| 10 | Kids animation / education | Long | Pacing for young viewers, repetition, color |
| 11 | Calm / faith / ambient | Long | What slow, low-cut editing looks like when it works |
| 12 | Fast facts / edutainment | Shorts | Hook density, captions, zooms |
| 13 | Gaming clips | Shorts | Readable action, HUD, sound hits |
| 14 | Podcast / talking-head clips | Shorts | Captions, punch-ins, reframing |
| 15 | Aesthetic / VFX / visual-trick edits | Shorts | The Pinterest-style look: transitions, masks, speed ramps, beat sync |

Selection rules:
- Pull candidates live with yt-dlp: the channel's uploads with view counts, or a search. Never
  pick from memory without checking views that day.
- Outlier ratio = video views ÷ the channel's median views over its last 30 uploads. Record the ratio.
- Mix creators. There is at most one creator per niche, and a creator never appears in more
  than two niches.
- Skip music videos, trailers, compilations of other people's clips, and anything whose views
  obviously come from something other than the video, such as a news event or a celebrity.
  Note any such skip.

## What to measure (numbers, by script)

`research/measure.py` produces these for every video. They are measured, not guessed.

- Metadata: title, channel, upload date, duration, views, likes and comments on the check date,
  channel subscribers, outlier ratio.
- Cuts: every hard cut with its timestamp, from ffmpeg scene scores.
  - Cuts per minute overall and per segment: 0-15s, 15-60s, 1-3 min, 3 min to the last minute,
    and the last minute.
  - Average and median shot length, and the shot-length spread.
  - Limit: dissolves, whip-pans and fast camera moves blur the count, so call it a floor on
    hard cuts, not a truth.
- Visual energy: the mean frame-to-frame change per minute. This separates a calm locked-off
  talking head from constant motion even when neither has many cuts.
- On-screen text: OCR on sampled frames gives the share of frames with text, and words on
  screen per minute.
- Speech: words per minute from YouTube captions, overall and in the first 30 seconds.
  Also the time until the first spoken word.
- Audio:
  - integrated loudness (LUFS) and loudness range;
  - the loudness curve, one value every 2 seconds;
  - silences over 0.4s and their count per minute;
  - audio onsets per minute (a proxy for sound-design density: hits, whooshes, risers).
- Frames for review: a contact sheet of the first 30 seconds at 2 frames per second, a sheet
  of the whole video at even spacing, and a frame just before and just after 12 sampled cuts.

## What to analyze (judgment, from the frames and transcript)

Each video gets one card. Every claim is marked **seen** (in frames, transcript or numbers)
or **inferred**.

1. **Idea and promise.** What does the title and thumbnail promise, and at what second does the
   video first deliver on it? What is the core curiosity gap?
2. **Hook (first 15-30s).** Which lines and images, in order. The hook type, for example a
   question, stakes, a demonstration, an in-medias-res start, or a payoff shown first. How fast
   does it reach the first new piece of information?
3. **Structure.** Chapters or beats with timestamps, where the escalation happens, and
   re-hooks: open loops, "but then", teasers of what's coming, callbacks. How the ending pays off.
4. **Editing style.** Cut rhythm and where it changes, jump cuts versus b-roll cuts, punch-ins,
   J/L cuts (visible from caption timing against cuts), and how a cut lines up with the speech
   (on the word, on the beat, or after the line).
5. **Graphics and animation.** Typography (family class, weight, case, size, where on screen),
   the colour system, lower thirds, maps, diagrams, charts, 3D, kinetic text, masks, parallax,
   and camera moves on stills.
6. **VFX and transitions.** Named precisely: whip pan, match cut, speed ramp, zoom
   transition, glitch, light leak, screen shake, green-screen composite, mask reveal, morph.
   Say how often each one appears. It matters more that a transition is rare than that it
   exists.
7. **Sound.** From the numbers and the transcript only; the audio is not listened to. When music
   drops out, silences used as punctuation, sound-hit density, the loudness pattern, and speech pace.
   Mark every audio claim "measured" or "inferred from transcript". Never write "the music
   swells" unless the loudness curve shows it.
8. **Retention mechanics: the why.** For each notable decision, the job it does for the viewer:
   - clarifying;
   - resetting attention;
   - building tension;
   - delivering proof;
   - showing a payoff;
   - setting the rhythm;
   - building identity or brand.

   Tie it to a moment. Pacing is a choice for the audience and the content, not a virtue in
   itself. Say what the fast videos and the slow videos each know.
9. **Outlier against control.** What the outlier does that the same channel's typical video
   doesn't (for Shorts, what the three outliers share). Label every causal claim a hypothesis.
10. **Steal list.** Three to five techniques worth reusing, each with its measured range (such as
    "punch-in every 4-7s during talking"), when it works, when it backfires, and a one-line
    HyperFrames recipe sketch.

## Synthesis

- **Per niche:** a DNA sheet with the typical ranges (cuts per minute by segment, shot length,
  text density, words per minute, loudness), the shared devices, and the differences between
  outliers and controls.
- **Across niches:** a technique library. Each technique gets its name, what it is, where it
  was seen (video and timestamp), the measured range, the viewer job it does, which niches
  use it and which avoid it, the failure mode, and the HyperFrames recipe. This library is
  the raw material for the video skill.

## Honesty rules

- Views don't prove the editing caused them. Outlier-versus-control is the best available
  evidence, and every conclusion drawn from it is a hypothesis.
- The audio is not listened to. Audio claims come from measurements and captions only, and are
  labelled so.
- Hard-cut counts are floors. Say so wherever a number is quoted.
- Never invent a view count, a timestamp or a quote. Anything not checked gets marked.

## Rights and storage

- Downloads are low resolution (360p; the first few ran at 480p), stored in `research/_local/` (never committed),
  and deleted as soon as a video's measurements and frames exist. Contact sheets stay local
  only, as working evidence.
- The public repo never gets another creator's frames, footage, audio or full transcript.
  It may cite the video by title, link and timestamp, and quote up to 15 words.
- Recreations in the skill use original assets.

## Deliverables

- `research/data/<video-id>.json`: the measurements.
- `research/cards/<niche>/<video-id>.md`: one card per video.
- `research/niches/<niche>.md`: one DNA sheet per niche.
- `research/TECHNIQUES.md`: the cross-niche technique library.
- `research/SAMPLE.md`: every video considered, picked or skipped, with views, outlier ratio
  and the check date.

## Scope add-on (2026-09-26)

Sound, music and VFX get the same depth as the editing, with attention to what works for a
given mood.

1. **Sound and music get equal weight with editing.** This covers mood-to-music parameters,
   the SFX vocabulary and placement, mixing and loudness, silence as a device, niche
   conventions, and game audio (feedback, juice, adaptive music, Roblox specifics).
   Knowledge chapters: `knowledge/music-and-mood.md`, `knowledge/sound-design.md`.
2. **VFX, motion and colour** are mapped to mood and genre, with HyperFrames build recipes.
   Knowledge chapter: `knowledge/vfx-and-motion.md`.
3. **Music is measured per video** by `audio_features.py`:
   - **Tempo.** Unreliable under constant narration, so label it.
   - **Whether cuts land on audio onsets more than chance.** This is a lift over random
     cut times.
   - **Brightness and bass share every 10 seconds.**
   - **Caption [music] tags.**
   - **The 2-second loudness curve.**

   The audio is not listened to. Mood claims come from these numbers plus the sourced
   chapters, and are labelled.
4. **Existing editing and sound skills** are read for ideas only. Their code and media are not
   copied, and every borrowed idea is credited in `TECHNIQUES.md` section 13.
