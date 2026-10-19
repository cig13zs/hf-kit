# Sound design and SFX for video, plus game audio

Status: v2 (2026-09-26). All sections written; open gaps are listed in section 10.
Scope: picking, placing, layering and mixing SFX in edited video; sound for Roblox
and small web/HTML games.

## 0. How to read this chapter

- You cannot hear. Every choice below is a number, a position on the timeline, or a
  rule. When a rule is marked **practice (inferred)**, it is editing convention, not
  a published standard; treat it as a strong default and break it only for a reason
  you can state.
- Sourced claims carry a bracketed source key, e.g. [S1]. The key list is in
  section 9, with URLs and the date checked.
- Units: dB = decibels relative to the clip's own level; LUFS/LKFS = integrated
  loudness (same unit, two names [S2]); dBTP = true peak; LU = loudness unit (1 LU =
  1 dB of loudness change).
- Frame math at 30 fps: 1 frame = 33 ms. At 24 fps: 42 ms. At 60 fps: 17 ms.

### Hard rules (apply always)

1. Voice is the anchor. No SFX, music or ambience may mask a word. (Section 3.)
2. Every SFX must answer "what visual event or story beat does this serve?" If there
   is no answer, cut it. (Section 4.)
3. Never reuse the identical file for more than 2 consecutive uses of the same event
   type; vary file, pitch or level. (Section 1, 3.)
4. Final master: true peak at or below -1 dBTP; no sample clipping. [S1][S3]
5. License check before placement: record source, license and attribution text for
   every file in the project's audio credits log. (Section 8.)

---

## 1. SFX taxonomy for editing

Timing columns use these terms:
- Lead: how far the sound starts before the visual event (the cut, the hit, the
  appearance).
- Sync point: which part of the sound lands on the event frame.
- Tail: how long it rings after.

All timings, lengths and genre notes in this table are **practice (inferred)** from
common editing convention unless a source key appears.

| SFX | Emotional job | Lead / sync / tail | Typical length | Layering | Heavy use | Avoid / sparing |
|---|---|---|---|---|---|---|
| **Whoosh / swish** | Motion, speed, "we are moving to something new" | Lead 4-10 frames; loudest point (the "pass-by" peak) on the cut or at the midpoint of the move; tail 0-6 frames | 0.3-1.2 s | Mid whoosh + optional low air layer; high-pass at 150-250 Hz so it does not muddy the voice | Shorts, gaming, tech, hype edits, trailers | Calm, faith, documentary interviews; never on every cut |
| **Riser** | Tension, anticipation, "something is coming" | Starts 1-4 s before the event; ends exactly on the event frame (hard stop or cut into an impact) | 1-8 s (2-4 s most common in Shorts) | Riser + impact at its end is the classic pair; can add a reverse cymbal in the last 0.5-1 s | Trailers, hype, reveals, countdowns, EDM-style edits | Calm, meditative, faith, most explainers |
| **Downlifter / drop-down** | Release, deflation, "settle in", or exit from a high-energy section | Starts on the event frame and falls after it; tail 1-3 s | 1-4 s | Often follows an impact; pairs with a music drop-out | Trailers, transitions out of a climax, gaming | Anything with continuous dialogue on top |
| **Impact / hit** | Emphasis, punctuation, "this matters" | Sync the transient to the exact frame (0 lead); tail 0.3-2 s | 0.2-2 s | Transient (click/snap) + body (mid thump) + low tail (sub). Keep total layers to 2-3 | Trailers, hype, gaming, sports, text slams | Soft explainers, calm, faith (use a soft "thud" or nothing) |
| **Boom** | Scale, weight, a big reveal | Sync on frame; tail 1-4 s | 1-5 s | Usually the low layer under an impact; high-pass nothing, low-pass above ~2-4 kHz | Trailers, documentaries at big moments, gaming | Talky sections; phone-speaker-only content loses most of it (practice) |
| **Sub drop** | Physical weight, "floor drops out", beat drop | Sync on frame; pitch falls over tail 0.5-2 s | 0.5-3 s | Layer under an impact or a music drop; check it on small speakers, add a 100-200 Hz harmonic layer so phones hear something | Hype, trailers, EDM edits, reveals | Anything where the music bass already fills 40-80 Hz |
| **Braam** | Epic dread, blockbuster scale | Sync on frame (often a title card); tail 2-5 s | 2-6 s | Stands alone or on top of a boom; duck music hard | Trailers, dramatic docs, gaming montages; also comedic parody use | Everyday creator content (reads as parody), calm, faith |
| **Reverse (reverse cymbal / reverse reverb)** | Suction into the next moment, dreamlike lead-in | Ends exactly on the event frame; lead = its full length | 0.5-3 s | Often the last part of a riser, or before a vocal line | Transitions, music videos, flashbacks | Dense dialogue; overuse sounds dated (practice) |
| **Glitch** | Digital error, tech, chaos, humor, jump in time | Sync on the glitch frame; tail 0-0.3 s | 0.1-1 s | Stutter + bit-crush layer; match the visual glitch length | Tech, gaming, hacking, meme edits | Calm, faith, prestige doc |
| **UI click / pop / tick** | Precision, interaction, counting, "a thing registered" | Sync on the frame the element changes; tail near 0 | 20-200 ms | Single layer; vary pitch per repeat | Explainers, app demos, tutorials, listicles, countdown ticks | Nature, calm, emotional scenes |
| **Typing** | Work, writing, hacking, text being composed | Sync each key to each character appearing, or use a bed that starts with the first character and stops with the last | Matches the text animation | One keyboard type per video; low level | Explainers, tech, story-time, chat-screen recreations | Calm pieces unless the story is about writing |
| **Camera shutter** | Capture, freeze frame, "evidence", snapshot | Sync the shutter click on the freeze frame or flash frame | 0.1-0.5 s | Optional white-flash visual; no other layers | Freeze-frame intros, photo reveals, "caught" moments | Formal docs (sparingly) |
| **Pop-in for text** | Light emphasis, playful arrival | Sync on the first frame the text is visible (or the overshoot peak of a scale-bounce) | 50-250 ms | Single layer; pitch-step for successive items (see 5.1) | Shorts, listicles, kids, explainers | Serious, grief, faith content |
| **Swoosh-in for graphics** | Arrival from off-screen, "incoming" | Lead 2-6 frames; peak when the element settles into place | 0.2-0.8 s | Shorter, brighter cousin of the whoosh | Explainers, lower thirds, social edits | Minimal or calm styles, which should use silence or a soft tick |
| **Foley** (footsteps, cloth, handling, object sounds) | Realism, presence, touch | Sync on contact frames (foot plant, object set-down) | Event-length | One foley layer per action; match the room (see 3.4) | Narrative, doc re-creations, ASMR, cooking, product ads | Pure motion-graphics pieces |
| **Ambience** (city, forest, office, wind) | Place, time, mood | Starts 0.5-2 s before a scene or on the cut; fades out with the scene; J/L cut across scene changes | Scene length | 1 bed per location, sometimes 2 (general + detail); keep 15-25 dB below voice (practice) | Docs, narrative, vlogs, calm/nature, games | Pure explainers over motion graphics (optional) |
| **Room tone** | Invisible glue; hides edits and silences | Continuous under all dialogue; fill every gap between dialogue clips | Whole scene | Recorded or matched to the dialogue room; never true digital silence under dialogue scenes | Any edited dialogue or interview | None; it is always needed where dialogue is edited |
| **Record scratch** | Abrupt stop, "wait, what?", comedic freeze | Sync on the freeze or cut; music stops on the same frame | 0.3-1 s | Music must cut out on the scratch; often followed by a beat of silence | Comedy, meme edits, story-time ("yep, that's me") | Anything serious; it is a cliché, use at most once per video |
| **Comedic stings** (boing, slide whistle, vine boom, sad trombone, crickets, rimshot) | Punchline, irony, awkwardness | Sync on the reaction frame or 2-6 frames after the joke lands; tail short | 0.2-2 s | Solo; duck or cut the music under it | Comedy, meme, kids, gaming | Brand, doc, faith, grief; overuse kills the joke (practice) |

### Placement decision rules (practice, inferred)

- Whoosh on a cut: align the whoosh peak to the cut frame, not its start. If the
  file has a slow build, the start will sit 4-10 frames before the cut.
- Riser into reveal: end the riser on the reveal frame; put an impact on the
  same frame; drop the music 0.3-1 s before the reveal (see 2.2).
- Impact: 0 frames lead. If it feels late, move it 1 frame earlier, never later.
  Audiences tolerate sound slightly after the picture better than before (this
  matches broadcast lip-sync tolerance windows; practice, inferred).
- Text pop: on the first visible frame, or on the overshoot frame of a
  scale-bounce.
- **Tails** of impacts and booms may run under the next shot; they must not run
  under the next spoken line at full level. Fade or duck them.

---

## 2. Density and restraint by genre

### 2.1 SFX per minute (practice, inferred)

Counts are *designed* SFX events (whooshes, pops, hits, stings), not ambience or
room tone.

| Genre | Designed SFX / min | Character | Notes |
|---|---|---|---|
| Fast Shorts / TikTok / Reels (hype, meme, gaming) | 15-40 | Bright, punchy, frequent | Sound on most cuts and text pops; still vary files |
| Listicle / "Top 10" Shorts | 10-25 | Pop-ins, ticks, whooshes | One sound family for the whole video |
| Explainers (motion graphics) | 4-12 | Clean UI clicks, soft swooshes | Sound the *key* entrances only |
| Tutorials / app demos | 2-8 | UI clicks matching real clicks | Voice clarity dominates |
| Documentary | 0-4 designed; ambience and foley continuous | Realistic, invisible | Big moments get one boom or riser at most |
| Vlogs | 2-10 | Ambience + a few transitions | Keep real sound; add SFX for jokes |
| Narrative / short film | Foley and ambience continuous; designed SFX rare | Invisible | Sound serves story, not edit |
| Calm, meditation, faith, devotional | 0-2 | Soft ambience (wind, water, room), bells only if culturally fitting | Silence and space are the design; no whooshes, no impacts, no comedic stings |
| Product ads | 6-20 | Tactile foley (clicks, snaps, pours) + a few whooshes | Satisfying object sounds carry the ad |
| Satisfying / ASMR | Continuous foley; 0 designed | Close, clean, high detail | No music-style SFX over the ASMR sound |

### 2.2 Silence as a device (practice, inferred)

| Device | How | Where |
|---|---|---|
| **Sound drop before a reveal** | Cut music and SFX to silence (or room tone only) 0.3-1.0 s before the reveal frame; bring the full mix back on the reveal, often with an impact | Reveals, punchlines, before/after, product hero shot |
| **Hard cut to silence** | On a shocking line, a freeze frame, or a comedic record scratch, cut *everything* on one frame; hold 0.5-2 s | Shock, comedy, grief beats |
| **Breath before the drop** | Pull the music out for one bar before a beat drop | Hype edits, music montages |
| **Silence for weight** | Leave 1-3 s of only ambience after an emotional line | Documentary, faith, testimonies |

Rules:
- "Silence" in a dialogue scene means room tone, not digital zero, unless the
  intent is a jarring void. (practice, inferred)
- One hard silence per 2-3 minutes at most, or it stops working. (practice, inferred)
- In Shorts, keep silences under ~1 s; longer gaps read as a broken video.
  (practice, inferred)

---

## 3. Mixing for video

### 3.1 Dialogue first

Order of operations (practice, inferred):
1. Clean and level dialogue: high-pass 70-100 Hz, remove noise, even out level.
2. Set dialogue loudness to target (3.3).
3. Add music under it; duck it (3.2).
4. Add SFX last; set each relative to the voice, never relative to the music.
5. Check the loudest SFX against the voice at the same timeline point.

Dialogue loudness norms (sourced):

| Standard | Dialogue / programme target | Measured how | True peak | Source |
|---|---|---|---|---|
| Netflix | -27 LKFS, +/-2 LU | Dialogue-gated (only speech is measured) | -2 dBTP | [S4] |
| AES TD1008 (streaming, speech measurable) | -18 LUFS, +1 LU | Dialogue integrated loudness | -1 dBTP at the codec input | [S3] |
| AES TD1008 news/talk and drama formats | -18 LUFS | Integrated | -1 dBTP | [S3] |
| EBU R128 (broadcast) | -23 LUFS, +/-0.5 LU | Integrated, whole programme | -1 dBTP | [S1][S2] |
| ATSC A/85 (US broadcast) | -24 LKFS | Integrated | (similar limits) | [S2] |

Relative levels (practice, inferred; check with a meter):

| Element | Level relative to voice |
|---|---|
| Music bed under speech | -15 to -25 dB below voice (short-term loudness) |
| Music with no speech | up to voice level or 3-6 dB below |
| Designed SFX (whoosh, pop, click) | -6 to -15 dB below voice; peaks may briefly match voice level on impacts between lines |
| Impacts / booms on reveal (no speech) | Can reach voice level; never above it by more than ~3 LU short-term |
| Ambience | -15 to -25 dB below voice |
| Room tone | Just audible; matched to the dialogue noise floor |

### 3.2 EQ carving and sidechain (practice, inferred)

- Speech intelligibility sits roughly 1-4 kHz. Cut 2-4 dB in that band on music (and
  on busy SFX) *while speech plays*. A dynamic EQ keyed from the voice does this only
  when needed.
- High-pass SFX and music that do not need lows (whooshes, pops, UI): 150-300 Hz.
- Keep one owner per low band: if the music has heavy bass, shorten or high-pass the
  sub drop.
- **Sidechain / ducking** music under voice: 6-12 dB of reduction, attack 5-50 ms,
  release 200-500 ms, so the music breathes back up between phrases without pumping.
  Remote editors with no sidechain: draw volume automation dips of 6-12 dB with
  150-300 ms ramps.
- Duck music 3-6 dB for 0.5-1 s under a key SFX (impact, riser end) so the SFX reads
  without being turned up.

### 3.3 Loudness targets for delivery

| Platform / use | Target integrated loudness | True peak | Source / status |
|---|---|---|---|
| YouTube (all videos) | Mix to about -14 LUFS. YouTube turns down videos louder than its reference; it does **not** turn quiet ones up | -1 dBTP | YouTube publishes no official LUFS number. The turn-down-only behaviour and the "content loudness" readout are documented from Stats for Nerds [S5]; the -14 figure is community-measured [S6] |
| Speech-led YouTube / podcast-style | -16 to -14 LUFS integrated; speech itself near -18 to -16 LUFS dialogue-gated | -1 dBTP | Inferred from [S3] and [S5]: louder than -14 gets turned down, quieter stays quiet |
| Broadcast (Europe) | -23 LUFS +/-0.5 LU | -1 dBTP | [S1][S2] |
| Broadcast (US) | -24 LKFS | not verified here; use -2 dBTP to be safe | [S2] |
| Netflix-style long form | -27 LKFS dialogue-gated | -2 dBTP | [S4] |
| TikTok / Reels / Shorts | No published target found. Use -14 LUFS, -1 dBTP | -1 dBTP | practice (inferred) |

Peak rules (sourced): keep true peak at or below -1 dBTP before any lossy encode;
lower-bitrate codecs overshoot more, so lower the limiter ceiling for low bitrates
[S3]. AES also advises no more than about 1 dB of limiting before final encoding,
because heavier limiting can sound worse than the occasional clip [S3]. Put a
true-peak limiter last in the chain [S3].

### 3.4 Reverb and space consistency (practice, inferred)

- One "room" per scene. If the voice is dry (close mic, studio), SFX that belong to
  the diegetic world get a short, quiet room reverb (0.3-0.8 s decay, 10-20% wet);
  designed, non-diegetic SFX (UI pops, whooshes) stay dry or share one short
  plate.
- An outdoor shot gets outdoor ambience, not a hall reverb.
- Room tone and ambience must continue across every dialogue edit inside a scene; a
  change in noise floor at a cut is audible even when the words are fine.
- Voiceover and on-camera audio in the same video: match their EQ and room enough
  that the switch is not jarring, or make the difference a deliberate style.

### 3.5 Amateur mistakes and fixes (practice, inferred unless noted)

| Mistake | Symptom (as seen on meters or waveforms) | Fix |
|---|---|---|
| SFX louder than voice | SFX short-term loudness above voice short-term loudness; peaks hit the limiter | Drop SFX 6-12 dB; duck under speech |
| Same whoosh on every cut | One file ID repeated across all cuts | Pool 3-6 variants; rotate; +/-1-3 semitone pitch; skip 1 in 3 cuts |
| Mismatched room tone | Noise floor jumps at edit points; gaps drop to digital silence | Lay continuous room tone; crossfade 5-20 ms at edits |
| Clipping | Sample peaks at 0 dBFS; true peak above -1 dBTP | Reduce gain before the limiter; true-peak limiter at -1 dBTP [S3] |
| Over-limiting to be "loud" | Integrated loudness far above -14 LUFS on YouTube | YouTube turns it down anyway, so you lose dynamics for nothing [S5]; target about -14 LUFS |
| Music fighting speech | Music within ~10 dB of voice under speech | Duck 6-12 dB and carve 1-4 kHz |
| Sub drops on phone content | Energy only below 60 Hz | Add a 100-200 Hz harmonic layer, or accept it is felt only on headphones |
| Stings on serious lines | Comedic SFX in grief/faith/news context | Remove; use silence |
| Hard cuts on SFX tails | Tail truncated mid-decay | Fade tails over 50-300 ms |

---

## 4. Syncing SFX to motion graphics and animation

### 4.1 Sync table (practice, inferred)

| Animation event | Sound | Sync frame |
|---|---|---|
| Text pop / scale-bounce in | Pop, soft tick | First visible frame, or overshoot peak |
| Word-by-word captions | Nothing, or at most a very quiet tick on emphasised words only | Word's first frame |
| Element slides in from off-screen | Swoosh-in | Swoosh peak on the settle frame (ease-out end) |
| Element exits | Reverse swoosh, or nothing | Peak at the start of the exit |
| Counter / number roll | Tick per step (throttled to max ~15/s), or a rising tone, plus a "ding" on the final value | Tick on each value change; ding on the final frame |
| Progress bar / line draw | Soft rising tone or a riser | Starts with the draw, ends on completion |
| Checkmark / success state | Short bright chime or click | First frame of the check |
| Error / cross | Low buzz or thud | First frame of the cross |
| Scene transition (wipe, zoom, whip) | Whoosh | Peak on the midpoint (whip) or the cut (wipe/zoom) |
| Logo reveal | Riser into impact or shimmer | Impact on the frame the logo resolves |
| Camera shake | Impact or boom | Shake start frame |

### 4.2 Selective sound, not "every animation gets a sound"

Decision rules (practice, inferred):
1. Rank the animations in each 5-10 s window by story importance. Sound the top
   1-2; leave the rest silent.
2. Secondary elements that enter *with* a primary element share its sound; no
   separate sound per element.
3. Staggered lists (bullets entering one by one): sound the first and last, or use
   a pitch-rising sequence on all items only when the list is the point of the scene
   (see 5.1 pitch steps).
4. Continuous or looping motion (floating icons, background particles): no SFX.
5. While the voice is speaking a sentence, prefer quieter or no SFX; place designed
   SFX in the gaps between phrases.
6. If more than ~60% of animations in a minute have sounds, cut half, starting with
   the smallest elements.

---

## 5. Game audio fundamentals

Most numbers in this section are design defaults (practice, inferred). Where a
middleware or platform documents the mechanism, the source key is given.

### 5.1 Feedback sounds and juice (practice, inferred)

| Event | Sound character | Length | Rules |
|---|---|---|---|
| Collect / coin | Bright, short, rising pitch | 50-300 ms | Pitch-step on combos (below) |
| Reward / level up | Major-key arpeggio or chime, longer | 0.5-2 s | Rarer events get longer, fuller sounds |
| Error / denied | Low, dull, short buzz or thud | 100-300 ms | Never harsh or loud; repeated errors must not fatigue |
| UI hover | Very quiet tick | 20-80 ms | Optional; quieter than click |
| UI click / confirm | Click or soft pop | 30-150 ms | Every button the same family |
| UI back / cancel | Lower-pitched click | 30-150 ms | Pitched down from confirm |
| Hit (dealt) | Punchy transient | 50-300 ms | Pair with screen shake/hit-stop |
| Hit (taken) | Duller, lower, with a vocal grunt or thud | 100-500 ms | Distinct from hit-dealt |
| Combo escalation | Same sound, pitch up per step | per event | +1 semitone (x1.0595 playback rate) or a musical-scale step per combo count; cap at +12 semitones; reset on combo break |

Pitch math: playback-rate multiplier = 2^(semitones/12). +1 st = 1.0595, +2 st =
1.1225, +5 st = 1.3348, +7 st = 1.4983, +12 st = 2.0.

Combo on a musical scale (sounds nicer than chromatic): major pentatonic steps
0, 2, 4, 7, 9, 12 semitones.

### 5.2 Variation, fatigue, voice limits

| Technique | Default | Basis |
|---|---|---|
| Pitch randomization | +/-1 to +/-2 semitones (rate 0.89-1.12) for footsteps, hits, UI repeats; +/-0.5 st for tonal UI | practice (inferred) |
| Volume randomization | +/-1 to +/-3 dB | practice (inferred) |
| Round-robin | 3-6 variants per frequent sound; never the same variant twice in a row | practice (inferred); Wwise Random Containers implement this [S14] |
| Cooldown | Same sound no more than once per 50-100 ms (merge rapid triggers) | practice (inferred) |
| Playback limit per sound | 2-8 simultaneous instances; beyond that, do not start the new one or kill the oldest/quietest | Mechanism documented by Wwise: a limit stops sounds from triggering when enough of that type already play [S14] |
| Priority | Player feedback > danger cues > dialogue > music > ambience > cosmetic | practice (inferred); Wwise uses priority plus limits to choose which voices survive [S14] |
| Global voice budget | Browser/mobile: aim under ~32 simultaneous sounds | practice (inferred) |

Listener-fatigue rules (practice, inferred):
- The most frequent sound in the game (footstep, click, shot) must be the shortest,
  softest and most varied.
- Rare sounds may be long and loud; common sounds may not.
- Avoid harsh 2-5 kHz energy in anything that repeats more than once a second.
- Give the player separate Music and SFX volume controls; MDN recommends volume and
  mute controls for web audio [S16].

### 5.3 Adaptive music

| Technique | What | When to use | Source |
|---|---|---|---|
| Horizontal re-sequencing | Move between music segments (explore -> combat -> victory) in response to game events, keeping the beat | State changes are discrete | [S15] |
| Vertical layering | Synchronized stems play together; a game parameter sets each layer's volume so intensity rises and falls | Intensity changes smoothly | [S15] |
| Stingers / transitions | Short phrases queued at the end of the current phrase, or laid on top for events | One-off events | [S15] |

Implementation defaults (practice, inferred):
- Switch horizontally on the next bar line (at 120 BPM in 4/4, a bar is 2 s); if
  waiting is too slow, crossfade over 0.5-1 s.
- Vertical layers: 2-4 stems of identical length and tempo, started on the same
  sample; fade layers over 1-2 s.
- Small web/Roblox games: vertical layering is the cheapest adaptive method (start
  all stems at once at volume 0, then fade).

### 5.4 Mood by game state (practice, inferred)

| State | Music | SFX / ambience |
|---|---|---|
| Menu / lobby | Calm loop, mid tempo, low intensity | Soft UI sounds |
| Explore / build | Light loop, few layers | Full ambience |
| Tension / danger | Add percussion and low drones; minor mode | Heartbeat, low rumble |
| Combat / boss | All layers, faster | Hits prominent; duck ambience |
| Victory | Major stinger, then calm | Reward chime |
| Fail / death | Short descending stinger; music drops out | Low thud, then silence 0.5-1.5 s |
| Shop / UI overlay | Music ducked 6-10 dB or low-pass filtered | UI clicks |

---

## 6. Roblox specifics

### 6.1 Upload limits [S8]

| Item | Limit |
|---|---|
| Formats | MP3, OGG, WAV, FLAC |
| Size / length | Under 20 MB and under 7 minutes |
| Sample rate | Up to 48 kHz |
| Channels | Mono, stereo, 3.0 or 5.1 |
| Uploads per 30 days | 2,000 if ID-verified; 100 if not |
| Cost | Free for both account types |
| After upload | Transcoding and moderation before the asset is usable; starts private |

### 6.2 Privacy and permissions (the 2022 audio change)

- On March 22, 2022, every newly uploaded audio asset became private, and existing
  audio longer than 6 seconds was also made private [S7].
- Stayed public: Roblox's own licensed music and SFX catalog, plus partner audio
  (APM, Monstercat, Pro Sound Effects, Nettwerk, Position Music) [S7].
- Private audio works in an experience only when the experience is owned by the same
  user or group that uploaded it, or has been granted permission [S7][S8]. Otherwise
  the sound silently fails to load, and scripts waiting on it do not fire [S7].
- Creators can grant usage to specific friends and experiences through the asset
  privacy system [S8]. Audio uses its own creation defaults, not the general Asset
  Privacy setting that covers images and meshes [S9].
- Sound effects can be shared publicly via the Creator Store; songs need ID
  verification and acceptance of the Audio Terms of Use to be distributed [S8].
- Roblox offers over 100,000 licensed SFX and music tracks free in the Creator
  Store [S8].

Agent rules (practice, inferred from the above):
1. Upload game audio from the account or group that owns the experience. A
   group game needs group-uploaded audio (or explicit permission).
2. If a sound plays in Studio but not live, check ownership and permission first.
3. Prefer Creator Store licensed audio for quick prototypes. Treat it as licensed for
   use inside Roblox only; do not reuse it in YouTube videos without checking that
   track's terms (not verified here).

### 6.3 Legacy Sound objects vs the Audio API

| | Legacy | Audio API (recommended) |
|---|---|---|
| Status | Sound, SoundGroup and SoundEffect are now discouraged [S10] | Out of Studio beta since Sept 10, 2024 [S11] |
| Play a file | `Sound` (SoundId, Volume, PlaybackSpeed, Looped) | `AudioPlayer` (AssetId, Volume, PlaybackSpeed, Looping) [S10] |
| Group / bus | `SoundGroup` (Sound.SoundGroup = group) | `AudioFader` fed by several Wires; SoundGroups do not work with the new API [S12] |
| Effects | SoundEffect children (EqualizerSoundEffect, etc.) | AudioEqualizer, AudioCompressor, AudioReverb, AudioPitchShifter, AudioFilter, AudioLimiter [S10][S11][S12] |
| 2D (UI, music) | Sound parented to SoundService or PlayerGui, or `SoundService:PlayLocalSound` [S13] | AudioPlayer -> Wire -> AudioDeviceOutput [S10] |
| 3D positional | Sound parented to a Part/Attachment | AudioPlayer -> Wire -> AudioEmitter; AudioListener -> Wire -> AudioDeviceOutput [S10] |
| Distance | RollOffMode, RollOffMin/MaxDistance | AudioEmitter DistanceAttenuation curve [S10] |
| Metering | PlaybackLoudness | AudioAnalyzer (SpectrumEnabled, GetSpectrum) [S11] |
| Extras | none | AudioTextToSpeech, AudioSpeechToText, voice chat via `VoiceChatService.UseAudioApi` [S10] |

SoundService globals [S13]: `AmbientReverb` (reverb preset applied to all sounds),
`RolloffScale`, `DistanceFactor`, `DopplerScale`, `RespectFilteringEnabled`,
`AcousticSimulationEnabled`, `PlayLocalSound()`, `SetListener()`, `GetListener()`.

Suggested bus layout for a simple Roblox game (practice, inferred):
- Master fader (AudioFader or SoundGroup "Master") <- Music, SFX, UI, Ambience.
- Music bus ducks 4-8 dB while a UI overlay or reward stinger plays.
- UI sounds are 2D and local (PlayLocalSound or AudioDeviceOutput path) so they are
  not replicated to other players.
- Settings menu exposes Music and SFX volume sliders bound to those faders.

---

## 7. Web / HTML game audio

Sourced mechanics [S16]:
- Browsers block audio until a user gesture. Create or `resume()` the AudioContext
  inside a click or key handler; check `audioCtx.state === "suspended"`.
- Use decoded AudioBuffers for short SFX; use a media element for long music.
- An AudioBufferSourceNode plays once. Make a new source node per play and reuse
  the decoded buffer.
- Volume goes through a GainNode; pitch through `playbackRate` or `detune`.
- Schedule changes with AudioParam methods (`setValueAtTime`, ramps) rather than
  polling.
- Offer play/stop, volume and mute controls, with accessible labels.

Minimal pattern (practice, inferred; the API calls are from [S16]):

```js
// One context, one master gain, buses as GainNodes. Add a library only
// if you need sprites, fallback formats or 3D panning at scale.
const ctx = new AudioContext();
const master = ctx.createGain(); master.connect(ctx.destination);
const sfxBus = ctx.createGain(); sfxBus.connect(master);
const musicBus = ctx.createGain(); musicBus.connect(master);
addEventListener('pointerdown', () => ctx.state === 'suspended' && ctx.resume(), { once: true });

const lastPlay = new Map();
function play(buffers, { bus = sfxBus, semis = 0, jitter = 1, gainDb = 0, cooldownMs = 60 } = {}) {
  const key = buffers[0]; const now = performance.now();
  if (now - (lastPlay.get(key) ?? -1e9) < cooldownMs) return;   // merge rapid triggers
  lastPlay.set(key, now);
  const src = ctx.createBufferSource();
  src.buffer = buffers[Math.floor(Math.random() * buffers.length)]; // round-robin-ish
  src.detune.value = (semis + (Math.random() * 2 - 1) * jitter) * 100; // cents
  const g = ctx.createGain(); g.gain.value = 10 ** ((gainDb + (Math.random() * 2 - 1) * 2) / 20);
  src.connect(g).connect(bus); src.start();
}
// combo: play(coinBufs, { semis: [0,2,4,7,9,12][Math.min(combo, 5)], jitter: 0 })
```

---

## 8. Free, legally usable SFX sources

Licenses change; re-check the specific file's page before using it, and log source,
license and attribution text per file.

| Source | License | Monetized YouTube | Games (commercial) | Attribution | Key limits | Source |
|---|---|---|---|---|---|---|
| **Freesound** | Per file: CC0, CC-BY 4.0, CC-BY-NC 4.0, older 3.0 variants, retired Sampling+ | CC0 yes; CC-BY yes with credit; **CC-BY-NC no** | Same as video | CC-BY: credit as `"Sound name" by user (freesound.org/s/ID/) licensed under CC-BY 4.0` | License is per file; filter by license; uploaders can change a license later, so record the license at download time | [S17] |
| **Sonniss #GameAudioGDC bundles** | Sonniss royalty-free license | Yes | Yes (unlimited projects, for life) | Not required | No reselling as standalone sounds; no redistribution as a library or asset pack; **no AI training**; cannot claim authorship | [S18] |
| **Kenney audio packs** | CC0 | Yes | Yes | Not required (credit "Kenney" optional); do not use the Kenney logo | CC0 | [S19] |
| **YouTube Audio Library (SFX)** | YouTube Audio Library terms | Yes; will not be Content ID claimed | Not stated; the help page covers YouTube use only | Some items need credit in the description (filter "attribution required") | Use outside YouTube not covered by the page checked | [S20] |
| **Pixabay sound effects** | Pixabay Content License | Yes | Yes when built into a game | Not required | No standalone sale or redistribution in substantially the same form; no commercial use of content showing trademarks/brands; not in a trademark | [S21][S22] |
| **BBC Sound Effects (RemArc)** | RemArc Licence | **No** (personal, educational, research only) | **No** | Required per licence | No commercial use; no political/social campaigning or fundraising; commercial licence sold separately | [S23] (official site could not be fetched; secondary sources) |
| **Roblox Creator Store audio** | Roblox licensed catalog | Not verified; assume no | Yes, inside Roblox experiences | n/a | Stays public in Roblox [S7] | [S7][S8] |

Decision rules (practice, inferred from the licenses above):
1. Monetized YouTube, fastest safe path: YouTube Audio Library SFX, then Kenney
   (CC0), Freesound CC0, Pixabay, Sonniss.
2. Freesound: accept only CC0 or CC-BY for anything monetized. Reject CC-BY-NC and
   Sampling+.
3. Games: Kenney, Freesound CC0/CC-BY, Pixabay, Sonniss are all fine *inside* a
   shipped game. Do not publish their raw files as a free public asset (for example
   a public Roblox Creator Store sound): that looks like the standalone
   redistribution the Sonniss and Pixabay licenses forbid. Keep those uploads
   private to your experience.
4. BBC RemArc: never for monetized videos or commercial games.
5. Never feed Sonniss sounds to AI training or audio-generation tools [S18].
6. Credits log fields: file name, source URL, author, license (with version),
   date downloaded, attribution string, where used.

---

## 9. Sources (all checked 2026-09-26)

- [S1] EBU R 128 page, v5.0 (Nov 2023): https://tech.ebu.ch/publications/r128
- [S2] Wikipedia, EBU R 128 (summary of R128 and ATSC A/85 values):
  https://en.wikipedia.org/wiki/EBU_R_128
- [S3] AES TD1008 v3.13, "Recommendations for Loudness of Internet Audio Streaming
  and On-Demand Distribution" (2021):
  https://aes.org/wp-content/uploads/2024/01/20210924_TD1008_v3.13.pdf
- [S4] Netflix Sound Mix Specifications and Best Practices v1.6:
  https://partnerhelp.netflixstudios.com/hc/en-us/articles/360001794307-Netflix-Sound-Mix-Specifications-Best-Practices-v1-6
- [S5] Production Advice, "YouTube Stats For Nerds" (2017):
  https://productionadvice.co.uk/stats-for-nerds/
- [S6] Search-result consensus on -14 LUFS (e.g. Frame.io workflow guide):
  https://workflow.frame.io/guide/loudness-for-youtube
- [S7] Roblox DevForum, "[Action Needed] Upcoming Changes to Asset Privacy for Audio":
  https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697
- [S8] Roblox Creator Hub, Audio assets: https://create.roblox.com/docs/audio/assets
- [S9] Roblox Creator Hub, Asset privacy: https://create.roblox.com/docs/projects/assets/privacy
- [S10] Roblox Creator Hub, Audio objects: https://create.roblox.com/docs/audio/objects
- [S11] Roblox DevForum, "Roblox Audio API Exits Beta" (Sept 10, 2024):
  https://devforum.roblox.com/t/roblox-audio-api-exits-beta-enhanced-sound-controls-now-available/3153454
- [S12] Roblox AudioFader reference and DevForum Audio API threads (search results):
  https://create.roblox.com/docs/reference/engine/classes/AudioFader ;
  https://devforum.roblox.com/t/new-audio-api-features-directional-audio-audiolimiter-and-more/3282100
- [S13] Roblox Creator Hub, SoundService reference:
  https://create.roblox.com/docs/reference/engine/classes/SoundService
- [S14] Audiokinetic Wwise-251 course, Playback Limits / voice management:
  https://www.audiokinetic.com/en/courses/wwise251/?id=Lesson5_Playback_Limits/
- [S15] The Game Audio Co., "Vertical Layering vs. Horizontal Resequencing", and
  Wikipedia "Adaptive music":
  https://www.thegameaudioco.com/making-your-game-s-music-more-dynamic-vertical-layering-vs-horizontal-resequencing ;
  https://en.wikipedia.org/wiki/Adaptive_music
- [S16] MDN, Web Audio API best practices:
  https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices
- [S17] Freesound FAQ (licenses): https://freesound.org/help/faq/
- [S18] Sonniss, "The License - #GameAudioGDC Bundle": https://sonniss.com/gdc-bundle-license/
- [S19] Kenney support/FAQ: https://kenney.nl/support
- [S20] YouTube Help, Audio Library: https://support.google.com/youtube/answer/3376882
- [S21] Pixabay License Summary: https://pixabay.com/service/license-summary/
- [S22] Pixabay Terms / Content License: https://pixabay.com/service/terms/
- [S23] BBC Sound Effects RemArc licence, via CDM
  (https://cdm.link/bbc-gives-away-16k-wav-sound-effects-disallows-using/) and the
  Renoise forum summary; official page https://sound-effects.bbcrewind.co.uk/licensing
  refused automated fetch on 2026-09-26.

---

## 10. Known gaps (as of 2026-09-26)

- YouTube publishes no official LUFS target; -14 LUFS rests on third-party
  measurement [S5][S6]. TikTok, Instagram and Shorts targets were not found.
- ATSC A/85 true-peak value not verified at the primary source.
- Pixabay: no audio-specific Content ID or game clause found in the pages fetched.
  Some Pixabay music is reported to trigger Content ID claims (not verified); SFX
  risk is lower but check.
- YouTube Audio Library: use outside YouTube (games, TikTok) not covered by the page
  checked.
- Roblox Creator Store licensed audio: off-platform use terms not checked.
- Roblox docs did not state whether legacy Sound and the Audio API can share one mix
  bus; treat them as separate paths.
- BBC RemArc terms come from secondary sources (official page blocked fetch).
- The SFX taxonomy, density counts, relative mix levels and sync timings are editing
  convention (practice, inferred); no published standard exists for them.
