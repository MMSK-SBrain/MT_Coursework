// Business rules shared by the harness (to validate model output) and the app (to warn and gate).
import type { BloomLevel, Course, HourBlock, LearningPath, LearningPlan, Outcome, Session, TeachingStyle, VideoKind } from "./model.js";

export const PATH_FAMILY: Record<LearningPath, "live" | "blended" | "selfPaced" | "content"> = {
  classroom: "live", lab: "live", bootcamp: "live",
  flipped: "blended", blended: "blended", cohort: "blended",
  elearning: "selfPaced", micro: "selfPaced",
  youtube: "content", shorts: "content",
};

/** Which video kinds each learning path allows. The first entry is the default. */
export const VIDEO_BY_PATH: Record<LearningPath, VideoKind[]> = {
  classroom: ["none", "demo"],
  lab: ["none", "demo"],
  bootcamp: ["none", "demo"],
  flipped: ["explainroo", "whiteboard", "slides"],
  blended: ["none", "demo", "explainroo", "whiteboard"],
  cohort: ["none", "explainroo", "slides"],
  elearning: ["none"],
  micro: ["whiteboard", "explainroo", "slides"],
  youtube: ["whiteboard", "explainroo", "screen", "slides"],
  shorts: ["explainroo", "whiteboard"],
};

export const STYLE_FAMILY: Record<TeachingStyle, "explain" | "engage" | "apply" | "investigate"> = {
  teaching: "explain", worked: "explain", story: "explain", analogy: "explain",
  discussion: "engage", debate: "engage", dyk: "engage", challenge: "engage",
  case: "apply", pbl: "apply", project: "apply", lab: "apply", roleplay: "apply",
  teardown: "investigate", failure: "investigate", expert: "investigate", retrieval: "investigate",
};

/** "Auto" style: pick a style from the outcome's Bloom level. */
export const AUTO_STYLE: Record<BloomLevel, TeachingStyle> = {
  remember: "retrieval", understand: "teaching", apply: "worked",
  analyse: "case", evaluate: "failure", create: "project",
};

export const BLOOM_ORDER: BloomLevel[] = ["remember", "understand", "apply", "analyse", "evaluate", "create"];

/** Measurable verbs per Bloom level. An outcome must start with one of these (case-insensitive). */
export const BLOOM_VERBS: Record<BloomLevel, string[]> = {
  remember: ["define", "list", "name", "recall", "identify", "state", "label"],
  understand: ["describe", "explain", "summarise", "summarize", "classify", "interpret", "compare", "illustrate", "outline"],
  apply: ["apply", "use", "calculate", "demonstrate", "solve", "write", "model", "perform", "implement", "operate", "measure", "inspect", "execute", "complete", "read", "carry out", "test", "adjust", "replace", "assemble", "install"],
  analyse: ["analyse", "analyze", "differentiate", "distinguish", "examine", "diagnose", "plan", "break down", "investigate", "trace", "determine", "troubleshoot"],
  evaluate: ["evaluate", "assess", "justify", "critique", "select", "defend", "judge", "prioritise", "prioritize", "validate"],
  create: ["design", "create", "develop", "construct", "formulate", "propose", "compose", "build"],
};

/** Verbs that are not measurable and must never start an outcome. */
export const VAGUE_VERBS = ["understand", "know", "learn", "appreciate", "be aware of", "be familiar with", "grasp", "realise", "realize"];

export function outcomeVerbProblem(o: Pick<Outcome, "text" | "bloom">): string | null {
  const t = o.text.trim().toLowerCase();
  const vague = VAGUE_VERBS.find((v) => t.startsWith(v + " "));
  if (vague) return `starts with the unmeasurable verb "${vague}"`;
  const ok = BLOOM_VERBS[o.bloom].some((v) => t.startsWith(v + " "));
  return ok ? null : `does not start with a ${o.bloom}-level verb (${BLOOM_VERBS[o.bloom].slice(0, 4).join(", ")}, ...)`;
}

/** Each hour of a session must be fully planned: blocks in hour h add up to exactly 60 minutes, without gaps or overlaps. */
export function hourBlockProblems(blocks: HourBlock[], sessionMinutes: number): string[] {
  const problems: string[] = [];
  const hours = Math.ceil(sessionMinutes / 60);
  for (let h = 1; h <= hours; h++) {
    const expected = h < hours ? 60 : sessionMinutes - 60 * (hours - 1);
    const inHour = blocks.filter((b) => b.hour === h).sort((a, b) => a.startMin - b.startMin);
    let cursor = 0;
    for (const b of inHour) {
      if (b.startMin !== cursor) problems.push(`hour ${h}: block "${b.title}" starts at ${b.startMin} min, expected ${cursor}`);
      cursor = b.startMin + b.minutes;
    }
    if (cursor !== expected) problems.push(`hour ${h}: blocks add up to ${cursor} min, expected ${expected}`);
  }
  const stray = blocks.filter((b) => b.hour > hours);
  if (stray.length) problems.push(`${stray.length} block(s) fall after the end of the session`);
  return problems;
}

/** Outcome ids that no session of the plan teaches. */
export function uncoveredOutcomes(course: Pick<Course, "outcomes">, plan: LearningPlan): string[] {
  const taught = new Set(plan.sessions.flatMap((s) => s.outcomeIds));
  return course.outcomes.map((o) => o.id).filter((id) => !taught.has(id));
}

/** Outcome ids not mapped to any module. */
export function unmappedOutcomes(course: Pick<Course, "outcomes">): string[] {
  return course.outcomes.filter((o) => o.moduleIds.length === 0).map((o) => o.id);
}

// ---- Outcome hierarchy: LO <- MO <- SO <- hour blocks ----------------------------

const bloomRank = (b: BloomLevel) => BLOOM_ORDER.indexOf(b);

/** Block kinds that don't have to serve a session outcome. */
const FREE_BLOCKS = new Set<HourBlock["kind"]>(["break", "wrap"]);

/**
 * Lesson-level check: the content of a session must serve its session outcomes.
 * Each SO needs a measurable verb and at least one block serving it; each teaching block must name a known SO.
 */
export function sessionOutcomeProblems(session: Pick<Session, "title" | "sessionOutcomes" | "blocks">): string[] {
  const problems: string[] = [];
  const ids = new Set(session.sessionOutcomes.map((so) => so.id));
  if (session.sessionOutcomes.length === 0) problems.push(`session "${session.title}" has no session outcomes`);
  for (const so of session.sessionOutcomes) {
    const verb = outcomeVerbProblem(so);
    if (verb) problems.push(`${so.id} ${verb}`);
    if (!session.blocks.some((b) => b.sessionOutcomeIds.includes(so.id))) problems.push(`${so.id} is not served by any block`);
  }
  for (const b of session.blocks) {
    const unknown = b.sessionOutcomeIds.filter((id) => !ids.has(id));
    if (unknown.length) problems.push(`block "${b.title}" names unknown session outcome(s) ${unknown.join(", ")}`);
    if (b.sessionOutcomeIds.length === 0 && !FREE_BLOCKS.has(b.kind)) problems.push(`block "${b.title}" serves no session outcome`);
  }
  return problems;
}

export interface ModuleOutcomeStatus {
  moduleId: string;
  moduleOutcomeId: string;
  sessionOutcomeIds: string[]; // SOs in the plan that serve this MO
  met: boolean;
  problem?: string;
}

/**
 * Module roll-up: an MO is met when at least one SO in the plan serves it at the MO's Bloom level or higher.
 * Sessions must reach the depth the module promises, not just mention its topic.
 */
export function moduleOutcomeCoverage(course: Pick<Course, "modules">, plan: LearningPlan): ModuleOutcomeStatus[] {
  const sos = plan.sessions.flatMap((s) => s.sessionOutcomes);
  return course.modules.flatMap((m) =>
    m.outcomes.map((mo) => {
      const serving = sos.filter((so) => so.moduleOutcomeIds.includes(mo.id));
      const top = serving.reduce((r, so) => Math.max(r, bloomRank(so.bloom)), -1);
      const status: ModuleOutcomeStatus = { moduleId: m.id, moduleOutcomeId: mo.id, sessionOutcomeIds: serving.map((so) => so.id), met: false };
      if (!serving.length) status.problem = "no session outcome serves it";
      else if (top < bloomRank(mo.bloom)) status.problem = `session outcomes reach ${BLOOM_ORDER[top]}, the module outcome needs ${mo.bloom}`;
      else status.met = true;
      return status;
    }),
  );
}

/** Course roll-up: an LO is met when it has module outcomes and all of them are met. */
export function learningOutcomeCoverage(course: Pick<Course, "modules" | "outcomes">, plan: LearningPlan): { outcomeId: string; met: boolean; moduleOutcomeIds: string[] }[] {
  const mo = moduleOutcomeCoverage(course, plan);
  const parents = new Map(course.modules.flatMap((m) => m.outcomes.map((o) => [o.id, o.outcomeIds] as const)));
  return course.outcomes.map((lo) => {
    const mine = mo.filter((s) => parents.get(s.moduleOutcomeId)?.includes(lo.id));
    return { outcomeId: lo.id, moduleOutcomeIds: mine.map((s) => s.moduleOutcomeId), met: mine.length > 0 && mine.every((s) => s.met) };
  });
}

export function videoAllowed(path: LearningPath, kind: VideoKind): boolean {
  return VIDEO_BY_PATH[path].includes(kind);
}

/** Free-tier limits. Kept here so the app and the billing code agree. */
export const FREE_TIER = {
  coursesPerMonth: 1,
  videoSecondsPerMonth: 300,
  paidFeatures: ["caseStudy", "slides", "instructorGuideDocx", "extraVideo", "extraCourse"] as const,
};
