import { existsSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { Course } from "@cg/core";
import { describe, expect, it } from "vitest";
import { importCourseDir } from "../src/index.js";

const root = join(dirname(fileURLToPath(import.meta.url)), "../../../courses");
const SLUGS = ["aezc517-systems-engineering", "aelzc441-automotive-vehicles", "aezc516-ice", "tuv-sud-automotive-technician"];

describe.each(SLUGS)("%s", (slug) => {
  const file = join(root, slug, "course.json");

  it("has a course.json that parses with the core Course schema", () => {
    expect(existsSync(file)).toBe(true);
    const c = Course.parse(JSON.parse(readFileSync(file, "utf8")));
    expect(c.slug).toBe(slug);
    expect(c.outcomesFrozenAt).toBeUndefined();
    expect(c.roles).toEqual([]);
    expect(c.fit).toEqual([]);
    expect(c.plans).toHaveLength(1);
    expect(c.plans[0]!.path).toBe("classroom");
    expect(c.outcomes.every((o) => o.origin === "handout" && o.provenance.model === "import")).toBe(true);
    const moduleIds = new Set(c.modules.map((m) => m.id));
    expect(c.outcomes.every((o) => o.moduleIds.every((m) => moduleIds.has(m)))).toBe(true);
    const outcomeIds = new Set(c.outcomes.map((o) => o.id));
    expect(outcomeIds.size).toBe(c.outcomes.length);
    expect(c.plans[0]!.sessions.every((s) => s.outcomeIds.every((id) => outcomeIds.has(id)))).toBe(true);
  });

  it("re-imports to the same content as the committed file", async () => {
    const committed = Course.parse(JSON.parse(readFileSync(file, "utf8")));
    const fresh = (await importCourseDir(join(root, slug), committed.createdAt)).course;
    expect(fresh).toEqual(committed);
  });
});

describe("known counts", () => {
  const load = (slug: string) => Course.parse(JSON.parse(readFileSync(join(root, slug, "course.json"), "utf8")));
  it("AEZC517 keeps the empty CO4/CO5 out", () => {
    const c = load("aezc517-systems-engineering");
    expect(c.objectives.map((o) => o.id)).toEqual(["CO1", "CO2", "CO3"]);
    expect(c.outcomes).toHaveLength(5);
    expect(c.plans[0]!.sessions).toHaveLength(16);
    expect(c.brief.contactHours).toBe(32);
  });
  it("AELZC441 has 20 sessions and 120 session outcomes", () => {
    const c = load("aelzc441-automotive-vehicles");
    expect(c.plans[0]!.sessions).toHaveLength(20);
    expect(c.outcomes).toHaveLength(120);
    expect(c.objectives).toHaveLength(4);
  });
  it("AEZC516 carries the handout LOs next to the sheet SOs", () => {
    const c = load("aezc516-ice");
    expect(c.outcomes.filter((o) => /^LO\d$/.test(o.id))).toHaveLength(5);
    expect(c.plans[0]!.sessions).toHaveLength(15);
    expect(c.modules).toHaveLength(6);
  });
  it("TUV has 55 sessions in 11 weekly modules and no objectives", () => {
    const c = load("tuv-sud-automotive-technician");
    expect(c.plans[0]!.sessions).toHaveLength(55);
    expect(c.modules).toHaveLength(11);
    expect(c.objectives).toEqual([]);
  });
});
