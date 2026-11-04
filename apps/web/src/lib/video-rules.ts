// Video rules by learning path (VIDEO_BY_PATH in core), enforced on every course write.
import { VIDEO_BY_PATH, videoAllowed, type Course, type LearningPlan } from "@cg/core";

/** Human-readable problems for sessions whose video kind is not allowed by their plan's path. */
export function videoProblems(course: Pick<Course, "plans">): string[] {
  return course.plans.flatMap((p) =>
    p.sessions
      .filter((s) => !videoAllowed(p.path, s.video))
      .map((s) => `Plan "${p.name}" (${p.path}), session ${s.index}: video "${s.video}" is not allowed; allowed: ${VIDEO_BY_PATH[p.path].join(", ")}`),
  );
}

/** Replace disallowed video kinds with the path default (first entry). Used on generated plans. */
export function coerceVideo(plan: LearningPlan): LearningPlan {
  const allowed = VIDEO_BY_PATH[plan.path];
  return {
    ...plan,
    sessions: plan.sessions.map((s) => (allowed.includes(s.video) ? s : { ...s, video: allowed[0]! })),
  };
}
