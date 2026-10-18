# VFX, transitions, motion design and colour, mapped to mood and genre

Status: v2 (2026-09-26). Web sources were checked on 2026-09-26; the key is at the end
(`[S#]` = web, `[L#]` = HyperFrames skill file). Claims with no tag are marked
**practice (inferred)**: editing convention or arithmetic, not a measured finding.

## How to use this chapter

1. Find the genre in section 6. It names a primary transition, camera moves, type style and look.
2. Look each named effect up in sections 1-4 for its duration and build recipe.
3. Before rendering, run the section 7 checklist.

Working assumptions for HyperFrames: one paused GSAP timeline, seek-safe, 30 fps. Nothing
may call `Math.random()` or run a live physics step at render time; pre-seed every "random"
value [L2]. Frame maths at 30 fps: 1f = 33.3 ms, 3f = 0.1 s, 6f = 0.2 s, 9f = 0.3 s,
15f = 0.5 s, 30f = 1 s.

### The one rule above all the others

Leave an effect out unless it does a job the viewer would miss. Apple's HIG says to add
motion purposefully, warns that gratuitous animation distracts, and prefers quick, precise
animations [S3]. Walter Murch ranks a cut's priorities as emotion (51%), story (23%) and
rhythm (10%), with eye trace and spatial continuity below them [S19]. An effect that serves
none of the top three is decoration.

---

## 1. Transitions taxonomy

### 1.1 Cut versus transition: resolve the two rules

- **Footage edits** (talking heads, gameplay, b-roll, podcasts): the hard cut is the default.
  Film shots have become steadily shorter, from about 12 s in the 1950s to under 4 s in the
  2000s [S15], and almost all of those changes are plain cuts. Other transitions are
  accents. **practice (inferred)** for the "almost all" part.
- **Motion-graphics compositions** (explainers, title sequences, animated scenes): the
  HyperFrames skill requires a transition between every scene and bans exit animations
  except on the final scene; the transition itself is the exit [L1]. Pick one primary
  transition for 60-70% of scene changes plus 1-2 accents, and never a new transition per
  scene [L1].

### 1.2 Table

Frame counts are totals at 30 fps. Where [L1] is cited, the energy-band durations come from
it: calm 0.5-0.8 s, medium 0.3-0.5 s, high 0.15-0.3 s [L1]. Genre fit, overuse failures
and recipes are **practice (inferred)** unless tagged.

| Transition | Narrative job | Frames @30 | Uses it | Avoids it | Overuse failure | One-line build |
|---|---|---|---|---|---|---|
| Hard cut | "Next." Invisible when it lands on action or on a sentence boundary | 0 | Every genre | None | Rarely the cut itself; bad cuts are bad timing | Clip B `data-start` = clip A end. No tween |
| Match cut | Links two things through shared shape, motion or sound [S16] | 0, or 6-12 if a matched move carries across | Documentary, explainer, VFX Shorts, storytime | Fast news | Every section joined by a "clever" match; reads as a trick | Place both subjects at the same centre and scale; cut on the frame the shapes line up; optionally continue one `x/scale` tween across the cut |
| J cut / L cut | J: next scene's audio starts before its picture [S17]. L: previous audio runs on under the new picture. Smooths speech, pulls the viewer forward | Audio offset 8-30 | Documentary, podcast clips, true crime, interviews | Beat-synced edits, where music owns the audio | Offsets on every cut blur who is speaking | J: set B's audio `data-start` 0.3-1 s before B's video. L: extend A's audio clip past A's video |
| Whip pan | Fast place or time jump, "meanwhile", energy; the blur hides the cut [S16] | 6-12 (3-6 each side) | Travel, challenge, gaming, tech b-roll, VFX Shorts | Calm/faith, most true crime | Seasick montage; direction flips between cuts | At time T: A `xPercent:0→-100, filter:blur(0→24px)`, `power2.in`, 0.2 s; B `xPercent:100→0, blur 24→0`, `power2.out`, same T |
| Zoom-through | Momentum "into" the next idea | 6-15 | Velocity edits, promos, gaming, tech hype | Calm, documentary, true crime | Every change zooms; motion sickness; template look | A `scale:1→1.6, opacity:1→0, blur 0→10px` `power3.in`; B `scale:0.7→1` `power3.out` at the same T |
| Spin | Playful disorientation, "flip the script" | 8-15 | Kids, comedy Shorts, gaming Shorts | Documentary, true crime, faith, tech review | Reads as an old wedding-video preset | Wrapper `rotation:0→180` + blur; swap scenes at the midpoint; B `rotation:-180→0`; `power2.inOut` |
| Glitch | Digital breakdown, error, tension | 3-8 | Tech news, gaming, horror or true-crime accents, VFX Shorts | Calm, kids, cooking | Constant glitching becomes wallpaper and hurts reading | 3 copies, RGB offset `x:±6px`, `mix-blend-mode:screen`, `clip-path:inset()` slices keyed on `steps(1)` with pre-seeded values [L1 lists glitch for tech and tense moods] |
| Light leak | Warmth, memory, a soft section change | 15-30 | Vlog, faith, cooking, nostalgic storytime | Clinical tech, news | Every cut washed orange | Radial-gradient div (amber to magenta), `mix-blend-mode:screen`, opacity 0→0.9→0 `sine.inOut`; cut under the peak [L1 maps light leak to warm and retro moods] |
| Film burn | Analog "end of reel", raw emotion | 12-24 | Music video, nostalgic, indie doc, VFX Shorts | Corporate, kids education | Cheesy outside an analog look | Burn overlay clip in `screen`, or a canvas noise field thresholded by a rising `progress` and mapped through a warm colour ramp |
| Luma / gradient wipe | Smooth, organic scene change | 12-24 | Brand, explainer, documentary | Fast Shorts | Becomes the "premium template" tell | CSS `mask-image:linear-gradient(...)` with animated `mask-position`, or a shader `progress` uniform against a luma texture [L4 "Clip/mask reveal", "Shader uniform"] |
| Mask / iris | Point the eye at one spot; open onto or close on a subject | 12-20 | Kids, retro, explainer, comedy | Documentary, true crime | Cartoon feel on a serious story | `clip-path:circle(0% at X Y)` → `circle(150% at X Y)`, `power3.inOut` |
| Shape wipe | Section divider in brand colour | 10-18 | Explainer, tech review, kids, fast facts | Calm, true crime | Brand slabs on every cut | Full-frame rect `scaleX:0→1` origin left; swap under it; `scaleX:1→0` origin right; `expo.inOut` |
| Morph | One thing becomes another: cause and effect, transformation | 15-30 | Explainer, science, data viz, logo reveals | Talking-head formats | Morphing between unrelated shapes | MorphSVG for silhouettes, FLIP for one element changing box [L4 "Shape interpolation", "Shared element"] |
| Dip to black | Time passes, a chapter closes, weight | 8-15 out + 8-15 in | Documentary, true crime, faith, film | Shorts (it spends seconds of attention) | A long video that keeps "ending" | Black div `opacity 0→1` `power1.in`, swap, `1→0` `power1.out`. [L1: outro uses the slowest, simplest transition, 0.6-1.0 s] |
| Flash / dip to white | Shock, realisation, a beat hit; a soft dip reads as dreamy | 2-6 flash; 8-15 soft dip | Velocity edits, gaming, challenge; soft dip in vlogs | True crime unless deliberate | Strobing; seizure risk | White div `opacity 0→1` in 2f, hold 0-2f, `1→0` in 4-8f `power2.out`. Max 3 flashes in any 1 s window [S18] |
| Smash cut | Abrupt contrast: chaos to calm, loud to silent, crowd to alone [S16] | 0 | Comedy, challenge, storytime, horror, gaming | Calm, faith | Loses its shock when every cut smashes | Hard cut on the loudest frame or into sudden silence; optionally one 1f white frame or a punch-in |

### 1.3 Placement rules

| Position in the video | Pick | Source |
|---|---|---|
| Opening | The most distinctive transition you will use; it sets the language (0.4-0.6 s) | [L1] |
| Between points of one section | Hard cut (footage) or the primary transition (graphics), ~0.3 s | [L1] |
| Section change | Something visibly different from the primary: dip, shape wipe, whip | [L1] |
| Climax or reveal | The boldest accent, used once | [L1] |
| Wind-down and outro | Back to gentle; outro slowest and simplest, 0.6-1.0 s | [L1] |

Photosensitivity guard: never more than three flashes, or three red flashes, in any
one-second window. A flash is a pair of opposing luminance changes of 10% or more; the
area limit is 25% of a 10-degree field [S18]. Beat-synced white flashes on a fast track
break this easily; when the beat is faster than 3 per second, flash on every other beat.

---

## 2. Camera moves on a 2D frame

| Move | Job | Numbers | HyperFrames build |
|---|---|---|---|
| Punch-in (jump-cut zoom) | Hides a jump cut on a talking head; lands a key line or punchline | Keep digital scale-ups to 110-120% to avoid visible softness [S7]. Alternate 100% and ~115% across cuts; go to ~130% only from 4K source. **practice (inferred)** for the alternation and 130% | Crop wrapper around the video. Hard punch: `tl.set(wrap,{scale:1.15, transformOrigin:"50% 35%"}, cutTime)` (origin near the eyes). Smooth push: 0.3-0.5 s `power2.out` [L3 "Punch-in / punch-out"] |
| Ken Burns | Life in stills: photos, documents, archival | 100% to 110-115% over a 5-10 s hold, with a small pan. **practice (inferred)** | `scale:1→1.12, xPercent:0→-3`, `sine.inOut` or `none` [L2 lists `sine` for Ken Burns]. Do not end mid-acceleration on the cut |
| 2.5D parallax | Depth from one flat photo; documentary archive, storytime | Foreground travels 1.5-3x the background; total travel 3-8% of frame width. **practice (inferred)** | Separate subject and background (the CLI has `remove-background`), stack the layers, move `x` at different rates; for true depth put `perspective` on the parent and move `z` [L3: scale alone is fake depth] |
| Screen shake | Impact: hit, explosion, bass drop, reveal | Drive it from a "trauma" value 0-1 that decays; displacement ∝ trauma², sampled from smooth noise, not white noise [S11]. Amplitude at 1080p: light 4-8 px, heavy 15-30 px; decay over 6-12f. Keep shake frequency under 15 Hz, because at 30 fps anything faster aliases. **practice (inferred)** for px and Hz | Pre-bake: `keyframes:[{x:12,y:-8,rotation:0.6},{x:-9,y:6},{x:5,y:-3},{x:-2,y:1},{x:0,y:0,rotation:0}]`, 0.25-0.4 s, `ease:"none"`. For longer shakes, sum two or three sines of different frequencies times `(1-t)²` |
| Speed ramp | Stretch the good moment, rush the dull part, land on a beat | Build in three phases (approach, focus, exit) with about four or five purposeful control points, not a preset's dozen [S9]. Common creator pattern: 1x → 1.5-3x → 0.2-0.5x on the hit → 1x. **practice (inferred)** for the multipliers | Pre-render the ramp with ffmpeg (`setpts` per segment, `minterpolate` or frame blending for slow parts), then place the result as one clip. Add a motion-blur streak on the fast part [L5 motion-blur-streak] |
| Dolly zoom (vertigo) | A realisation, dread, the world tilting | 1-3 s. The subject holds size while the background grows or shrinks. **practice (inferred)** | 2D: subject layer constant while background `scale:1→1.4` (or reverse). 3D (Three.js): change FOV and camera distance together so `distance × tan(fov/2)` stays constant, which keeps the subject's size fixed (geometry) |

Decision rules (**practice (inferred)**):
- One camera move per shot. A Ken Burns under a punch-in under a shake is three moves fighting.
- Punch on meaning (the claim, the joke, the number), never on a timer. Creator guidance on
  zoom jump cuts makes the same point: place them at key lines, not randomly [S8].
- A zoom that ends exactly as the next cut starts reads as unfinished; let it settle 4-6f first.

---

## 3. Motion principles for graphics

### 3.1 Disney's principles, translated for video graphics

| Principle | What it means on a graphic | Default | Source |
|---|---|---|---|
| Slow in / slow out | Nothing starts or stops at full speed except mechanical motion | Decelerate on entry, accelerate on exit | [S1], [L2] |
| Anticipation | A small counter-move before a big one, which primes the eye | 3-6f back 5-8 px or scale 0.95 before a hero move; skip on text lines | UI adaptation [S4]; numbers **practice (inferred)** |
| Follow-through / overlapping action | Secondary parts land after the main body | Card lands, then its label and shadow 2-4f later | Secondary element delayed behind primary [S4]; frames **practice (inferred)** |
| Overshoot (squash and stretch, softened) | Travel past the target, settle back | 1-1.5% overshoot is "felt, not seen"; 5-10% is the playful register | [L2 spring table] |
| Staging | One focal point at a time | Dim or blur the rest while one element speaks | **practice (inferred)** |
| Timing | Duration carries weight: heavy things move slower | See 3.3 | [S1] |
| Arcs | Natural paths curve | Use MotionPath for travel over ~20% of the frame | [L4 "Path travel"] |
| Exaggeration | Push only the beat that matters | One hero exaggeration per scene | **practice (inferred)** |

### 3.2 Easing

Material 3's tokens pin the directional rule: decelerate curves for elements entering,
accelerate curves for elements leaving, standard curves for things that start and end on
screen [S1]. Its values: standard `cubic-bezier(0.2,0,0,1)`, standard decelerate `(0,0,0,1)`,
standard accelerate `(0.3,0,1,1)`, emphasized decelerate `(0.05,0.7,0.1,1)`, emphasized
accelerate `(0.3,0,0.8,0.15)` [S1].

| GSAP ease | Character | Use | Avoid |
|---|---|---|---|
| `power3.out` (HyperFrames house default), `power4.out` | Fast launch, long settle | Entrances: titles, cards, lower thirds [L2] | Exits |
| `expo.out` | Sharper settle; close to M3 emphasized decelerate. **practice (inferred)** | Hero reveals, premium brand, punchy entrances [L2] | Calm pieces |
| `power2.in`, `power3.in` | Accelerates away | Exits and the outgoing half of a transition [S1 rule] | Entrances |
| `sine.inOut`, `power1.inOut` | Symmetric and calm | Crossfades, drifts, loops, Ken Burns [L2] | Beat hits |
| `expo.inOut`, `power4.inOut` | Snappy and dramatic | Fast scene transitions in high-energy edits [L2, L1 "snappy" preset] | Calm, faith |
| `circ.inOut` | Fast middle, gentle ends | Camera moves, orbits [L2] | Text entrances |
| `back.out(1.2-1.7)`, `elastic`, `bounce` | Overshoot, spring, ball drop | Explicitly playful beats only: kids, comedy, stickers. HyperFrames calls them rare, never a default [L2] | Any serious register; as a global default |
| `none` | Linear, mechanical | Tickers, progress bars, camera drift under other motion, pre-baked shake keyframes [L2] | Entrances |
| `steps(n)` | Discrete jumps | Typewriters, counters, retro UI, glitch [L2] | Anything meant to feel smooth |

Rules:
- Use about three easing characters per video and vary them by energy inside the smooth
  families (sine/power1 calm, power3 standard, power4/expo punch). One ease everywhere is
  flat; bounce everywhere is cheap, and the second failure is worse [L2].
- To use the exact M3 curves, register them with GSAP CustomEase (it accepts cubic-bezier
  control points). **practice (inferred)**; not re-verified against GSAP docs this session.

### 3.3 Durations

M3 duration tokens, converted to frames at 30 fps: short 50-200 ms (1.5-6f), medium
250-400 ms (7.5-12f), long 450-600 ms (13.5-18f), extra-long 700-1000 ms (21-30f) [S1].

| Element | Enter | Exit | Basis |
|---|---|---|---|
| Small element: icon, chip, bullet, sticker | 6-9f (0.2-0.3 s) | 4-6f | M3 short/medium tokens [S1]; mapping **practice (inferred)** |
| Title, lower third, card, panel | 12-21f (0.4-0.7 s) | 9-15f | M3 long/extra-long [S1]; mapping **practice (inferred)** |
| Full-frame scene transition | Energy band in section 1 | same | [L1] |
| Calm or luxury register | Up to 24-30f | 15-24f | [L1] calm band; [S1] extra-long |

Rules (**practice (inferred)**): exits run 20-30% shorter than entrances, and in HyperFrames
multi-scene work, exits happen only in the final scene [L1]. Video can run a little slower
than app UI because nobody is waiting to tap, but nothing the viewer must read should take
under 6f to arrive.

### 3.4 Stagger

| Unit | Gap between items | Cap |
|---|---|---|
| Characters | 0.02-0.04 s | Whole word in ≤ 0.4 s |
| Words | 0.06-0.12 s | Whole line in ≤ 0.8 s |
| List items, cards | 0.08-0.15 s | Last item lands within ~0.8-1.0 s of the first |

All **practice (inferred)**. The cap matters more than the gap: a 12-item list at 0.15 s
takes 1.8 s to assemble, which is too long, so shrink the gap or group the items.

### 3.5 Reading hold time

| Standard | Rate | Source |
|---|---|---|
| BBC subtitles | 160-180 words per minute (2.7-3 words/s); about 0.3 s per word minimum, so 4 words ≈ 1.2 s | [S5] |
| Netflix English | Max 20 characters/s for adults, 17 for children's content | [S6] |
| Netflix general | Each subtitle event on screen from 5/6 s up to 7 s | [S6] |

Hold rules for on-screen text:
- Text not spoken aloud: `hold = max(1.5 s, words × 0.35 s)` after the entrance finishes;
  for kids' content use `words × 0.45 s`. Derived from [S5] and [S6]; the formula is
  **practice (inferred)**.
- Text that repeats the voiceover (captions, keyword pops) may follow the voice, but no
  single caption flashes up for less than 5/6 s unless it is one word synced to speech [S6].
- A big number or stat needs one read plus one beat to land: at least 1.5-2 s.
  **practice (inferred)**

### 3.6 Kinetic typography styles

| Style | Mood | Genres | Build |
|---|---|---|---|
| Word-by-word karaoke captions | Pace, retention | Shorts, podcast clips, storytime | Split words; highlight the active word; `scale 0.92→1` over 3-4f `power3.out` |
| Beat slam | Aggression, emphasis | Hype, gaming, velocity edits | Word `scale 1.6→1` in 3f `expo.out` + 1f flash + small shake [L5 kinetic-beat-slam] |
| Masked line reveal | Premium, editorial, calm authority | Documentary, brand, explainer | Line wrapper `overflow:hidden`; inner `yPercent:100→0` `power3.out`, words staggered 0.08 s |
| Typewriter | Documents, suspense, terminals | Tech, true crime, news | `steps(n)` on a char reveal; blinking caret |
| Scramble / decode | Hacking, mystery, reveal | Tech news, gaming | Pre-seeded character cycles on `steps` |
| Gentle fade and drift | Reflection, stillness | Faith, calm, documentary | `opacity 0→1, y:12→0`, 0.8 s `sine.out` |
| Gradient sweep | Brand shine on one word | Tech launch, premium | Once per video at most [L5 gradient-text-sweep]; see section 7 |

HyperFrames ships 24 named text effects [L6]; check them before hand-building.

---

## 4. Colour and look by mood

Source key for this section: teal-orange rationale [S12], bleach bypass [S13], film grain
filter [S14]. Filter values are starting points, **practice (inferred)**; grade against a
reference frame, not by eye alone.

| Look | Mood | Fits | Avoid | Fake it |
|---|---|---|---|---|
| Teal-orange | Blockbuster energy; skin pops because skin sits in the orange range and orange is near-complementary to teal [S12] | Challenge, travel, hype, VFX Shorts | Calm, kids, faith | Teal layer (`#0d4f5c`) at 0.25-0.35 in `soft-light` over footage, masked to shadows with a luminance mask; or SVG `feComponentTransfer` lifting blue in the low range and red in the high range |
| Bleach bypass / desaturated | Grit, bleakness, war-report realism: reduced saturation, higher contrast, heavier grain, crushed blacks [S13]. Saving Private Ryan used heavy silver retention [S13] | True crime, war and history docs, gritty drama | Kids, cooking, faith | `filter: saturate(0.45) contrast(1.3) brightness(0.95)` + grain at 0.1 |
| High-key pastel | Light, safe, friendly | Kids education, lifestyle, cooking, faith | True crime, horror | `filter: brightness(1.08) saturate(0.85) contrast(0.9)` + cream overlay in `screen` at 0.1 |
| Low-key noir | Secrets, danger, mystery | True crime, horror, mystery storytime | Kids, cooking | `grayscale(1) contrast(1.5) brightness(0.8)` or keep a single accent colour; heavy vignette |
| Warm nostalgic | Memory, comfort, home | Storytime, faith, vlog, cooking | Clinical tech | `sepia(0.25) saturate(1.1)` + amber overlay `soft-light` 0.15 + grain + halation |
| Cold clinical | Precision, sterility, unease | Tech review, science, medical, cyber | Faith, cooking | `saturate(0.8) hue-rotate(-8deg)` + blue overlay `soft-light` 0.15; clean white UI, no grain |
| Film grain | Texture, "shot on film", hides banding | Documentary, indie, nostalgic, VFX Shorts | Screen recordings, UI demos | SVG `<feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch">` [S14]; layer at 0.05-0.12, `mix-blend-mode:overlay`; change `seed` per frame from a pre-seeded list so it moves |
| Halation | Red-orange glow bleeding from highlights | Nostalgic, dreamy, music | Tech, clinical | Duplicate layer → `brightness(1.4) contrast(2)` to keep highlights → `blur(10-20px)` → tint red-orange → `screen` at 0.3-0.5 |
| VHS | 80s-90s home video, found footage, creepy | Retro gaming, horror, nostalgic storytime | Premium brand | Scanlines (`repeating-linear-gradient`, 2-3 px), RGB split 2-4 px, horizontal jitter on `steps`, `saturate(1.3) blur(0.6px)`, date stamp |
| Chromatic aberration | Glitch, tension, lens realism | Tech, gaming, horror, velocity edits | Calm, text-heavy frames | Three copies isolated to R, G, B with `feColorMatrix`, offset ±2-6 px, `screen` [L5 chromatic-glitch] |
| Vignette | Pulls the eye to the centre, adds mood | Most cinematic looks | UI screen recordings, flat explainers | `radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,.5) 100%)` overlay |
| Bloom | Dreamy, magical, heavenly, neon | Faith, fantasy, synthwave, VFX | Documentary realism | Blurred bright copy in `screen`, or Three.js UnrealBloomPass [L5 ambient-glow-bloom] |

Rules (**practice (inferred)**):
- One look per video, set at the start and held. Switching grades between sections reads as
  a mistake unless the switch means something (a flashback, an alternate timeline).
- Stack at most three texture layers (for example grade + grain + vignette). Every added
  overlay costs render time and legibility.
- Text and UI sit above the grade and grain layers, never under them.
- Before building any named look, search the HyperFrames registry: it ships ready blocks for
  CRT, glitch, grain and chromatic aberration [L7].

---

## 5. "Aesthetic" and "velocity" edits

### 5.1 What they are made of

| Ingredient | What it does | Build note |
|---|---|---|
| Speed ramp | The core move: approach, focus, exit, with about four or five control points [S9] | Pre-render the ramp (section 2) |
| Beat sync | Speed changes and hits land on the loudest musical moments [S10]; the slow point goes on the action, not just the nearest beat marker [S9] | Run the HyperFrames `beats` command on the track, then place hits on real action frames near the beats |
| Flashes | Mark the drop or the hit [S9] | 2-6f white flash; three-per-second cap [S18] |
| Shake | Adds energy on fast parts [S9, S10] | Pre-baked decaying keyframes (section 2) |
| Zoom and zoom-blur | Focus on the key moment [S10] | `scale` + radial or directional blur for 3-6f |
| Motion blur | Makes the speed changes read as smooth [S10] | Blur streak layer or frame blending in the pre-render |
| Presets people copy | Flash, fade blur, blur shake, retro zoom [S10] | Avoid named presets as-is; see 5.3 |
| Masks and text reveals | "Aesthetic" (Pinterest-style) edits lean on soft masks, slow motion, grain, light leaks and short lowercase text lines | Masked reveal type (3.6), warm nostalgic look (4). **practice (inferred)**: no credible tutorial source found |

### 5.2 Why they hold attention

- Film has moved toward shorter shots and more on-screen motion over decades [S15]. Cutting's
  lab also found that modern shot-length patterns increasingly resemble the 1/f fluctuation
  found in human attention [S15].
- Beat sync lets sound predict the picture: the viewer anticipates the drop and gets a visual
  payoff on it. **practice (inferred)**
- Speed variation builds contrast, and contrast is what the eye tracks: fast then slow
  frames the slow moment as the important one. **practice (inferred)**

### 5.3 Where it becomes noise

| Failure | Sign | Fix |
|---|---|---|
| Every beat gets a hit | Motion feels "mechanically pulsed"; repeated peaks without repeated action [S9] | Hit the downbeats of phrases and the drop; leave the rest clean |
| Effects hide a bad ramp | Flashes and shakes piled on a jerky curve [S9] | Lock the ramp first, then add effects [S9] |
| No time to read the motion | The viewer never sees what happened [S9] | Hold the slow point for 8-15f. **practice (inferred)** |
| Flash strobing | More than 3 flashes/s | Cap per [S18] |
| Effects on informational content | Captions, numbers or UI shaking | Keep text and data still; move the footage under them. **practice (inferred)** |
| Transitions on every cut | Template-pack look | 1-2 showy transitions per 15 s Short is one creator guideline [S20, low-credibility source]; treat it as a ceiling |

Decision rule: use the velocity style only when the footage has real motion and the track
has a clear beat (sport, gameplay, cars, dance, travel, VFX). Never use it on talking heads,
data explainers, true crime or calm/faith content. **practice (inferred)**

---

## 6. Genre defaults

All rows are **practice (inferred)** starting points, built from the sections above. The
research brief's per-niche video analysis should confirm or overturn them; where it
disagrees, it wins.

| Genre | Transitions | Camera | Type and graphics | Look | Leave out |
|---|---|---|---|---|---|
| Documentary / video essay | Hard cuts, J/L cuts, dip to black between chapters, rare match cut | Ken Burns and 2.5D parallax on archive stills; slow push-ins | Masked line reveals, map and date cards, `power3.out`/`sine` | Mild grain, vignette, warm or desaturated by topic | Zoom-throughs, spins, glitch, bounce |
| Animated explainer | One primary (push or crossfade, 0.3-0.4 s) + morphs and shape wipes for section changes | Camera pans across one large canvas between stations | Staggered builds, path draws, morphs; `power3.out`, rare `back.out` | Flat brand palette, no grain | Film burn, VHS, shake |
| Science entertainment | Hard cuts, whip or zoom accents on reveals, smash cut to results | Punch-ins on reactions and results; speed ramp on the test | Callouts, arrows, measurement readouts, slow-mo replays with labels | Clean, bright, slight teal-orange outdoors | Heavy grading that hides the real result |
| Challenge / spectacle | Fast hard cuts, smash cuts, whip pans, flash on reveals | Punch-ins every few lines, shake on impacts, speed ramps | Big bold captions, counters, stakes on screen | Saturated teal-orange | Slow dissolves, dips to black |
| Tech review | Hard cuts, short shape wipes between sections | Slow product orbits and pushes (sine), macro Ken Burns | Clean spec cards, masked reveals, `expo.out` | Cold clinical, dark backdrops, subtle bloom on the product | Glitch spam, film burn, bounce |
| Fast tech news | Hard cuts, short glitch or whip accents on topic change | Punch-ins on the host, quick zooms onto screenshots | Headline slams, typewriter source cards, tickers | Cold or neutral, light chromatic accents | Dips to black, long transitions |
| Gaming commentary | Hard cuts on the jokes, smash cuts, occasional zoom-through | Punch-ins on gameplay moments, shake on hits, freeze frames | Meme captions, beat slams, arrows and circles | Game's own colours; VHS or CRT for retro titles | Clinical polish, slow crossfades |
| True crime | Hard cuts, J/L cuts, dip to black, rare smash cut | Slow push-ins, Ken Burns on photos and documents | Typewriter documents, redaction bars, dates, gentle fades | Desaturated or low-key noir, grain, vignette | Bounce, spins, bright flashes, playful eases |
| Cooking | Hard cuts on action, match cuts between steps, light leak rarely | Top-down Ken Burns, speed ramps on long processes, macro slow-mo | Soft ingredient and quantity labels, `power2.out` | Warm, high-key, saturated food colours | Glitch, heavy shake, cold grades |
| Kids education | Iris, shape wipes, spins in moderation | Gentle zooms onto the thing being taught | Big rounded type, `back.out` allowed, longer holds (`words × 0.45 s`) | High-key pastel, bright primaries | Glitch, flashes, shake, dark looks |
| Calm / faith | Long crossfades, soft light leaks, dip to black or white | Very slow Ken Burns and drifts (`sine.inOut`) | Gentle fade and drift, long holds, serif or soft sans | Warm, bloom, halation, soft vignette | Anything fast: whips, glitch, shake, slams |
| Fast-facts Shorts | Hard cuts every 1-2 s, occasional zoom-through or flash on the payoff | Punch-ins, fast Ken Burns on stills | Karaoke captions, number counters, pop-in images | Saturated, high contrast | Dips to black, long intros |
| Gaming Shorts | Hard cuts, whip pans, zoom-throughs on highlights | Punch-ins, shake, speed ramps, freeze frames | Beat slams, meme text, arrows | Game colours, chromatic accents on hits | Slow transitions, long holds |
| Podcast clips | Hard cuts between speakers; J/L cuts | Punch-in alternation 100% / ~115% on key lines [S7] | Karaoke captions, speaker name tags, a keyword pop | Neutral, the room's own colour | Transitions between speakers, shake, glitch |
| VFX Shorts | Match cuts and whip pans that hide the effect; one flash or burn | Speed ramps, dolly zoom, shake on impact | Minimal text; the effect is the content | Teal-orange or film look, grain, halation | Captions over the effect, busy overlays |
| Animated storytime | Hard cuts on dialogue beats, iris or dip for scene changes | Slow pushes, parallax on backgrounds | Karaoke captions, speech bubbles, emphasis slams on punchlines | Warm or pastel; noir for spooky stories | Velocity-edit tricks, glitch spam |

---

## 7. Anti-slop: motion tells that look generic

| Tell | Why it reads as template or AI-made | Do instead |
|---|---|---|
| Every element bounces or pops in | Overshoot everywhere is the cheapest-reading failure [L2] | `power3.out` or a critically damped spring by default; keep `back.out` for one playful beat [L2] |
| One ease on everything | Motion becomes flat and uniform [L2] | Three easing characters, chosen by energy [L2] |
| A different transition on every scene | No visual language [L1] | One primary for 60-70% of changes plus 1-2 accents [L1] |
| Constant slow zoom on every shot | Nothing is emphasised when everything moves | Hold still shots still; push only on the beats that matter. **practice (inferred)** |
| Gradient text on every heading | Reads as a template and hurts contrast | Solid type in one accent colour; one gradient sweep per video at most. **practice (inferred)** |
| Everything staggers in, every time | The viewer waits for layouts to assemble | Stagger only the first build of a layout; later changes cut or swap in place. **practice (inferred)** |
| Glitch, shake and flash with no trigger | Effects detached from sound and story | Tie every impact effect to an audio event or a story beat. **practice (inferred)** |
| Decorative motion under text | Competes with reading; Apple's HIG calls gratuitous animation distracting [S3] | Freeze or dim the background while text holds |
| Flashes on every beat | Noise, and a seizure risk past 3/s [S18] | Phrase downbeats and drops only |
| Stock look presets stacked (grain + leak + VHS + aberration) | Texture soup | One look, at most three texture layers (section 4) |
| Entrance with no exit logic | Elements pile up and the frame clutters | Plan what leaves; in multi-scene HyperFrames work, the transition is the exit [L1] |
| Motion as the only carrier of meaning | Viewers who skim or mute miss it | Pair motion with text or voice; Apple's HIG says to make motion optional [S3] |

Pre-render checklist:
1. Can you name the job of every transition and effect in one phrase? Cut the rest.
2. Is there one primary transition, one look, and three easing characters?
3. Does every piece of on-screen text meet the hold rule in 3.5?
4. Are there more than 3 flashes in any 1 s window? [S18]
5. Does anything move under text while the viewer is reading?

---

## Source key

Web sources, all checked 2026-09-26. Entries marked "via search summary" were read through
a search tool's summary of the page, not a direct fetch.

| Key | Source | URL |
|---|---|---|
| S1 | Material Components (Android), Motion theming doc: M3 easing and duration tokens | https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md |
| S3 | Apple Human Interface Guidelines, Motion (via search summary) | https://developer.apple.com/design/human-interface-guidelines/motion |
| S4 | IxDF, applying Disney's 12 principles to UI; UX Collective, the same topic (via search summary) | https://ixdf.org/literature/article/ui-animation-how-to-apply-disney-s-12-principles-of-animation-to-ui-design ; https://uxdesign.cc/disneys-12-principles-of-animation-exemplified-in-ux-design-5cc7e3dc3f75 |
| S5 | Clevercast summary of the BBC subtitle guidelines (via search summary; bbc.co.uk could not be fetched) | https://www.clevercast.com/bbc-subtitling-guidelines/ |
| S6 | Netflix Partner Help Center, English (USA) Timed Text Style Guide and General Requirements (via search summary) | https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide ; https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements |
| S7 | EditingCorp, tricks to hide jump cuts (via search summary) | https://www.editingcorp.com/video-editing-tricks-to-hide-jump-cuts/ |
| S8 | Katie Steckly, zoom jump cut explainer (TikTok, via search summary) | https://www.tiktok.com/@katiesteckly/video/7354004424777288965 |
| S9 | CapCut Guide, velocity edit: speed curve and beat sync (fetched) | https://capcutguide.com/capcut-velocity-edit/ |
| S10 | CapCut, how to do velocity (via search summary) | https://www.capcut.com/resource/how-to-do-velocity-on-capcut |
| S11 | Squirrel Eiserloh, GDC 2016 "Juicing Your Cameras With Math" (via search summary) | http://www.mathforgameprogrammers.com/gdc2016/GDC2016_Eiserloh_Squirrel_JuicingYourCameras.pdf |
| S12 | Adobe, why use orange and teal grading; PetaPixel on the look (via search summary) | https://www.adobe.com/creativecloud/video/hub/features/why-use-orange-teal-grading.html ; https://petapixel.com/2017/02/23/orange-teal-look-popular-hollywood/ |
| S13 | Boris FX, bleach bypass guide; American Cinematographer on Saving Private Ryan (via search summary) | https://borisfx.com/blog/what-is-bleach-bypass-complete-guide-film-technique/ ; https://theasc.com/magazine/nov98/soupdujour/pg2.htm |
| S14 | CSS-Tricks, Grainy Gradients (via search summary) | https://css-tricks.com/grainy-gradients/ |
| S15 | James Cutting et al., shot structure and the evolution of Hollywood film; attention and 1/f shot patterns (via search summary) | https://jov.arvojournals.org/article.aspx?articleid=2138011 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3485803/ ; http://cutting.psych.cornell.edu/curresearch.htm |
| S16 | StudioBinder, types of editing transitions; match cuts (via search summary) | https://www.studiobinder.com/blog/types-of-editing-transitions-in-film/ ; https://www.studiobinder.com/blog/match-cuts-creative-transitions-examples/ |
| S17 | Wikipedia, J cut (fetched) | https://en.wikipedia.org/wiki/J_cut |
| S18 | W3C, Understanding WCAG 2.1 SC 2.3.1 Three Flashes or Below Threshold (fetched) | https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html |
| S19 | StudioBinder, Walter Murch's Rule of Six (via search summary) | https://www.studiobinder.com/blog/walter-murch-rule-of-six/ |
| S20 | Goodreads author blog, TikTok transitions (low credibility; via search summary) | https://www.goodreads.com/author_blog_posts/24175131-how-to-do-transitions-on-tiktok |

HyperFrames skill references (read 2026-09-26, HyperFrames 0.8.77):

| Key | File |
|---|---|
| L1 | `hyperframes-animation/transitions/overview.md` |
| L2 | `hyperframes-animation/adapters/gsap-easing-and-stagger.md` |
| L3 | `hyperframes-keyframes/SKILL.md` |
| L4 | `hyperframes-keyframes/references/keyframe-patterns.md` |
| L5 | `hyperframes-animation/rules/` (chromatic-glitch, kinetic-beat-slam, ambient-glow-bloom, motion-blur-streak, gradient-text-sweep); file names seen, contents not read |
| L6 | `hyperframes-animation` skill description (24 named text-animation effects) |
| L7 | `hyperframes-registry` skill description (registry covers CRT, glitch, grain, chromatic aberration) |

## Known gaps

- Apple HIG, BBC, Netflix and most film-craft sources were read through search summaries,
  not full-page fetches. Re-fetch them before quoting numbers in public material.
- No credible source was found for the Pinterest "aesthetic edit" style, or for the claim
  that velocity edits raise retention. Both are practice (inferred).
- Frame counts per transition, shake amplitudes, stagger gaps and the genre table are
  convention, not measurement. The brief's per-niche video analysis should replace them
  with measured values.
- GSAP CustomEase accepting cubic-bezier strings was not re-verified.
