import { BLOOM_VERBS, type BloomLevel, type Provenance } from "@cg/core";

export function provenance(promptId: string, now: string): Provenance {
  return { model: "import", promptId, promptVersion: "1", costUsd: 0, createdAt: now, builtFrom: [] };
}

/** Verbs the source documents use that the core verb table does not list. Used only to pick a Bloom level. */
const EXTRA_VERBS: Record<string, BloomLevel> = {
  recognize: "remember", recognise: "remember", locate: "remember", "name and locate": "remember", memorize: "remember",
  discuss: "understand", introduce: "understand", impart: "understand", help: "understand", recognizing: "understand",
  distinguish: "understand", determine: "apply", convert: "apply", decode: "apply", navigate: "apply", read: "apply",
  develop: "create", integrate: "create", compare: "understand", "differentiate between": "analyse",
  assess: "evaluate", sketch: "apply", draw: "apply", interpret: "understand", conduct: "apply", carry: "apply",
  inspect: "apply", test: "apply", check: "apply", record: "apply", install: "apply", remove: "apply", replace: "apply",
  disassemble: "apply", assemble: "apply", fit: "apply", repair: "apply", adjust: "apply", tighten: "apply", torque: "apply",
  verify: "evaluate", troubleshoot: "analyse", compute: "apply", estimate: "apply", predict: "analyse", relate: "understand",
  prepare: "apply", follow: "apply", wear: "apply", handle: "apply",
  create: "create", show: "understand", reproduce: "remember",
  execute: "apply", complete: "apply", document: "apply", set: "apply", connect: "apply", crimp: "apply", make: "apply", produce: "apply",
  align: "apply", maintain: "apply", route: "apply", reassemble: "apply", reinstall: "apply", cut: "apply", press: "apply", lay: "apply",
  organize: "apply", organise: "apply", listen: "apply", score: "apply", achieve: "apply", reference: "apply", "cross-reference": "apply",
  articulate: "understand", support: "understand", decide: "evaluate", review: "evaluate", research: "analyse", link: "understand",
  understand: "understand", aim: "understand",
};

export interface BloomGuess { bloom: BloomLevel; how: "verb" | "stated" | "default" }

export function normBloom(s: string | undefined): BloomLevel | undefined {
  if (!s) return undefined;
  const t = s.trim().toLowerCase().replace(/^analyze$/, "analyse");
  return (["remember", "understand", "apply", "analyse", "evaluate", "create"] as const).find((b) => b === t);
}

/** Infer a Bloom level from the leading verb. Falls back to the level stated in the source, then to "understand". */
export function inferBloom(text: string, stated?: string): BloomGuess {
  const t = text.trim().toLowerCase().replace(/^[^a-z]+/, "").replace(/^(?!apply\b)[a-z]+ly\s+/, ""); // drop a leading adverb ("Safely isolate ...")
  const entries: [string, BloomLevel][] = [];
  for (const [lvl, verbs] of Object.entries(BLOOM_VERBS) as [BloomLevel, string[]][]) for (const v of verbs) entries.push([v, lvl]);
  for (const [v, lvl] of Object.entries(EXTRA_VERBS)) entries.push([v, lvl]);
  entries.sort((a, b) => b[0].length - a[0].length);
  const hit = entries.find(([v]) => t.startsWith(v + " ") || t === v);
  const s = normBloom(stated);
  if (hit) return { bloom: hit[1], how: "verb" };
  if (s) return { bloom: s, how: "stated" };
  return { bloom: "understand", how: "default" };
}

export function sentenceCase(s: string): string {
  return s.replace(/\s+/g, " ").trim();
}

export function titleCaseIfShouting(s: string): string {
  const t = s.trim();
  if (t !== t.toUpperCase()) return t;
  return t.toLowerCase().replace(/\b[a-z]/g, (c) => c.toUpperCase());
}

export function plain(s: string): string {
  return s.replace(/\*\*/g, "").replace(/`/g, "").replace(/\s+/g, " ").trim();
}

export function round1(n: number): number {
  return Math.round(n * 10) / 10;
}
