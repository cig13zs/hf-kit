# Measured styles

| style id | niche | creator measured | format | captions | blocks | mix |
|---|---|---|---|---|---|---|
| archive-essay | documentary | Johnny Harris | 16:9 | none | doc-highlight, progress-badge, film-gate | silence-at-heaviest-line, dip-before-clip |
| world-explainer | animated-explainer | Kurzgesagt | 16:9 | none | world-camera, pill-label, chapter-card, ui-window | voice-first-flat, pause-at-turn, fade-under-end-card |
| build-payoff | science-entertainment | Mark Rober | 16:9 | none | progress-badge | payoff-lift, pause-at-turn |
| challenge-metronome | challenge-spectacle | MrBeast | 16:9 | punch | progress-badge, number-card | tension-bed |
| proof-review | tech-review | Marques Brownlee | 16:9 | none | number-card | pause-at-turn |
| screen-news | tech-news-screen | Fireship | 16:9 | punch | doc-highlight, chapter-card | dip-before-clip |
| series-gameplay | gaming-longform | Grian | 16:9 | none | none | silence-at-heaviest-line |
| campfire-story | storytelling-true-crime | MrBallen | 16:9 | none | none | silence-at-heaviest-line, tension-bed |
| tasting-tour | cooking | Joshua Weissman | 16:9 | keyword | number-card, tier-board | pause-at-turn |
| block-lesson | kids-education | Numberblocks | 16:9 | none | progress-badge, world-camera | pause-at-turn |
| calm-teaching | calm-faith | BibleProject | 16:9 | none | chapter-card, world-camera | voice-first-flat, pause-at-turn, exhale-tail |
| drawn-storytime | animated-storytime | JaidenAnimations | 16:9 | none | none | silence-at-heaviest-line, thin-bed-lift-in-pauses |
| facts-short | shorts-facts | Zack D. Films | 9:16 | cards | zoom-through | gapless-bed |
| news-short | shorts-gaming | KreekCraft | 9:16 | karaoke | face-banner-stack, doc-highlight | none |
| podcast-clip | shorts-podcast | The Diary Of A CEO | 9:16 | speaker | question-card, number-card | none |
| one-take-trick | shorts-vfx | Zach King | 9:16 | cards | blur-swap | pause-at-turn |

`tools/scaffold.py --style` loads a style's tokens and blocks; `tools/check.py --style` compares a render with its measured ranges.
