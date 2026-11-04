// Code-checked rules per stage, built on the shared rules in @cg/core.
// Each returns human-readable problems; the runner feeds them back to the model for one repair.
import {
  BLOOM_ORDER, hourBlockProblems, outcomeVerbProblem, uncoveredOutcomes, videoAllowed,
  type BloomLevel, type EditInstruction, type HourBlock, type LearningPath, type LearningPlan, type Module, type Outcome,
} from "@cg/core";

const dupes = (ids: string[]) => [...new Set(ids.filter((id, i) => ids.indexOf(id) !== i))];

export function outcomeSetProblems(
  d: { objectives: { id: string }[]; outcomes: { id: string; text: string; bloom: BloomLevel; moduleIds: string[]; objectiveIds: string[] }[] },
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
  if (uncovered.length) p.push(`module(s) ${uncovered.join(", ")} are not covered by any outcome`);
  for (const id of dupes(d.outcomes.map((o) => o.id))) p.push(`duplicate outcome id ${id}`);
  for (const id of dupes(d.objectives.map((o) => o.id))) p.push(`duplicate objective id ${id}`);
  return p;
}

export function fitProblems(
  changes: { kind: "add" | "strengthen" | "trim"; targetModuleId: string; hoursDelta: number; roleIds: string[] }[],
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

export function hourPlanProblems(blocks: Pick<HourBlock, "hour" | "startMin" | "minutes" | "title" | "outcomeIds">[], sessionMinutes: number, sessionOutcomeIds: string[]): string[] {
  const p = hourBlockProblems(blocks as HourBlock[], sessionMinutes);
  const allowed = new Set(sessionOutcomeIds);
  blocks.forEach((b) => {
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
