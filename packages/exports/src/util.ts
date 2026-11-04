import type { Course, HourBlock, LearningPlan, Session } from "@cg/core";

export function findSession(course: Course, planId: string, sessionId: string): { plan: LearningPlan; session: Session } {
  const plan = course.plans.find((p) => p.id === planId);
  if (!plan) throw new Error(`Plan not found: ${planId}`);
  const session = plan.sessions.find((s) => s.id === sessionId);
  if (!session) throw new Error(`Session not found: ${sessionId} in plan ${planId}`);
  return { plan, session };
}

export const pad2 = (n: number) => String(n).padStart(2, "0");

/** "1:05" style clock from minutes since the start of the session. */
export const clock = (min: number) => `${Math.floor(min / 60)}:${pad2(min % 60)}`;

export function blockRange(b: HourBlock): string {
  const start = (b.hour - 1) * 60 + b.startMin;
  return `${clock(start)}-${clock(start + b.minutes)}`;
}

export const sortedBlocks = (blocks: HourBlock[]) =>
  [...blocks].sort((a, b) => a.hour - b.hour || a.startMin - b.startMin);

export const approvedLinks = (s: Session) => s.links.filter((l) => l.approved);

export function outcomeText(course: Course, id: string): string {
  const o = course.outcomes.find((x) => x.id === id);
  return o ? o.text : id;
}

/** Split prose into sentences (good enough for activity text). */
export function sentences(text: string): string[] {
  return text.split(/(?<=[.!?])\s+/).map((s) => s.trim()).filter(Boolean);
}

export function shorten(text: string, max: number): string {
  const t = text.replace(/\.$/, "");
  return t.length <= max ? t : t.slice(0, max - 1).replace(/\s+\S*$/, "") + "…";
}
