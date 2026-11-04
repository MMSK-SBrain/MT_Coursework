import { VIDEO_BY_PATH } from "@cg/core";
import { describe, expect, it } from "vitest";
import { addPlan, updateSession } from "./course-logic";
import { mockStages } from "./mock-stages";
import { prepareCourseWrite } from "./repo";
import { sampleCourse } from "./test-fixtures";
import { coerceVideo, videoProblems } from "./video-rules";

describe("video rules by path", () => {
  it("accepts the sample plan and rejects a disallowed kind", async () => {
    const { course } = await sampleCourse();
    expect(videoProblems(course)).toEqual([]);
    const plan = course.plans[0]!;
    const bad = updateSession(course, plan.id, plan.sessions[0]!.id, { video: "explainroo" }); // classroom: none or demo only
    expect(videoProblems(bad)).toHaveLength(1);
    expect(() => prepareCourseWrite(course, bad, "u-test")).toThrow(/not allowed/);
  });

  it("eLearning plans never get video", async () => {
    const { course } = await sampleCourse();
    const g = await mockStages.draftPlan(course, { path: "elearning", style: "auto" });
    const c = addPlan(course, g.value);
    expect(c.plans[1]!.sessions.every((s) => s.video === "none")).toBe(true);
    const forced = updateSession(c, c.plans[1]!.id, c.plans[1]!.sessions[0]!.id, { video: "whiteboard" });
    expect(videoProblems(forced)[0]).toMatch(/elearning/);
  });

  it("coerces generated sessions to the path default", async () => {
    const { course } = await sampleCourse();
    const plan = { ...course.plans[0]!, path: "flipped" as const }; // sessions are none/demo, flipped allows neither
    const fixed = coerceVideo(plan);
    expect(fixed.sessions.every((s) => VIDEO_BY_PATH.flipped.includes(s.video))).toBe(true);
    expect(fixed.sessions[0]!.video).toBe(VIDEO_BY_PATH.flipped[0]);
  });
});
