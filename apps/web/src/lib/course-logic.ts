// Pure course transitions shared by the UI (teacher decisions) and the job handlers (generated content).
// No I/O here, so everything is unit-testable and safe to import in client components.
import type {
  CaseStudy, Course, FitChange, FurtherLink, HourBlock, JobRole, LearningPlan, Module, ModuleOutcome, Objective, Outcome,
  OutcomeSuggestion, Provenance,
} from "@cg/core";
import { BLOOM_ORDER, BLOOM_VERBS, type ParsedInputs } from "@cg/core";
import type { CourseMeta } from "./course-meta";
import { coerceVideo } from "./video-rules";

export const nowIso = () => new Date().toISOString();

export function humanProvenance(promptId: string, builtFrom: string[] = []): Provenance {
  return { model: "human", promptId, promptVersion: "0", costUsd: 0, createdAt: nowIso(), builtFrom };
}

export function newCourse(id: string, ownerId: string, title = "Untitled course"): Course {
  const t = nowIso();
  return {
    id, slug: id, ownerId,
    brief: { title, audience: "", level: "ug", contactHours: 30, industry: "", markets: ["India"], textbooks: [], notes: "" },
    sources: [], modules: [], structureVersion: 1, roles: [], fit: [], objectives: [], outcomes: [], plans: [],
    createdAt: t, updatedAt: t,
  };
}

// ---- Stage 1 ------------------------------------------------------------------

export function applyParsed(course: Course, meta: CourseMeta, p: ParsedInputs, prov: Provenance): [Course, CourseMeta] {
  const brief = { ...course.brief, ...Object.fromEntries(Object.entries(p.brief).filter(([, v]) => v !== undefined)) };
  return [
    { ...course, brief, modules: p.modules, objectives: p.objectives, outcomes: p.outcomes },
    { ...meta, inputGaps: p.gaps, baseModules: undefined, provenance: { ...meta.provenance, inputs: prov } },
  ];
}

// ---- Stage 2 ------------------------------------------------------------------

export function applyRoles(
  course: Course, meta: CourseMeta, r: { keywords: string[]; roles: JobRole[]; occupationsRead: number }, prov: Provenance,
): [Course, CourseMeta] {
  // Keep the teacher's own roles and earlier selections.
  const wasSelected = new Set(course.roles.filter((x) => x.selected).map((x) => x.title.toLowerCase()));
  const own = course.roles.filter((x) => x.addedByUser);
  const found = r.roles.map((x) => (wasSelected.has(x.title.toLowerCase()) ? { ...x, selected: true } : x));
  return [
    { ...course, roles: [...found, ...own] },
    { ...meta, keywords: r.keywords, occupationsRead: r.occupationsRead, provenance: { ...meta.provenance, roles: prov } },
  ];
}

export function addOwnRole(course: Course, title: string): Course {
  const t = title.trim();
  if (!t) return course;
  const id = `u${course.roles.filter((r) => r.addedByUser).length + 1}-${Date.now().toString(36)}`;
  const role: JobRole = { id, title: t, skills: [], matchedSkills: [], moduleMatch: 0, evidence: [], selected: true, addedByUser: true };
  return reopenStructure({ ...course, roles: [...course.roles, role] });
}

export function toggleRole(course: Course, roleId: string, selected: boolean): Course {
  // Changing the roles reopens the structure (the prototype does the same); nothing changes until it is confirmed again.
  return reopenStructure({ ...course, roles: course.roles.map((r) => (r.id === roleId ? { ...r, selected } : r)) });
}

// ---- Stage 3 ------------------------------------------------------------------

export function applyFit(course: Course, changes: FitChange[]): Course {
  return { ...course, fit: changes, structureConfirmedAt: undefined };
}

export function decideFit(course: Course, id: string, decision: FitChange["decision"], edit?: Partial<Pick<FitChange, "text" | "targetModuleId" | "hoursDelta">>): Course {
  return { ...course, fit: course.fit.map((f) => (f.id === id ? { ...f, ...edit, decision } : f)) };
}

export const allFitDecided = (course: Pick<Course, "fit">) => course.fit.every((f) => f.decision !== "pending");

export function addOwnFit(course: Course, text: string): Course {
  const t = text.trim();
  if (!t) return course;
  const m = /\b(M\d+)\b/.exec(t);
  const target = m && course.modules.some((x) => x.id === m[1]) ? m[1]! : "new";
  const change: FitChange = {
    id: `own-${Date.now().toString(36)}`, kind: "add", text: t, reason: "Proposed by you", targetModuleId: target,
    hoursDelta: 1, roleIds: [], decision: "pending", provenance: humanProvenance("fit.own"),
  };
  return { ...course, fit: [...course.fit, change] };
}

/** Apply accepted and changed fit decisions to the base modules. */
export function modulesAfterFit(base: Module[], fit: FitChange[]): Module[] {
  const mods = base.map((m) => ({ ...m, topics: [...m.topics], outcomes: [...m.outcomes] }));
  for (const f of fit) {
    if (f.decision !== "accepted" && f.decision !== "changed") continue;
    if (f.targetModuleId === "new") {
      const n = mods.reduce((a, m) => Math.max(a, Number(m.id.replace(/\D/g, "")) || 0), 0) + 1;
      mods.push({ id: `M${n}`, title: f.text, hours: Math.max(0, f.hoursDelta), topics: [f.text], outcomes: [], foundIn: "fit" });
      continue;
    }
    const m = mods.find((x) => x.id === f.targetModuleId);
    if (!m) continue;
    m.hours = Math.max(0, m.hours + f.hoursDelta);
    if (f.kind !== "trim") m.topics.push(f.text);
    else m.note = [m.note, `Trimmed: ${f.text}`].filter(Boolean).join(" · ");
  }
  return mods;
}

/** Confirm the course structure: decisions applied, version bumped (v1 → v2 on the first confirmation). */
export function confirmStructure(course: Course, meta: CourseMeta): [Course, CourseMeta] {
  if (!allFitDecided(course)) throw new Error("Decide every proposed change first");
  const base = meta.baseModules ?? course.modules;
  // The base snapshot predates the drafted module outcomes: carry the current MOs over so a re-confirmation keeps them.
  const current = new Map(course.modules.map((m) => [m.id, m.outcomes]));
  const withMos = base.map((m) => ({ ...m, outcomes: current.get(m.id) ?? m.outcomes }));
  return [
    { ...course, modules: modulesAfterFit(withMos, course.fit), structureVersion: course.structureVersion + 1, structureConfirmedAt: nowIso() },
    { ...meta, baseModules: base },
  ];
}

export function reopenStructure(course: Course): Course {
  return course.structureConfirmedAt ? { ...course, structureConfirmedAt: undefined } : course;
}

/** Coverage of one role before and after the accepted changes. Heuristic: the core model has no coverage numbers. */
export function roleCoverage(course: Pick<Course, "fit">, role: JobRole): [number, number] {
  const before = Math.round(role.moduleMatch);
  const boosts = course.fit.filter((f) => f.roleIds.includes(role.id) && f.kind !== "trim" && f.decision !== "rejected").length;
  return [before, Math.min(100, before + boosts * 8)];
}

// ---- Stage 4 ------------------------------------------------------------------

export function applyOutcomes(course: Course, meta: CourseMeta, d: { objectives: Objective[]; outcomes: Outcome[]; modules?: Module[] }): [Course, CourseMeta] {
  // Locked items are kept exactly as they are, whatever the draft says.
  const keep = <T extends { id: string; locked: boolean }>(old: T[], drafted: T[]) => {
    const locked = new Map(old.filter((o) => o.locked).map((o) => [o.id, o]));
    const out = drafted.map((o) => locked.get(o.id) ?? o);
    for (const o of locked.values()) if (!out.some((x) => x.id === o.id)) out.push(o);
    return out;
  };
  // Module outcomes (MOs) come back on the drafted modules. Only their MOs are taken: the confirmed structure
  // (titles, hours, topics) stays as the teacher confirmed it.
  const drafted = new Map((d.modules ?? []).map((m) => [m.id, m.outcomes]));
  const modules = course.modules.map((m) => (drafted.has(m.id) ? { ...m, outcomes: keep(m.outcomes, drafted.get(m.id)!) } : m));
  return [
    { ...course, modules, objectives: keep(course.objectives, d.objectives), outcomes: keep(course.outcomes, d.outcomes) },
    { ...meta, outcomesDraftedFor: course.structureVersion },
  ];
}

/** Apply `fn` to the module outcome `id` (MOs live inside their module). */
const mapModuleOutcomes = (course: Course, fn: (mo: ModuleOutcome) => ModuleOutcome[] | ModuleOutcome): Module[] =>
  course.modules.map((m) => ({ ...m, outcomes: m.outcomes.flatMap((mo) => fn(mo)) }));

/** Edit the text of an LO, MO or course objective (locked items are left alone). */
export function editOutcomeText(course: Course, id: string, text: string): Course {
  const t = text.trim();
  if (!t) return course;
  return {
    ...course,
    modules: mapModuleOutcomes(course, (mo) => (mo.id === id && !mo.locked ? { ...mo, text: t } : mo)),
    outcomes: course.outcomes.map((o) => (o.id === id && !o.locked ? { ...o, text: t } : o)),
    objectives: course.objectives.map((o) => (o.id === id && !o.locked ? { ...o, text: t } : o)),
  };
}

export function setLocked(course: Course, id: string, locked: boolean): Course {
  return {
    ...course,
    modules: mapModuleOutcomes(course, (mo) => (mo.id === id ? { ...mo, locked } : mo)),
    outcomes: course.outcomes.map((o) => (o.id === id ? { ...o, locked } : o)),
    objectives: course.objectives.map((o) => (o.id === id ? { ...o, locked } : o)),
  };
}

/** Accept a suggested rewrite. A split replaces the outcome with two (id and id + "b"). */
export function acceptSuggestion(course: Course, s: OutcomeSuggestion, prov: Provenance): Course {
  const target = course.outcomes.find((o) => o.id === s.targetId);
  const mo = course.modules.flatMap((m) => m.outcomes).find((x) => x.id === s.targetId);
  if (!target && mo) {
    const repl: ModuleOutcome[] = s.proposed.map((p, i) => ({
      ...mo, id: i === 0 ? mo.id : `${mo.id}${String.fromCharCode(97 + i)}`, text: p.text, bloom: p.bloom, provenance: prov,
    }));
    return { ...course, modules: mapModuleOutcomes(course, (x) => (x.id === s.targetId ? repl : x)) };
  }
  if (!target) {
    const first = s.proposed[0]!;
    return { ...course, objectives: course.objectives.map((o) => (o.id === s.targetId ? { ...o, text: first.text, provenance: prov } : o)) };
  }
  const repl: Outcome[] = s.proposed.map((p, i) => ({
    ...target, id: i === 0 ? target.id : `${target.id}${String.fromCharCode(97 + i)}`, text: p.text, bloom: p.bloom, provenance: prov,
  }));
  return { ...course, outcomes: course.outcomes.flatMap((o) => (o.id === s.targetId ? repl : [o])) };
}

export const freezeOutcomes = (course: Course): Course => ({ ...course, outcomesFrozenAt: nowIso() });
export const unfreezeOutcomes = (course: Course): Course => ({ ...course, outcomesFrozenAt: undefined });

// ---- Stage 5 ------------------------------------------------------------------

export function addPlan(course: Course, plan: LearningPlan): Course {
  return { ...course, plans: [...course.plans, coerceVideo(plan)] };
}

export function updateSession(course: Course, planId: string, sessionId: string, patch: Partial<LearningPlan["sessions"][number]>): Course {
  return {
    ...course,
    plans: course.plans.map((p) =>
      p.id !== planId ? p : { ...p, sessions: p.sessions.map((s) => (s.id === sessionId ? { ...s, ...patch } : s)) },
    ),
  };
}

export function findSession(course: Course, planId: string, sessionId: string) {
  const plan = course.plans.find((p) => p.id === planId);
  const session = plan?.sessions.find((s) => s.id === sessionId);
  if (!plan || !session) throw new Error(`Session ${planId}/${sessionId} not found`);
  return { plan, session };
}

// ---- Stage 6 ------------------------------------------------------------------

/** A fresh hour-wise plan also clears the stale flag: the session has been rebuilt from current outcomes. */
export const applyHourPlan = (course: Course, planId: string, sessionId: string, blocks: HourBlock[]): Course =>
  updateSession(course, planId, sessionId, { blocks, stale: false });

export function applyLinks(course: Course, planId: string, sessionId: string, links: FurtherLink[]): Course {
  const { session } = findSession(course, planId, sessionId);
  const approved = new Map(session.links.filter((l) => l.approved).map((l) => [l.url, l]));
  const merged = [...approved.values(), ...links.filter((l) => !approved.has(l.url))];
  return updateSession(course, planId, sessionId, { links: merged });
}

export function applyCaseStudy(course: Course, planId: string, sessionId: string, cs: CaseStudy): Course {
  if (cs.label === "real" && cs.sources.length === 0) throw new Error("A real case study needs checkable sources");
  const { session } = findSession(course, planId, sessionId);
  return updateSession(course, planId, sessionId, { caseStudies: [...session.caseStudies, cs] });
}

// ---- Suggested edits for module outcomes and objectives ----------------------------

/**
 * Stages.suggestOutcomeEdit only looks up course LOs. To suggest edits for a module outcome (MO) or a course
 * objective (CO), the item is presented to it as an LO in a view of the course; the suggestion keeps the item's id.
 */
