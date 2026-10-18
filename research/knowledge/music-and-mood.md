# Music and Mood for Video

Reference chapter for a video-making agent that cannot hear audio. It turns a mood
or genre into searchable, checkable music parameters, then says where to place the
track, how to cut to it, and how to mix it under a voice.

Version: v2, 2026-09-26. Gaps are listed at the end.

## How to read the tags

- `[S#]` points to the source list at the bottom (URL + date checked).
- `[P]` = practice (inferred): common editing or scoring practice that this chapter
  did not verify against a published source. A strong default, not a rule.
- `[D]` = derived: arithmetic from stated inputs (BPM math).
- `[M]` = measured by this project (a card under `research/cards/`).

---

## 0. Agent workflow in one screen

1. Tag each script section with a mood from the Section 1 table. Most videos need
   1 to 4 moods, not one per scene. `[P]`
2. Read the genre block (Section 5): music role (bed, featured, absent), energy,
   how often the track changes.
3. Build the library query: 2-3 mood tags in that library's vocabulary (Section 2.2)
   + BPM range + instrumental + minimum duration.
4. Vet candidates without listening `[P]`:
   - library metadata: BPM, key, mood tags, vocals flag, stems available;
   - a loudness-over-time trace (for example ffmpeg's `ebur128` filter) to find
     intro, builds, drops, breakdowns and the ending;
   - a beat tracker (for example librosa) for the bar grid and first downbeat.
5. Place: section starts on script turns, cuts on bar lines, risers/stingers or
   silence at reveals (Section 3).
6. Mix: duck under voice, carve the consonant band, hit the platform target (Section 4).
7. Run the failure-mode checks (Section 6) before export.

---

## 1. Mood to music parameters

### 1.1 What the research says

| Finding | Use it as | Source |
|---|---|---|
| Arousal tracks tempo, pitch height, loudness and timbre brightness; valence tracks mode (major/minor) and consonance. | Set energy with tempo, density, loudness, brightness; set positive/negative with mode and harmony. | `[S1]` `[S2]` |
| When six cues were varied independently, importance ranked mode > tempo > register > dynamics > articulation > timbre. Effects were mostly linear and additive; the study found no significant cue interactions across 84 comparisons. | Mode and tempo are the first filters. Cues stack, so fixing one wrong cue helps without breaking the others. | `[S3]` |
| Cue settings from that study: happy = major, fast, high register, staccato. Sad = minor, slow, low register, legato. Scary = low register, minor, loud. Peaceful = high register, slow, soft, legato. | Starting points for rows in 1.2. | `[S3]` |
| Across 104 speech and 41 music-performance studies, the same cue profiles signal the same emotions in voice and music. Anger: fast, loud, bright, fast attacks. Fear: fast, usually soft, high pitch, irregular timing. Happiness: fast, medium-high level, high pitch, fast attacks. Sadness: slow, soft, dull, low pitch, slow attacks. Tenderness: slow, soft, dull, slow attacks, regular timing. | The music's emotional "voice" should match the narrator's delivery, or they conflict. | `[S4]` |
| Music induces emotion through six mechanisms: brain-stem reflex, evaluative conditioning, emotional contagion, visual imagery, episodic memory, musical expectancy. | Stingers exploit the reflex (sudden loud onsets). Nostalgia cues exploit memory. Builds and held-back resolutions exploit expectancy. | `[S5]` |
| Viewers shown ambiguous film clips with positive, negative or no music interpreted endings and characters differently, and remembered different objects, depending on the music. | Music tells the viewer how to read an ambiguous shot. A wrong-mood track changes the meaning, not just the feel. | `[S6]` (design confirmed; result from the published abstract) |

Decision rules:
- Set arousal first (tempo, density, loudness, brightness), then valence (mode,
  harmony). Reject a track whose valence is wrong even if its tempo fits; tempo can be
  hidden by editing, mode cannot. `[P]` (ordering follows the cue weights in `[S3]`)
- Match the narrator. A soft, slow read over a fast, bright track sends two emotions
  at once `[S4]`.

### 1.2 Parameter table

BPM ranges are search defaults, not laws. Direction of each cue follows `[S1]`-`[S4]`;
the specific numbers, instruments and progressions are `[P]`. Half-time drums (felt
pulse at half the listed BPM) are common in epic, hype and trailer music. `[P]`

| Mood | BPM | Mode / harmony | Instruments / timbre | Rhythm density | Dynamics / energy curve | Register / brightness |
|---|---|---|---|---|---|---|
| Tension / suspense | 70-110 pulse, or no clear pulse | Minor, pedal tones, unresolved chords, chromatic lines | Low string ostinato, pulsing synth bass, ticking percussion, sul ponticello strings | Medium: steady 8th/16th ostinato | Slow continuous build; no release until the payoff | Low bed + one high sustained note; darkish |
| Mystery | 70-100 | Minor or modal (Dorian, Phrygian), whole-tone colour, open cadences | Pizzicato, celesta, muted piano, harp, soft pads | Sparse, "questioning" phrases | Low-medium, flat; phrases end unresolved | Mid; soft highs |
| Dread / horror | 40-70 or ametric | Atonal clusters, minor 2nds, tritones, drones | Sub drones, bowed metal, reversed sounds, breath textures | Very sparse, irregular | Very quiet bed, sudden loud stings | Extremes (sub + shrill); dark overall |
| Wonder / awe | 60-90, slow harmonic rhythm | Major or Lydian, suspended chords | Choir pads, strings, celesta, piano arpeggios, shimmer synths, long reverb | Low-medium, arpeggiated | Slow swell to one wide climax | Very wide register; bright top |
| Triumph / epic | 80-140 (drums often half-time) | Major, or minor resolving to major; strong root motion | Brass, full orchestra, taiko and toms, choir | High drums under long melody notes | Build, loud peak, hold, resolve | Full range; bright brass |
| Uplifting / inspiring | 100-130 | Major, common pop progressions, sus chords | Piano, acoustic guitar, strings, claps, four-on-floor kick later | Medium, grows each section | Stepwise build every 8-16 bars | Mid-high; bright |
| Playful / quirky | 100-140 | Major with chromatic passing notes | Pizzicato, ukulele, glockenspiel, marimba, bassoon, whistling | Bouncy staccato, syncopation | Moderate, stop-start | Mid-high; bright |
| Comedic | Any; follows the joke | Major; deliberate "wrong" notes | Tuba, bassoon, slide whistle, kazoo, comic stingers | Hits sync to action | Punctuation, not bed: short cues and hard stops | Mid; bright |
| Cozy / calm | 60-90 | Major 7th/9th chords (lo-fi, jazz) | Rhodes, soft keys, acoustic guitar, brushed drums, vinyl crackle | Low, laid-back swing | Flat, low, no big peaks | Mid; warm, highs rolled off |
| Melancholy / sad | 50-80 | Minor, or major with borrowed minor iv; descending bass | Solo piano, cello, strings, pads | Sparse, legato | Soft; small swells | Mid-low; dull |
| Nostalgic | 70-100 | Major with borrowed chords, maj7 | Rhodes, tape-wobbled synths, music box, acoustic guitar | Medium-low | Soft, steady | Warm, low-passed |
| Romantic | 60-90 | Major 7ths/9ths, lush voicings | Strings, piano, acoustic guitar, soft solo line | Low, legato | Gentle swells | Mid; warm |
| Urgent / news | 110-130 | Minor or modal ostinato, little resolution | Synth pulses, staccato strings, ticking hats, timpani and impacts | High, 16ths | Constant high, stabs at section turns | Mid-high; hard attacks |
| Confident / tech product | 100-125 | Major or bright minor over a steady groove | Clean synths, plucks, muted guitar, tight drums, sub bass | Medium-high, quantized | Steady, builds to logo or reveal | Bright, clean, wide |
| Hype / energetic | 120-160 (trap/phonk often half-time) | Often minor, short loops | 808 bass, heavy kick, synth leads, risers, drops | High | Builds and drops; loudest material | Full range; bright |
| Childlike | 90-130 | Simple diatonic major, I-IV-V | Glockenspiel, xylophone, ukulele, toy piano, claps, whistling | Medium, bouncy | Steady, cheerful | High; bright |
| Sacred / reverent | 50-80 or free time | Major or modal, plagal (IV-I) motion, open fifths, sustained chords | Choir, organ, strings, soft piano, pads, long reverb | Very low, sustained | Slow swells, no hits | Wide; soft top |

### 1.3 Script signal to default mood `[P]`

| Script signal | Default mood | Why |
|---|---|---|
| A question the video answers later | Mystery | Keeps expectancy open `[S5]` |
| A number, stake, deadline or threat | Tension | Builds anticipation |
| A result, record, finished build | Triumph or uplifting | Resolution after tension |
| Real loss, harm, apology | Melancholy at low level, or no music | Avoid telling viewers how to feel |
| Tutorial step or process | Cozy/calm or confident | Low attention cost under voice |
| Joke or absurd visual | Comedic stinger, then back to the bed | Punctuation, not a new bed |

---

## 2. How music libraries tag mood and genre

### 2.1 Library comparison (all checked 2026-09-26)

| Library | Search facets | Licence for YouTube | Content ID behaviour | Gotchas for an agent |
|---|---|---|---|---|
| YouTube Audio Library | Track title, genre, mood, artist, attribution, duration `[S7]`. Mood values reported as angry, bright, calm, dark, dramatic, funky, happy, inspirational, romantic, sad `[S8]` | Standard licence: no credit. Creative Commons tracks: credit the artist in the description. Filter "attribution not required" to skip that step `[S7]` | Audio Library downloads "won't be claimed" through Content ID; monetizable in YPP `[S7]` | Only inside YouTube Studio. Only 10 coarse moods. Tracks are widely reused `[P]` |
| Epidemic Sound | 34 moods (below) `[S9]`; genres and themes (Vlogs, Travel, Corporate, Sports) `[S9]` | Subscription; connect the channel or link the video URL to the licence `[S10]` | Videos published during an active subscription on a connected channel stay cleared; videos published after it ends are not `[S10]` | Connect the channel before publishing. Never publish new videos with the library after the subscription lapses `[S10]` |
| Artlist | Mood, tempo, genre, instrument, sound-alikes; "Song Match" suggests 20 similar tracks from a Spotify or YouTube reference `[S11]` | Subscription licence | Claims can appear even when licensed; dispute, then add channel or video to the Clearlist; release can take up to 24 h `[S12]` | Cannot be cleared if downloaded without an active subscription or used outside licence scope `[S12]` |
| Pixabay Music | Genre and tag pages; moods seen include bright, catchy, cheerful (full facet list not visible to the fetcher) `[S13]` | Free, no attribution required, no standalone resale `[S14]` | Some contributors register tracks with Content ID. Dispute with the per-track licence certificate text; processing can take up to 30 days `[S15]` | Save the certificate .txt beside every download `[S15]` |

Epidemic Sound mood list `[S9]`: Happy, Dreamy, Epic, Laid Back, Euphoric, Quirky,
Suspense, Running, Relaxing, Mysterious, Sentimental, Sad, Angry, Busy & Frantic,
Changing Tempo, Chasing, Dark, Eccentric, Elegant, Fear, Floating, Funny, Glamorous,
Heavy & Ponderous, Hopeful, Marching, Peaceful, Restless, Romantic, Scary, Sexy,
Smooth, Sneaking, Weird.

### 2.2 Mood to library vocabulary `[P]`

| Chapter mood | YouTube Audio Library mood | Epidemic Sound moods | Free-text query (Artlist, Pixabay) |
|---|---|---|---|
| Tension / suspense | Dark, Dramatic | Suspense, Sneaking, Restless | suspense tension thriller |
| Mystery | Dark, Calm | Mysterious, Sneaking, Floating | mysterious curious investigation |
| Dread / horror | Dark | Scary, Fear, Dark | horror eerie drone |
| Wonder / awe | Inspirational, Calm | Dreamy, Floating, Epic | wonder magical ambient cinematic |
| Triumph / epic | Dramatic, Inspirational | Epic, Marching, Euphoric | epic heroic trailer orchestral |
| Uplifting / inspiring | Inspirational, Happy, Bright | Hopeful, Happy, Euphoric | uplifting inspiring hopeful |
| Playful / quirky | Happy, Funky, Bright | Quirky, Eccentric, Funny | quirky playful whimsical |
| Comedic | Funky, Happy | Funny, Quirky, Weird | comedy funny cartoon |
| Cozy / calm | Calm | Laid Back, Relaxing, Peaceful, Smooth | lo-fi chill calm acoustic |
| Melancholy / sad | Sad | Sad, Sentimental | sad piano emotional |
| Nostalgic | Calm, Sad, Romantic | Sentimental, Dreamy | nostalgic retro warm |
| Romantic | Romantic | Romantic, Sentimental, Elegant | romantic love tender |
| Urgent / news | Dramatic, Dark | Busy & Frantic, Restless, Chasing | news urgent pulse |
| Confident / tech | Bright, Funky | Smooth, Running, Elegant (+ theme Corporate) | corporate tech modern minimal |
| Hype / energetic | Bright, Angry, Funky | Euphoric, Running, Chasing, Angry | energetic hype phonk sport |
| Childlike | Happy, Bright | Happy, Quirky, Funny | kids cartoon ukulele glockenspiel |
| Sacred / reverent | Calm, Inspirational | Peaceful, Floating, Hopeful | worship ambient choir |

### 2.3 Query recipe `[P]` unless cited

1. 2-3 mood tags from 2.2, in the library's own words.
2. BPM range from 1.2. Without a BPM filter, add a genre that implies it
   (lo-fi = slow; house/EDM = about 120-128).
3. Instrumental only for anything under narration: sung words compete with spoken ones.
4. Duration at least the section length, or plan a loop edit (3.9).
5. Prefer tracks with stems, so the melody can be dropped under dense narration.
6. Skip page one of "popular" or "trending" for bed music (Section 6).
7. Record per track: library, track ID/URL, download date, licence type, and
   (Pixabay) the certificate text. This is what clears a claim later `[S10]` `[S12]` `[S15]`.

---

## 3. Editing to music

### 3.1 Beat math `[D]`

- Seconds per beat = 60 / BPM. Seconds per 4/4 bar = 240 / BPM.
- Frames per beat = fps x 60 / BPM. Frames per bar = fps x 240 / BPM.
- Cut every N bars: interval = N x 240 / BPM seconds.

| BPM | Beat (s) | 1 bar (s) | 2 bars (s) | 4 bars (s) | 1 bar @24 fps | 1 bar @30 fps | 1 bar @60 fps |
|---|---|---|---|---|---|---|---|
| 60 | 1.000 | 4.000 | 8.000 | 16.000 | 96 | 120 | 240 |
| 80 | 0.750 | 3.000 | 6.000 | 12.000 | 72 | 90 | 180 |
| 90 | 0.667 | 2.667 | 5.333 | 10.667 | 64 | 80 | 160 |
| 100 | 0.600 | 2.400 | 4.800 | 9.600 | 57.6 | 72 | 144 |
| 110 | 0.545 | 2.182 | 4.364 | 8.727 | 52.4 | 65.5 | 130.9 |
| 120 | 0.500 | 2.000 | 4.000 | 8.000 | 48 | 60 | 120 |
| 128 | 0.469 | 1.875 | 3.750 | 7.500 | 45 | 56.25 | 112.5 |
| 140 | 0.429 | 1.714 | 3.429 | 6.857 | 41.1 | 51.4 | 102.9 |
| 150 | 0.400 | 1.600 | 3.200 | 6.400 | 38.4 | 48 | 96 |

Worked example: 128 BPM, 30 fps, cut every 2 bars = 3.75 s = 112.5 frames. Place cut k
at round(first_downbeat_s x 30 + k x 112.5). Rounding each cut from its absolute
time keeps error under half a frame; adding a rounded 112 or 113 each time drifts. `[D]`

Pace by genre `[P]`:

| Content | Cut interval |
|---|---|
| Hype Shorts, VFX/transition edits | every beat to every bar |
| Fast-facts and gaming Shorts | every 1-2 beats under speech, bar for b-roll |
| Explainer b-roll, montage | every 1-2 bars |
| Documentary, calm, faith | every 2-4 bars or free (cut on speech) |

Take the grid from the track, not the nominal BPM: many tracks have a pickup or
silence before the first downbeat. `[P]`

### 3.2 On the beat vs off the beat `[P]`

| Cut placement | Effect | Use for |
|---|---|---|
| On beat 1 of a bar | Strongest, "locked" | Section starts, reveals, montage hits |
| Every beat, or on 2 and 4 | Driving | Hype, Shorts, montages |
| 1-2 frames before the beat | Reads as on time: the new shot registers as the beat lands | Most music-led cuts |
| Off the beat, free | Invisible; edit follows speech | Talking head, documentary, tutorials |

Default: music-led sequence = cut 1-2 frames early on beats or bars; narration-led
sequence = cut on speech and let the music sit.

### 3.3 Hit points and sync points

- A hit point is a frame where a musical accent is meant to coincide with a visual
  event (a door slam, a punch, a logo). Composers and directors choose them in a
  spotting session before scoring `[S16]`.
- Syncing music to every on-screen action is called Mickey-Mousing, named after
  early Mickey Mouse cartoons `[S17]`. It suits comedy, kids and animation; in
  documentary it reads as cartoonish `[P]`.
- Agent rules `[P]`:
  - About one strong hit per 10-20 s of bed music in long form.
  - Put the biggest accent in the section on its single most important visual.
  - If no accent lands where needed, slip the music by whole bars or move the edit.
    Avoid stretching the music by more than a few percent.

### 3.4 Stingers and risers into reveals `[P]`

- Riser: rising noise or pitch sweep, 1, 2 or 4 bars long, ending exactly on the
  reveal frame. Riser start = reveal time - riser length.
- Stinger or impact: short hit (0.5-3 s) on the reveal frame, often with a sub drop.
- Pattern: riser -> 1-4 frames of near-silence -> impact + reveal. The gap increases
  contrast. The jolt comes from the brain-stem reflex to sudden loud onsets `[S5]`.
- Limit: about one riser-impact pair per minute in long form. Shorts can use more,
  but not on every cut.

### 3.5 Drops `[P]`

- The drop is the first downbeat after a build where the full beat returns. Put the
  payoff shot on that downbeat.
- To find it without hearing: in the short-term loudness trace, the largest upward
  jump after a quieter stretch of 4-16 bars, snapped to the nearest downbeat.

### 3.6 The music-out moment `[P]`

- Remove music (leave room tone) under the line that matters most: the key fact, an
  admission, the setup of a punchline.
- Hard cut on a downbeat for shock; 0.3-1 s fade for a softer drop.
- Bring music back on the next section's downbeat, not mid-phrase.
- One to three per long video. It works because it is rare.

### 3.7 Pre-lap and post-lap

- Split edits: in a J-cut the next scene's audio begins under the previous scene's
  picture; in an L-cut the previous scene's audio continues under the next picture
  `[S18]`. Pre-lap is the J-cut case applied to music or dialogue `[P]`.
- Music pre-lap: start the next cue 0.5-2 bars before the picture cut. It pulls the
  viewer forward `[P]`.
- Music post-lap: let the previous cue's last chord or tail ring 1-2 s over the new
  picture. It carries the mood across `[P]`.

### 3.8 Changing the track at chapter turns `[P]`

- Change when the script's mood changes, not on a timer.
- Options, best first:
  1. First cue ends on its final chord; new cue enters on the next downbeat.
  2. A 0.5-1 s music-out gap between cues.
  3. A 1-2 bar crossfade when both cues share tempo and key.
  4. A plain crossfade between unrelated cues (weakest; smears harmony and rhythm).
- A whoosh or stinger on the join hides a tempo change.

### 3.9 Looping and extending on bar lines `[P]`

- Loop sections that start and end on bar lines, in 4- or 8-bar phrases. A cut on
  the right bar but mid-phrase still sounds wrong.
- Cut on a downbeat transient (kick or chord hit), which masks the join. Use a
  5-20 ms crossfade to prevent clicks.
- Reverb tails: a cut that chops a tail sounds abrupt. Crossfade longer (50-200 ms)
  or pick a loop point with the same density on both sides.
- Extend by repeating a middle section; never repeat the intro or the ending.
- Shorten by removing whole phrases, and keep the track's real ending.
- Back-time the ending: place the track's final chord on the video's last beat,
  then fill backwards, so the video never ends on a fade in mid-phrase.
- Check a seam without hearing: compare short-term loudness and spectral centroid
  in the 0.5 s either side of the cut; a jump larger than elsewhere in the track
  marks a bad seam.

---

## 4. Music under voice

### 4.1 Levels and ducking

| Parameter | Value | Source |
|---|---|---|
| Accessibility bar: background sound vs foreground speech | At least 20 dB lower, except sounds of 1-2 s (WCAG 2.1 SC 1.4.7, level AAA) | `[S19]` |
| Duck amount, dialogue-heavy content | About -12 dB; -6 to -8 dB if the bed is already quiet | `[S20]` (tutorial guidance) |
| Duck amount, vlogs | -15 to -25 dB | `[S20]` (tutorial guidance) |
| Duck fades | Under about 200 ms sounds abrupt; longer sounds natural | `[S20]` |
| Perceived loudness of speech vs music at equal LUFS | Speech sounds 2-3 dB louder than music at the same integrated loudness | `[S14]` |
| Agent default under narration | Music 18-22 LU below the voice while speaking; release to about 10-14 LU below in gaps longer than 1 s | `[P]` (bracketed by `[S19]` and `[S20]`) |

Worked example `[P]`: voice short-term loudness around -14 LUFS, so the bed sits
near -32 to -36 LUFS short-term under speech and rises toward -24 to -28 LUFS in
pauses. Measure both with the loudness trace; do not trust fader numbers.

Sidechain vs manual automation `[P]`:

| Method | Strength | Weakness | Use when |
|---|---|---|---|
| Sidechain compression (voice triggers gain reduction on music; for example ffmpeg `sidechaincompress`) | Automatic, consistent, handles fast talk | Pumps with short release; long release swallows musical swells | Fast, continuous narration (news, Shorts) |
| Manual keyframe automation from speech timestamps (VAD or transcript) | Music can swell in pauses and land on phrase ends | More work; needs accurate timestamps | Documentary, storytelling, anything with pauses |
| Editor auto-ducking (writes keyframes for you) | Fast, editable afterwards | Needs sensitivity and fade tuning `[S20]` | First pass, then adjust |

Agent default: build the duck from transcript word timings, 250-400 ms fade down
starting 100-200 ms before the first word, 500-800 ms fade up after the last word,
and merge gaps shorter than 1 s so the bed does not pump. `[P]`

### 4.2 EQ carving for intelligibility

- Consonants sit mainly in 2-4 kHz. Octave bands centred at 2 kHz, 4 kHz and 1 kHz
  contribute about 30%, 25% and 20% of speech intelligibility respectively `[S21]`.
- So carve the music, not the voice `[P]`:
  - broad bell cut of 3-6 dB centred near 2-3 kHz (Q about 0.7-1.0) on the music bus;
  - better: a dynamic EQ or multiband sidechain that makes this cut only while the
    voice is active;
  - if the voice is still masked, choose a track with less 1-4 kHz content (pads,
    low piano, bass-led beats) over lead synths, bright guitars or vocals.
- Keep the voice's own 2-4 kHz intact; chest-mounted mics already lose some of that
  band `[S21]`.

### 4.3 Loudness targets

| Delivery | Target | Source |
|---|---|---|
| YouTube (long form) | Played back normalized to about -14 LUFS. Louder uploads are turned down; quieter ones are not turned up. Check "content loudness" in Stats for Nerds | `[S22]` (third-party measurement; YouTube publishes no official number) |
| YouTube Shorts | No separate figure found; assume the YouTube behaviour above | gap |
| TikTok, Instagram Reels | No official spec found; third-party guides conflict (some say about -14 LUFS normalization, others say no in-feed normalization) | `[S23]` |
| Spotify (music and podcasts on Spotify) | -14 LUFS default; Loud -11, Quiet -19; quiet tracks turned up; masters at -1 dBTP (or -2 dBTP if louder than -14 LUFS) | `[S24]` |
| Apple Podcasts | -16 LKFS ±1 dB; true peak no higher than -1 dBFS; measured per ITU-R BS.1770 | `[S25]` |
| AES TD1008 streaming: speech and mixed content | -18 LUFS distribution loudness | `[S14]` |
| AES TD1008 streaming: music normalized separately | -16 LUFS | `[S14]` |
| EBU R128 broadcast | -23 LUFS ±0.5 LU (±1 LU live); max true peak -1 dBTP | `[S26]` |

Agent defaults `[P]`:
- YouTube, Shorts, TikTok, Reels: mix to -14 LUFS integrated, true peak ≤ -1 dBTP.
  Louder gains nothing on YouTube `[S22]` and costs dynamics.
- Podcast feed: -16 LUFS, ≤ -1 dBTP `[S25]`.
- Broadcast delivery: -23 LUFS, ≤ -1 dBTP `[S26]`.
- Reference point: one measured animated explainer sat at -15.4 LUFS integrated with
  a 2.2 LU loudness range, a very flat mix `[M]` (card `animated-explainer/0NY2gAftzJE`).

---

## 5. Per-genre conventions

All rows are `[P]` unless marked. "Changes" = how often the music track changes.

| Genre | Music role | Energy | Changes | Signature moves | Common mistakes |
|---|---|---|---|---|---|
| Documentary / video essay | Bed under narration; featured in chapter openers and montages | Low-medium | Per chapter (every 3-8 min) | Minimal piano, pads, ambient pulses; music-out on the thesis line | Wall-to-wall music; melodic tracks fighting the VO; trailer-epic music on minor points |
| Animated explainer | Continuous bed, synced accents | Medium, steady | Per section (1-3 min) | Hits on animation beats; flat, dense mix (measured: -15.4 LUFS, LRA 2.2 LU `[M]`) | Busy 1-4 kHz bed under dense narration; no accents, so the animation feels unscored |
| Science / engineering entertainment | Bed; featured in build montages and test results | Medium-high | Per segment (1-3 min) | Tension bed before a test, riser into the result, drop or silence at the outcome | Same hype loop throughout; no silence before the test outcome |
| Challenge / spectacle | Near-constant bed | High | Often (every 30-90 s, per challenge beat) | Tension beds under countdowns, stingers on eliminations and stakes, triumph at the win | One loop for the whole video; no dynamic contrast; music masking the host |
| Tech review | Light bed (clean electronic, lo-fi) or absent under talking head; featured over product b-roll | Low-medium | Rarely (per section) | Music up on b-roll, down or out on spec talk | Vocal tracks; beats that fight spec lists; no duck at b-roll-to-talk transitions |
| Fast tech news | Quiet driving bed or none under dense speech; comic stingers | Medium-high | Rarely | Meme stingers on jokes, hard music-outs | Any melodic bed under fast speech; stingers every sentence |
| Gaming commentary | Game audio first; low bed or none | Follows gameplay | With game segments | Music swells for highlights, out for commentary peaks | Stacking a bed on the game's own music; game soundtracks drawing Content ID claims |
| True crime / storytelling | Sparse dark ambient bed (mystery, dread); long stretches without music | Low | At act turns | Music-out for victim details and key evidence; slow tension builds to reveals | Horror stingers on real victims; constant tension that numbs; upbeat tracks |
| Cooking | Warm upbeat, jazz or lo-fi bed | Medium-low | Per recipe stage | Music down for sizzle and chopping sounds | Music masking cooking sounds; one loud track throughout |
| Kids education | Featured: bright, childlike cues and songs | Medium-high, steady | Per segment | Mickey-Mousing on actions `[S17]`, jingles for recaps | Minor or dark cues; frantic tempos; sung lyrics over teaching lines |
| Calm / faith | Sacred or cozy bed (pads, piano, choir) | Low | Rarely (one per video or per section) | Slow swells under key lines; long reverb | Percussion; stingers; trailer-style builds; bed too loud for reflective speech |
| Fast-facts Shorts | Continuous bed (mystery, tension or trending sound) | Medium-high | Once per Short, if at all | Cuts every 1-2 beats; bed starts on frame 1 | Track change mid-Short; music intro longer than 1 s before the hook; bed drowning VO on phone speakers |
| Gaming Shorts | Featured hype or phonk | High | One track | Drop synced to the highlight; cuts on beats | Drop missing the payoff; commercial tracks used outside the platform's own library, drawing claims |
| Podcast-clip Shorts | Speech-led; bed absent or very low (ambient, lo-fi) | Low | One track | Bed only under captions-heavy intros | Bed fighting overlapping speakers; music implying an emotion the speaker is not showing |
| VFX / transition edits | Featured: the music drives the edit | High | One track | Every transition on a beat or drop; riser ends on the transition frame | Transitions 1-3 frames off the beat; riser ending before or after the effect |
| Animated storytime | Bed under VO, mood follows the story | Medium | Per story beat (every 1-2 min) | Comic stingers and Mickey-Mousing on jokes; music-out before punchlines | Bed never stops; a stinger on every line |

---

## 6. Failure modes

| Failure | How to detect without hearing | Fix |
|---|---|---|
| Music fights the voice | Music within 20 dB of the voice during speech `[S19]`; strong music energy in 1-4 kHz under speech `[S21]`; track has vocals | Duck to 18-22 LU below voice; carve 2-3 kHz; switch to stems without melody or to a sparser track `[P]` |
| Mismatched mood | Library tags, mode or BPM contradict the section's mood row; valence opposite to the script's `[S3]` | Re-query with the 2.2 vocabulary; change mode before tempo `[P]` |
| Same stock track as everyone | Track sits on page one of "popular" or "trending"; YouTube Audio Library staples | Skip page one; sort by newest; combine two mood tags; use stems to re-arrange `[P]` |
| Abrupt loop seam | Cut not on a bar line; loudness or spectral jump at the seam larger than elsewhere | Move to a downbeat on a 4- or 8-bar phrase; 5-20 ms crossfade; keep reverb tails `[P]` |
| Ending mid-phrase | Track still at full level on the last frame | Back-time the real ending to the last beat `[P]` |
| Content ID claim | Claim appears in YouTube Studio | Claims are not strikes; claimant can block, monetize or track `[S27]`. Clear with library tools: Epidemic channel connection `[S10]`, Artlist Clearlist `[S12]`, Pixabay certificate dispute `[S15]` |
| Copyright strike | A takedown request, not a Content ID match; counts toward the three-strike policy `[S27]` | Never use commercial or trending tracks outside a licence that covers the platform; keep the per-track licence record (2.3 step 7) |
| Too loud or crushed | Integrated loudness above -14 LUFS for YouTube | Turned down anyway `[S22]`; remix to -14 LUFS with ≤ -1 dBTP |

---

## Gaps

- Pixabay Music's full facet list (mood, movement, BPM filters) could not be read
  from the page fetch.
- YouTube Audio Library mood values come from a third-party guide; the official help
  page confirms a mood filter but does not list values.
- No official loudness spec found for TikTok, Instagram Reels or YouTube Shorts.
- Most BPM ranges, instrument lists, ducking defaults and genre rows are practice,
  not published sources. Film-scoring texts (for example on spotting and temp tracks)
  and measured genre samples from `research/cards/` should replace `[P]` tags over time.
- Boltz (2001) result is taken from the published abstract; the full text was not read.

---

## Sources

All checked 2026-09-26.

- [S1] Gabrielsson, A. & Lindstrom, E. (2010). The role of structure in the musical expression of emotions. In Handbook of Music and Emotion. https://academic.oup.com/book/38621/chapter/335187128
- [S2] Same chapter, research summary page. https://www.researchgate.net/publication/263964370_The_Role_of_Structure_in_the_Musical_Expression_of_Emotions
- [S3] Eerola, T., Friberg, A. & Bresin, R. (2013). Emotional expression in music: contribution, linearity, and additivity of primary musical cues. Frontiers in Psychology 4:487. https://www.frontiersin.org/articles/10.3389/fpsyg.2013.00487/full
- [S4] Juslin, P. N. & Laukka, P. (2003). Communication of emotions in vocal expression and music performance: Different channels, same code? Psychological Bulletin 129, 770-814 (summary table, p. 802). https://www.brainmusic.org/EducationalActivities/Juslin_emotion2003.pdf
- [S5] Juslin, P. N. & Vastfjall, D. (2008). Emotional responses to music: The need to consider underlying mechanisms. Behavioral and Brain Sciences 31, 559-575. https://www.researchgate.net/publication/23291396_Emotional_Responses_to_Music_The_Need_to_Consider_Underlying_Mechanisms
- [S6] Boltz, M. G. (2001). Musical soundtracks as a schematic influence on the cognitive processing of filmed events. Music Perception 18(4), 427-454. https://mp.ucpress.edu/content/18/4/427
- [S7] YouTube Help, Use music and sound effects from the Audio Library. https://support.google.com/youtube/answer/3376882
- [S8] Influencer Marketing Hub, YouTube Audio Library guide (mood values). https://influencermarketinghub.com/youtube-audio-library/
- [S9] Epidemic Sound, Music by mood. https://www.epidemicsound.com/music/moods/
- [S10] Epidemic Sound Help Center, Why was a Content ID claim received from Epidemic Sound? https://help.epidemicsound.com/hc/en-us/articles/26253712691730-Why-was-a-Content-ID-claim-received-from-Epidemic-Sound ; see also https://help.epidemicsound.com/hc/en-us/articles/26248340314258-Safelisting
- [S11] Artlist Blog, Song Match; Artlist Help, Browsing Artlist's music catalog. https://artlist.io/blog/song-match-feature/ ; https://help.artlist.io/hc/en-us/articles/29596157272221-Browsing-Artlist-s-Music-catalog
- [S12] Artlist Help, Understanding copyright and Content ID claims; Understanding Artlist's Clearlist. https://help.artlist.io/hc/en-us/articles/29648852943901-Understanding-copyright-and-Content-ID-claims ; https://help.artlist.io/hc/en-us/articles/29648622402333-Understanding-Artlist-s-Clearlist
- [S13] Pixabay Music browse page. https://pixabay.com/music/
- [S14] AES TD1008 (2021), Recommendations for Loudness of Internet Audio Streaming and On-Demand Distribution (now AES77-2023). https://aes2.org/wp-content/uploads/2024/01/20210924_TD1008_v3.13.pdf
- [S15] Pixabay Blog, How to clear a YouTube Content ID claim with a Pixabay License Certificate. https://pixabay.com/blog/posts/how-to-clear-a-youtube-content-id-claim-with-a-pix-190/
- [S16] FilmDaft, Film Scoring 101 (hit points, spotting sessions). https://filmdaft.com/film-scoring-101-meaning-types-techniques-and-examples/
- [S17] Wikipedia, Mickey Mousing. https://en.wikipedia.org/wiki/Mickey_Mousing
- [S18] Wikipedia, Split edit (J-cut, L-cut). https://en.wikipedia.org/wiki/Split_edit
- [S19] W3C, Understanding WCAG 2.1 Success Criterion 1.4.7: Low or No Background Audio. https://www.w3.org/WAI/WCAG21/Understanding/low-or-no-background-audio.html
- [S20] Premiere Pro auto-ducking tutorials (duck amounts and fade guidance; tutorial advice, not Adobe defaults). https://www.freepik.com/blog/how-to-use-auto-ducking-in-premiere-pro-for-clean-professional-audio/ ; https://www.junoschool.org/article/audio-ducking-premiere-pro-vlogs/
- [S21] DPA Microphones, Facts about speech intelligibility. https://www.dpamicrophones.com/mic-university/background-knowledge/facts-about-speech-intelligibility/
- [S22] Production Advice (Ian Shepherd), YouTube Stats for Nerds normalization values. https://productionadvice.co.uk/stats-for-nerds/
- [S23] Third-party platform loudness guides (conflicting on TikTok). https://clickyapps.com/creator/video/guides/lufs-targets-2025 ; https://www.songbrain.ai/guides/lufs-for-spotify-and-tiktok
- [S24] Spotify for Artists, Loudness normalization. https://support.spotify.com/us/artists/article/loudness-normalization/
- [S25] Apple Podcasts for Creators, Audio requirements. https://podcasters.apple.com/support/893-audio-requirements
- [S26] EBU R 128, Loudness normalisation and permitted maximum level of audio signals. https://tech.ebu.ch/docs/r/r128.pdf
- [S27] YouTube Help, Copyright strikes vs Content ID claims. https://support.google.com/youtube/answer/7002106
- [M] This project's measured card: `research/cards/animated-explainer/0NY2gAftzJE.md`.
