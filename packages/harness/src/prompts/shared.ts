// Guidance shared by all stage prompts. Folded in from .claude/skills/course-design-skill/SKILL.md.
import { BLOOM_ORDER, BLOOM_VERBS, VAGUE_VERBS } from "@cg/core";

export const JSON_RULES = [
  "Return ONLY one JSON object that matches the shape given. No markdown fences, no comments, no text before or after.",
  "Use double quotes. Do not add keys that are not in the shape.",
].join("\n");

export const FACTS_RULES = [
  "Facts are supplied, never recalled. Use only the facts inside <context>: job postings, handout text, search results, standards list.",
  "Do not invent companies, posting counts, statistics, URLs, standard clause numbers or quotes. If a fact you need is not in the context, write around it in general terms.",
].join("\n");

export const BLOOM_GUIDE =
  "Bloom levels and the measurable verbs allowed for each (an outcome must START with one of these verbs):\n" +
  BLOOM_ORDER.map((b) => `- ${b}: ${BLOOM_VERBS[b].join(", ")}`).join("\n") +
  `\nNever start an outcome with a vague verb: ${VAGUE_VERBS.join(", ")}.`;

export const DESIGN_PRINCIPLES = [
  "Instructional design principles:",
  "- Backward design: decide what learners will DO, how we will KNOW they can, then what experiences get them there.",
  "- Outcomes describe observable performance with an object and, where useful, a condition (\"given a ...\") or standard.",
  "- For vocational and professional audiences, target Apply level or higher; keep Remember/Understand for genuine foundations.",
  "- Match Bloom level to activity: knowledge -> remember/understand; skills -> apply and above.",
  "- Cognitive load: 3-5 new concepts per session; one concept at a time; worked examples before independent practice.",
  "- Session flow follows Gagne's events: hook, state objectives, recall prior knowledge, present, guide with examples, practise, feedback, check, summary/transfer.",
  "- Spaced and retrieval practice: revisit key ideas across sessions, include quick checks.",
  "- Automotive, mechanical and manufacturing: safety comes first; tools before systems; troubleshooting method matters; ~70/30 practice to theory is common for technicians.",
  "- IT and tools: hands-on lab time is essential; teach principles as well as tool steps.",
].join("\n");

/** Wrap supplied facts so the model can tell them apart from instructions. */
export function context(label: string, body: string): string {
  return `<context name="${label}">\n${body.trim()}\n</context>`;
}

export function examplesBlock(examples: string): string {
  return examples.trim() ? `Worked examples from real courses (follow their quality and level of detail, not their content):\n${examples.trim()}\n` : "";
}

export function json(v: unknown): string {
  return JSON.stringify(v);
}

/** Keep long source text within a budget so narrow calls stay narrow. */
export function clip(s: string, max: number): string {
  return s.length <= max ? s : s.slice(0, max) + `\n[... ${s.length - max} more characters omitted]`;
}
