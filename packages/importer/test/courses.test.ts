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
    const loIds = new Set(c.outcomes.map((o) => o.id));
    expect(loIds.size).toBe(c.outcomes.length);
    // hierarchy links resolve: MO -> LO, SO -> MO
    const moIds = new Set(c.modules.flatMap((m) => m.outcomes.map((o) => o.id)));
    expect(c.modules.every((m) => m.outcomes.every((o) => o.outcomeIds.every((id) => loIds.has(id))))).toBe(true);
    const sessions = c.plans[0]!.sessions;
    expect(sessions.every((s) => s.sessionOutcomes.every((so) => so.moduleOutcomeIds.every((id) => moIds.has(id))))).toBe(true);
    expect(sessions.every((s) => s.sessionOutcomes.length > 0)).toBe(true);
    const soIds = sessions.flatMap((s) => s.sessionOutcomes.map((o) => o.id));
    expect(new Set(soIds).size).toBe(soIds.length);
    expect(soIds.every((id) => /^S\d+\.SO\d+$/.test(id))).toBe(true);
    expect(c.modules.flatMap((m) => m.outcomes).every((o) => /^M\d+\.MO\d+$/.test(o.id))).toBe(true);
    // blocks only name SOs of their own session
    expect(sessions.every((s) => s.blocks.every((b) => b.sessionOutcomeIds.every((id) => s.sessionOutcomes.some((so) => so.id === id))))).toBe(true);
  });

  it("re-imports to the same content as the committed file", async () => {
    const committed = Course.parse(JSON.parse(readFileSync(file, "utf8")));
    const fresh = (await importCourseDir(join(root, slug), committed.createdAt)).course;
    expect(fresh).toEqual(committed);
  });
});

describe("known counts and mapping", () => {
  const load = (slug: string) => Course.parse(JSON.parse(readFileSync(join(root, slug, "course.json"), "utf8")));
  it("AEZC517: LOs from the handout, session outcomes from the frameworks, no MOs", () => {
    const c = load("aezc517-systems-engineering");
    expect(c.objectives.map((o) => o.id)).toEqual(["CO1", "CO2", "CO3"]);
    expect(c.outcomes.map((o) => o.id)).toEqual(["LO1", "LO2", "LO3", "LO4", "LO5"]);
    expect(c.modules.every((m) => m.outcomes.length === 0)).toBe(true);
    const s = c.plans[0]!.sessions;
    expect(s).toHaveLength(16);
    expect(s[3]!.sessionOutcomes[0]!.text).toMatch(/^Distinguish between stakeholder needs/);
    expect(s[3]!.outcomeIds).toEqual(["LO2", "LO4"]);
    expect(c.brief.contactHours).toBe(32);
  });
  it("AELZC441: yaml SOs are session outcomes under the module's MO; COs are the only LOs", () => {
    const c = load("aelzc441-automotive-vehicles");
    const s = c.plans[0]!.sessions;
    expect(s).toHaveLength(20);
    expect(s.reduce((a, x) => a + x.sessionOutcomes.length, 0)).toBe(120);
    expect(c.modules.map((m) => m.outcomes.length)).toEqual([1, 1, 1, 1, 1, 1]);
    expect(c.outcomes.map((o) => o.id)).toEqual(["LO1", "LO2", "LO3", "LO4"]);
    expect(s[0]!.sessionOutcomes[0]!.moduleOutcomeIds).toEqual(["M1.MO1"]);
    expect(c.modules[0]!.outcomes[0]!.outcomeIds).toEqual(["LO3"]);
    expect(s[0]!.sessionOutcomes[0]!.id).toBe("S1.SO1");
  });
  it("AEZC516: sheet SOs on sessions, sheet MOs on modules, handout LOs unmapped", () => {
    const c = load("aezc516-ice");
    expect(c.outcomes.map((o) => o.id)).toEqual(["LO1", "LO2", "LO3", "LO4", "LO5"]);
    expect(c.outcomes.every((o) => o.moduleIds.length === 0)).toBe(true);
    const s = c.plans[0]!.sessions;
    expect(s).toHaveLength(15);
    expect(s.reduce((a, x) => a + x.sessionOutcomes.length, 0)).toBe(63);
    expect(c.modules).toHaveLength(6);
    expect(c.modules[2]!.outcomes.map((o) => o.id)).toEqual(["M3.MO1", "M3.MO2", "M3.MO3"]);
    expect(s[4]!.sessionOutcomes[0]!.moduleOutcomeIds).toEqual(["M3.MO1"]);
  });
  it("TUV: DAY objectives are session outcomes; no MOs or LOs are invented", () => {
    const c = load("tuv-sud-automotive-technician");
    const s = c.plans[0]!.sessions;
    expect(s).toHaveLength(55);
    expect(s[0]!.sessionOutcomes[0]!.text).toMatch(/^Name and locate/);
    expect(c.modules).toHaveLength(11);
    expect(c.modules.every((m) => m.outcomes.length === 0)).toBe(true);
    expect(c.outcomes).toEqual([]);
    expect(c.objectives).toEqual([]);
  });
  it("no block is linked to a session outcome without a source saying so", () => {
    for (const slug of SLUGS) expect(load(slug).plans[0]!.sessions.every((s) => s.blocks.every((b) => b.sessionOutcomeIds.length === 0))).toBe(true);
  });
});
