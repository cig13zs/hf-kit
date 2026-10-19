# The floating tree illusion (Zach King)

https://www.youtube.com/shorts/tOIFZ8O6Ezk · 0:11 vertical Short · 4.0M views · **control, 1.08× channel median**
· uploaded 2026-05-30 · checked 2026-09-26 · data: `data/tOIFZ8O6Ezk.json`

| Measure | Value |
|---|---|
| Hard cuts/min (floor) | **0** in every segment: 0-3s, 3-11s |
| Shot length | 0 detected cuts; one 11s shot. A blurred turn at 0:07.6-0:08.4 could hide a join (inferred) |
| Visual energy | 1.34 (one value; the highest of the three in this niche) |
| On-screen text | 0%: no captions or titles (seen) |
| Speech | 11 words, 60 wpm, first word at 3.44s |
| Audio | −13.7 LUFS, LRA 11.1 LU, 0 silences over 0.4s, onsets 76.4/min |
| Loudness curve | a steady climb: −22.1 (2s), −20.3 (4s), −19.2 (6s), −12.6 (8s), −9.7 (10s). About 12 LU from start to the fall |
| Music | tempo estimate 107.7 BPM, confidence 1.26 (measured); cuts-on-onsets lift not computable (no cuts); brightness 1579 Hz; bass share 0.277; no caption [music] tags |

## 1. Idea and promise
The title names the trick and calls it an illusion. Frame 1 shows it at once: a tree trunk
hanging in the air above its own cut stump, with a man working underneath (seen, 0:00). The
curiosity gap (how is it floating) is never explained; the video turns into a slapstick
fall instead. With the word "illusion" in the title, the viewer is told in advance that
it's a trick (inferred).

## 2. Hook (0-3s, then to 11s)
- 0:00.0 Low handheld angle: the floating trunk, the stump below, and a man in a green
  shirt and apron crouched between them with a palette of paint cups (seen).
- 0:00-0:03.4 No speech (measured first word at 3.44s). The camera circles closer (seen).
- 0:03.4 A short spoken line while he works under the trunk (transcript).
- 0:04.5-0:07.5 The camera pushes in under the trunk; he looks up at it (seen).
- 0:07.6-0:08.4 He turns, drops the palette and runs (seen); exclamations in the transcript.
- 0:08.9-0:10.6 The trunk tips and falls; it lands across him (0:10.6-0:10.9) (seen).
- Hook type: an impossible state shown from frame 1, then a slapstick payoff.

## 3. Structure
Floating trunk and worker (0:00-0:07.5) → alarm and escape attempt (0:07.6-0:08.8) → the fall
(0:08.9-0:10.6) → pinned under the trunk, end (0:10.6-0:11) (all seen). One setup, one
payoff, no second turn.

## 4. Editing style
No detected cuts. A single handheld take moves in close under the trunk, then swings wide
to catch the fall (seen). The camera moves more here than in the two outliers (visual
energy 1.34 against 0.68-0.79, measured), and the blurred turn at 0:07.6-0:08.4 is the
likely seam (inferred).

## 5. Graphics and animation
None as overlays (seen). Bright daylight, blue sky, a garden fence and flowers; natural
colour, no visible grade (seen).

## 6. VFX and transitions
- Floating object (the trunk): present from frame 1 (seen).
- Falling object landing on the performer: once, at the end (seen).
- No transitions, flashes or ramps seen.

## 7. Sound (measured only)
- **A 12 LU climb** from −22.1 at 2s to −9.7 at 10s (measured). The loudest reading is the
  fall. A build into a crash is the likely source: rising music, shouting, the impact
  (inferred).
- −13.7 LUFS integrated, LRA 11.1 LU, no silences, onsets 76.4/min (measured).
- Speech starts at 3.44s and stays sparse (11 words) (measured).
- Music block: tempo estimate 107.7 BPM at confidence 1.26, brightness 1579 Hz, bass share 0.277, no caption [music] tags; cuts-on-onsets lift not computable (measured).

## 8. Retention mechanics: why
- Impossible state in frame 1. The strangeness is visible at once. Job: resetting
  attention.
- Push-in under the trunk. Putting the camera, and the worker, under the danger builds
  dread. Job: building tension.
- The fall on a rising sound curve. Loudness climbs into the crash. Job: showing a
  payoff, with sound doing the build.
- What it lacks: no transformation on camera, no question to the viewer, no second beat.

## 9. Control against the outliers
Outliers: 5jhEoRZXhjE (44.3×, a famous mural whose ladder and balloon become real) and
X0wxLr5W2X8 (14.05×, a cake-or-fake guessing game). All three share zero cuts, a handheld
single-take look, no captions over the effect, and the creator performing on camera. What
the outliers do that this one doesn't, all hypotheses:
- A transformation on camera. Flat becomes real, or objects turn out to be something
  else; here the impossible thing is already there in frame 1.
- Borrowed attention: a world-famous artwork, or a trend format the feed knows.
- **Two or three reveals** against one.
- **A title that asks or claims** against a title that labels the trick an illusion.
- **A calmer camera** (0.68-0.79 against 1.34, measured) that lets the trick read.
It also has the highest likes per view of the three (1.47% against 0.51-0.59%, measured):
it seems to have reached mostly the existing audience (inferred).

## 10. Steal list
| Technique | Measured range | Works when | Backfires when | HyperFrames recipe |
|---|---|---|---|---|
| Sound-led build into a crash | +12 LU over 8s, peak on the impact | slapstick and disaster payoffs | the payoff is quiet or emotional | audio group gain automation from −22 to −10 LUFS over the build; an impact on the landing frame |
| Impossible state in frame 1 | visible at 0.0s | a strong single image | the image alone gives the whole joke away (as here) | open on the effect scene; no title or caption |
| Push-in under the danger | 3s push, 4.5-7.5s | tension before a fall or reveal | the move blurs the trick | `scale 1→1.25` over 3s `sine.in`, anchored on the hazard |
| Avoid: naming the trick | "illusion" in the title | tutorial or behind-the-scenes posts | the Short depends on wonder (outliers asked or claimed instead, hypothesis) | title as a question or claim, not a label |
