// Outcome hierarchy helpers: CO -> course LO -> module outcome (MO) -> session outcome (SO) -> blocks.
// Used by MockStages, the fixtures and the eval seeds to build data that passes the core roll-up rules.
import {
  BLOOM_ORDER, BLOOM_VERBS,
  type BloomLevel, type Course, type Module, type ModuleOutcome, type Outcome, type Provenance, type SessionOutcome,
} from "@cg/core";

/**
 * The highest Bloom level a module's hours can support. A 1-hour module can introduce ideas;
 * evaluating or creating needs time for practice and feedback.
 */
export function maxBloomForHours(hours: number): BloomLevel {
  if (hours <= 1) return "understand";
  if (hours <= 2) return "apply";
  if (hours <= 3) return "analyse";
  return "create";
}

export const bloomRank = (b: BloomLevel) => BLOOM_ORDER.indexOf(b);
export const minBloom = (a: BloomLevel, b: BloomLevel): BloomLevel => (bloomRank(a) <= bloomRank(b) ? a : b);

/** Rewrite an outcome so it starts with a verb of `bloom` (used when capping a level). */
export function withBloomVerb(text: string, from: BloomLevel, to: BloomLevel): string {
  if (from === to) return text;
  const words = text.trim().split(/\s+/);
  return `${cap(BLOOM_VERBS[to][0]!)} ${words.slice(1).join(" ")}`;
}

const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);

export const moduleOutcomeId = (moduleId: string, n: number) => `${moduleId}.MO${n}`;
export const sessionOutcomeId = (sessionIndex: number, n: number) => `S${sessionIndex}.SO${n}`;

/** One MO per LO that names the module, capped at the Bloom level the module's hours support. */
export function deriveModuleOutcomes(modules: Module[], outcomes: Outcome[], prov: Provenance): Module[] {
  return modules.map((m) => {
    if (m.outcomes.length) return m;
    const los = outcomes.filter((o) => o.moduleIds.includes(m.id));
    const mos: ModuleOutcome[] = los.map((lo, i) => {
      const bloom = minBloom(lo.bloom, maxBloomForHours(m.hours));
      return { id: moduleOutcomeId(m.id, i + 1), text: withBloomVerb(lo.text, lo.bloom, bloom), bloom, outcomeIds: [lo.id], locked: false, provenance: { ...prov, builtFrom: [lo.id, m.id] } };
    });
    return { ...m, outcomes: mos };
  });
}

interface SessionLike {
  index: number;
  title: string;
  outcomeIds: string[];
}

/**
 * SOs for a list of sessions so every MO is served at its Bloom level: each MO goes to the
 * least-loaded session that teaches one of its LOs. A session left without an SO gets one
 * from its first LO.
 */
export function deriveSessionOutcomes(course: Pick<Course, "modules" | "outcomes">, sessions: SessionLike[], prov: Provenance): SessionOutcome[][] {
  const out: SessionOutcome[][] = sessions.map(() => []);
  const mos = course.modules.flatMap((m) => m.outcomes);
  for (const mo of mos) {
    const candidates = sessions.map((s, i) => ({ s, i })).filter(({ s }) => s.outcomeIds.some((lo) => mo.outcomeIds.includes(lo)));
    if (!candidates.length) continue;
    const { s, i } = candidates.reduce((a, b) => (out[b.i]!.length < out[a.i]!.length ? b : a));
    out[i]!.push({ id: sessionOutcomeId(s.index, out[i]!.length + 1), text: mo.text, bloom: mo.bloom, moduleOutcomeIds: [mo.id], locked: false, provenance: { ...prov, builtFrom: [mo.id] } });
  }
  sessions.forEach((s, i) => {
    if (out[i]!.length) return;
    const lo = course.outcomes.find((o) => s.outcomeIds.includes(o.id));
    const parent = mos.find((mo) => lo && mo.outcomeIds.includes(lo.id));
    // Revisit the LO below its full level (spaced practice); the MO is met by its main session.
    const bloom: BloomLevel = lo && bloomRank(lo.bloom) > bloomRank("understand") ? "understand" : lo?.bloom ?? "understand";
    const text = lo ? withBloomVerb(lo.text, lo.bloom, bloom) : `Explain the key ideas of ${s.title}.`;
    out[i]!.push({ id: sessionOutcomeId(s.index, 1), text, bloom, moduleOutcomeIds: parent ? [parent.id] : [], locked: false, provenance: { ...prov, builtFrom: lo ? [lo.id] : [] } });
  });
  return out;
}
