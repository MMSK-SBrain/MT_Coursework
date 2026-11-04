// Database access for courses, usage, credits and the generation log.
import { Course, type Generated } from "@cg/core";
import { and, eq, gt, sql } from "drizzle-orm";
import { CourseMeta } from "./course-meta";
import { db, schema } from "./db";
import { HttpError } from "./errors";
import { monthKey, type Credits, type MonthUsage, type PaidFeature } from "./quota";
import { markStale } from "./stale";
import { videoProblems } from "./video-rules";

const { courses, usage, purchases, generationLog } = schema;

export async function loadCourse(userId: string, id: string): Promise<{ course: Course; meta: CourseMeta }> {
  const row = await db().query.courses.findFirst({ where: and(eq(courses.id, id), eq(courses.ownerId, userId)) });
  if (!row) throw new HttpError(404, "Course not found");
  return { course: Course.parse(row.data), meta: CourseMeta.parse(row.meta ?? {}) };
}

/**
 * The single write path for a course: validates with the core schema, enforces video rules by path and marks
 * dependent sessions stale when frozen outcomes or the confirmed structure changed.
 */
export function prepareCourseWrite(prev: Course | null, nextRaw: unknown, ownerId: string): Course {
  const parsed = Course.parse(nextRaw);
  if (prev && parsed.id !== prev.id) throw new HttpError(400, "Course id cannot change");
  const problems = videoProblems(parsed);
  if (problems.length) throw new HttpError(400, problems[0]!, { problems });
  const next = prev ? markStale(prev, parsed) : parsed;
  return { ...next, ownerId, updatedAt: new Date().toISOString() };
}

export async function insertCourse(ownerId: string, course: Course): Promise<Course> {
  const c = prepareCourseWrite(null, course, ownerId);
  await db().insert(courses).values({ id: c.id, ownerId, title: c.brief.title, data: c, meta: {} });
  return c;
}

export async function saveCourse(ownerId: string, prev: Course, nextRaw: unknown, meta: CourseMeta): Promise<Course> {
  const c = prepareCourseWrite(prev, nextRaw, ownerId);
  const m = CourseMeta.parse(meta);
  const res = await db()
    .update(courses)
    .set({ data: c, meta: m, title: c.brief.title, updatedAt: new Date() })
    .where(and(eq(courses.id, c.id), eq(courses.ownerId, ownerId)))
    .returning({ id: courses.id });
  if (!res.length) throw new HttpError(404, "Course not found");
  return c;
}

// ---- Usage ----------------------------------------------------------------------

export async function monthUsage(userId: string, month = monthKey()): Promise<MonthUsage> {
  const row = await db().query.usage.findFirst({ where: and(eq(usage.userId, userId), eq(usage.month, month)) });
  return { coursesStarted: row?.coursesStarted ?? 0, videoSeconds: row?.videoSeconds ?? 0 };
}

export async function addUsage(userId: string, d: Partial<MonthUsage>, month = monthKey()): Promise<void> {
  const cs = d.coursesStarted ?? 0, vs = d.videoSeconds ?? 0;
  await db()
    .insert(usage)
    .values({ userId, month, coursesStarted: cs, videoSeconds: vs })
    .onConflictDoUpdate({
      target: [usage.userId, usage.month],
      set: { coursesStarted: sql`${usage.coursesStarted} + ${cs}`, videoSeconds: sql`${usage.videoSeconds} + ${vs}` },
    });
}

// ---- Paid credits ------------------------------------------------------------------

export async function credits(userId: string): Promise<Credits> {
  const rows = await db()
    .select({ feature: purchases.feature, left: sql<number>`sum(${purchases.quantity} - ${purchases.consumed})::int` })
    .from(purchases)
    .where(and(eq(purchases.userId, userId), eq(purchases.status, "paid")))
    .groupBy(purchases.feature);
  return Object.fromEntries(rows.map((r) => [r.feature, Number(r.left)]));
}

/** Use one unit of a paid feature. Returns false when none is left. */
export async function consumeCredit(userId: string, feature: PaidFeature): Promise<boolean> {
  const res = await db().execute(sql`
    update purchases set consumed = consumed + 1
    where id = (select id from purchases
                where user_id = ${userId} and feature = ${feature} and status = 'paid' and consumed < quantity
                order by created_at limit 1 for update skip locked)
    returning id`);
  return res.length > 0;
}

export async function hasCredit(userId: string, feature: PaidFeature): Promise<boolean> {
  const row = await db().query.purchases.findFirst({
    where: and(eq(purchases.userId, userId), eq(purchases.feature, feature), eq(purchases.status, "paid"), gt(sql`${purchases.quantity} - ${purchases.consumed}`, 0)),
  });
  return !!row;
}

// ---- Generation log (append-only) -----------------------------------------------------

export async function logGeneration(e: { jobId?: string; userId?: string; courseId?: string; jobType: string; g: Pick<Generated<unknown>, "provenance" | "warnings"> }) {
  const p = e.g.provenance;
  await db().insert(generationLog).values({
    jobId: e.jobId, userId: e.userId, courseId: e.courseId, jobType: e.jobType, model: p.model, promptId: p.promptId,
    promptVersion: p.promptVersion, costUsd: String(p.costUsd ?? 0), builtFrom: p.builtFrom ?? [], warnings: e.g.warnings,
  });
}
