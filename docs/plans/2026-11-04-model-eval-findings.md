# Model evaluation findings (2026-11-04)

Status: **paused**. The OpenRouter key hit its $5.00 monthly limit ($5.02 used; resets 2026-12-01). The rerun after the fixes is incomplete.

## Setup

- **Tool:** `pnpm --filter @cg/harness eval -- --models a,b --stages ... --briefs ... --judge ... --max-usd N`. Raw results are in `packages/harness/eval-results/`, which is gitignored and local only.
- **Briefs:** `ev-powertrain-diploma`, `aezc516-ice`, `school-electrical-safety`, from `packages/harness/eval/briefs.ts`.
- **Stages:** `draftOutcomes`, `proposeFit` and `draftHourPlan`.
- **Judge:** `anthropic/claude-sonnet-5.5`, scoring 1–5 per rubric criterion, mapped to 0–1 as (score − 1)/4. The pass threshold is 0.75, which means an average of 4 out of 5.
- **Prices:** model ids and prices were taken from openrouter.ai on 2026-11-04. The ids in `packages/harness/src/config.ts` are still placeholders.

## Run 1: six models, before the fixes (54 runs, $3.70)

| Model | Mean score | Model cost, 9 outputs | Mean latency | Failures |
|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 (baseline) | 0.60 | $0.85 | 53 s | 0 |
| z-ai/glm-5.3-flash | 0.54 | $0.17 | 26 s | 0 |
| z-ai/glm-5.3 | 0.52 | $0.22 | 34 s | 0 |
| deepseek/deepseek-v4-pro-0813 | 0.51 | $0.34 | 100 s | 2 timeouts (120 s) on draftOutcomes |
| qwen/qwen3.8-flash | 0.49 | $0.17 | 89 s | 0 |
| qwen/qwen3.7-plus | 0.43 | $0.24 | 122 s | 0 |

By stage:
- **Mean calls per output:** draftOutcomes and proposeFit took 3–4 calls (retry, rule repair, rubric repair). draftHourPlan took 1–1.7.
- **Accepted outputs:** no model, the Claude baseline included, had any output reach 0.75.
- **Cost against attempts:** paying more did not reduce the number of attempts. DeepSeek cost twice as much as GLM 5.3 Flash, scored lower and was four times slower. Sonnet still needed about 3 calls per outcome draft.

**Provisional choice: GLM 5.3 Flash.** It reaches about 90% of the baseline score at about 20% of the cost, and it is the fastest model tested.

## Why scores were low

Six outputs were re-judged with the judge's reasons kept (GLM 5.3 Flash and Sonnet on aezc516-ice, all three stages).

1. **Unfair judging (eval fault).** The judge saw only module titles, while the model saw roles, skills, objectives and the earlier outcomes. Correct content was therefore marked as invented, for example INCA from a role's skills and CO1.
2. **Placeholder test data (eval fault).** The briefs used a generic "CO1" objective and example.org evidence links.
3. **Real quality problems, shared by Claude and GLM:**
   - durations written in a block disagree with its minutes; the prompt's "insert a 10-minute break" rule caused a 10-minute break in a 5-minute block;
   - `academicConflict` is misused for "no conflict" notes;
   - fit changes are not ordered by importance;
   - there is no individual practice before group work;
   - quick checks have no expected answers;
   - outcomes chain several variables;
   - handout outcomes are dropped;
   - tools are named that are not in the context;
   - index tags such as "[0]" leak into learner-facing text.
4. **A latent scoring risk.** A criterion the judge leaves out counts as 1, which is 0. The judge did sometimes omit `score`. Schema validation retries this, but nothing guards against a missing criterion.

## Fixes made (commit bb6b572)

- **Judge context.** The reviewer, both inline and in the eval, judges against the exact facts the model was given: the model's user prompt without the worked examples (`StageTrace.facts`).
- **Test briefs.** Each brief has 2–3 real objectives, and the placeholder links are removed.
- **Prompts:**
  - draftHourPlan v4: durations must match block minutes; individual practice comes before group work; checks are written as "Question? Expected: …"; no index tags in learner text.
  - proposeFit v3: changes ordered by importance; `academicConflict` only for real conflicts, naming the id; only ids from the context.
  - draftOutcomes v3: atomic outcomes, aiming for 6–8 LOs; handout intent kept; tools only from the context.
- **Code checks that trigger a repair:**
  - a duration in a block's text longer than the block;
  - "no conflict" text in `academicConflict`.
- **Eval rows** now keep the output and the judge's issues.
- **Earlier the same day:**
  - The reasoning budget is capped at half of max_tokens (default 2048), and max_tokens defaults to 8192. Qwen 3.8 Flash had used all 4096 tokens on reasoning and returned no content.
  - The eval has a `--max-usd` cap that counts the cost OpenRouter reports, including on failed calls.
  - The report adds "mean calls" and "cost per accepted output".

## Run 2: after the fixes (incomplete; the key limit was hit)

| Stage | Brief | GLM 5.3 Flash, run 1 → run 2 | Claude Opus 5.5 |
|---|---|---|---|
| draftOutcomes | ev-powertrain-diploma | 0.38 → 0.46 | 0.63 |
| proposeFit | ev-powertrain-diploma | 0.63 → 0.58 | **0.79 (first pass)** |
| draftHourPlan | ev-powertrain-diploma | 0.50 → 0.50 | judge cut off by the limit |
| draftOutcomes | aezc516-ice | 0.58 → 0.54 | not run |

- **GLM after the fixes:** its scores barely moved. Unfair judging was not the main cause of the gap.
- **Opus:** the only model to pass 0.75 so far, at about 10 times GLM's cost per output ($0.11–0.24 against about $0.02).
- **Sample size:** too few results to decide on a model.

## When resuming

1. Raise the OpenRouter key's monthly limit (about $15), or wait for the reset on 2026-12-01.
2. Rerun only the missing rows. Estimated cost is about $3.
   ```
   pnpm --filter @cg/harness eval -- --models z-ai/glm-5.3-flash,anthropic/claude-opus-5.5 \
     --stages draftOutcomes,proposeFit,draftHourPlan \
     --briefs ev-powertrain-diploma,aezc516-ice,school-electrical-safety \
     --judge anthropic/claude-sonnet-5.5 --max-usd 4
   ```
3. Read the saved GLM outputs alongside the judge's issues (`row.output` and `row.issues` in the eval JSON), and decide between:
   - (a) more prompt work;
   - (b) structural changes, for example drafting outcomes one module at a time, or more narrow calls;
   - (c) a hybrid, with the cheap model for most stages and a stronger model only where it passes (Opus or Sonnet for course–job fit).
4. Consider whether 0.75 is the right bar. Sonnet averaged 0.60, so the bar is strict. Calibrate it against a human rating of a few outputs.
5. Guard the scoring: treat a missing criterion as a reviewer error and retry, not as a score of 1.
6. Put the winning model ids in `packages/harness/src/config.ts`.
7. Make the tool save results after each row. It currently writes only at the end, so a stopped run loses everything.
