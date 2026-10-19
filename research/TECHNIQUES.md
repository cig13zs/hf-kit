# Technique library: how the 48 videos are edited

Cross-niche synthesis of the 16 niche sheets (`niches/*.md`, 48 videos checked 2026-09-26), the
three `knowledge/` chapters, and ideas from third-party video and audio skills (credited in
section 13). Written 2026-09-27. This is the raw material for the video skill and for `styles/*.json`.

## Bottom line
- Pace doesn't travel. Against their own control, outliers cut slower in 4 niches, faster in 4
  (each with a confound) and on either side in 5. Copy a niche's house rate when you copy its
  format; never raise the cut rate to chase views. Read section 0 before section 2.
- What recurs in outliers is script and proof, not edit surface: a person with something at
  stake (6 niches), the stake or claim said in the first seconds, evidence on screen (5 niches),
  and the title's answer held back. All hypotheses.
- Two measured leads in the audio and speech data: both outliers carry fewer music-only
  stretches than their control in 8 niches, and talk denser in the first 30 s in 8 niches.
  Both hypotheses.
- Flashy transitions are rare everywhere. 15 of 16 niches use no whip, glitch, spin or
  zoom transition as a habit (at most 1-3 accents a video). The slow styles move the camera
  inside the shot instead of cutting.
- Silence is the most shared sound device: a short drop before a reveal, after the heaviest
  line, or at a chapter end, in 12 of 16 niches. It works because it is rare.
- **Loudness didn't separate outliers** anywhere (−5.6 to −33.9 LUFS across the 48). Mix to
  −14 LUFS, −1 dBTP as the house default.

## How to read this file
| Tag | Meaning |
|---|---|
| M | Measured by `measure.py` / `audio_features.py` (numbers in `data/*.json` and the sheets) |
| S | Seen in frames or transcripts |
| I | Inferred |
| H | Hypothesis from outlier against control. Views don't prove the edit caused them |
| R | Reference chapter (`knowledge/*.md`): practice or published source, not measured here |
| recipe | A build setting from a sheet's steal list or `SPEC.md`. Design choice, not a measurement |

- Hard-cut counts are floors. Dissolves, whips, camera moves and overlays go uncounted;
  Minecraft menus add false cuts.
- Nobody listened to the audio. Sound claims come from loudness, spectrum, onset timing and
  caption tags. Onsets per minute mostly count speech syllables.
- **Tempo is unusable under narration** in all 16 niches (low confidence, per-minute readings
  swinging by 60-100 BPM). Take BPM from `knowledge/music-and-mood.md`, never from a sheet.
- One creator per niche. Every "niche" finding is one channel's house style.
- **Quotes** are at most 15 words. Every number traces to a sheet, a card or a data file.

### Video key
O = outlier, R = recent outlier, C = control.
| Niche (creator) | O | R | C |
|---|---|---|---|
| documentary (Johnny Harris) | 2r5eKpptixo | GV8KGcFqeLc | OMbV1rIPhCg |
| animated-explainer (Kurzgesagt) | 0NY2gAftzJE | _zfN9wnPvU0 | pHJIhxZEoxg |
| science-entertainment (Mark Rober) | DPZzrlFCD_I | P4gNS0Iiu0Q | 9IiYOTzJ2uw |
| challenge-spectacle (MrBeast) | KrLj6nc516A | 4l97aNza_Zc | QJI0an6irrA |
| tech-review (Marques Brownlee) | Od6M0AXpcxQ | 6D__H_DO2Xk | ANmTVYkEtLw |
| tech-news-screen (Fireship) | FluKUJyeYD8 | aspmNhKAFMc | E7la7-dtfVM |
| gaming-longform (Grian) | Qk0iCPmtLUA | 2teag5QC7NA | UjjRGyre3RY |
| storytelling-true-crime (MrBallen) | QfxhFa5hEX8 | R4G4tiPTTDM | VGiLQIzQW2Q |
| cooking (Joshua Weissman) | 3pgUFPtqJu4 | AJiGaXRsFNU | 4TyPUB6o-t8 |
| kids-education (Numberblocks) | DC-bErjbu0E | J8eVD2PpX_Q | OXjorKzZoUU |
| calm-faith (BibleProject) | 3EkD-alQhT8 | b54d_GhBthI | Q7PgVAN2MPo |
| animated-storytime (JaidenAnimations) | plSyrHqUh78 | Oc91iOxcB3c | OQx7q6mwkV4 |
| shorts-facts (Zack D. Films) | NdKRD1j9juE | p832whe8hrI | nw6LtopYGlc |
| shorts-gaming (KreekCraft) | rssMorwX9Ws | 2n1rIXEeybM | qvrxyBRhi_0 |
| shorts-podcast (The Diary Of A CEO) | 8Ho3a4bkkV8 | 0YVdjmU13E4 | -svLMqHJGaU |
| shorts-vfx (Zach King) | 5jhEoRZXhjE | X0wxLr5W2X8 | tOIFZ8O6Ezk |

"All 3" in a table means all three videos of that niche.

### hf-kit vocabulary
Blocks are the files in `blocks/`: `pill-label`, `chapter-card`, `number-card`
(`clean`|`money`), `progress-badge`, `question-card`, `doc-highlight`, `film-gate`,
`world-camera`, `ui-window`, `tier-board`, `face-banner-stack`, `zoom-through`, `blur-swap`.
Captions come from `tools/captions.py --variant cards|karaoke|speaker|keyword|punch`. SFX events
are the rows of `sound/SFX.md`. Mix presets are the sections of `sound/MIX.md`; SPEC.md's schema
spells two of them (`silence-at-heaviest-line`, `dip-before-clip`), and this file proposes ids
for the rest:

| Proposed id | `sound/MIX.md` section | Key numbers (recipe) |
|---|---|---|
| `voice-first-flat` | Voice-first flat mix | VO `1` with a 4:1 compressor; bed `0.15` (about −16 dB); LRA ≤3 LU |
| `pause-at-turn` | One pause at the turn | bed 0.15 → 0.03 at T, held 0.7 s, back by T+1 |
| `silence-at-heaviest-line` | Silence at the heaviest line | bed to 0 over 0.5 s before the line; back on the next downbeat |
| `dip-before-clip` | Dip before a loud clip | bed to about 0.0075 from 0.5-1 s before the clip; clip at `1` |
| `endcard-fade` | Long fade under the end card | bed 0.15 → 0 over 14 s ending on the last frame |
| `exhale-tail` | Exhale tail | 26-35 s music alone, 6.8-10.4 LU under the body, silent last 0.7-6 s |
| `gapless-bed` | Gapless loud bed | bed `0.1`, 18-22 LU under VO, full length, 0 silences |
| `tension-section` | Tension bed for one section | dark drone at `0.708` (−3 dB) for one sub-composition |
| `payoff-lift` | Payoff montage lift | music `1.585` (+4 dB), VO off, clips on bar lines |
| `thin-bed-pauses` | Thin bed lifted in pauses | bed `0.08`, high-pass 150 Hz, up to `1` over 0.8 s in pauses |

---

## 0. What didn't separate outliers from controls

Read this before copying anyone's pace. Direction = both outliers above, both below, or split
around their own control (values from `data/*.json`, all M).

| Measure | Outliers higher | Outliers lower | Split or equal | Verdict |
|---|---|---|---|---|
| Hard cuts/min, overall (floor) | true crime (control is another sub-format), cooking (gap is the opening only), kids (different formats), calm-faith (body equal: 4.4-4.9 vs 4.3) | documentary (14.6-14.8 vs 23.4), challenge (27.9-29.3 vs 30.9), tech-news (11.0-13.3 vs 15.6), shorts-gaming (5.0-15.0 vs 16.0) | explainer, science (19.7 and 47.9 vs 41.2), storytime, shorts-facts, podcast, tech-review and gaming (one outlier equals the control), shorts-vfx (0 cuts in all) | **Not a lever.** Every "faster" case has a confound |
| Cuts/min in the first 15 s | cooking (32-60 vs 4), true crime (12-20 vs 0), documentary (36-48 vs 24), shorts-facts (3-15 s: 5-10 vs 0), podcast (3-15 s: 15-30 vs 5) | gaming (0 vs 16), tech-news (12 vs 16), storytime (0-20 vs 24) | the other 8 | Mixed. A fast open and an unbroken open both won (see 1.4, 1.5) |
| Median shot | follows the cut rate | | | Not a lever |
| Words per minute, overall | tech-review (200.5-200.7 vs 176.4), calm-faith (151-157 vs 126), documentary (152-171 vs 144), storytime (169-190 vs 165), shorts-facts (163-177 vs 160) | challenge (174-183 vs 193), science (129-157 vs 167), true crime (185-188 vs 191) | 8 niches (kids within 1 wpm counted here) | Leans faster in talk-led formats; not reliable |
| Integrated loudness | science (−11.5 and −7.5 vs −13.8), kids reveal pair (−18.1 vs −22.2); by under 1.1 LU in explainer and tech-review | storytime, tech-news, documentary, calm-faith | the rest | Not a lever. YouTube turns loud uploads down anyway (R) |
| Silences/min | documentary (0.71-1.02 vs 0.23), storytime (1.52 and 0.19 vs 0.11), tech-review (4.87-5.09 vs 3.94; its sheet reads this as no difference) | podcast after the hook (0-1 vs 16 pauses), cooking (0.14-0.26 vs 0.67), calm-faith (0.17-0.25 vs 0.53), science (0.05-0.57 vs 0.8) | true crime (4.72 and 0.71 vs 2.52), kids, and the rest | Direction depends on the format: weight in essays, no dead air in clips |
| On-screen text share | where the text is proof: documentary, explainer, tech-news, true crime | where it isn't: calm-faith verse cards (3-5% vs 12%), tech-review graphics (fewest in the biggest outlier) | | Proof tracked views; decoration didn't (4.1) |
| Designed transitions | | | none in any niche's outlier or control as a habit | Not a lever |
| Controversy | | explainer: comments per view lowest in the biggest outlier (0.05%) | | Not supported |

**What did recur** (every line H):
1. A person with something at stake: explainer, storytime, challenge, documentary, tech-news,
   shorts-facts (3.1).
2. Proof on screen: documentary, explainer, tech-news, true crime, shorts-gaming (4.1).
3. The stake or full claim in the first seconds: science, shorts-facts, shorts-gaming,
   storytime, calm-faith, tech-review (1.1, 1.2).
4. Denser speech in the first 30 s: both outliers above the control in 8 niches (tech-review,
   calm-faith, documentary, cooking, shorts-facts, science, true crime, podcast); below in 3
   (gaming, explainer, storytime). Several controls open slowly (a skit, a wordless intro, a
   single take).
5. Fewer music-only stretches: both outliers carry fewer [music] caption tags per minute than
   the control in 8 niches (8.5).
6. Cuts on a sound onset: both outliers above the control's lift in 5 niches (2.5). Weak,
   because onsets include syllables.

**Confounds to keep in view:** one creator per niche; tech-review's outliers cover a launch-week
product (a news event); both gaming outliers are first episodes; the kids outlier is an hour-long
compilation; the true-crime control is a different sub-format; the science outlier is from 2019
against 2024-25 videos; upload ages differ in several Shorts niches.

---

## 1. Hook and first 15 s

### 1.1 Voice on frame one
The narrator or host speaks on the first frame. No logo, title card or music intro comes first.

| Where | Measured | Label |
|---|---|---|
| explainer, all 3 | first word 0.0-0.56 s; 154-166 wpm in the first 30 s | M |
| science, challenge, tech-news, gaming-longform, true crime, cooking, storytime (all 3 each) | first word 0.0-0.24 s | M |
| shorts-facts, shorts-gaming (all 3 each) | first word 0.0 s | M |
| tech-review: Od6M0AXpcxQ, 6D__H_DO2Xk vs ANmTVYkEtLw | 2.36-2.4 s vs 16.32 s; the control opens on a 73 s music-led skit | M, H |
| calm-faith: 3EkD-alQhT8, b54d_GhBthI vs Q7PgVAN2MPo | 0.56-0.72 s vs 8.64 s of wordless series intro | M, H |
| Exceptions: documentary 2r5eKpptixo (9.7 s, opens on documents), shorts-vfx 5jhEoRZXhjE (13.36 s, the trick is the hook), kids (1.1-7.4 s, a jingle first) | | M |

- Works: any narrated or presenter-led video with a clear promise.
  **Backfires:** when the picture is the hook (a trick, a supercut of documents) or the first
  frame can't be read without context.
- Mood / genre: every talk-led format; in wonder and magic formats the image leads.
- hf-kit: voice `<audio data-start="0">`, no title scene before it. `check.py`
  `first_word_s` range `[0, 0.6]` for narrated styles, `[0, 2.5]` for review styles.

### 1.2 The stake, rule or claim in the first seconds
Say what could go wrong, what's won, or the full claim, before any setup.

| Where | Measured | Label |
|---|---|---|
| challenge, all 3 | premise, rule and prize stated by 0:10-0:22 | S |
| science: DPZzrlFCD_I, P4gNS0Iiu0Q vs 9IiYOTzJ2uw | stakes by 0:15-0:36 vs 4:55-5:22 | S, H |
| shorts-facts: NdKRD1j9juE, p832whe8hrI vs nw6LtopYGlc | a life at risk by 1.0-1.5 s vs never | S, H |
| shorts-gaming: rssMorwX9Ws, 2n1rIXEeybM vs qvrxyBRhi_0 | full claim spoken from 0.0 s vs a teaser, topic at about 1.5-3.4 s | S, H |
| storytime: plSyrHqUh78, Oc91iOxcB3c | 3 rules in 16 s; 2 viewer objections in 23 s | S |
| calm-faith: 3EkD-alQhT8, b54d_GhBthI | the problem within 0.75 s; question or promise by 0:16-0:27 | S, H |

- Works: challenges, survival and safety, news, how-to.
  **Backfires:** fake stakes (clickbait), or a rule that needs a paragraph.
- Mood / genre: tension, hype, dread.
- hf-kit: a script rule, no block. A prize or price lands as `number-card` `variant: money`
  on the spoken number (`scale 1.4→1`, 250 ms, recipe). In Shorts the first caption group is
  the claim's noun phrase.

### 1.3 Show the payoff or the proof first
Open on the finished thing, the result or the source, then explain it.

| Where | Measured | Label |
|---|---|---|
| science, all 3 | a superlative spoken at 0.0-0.2 s over the finished build; 178-220 wpm in the first 30 s | S, M |
| tech-review: Od6M0AXpcxQ | 4 event b-roll shots about 2 s apart under the VO; face at 10.7 s | S |
| shorts-gaming, all 3 | the source post or screenshot on screen by 2.2 s | S |
| shorts-podcast: 8Ho3a4bkkV8 | credential label at 1.0 s | S |
| shorts-vfx: 5jhEoRZXhjE, X0wxLr5W2X8 vs tOIFZ8O6Ezk | a world-famous mural or a known trend, readable by about 2 s, vs an original gag | S, H |

- Works: the object looks good in one frame; first-hand footage; claims viewers might doubt.
  **Backfires:** the object underwhelms; stock footage; a weak source invites "fake" comments; a
  borrowed icon you have no right to use.
- Mood / genre: triumph, curiosity.
- hf-kit: hero clip at `data-start="0"` with the VO on frame 0; source scene by 1.9 s,
  `scale 0.96→1` 0.3 s `power2.out` (recipe); `ui-window` for a source that needs framing.

### 1.4 Fast open, slower body
Cut the first 15 s at two to four times the body rate, then settle.

| Where | Measured (floors) | Label |
|---|---|---|
| documentary, all 3 | 24-48 cuts/min in 0-15 s; 13-23 in the body | M |
| documentary: GV8KGcFqeLc | supercut cold open at 48 cuts/min, sub-second clips | M, S |
| cooking: 3pgUFPtqJu4, AJiGaXRsFNU vs 4TyPUB6o-t8 | 32-60 cuts/min in 0-15 s vs 4 (a 12.4 s single take); bodies equal at about 30 | M, H |
| true crime: QfxhFa5hEX8, R4G4tiPTTDM vs VGiLQIzQW2Q | 3-5 inserts on the hook's nouns (12-20 cuts/min), then 30-45 s on the host; control has no cut | M, H |
| calm-faith: 3EkD-alQhT8 | 20 cuts/min in 0-15 s, shots lengthening from 2.3 to 11 s | M |
| shorts-podcast: 0YVdjmU13E4 vs -svLMqHJGaU | 30 cuts/min in 3-15 s vs 5 | M |

- Works: many strong images; a claim that's already everywhere; a trip or tasting whose
  ending can be previewed unresolved. **Backfires:** similar-looking shots; a preview that gives
  the answer away; clips without source labels.
- Mood / genre: curiosity, hype, tension.
- hf-kit: 8-10 clips at `data-duration` 0.3-0.8 s, each keeping its source lower third,
  then the host track (recipe, documentary and cooking).

### 1.5 Unbroken opening move
The opposite strategy, and it also won: no cut while the camera or the cast carries the open.
calm-faith's two outliers used opposite hooks (20 cuts/min, and none for 40 s), so the material
decides.

| Where | Measured | Label |
|---|---|---|
| calm-faith: b54d_GhBthI | 0 cuts for 40.3 s at 152 wpm | M |
| explainer, all 3 | first cut at 5.9-22.9 s | M |
| gaming-longform: Qk0iCPmtLUA, 2teag5QC7NA vs UjjRGyre3RY | the whole cast uncut for 40-206 s vs a to-camera plan at 16 cuts/min in 0-15 s | M, H |
| kids: J8eVD2PpX_Q, OXjorKzZoUU | 0 cuts in 0-15 s; one camera flight from the book to the character | M, S |
| shorts-facts, all 3 | 0 hard cuts in 0-3 s; first hard cut at 4.67-21.62 s; camera moves instead | M |
| shorts-vfx, all 3 | one take, 0 hard cuts | M |

- Works: an illustrated world the camera can travel; several people reacting live; a trick
  that must read as one take. **Backfires:** a talking head or a still under slow narration
  (reads as frozen).
- Mood / genre: wonder, calm, playful.
- hf-kit: `world-camera` (stations `[{t,x,y,scale}]`, `sine.inOut`, parallax layers at
  0.6×, 1× and 1.4×, recipe); in 9:16, `zoom-through` between scenes.

### 1.6 A question the viewer can answer
Pose a question on screen or aloud, then give the viewer a beat to guess.

| Where | Measured | Label |
|---|---|---|
| shorts-podcast, all 3 | question card in the first seconds: white box, black heavy caps, two lines | S |
| shorts-podcast: 0YVdjmU13E4 | the title answered at 3.5 s | S |
| shorts-vfx: X0wxLr5W2X8 | question spoken at 0.0 s, word-by-word caption gone by 2.0 s, then no text | S |
| kids: J8eVD2PpX_Q vs OXjorKzZoUU | silhouette, clues, a 1.73 s silence after the question, then the name at 0:43; the control has no clues and no pause | M, H |

- Works: clips answering one clear question; tricks with a visible answer; reveals for
  young viewers. **Backfires:** the clip wanders off the card's question; the answer is obvious
  or given away by the clues.
- Mood / genre: curiosity, playful.
- hf-kit: `question-card` (9:16, static, 3-6 s at the seam of a stacked split). Kids reveal:
  `filter:brightness(0)→brightness(1)` 400 ms `power2.out` with the bed at `v:0` for 1.5-2 s
  before the line (recipe, no block yet).

### 1.7 Hook before the brand
The ident, series title or channel pitch comes after the hook's question.

| Where | Measured | Label |
|---|---|---|
| calm-faith: 3EkD-alQhT8, b54d_GhBthI vs Q7PgVAN2MPo | series title at 0:25.5-0:26, after the problem, vs an 8.6 s wordless intro plus a recap | S, H |
| tech-news, all 3 | a 43-50 s cold open, then a fixed show line and title card | M, S |
| true crime, all 3 | one-line premise, then the fixed pitch (0:11-0:29), then about 20-22 s without speech before the story | S |

- Works: series with regulars. **Backfires:** a new channel's fixed bit means nothing yet.
- Mood / genre: all long-form series.
- hf-kit: `chapter-card` as the title card, with a series or date variable. Calm register:
  `opacity 0→1, y 12→0`, 0.8 s `sine.out`, held 3-4 s (recipe).

---

## 2. Pacing and cut rhythm

Section 0 applies: the house rates below describe formats, and none of them tracked views.

### 2.1 House cut-rate registers (reference table)
| Register | Niche | Cuts/min overall (floor) | Median shot | Where the rate moves | Label |
|---|---|---|---|---|---|
| Metronome | challenge | 27.9-30.9 | 1.53-1.8 s | never slows in the body | M |
| Metronome | cooking | 28.1-31.8 | 1.53-1.73 s | faster only in the outliers' first 15 s | M |
| Vlog rate on drawings | storytime | 21.6-23.3 | 1.88-2.0 s | last minute 6-10 | M |
| Two-speed | documentary | 14.6-23.4 | 1.64-2.71 s | archive fast, argument slow, last minute 1-4 | M |
| Wide | science | 19.7-47.9 | 1.0-2.12 s | payoff montages slow to 7 | M |
| Overlay-led | tech-news | 11.0-15.6 | 2.67-3.73 s | cards added onto the frame aren't counted | M |
| Talk plus b-roll | tech-review | 5.5-7.4 | 5.57-7.96 s | verdict in one take | M |
| Camera-led | explainer | 4.3-5.7 | 6.54-9.37 s | flat | M |
| Camera-led | calm-faith | 3.2-5.0 | 5.76-6.83 s in the outliers | rises in the application section | M |
| Play-led | gaming-longform | 5.3-7.5 | 2.35-3.4 s | ensemble scenes uncut; menus add false cuts | M |
| Host-led | true crime | 1.0-3.3 | 7.92-20.04 s | spikes at the evidence | M |
| Camera flights | kids | 0.7-9.5 | 4.08-45.0 s | flat | M |
| Shorts | shorts-podcast | 13.5-30.3 | 1.5-2.43 s | | M |
| Shorts | shorts-gaming | 5.0-16.0 | 2.03-6.0 s | | M |
| Shorts | shorts-facts | 2.2-5.9 | 4.67-13.55 s | camera moves hide the joins | M |
| Shorts | shorts-vfx | 0 | whole video | one take | M |

### 2.2 Metronome edit
Cut on every speaker turn and reaction; no clip longer than about 3.7 s outside set pieces.

| Where | Measured (floors) | Label |
|---|---|---|
| challenge, all 3 | 27.9-30.9 cuts/min; median 1.53-1.8 s; p10-p90 0.84-3.71 s; no slow section | M |
| cooking, all 3 | body 28.7-31.1 cuts/min; median 1.53-1.73 s; p90 3.5-4.0 s | M |
| science: P4gNS0Iiu0Q | 47.9 cuts/min, median 1.0 s (a versus video) | M |

- Works: dialogue-heavy group footage; energetic hosts on rich location footage.
  **Backfires:** calm or reflective content; a static one-angle studio (reads as twitchy).
- Mood / genre: hype, comedy.
- hf-kit: no block; cap clip `data-duration` at the niche's p90. Style ranges: body
  `[28, 31]`, `median_shot_s` `[1.5, 1.8]`.

### 2.3 Jump cuts on phrase boundaries
Remove breaths and join sentence to sentence.

| Where | Measured | Label |
|---|---|---|
| cooking, all 3 | cuts land in speech pauses at 1.43-1.56× chance; 229-235 wpm | M |
| calm-faith: Q7PgVAN2MPo (control) vs outliers | control's cuts wait for pauses (1.33×); outliers cut over the voice (0.89-1.04×) | M, H |

- Works: fast talkers with one continuous A-roll plus inserts.
  **Backfires:** one static angle; in teaching, a picture that waits for every pause (the
  calm-faith control's habit).
- hf-kit: cut list from caption gaps of 0.25 s or more; remove each gap (recipe, cooking).
  Borrowed: sample-accurate transcript splices (`media-use` transcript-cut reasoning).

### 2.4 B-roll over a continuous voice (L-cut)
The voice runs across the cut; the picture changes on the noun.

| Where | Measured | Label |
|---|---|---|
| tech-review, all 3 | cuts in speech pauses at 0.74-0.92× chance; 8.5-12 cuts/min in feature runs | M |
| calm-faith: 3EkD-alQhT8, b54d_GhBthI | 0.89-1.04× (image changes on the noun) | M |
| shorts-podcast: 8Ho3a4bkkV8 | host reaction cutaways over the guest's audio; 4 host shots in 8 s at a strong claim | S |

- Works: spec walkthroughs, teaching, big claims in interviews.
  **Backfires:** the b-roll doesn't show the noun being said; a cutaway hides the speaker's key
  gesture.
- Mood / genre: sincerity, calm, curiosity.
- hf-kit: one continuous voice track; b-roll clips placed on nouns from caption timings. J-cut:
  next clip's audio `data-start` 0.3-1 s before its picture (R).

### 2.5 Cut on a sound onset
Cuts land on a word start or a hit more often than chance.

| Where (cut-on-onset lift, outliers vs control) | Measured | Label |
|---|---|---|
| shorts-podcast | 2.26 (8Ho3a4bkkV8), 1.21 (0YVdjmU13E4) vs 0.59 | M, H |
| true crime | 1.22 (QfxhFa5hEX8), 1.57 (R4G4tiPTTDM) vs 1.06 | M, H |
| storytime | 1.23 (plSyrHqUh78), 1.22 (Oc91iOxcB3c) vs 1.02 | M, H |
| calm-faith | 1.44 (3EkD-alQhT8), 1.19 (b54d_GhBthI) vs 0.95 | M, H |
| cooking | 1.14, 1.13 vs 1.05 | M, H |
| No pattern: explainer, tech-news, tech-review (split); documentary, challenge (flat at 0.96-1.02); gaming, science (split) | | M |

- Reading: a lead, not a finding. Onsets include syllables, so a high lift can mean "cut on
  the word" or "a hit on the insert".
- Works: dialogue edits, evidence inserts. **Backfires:** a cut that clips a consonant.
- hf-kit: snap cut times to transcript word starts, 1-2 frames early (recipe, podcast). Add
  SFX.md "Impact on reveal" on evidence inserts. Borrowed: a beat QA that compares each anchor
  with its word timing and guards shot tails (idea from `video-talkcraft`'s `beat_lint.py`;
  implement it independently).

### 2.6 Two-speed edit
Spend cuts where the content changes register: fast for events and evidence, slow for argument.

| Where | Measured (floors) | Label |
|---|---|---|
| documentary | archive runs 19-45 cuts/min; argument 2-19 | M |
| true crime | 10 cuts in the evidence minute vs 0-5 elsewhere | M |
| tech-news | 13-15 cuts/min for context, 8-9 for statements; FluKUJyeYD8's body speeds to 18.6 for the mess, aspmNhKAFMc slows to 7.5 for statements | M |
| calm-faith | 12 cuts/min in the application section (3EkD-alQhT8 6:01-7:00), about 10 (b54d_GhBthI 4:08-4:49), against a 4.4-4.9 body | M |

- Works: events first, judgment second; a proof chapter; the turn from "them" to "you".
  **Backfires:** inserts spread evenly (proof stops feeling special); a host section of 60 s+ with
  no cutaway.
- Mood / genre: tension, curiosity, calm.
- hf-kit: two sub-compositions, a montage track and a host track with inserts every 5-15 s;
  an evidence sub-composition with 4-8 inserts of 4-8 s (recipe). Borrowed: a shot-function label
  on every clip in the EDL makes the two speeds explicit (`editing-montage`).

### 2.7 Long take for judgment
Hold the verdict or the decision in one shot.

| Where | Measured | Label |
|---|---|---|
| tech-review, all 3 | verdict in one take of 45.8-103.6 s; visual energy 0.21-0.33 | M |
| cooking, all 3 | the longest shots (11.4-17.0 s) are tasting verdicts | M |
| gaming-longform | decisions played with 0 cuts, visual energy 0.06-0.36, for 1-2 min | M |
| documentary, all 3 | 1-4 cuts in the last minute | M |

- Works: a trusted voice at 175-200 wpm; taste and opinion; votes and countdowns.
  **Backfires:** a slow or unknown presenter; vague verdicts.
- Mood / genre: sincerity.
- hf-kit: one A-roll clip, no music, no graphics until the score is spoken; then a hard cut to
  `number-card` or `tier-board` (recipe).

### 2.8 Few cuts, a moving camera
Motion inside the shot does the work of cuts.

| Where | Measured | Label |
|---|---|---|
| explainer, all 3 | 4.3-5.7 cuts/min; median shot 6.5-9.4 s; pushes, pans, macro-to-micro zooms and morphs inside shots | M, S |
| calm-faith, all 3 | runs of 40-139 s without a hard cut while visual energy stays 0.5-1.5 | M |
| kids | camera flights instead of cuts; 0.7-9.5 cuts/min | M, S |
| shorts-facts, all 3 | 2-4 hard cuts in 36-54 s; joins on whips, push-ins and zoom-throughs | M, S |
| shorts-vfx: 5jhEoRZXhjE, X0wxLr5W2X8 vs tOIFZ8O6Ezk | calmer camera in the outliers (visual energy 0.68-0.79 vs 1.34) | M, H |

- Works: illustrated worlds; reflective teaching at 150+ wpm; a trick that must read in one
  look. **Backfires:** a talking head (a 40 s static head reads frozen); a slow zoom on every shot
  (R).
- Mood / genre: wonder, calm, playful.
- hf-kit: `world-camera`. Shot floor: no clip under 3 s outside the hook and the application;
  each long clip gets one `sine.inOut` drift, `scale 1→1.06` (recipe, calm-faith). Borrowed:
  velocity-matched seams where the camera carries across a cut, used selectively
  (`faceless-explainer` cut catalog).

### 2.9 Wide and close, event and reaction
Alternate framings of the same take, or cut from an event to a reaction.

| Where | Measured | Label |
|---|---|---|
| storytime | punch-ins and reaction close-ups on still drawings (plSyrHqUh78 4:13.9, Oc91iOxcB3c 6:47, OQx7q6mwkV4 4:55); about one reaction cut per event beat | S |
| gaming-longform | avatar talking head, wide and close alternating every 1.5-3.5 s in intros and outros | M |
| shorts-podcast, all 3 | hard cuts between real camera angles; no digital punch-in seen | S |

- Works: narrator-led comedy; series intros. **Backfires:** the same face every time; long
  explanations.
- Mood / genre: comedy, sincerity.
- hf-kit: on drawings, `tl.set(art,{scale:1.3,transformOrigin:"55% 40%"})` on alternate
  cuts (recipe). On footage, a hard punch of 110-120% with the origin near the eyes (R).

### 2.10 No dead air after the hook
Tighten voice gaps once the hook has landed.

| Where | Measured | Label |
|---|---|---|
| shorts-podcast: 8Ho3a4bkkV8, 0YVdjmU13E4 vs -svLMqHJGaU | 1 and 0 pauses over 0.4 s after the opening vs 16 in the control's last 44 s, whose picture energy falls to 0.64 | M, H (the clearest audio split in the Shorts) |
| shorts-facts, shorts-gaming (all 3 each) | 0 silences over 0.4 s | M |
| tech-news, all 3 | no silence before the final second | M |
| cooking: outliers vs 4TyPUB6o-t8 | 0.14-0.26 silences/min vs 0.67 | M |
| Counter: gaming-longform keeps 10-11.6 silences/min (12.7-15.3% of runtime); true crime keeps structural gaps | | M |

- Works: information Shorts, clips over 45 s. **Backfires:** a punchline that needs its beat
  (keep one deliberate pause); long-form play and story, where the quiet is part of the format.
- hf-kit: remove voice gaps over 0.4 s (or cap them at 0.2-0.3 s); style range
  `silences_per_min` `[0, 0]` for these Shorts.

### 2.11 Density from the words, not the cuts
| Where | Measured | Label |
|---|---|---|
| tech-review | outliers 200.5-200.7 wpm vs 176.4, at the same or a lower cut rate | M, H |
| calm-faith | outliers 151-157 wpm, 3-4 filler words vs 126 wpm, 17 fillers, 11.75 speech gaps/min | M, H |
| 8 niches | both outliers speak faster than the control in the first 30 s (section 0) | M, H |

- Works: scripted narration. **Backfires:** unscripted talk padded with fillers.
- hf-kit: no block. Pace the voiceover to the style's wpm and check with
  `research/measure.py` (`check.py` doesn't report wpm).

---

## 3. Structure and retention devices

### 3.1 A person with something at stake
The most repeated outlier difference in the sample. In every row the edit and mix match the
control, so the protagonist is a script choice.

| Where | Outliers vs control | Label |
|---|---|---|
| explainer: 0NY2gAftzJE, _zfN9wnPvU0 vs pHJIhxZEoxg | a woman treating her own cancer; the channel testing AI on itself vs a personified tree | S, H |
| storytime: plSyrHqUh78, Oc91iOxcB3c vs OQx7q6mwkV4 | the creator is the protagonist throughout vs invented characters from 0:56 | S, H |
| challenge: KrLj6nc516A, 4l97aNza_Zc vs QJI0an6irrA | one price ladder, or two colour-coded exes, vs 30 celebrities | S, H |
| documentary: 2r5eKpptixo, GV8KGcFqeLc vs OMbV1rIPhCg | danger and power with named antagonists vs a pleasant system | S, H |
| tech-news: FluKUJyeYD8, aspmNhKAFMc vs E7la7-dtfVM | named lab leaders and researchers as cut-outs vs one founder | S, H |
| shorts-facts: NdKRD1j9juE, p832whe8hrI vs nw6LtopYGlc | a man, or "you", in mortal danger vs film trivia | S, H |

- Works: any format. **Backfires:** invented stakes for real victims; strawman characters.
- hf-kit: script rule. Give the protagonist a side colour (`--hk-side-a`) and keep it.

### 3.2 A premise you can say in one line
| Where | Measured | Label |
|---|---|---|
| science: DPZzrlFCD_I, P4gNS0Iiu0Q vs 9IiYOTzJ2uw | a pool of Jell-O; one robot against five vs a party, a sick kid, a cartoon and three builds | S, H |
| challenge: outliers vs QJI0an6irrA | one contrast or one pair vs an ensemble | S, H |
| shorts-gaming: rssMorwX9Ws, 2n1rIXEeybM vs qvrxyBRhi_0 | titles name the thing vs "oh no" | S, H |
| shorts-vfx: 5jhEoRZXhjE, X0wxLr5W2X8 vs tOIFZ8O6Ezk | a claim or a question vs a title calling it an illusion | S, H |

- hf-kit: none; a planning check.

### 3.3 Hold the title's answer, pay small proofs early
| Where | Measured | Label |
|---|---|---|
| explainer: 0NY2gAftzJE, _zfN9wnPvU0 vs pHJIhxZEoxg | the title's question paid at 13:40-14:14 and 5:06-5:30 vs 0:31 | S, H |
| shorts-facts: p832whe8hrI, NdKRD1j9juE | the answer at 83% of runtime; setup explained at 61% | S, H |
| tech-news: aspmNhKAFMc, FluKUJyeYD8 vs E7la7-dtfVM | a loop opened by 0:43 paid at 3:07; a claim deflated at 6:23 vs a loop paid in 30 s | S, H |
| documentary: 2r5eKpptixo, GV8KGcFqeLc vs OMbV1rIPhCg | proof by 0:19; best device by 7:08 vs the control's device at 21:46 | S, H |

- Reading: hold the answer, not the evidence.
- Works: question titles, survival stories, disputes. **Backfires:** a weak payoff (a late
  answer then feels like a cheat); a middle with no tension of its own.
- hf-kit: in Shorts, the answer scene near `0.75 × duration` (recipe); in long form, one
  `doc-highlight` or `ui-window` proof inside the first minute. Borrowed: thesis-first story
  ordering (`faceless-explainer`) agrees with the documentary rows; it conflicts with holding
  the answer only if the thesis states the answer.

### 3.4 "But" turns and an objection voice
Reset the question at intervals.

| Where | Measured | Label |
|---|---|---|
| shorts-facts: NdKRD1j9juE, p832whe8hrI vs nw6LtopYGlc | 2 and 4 "but" turns, about 9-10 s apart, vs 0 | S, H |
| calm-faith: 3EkD-alQhT8, b54d_GhBthI vs Q7PgVAN2MPo | the viewer's doubt voiced about every 45 s; 4 questions in 6 min vs 2 in 5 min | S, H |
| storytime: Oc91iOxcB3c | two viewer objections in the hook, answered at 13:51 and 14:38 | S |
| science, all 3 | test, fail, fix: one loop per 30-90 s | S |

- Works: problem-solution stories; any explanation over 3 min. **Backfires:** trivial turns;
  strawman objections; so frequent it reads as a skit.
- Mood / genre: tension, curiosity.
- hf-kit: one sub-composition per attempt, each ending on a 6-frame red failure flash; the
  objection voice gets its own colour chip (recipe).

### 3.5 A progress device the viewer can read
| Where | Measured | Label |
|---|---|---|
| challenge, all 3 | a price that only rises, a day count, a remaining count that only falls; visible every 1-5 min | S |
| documentary: GV8KGcFqeLc, OMbV1rIPhCg | a 4-step board; an N/26 counter | S |
| cooking: 3pgUFPtqJu4, AJiGaXRsFNU vs 4TyPUB6o-t8 | taste levels 1-4 previewed at 0:19.5 (3pgUFPtqJu4); an S-D tier board shown 3 times, about 1.2 verdicts/min (AJiGaXRsFNU); vs about 13 parallel rounds with no carried score | S, H |
| kids: J8eVD2PpX_Q, OXjorKzZoUU | the numeral badge stays from the reveal to the end | S |

- Works: long videos with a countable goal. **Backfires:** it stops changing for 5+ min, or
  appears once and is forgotten.
- hf-kit: `progress-badge` (changes as JSON; pop `scale 1.4→1` 200 ms `back.out`, recipe);
  `tier-board` (items drop in, the winner glows); SFX.md "Tick for counter".

### 3.6 Scheduled re-hook events
| Where | Measured | Label |
|---|---|---|
| gaming-longform: 2teag5QC7NA vs UjjRGyre3RY | a server event every 5-10 min, each with its own sound cue, vs a build plan with two threads | S, M, H |
| science: P4gNS0Iiu0Q | 5 rounds of 2-4 min | S |
| kids: DC-bErjbu0E | songs at about 0, 19, 44 and 57 min | M |

- hf-kit: a reusable event sub-composition: the cue audio plus a hard cut to the event's
  first frame (recipe).

### 3.7 Chapter resets
Mark each new chapter with one fixed device.

| Device | Where | Measured | Label |
|---|---|---|---|
| Spoken chapter card | explainer, all 3 | one per video at 1:52-6:02; the VO says the title as the card appears | S |
| Date line | true crime, all 3 | every story opens on a date | S |
| Backdrop change | true crime | 4-7 location backdrops per 34 min, each held 1-9 min | M |
| Spoken signpost | gaming-longform: Qk0iCPmtLUA | "day two" after 3.3 s of silence (20:02) | M, S |

- Works: videos over 8 min with a turn. **Backfires:** Shorts; more than two cards per video;
  a backdrop change mid-scene.
- hf-kit: `chapter-card` (`yPercent 100→0`, 500 ms `power3.out`, 80 ms stagger, `data-start`
  on the spoken title's first word, recipe).

### 3.8 Callbacks and bookends
| Where | Measured | Label |
|---|---|---|
| storytime: plSyrHqUh78 | every fallen name returns in a roll call, 9 names in about 9 s (16:50-16:59) | S |
| storytime: Oc91iOxcB3c | both hook objections answered at 13:51 and 14:38 | S |
| tech-review: ANmTVYkEtLw | the skit's dark, bassy sound returns at the callback (bass share 0.45-0.49, brightness 642-926 Hz) | M; "same cue" I |

- hf-kit: reuse the setup's sub-composition as a 0.4-1 s insert just before the payoff line
  (recipe).

### 3.9 Attachment and loss
| Where | Measured | Label |
|---|---|---|
| storytime: plSyrHqUh78 | a nicknamed team that dies one by one; silences of 0.4-2.2 s on deaths and reversals, 1.52/min | M, S |
| storytime: Oc91iOxcB3c | about 8 min of setbacks before the kitten comes home | S |
| gaming-longform: 2teag5QC7NA | a −14 LUFS hit, then 3.5 s of near silence over the death screen (3:58) | M |

- Works: a named character the viewer knows. **Backfires:** trivial losses; real-world
  tragedy.
- Mood / genre: comedy with heart, dread.
- hf-kit: no block yet. Pause the scene's child timeline, `filter:grayscale(1)` over 300 ms,
  a card `scale 1.3→1` 150 ms `power4.out`, bed lane `v:0` for 1.2 s (recipe).

Borrowed for structure: the shot-board row and continuity anchors (`storyboard-previsualization`) and the director worksheet's observable-action and end-state checks (`DirectorSKILL`)
turn these devices into a plan an agent can check; the short-form retention diagnosis
(`social-short-production`) reads a channel's own analytics against them.

---

## 4. On-screen text and captions

Hold rule for any text not spoken aloud: `max(1.5 s, words × 0.35 s)`, or `words × 0.45 s` for
children; a big number needs 1.5-2 s (R). Nothing the viewer must read arrives in under 6 frames
(R).

### 4.1 Receipts on screen
Show the source (document, post, chart, photo) while making the claim.

| Where | Text share, outliers vs control | What | Label |
|---|---|---|---|
| documentary | 23% (2r5eKpptixo), 12% (GV8KGcFqeLc) vs 3% | highlighted documents, charts, a checklist; 5 documents in 3.5 s in the JFK hook | M, S, H |
| explainer | 14-17% vs 5% | an app window, a comment wall, a detector score, a scatter chart | M, S, H |
| tech-news | 57-72% vs 47%; 10.6-21.2 vs 6.7 words per frame | statements, tweets, benchmark tables as cards on black | M, H |
| true crime | 3-12% vs 0% | photos, footage and documents | M, S, H |
| shorts-gaming | 63-95%, all 3 | the post or app screen, by 2.2 s | M, S |
| storytime: Oc91iOxcB3c | | real photos and video of the cat in one grid | S |
| science: DPZzrlFCD_I | | 3-4 clips in about 5 s showing others failed | S |

- Counter-evidence: where the text isn't proof it didn't help: calm-faith's outliers show
  less text (3-5% vs 12%, verse cards), and tech-review's biggest outlier has no graphics at all.
- Works: contested or hyped claims; news; real cases. **Backfires:** a card that can't be
  read in its hold; a highlight that doesn't match the words spoken; decorative windows.
- Mood / genre: curiosity, tension, dread.
- hf-kit: `doc-highlight` (typed page, highlight `scaleX 0→1` 250 ms `power2.out`, page drift
  `y -2%`); `ui-window` (in `y 40→0` 400 ms `power3.out`, typed text `steps(n)` at 40 ms a
  character, bar `scaleX 0→0.8` 1.2 s); cards on `#0b0b0b` tilted ±2° (recipe, tech-news).
  Borrowed: a claim-to-screen table and deterministic factual graphics
  (`explainer-video-production`); numbered-grid → crop → finer-grid → marked-box grounding to
  place a highlight on a screenshot (`motion-graphics` grounding protocol).

### 4.2 Highlight the spoken clause
| Where | Measured | Label |
|---|---|---|
| documentary | a red bar behind one phrase of a document | S |
| tech-news, all 3 | orange or red bars on the quoted line; hand-drawn white arrows and underlines | S |
| shorts-gaming: 2n1rIXEeybM | read-along highlight, 4 steps in 6 s | S |

- Backfires: a bar over the whole paragraph.
- hf-kit: `doc-highlight` with `revealAt` on the clause's first word.

### 4.3 Label on first appearance
| Where | Measured | Label |
|---|---|---|
| explainer, all 3 | bold white sans on a coloured pill ("Stoma", "Script Writing", immune cells); labels fill most of the 5-17% text share | S, M |

- Works: 3+ new terms or actors. **Backfires:** labels that stay after the first pass.
- hf-kit: `pill-label` (`scale 0.6→1`, 0.2 s `back.out(1.7)`, hold by the rule above, out
  150 ms `power2.in`).

### 4.4 Numbers as cards
| Where | Measured | Label |
|---|---|---|
| tech-review | 0-5 cards per video (prices, a benchmark, wattage); none in Od6M0AXpcxQ | S |
| challenge, all 3 | one outlined green money figure per step | S |
| cooking: 3pgUFPtqJu4, 4TyPUB6o-t8 | a price on screen by 0:04.5-0:09; big green numerals | S |

- Works: prices, benchmarks, prize reveals. **Backfires:** every number styled, so none
  matters; decorative labels on non-numeric claims.
- hf-kit: `number-card` `clean` (numerals 96 px bold, `y 20→0` 0.4 s `power3.out`) or
  `money` (`#39ff6a`, 4 px dark stroke, glow, `scale 1.4→1` 250 ms). Borrowed: source,
  denominator, baseline and proportional-animation rules for numbers and bars
  (`motion-graphics-direction`).

### 4.5 Short-form caption tracks
Three measured variants. OCR undercounts all three.

| Variant | Where | Seen | Label |
|---|---|---|---|
| cards | shorts-facts, all 3 | captions in nearly every frame; 2-4 words, about one card a second, near 78% of frame height, sentence case, no box, no active-word highlight | S |
| karaoke | shorts-gaming, all 3 | condensed bold caps, white with a dark outline, 2-4 words, one word in cyan or yellow | S |
| speaker | shorts-podcast, all 3 | host always yellow, guest white in the outliers, 1-5 words, no box; the control used 5 colours | S, H |

- Works: cards under 160-200 wpm narration; karaoke for 215-305 wpm talk; speaker colours for
  two or three voices. **Backfires:** faces or products at caption height; more than three
  speaker colours; karaoke on slow, emotional delivery.
- hf-kit: `captions.py --variant cards|karaoke|speaker`. Borrowed: rail versus promoted
  embed, bad-clip refusal and preview-before-render checks (`embedded-captions`); the final
  mixed audio as the caption source of truth (`captions-media-accessibility`); semantic line
  breaks and worst-frame QA (`title-kinetic-typography`); dated safe-zone tests per platform
  (`social-short-production`); text-behind-subject layering kept in sync (`media-use`).

### 4.6 Emphasis type, not running subtitles (long form)
| Where | Measured | Label |
|---|---|---|
| challenge, all 3 | one punch caption per beat, a few per video; outlined display type for key words only | S |
| tech-news, all 3 | sticker captions on the key noun: heavy condensed caps, tilted 5-15°, 1-3 per 30 s in the hooks | S |
| cooking, all 3 | keywords in a second colour, money in green | S |

- OCR reads 0-3% text in challenge and cooking; it misses this stylised type (M floor).
- Backfires: running subtitles in this style; whole sentences as stickers; everything
  coloured.
- hf-kit: `captions.py --variant punch` (heavy italic caps, stroke, `scale 0.6→1` 120 ms, held
  1.2 s) or `--variant keyword` (`.kw`, `.money`, `scale 0.92→1` over 3 frames). The tech-news
  sticker is the punch variant plus `rotate:-8deg` and a 6 px stroke (recipe; not a variant yet).

### 4.7 Text off
No captions and no lower thirds: the voice and the picture carry it.

| Where | Measured | Label |
|---|---|---|
| science, all 3 | 0-3% text, no captions | M |
| gaming-longform, all 3 | 0-3% added text; only the game's HUD | M |
| shorts-vfx, all 3 | 0% over the effect; at most a 1.5 s opening question | M, S |
| calm-faith | outliers 3-5% vs control 12% | M, H |

- Works: physical spectacle, visual tricks, reflective long-form narration.
  **Backfires:** explainers; Shorts watched muted (untested here).
- hf-kit: no caption track after the first 2 s.

### 4.8 Honesty and authority labels
| Label | Where | Measured | Label tag |
|---|---|---|---|
| "(NOT) REAL" on staged or stock images | true crime outliers | on every reenactment insert | S, H |
| Credential | shorts-podcast: 8Ho3a4bkkV8, 0YVdjmU13E4 vs -svLMqHJGaU | credential at 1.0 s; a name card at 0:35 vs role tags too small to read | S, H |

- hf-kit: no blocks yet. Honesty label: typewriter caps top-centre, 14 px at 1080p,
  `opacity 0.85` (recipe). Credential: handwritten-style text plus an SVG arrow drawn with
  `strokeDashoffset` over 0.4 s (recipe).

### 4.9 Layouts for 9:16
| Where | Measured | Label |
|---|---|---|
| shorts-gaming, all 3 | face in the top 30-33%, a banner, the content box below | S |
| shorts-podcast, all 3 | stacked split with the question card at the seam | S |

- hf-kit: `face-banner-stack` (its topic-top mode is a rounded 16:9 box at the top);
  `question-card`. Borrowed: the card/video split, stack, PiP and overlay options with portrait
  type sizes (`talking-head-recut`); a choice between screen-space and tracked overlays with a
  fallback (`motion-graphics-direction`).

---

## 5. Motion graphics and transitions

### 5.1 Hard cut by default; flashy transitions are rare
| Niche | What the sampled cut pairs showed | Label |
|---|---|---|
| documentary | hard cuts; single-frame accents only (a light-leak flash at GV8KGcFqeLc 0:15, black frames) | S |
| explainer | one zoom-blur and one screen tunnel (_zfN9wnPvU0); dissolves and morphs otherwise | S |
| science, gaming-longform, true crime, shorts-podcast, shorts-gaming | none | S |
| challenge | a white flash 0-2 times per video | S |
| tech-review | the channel ident and one iris | S |
| tech-news | a pixel-block dissolve 1-3 times per video | S |
| cooking | in-camera swishes; one picture-in-picture | S |
| kids | none; sparkles, glow and confetti bursts inside shots | S |
| calm-faith | dissolves, fades to white or black, one page turn | S |
| storytime | none in 36 sampled cut pairs; speed lines and impact frames inside shots | S |
| shorts-facts | the exception: camera whips, push-ins and zoom-throughs are the join | S |
| shorts-vfx | joins hidden inside whips and blurred moves | I |

- hf-kit: clip B's `data-start` = clip A's end, no tween. In motion-graphics work, one primary
  transition for 60-70% of scene changes plus 1-2 accents (R, HyperFrames transitions doc).

### 5.2 One accent, kept for a turn
| Where | Measured | Label |
|---|---|---|
| tech-news, all 3 | pixel-block dissolve at topic turns, never on every cut | S |
| challenge: KrLj6nc516A, 4l97aNza_Zc vs QJI0an6irrA | a white flash on an explosion; two in a hook vs none | S |
| explainer: _zfN9wnPvU0 | one zoom-blur | S |

- Backfires: on every cut (template look); more than 3 flashes in any second (seizure risk,
  WCAG 2.3.1, R).
- hf-kit: no pixel-dissolve block yet: a 16×9 grid of divs, pre-seeded `opacity 1→0` stagger
  over 250 ms, `steps(1)` (recipe). Flash: white div in over 2 frames, out over 4-8 (R).
  Borrowed: the restrained Social Flash verification steps (`media-use` recipe seeds).

### 5.3 Camera-move joins
| Where | Measured | Label |
|---|---|---|
| shorts-facts, all 3 | 2-4 hard cuts per 36-54 s; scenes join through zooms into objects and blurred whips | M, S |
| explainer, all 3 | macro-to-micro zooms and morphs | S |
| kids: J8eVD2PpX_Q, OXjorKzZoUU | one continuous camera from the book to the page to the character | S |

- Works: 3D or illustrated worlds. **Backfires:** live-action talking heads; zooming on every
  change (motion sickness, R).
- hf-kit: `zoom-through` (scene A `scale 1→6` `power3.in` 0.4 s around the object; scene B
  `scale 0.6→1` `power3.out` at the same time).

### 5.4 Hide the join inside motion
| Where | Measured | Label |
|---|---|---|
| shorts-vfx, all 3 | 0 hard cuts in 11-26 s | M; joins I |
| gaming-longform | 5-10 of 12 sampled cut pairs per video touch an inventory screen | S |

- Backfires: a visible swap frame; menus shorter than 0.3 s.
- hf-kit: `blur-swap` (before and after layers swapped at the peak of a 4-6 frame blur,
  `blur 0→20px→0`).

### 5.5 Entrances land on the word
Measured: elements enter on the spoken word (seen in explainer, tech-news, kids, podcast). The
durations and eases are recipes, not measurements.

| Element | Recipe | Source row |
|---|---|---|
| Masked line reveal | `yPercent 100→0`, 500 ms `power3.out`, 80 ms stagger | explainer chapter card |
| Card on black | `y 20→0`, `opacity 0→1`, 200 ms `power3.out` | tech-news receipts |
| Pill | `scale 0.6→1`, 0.2 s `back.out(1.7)` | explainer pill label |
| Sticker | `scale 1.3→1`, 120 ms `expo.out` | tech-news sticker caption |
| Calm title | `opacity 0→1, y 12→0`, 0.8 s `sine.out` | calm-faith series title |

- Rules (R): decelerate in, accelerate out; about three easing characters per video; exits
  20-30% shorter than entrances; `back.out` and bounce for playful beats only; one gradient sweep
  per video at most.
- Borrowed: GSAP backward-seek and side-effect checks before a render
  (`gsap-animation-composition`).

### 5.6 Camera on stills
| Where | Measured | Label |
|---|---|---|
| explainer, all 3 | the camera travels one illustrated world | S |
| documentary, all 3 | archive stills and period maps with drawn red or gold routes | S |
| true crime: outliers | host keyed over a location still, changed per chapter | S |

- hf-kit: `world-camera` (three parallax layers). Ken Burns on a still: `scale 1→1.12,
  xPercent 0→-3`, `sine.inOut`, over a 5-10 s hold (R). One camera move per shot (R). No map block
  yet.

---

## 6. VFX and colour

Nothing in the 48 was measured for grade. Colour claims below are seen in frames; grade
recipes are reference.

### 6.1 The palette carries meaning
| Where | Seen | Label |
|---|---|---|
| explainer, all 3 | flat vector on deep purple and navy, with green, magenta, cyan and orange for whatever acts | S |
| calm-faith, all 3 | one illustrated world per video; 2-3 fixed palettes (desert, garden, presence; history against teaching) | S |
| storytime, all 3 | black line art on white, colour only on the subject; a lavender-grey wash for rooms and flashbacks | S |
| kids, all 3 | one colour per number | S |

- Works: abstract ideas; a character the story is about. **Backfires:** a palette that drifts
  scene to scene; everything coloured, so nothing pops.
- hf-kit: tokens per world (`--hk-bg`, `--hk-accent`, `--hk-side-a/b`); one world class per
  scene sub-composition; 0.6-0.8 s crossfade when the world changes (recipe). Borrowed:
  visual-grammar invariants, controlled variables and failure signals (`visual-style-direction`).

### 6.2 Colour-coded sides
| Where | Seen | Label |
|---|---|---|
| explainer | 3-4 actor colours per video (virus against cancer, AI against humans) | S |
| challenge: 4l97aNza_Zc | two colours on clothes, tags and sets | S |
| shorts-podcast | a colour per speaker in captions | S |

- Backfires: more than four colours; more than three sides.
- hf-kit: `--hk-side-a` `#3be8ff`, `--hk-side-b` `#ff7a3b`; the enemy's colour also drives its
  glow, `drop-shadow(0 0 12px var(--enemy))` (recipe).

### 6.3 Glow on the named noun
| Where | Seen | Label |
|---|---|---|
| shorts-facts, all 3 | the object the narration names lights up as it's said, 7 or more times per video | S |

- Backfires: every object glows. **Works:** a moving camera under dense narration.
- hf-kit: no block yet: a masked cut-out with `drop-shadow(0 0 12px var(--glow))`, in over 4
  frames, held 1-1.5 s (recipe).

### 6.4 Archive in a film gate
| Where | Seen | Label |
|---|---|---|
| documentary, all 3 | archive footage, prints and period maps in a rounded dark vignette with warm, textured colour | S |

- Backfires: modern footage gets it too. **Mood:** nostalgia, history.
- hf-kit: `film-gate` (`box-shadow: inset 0 0 120px 60px #000`, `border-radius 24px`, archive
  clips only). Borrowed: the Film Memory and VHS Playback recipe seeds with their before/after
  verification (`media-use`).

### 6.5 Real over rendered
| Where | Seen or measured | Label |
|---|---|---|
| science, all 3 | fire, smoke, snow, sparks and Jell-O are real; no designed transitions | S |
| shorts-vfx, all 3 | effects that look practical, natural light, no visible grade; a calm camera in the outliers (0.68-0.79 vs 1.34) | S, M |

- hf-kit: for our renders, one look per video and at most three texture layers (R).

### 6.6 Grades by mood (reference only)
Teal-orange for challenge and hype; bleach bypass or low-key noir for true crime and mystery;
high-key pastel for kids and cooking; warm nostalgic with grain and halation for memory; cold
clinical for tech (R). One look per video, set at the start; text sits above grade and grain (R).
Borrowed: the intent-to-treatment decision table, HDR guard and before/after check, plus the
Editorial Halftone and Cached Error Diffusion seeds (`media-use`).

---

## 7. Sound design and SFX

Designed-SFX density is unmeasured in every niche: onsets per minute (60-130) follow speech. In
shorts-gaming they rise with speaking rate (215 wpm → 90, 264 → 104, 305 → 130 onsets/min, M).
The sections below use loudness, spectrum, onset timing and caption tags.

### 7.1 The loudest moment is a person
| Where | Measured | Label |
|---|---|---|
| challenge, all 3 | the loudest windows are shouting and money moments; an explosion doesn't top the shouting (KrLj6nc516A) | M |
| gaming-longform, all 3 | the loudest window is laughter or an excited shout, 8.2-16.6 LU over the median | M |
| true crime, all 3 | the story's climax line, 4.8-7.6 LU over the median | M |
| tech-news, all 3 | a borrowed clip with its own audio, 3-8 LU over the median | M |

- Reading: peaks are reactions and real sound, not designed effects.
- hf-kit: impacts at or under the voice (SFX.md: impact −6 dB under the voice); let reaction
  audio peak and catch it with a true-peak limiter rather than flattening it.

### 7.2 A sound on the evidence insert
| Where | Measured | Label |
|---|---|---|
| true crime, storytime | outliers' cut-on-onset lift 1.22-1.57 vs 1.02-1.06 in the controls (2.5) | M, H |
| true crime: VGiLQIzQW2Q | `>> [music] >>` inside sentences at key lines (21:24) | S; short stings I |

- hf-kit: SFX.md "Impact on reveal" (transient on the insert's first frame, −6 dB under the
  voice) or "Pop-in" (−12 dB) for small inserts. Borrowed: a motion-to-sound cue schema of
  `{relative time, sound role, visual event, gain, optional rate/trim}` (idea from
  `video-talkcraft`'s sfx map; implement independently with our own cleared files).

### 7.3 Build into the impact, fall away after it
| Where | Measured | Label |
|---|---|---|
| shorts-vfx: tOIFZ8O6Ezk | a steady 12 LU climb into the crash | M |
| shorts-vfx: 5jhEoRZXhjE | peak at the confrontation (−12.1, 12-14 s), then about 9.6 LU down; brightness about 1530 → 348 Hz, bass share 0.11-0.13 → 0.36 | M |
| gaming-longform: 2teag5QC7NA | an explosion at 3:56 falling 50 LU into the death screen at 4:00 | M |

- Works: builds, falls, escapes. **Backfires:** talk-led Shorts, where the voice stays level.
- hf-kit: SFX.md "Riser into payoff" (1-4 s lead ending on the payoff frame) plus "Impact on
  reveal"; then gain automation down 8-10 LU with a low-pass for a quiet ending (recipe). Pattern:
  riser → 1-4 frames of near silence → impact, about one pair a minute in long form (R).

### 7.4 Event cues
| Where | Measured | Label |
|---|---|---|
| gaming-longform: 2teag5QC7NA | 10 [funky music] cues plus bells and ticking, one per scheduled event | M (tags) |
| kids: J8eVD2PpX_Q, OXjorKzZoUU | a jingle opens both reveals, then a 0.72 s gap (0:08.9) | M |
| tech-review: Od6M0AXpcxQ, 6D__H_DO2Xk | the channel ident; music tagged at 0:00.7 | M (tags) |

- hf-kit: a reusable event sub-composition carrying its cue (recipe).

### 7.5 Restraint by genre (reference)
Designed SFX per minute (R): fast Shorts 15-40; listicles 10-25; explainers 4-12; tutorials 2-8;
documentary 0-4; calm and faith 0-2. Sound the top one or two animations in each 5-10 s window;
no SFX on looping motion; rotate 3-6 variants; SFX 6-15 dB under the voice (R). The only measured
hint: kids content has the lowest onset rate among talk-led niches (76-78/min, M), but syllables
dominate that number.
- hf-kit: SFX.md event map (pop-in, whoosh on transition, impact on reveal, riser into
  payoff, tick for counter, sub drop), with generated files in `sound/sfx/`. Borrowed:
  material, distance, sync priority and a stem/asset manifest per sound (`sound-design-foley`); the SFX manifest's event timings, after fixing its J/L-cut error (`media-use`).

---

## 8. Music and mood

### 8.1 Music follows speech, not the beat
| Where | Cut-on-onset lift | Label |
|---|---|---|
| documentary | 0.96-1.01 | M |
| challenge | 0.98-1.02 | M |
| kids | 1.01-1.03 | M |
| gaming-longform | 0.94-1.13 | M |
| cooking | 1.05-1.14 | M |
| science: DPZzrlFCD_I | 1.31, the only beat-cut stretch in the sample, in montages with no narration | M |

- Rule: under narration, cut on speech and let the music sit; in a music-only montage, cut 1-2
  frames before beats or bars (R).
- hf-kit: no beat grid under the voice. Borrowed: the reliable-grid versus phrase-flow
  decision (`music-to-video`); real-transient and rendered-output beat checks
  (`video-shotcraft`).

### 8.2 Payoff montage: music takes over
| Where | Measured | Label |
|---|---|---|
| science: DPZzrlFCD_I | montages at 2:29-3:13, 5:00-6:58 and 8:41-9:45 with no narration; about 4 LU over the narration; bass share 0.43-0.57; 7 cuts/min against 16-32 around them | M |
| gaming-longform: Qk0iCPmtLUA, UjjRGyre3RY | one music time-lapse of about 27-28 s per episode (58:39, 11:45) | M |
| kids: DC-bErjbu0E | four song blocks carry the lessons (0:11-3:28, 18:38-25:26, 44:25-48:49, 53:19-61:44) | M |

- Works: visually satisfying action; build progress. **Backfires:** dull or repetitive action;
  a montage for every task.
- Mood / genre: triumph, playful.
- hf-kit: `payoff-lift` (music `1.585`, VO off, 4-8 s clips on bar lines).

### 8.3 Music at the edges, not under the talk
| Where | Measured | Label |
|---|---|---|
| tech-review, all 3 | [music] tags only in the first minute and the sponsor or outro; bass share 0.3-0.6 there vs 0.14-0.24 under talk; 3.9-5.1 open silences/min | M |
| tech-news: FluKUJyeYD8, aspmNhKAFMc | no [music] tags | M |
| storytime, all 3 | bass share 0.05-0.13; 0.06-0.34 tags/min; low end rises only where the voice drops out | M |
| gaming-longform, all 3 | music only for a time-lapse or an event | M |
| shorts-podcast | no tags in 2 of 3; 5 of 0YVdjmU13E4's 6 tags within about 2 s of a stylised insert or the name card | M |

- The chapter's "music up on b-roll" for tech review is not seen: b-roll in the body carries no
  tagged music (M against R).
- Works: talk-led reviews; one fast narrator. **Backfires:** a room-noise problem the bed was
  hiding; slow, quiet stories that need mood.
- Mood / genre: sincerity, comedy, curiosity.
- hf-kit: `thin-bed-pauses`, or music clips only in the intro and outro scenes.

### 8.4 A continuous flat bed
| Where | Measured | Label |
|---|---|---|
| explainer, all 3 | [music] tags from the first 5 s at 3.3-6.5/min; bass share 0.21-0.27; LRA 2.2 | M |
| calm-faith, all 3 | body spread 3.1-3.7 LU; no silence in the body; Q7PgVAN2MPo's 11.75 speech gaps/min leave only 0.53 silences/min | M; "filled by the bed" I |
| shorts-facts, all 3 | LRA 2.0-2.3, zero silences | M; bed I |

- Works: dense narration; reflective teaching. **Backfires:** a melodic bed in 1-4 kHz under
  dense speech (it masks consonants, R).
- Mood / genre: wonder, calm.
- hf-kit: `voice-first-flat` or `gapless-bed`. Carve 3-6 dB around 2-3 kHz on the bed (R).

### 8.5 Fewer music-only stretches (outlier lead)
A [music] caption tag marks music heard with no words. Both outliers carry fewer tags per minute
than their control in 8 niches (values from `data/*.json`):

| Niche | Outliers | Control | Label |
|---|---|---|---|
| explainer | 4.79, 3.34 | 6.53 | M |
| storytime | 0.11, 0.06 | 0.34 | M |
| calm-faith | 0.25, 0.33 | 1.78 | M |
| challenge | 0.9, 0.24 | 1.27 | M |
| cooking | 0.14, 0.18 | 2.31 | M |
| documentary | 1.31, 1.34 | 1.9 | M |
| tech-review | 0.52, 0.19 | 0.64 | M |
| tech-news | 0, 0 | 0.17 | M |
| Reverses: true crime | 0.2, 1.5 | 1.33 | M |

- Reading (H): the outliers keep a voice on top more of the time. Caption types differ (auto
  against human), so treat it as a lead.
- hf-kit: plan music-only moments as events (8.2, 9.4), not as filler between lines.

### 8.6 Score one section differently
Darker and bassier for tension, in one section only.

| Where | Measured | Label |
|---|---|---|
| challenge: 4l97aNza_Zc | the lie-detector minutes about 3 LU quieter; brightness 1382 → 942-1175 Hz; bass share 0.32-0.34 | M |
| shorts-facts: NdKRD1j9juE, p832whe8hrI vs nw6LtopYGlc | loudest and bassiest on the danger beats (bass share up to 0.34) inside a 2-3 LU band; the control stays flat | M, H |
| calm-faith: b54d_GhBthI | bass share 0.26-0.37 under the unbroken opening and 0.35 under the fall, vs a 0.17 median | M |
| cooking: 3pgUFPtqJu4 | the processing minutes darker (531 Hz against 691 Hz) | M; source unknown |

- Backfires: a dark mix all the way through; constant tension that numbs (R).
- Mood / genre: tension, dread.
- hf-kit: `tension-section`; in Shorts, bed +2 LU with a low-shelf boost over the danger scene
  and −2 LU for the waiting beat, voice fixed (recipe).

### 8.7 Bed on for tension, off for exposition
| Where | Measured | Label |
|---|---|---|
| true crime: VGiLQIzQW2Q | minutes with [music] tags have no silences; minutes without have 6-12 per minute | M |
| true crime: QfxhFa5hEX8 | the fewest tags and the most silences (4.72/min) | M |

- Backfires: a bed that drops mid-sentence.
- hf-kit: music volume keyed to transcript sections, 0.8 s fades at section borders (recipe).

### 8.8 One swell at a climax
| Where | Measured | Label |
|---|---|---|
| documentary: GV8KGcFqeLc | about 9 LU over the median at 17:50-17:54, in a [music] gap | M |
| calm-faith: 3EkD-alQhT8, b54d_GhBthI | bumps of 2.5-4 LU on dramatic beats (3EkD-alQhT8 0:20, 1:32, 2:30, 3:26; b54d_GhBthI 0:44, 1:14, 4:18) | M; cause I |
| science: DPZzrlFCD_I | payoff minutes about 4 LU over the narration | M |

- Rule (R): about one strong hit per 10-20 s of bed; the biggest accent on the section's most
  important picture.
- hf-kit: no preset; a `data-automation` volume lane raising the bed 2.5-4 LU for the beat.

### 8.9 A darker tail
| Where | Measured | Label |
|---|---|---|
| explainer: _zfN9wnPvU0, pHJIhxZEoxg | last 10 s bass share 0.88 and 0.89, brightness 476 and 106 Hz, against medians of 0.21-0.27 and 1014-1203 Hz | M |
| calm-faith: 3EkD-alQhT8, b54d_GhBthI | the outro cue roughly halves in brightness (469-545 vs 1106 Hz; 440-635 vs 1178 Hz) | M |
| shorts-vfx: 5jhEoRZXhjE | last 6 s brightness about 1530 → 348 Hz | M |

- hf-kit: an outro cue darker than the bed, with `endcard-fade` or `exhale-tail`.

### 8.10 The song is the lesson
| Where | Measured | Label |
|---|---|---|
| kids: DC-bErjbu0E | the eight times table sung 3 times, with the chorus 3 times, in 4:18 | M, S |

- Looks like a conflict with the chapter's "no sung lyrics over teaching lines" (R), but here the
  lyric is the teaching and nothing competes with it.
- hf-kit: equation bubble `from({scale:0,rotation:-12})`, 250 ms `back.out(2)` on the sung
  answer; hold `words × 0.45 s` (recipe).

Borrowed for music: cue IDs, planned silences and exits, and composition-versus-master rights
checks (`music-supervision-scoring`).

---

## 9. Mix and loudness

### 9.1 Master to −14 LUFS, −1 dBTP
| Niche | Integrated LUFS (M) | LRA LU (M) |
|---|---|---|
| challenge | −5.6 to −8.1 | 3.6-5.3 |
| science | −7.5 to −13.8 | 1.7-9.7 |
| shorts-facts | −10.9 to −11.6 | 2.0-2.3 |
| shorts-gaming | −12.1 to −14.9 | 1.0-2.4 |
| storytime | −12.9 to −15.9 | 2.2-6.8 |
| shorts-vfx | −13.7 to −33.9 | 8.4-14.2 |
| shorts-podcast | −14.1 to −21.7 | 3.6-5.8 |
| explainer | −15.4 to −15.9 | 2.2 |
| tech-review | −15.9 to −17.0 | 4.1-5.0 |
| documentary | −16.1 to −18.0 | 5.9-7.9 |
| calm-faith | −16.1 to −18.0 | 4.7-6.0 |
| true crime | −16.4 to −16.9 | 5.0-8.2 |
| cooking | −18.2 to −21.0 | 5.3-6.6 |
| kids | −18.1 to −22.4 | 6.6-13.2 |
| gaming-longform | −19.3 to −22.3 | 9.7-15.0 |
| tech-news | −20.3 to −23.8 | 2.4-3.2 |

- Loudness separated nothing (section 0). YouTube turns loud uploads down and doesn't raise quiet
  ones (R; community-measured, YouTube publishes no number). Shorts, TikTok and Reels have no
  published target: −14 there is our house default, not a platform rule (R; wording qualified per
  `social-short-production`).
- hf-kit: `check.py`'s master line (target −14, ceiling −1 dBTP). Borrowed: a local loudness
  meter and delivery checks (`audio-mixing-mastering`); probe → decide → encode → probe
  (`ffmpeg-media-finishing`).

### 9.2 Flat, voice-first mix
| Where | Measured | Label |
|---|---|---|
| explainer, all 3 | LRA 2.2; per-minute means within 0.5-0.8 LU across the body | M |
| tech-news, all 3 | LRA 2.4-3.2 | M |
| shorts-facts, shorts-gaming | LRA 1.0-2.4 | M |
| storytime: plSyrHqUh78, Oc91iOxcB3c vs OQx7q6mwkV4 | 4.1 and 2.2 vs 6.8 (one narrator against a cast) | M |

- Works: one narrator, dense narration. **Backfires:** calm or story pieces that need
  dynamics.
- hf-kit: `voice-first-flat`; render and check LRA ≤3 LU.

### 9.3 Wide mix for casts, songs and reactions
| Where | Measured | Label |
|---|---|---|
| gaming-longform | LRA 9.7-15.0; loudest window 8.2-16.6 LU over the median | M |
| kids | LRA 6.6-13.2 | M |
| shorts-vfx | LRA 8.4-14.2; the 2 s curve swings 9.6-14.1 LU inside each Short | M |
| science: DPZzrlFCD_I | LRA 9.7 | M |

- Backfires: a body 5-8 LU under its intro (the kids control's flaw); fix with pauses and a −14
  master, not a quiet master.
- hf-kit: no flattening; a true-peak limiter last, with no more than about 1 dB of limiting
  (R).

### 9.4 Silence as punctuation
The most shared sound device: used in 12 of 16 niches, absent in tech-news, shorts-facts,
shorts-gaming and the podcast outliers.

| Use | Where | Measured | Label |
|---|---|---|---|
| Drop before a reveal | science: DPZzrlFCD_I | 0.55 s silence before the tarp reveal (4:30) | M |
| | science: 9IiYOTzJ2uw | a dip to −22/−26 before the kid's surprise (10:04) | M |
| | true crime: R4G4tiPTTDM | 0.4-0.9 s gaps in the 10 s before a character notices something (14:24-14:34, 20:41-20:52) | M |
| | kids: J8eVD2PpX_Q | 1.73 s after the guessing question (0:40.5) | M |
| | cooking: AJiGaXRsFNU | 1.09 s before a verdict (17:58) | M |
| | shorts-vfx: X0wxLr5W2X8 | 0.8-1.95 s gaps around the reveals; 46% of runtime silent | M |
| | gaming-longform: 2teag5QC7NA | 2.4-3.3 s gaps 16 s before the loudest window (41:03-41:08) | M |
| Weight after the heaviest line | documentary: 2r5eKpptixo, GV8KGcFqeLc vs OMbV1rIPhCg | 0.71-1.02 silences/min of 0.4-1.5 s, clustered at thesis lines, vs 0.23 | M, H |
| | calm-faith: 3EkD-alQhT8 | near silence at −41.7 LUFS right after the thesis (6:58), once | M |
| | calm-faith: b54d_GhBthI | −5 LU and a 2.0 s speech gap at the turn (5:02), once | M |
| | explainer, all 3 | one pause per video: 0.41 s (0NY2gAftzJE 6:21), 0.74 s (pHJIhxZEoxg 9:39.8), a 2.3 LU dip (_zfN9wnPvU0 8:18) | M |
| | storytime: plSyrHqUh78 | 0.4-2.2 s silences on deaths and reversals, 1.52/min | M |
| Chapter punctuation | true crime, all 3 | 2.5-6.2 s after the last line of a story or chapter, 2-6 per video, down to −43 to −65 LUFS | M |
| | gaming-longform | 3.3 s before "day two" (Qk0iCPmtLUA 20:02); 4.1 s on a loading screen (UjjRGyre3RY 15:48) | M |
| Comic timing | tech-review: Od6M0AXpcxQ, 6D__H_DO2Xk | 0.85-1.2 s and a −26.4 dip on a subscribe gag (Od6M0AXpcxQ); a 2.6 s gap at an archival "No" and 0.55-0.97 s while reading prices (6D__H_DO2Xk) | M |
| | challenge: KrLj6nc516A | a dip to −17.5 under a slow car door (8:24-8:28) | M |
| | cooking: 3pgUFPtqJu4 | after a joke (3:52); a censor mute (5:22) | M |

- Rarity is the point: once per video in explainer and calm-faith; under about one a minute in
  documentary; about one per two minutes for verdicts (cooking steal list); at most one hard
  silence per 2-3 min (R). In Shorts keep it under about 1 s (R), except comic reveals
  (shorts-vfx, measured 0.8-1.95 s).
- Backfires: after every paragraph; in information Shorts (reads as broken); a gag silence on a
  real tragedy.
- hf-kit: `silence-at-heaviest-line`; `pause-at-turn`; chapter gap = every track off with a
  black div for 2.5-6.2 s (recipe); comic beat = cut the A-roll with 1-2.5 s of room tone. Under
  dialogue, "silence" means room tone, not digital zero (R).

### 9.5 Dip before a loud clip
| Where | Measured | Label |
|---|---|---|
| documentary: 2r5eKpptixo | −28.8 LUFS at 4:12 before the −10.7 peak at 4:20; archive news clips are the three loudest windows, 7-8 LU over the median | M |
| tech-news, all 3 | borrowed clips 3-8 LU over the median, narration stopped | M |

- Backfires: on every clip; clips every 30 s (the reset stops resetting).
- hf-kit: `dip-before-clip`.

### 9.6 Duck and carve under the voice (reference)
Music 18-22 LU under the voice while it speaks, rising to 10-14 LU under in gaps over 1 s; duck
down over 250-400 ms starting 100-200 ms before the first word, up over 500-800 ms, and merge gaps
under 1 s so the bed doesn't pump; carve 3-6 dB near 2-3 kHz on the bed (R). `sound/MIX.md` notes
that music under speech needs a measured voice carve before a final render.
Borrowed: the ducking-lane shape (`media-use` `duck.mjs`); "solo the named stem", no surgical
fixes on bled stems, and a mono check after widening (`mix-engineer`); line-level dialogue
repair that keeps the original performance, useful for clip channels (`dialogue-editing-adr`).

---

## 10. Endings

### 10.1 Shorts end on the payoff
| Where | Measured | Label |
|---|---|---|
| shorts-facts, all 3 | the payoff image ends it; no call to action, no end card | S |
| shorts-gaming, all 3 | 0 s of outro; the last informative line ends the video | M, S |
| shorts-vfx, all 3 | the payoff frame, no outro | S |

- hf-kit: no end scene; the last caption group ends the timeline.

### 10.2 Long form slows in the last minute
| Where | Cuts in the last minute (floor) | Label |
|---|---|---|
| documentary | 1-4 | M |
| explainer | 3 (0NY2gAftzJE, pHJIhxZEoxg); 12 (_zfN9wnPvU0) | M |
| tech-news | 2-8 | M |
| storytime | 6-10, under credits | M |
| calm-faith outliers | 0-4 | M |
| kids: DC-bErjbu0E | 3, visual energy 0.32, a bedtime ending | M |
| Counter: science 26-59, cooking 22-27, challenge 19-39 keep full pace to the end | | M |

- hf-kit: a `last_min` range in the style JSON.

### 10.3 A quiet tail under the credits
| Where | Measured | Label |
|---|---|---|
| documentary: 2r5eKpptixo, OMbV1rIPhCg | credits in silence or near silence for 14-20 s | M |
| explainer: _zfN9wnPvU0, pHJIhxZEoxg | a fade of about 31 LU over the last 14-16 s under the end card | M |
| calm-faith: all 3 | 26-35 s of music-only credits 6.8-10.4 LU under the body, ending in 0.7-6.1 s of silence | M |
| storytime: plSyrHqUh78 | credits 10-15 LU under the body | M |
| Counter: storytime Oc91iOxcB3c's last 20 s is its loudest stretch | | M |

- Works: an end card, credits or a support ask. **Backfires:** Shorts (over about 1 s of quiet
  reads as broken, R); a video that ends on a line of VO.
- hf-kit: `endcard-fade` (end-card scene 15-20 s) or `exhale-tail` (back-time the cue's last
  chord to the logo frame).

### 10.4 Sponsor and brand after the content, or inside it
| Where | Measured | Label |
|---|---|---|
| tech-review: Od6M0AXpcxQ, ANmTVYkEtLw | sponsor after the content, "AD" label bottom-left | S |
| tech-news, all 3 | sponsor at the end, 13-43 s, then a fixed sign-off | M, S |
| science, all 3 | a closing gag, then the ad or end card | S |
| challenge: KrLj6nc516A, 4l97aNza_Zc vs QJI0an6irrA | own brand inside a stunt (chocolate survives an explosion, KrLj6nc516A 3:35-4:07) vs a TV-series plug at both ends | S, H |

- hf-kit: the sponsor as its own final sub-composition with one offer sticker (recipe).

### 10.5 Fixed sign-off
| Where | Seen | Label |
|---|---|---|
| gaming-longform, all 3 | a recap, what's next, goodbye | S |
| cooking, all 3 | the same short sign-off | S |
| true crime, all 3 | thanks, a comments ask, a playlist pointer | S |
| explainer, all 3 | the same "Support Human-Made Art" end card | S |

- hf-kit: one end-card sub-composition per channel, reused.

---

## 11. Mood table

M = from the 48 videos (a measured number, or seen in their frames where the cell says "seen").
R = reference chapters. Cut rates are hard-cut floors. Where a mood had no sampled video, the
cell is R only.

| Mood | Cut rate | Shot length | Music: tempo feel, instruments, bed level | SFX palette | Colour | Motion easing |
|---|---|---|---|---|---|---|
| **Dread** (true crime; survival Shorts) | M: 1.0-3.3/min (true crime); 2.2-5.9/min with camera moves (shorts-facts) | M: median 7.9-20.0 s (true crime); 4.7-13.6 s (shorts-facts) | M: sparse bed, on for tension, off for exposition; 0.2-1.5 [music] tags/min. R: 40-70 BPM or no pulse; sub drones, clusters, bowed metal; very quiet bed with rare stings | M: 2.5-6.2 s structural silences; 0.4-0.9 s gaps before a discovery; bass share up to 0.34 on danger beats. R: no horror stings on real victims | M (seen): no visible grade; host keyed over location stills. R: low-key noir or bleach bypass, grain, vignette | M (seen): no punch-ins, whips or zooms. R: slow push-ins, Ken Burns, `sine.inOut`, fades; no bounce |
| **Tension** (one section; essays about power) | M: documentary outliers 14.6-14.8/min against a 23.4 control | M: median 2.1-2.7 s (documentary outliers) | M: one section −3 LU, brightness −15-32%, bass share +0.15 (4l97aNza_Zc). R: 70-110 BPM pulse or none, minor, low ostinato, no release until the payoff; bed 18-22 LU under voice | M: 0.4-1.5 s silences at the heaviest lines (0.7-1.0/min); a dip to −28.8 before the key clip. R: ticking, riser → near silence → impact | M (seen): a lamp-lit dark desk set (documentary outliers). R: desaturated or cold | M (seen): hard cuts, single-frame accents. R: masked line reveals `power3.out`, slow pushes |
| **Curiosity / news** (tech news, trivia) | M: 11.0-15.6/min, most changes are overlays | M: median 2.67-3.73 s | M: no [music] tags in the tech-news outliers. R: mystery 70-100 BPM, pizzicato, celesta, muted piano; a quiet driving bed or none under dense speech | M: a borrowed clip as the stinger, +3 to +8 LU; zero silence in the body. R: UI clicks, typing, short glitch | M (seen): black canvas, orange highlight bars, white arrows. R: cold or neutral, light chromatic accents | M (seen): pixel-block dissolve at topic turns; no camera moves. R: `steps(n)` typewriter, 200 ms `power3.out` cards |
| **Wonder** (explainers, magic Shorts) | M: 4.3-5.7/min (explainer); 0, one take (shorts-vfx) | M: median 6.5-9.4 s, p90 up to 27 s; the whole Short in one take | M: bed from the first 5 s, 3.3-6.5 tags/min, bass share 0.21-0.27, LRA 2.2. R: 60-90 BPM, major or Lydian, choir pads, celesta, arpeggios, long reverb; one slow swell | M: one short pause per video at the turn (0.41-0.74 s). R: 4-12 clean designed SFX/min; shimmer on reveals | M (seen): flat vector on deep purple with neon actors; natural light, no grade (vfx). R: bloom for magic | M: calm camera around the trick (visual energy 0.68-0.79). M (seen): pushes and zooms inside the shot. R: `sine.inOut` camera, `power3.out` entrances |
| **Hype** (challenge, versus) | M: 27.9-30.9/min (challenge); 47.9/min (P4gNS0Iiu0Q) | M: median 1.0-1.8 s; p90 about 2.1-3.7 s | M: near-constant sound, −5.6 to −8.1 LUFS, LRA 3.6-5.3; cuts ignore the beat (lift 0.98-1.02). R: 120-160 BPM (half-time common), 808, heavy kick, risers and drops | M: 0-1 silences per video; peaks are shouting, not effects. R: whooshes, impacts, sub drops; 15-40 designed SFX/min in Shorts | M (seen): outlined green money type, two-colour character system. R: saturated teal-orange | M (seen): hard cuts, white flash 0-2 per video. R: punch-ins, shake on impacts, `expo.out`, `back.out` pops |
| **Triumph** (payoffs) | M: 7/min in the payoff montage against 16-32 around it (DPZzrlFCD_I) | M: about 8.6 s average in that montage (derived from 7 cuts/min) | M: music takes over, about +4 LU, bass share 0.43-0.57, cuts on onsets 1.31×, VO off. R: major, brass, taiko, choir; build, peak, hold, resolve | M: 0.55 s silence right before the reveal. R: riser into impact, boom on the result | M (seen): practical spectacle (real fire, smoke, Jell-O). R: clean, bright, slight teal-orange outdoors | R: `expo.out` hero reveal; winner `scale 1.15` plus glow (recipe) |
| **Calm** (reflective teaching) | M: body 4.4-4.9/min; runs of 40-139 s with no hard cut | M: median 5.8-6.8 s, p10 3.2-5.0 s (outliers) | M: constant bed, body spread 3.1-3.7 LU; 2.5-4 LU bumps on dramatic beats; darker outro cue. R: 50-80 BPM or free time; pads, piano, choir, long reverb; bed 18-22 LU under VO | M: no mid-body silence; one breath at the payoff (−5 LU for 2 s, or −41.7 LUFS). R: 0-2 designed SFX/min; no whooshes, impacts or stings | M (seen): one illustrated world per video, 2-3 fixed palettes. R: warm, bloom, halation, soft vignette | M (seen): dissolves, fades, one page turn. R: `sine.inOut` drifts; fade and drift, 0.8 s `sine.out` |
| **Sincerity** (interviews, verdicts) | M: 13.5-30.3/min between real angles (podcast outliers); 0 cuts for 45.8-103.6 s in a verdict (tech-review) | M: median 1.5-2.4 s (podcast); verdict take 45.8-103.6 s at visual energy 0.21-0.33 | M: no bed in 2 of 3 podcast clips; tech-review music only at the edges (bass 0.14-0.24 under talk). R: bed absent or very low; no emotion the speaker isn't showing | M: no dead air after the hook (0-1 pauses). R: no designed SFX | M (seen): dark studio with warm practicals; lit presenter rooms. R: the room's own colour | M (seen): hard cuts and reaction L-cuts, no digital punch-ins. R: 100% / ~115% punch alternation on key lines |
| **Comedy** (narrated storytime, gags) | M: 21.6-23.3/min on drawings | M: median 1.88-2.0 s | M: thin bed, bass share 0.05-0.13, ≤0.34 tags/min; the low end arrives in pauses. R: follows the joke; short cues, hard stops; pizzicato, tuba, bassoon | M: comic silences 0.85-2.6 s, dips to −24/−26 (tech-review gags); a −17.5 comic dip (KrLj6nc516A). R: record scratch at most once; stings sparingly | M (seen): black line art on white, colour on the subject only. R: warm or pastel | M (seen): punch-ins on reaction close-ups; speed lines and impact frames inside shots. R: `back.out` for playful beats only |
| **Playful / childlike** (preschool) | M: 0.7-9.5/min; 1-5 hard cuts in a 1.5-2 min reveal | M: median 4.1-45.0 s | M: jingle or song openings; songs carry the lessons; −18.1 to −22.4 LUFS, LRA 6.6-13.2. R: 90-130 BPM, simple major I-IV-V, glockenspiel, ukulele, toy piano | M: 1.3-3.81 pauses/min; a 1.73 s answer pause; the lowest onset rate (76-78/min). R: pop-ins, chimes, Mickey-Mousing on actions | M (seen): one bright colour per number. R: high-key pastel, bright primaries | M (seen): continuous 3D camera flights; sparkles and bursts; no whip, glitch or shake. R: `back.out` allowed; holds `words × 0.45 s` |
| **Nostalgia** (archive, memory) | M: archive montage 19-45/min inside documentaries | R: 5-10 s Ken Burns holds on stills | M: documentary brightness medians 742-825 Hz, the darkest niche. R: 70-100 BPM, Rhodes, tape-wobbled synths, music box; warm, low-passed | M: credits in near silence for 14-20 s (documentary). R: vinyl crackle, soft ambience | M (seen): archive in a rounded dark vignette with warm, textured colour. R: sepia 0.25, amber soft-light, grain, halation | M (seen): one single-frame light-leak flash (GV8KGcFqeLc). R: light leak 15-30 frames, `sine.inOut` |

---

## 12. Recipe gaps in hf-kit

What the evidence asks for that the kit doesn't have yet:
- Blocks: tilted sticker caption (a `punch` variant), pixel-block dissolve, glow on the named
  noun, loss card, silhouette reveal, map with a drawn route (a documentary house device), honesty
  label, credential label with a drawn arrow.
- Checks: `check.py` doesn't report text share or wpm, so style ranges for those go unchecked;
  run `research/measure.py` for them.
- Mix: no preset for a single swell (8.8); use a raw `data-automation` lane.

## 13. Credits for borrowed ideas

Each idea comes from a third-party skill that was read for this library. The ideas are adapted;
no code or bundled media was copied.

| Idea | Source skill | Used in |
|---|---|---|
| Intent-to-treatment table, HDR guard, before/after verification | `media-use` | 6.6 |
| Film Memory, VHS Playback, Editorial Halftone, Cached Error Diffusion seeds; restrained Social Flash checks | `media-use` | 5.2, 6.4, 6.6 |
| SFX manifest event timings (fix the J/L-cut error first) | `media-use` | 7.5 |
| Transcript-cut splice reasoning; text-behind-subject sync; ducking-lane shape | `media-use` | 2.3, 4.5, 9.6 |
| Rail vs promoted captions, bad-clip refusal, matte-leak and preview checks | `embedded-captions` | 4.5 |
| Reliable-grid vs phrase-flow music planning | `music-to-video` | 8.1 |
| Card/video split, stack, PiP and overlay layouts | `talking-head-recut` | 4.9 |
| Numbered-grid image grounding | `motion-graphics` | 4.1 |
| Thesis-first ordering, voice-synced reveals, velocity-matched seams | `faceless-explainer` | 2.8, 3.3 |
| Loudness meter and delivery checks | `audio-mixing-mastering` | 9.1 |
| Material, distance, sync priority, stem manifest | `sound-design-foley` | 7.5 |
| Cue IDs, silences and exits, composition vs master rights | `music-supervision-scoring` | 8 |
| Line-level dialogue repair keeping the original performance | `dialogue-editing-adr` | 9.6 |
| Final audio as caption source of truth | `captions-media-accessibility` | 4.5 |
| Shot functions and EDL handoff | `editing-montage` | 2.6 |
| Source, denominator, baseline, proportional animation; screen-space vs tracked overlays | `motion-graphics-direction` | 4.1, 4.4, 4.9 |
| Semantic line breaks, worst-frame text QA | `title-kinetic-typography` | 4.5 |
| GSAP backward-seek and side-effect checks | `gsap-animation-composition` | 5.5 |
| Shot-board rows and continuity anchors | `storyboard-previsualization` | 3 |
| Visual-grammar invariants and failure signals | `visual-style-direction` | 6.1 |
| Claim-to-screen table, deterministic factual graphics | `explainer-video-production` | 4.1 |
| Safe-zone tests, qualified loudness wording, retention diagnosis | `social-short-production` | 3, 4.5, 9.1 |
| Probe → decide → encode → probe | `ffmpeg-media-finishing` | 9.1 |
| Observable-action and end-state planning checks | `DirectorSKILL` | 3 |
| Motion-to-sound cue schema; beat QA against word timing | `video-talkcraft` (idea only; its licence is noncommercial) | 2.5, 7.2 |
| Solo the named stem, mono check after widening | `mix-engineer` (a third-party music-skills pack) | 9.6 |
| Recipe-card format; real-transient beat checks | `video-shotcraft` | 8.1, and the shape of every entry here |
