import { describe, expect, it } from "vitest";
import { z } from "zod";
import { extractJson, runStage, StageValidationError } from "../src/runner.js";
import type { PromptModule } from "../src/prompts/types.js";
import { OUTCOMES_RUBRIC } from "../src/prompts/review.js";
import { ScriptedClient, badReview, fixedNow, goodReview, testConfig } from "./helpers.js";

const prompt: PromptModule<{ n: number }, { items: string[] }> = {
  id: "test.items", version: "7", system: "sys", user: (i, ctx) => `n=${i.n} ${ctx.examples}`,
  output: z.object({ items: z.array(z.string()).min(1) }),
};
const mustHaveB = (o: { items: string[] }) => (o.items.includes("b") ? [] : ['items must include "b"']);
const deps = (client: ScriptedClient) => ({ client, config: testConfig, now: fixedNow });
const ids = OUTCOMES_RUBRIC.criteria.map((c) => c.id);

describe("extractJson", () => {
  it("handles fences and chatter", () => {
    expect(extractJson('```json\n{"a":1}\n```')).toEqual({ a: 1 });
    expect(extractJson('Sure! {"a":[1,2]} hope this helps')).toEqual({ a: [1, 2] });
    expect(() => extractJson("no json")).toThrow();
  });
});

describe("runStage", () => {
  it("returns validated output with provenance", async () => {
    const c = new ScriptedClient([{ items: ["b"] }]);
    const r = await runStage({ stage: "draftPlan", prompt, input: { n: 1 }, builtFrom: ["LO1", "LO1", "M2"], rules: mustHaveB }, deps(c));
    expect(r.value).toEqual({ items: ["b"] });
    expect(r.warnings).toEqual([]);
    expect(r.provenance).toEqual({ model: "test/draftPlan", promptId: "test.items", promptVersion: "7", costUsd: 0.001, createdAt: "2026-11-04T12:00:00.000Z", builtFrom: ["LO1", "M2"] });
    expect(c.requests[0]!.messages[1]!.content).toBe("n=1 ");
  });

  it("retries once with validation errors appended", async () => {
    const c = new ScriptedClient(["not json at all", { items: [] }, { items: ["b"] }]);
    const r = await runStage({ stage: "draftPlan", prompt, input: { n: 1 }, builtFrom: [] }, deps(c)).catch((e) => e);
    // call 1 invalid JSON -> retry (call 2) still invalid -> fallback model full attempt (call 3) valid
    expect(r.value).toEqual({ items: ["b"] });
    expect(c.requests[1]!.messages.at(-1)!.content).toMatch(/did not match the required shape/);
    expect(c.requests[2]!.model).toBe("test/draftPlan-fallback");
    expect(r.trace.validationRetries).toBe(1);
    expect(r.provenance.costUsd).toBeCloseTo(0.003);
  });

  it("throws StageValidationError when primary and fallback both fail", async () => {
    const c = new ScriptedClient(["x", "x", "x", "x"]);
    await expect(runStage({ stage: "draftPlan", prompt, input: { n: 1 }, builtFrom: [] }, deps(c))).rejects.toBeInstanceOf(StageValidationError);
  });

  it("repairs rule failures once, and keeps survivors as warnings", async () => {
    const fixed = new ScriptedClient([{ items: ["a"] }, { items: ["a", "b"] }]);
    const r1 = await runStage({ stage: "draftPlan", prompt, input: { n: 1 }, builtFrom: [], rules: mustHaveB }, deps(fixed));
    expect(r1.value.items).toEqual(["a", "b"]);
    expect(r1.trace.ruleRepair).toBe("accepted");
    expect(fixed.requests[1]!.messages.at(-1)!.content).toMatch(/items must include "b"/);
    expect(r1.warnings).toEqual([]);

    const stubborn = new ScriptedClient([{ items: ["a"] }, { items: ["c"] }]);
    const r2 = await runStage({ stage: "draftPlan", prompt, input: { n: 1 }, builtFrom: [], rules: mustHaveB, advisories: () => ["advisory"] }, deps(stubborn));
    expect(r2.value.items).toEqual(["a"]);
    expect(r2.trace.ruleRepair).toBe("rejected");
    expect(r2.warnings).toEqual(['items must include "b"', "advisory"]);
  });

  it("runs rubric review and one repair below threshold", async () => {
    const c = new ScriptedClient([{ items: ["b"] }, badReview(ids), { items: ["b", "better"] }]);
    const r = await runStage({ stage: "draftOutcomes", prompt, input: { n: 1 }, builtFrom: [], rules: mustHaveB, rubric: { rubric: OUTCOMES_RUBRIC, contextText: "ctx" } }, deps(c));
    expect(c.requests[1]!.model).toBe("test/review");
    expect(c.requests[2]!.messages.at(-1)!.content).toMatch(/LO2 is vague/);
    expect(r.value.items).toEqual(["b", "better"]);
    expect(r.trace.rubric).toMatchObject({ score: 0.25, repaired: true });

    const good = new ScriptedClient([{ items: ["b"] }, goodReview(ids)]);
    const r2 = await runStage({ stage: "draftOutcomes", prompt, input: { n: 1 }, builtFrom: [], rubric: { rubric: OUTCOMES_RUBRIC, contextText: "ctx" } }, deps(good));
    expect(r2.trace.rubric).toMatchObject({ score: 1, repaired: false });
    expect(good.requests).toHaveLength(2);
  });
});
