# Tech review: niche DNA

Channel: Marques Brownlee (median 4.7M views over the last 30 uploads). The videos:
- [Od6M0AXpcxQ](../cards/tech-review/Od6M0AXpcxQ.md), "iPhone 18 Pro/Duo Impressions:
  Mogged": outlier, 5.7×, 17:14.
- [6D__H_DO2Xk](../cards/tech-review/6D__H_DO2Xk.md), "iPhone Duo: What We Missed!": recent
  outlier, 2.6×, 10:36.
- [ANmTVYkEtLw](../cards/tech-review/ANmTVYkEtLw.md), "Google Pixel 11/Pro Review: Poker
  Face": control, 1.02×, 12:27.

Checked 2026-09-26.

**Read this first:** both outliers cover the first folding iPhone in its launch week. The
brief lists views that come from a news event as a skip reason. SAMPLE.md kept them, so
every outlier-against-control finding below is weaker than usual.

## Ranges table
Hard cuts are floors. OCR text shares are also floors in this niche: it missed price cards,
charts and labels that are visible in the frames.

| Measure | Min (video) | Max (video) | Outliers only |
|---|---|---|---|
| Cuts/min overall | 5.5 (Od6M) | 7.4 (6D, ANm) | 5.5-7.4 |
| Cuts/min 0-15s | 8.0 (6D) | 16.0 (Od6M) | 8.0-16.0 |
| Cuts/min 15-60s | 9.3 (Od6M) | 16.0 (ANm, skit) | 9.3-12.0 |
| Cuts/min 1-3 min | 8.5 (6D) | 9.0 (Od6M, ANm) | 8.5-9.0 |
| Cuts/min body | 4.5 (Od6M) | 6.7 (6D) | 4.5-6.7 |
| Cuts/min last minute | 6.0 (Od6M, 6D) | 7.0 (ANm) | 6.0 |
| Median shot | 5.6s (ANm) | 8.0s (Od6M) | 5.8-8.0s |
| Shot p10-p90 | 2.3-16.0s (ANm) | 3.4-17.3s (Od6M) | 2.7-17.3s |
| Longest take | 45.8s (ANm) | 103.6s (Od6M) | 49-104s |
| First cut | 4.5s (Od6M) | 7.5s (ANm) | 4.5-6.5s |
| Visual energy per minute | 0.21 (Od6M, verdict) | 0.90 (ANm, minute 2) | 0.21-0.72 |
| On-screen text share (OCR floor) | 0% (6D) | 3% (Od6M, ANm) | 0-3% |
| Speech wpm | 176.4 (ANm) | 200.7 (Od6M) | 200.5-200.7 |
| Speech wpm, first 30s | 22 (ANm) | 194 (Od6M) | 188-194 |
| First spoken word | 2.36s (6D) | 16.32s (ANm) | 2.36-2.4s |
| Integrated loudness | −17.0 LUFS (ANm) | −15.9 LUFS (Od6M) | −16.7 to −15.9 |
| LRA | 4.1 LU (ANm) | 5.0 LU (6D) | 4.6-5.0 |
| Body loudness spread (p10-p90) | 3.6 LU (ANm) | 4.2 LU (6D) | 3.9-4.2 |
| Silences/min | 3.94 (ANm) | 5.09 (6D) | 4.87-5.09 |
| Speech gaps of 1s+/min (caption proxy) | 5.00 (6D) | 5.46 (ANm) | 5.00-5.22 |
| Onsets/min | 88.9 (6D, ANm) | 91.4 (Od6M) | 88.9-91.4 |
| Cuts landing in speech pauses (lift) | 0.74 (6D) | 0.92 (ANm) | 0.74-0.76 |
| Music lift (cuts on audio onsets) | 1.23 (Od6M) | 1.51 (6D) | 1.23-1.51 |
| Tempo | 69.8 BPM, confidence 1.05 (Od6M) | 136 BPM, confidence 1.80 (6D) | 69.8-136 BPM |

## Shared devices (the house style)
Seen or measured in all three:
- **A-roll for judgement, hands-on b-roll for facts.**
  - The A-roll is the presenter to camera in a lit room: warm lamps (Od6M), a white studio
    with a red panel (6D), a dark set with pink window light (ANm).
  - The b-roll is macro and hand-held product shots with shallow depth of field, often on a
    magenta backdrop or with pink accents.
- **B-roll under continuous talk.** Cuts land in speech pauses at or below chance (lift
  0.74-0.92). The voice runs across the cut; this is the L-cut workflow.
- **The verdict in one long take.** 45.8-103.6 seconds without a cut, where visual energy
  falls to 0.21-0.33.
- **Hard cuts only.** No whip, zoom, glitch or wipe was seen. The only designed transitions
  are the channel ident and one iris (Od6M, 6D).
- **Graphics only for numbers.** Price cards, a benchmark chart, a wattage label, a spec
  card. There are none in the biggest outlier.
- **A speech-led mix.** Flat level (3.6-4.2 LU body spread), 3.9-5.1 open silences a minute,
  and music only at the edges (see the profile below).
- **The sponsor after the content,** with an "AD" label bottom-left (Od6M, ANm; 6D has no
  sponsor).
- **About 200 wpm in the outliers** (176 in the control): density comes from the voice, not
  the edit.

## Outlier against control
Every line is a hypothesis.
- **The topic and access dominate.** Both outliers cover a launch-week product people were
  waiting for. One adds event-floor footage, the other an Apple executive interview. The
  control is a routine review. This is the most likely cause of the view gap, and it is not
  an edit.
- **Talk and proof in the first 3 seconds.** The outliers speak at 2.36-2.4s (188-194 wpm in
  the first 30s) over event b-roll or straight to camera. The control spends 73s on a
  music-led poker skit, with its first word at 16.3s and 22 wpm in the first 30s.
- **Faster delivery.** 200.5-200.7 wpm against 176.4.
- **Not differences:**
  - cut rate (6D equals the control at 7.4);
  - median shot;
  - loudness;
  - silences;
  - long verdict takes.
- **Graphics density runs opposite to the views.** Od6M has none, the control has the most.
  That argues graphics are not the driver, not that they hurt.

## Sound and music profile
| Claim | Label |
|---|---|
| Integrated loudness −15.9 to −17.0 LUFS, close to YouTube's reference; LRA 4.1-5.0 LU | measured |
| Flat bodies, with a 3.6-4.2 LU spread | measured |
| 3.9-5.1 silences a minute, mostly 0.4-0.9s, so pauses between phrases are left open | measured |
| Music is tagged only at the edges: Od6M at 0:00.7-0:05.2 and 16:07-17:04 (sponsor); 6D at 0:00.7 and 0:13.0; ANm across the skit (0:00-0:58), then 11:06-12:24 | measured (caption tags) |
| Bass share rises where music is tagged: ANm skit 0.37-0.60, Od6M sponsor 0.30-0.44, 6D intro 0.27-0.31 and outro 0.40, against 0.14-0.24 under talk | measured |
| The review body carries no bed or a very low one | inferred from open silences plus no tags |
| The knowledge chapter's "light bed or absent under talking head" is confirmed. Its "music up on b-roll" is **not** seen: b-roll inside the body carries no tagged music | measured tags against a practice claim |
| Silence is comic timing: the subscribe gag (Od6M, silences of 0.85-1.2s, a −26.4 dip), the archival "No" (6D, a 2.6s gap), reading prices (6D, 0.55-0.97s) | measured, with the purpose from the transcript |
| The ANm skit's dark, bass-heavy sound returns at the callback (bass 0.45-0.49, brightness 642-926 Hz), a musical bookend | measured; the "same cue" is inferred |
| No clear beat in any of the three | measured |
| Onsets of 89-91 a minute are dominated by syllables at 176-200 wpm | inferred |

## Steal list
| Technique | Measured range | Works when | Backfires when | HyperFrames recipe |
|---|---|---|---|---|
| Talk in the first 3 seconds | first word at 2.36-2.4s; 188-194 wpm in the first 30s | any review or explainer with a clear promise | the presenter has nothing new to say yet | VO or A-roll `data-start ≤ 2.5`; ident ≤ 2s |
| Proof-footage open | 4 b-roll shots about 2s apart under the VO, face at 10.7s (Od6M) | first-hand or exclusive footage | stock or generic footage | 4 b-roll clips at 2.4/4.5/7.0/8.9s over one continuous VO; A-roll from 10.7s |
| B-roll under continuous talk | cut-in-pause lift 0.74-0.92; 8.5-12 cuts/min in feature runs | spec walkthroughs | the b-roll doesn't show the noun being said | one continuous A-roll audio track; b-roll clips placed on nouns from the caption timings |
| Verdict in one take | 45.8-103.6s, no cut; visual energy 0.21-0.33 | an established, trusted voice at 175-200 wpm | a slow or unknown presenter | a single A-roll clip; no music; no graphics |
| Music only at the edges | tags in the first 0-60s and the sponsor/outro only; bass 0.3-0.6 there, 0.14-0.24 under talk | talk-led reviews | a channel that needs a bed to hide room noise | music clips only in the intro and outro scenes; room tone under the body |
| Numbers as cards, nothing else | 0-5 graphic cards a video | prices, benchmarks, wattage | decorative labels on non-numeric claims | white rounded card, numerals 96px bold, caps label 20px; `y 20→0, opacity 0→1` 0.4s `power3.out` on the spoken number |
| Silence as comic timing | gaps of 0.85-2.6s; dips to −24/−26 LUFS | a recurring gag, a punchline, a CTA | serious or safety content | cut the A-roll with 1-2.5s of room tone; nothing else on the track |
