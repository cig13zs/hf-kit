# oh no 😭 (KreekCraft)

https://www.youtube.com/shorts/qvrxyBRhi_0 · 0:15 vertical Short · 633K views · **control, 1.0× channel median**
· uploaded 2026-09-15 · checked 2026-09-26 · data: `data/qvrxyBRhi_0.json`

| Measure | Value |
|---|---|
| Hard cuts/min (floor) | 16.0 overall · 0-3s: **20.0** (one cut at 1.57s) · 3-15s: 15.0 · no 15-60s or 60s+ segment |
| Shot length | 4 cuts (1.57, 5.57, 9.17, 12.53s), median 3.4s, p10-p90 1.9-3.8s: the most regular rhythm in the niche |
| Visual energy | 1.12 (one value) |
| On-screen text | 63% of sampled frames, 3.9 words per frame |
| Speech | 264 wpm, first word at 0.0s, 66 words in 15s |
| Audio | −13.0 LUFS, LRA 1.5 LU, 0 silences over 0.4s, onsets 104/min |
| Loudness curve | −12.3 to −13.8 LUFS from 2s to 14s, no shape |
| Music | tempo estimate 129.2 BPM, confidence 2.34 (measured); cuts-on-onsets lift not computed (null; 4 cuts); brightness 1056 Hz; bass share 0.03; no caption [music] tags |

## 1. Idea and promise
The title gives no topic, only a reaction and a crying emoji. The first line is a teaser:
players "aren't going to like this" (seen, 0:00). The topic, paid early access to an
anniversary event for subscribers of the paid tier, arrives only from about 1.5-3.4s (seen
in transcript and frames). The curiosity gap is "what's the bad news", and the answer
matters only to the viewers who care about early access.

## 2. Hook (0-3s, then to 15s)
- 0:00.0 Split layout: face top third on the green backdrop, a red banner reading "ROBLOX
  PLUS", and in the lower panel a talking-head clip of an older man with his own burned-in
  subtitle, shown without context (seen). Who he is isn't stated on screen.
- Captions: two stacked lines, yellow and white condensed uppercase, placed right under the
  banner rather than at the bottom (seen).
- 0:01.57 First cut: the lower panel becomes a social post about subscriber early access,
  with a "Play Early" button and a cursor hand drawn over it (seen).
- Hook type: vague negative teaser. The banner names the topic before the voice does.

## 3. Structure
Teaser (0:00-0:01.57) → post on early access (0:01.57-0:05.57) → post announcing the event
with its key art (0:05.57-0:09.17) → background for viewers who don't know the event, then
a second creator's post confirming it (0:09.17-0:12.53) → the key art enlarged, and a closing
line predicting that the comments on this video will be lively (0:12.53-0:15) (all seen).
Every 3.4-4 seconds a new post: the rhythm is regular (measured cut times). The ending
openly invites argument and delivers no result.

## 4. Editing style
Same template as the channel's how-to Short: fixed face, banner, a lower panel that swaps.
Here the swaps are detected as cuts because the panel content changes more of the frame
(cut sheet, seen). Four swaps at nearly even spacing, 3.4-4.0s apart (measured). No
punch-ins, no layout changes (seen).

## 5. Graphics and animation
- Face top, red rounded banner with white bold uppercase "ROBLOX PLUS", captions directly
  under it in two colours, screenshots below (seen).
- A cursor-hand graphic over the "Play Early" button (seen, 0:02-0:05.5).
- No gameplay footage (seen).

## 6. VFX and transitions
None seen besides hard swaps of the lower panel.

## 7. Sound (measured only)
- −13.0 LUFS, LRA 1.5 LU, no silences, a flat 2-second curve (measured). Same flat talk mix
  as the two outliers.
- Onsets 104/min at 264 wpm (measured); speech is the likeliest source (inferred).
- Music block: tempo estimate 129.2 BPM at confidence 2.34, brightness 1056 Hz, bass share 0.03, no caption [music] tags; cuts-on-onsets lift not computed (measured).

## 8. Retention mechanics: why
- **Topic banner from frame 1.** The banner names the subject before the voice does, which
  partly rescues the vague opening line. Job: clarifying.
- **Regular post swaps.** A new screenshot every 3.4-4 seconds. Job: resetting attention.
- **Comment bait at the end.** It invites argument in the comments (0.25% of views,
  measured), but it gives the viewer no payoff to watch for (inferred).
- What's missing: a result, a demonstration, or a stake that touches most viewers.

## 9. Control against the outliers
Outliers: rssMorwX9Ws (3.63×, a how-to) and 2n1rIXEeybM (2.37×, a regional ban). All three
share the face-plus-screenshot template, condensed captions, speech from 0.0s at 215-305
wpm, flat mixes with no silences, and no gameplay. What the outliers do that this one
doesn't, all hypotheses:
- **Name the stake in the first sentence.** Both outliers state the whole claim in line 1;
  this one teases and names it later.
- **Reach most players.** A trick anyone can use, or a ban affecting many kids, against a
  perk for paying subscribers.
- **Show a result or evidence.** The old logo appearing, or kids at a TV, against key art
  for an event not yet out.
- **A title with a topic.** Both outlier titles name the thing; "oh no" doesn't.
This video has the fastest cuts (16/min) and the most even rhythm in the niche, yet the
fewest views, so cut rate isn't the lever here (measured; causal reading is a hypothesis).
It also has the highest likes per view (2.4% against 1.7-2.1%, measured): its narrower
audience may be the most loyal one (inferred).

## 10. Steal list
| Technique | Measured range | Works when | Backfires when | HyperFrames recipe |
|---|---|---|---|---|
| Topic banner | on screen 100% of runtime | a vague or emotional first line | the banner repeats the caption word for word | red rounded rect at ~35% height, white 900-weight uppercase, static |
| Even screenshot swaps | a new post every 3.4-4.0s | news assembled from several sources | the posts say the same thing | one image clip per post; `data-start` every 3.6s; no transition |
| Cursor-on-button graphic | one 4s hold | features, buttons, "how to get it" | nothing is clickable in the story | cursor PNG with `x/y` tween to the button, `scale 1→0.9→1` over 6f as a click |
| Avoid: vague teaser opener | topic named at ~1.5-3.4s, not 0s | an audience that already trusts the creator | cold viewers; both outliers named the stake at 0s (hypothesis) | put the concrete claim in caption group 1 |
