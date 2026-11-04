import { describe, expect, it } from "vitest";
import { mkdtemp, mkdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { ExampleStore, loadCourseFiles } from "../src/examples.js";
import { aezc517Course } from "../src/fixtures/aezc517.js";

describe("ExampleStore", () => {
  it("tolerates a missing courses directory and falls back to the inline example", async () => {
    const s = new ExampleStore({ coursesDir: "/definitely/not/here" });
    const courses = await s.courses();
    expect(courses.map((c) => c.id)).toEqual(["aezc517"]);
    const text = await s.forStage("draftOutcomes");
    expect(text).toContain("AEZC517");
    expect(text).toContain("Write verifiable system requirements");
    expect(await s.forStage("draftHourPlan")).toContain("The pack that must never overheat");
  });

  it("never uses the course being generated as its own example", async () => {
    const s = new ExampleStore({ coursesDir: "/definitely/not/here" });
    expect(await s.forStage("draftOutcomes", { exclude: { code: "AEZC517" } })).toBe("");
  });

  it("loads valid course.json files and skips broken ones", async () => {
    const dir = await mkdtemp(join(tmpdir(), "cg-examples-"));
    await mkdir(join(dir, "good"));
    await mkdir(join(dir, "broken"));
    await mkdir(join(dir, "nojson"));
    await writeFile(join(dir, "good", "course.json"), JSON.stringify({ ...aezc517Course(), id: "good" }));
    await writeFile(join(dir, "broken", "course.json"), "{ not json");
    const r = await loadCourseFiles(dir);
    expect(r.courses.map((c) => c.id)).toEqual(["good"]);
    expect(r.skipped).toHaveLength(1);
  });
});
