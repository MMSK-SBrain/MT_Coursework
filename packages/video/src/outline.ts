// The seam between "what the video says" and "how explainroo draws it".
// templateOutline() fills a ScriptOutline from session content with plain templates.
// The AI harness can later write a ScriptOutline itself (an LLM script) and hand it to buildProject().
import type { Course, HourBlock, LearningPlan, Session, VideoKind } from "@cg/core";
import { STYLE_FAMILY } from "@cg/core";

export type Visual =
  | { type: "hook"; text: string } // markers: q
  | { type: "objectives"; title: string; items: string[] } // markers: i1..iN
  | { type: "flow"; title: string; steps: string[] } // markers: s1..sN
  | { type: "point"; title: string; caption: string } // markers: t, c
  | { type: "example"; label: string; text: string } // markers: e
  | { type: "question"; text: string } // markers: q
  | { type: "recap"; title: string; items: string[] } // markers: i1..iN
  | { type: "media"; title: string; caption: string; asset?: string }; // markers: m, c

export interface OutlineScene {
  /** explainroo scene id: lowercase letters, digits and dashes. */
  id: string;
  chapter?: string;
  /** Spoken text. Must contain the [#marker]s its visual uses (see Visual). {shown|spoken} is allowed. */
  narration: string;
  visual: Visual;
  /** Lower number = more essential. Scenes with the highest numbers are dropped first to fit a time limit. */
  priority: number;
}

export interface ScriptOutline {
  title: string;
  /** Small label on slides, e.g. "AEZC517 Systems Engineering". */
  courseLabel: string;
  scenes: OutlineScene[];
}

export const MARKERS: Record<Visual["type"], (v: Visual) => string[]> = {
  hook: () => ["q"],
  question: () => ["q"],
  example: () => ["e"],
  point: () => ["t", "c"],
  media: () => ["m", "c"],
  objectives: (v) => ((v as { items: string[] }).items).map((_, i) => `i${i + 1}`),
  recap: (v) => ((v as { items: string[] }).items).map((_, i) => `i${i + 1}`),
  flow: (v) => ((v as { steps: string[] }).steps).map((_, i) => `s${i + 1}`),
};

export function markersIn(narration: string): string[] {
  return [...narration.matchAll(/\[#([A-Za-z0-9_-]+)\]/g)].map((m) => m[1]!);
}

/** Problems that would make explainroo reject or mis-time the outline. Empty array = fine. */
export function outlineProblems(o: ScriptOutline): string[] {
  const problems: string[] = [];
  const seen = new Set<string>();
  if (!o.scenes.length) problems.push("outline has no scenes");
  for (const sc of o.scenes) {
    if (!/^[a-z][a-z0-9-]*$/.test(sc.id)) problems.push(`scene id "${sc.id}" must be lowercase letters, digits and dashes`);
    if (seen.has(sc.id)) problems.push(`duplicate scene id "${sc.id}"`);
    seen.add(sc.id);
    if (!sc.narration.trim()) problems.push(`scene "${sc.id}" has no narration`);
    const have = new Set(markersIn(sc.narration));
    for (const m of MARKERS[sc.visual.type](sc.visual)) {
      if (!have.has(m)) problems.push(`scene "${sc.id}" (${sc.visual.type}) needs a [#${m}] marker in its narration`);
    }
  }
  return problems;
}

// ---- text helpers -------------------------------------------------------------------------

const PRONOUNCEABLE = new Set(["ASPICE", "INCOSE", "SysML", "MBSE", "HARA", "DOORS", "AUTOSAR", "SOTIF", "TARA", "ASIL", "SIL", "HIL"]);
const SPOKEN_SPECIAL: Record<string, string> = { "V&V": "V and V", "HIL": "H I L", "SIL": "S I L", "BMS": "B M S", "EV": "E V", "OEM": "O E M", "OEMs": "O E Ms" };

/** Make user text safe and readable for the narration: strip script syntax, add {shown|spoken} for acronyms. */
export function speakable(text: string): string {
  const clean = text
    .replace(/[\[\]{}|]/g, " ")
    .replace(/^[>#\s]+/, "")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/[—–]/g, ",");
  return clean.replace(/\b[A-Za-z]*[A-Z][A-Za-z&]*\b/g, (w) => {
    if (SPOKEN_SPECIAL[w]) return `{${w}|${SPOKEN_SPECIAL[w]}}`;
    if (/^[A-Z]{2,6}$/.test(w) && !PRONOUNCEABLE.has(w)) return `{${w}|${w.split("").join(" ")}}`;
    return w;
  }).replace(/\bV&V\b/g, "{V&V|V and V}");
}

const stripEnd = (s: string) => s.trim().replace(/[.!?:;]+$/, "");
const lowerFirst = (s: string) => (/^[A-Z][a-z]/.test(s) ? s[0]!.toLowerCase() + s.slice(1) : s);
const slug = (s: string, fallback: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40).replace(/-+$/, "") || fallback;

/** Shorten a label for a diagram box, at a word boundary. */
export function shortLabel(s: string, max = 30): string {
  const t = stripEnd(s);
  if (t.length <= max) return t;
  const cut = t.slice(0, max);
  const words = cut.slice(0, Math.max(cut.lastIndexOf(" "), 12)).trim().split(" ");
  while (words.length > 1 && /^(and|what|the|a|an|of|to|for|with|or|in|on|that)$/i.test(words[words.length - 1]!)) words.pop();
  return words.join(" ").replace(/[,;:]$/, "");
}

/** Rough speaking time in seconds (explainroo Kokoro ~150 wpm plus lead and hold per scene). */
export function estimateSec(narrations: string[]): number {
  let total = 1.4; // end padding
  for (const n of narrations) {
    const spoken = n.replace(/\[#[^\]]*\]/g, " ").replace(/\{[^|}]*\|([^}]*)\}/g, "$1");
    const words = spoken.split(/\s+/).filter(Boolean).length;
    const pauses = (spoken.match(/[.!?]/g)?.length ?? 0) * 0.3;
    total += words / 2.3 + pauses + 0.35 + 0.7;
  }
  return Math.round(total * 10) / 10;
}

// ---- templates ----------------------------------------------------------------------------

export class VideoPlanError extends Error {}

export function findSession(course: Course, planId: string, sessionId: string): { plan: LearningPlan; session: Session } {
  const plan = course.plans.find((p) => p.id === planId);
  if (!plan) throw new VideoPlanError(`plan "${planId}" not found`);
  const session = plan.sessions.find((s) => s.id === sessionId);
  if (!session) throw new VideoPlanError(`session "${sessionId}" not found in plan "${planId}"`);
  return { plan, session };
}

function hookNarration(style: keyof typeof STYLE_FAMILY, title: string, example?: string): string {
  const topic = lowerFirst(stripEnd(title));
  const ex = example ? ` ${speakable(stripEnd(example))}.` : "";
  switch (STYLE_FAMILY[style]) {
    case "engage": return `[#q] Let us start with a question. ${speakable(stripEnd(title))}? Think about it for a moment.${ex}`;
    case "apply": return `[#q] Imagine you have to sort this out on a real project. ${speakable(stripEnd(title))}.${ex}`;
    case "investigate": return `[#q] Let us take a close look at ${speakable(topic)}, and see what the details tell us.${ex}`;
    default: return `[#q] ${speakable(stripEnd(title))}.${ex || " It sounds simple. It is easy to get wrong."}`;
  }
}

export interface TemplateOptions {
  kind: VideoKind;
  /** Rough target length. Lowest-priority scenes are dropped until the estimate fits. */
  targetSec: number;
  /** Asset paths (inside the explainroo project, e.g. "assets/bench.mp4") for demo and screen videos, in scene order. */
  mediaAssets?: string[];
}

/** Turn a session (outcomes, hour blocks, industry examples, style) into a ScriptOutline with plain templates. */
export function templateOutline(course: Course, planId: string, sessionId: string, opt: TemplateOptions): ScriptOutline {
  const { session } = findSession(course, planId, sessionId);
  const outcomes = session.outcomeIds.map((id) => course.outcomes.find((o) => o.id === id)).filter((o): o is NonNullable<typeof o> => !!o);
  const blocks: HourBlock[] = [...session.blocks].sort((a, b) => a.hour - b.hour || a.startMin - b.startMin);
  const teach = blocks.filter((b) => ["teach", "activity", "case"].includes(b.kind));
  const examples = [...new Map(blocks.filter((b) => b.industryExample).map((b) => [b.industryExample!.text, b.industryExample!])).values()];
  const questions = blocks.flatMap((b) => b.check);
  const buildScenes = (compact: boolean): OutlineScene[] => {
  // compact: only the first clause of the first outcome, no example in the hook (for very short targets)
  const full = outcomes.map((o) => stripEnd(o.text));
  const outcomeText = compact ? full.slice(0, 1).map((t) => t.split(/,| with /)[0]!) : full;
  const scenes: OutlineScene[] = [];
  const add = (s: OutlineScene) => scenes.push(s);

  add({ id: "hook", chapter: session.title.slice(0, 60), priority: 0, visual: { type: "hook", text: stripEnd(session.title) },
    narration: hookNarration(session.style, session.title, compact ? undefined : examples[0]?.text) });

  if (outcomeText.length) {
    const lines = outcomeText.map((t, i) => `[#i${i + 1}] ${speakable(lowerFirst(t))}.`);
    add({ id: "outcomes", priority: 1, visual: { type: "objectives", title: "By the end you can", items: outcomeText },
      narration: `By the end of this video, you will be able to:\n${lines.join("\n")}` });
  }

  if (opt.kind === "demo" || opt.kind === "screen") {
    const items = teach.length ? teach : [];
    const n = Math.max(items.length, 1);
    for (let i = 0; i < Math.min(n, 4); i++) {
      const b = items[i];
      const title = b ? stripEnd(b.title) : stripEnd(session.title);
      const verb = opt.kind === "demo" ? "Watch how" : "Now follow along on screen:";
      add({ id: `${opt.kind}-${i + 1}-${slug(shortLabel(title), "part")}`, priority: 2 + i, visual: { type: "media", title, caption: title, asset: opt.mediaAssets?.[i] },
        narration: `[#m] ${verb} ${speakable(lowerFirst(title))}. [#c] Pay attention to the order of the steps and to what each one produces.` });
    }
  } else {
    if (teach.length >= 3) {
      const steps = teach.slice(0, 5).map((b) => shortLabel(b.title));
      const said = steps.map((t, i) => `[#s${i + 1}] ${i === 0 ? "First" : i === steps.length - 1 ? "Finally" : "Then"}, ${speakable(lowerFirst(t))}.`);
      add({ id: "flow", priority: 2, visual: { type: "flow", title: "The path", steps }, narration: `The session follows ${steps.length} steps.\n${said.join("\n")}` });
    }
    teach.slice(0, 3).forEach((b, i) => {
      const title = stripEnd(b.title);
      add({ id: `point-${i + 1}-${slug(shortLabel(title), "part")}`, priority: 3 + i, visual: { type: "point", title, caption: shortLabel(b.activity, 90) },
        narration: `[#t] ${speakable(title)}. [#c] ${speakable(stripEnd(b.activity.split(/(?<=[.!?])\s/)[0] ?? b.activity))}.` });
    });
  }

  examples.slice(0, 2).forEach((ex, i) => {
    add({ id: `example-${i + 1}`, priority: i === 0 ? 4 : 7, visual: { type: "example", label: `In ${ex.sector}`, text: stripEnd(ex.text) },
      narration: `[#e] In ${speakable(ex.sector)}, this shows up like this. ${speakable(stripEnd(ex.text))}.` });
  });

  if (questions[0]) {
    add({ id: "check", priority: 6, visual: { type: "question", text: stripEnd(questions[0]) },
      narration: `[#q] Pause and think. ${speakable(stripEnd(questions[0]))}?` });
  }

  if (outcomeText.length) {
    const lines = outcomeText.map((t, i) => `[#i${i + 1}] ${speakable(lowerFirst(t))}.`);
    add({ id: "recap", priority: 5, visual: { type: "recap", title: "Recap", items: outcomeText },
      narration: `To recap, you can now:\n${lines.join("\n")}` });
  }

  return scenes;
  };

  // Fit the target: drop the least essential scenes first (keeping order); if two scenes are still too long, go compact.
  const fit = (scenes: OutlineScene[]) => {
    let kept = scenes;
    while (kept.length > 2 && estimateSec(kept.map((s) => s.narration)) > opt.targetSec) {
      const worst = Math.max(...kept.map((s) => s.priority));
      const idx = kept.map((s) => s.priority).lastIndexOf(worst);
      kept = kept.filter((_, i) => i !== idx);
    }
    return kept;
  };
  let kept = fit(buildScenes(false));
  if (estimateSec(kept.map((s) => s.narration)) > opt.targetSec) kept = fit(buildScenes(true));
  return { title: session.title, courseLabel: [course.brief.code, course.brief.title].filter(Boolean).join(" "), scenes: kept };
}
