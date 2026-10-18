# hf-kit blocks

Each file is a HyperFrames sub-composition. Set the host `data-composition-id` to the filename stem and pass overrides through `data-variable-values`.

| Block | Format | Source row | Variables |
|---|---|---|---|
| `pill-label` | 16:9 or 9:16 | animated-explainer: Pill label on first appearance | `text`, `actorColor`, `enterAt`, `holdSeconds` |
| `chapter-card` | 16:9 or 9:16 | animated-explainer: Spoken chapter card | `title`, `backgroundColor`, `textColor` |
| `number-card` | 16:9 or 9:16 | tech-review: Numbers as cards, nothing else; challenge-spectacle: Outlined money type | `number`, `label`, `variant` (`clean` or `money`), `accentColor` |
| `progress-badge` | 16:9 or 9:16 | challenge-spectacle: One progress device | `caption`, `changes` (JSON `[{"t":0,"value":"10"},...]`), `badgeColor` |
| `question-card` | 9:16 only | shorts-podcast: Question card over a stacked split | `question`, `topLabel`, `bottomLabel`, `cardColor` |
| `doc-highlight` | 16:9 or 9:16 | documentary: Highlighted source document | `heading`, `before`, `highlight`, `after`, `highlightColor`, `revealAt` |
| `film-gate` | 16:9 or 9:16 | documentary: Film-gate archive look | `radiusPx`, `blurPx`, `spreadPx`, `shadowColor` |
| `world-camera` | 16:9 | animated-explainer: Long take through one world | `landmarks` (JSON `[{"x","y","text"}]` in world px; the world is 2x the frame), `stations` (JSON `[{"t","at" or "focus":[x,y],"scale"}]`), `title`, `accentOverride` |
| `ui-window` | 16:9 or 9:16 | animated-explainer: UI window as evidence | `title`, `message`, `progress`, `accentOverride` |
| `tier-board` | 16:9 | cooking: Scoring spine carried to a champion | `title`, `items` (JSON `[{"label","tier","t","img"?,"winner"?}]`), `winnerTime`, `positiveOverride` |
| `face-banner-stack` | 9:16 only | shorts-gaming: Face-banner-content stack (`topic-top` mode puts a rounded 16:9 topic box at the top) | `layout`, `banner`, `faceLabel`, `contentLabel`, `topicLabel`, `bannerOverride` |
| `zoom-through` | 16:9 or 9:16 | shorts-facts: Camera-move joins over hard cuts | `fromLabel`, `toLabel`, `transitionTime`, `objectX`, `objectY`, `accentOverride` |
| `blur-swap` | 16:9 or 9:16 | shorts-vfx: One-take look, Transformation on camera | `beforeText`, `afterText`, `swapTime`, `frames` (4-6), `fps`, `accentOverride` |
