# @cg/video

Implements `VideoBuilder` from `@cg/core` on top of explainroo (`EXPLAINROO_DIR`, default `/Volumes/Dev/explainroo`; never modified).

- `createVideoBuilder({ maxSec, targetSec, media }).plan(course, planId, sessionId)` builds a `VideoProject` from the session (outcomes, hour blocks, industry examples, style) with templates. `planKind(..., kind)` overrides the session's kind (still checked against `VIDEO_BY_PATH`).
- **LLM seam:** `buildProject(outline: ScriptOutline, { kind, path?, maxSec?, media? })`. An LLM only has to produce a `ScriptOutline` (scenes with narration containing `[#marker]`s, plus one typed visual each; see `outline.ts`). `outlineProblems()` validates it.
- `render(project, { workDir, maxSec })`: refuses when `estimatedSec > maxSec` (nothing is written), writes `<workDir>/project`, runs `voice` (real length checked against `maxSec` again), `check` (errors stop the render), then `render`, all with `--json`.
- `pnpm --filter @cg/video sample` writes all five kinds to `out/<kind>/project` and renders the explainroo one (`SAMPLE_RENDER=all` renders all, `=0` none; `SAMPLE_SEC`, `SAMPLE_KINDS`).

`VideoProject.assets` carries `video.json` (and `look.json` for whiteboard) as ordinary assets, plus user media under `assets/`.

## Whiteboard: what works, and what explainroo would need

Built from the `paper` look with a custom `look.json` (white board, marker colours, `boil: 3`): rough.js strokes drawn on with `enter: 'draw'`, text written with `enter: 'write'` in the hand font, stick figures drawn stroke by stroke from `s.circle`/`s.line`, hand-drawn underlines (`s.annotate`).

Missing in explainroo for a real whiteboard-animation look:
1. A visible hand and marker that follows the stroke being drawn (the stroke is revealed without a pen tip).
2. Stroke reveal timed to the narration: `draw` has a fixed `dur`; a "draw this path while this sentence is spoken" option (`dur: 'until:#marker'`) would sync drawing to speech.
3. An erase or wipe element exit (`exit: 'wipe'`/`'scrub'`) so one board can be reused across a scene.
4. Importing line art (SVG with stroke order) as a drawable asset, so a library of figures (cars, packs, benches) can be drawn instead of hand-built stick figures.
5. Marker sound (`scribble` exists, but is not tied to the visible stroke length).

## Images and clips

Already supported by explainroo (`s.image`, `s.clip`, frames `window`/`browser`). Nothing needs adding. `demo` and `screen` videos use `s.clip` for `.mp4/.mov/.webm/.m4v` and `s.image` otherwise; with no media they show a dashed placeholder box. Not available: clips that need a camera crop or picture-in-picture of a face; `s.clip` has `from`/`speed`/`volume` but no crop.

## Core contract changes wanted (not made; core is frozen)

- `VideoProject` has no `kind` or `config` field; `video.json` travels as an asset. A typed `videoJson?: object` and `kind: VideoKind` would be cleaner, and let the app show a "placeholder clips" warning (`placeholders: string[]`).
- `VideoBuilder.plan` has no options (target length, supplied media, voice). They go to the constructor here.
