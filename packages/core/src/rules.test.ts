import { describe, expect, it } from "vitest";
import { hourBlockProblems, outcomeVerbProblem, uncoveredOutcomes, videoAllowed } from "./rules.js";
import type { HourBlock, LearningPlan, Outcome } from "./model.js";

const prov = { model: "test", promptId: "t", promptVersion: "1", costUsd: 0, createdAt: "2026-11-04T00:00:00Z", builtFrom: [] };
const block = (hour: number, startMin: number, minutes: number): HourBlock => ({
  id: `b${hour}-${startMin}`, hour, startMin, minutes, kind: "teach", title: `b${startMin}`, activity: "x",
  outcomeIds: [], style: "teaching", check: [], needsSlides: false, provenance: prov,
});

describe("rules", () => {
  it("flags vague and wrong-level verbs", () => {
    expect(outcomeVerbProblem({ text: "Understand the V-model", bloom: "understand" })).toMatch(/unmeasurable/);
    expect(outcomeVerbProblem({ text: "Describe the V-model", bloom: "evaluate" })).toMatch(/evaluate-level/);
    expect(outcomeVerbProblem({ text: "Evaluate two BMS designs", bloom: "evaluate" })).toBeNull();
  });
  it("checks hour blocks add up", () => {
    expect(hourBlockProblems([block(1, 0, 20), block(1, 20, 40), block(2, 0, 60)], 120)).toEqual([]);
    expect(hourBlockProblems([block(1, 0, 20), block(1, 25, 30)], 60)).toHaveLength(2);
    expect(hourBlockProblems([block(1, 0, 60), block(2, 0, 30)], 90)).toEqual([]);
  });
  it("finds uncovered outcomes", () => {
    const o = (id: string) => ({ id }) as Outcome;
    const plan = { sessions: [{ outcomeIds: ["LO1"] }] } as unknown as LearningPlan;
    expect(uncoveredOutcomes({ outcomes: [o("LO1"), o("LO2")] }, plan)).toEqual(["LO2"]);
  });
  it("enforces video rules by path", () => {
    expect(videoAllowed("elearning", "explainroo")).toBe(false);
    expect(videoAllowed("classroom", "demo")).toBe(true);
    expect(videoAllowed("youtube", "whiteboard")).toBe(true);
  });
});
