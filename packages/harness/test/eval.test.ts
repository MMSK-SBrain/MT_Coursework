import { describe, expect, it } from "vitest";
import { mkdtemp, readdir, readFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { main, parseArgs } from "../eval/run.js";
import { EVAL_COURSES } from "../eval/briefs.js";
import type { ChatClient, ChatRequest } from "../src/openrouter.js";
import { goodReview } from "./helpers.js";
import { OUTCOMES_RUBRIC } from "../src/prompts/review.js";

describe("eval CLI", () => {
  it("has at least 5 fixed briefs", () => {
    expect(EVAL_COURSES.length).toBeGreaterThanOrEqual(5);
  });

  it("exits with a clear message when OPENROUTER_API_KEY is missing", async () => {
    const errs: string[] = [];
    const code = await main([], {}, { err: (s) => errs.push(s), log: () => {} });
    expect(code).toBe(2);
    expect(errs.join("\n")).toMatch(/OPENROUTER_API_KEY is not set/);
  });

  it("rejects unknown stages", () => {
    expect(() => parseArgs(["--stages", "nope"])).toThrow(/unknown stage/);
  });

  it("runs end to end with a fake client and writes JSON + markdown", async () => {
    const course = EVAL_COURSES[0]!;
    // Answer the outcomes prompt with the course's own outcomes and the reviewer with full marks.
    const client: ChatClient = {
      async chat(req: ChatRequest) {
        const isReview = req.messages[0]!.content.includes("strict, experienced instructional designer");
        const content = isReview
          ? JSON.stringify(goodReview(OUTCOMES_RUBRIC.criteria.map((c) => c.id)))
          : JSON.stringify({
            objectives: course.objectives.map(({ id, text }) => ({ id, text })),
            outcomes: course.outcomes.map(({ id, text, bloom, moduleIds, objectiveIds, roleIds, origin }) => ({ id, text, bloom, moduleIds, objectiveIds, roleIds, origin })),
          });
        return { content, model: req.model, costUsd: 0.0005, promptTokens: 1, completionTokens: 1 };
      },
    };
    const out = await mkdtemp(join(tmpdir(), "cg-eval-"));
    const code = await main(["--models", "fake/a", "--stages", "draftOutcomes", "--briefs", course.id, "--judge", "fake/judge", "--out", out], {}, { client, log: () => {} });
    expect(code).toBe(0);
    const files = await readdir(out);
    expect(files.filter((f) => f.endsWith(".json"))).toHaveLength(1);
    const md = await readFile(join(out, files.find((f) => f.endsWith(".md"))!), "utf8");
    expect(md).toContain("| draftOutcomes | `fake/a` | 1/1 | 1.00 |");
  });
});
