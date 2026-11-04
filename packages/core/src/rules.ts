// Business rules shared by the harness (to validate model output) and the app (to warn and gate).
import type { BloomLevel, Course, HourBlock, LearningPath, LearningPlan, Outcome, TeachingStyle, VideoKind } from "./model.js";

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
  apply: ["apply", "use", "calculate", "demonstrate", "solve", "write", "model", "perform", "implement", "operate", "measure"],
  analyse: ["analyse", "analyze", "differentiate", "examine", "diagnose", "plan", "break down", "investigate", "trace"],
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

export function videoAllowed(path: LearningPath, kind: VideoKind): boolean {
  return VIDEO_BY_PATH[path].includes(kind);
}

/** Free-tier limits. Kept here so the app and the billing code agree. */
export const FREE_TIER = {
  coursesPerMonth: 1,
  videoSecondsPerMonth: 300,
  paidFeatures: ["caseStudy", "slides", "instructorGuideDocx", "extraVideo", "extraCourse"] as const,
};
