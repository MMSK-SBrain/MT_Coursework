// Code-checked rules per stage, built on the shared rules in @cg/core.
// Each returns human-readable problems; the runner feeds them back to the model for one repair.
import {
  BLOOM_ORDER, hourBlockProblems, learningOutcomeCoverage, moduleOutcomeCoverage, outcomeVerbProblem, sessionOutcomeProblems,
  uncoveredOutcomes, videoAllowed,
  type BloomLevel, type Course, type EditInstruction, type HourBlock, type LearningPath, type LearningPlan, type Module, type Outcome,
} from "@cg/core";
import { bloomRank, maxBloomForHours } from "./hierarchy.js";

const dupes = (ids: string[]) => [...new Set(ids.filter((id, i) => ids.indexOf(id) !== i))];

export function outcomeSetProblems(
  d: {
    objectives: { id: string }[];
    outcomes: { id: string; text: string; bloom: BloomLevel; moduleIds: string[]; objectiveIds: string[] }[];
    moduleOutcomes?: MoDraft[];
  },
  modules: Module[],
): string[] {
  const p: string[] = [];
  const modIds = new Set(modules.map((m) => m.id));
  const objIds = new Set(d.objectives.map((o) => o.id));
  for (const o of d.outcomes) {
    const v = outcomeVerbProblem(o);
    if (v) p.push(`${o.id} ${v}`);
    const badMods = o.moduleIds.filter((m) => !modIds.has(m));
    if (badMods.length) p.push(`${o.id} names unknown module(s) ${badMods.join(", ")}`);
    const badObj = o.objectiveIds.filter((m) => !objIds.has(m));
    if (badObj.length) p.push(`${o.id} names unknown objective(s) ${badObj.join(", ")}`);
    if (!o.objectiveIds.length) p.push(`${o.id} is not linked to any objective`);
  }
  const covered = new Set(d.outcomes.flatMap((o) => o.moduleIds));
  const uncovered = modules.filter((m) => !covered.has(m.id)).map((m) => m.id);
  // With module outcomes, modules are covered through their MOs (checked below), so LOs may leave moduleIds empty.
  if (uncovered.length && !d.moduleOutcomes) p.push(`module(s) ${uncovered.join(", ")} are not covered by any outcome`);
  if (d.moduleOutcomes) p.push(...moduleOutcomeDraftProblems(d.moduleOutcomes, modules, d.outcomes.map((o) => o.id)));
  for (const id of dupes(d.outcomes.map((o) => o.id))) p.push(`duplicate outcome id ${id}`);
  for (const id of dupes(d.objectives.map((o) => o.id))) p.push(`duplicate objective id ${id}`);
  return p;
}

export function fitProblems(
  changes: { kind: "add" | "strengthen" | "trim"; targetModuleId: string; hoursDelta: number; roleIds: string[]; academicConflict?: string }[],
  modules: Module[],
  roleIds: string[],
  contactHours: number,
): string[] {
  const p: string[] = [];
  const mods = new Set(modules.map((m) => m.id));
  const roles = new Set(roleIds);
  changes.forEach((c, i) => {
    const n = `change ${i + 1}`;
    if (c.targetModuleId !== "new" && !mods.has(c.targetModuleId)) p.push(`${n} targets unknown module ${c.targetModuleId}`);
    if (c.kind === "trim" && c.hoursDelta >= 0) p.push(`${n} is a trim but hoursDelta is ${c.hoursDelta} (must be negative)`);
    if (c.kind !== "trim" && c.hoursDelta <= 0) p.push(`${n} is ${c.kind} but hoursDelta is ${c.hoursDelta} (must be positive)`);
    if (c.kind === "trim" && c.targetModuleId === "new") p.push(`${n} trims a "new" module`);
    const bad = c.roleIds.filter((r) => !roles.has(r));
    if (bad.length) p.push(`${n} names unselected or unknown role(s) ${bad.join(", ")}`);
    if (!c.roleIds.length) p.push(`${n} is not linked to any selected role`);
    if (c.academicConflict && /\b(no|not an?|without)\s+(academic\s+)?conflict|does not conflict|doesn't conflict/i.test(c.academicConflict))
      p.push(`${n} writes "${c.academicConflict.slice(0, 60)}" in academicConflict; leave the field out when there is no conflict`);
  });
  const net = changes.reduce((a, c) => a + c.hoursDelta, 0);
  if (Math.abs(net) > 0.1 * contactHours) p.push(`net hours change is ${net} h, more than 10% of the ${contactHours} contact hours`);
  return p;
}

export function planProblems(
  sessions: { outcomeIds: string[]; video: LearningPlan["sessions"][number]["video"]; title: string }[],
  outcomes: Pick<Outcome, "id">[],
  path: LearningPath,
): string[] {
  const p: string[] = [];
  const known = new Set(outcomes.map((o) => o.id));
  const fakePlan = { sessions } as unknown as LearningPlan;
  const unc = uncoveredOutcomes({ outcomes: outcomes as Outcome[] }, fakePlan);
  if (unc.length) p.push(`outcome(s) ${unc.join(", ")} are not taught by any session`);
  sessions.forEach((s, i) => {
    if (!videoAllowed(path, s.video)) p.push(`session ${i + 1} "${s.title}" uses video "${s.video}", not allowed for path ${path}`);
    const bad = s.outcomeIds.filter((o) => !known.has(o));
    if (bad.length) p.push(`session ${i + 1} names unknown outcome(s) ${bad.join(", ")}`);
  });
  return p;
}

export function hourPlanProblems(blocks: Pick<HourBlock, "hour" | "startMin" | "minutes" | "title" | "outcomeIds" | "activity">[], sessionMinutes: number, sessionOutcomeIds: string[]): string[] {
  const p = hourBlockProblems(blocks as HourBlock[], sessionMinutes);
  const allowed = new Set(sessionOutcomeIds);
  blocks.forEach((b) => {
    // A stated duration longer than the block itself ("10-minute break" in a 5-minute block) can't be run as written.
    // ponytail: only catches over-long durations; sums of sub-steps are left to the reviewer.
    for (const m of `${b.title} ${b.activity}`.matchAll(/\b(\d{1,3})\s*(?:-|–)?\s*(?:min|mins|minutes|minute)\b/gi)) {
      const n = Number(m[1]);
      if (n > b.minutes) { p.push(`block "${b.title}" is ${b.minutes} min but its text says ${n} minutes`); break; }
    }
    const bad = b.outcomeIds.filter((o) => !allowed.has(o));
    if (bad.length) p.push(`block "${b.title}" names outcome(s) ${bad.join(", ")} that this session does not teach`);
  });
  if (!blocks.some((b) => b.outcomeIds.length)) p.push("no block is linked to the session's outcomes");
  return p;
}

export function suggestionProblems(proposed: { text: string; bloom: BloomLevel }[], original: Outcome, kind: EditInstruction["kind"]): string[] {
  const p: string[] = [];
  proposed.forEach((o, i) => {
    const v = outcomeVerbProblem(o);
    if (v) p.push(`proposal ${i + 1} ${v}`);
  });
  if (kind === "split" && proposed.length !== 2) p.push(`a split must return exactly 2 outcomes, got ${proposed.length}`);
  if (kind !== "split" && proposed.length !== 1) p.push(`return exactly 1 outcome, got ${proposed.length}`);
  if (kind === "raiseBloom" && proposed[0] && BLOOM_ORDER.indexOf(proposed[0].bloom) <= BLOOM_ORDER.indexOf(original.bloom))
    p.push(`the Bloom level must rise above ${original.bloom}, got ${proposed[0].bloom}`);
  if (kind === "shorten" && proposed[0] && proposed[0].text.length >= original.text.length) p.push("the shortened outcome is not shorter than the original");
  return p;
}

export function indexProblems(label: string, idx: number[], size: number): string[] {
  const bad = idx.filter((i) => i >= size);
  const p = bad.length ? [`${label} index(es) ${bad.join(", ")} do not exist (there are ${size})`] : [];
  for (const d of dupes(idx.map(String))) p.push(`${label} index ${d} is used more than once`);
  return p;
}

// ---- Outcome hierarchy --------------------------------------------------------------------------

export interface MoDraft {
  moduleId: string;
  text: string;
  bloom: BloomLevel;
  outcomeIds: string[];
}

/** Module outcomes: every module has 1-4, each serves known LOs at a level its hours support; every LO is served. */
export function moduleOutcomeDraftProblems(mos: MoDraft[], modules: Module[], loIds: string[]): string[] {
  const p: string[] = [];
  const los = new Set(loIds);
  for (const m of modules) {
    const mine = mos.filter((x) => x.moduleId === m.id);
    if (!mine.length) p.push(`module ${m.id} has no module outcomes`);
    if (mine.length > 4) p.push(`module ${m.id} has ${mine.length} module outcomes; keep it to 1-4`);
    const capB = maxBloomForHours(m.hours);
    mine.forEach((mo, i) => {
      const n = `${m.id} module outcome ${i + 1}`;
      const v = outcomeVerbProblem(mo);
      if (v) p.push(`${n} ${v}`);
      if (bloomRank(mo.bloom) > bloomRank(capB)) p.push(`${n} is at ${mo.bloom}, but ${m.hours} h can support at most ${capB}`);
      if (!mo.outcomeIds.length) p.push(`${n} serves no learning outcome`);
      const bad = mo.outcomeIds.filter((x) => !los.has(x));
      if (bad.length) p.push(`${n} names unknown learning outcome(s) ${bad.join(", ")}`);
    });
  }
  const known = new Set(modules.map((m) => m.id));
  for (const mo of mos) if (!known.has(mo.moduleId)) p.push(`module outcome "${mo.text.slice(0, 40)}" names unknown module ${mo.moduleId}`);
  const served = new Set(mos.flatMap((m) => m.outcomeIds));
  const orphan = loIds.filter((id) => !served.has(id));
  if (orphan.length) p.push(`learning outcome(s) ${orphan.join(", ")} are served by no module outcome`);
  return p;
}

/** Session outcomes in a drafted plan: each session has some, with measurable verbs and known parent MOs. */
export function sessionOutcomeDraftProblems(
  sessions: { title: string; sessionOutcomes: { text: string; bloom: BloomLevel; moduleOutcomeIds: string[] }[] }[],
  moIds: string[],
): string[] {
  const p: string[] = [];
  const known = new Set(moIds);
  sessions.forEach((s, i) => {
    if (!s.sessionOutcomes.length) p.push(`session ${i + 1} "${s.title}" has no session outcomes`);
    s.sessionOutcomes.forEach((so, k) => {
      const n = `session ${i + 1} outcome ${k + 1}`;
      const v = outcomeVerbProblem(so);
      if (v) p.push(`${n} ${v}`);
      const bad = so.moduleOutcomeIds.filter((x) => !known.has(x));
      if (bad.length) p.push(`${n} names unknown module outcome(s) ${bad.join(", ")}`);
      if (known.size && !so.moduleOutcomeIds.length) p.push(`${n} serves no module outcome`);
    });
  });
  return p;
}

/** Roll-up: unmet module outcomes in a plan (repairable) and unmet course LOs (warnings). */
export function rollUp(course: Pick<Course, "modules" | "outcomes">, plan: LearningPlan): { moProblems: string[]; loProblems: string[]; moMet: number; moTotal: number; loMet: number; loTotal: number } {
  const mo = moduleOutcomeCoverage(course, plan);
  const hasMos = mo.length > 0;
  const lo = hasMos ? learningOutcomeCoverage(course, plan) : [];
  return {
    moProblems: mo.filter((s) => !s.met).map((s) => `module outcome ${s.moduleOutcomeId} is not met: ${s.problem}`),
    loProblems: lo.filter((s) => !s.met).map((s) => `learning outcome ${s.outcomeId} is not met by the plan (${s.moduleOutcomeIds.length ? "some of its module outcomes are unmet" : "it has no module outcomes"})`),
    moMet: mo.filter((s) => s.met).length, moTotal: mo.length,
    loMet: lo.filter((s) => s.met).length, loTotal: lo.length,
  };
}

/**
 * Hour-plan check against the session outcomes, split into what the hour-plan call can fix
 * (blocks) and what it cannot (the SOs themselves, which come from the plan).
 */
export function hourPlanSoProblems(
  session: { title: string; sessionOutcomes: { id: string; text: string; bloom: BloomLevel }[] },
  blocks: { title: string; kind: HourBlock["kind"]; sessionOutcomeIds: string[] }[],
): { fixable: string[]; upstream: string[] } {
  if (!session.sessionOutcomes.length) return { fixable: [], upstream: [`session "${session.title}" has no session outcomes; redraft the plan`] };
  const all = sessionOutcomeProblems({ title: session.title, sessionOutcomes: session.sessionOutcomes, blocks } as never);
  const verbProblem = (x: string) => session.sessionOutcomes.some((so) => x.startsWith(`${so.id} `) && !x.endsWith("is not served by any block"));
  return { fixable: all.filter((x) => !verbProblem(x)), upstream: all.filter(verbProblem) };
}
