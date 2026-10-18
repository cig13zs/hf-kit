# Niche DNA: kids animation / education

Three Numberblocks videos, checked 2026-09-26. Cards: `cards/kids-education/`.
- DC-bErjbu0E, "The Super Duper Heroes of Numberland": long-form outlier, 8.73×, 1:02:31, a
  compilation of about 14 segments (first 5 minutes studied closely)
- J8eVD2PpX_Q, "Meet Numberblock 33": recent outlier, 3.8×, 2:06
- OXjorKzZoUU, "Meet Numberblock 37": control, 0.98×, 1:30

All three come from one channel. The two reveals share one template, which makes them a clean
pair; the compilation is a different format, so it speaks to format more than editing. The
characters are 3D renders. HyperFrames can build the 2D equivalent (unit blocks as divs or
SVG) and the whole type, badge and camera layer; for true 3D, Three.js is available as a
HyperFrames runtime.

## Ranges (all measured; cut counts are floors)
| Measure | Min | Max |
|---|---|---|
| Cuts/min overall | 0.7 (OXjorKzZoUU, one cut) | 9.5 (DC-bErjbu0E) |
| Cuts/min 0-15s | 0 (J8eVD2PpX_Q, OXjorKzZoUU) | 8.0 (DC-bErjbu0E) |
| Cuts/min 15-60s | 0 (OXjorKzZoUU) | 10.7 (DC-bErjbu0E) |
| Cuts/min after 60s | 2.0 (OXjorKzZoUU, 60-90s) | 9.5 (DC-bErjbu0E, 1-3 min); J8eVD2PpX_Q 2.7 |
| Cuts/min body, last minute | only DC-bErjbu0E has them: 9.7 and 3.0 | - |
| Median shot | 4.1s (DC-bErjbu0E) | 45.0s (OXjorKzZoUU); J8eVD2PpX_Q 19.9s |
| First cut | 2.9s (DC-bErjbu0E) | 74.9s (OXjorKzZoUU, the end screen) |
| Visual energy, mean per minute | 0.61 (OXjorKzZoUU) | 0.97 (DC-bErjbu0E) |
| On-screen text share | 0% (DC-bErjbu0E) | 17% (OXjorKzZoUU; mostly its end screen, inferred) |
| Speech wpm overall | 79 (OXjorKzZoUU) | 98 (DC-bErjbu0E) |
| Speech wpm first 30s | 72 (J8eVD2PpX_Q) | 94 (DC-bErjbu0E) |
| First spoken word | 1.1s (J8eVD2PpX_Q, OXjorKzZoUU) | 7.4s (DC-bErjbu0E) |
| Integrated loudness | −22.4 LUFS (DC-bErjbu0E) | −18.1 LUFS (J8eVD2PpX_Q) |
| Loudness range | 6.6 LU (DC-bErjbu0E) | 13.2 LU (J8eVD2PpX_Q) |
| Silences/min (>0.4s) | 1.3 (DC-bErjbu0E) | 3.81 (J8eVD2PpX_Q) |
| Onsets/min | 76 (DC-bErjbu0E) | 78 (J8eVD2PpX_Q) |
| Music: cuts-on-onsets lift | 1.01 (DC-bErjbu0E) | 1.03 (J8eVD2PpX_Q); not computable for OXjorKzZoUU |
| Music: tempo | 73.8 BPM (OXjorKzZoUU, confidence 1.64) | 152.0 BPM (J8eVD2PpX_Q, confidence 1.35); DC-bErjbu0E 95.7 BPM (confidence 1.39); all weak |
| Music: bass share median | 0.12 (J8eVD2PpX_Q) | 0.24 (OXjorKzZoUU) |
| Music: brightness median | 996 Hz (OXjorKzZoUU) | 1296 Hz (J8eVD2PpX_Q) |

## Shared devices (all three: the house style)
- **The body is the number.** Characters are stacks of unit blocks, one colour per number,
  and the count of blocks is the value (seen in all three).
- **The numeral stays on screen.** Above each head in the compilation; a corner badge in the
  reveals from the moment of the reveal (seen).
- **Slow speech:** 79-98 wpm (measured), about half the animated explainers' 156-162.
- **Camera flights instead of cuts:** 0.7-9.5 cuts/min (measured). The reveals are one
  continuous 3D camera from the book to the page to the character (seen); the compilation
  cranes and tracks inside its scenes (seen).
- **Musical openings.** Both reveals open with a rhymed jingle about the magic book (0:01; sung is inferred); the
  compilation opens with a times-table song (0:07) (seen in transcripts).
- **Quiet, wide mixes:** −18.1 to −22.4 LUFS and LRA 6.6-13.2 LU (measured), the quietest and
  widest in the sample so far.
- **Pauses:** 1.3-3.81 silences/min (measured), and a 0.72s gap right after the jingle in both
  reveals (0:08.9, measured).
- **Participation prompts:** "who could this Numberblock be?", "Shout it out if you know",
  counting aloud (seen in transcripts).
- **No whip, glitch or shake** in any sampled frame (seen). The accents are sparkles, glow,
  confetti and bursts.
- **Cuts at chance against sound onsets** (lift 1.01-1.03, measured).

## Outlier against control (every causal claim is a hypothesis)
| Dimension | J8eVD2PpX_Q (3.8×) | DC-bErjbu0E (8.73×) | Control OXjorKzZoUU (0.98×) |
|---|---|---|---|
| Format | 2-min reveal, same template | 62-min themed compilation | 90-s reveal |
| Theme | football, with gags | superheroes and a villain | hide-and-seek, "wild card" |
| Clues before the guess | yes | - | none |
| Answer pause | 1.73s silence | - | no silence over 0.4s |
| Facts shown | 5 clubs, 3 split forms | a full times table sung 3 times | 2 clubs, 1 split form |
| Cuts/min | 2.4 | 9.5 | 0.7 |
| LUFS, LRA | −18.1, 13.2 LU | −22.4, 6.6 LU | −22.2, 12.1 LU |
| wpm | 80 | 98 | 79 |

Hypotheses:
1. **Format drives the compilation.** An hour on one theme, with songs every 15-20 minutes and
   a bedtime ending, suits long, parent-started sessions. Its edit (9.5 cuts/min, steady) is
   unremarkable, so the edit is unlikely to explain the 8.73×.
2. **Inside one template, content density wins.** The 33 reveal gives clues before the guess,
   a real pause to answer, a theme with jokes and more facts shown as parts. The 37 reveal has
   none of these. The pace and the template are the same.
3. **A louder master may help on devices.** The 33 reveal is 4.1 LU louder than 37. YouTube does
   not turn quiet uploads up, so 37 plays quieter on the same tablet (inferred). This is weak:
   the compilation is as quiet as the control and still leads.
4. **Confound:** the 33 reveal had two more days online at the check (12 against 10), and the
   number itself may draw different search interest.

## Sound and music profile
- **Level:** −18.1 to −22.4 LUFS integrated (measured), 4-8 LU under YouTube's −14 reference.
  These play noticeably quieter than most videos (inferred from the knowledge chapter's
  normalisation rule). For a new kids channel, keep the knowledge chapter's −14 default and
  get dynamics from pauses instead of a quiet master.
- **Range:** 6.6-13.2 LU (measured), three to six times the animated explainers' 2.2. Jingles,
  songs and cheers are loud; narration and answer pauses are quiet (measured in the reveals'
  curves: intros −16 to −21, bodies −16 to −28, pauses −26 to −36).
- **Silence as a turn for the child:** a 1.73s silence after "who could this Numberblock be?"
  (J8eVD2PpX_Q 0:40.5, measured). Reading it as a participation pause is inferred.
- **Songs carry the lessons:** the compilation's [music] tags cluster in four song blocks (0:11-3:28,
  18:38-25:26, 44:25-48:49, 53:19-61:44), and the first song is the eight times table itself
  (measured and seen). The music chapter's kids row warns against sung lyrics over teaching
  lines. Here the lyrics are the teaching, which is a different case: nothing competes with them.
- **Low sound-design density:** 76-78 onsets/min (measured), the lowest of the three niches in
  this batch (explainers 96-99, storytime 82-95).
- **Timbre:** brightness 996-1296 Hz, bass share 0.12-0.24 (measured), between the storytime
  niche's thin low end (0.05-0.13) and the explainers' (0.21-0.27).
- **Tempo** is unusable in all three (measured, weak confidence).

## Steal list
| Technique | Measured range | Works when | Backfires when | HyperFrames recipe |
|---|---|---|---|---|
| The body is the number | 1 block per unit, one colour per value | teaching counts, place value, times tables | abstract quantities with no unit | CSS grid of `.block` divs (`width:48px;aspect-ratio:1;border-radius:6px`), count generated from a variable; the ones group keeps a distinct colour |
| Numeral badge and collection row | badge from the reveal to the end; 2-5 club icons | a list of properties | icons that are never named | badge pinned top-left on its own track clip; icons `from({y:-30,scale:0,autoAlpha:0})`, 300 ms `back.out(2)`, on each spoken name |
| Silhouette, clues, pause, reveal | silhouette 0:01.5-10; name at 0:43; 1.73s pause | a reveal for young viewers | clues that give it away at once; older viewers | `filter:brightness(0)` → `brightness(1)`, 400 ms `power2.out`; bed volume lane `v:0` for 1.5-2s before the reveal line; sparkle burst on the name |
| Lesson as a sung chorus | table sung 3× with chorus 3× in 4:18; bubble on the sung answer | fixed sequences to memorise | narration over the song | equation bubble `from({scale:0,rotation:-12})`, 250 ms `back.out(2)` on the answer word; hold `max(1.5s, words×0.45s)` |
| One camera through one world | 1-5 hard cuts in 1.5-2 min | short, single-character episodes | long pieces with many locations | one scene; a `#world` group with book, page and set as layers; camera = `tl.to("#world",{scale:3,x:...,y:...,duration:1.2,ease:"power2.inOut"})` per station |
| Show the parts | 1-3 split forms per reveal | anything made of units | parts that leave the frame | GSAP Flip between layouts, `Flip.from(state,{duration:0.6,ease:"power2.inOut",stagger:0.01})` |
| Songs as landmarks, bedtime ending | songs at 0, ~19, ~44, ~57 min; last minute 3 cuts, energy 0.32 | compilations over 30 min | single short videos | root timeline of segment sub-compositions; 1.5s rainbow-ray bumper (`conic-gradient`, `rotation:0→90`, `scale:0.2→2.5`, 600 ms `expo.out`); final segment with 6-10s shots and `sine.inOut` drifts |
| Pauses for dynamics, not a quiet master | LRA 6.6-13.2 at −18 to −22 LUFS here | preschool content | the body drops 5-8 LU under the intro (the control's flaw) | master to −14 LUFS; keep jingle and body within ±2 LU; get range from 0.7-1.7s pauses with the bed lane at `v:0` |
