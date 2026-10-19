# Niche DNA: fast-facts Shorts (Zack D. Films)

Sample, all vertical Shorts from one creator, checked 2026-09-26 (see `SAMPLE.md` for the
one-creator deviation):
- NdKRD1j9juE, "He Drifted At Sea For 133 Days", outlier 4.76×, 0:41. Card: `cards/shorts-facts/NdKRD1j9juE.md`
- p832whe8hrI, "What To Do If Your Car Sinks?", recent outlier 2.6×, 0:54. Card: `cards/shorts-facts/p832whe8hrI.md`
- nw6LtopYGlc, "How Back To The Future Created Its Lightning", control 0.98×, 0:36. Card: `cards/shorts-facts/nw6LtopYGlc.md`

p832whe8hrI and the control went up the same day, so that pair is the cleanest comparison.
Three videos from one channel is a thin base; every range below is a sample of three.

## Ranges table (measured)
| Measure | Min | Max |
|---|---|---|
| Duration | 36s (nw6LtopYGlc) | 54s (p832whe8hrI) |
| Hard cuts/min, overall (floor) | 2.2 (p832whe8hrI) | 5.9 (NdKRD1j9juE) |
| Cuts/min 0-3s | 0 (all three) | 0 (all three) |
| Cuts/min 3-15s | 0 (nw6LtopYGlc) | 10.0 (NdKRD1j9juE) |
| Cuts/min 15s-end | 1.5 (p832whe8hrI, 15-54s) | 5.7 (nw6LtopYGlc, 15-36s) |
| Cuts/min 60s-end | none: all under 60s | |
| First hard cut | 4.67s (NdKRD1j9juE) | 21.62s (nw6LtopYGlc) |
| Median shot | 4.7s (NdKRD1j9juE) | 13.6s (p832whe8hrI) |
| Visual energy | 1.25 (nw6LtopYGlc) | 1.7 (NdKRD1j9juE) |
| OCR text share | 17% (p832whe8hrI) | 23% (NdKRD1j9juE). Captions are in nearly every frame of all three (seen): OCR undercounts them |
| Speech wpm, overall | 160 (nw6LtopYGlc) | 177 (NdKRD1j9juE) |
| Speech wpm, first 30s | 160 (nw6LtopYGlc) | 200 (NdKRD1j9juE) |
| First spoken word | 0.0s (all three) | 0.0s (all three) |
| Integrated loudness | −11.6 LUFS (p832whe8hrI) | −10.9 LUFS (NdKRD1j9juE) |
| Loudness range | 2.0 LU (nw6LtopYGlc) | 2.3 LU (NdKRD1j9juE) |
| Silences/min (over 0.4s) | 0 (all three) | 0 (all three) |
| Onsets/min | 84.9 (NdKRD1j9juE) | 91.1 (p832whe8hrI) |
| Music tempo | 73.8 BPM (NdKRD1j9juE, confidence 1.99) | 152.0 BPM (p832whe8hrI, confidence 1.71); nw6LtopYGlc 76.0 (confidence 1.4). All weak under narration |
| Cut-on-onset lift | not computable: too few cuts (null for all three) | |
| Bass share per 10s | 0.17 (nw6LtopYGlc) | 0.34 (NdKRD1j9juE at 20-30s, the shark kill; p832whe8hrI at 30-40s, trapped) |
| Brightness per 10s | 1106 Hz (p832whe8hrI, 0-10s: going underwater) | 1646 Hz (NdKRD1j9juE, 30-40s) |
| Likes per view | 3.8% (nw6LtopYGlc) | 4.5% (p832whe8hrI) |

## Shared devices: the house style (all seen unless marked)
- Narration on frame 1 and no title card. First word at 0.0s in all three; the first
  frame is an action already under way.
- **3D animated re-enactment** with semi-realistic, expressive characters, and a camera that
  never stops moving.
- Hard cuts are rare. Scene changes ride on camera moves: motion-blurred whips, push-ins,
  zoom-throughs into objects. The hard-cut counts (2-4 per video) are heavy floors.
- One-second caption cards: white bold rounded sans, sentence case, soft shadow, 2-4
  words, centred near 78% of frame height, with no box and no active-word highlight. The
  captions change faster than the pictures and set the rhythm.
- Glow on the named noun. The object the narration names lights up (yellow, green, red,
  cyan or magenta) as it is said. Seven or more per video.
- In-world branding. The channel name is printed on a prop or costume inside the scene
  in all three.
- Loud, flat, gapless mix: about −11 LUFS, LRA about 2 LU, no silences (measured).
- **The ending is the payoff image** (rescue, surfacing, finished shot) with no call to
  action and no end card.

## Outlier against control (every causal claim is a hypothesis)
| Device | Outliers | Control |
|---|---|---|
| Who is at risk | a man (NdKRD1j9juE) or "you" (p832whe8hrI), in mortal danger | nobody; film trivia |
| "But" turns | 2 (NdKRD1j9juE), 4 (p832whe8hrI) | 0; list connectives only |
| When the title's answer lands | 83% (car) or the number at 34/41s; context held to 61% | begins at 0:00 |
| Speech, first 30s | 176-200 wpm | 160 wpm |
| Hard cuts in 3-15s | 5-10/min | 0/min |
| Likes per view | 4.5% | 3.8% |
| Loudness and spectrum follow the story | yes: loudest and bassiest in the danger beats (measured) | flat; loudest at the opening |

- H1: stakes carry the gap. Both outliers put a life at risk in the first 1.5 seconds;
  the control never does. Look, captions and mix are identical, so the difference is in the
  script, not the edit surface.
- H2: turns keep people past the middle. The outliers reset the question every 9-10
  seconds with a "but" or a "You see"; the control runs as a list.
- H3: the answer held late is the retention engine. The car Short answers its own title
  at 83% of runtime, and the drift Short explains its setup at 61%.
- H4: the sound scores the danger. Both outliers' loudness, brightness and bass move
  with the danger beats inside their flat mixes; the control's don't (measured shapes;
  the effect on viewers is a hypothesis).
- The cut rate does not separate outliers from the control (2.2 and 5.9 against 3.3/min).
  The edit's pace is house style, not the lever.

## Sound and music profile
- Measured: −10.9 to −11.6 LUFS integrated, about 3 LU hotter than the −14 LUFS
  YouTube reference, so playback is likely turned down (reference from
  `knowledge/sound-design.md` §3.3; the platform behaviour for Shorts is inferred). LRA
  2.0-2.3 LU. No silence over 0.4s anywhere. Onsets 85-91/min whether the video has 2 or 4
  hard cuts.
- Measured shape: the 2-second curve stays in a 3 LU band, but p832whe8hrI shows a
  story-shaped swell inside it: loudest at the window smash, lowest through the trapped
  stretch, up again at the escape. NdKRD1j9juE peaks at the shark attack. The control's peak
  is its opening, with no lift at the reveal flash.
- Inferred: a continuous bed under wall-to-wall narration, with dense foley or SFX
  hits (85-91 onsets/min) that are not tied to cuts. This fits the chapter's fast-facts row
  ("continuous bed", `knowledge/music-and-mood.md` §5) and the Shorts rule of silences
  under about 1s (`knowledge/sound-design.md` §2.2); these videos take that to zero.
  Mood from the script: tension for the survival stories, wonder or a neutral tone for the
  trivia (inferred; no music data).
- Music block (all three): tempo estimates of 73.8, 152.0 and 76.0 BPM at low
  confidence; cut-on-onset lift can't be computed with 2-4 cuts. Both outliers move their
  spectrum with the story: the drift Short's bass share jumps to 0.34 in the violent 20-30s
  window and a caption [music] tag sits under its ending (36.5s); the car Short is darkest
  as it sinks (1106 Hz, 0-10s) and bassiest in the trapped stretch (0.34, 30-40s). The
  control's brightness and bass stay flat, with no tags (measured). Reading: the outliers
  score their danger, the control scores nothing in particular (inferred; a hypothesis
  about cause). Don't pick BPM from this sheet.

## Steal list
| Technique | Measured range | Works when | Backfires when | HyperFrames recipe |
|---|---|---|---|---|
| Frame-1 narration, no title card | first word 0.0s; action under way in frame 1 (3/3) | any narrated Short | the first frame is unreadable without context | voice track `data-start="0"`; the first scene starts mid-motion (`tl.from` a transform already in progress, no fade-in) |
| Life at risk by 1.5s | disaster at 1.0-1.5s (p832whe8hrI); ordeal in frame 1 (NdKRD1j9juE) | survival, safety, "what would you do" | the stakes are fake or clickbait | open on the danger scene; move context to ~60% of runtime |
| "But" ladder | 2-4 turns, 9-10s apart (outliers only, hypothesis) | problem-solution stories | each "but" is trivial | one sub-composition per attempt; each ends on a 6f red failure flash |
| Hold the answer late | answer at 61-83% of runtime (outliers) | question titles, "how did he survive" | the payoff is weak; late answers then feel like a cheat | put the answer scene at `0.75 × duration`; everything before it is an attempt |
| One-second caption cards | 2-4 words, ~1 per second, ~78% height | 160-200 wpm narration | faces or products at that height | group transcript words 2-4 per card; `opacity 0→1` in 2f; no motion |
| Glow the named noun | 7-8 per Short, synced to the word | a moving camera under dense narration | every object glows | masked cut-out with `drop-shadow(0 0 12px var(--glow))`, in over 4f, hold 1-1.5s |
| Camera-move joins over hard cuts | 2-4 hard cuts per 36-54s; median shot 4.7-13.6s | 3D or illustrated worlds | live-action talking heads | zoom-through: scene A `scale 1→6` `power3.in` 0.4s around the object, scene B `scale 0.6→1` `power3.out` at the same time |
| Score the danger inside a flat mix | 2-3 LU swell and bass share up to 0.34 on the danger beats; LRA still 2.1-2.3 | survival and dread stories | trivia and process, where there is no danger to score | automate the bed: +2 LU and a low-shelf boost over the danger scene, −2 LU for the waiting beat; keep the voice fixed |
| Gapless loud bed | LRA 2.0-2.3 LU, 0 silences | narration-led Shorts | calm or reflective topics; also mix to −14 LUFS, since the −11 LUFS here gains nothing on YouTube (inferred) | bed track for the full duration under the voice at −18 to −22 LU, then normalise the render to −14 LUFS, −1 dBTP |
