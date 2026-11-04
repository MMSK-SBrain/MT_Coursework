// Changes ripple down: editing outcomes (which are frozen before any plan exists) or the confirmed course structure
// marks every dependent session out of date (Session.stale).
import type { Course, Module, ModuleOutcome, Outcome } from "@cg/core";

const outcomeKey = (o: Outcome) => JSON.stringify([o.text, o.bloom, [...o.moduleIds].sort()]);
const moduleKey = (m: Module) => JSON.stringify([m.title, m.hours, m.topics]);
const moKey = (o: ModuleOutcome) => JSON.stringify([o.text, o.bloom, [...o.outcomeIds].sort()]);

/** Module outcome (MO) ids whose text, Bloom level or parent LOs changed, or that were removed. */
export function changedModuleOutcomeIds(prev: Pick<Course, "modules">, next: Pick<Course, "modules">): Set<string> {
  const after = new Map(next.modules.flatMap((m) => m.outcomes.map((o) => [o.id, moKey(o)] as const)));
  const changed = new Set<string>();
  for (const o of prev.modules.flatMap((m) => m.outcomes)) if (after.get(o.id) !== moKey(o)) changed.add(o.id);
  return changed;
}

/** Outcome ids whose text, Bloom level or modules changed, or that were removed. */
export function changedOutcomeIds(prev: Pick<Course, "outcomes">, next: Pick<Course, "outcomes">): Set<string> {
  const after = new Map(next.outcomes.map((o) => [o.id, outcomeKey(o)]));
  const changed = new Set<string>();
  for (const o of prev.outcomes) if (after.get(o.id) !== outcomeKey(o)) changed.add(o.id);
  return changed;
}

/** Module ids that were added, removed or changed. Only counts once a structure has been confirmed. */
export function changedModuleIds(prev: Course, next: Course): Set<string> {
  const changed = new Set<string>();
  if (!prev.structureConfirmedAt && !next.structureConfirmedAt) return changed;
  const before = new Map(prev.modules.map((m) => [m.id, moduleKey(m)]));
  const after = new Map(next.modules.map((m) => [m.id, moduleKey(m)]));
  for (const [id, k] of before) if (after.get(id) !== k) changed.add(id);
  for (const id of after.keys()) if (!before.has(id)) changed.add(id);
  return changed;
}

/**
 * Returns `next` with dependent sessions marked stale. A session depends on its outcomes and, through them,
 * on their modules. A newer structure version also outdates sessions built from an older one that touch a changed module.
 */
export function markStale(prev: Course, next: Course): Course {
  const outs = changedOutcomeIds(prev, next);
  const mods = changedModuleIds(prev, next);
  const mos = changedModuleOutcomeIds(prev, next);
  if (outs.size === 0 && mods.size === 0 && mos.size === 0) return next;
  const modulesOf = new Map<string, string[]>();
  for (const o of [...prev.outcomes, ...next.outcomes]) modulesOf.set(o.id, [...(modulesOf.get(o.id) ?? []), ...o.moduleIds]);
  const depends = (s: Course["plans"][number]["sessions"][number]) =>
    s.outcomeIds.some((id) => outs.has(id) || (modulesOf.get(id) ?? []).some((m) => mods.has(m))) ||
    s.sessionOutcomes.some((so) => so.moduleOutcomeIds.some((id) => mos.has(id)));
  return {
    ...next,
    plans: next.plans.map((p) => ({
      ...p,
      sessions: p.sessions.map((s) => (s.stale || !depends(s) ? s : { ...s, stale: true })),
    })),
  };
}

export function staleSessionCount(course: Pick<Course, "plans">): number {
  return course.plans.reduce((n, p) => n + p.sessions.filter((s) => s.stale).length, 0);
}
