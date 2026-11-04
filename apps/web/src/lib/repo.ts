// Database access for courses, usage, credits and the generation log.
import { Course, FREE_TIER, type Generated, type SourceFile } from "@cg/core";
import { and, eq, inArray, sql } from "drizzle-orm";
import { CourseMeta } from "./course-meta";
import { db, schema, type Db } from "./db";
import { HttpError } from "./errors";
import { monthKey, type Credits, type MonthUsage, type PaidFeature } from "./quota";
import { markStale } from "./stale";
import { videoProblems } from "./video-rules";

const { courses, usage, purchases, generationLog, uploads } = schema;

/** The database or an open transaction. */
export type Exec = Db | Parameters<Parameters<Db["transaction"]>[0]>[0];

/** Every course read is scoped to its owner: another teacher's course is a 404. */
export async function loadCourse(userId: string, id: string): Promise<{ course: Course; meta: CourseMeta }> {
  const row = await db().query.courses.findFirst({ where: and(eq(courses.id, id), eq(courses.ownerId, userId)) });
  if (!row) throw new HttpError(404, "Course not found");
  return { course: Course.parse(row.data), meta: CourseMeta.parse(row.meta ?? {}) };
}

export interface WriteOptions {
  /**
   * Sources are server-managed: only the upload route sets them (via this option). Any `sources` in a client- or
   * job-supplied course are ignored and the stored list is kept, so a source can never point at a file the
   * uploads table did not record for this owner and course.
   */
  sources?: SourceFile[];
}

/**
 * The single write path for a course: validates with the core schema, keeps sources server-managed, enforces video
 * rules by path and marks dependent sessions stale when frozen outcomes or the confirmed structure changed.
 */
export function prepareCourseWrite(prev: Course | null, nextRaw: unknown, ownerId: string, opts: WriteOptions = {}): Course {
  const parsed = Course.parse(nextRaw);
  if (prev && parsed.id !== prev.id) throw new HttpError(400, "Course id cannot change");
  const sources = opts.sources ?? prev?.sources ?? [];
  const problems = videoProblems(parsed);
  if (problems.length) throw new HttpError(400, problems[0]!, { problems });
  const next = prev ? markStale(prev, { ...parsed, sources }) : { ...parsed, sources };
  return { ...next, ownerId, slug: prev?.slug ?? next.slug, createdAt: prev?.createdAt ?? next.createdAt, updatedAt: new Date().toISOString() };
}

export async function insertCourse(ownerId: string, course: Course, x: Exec = db()): Promise<Course> {
  const c = prepareCourseWrite(null, { ...course, sources: [] }, ownerId);
  await x.insert(courses).values({ id: c.id, ownerId, title: c.brief.title, data: c, meta: {} });
  return c;
}

export async function saveCourse(ownerId: string, prev: Course, nextRaw: unknown, meta: CourseMeta, opts: WriteOptions = {}): Promise<Course> {
  const c = prepareCourseWrite(prev, nextRaw, ownerId, opts);
  const m = CourseMeta.parse(meta);
  const res = await db()
    .update(courses)
    .set({ data: c, meta: m, title: c.brief.title, updatedAt: new Date() })
    .where(and(eq(courses.id, c.id), eq(courses.ownerId, ownerId)))
    .returning({ id: courses.id });
  if (!res.length) throw new HttpError(404, "Course not found");
  return c;
}

/** Throws unless every source of the course is an upload recorded for this owner and this course. */
export async function assertOwnedSources(ownerId: string, course: Course): Promise<void> {
  if (!course.sources.length) return;
  const keys = course.sources.map((s) => s.storageKey);
  const rows = await db()
    .select({ key: uploads.storageKey })
    .from(uploads)
    .where(and(inArray(uploads.storageKey, keys), eq(uploads.ownerId, ownerId), eq(uploads.courseId, course.id)));
  const ok = new Set(rows.map((r) => r.key));
  if (keys.some((k) => !ok.has(k))) throw new HttpError(403, "A source file does not belong to this course");
}

// ---- Usage ----------------------------------------------------------------------

export async function monthUsage(userId: string, month = monthKey()): Promise<MonthUsage> {
  const row = await db().query.usage.findFirst({ where: and(eq(usage.userId, userId), eq(usage.month, month)) });
  return { coursesStarted: row?.coursesStarted ?? 0, videoSeconds: row?.videoSeconds ?? 0 };
}

const ensureUsageRow = (x: Exec, userId: string, month: string) =>
  x.insert(usage).values({ userId, month }).onConflictDoNothing({ target: [usage.userId, usage.month] });

/** Atomically take one free course slot for the month. False when the free courses are used up. */
export async function reserveFreeCourse(x: Exec, userId: string, month = monthKey()): Promise<boolean> {
  await ensureUsageRow(x, userId, month);
  const rows = await x.execute(sql`
    update usage set courses_started = courses_started + 1
    where user_id = ${userId} and month = ${month} and courses_started < ${FREE_TIER.coursesPerMonth}
    returning user_id`);
  return rows.length > 0;
}

/** Count a course paid with a credit (keeps the monthly counter honest without using a free slot). */
export async function countPaidCourse(x: Exec, userId: string, month = monthKey()): Promise<void> {
  await ensureUsageRow(x, userId, month);
  await x.execute(sql`update usage set courses_started = courses_started + 1 where user_id = ${userId} and month = ${month}`);
}

/** Atomically take `seconds` of the free monthly video allowance. False when they do not fit. */
export async function reserveFreeVideo(x: Exec, userId: string, seconds: number, month = monthKey()): Promise<boolean> {
  await ensureUsageRow(x, userId, month);
  const rows = await x.execute(sql`
    update usage set video_seconds = video_seconds + ${seconds}
    where user_id = ${userId} and month = ${month} and video_seconds + ${seconds} <= ${FREE_TIER.videoSecondsPerMonth}
    returning user_id`);
  return rows.length > 0;
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

/** Atomically use one unit of a paid feature. Returns the purchase id it came from, or null when none is left. */
export async function consumeCredit(userId: string, feature: PaidFeature, x: Exec = db()): Promise<string | null> {
  const rows = await x.execute<{ id: string }>(sql`
    update purchases set consumed = consumed + 1
    where id = (select id from purchases
                where user_id = ${userId} and feature = ${feature} and status = 'paid' and consumed < quantity
                order by created_at limit 1 for update skip locked)
    returning id`);
  return rows[0]?.id ?? null;
}

/** Give back a unit taken by consumeCredit (the paid work failed). */
export async function refundCredit(purchaseId: string, x: Exec = db()): Promise<void> {
  await x.execute(sql`update purchases set consumed = consumed - 1 where id = ${purchaseId} and consumed > 0`);
}

/** Run paid work with a credit reserved up front; the credit is refunded if the work throws. */
export async function withCredit<T>(userId: string, feature: PaidFeature, work: () => Promise<T>): Promise<T> {
  const purchaseId = await consumeCredit(userId, feature);
  if (!purchaseId) throw new HttpError(402, "No credit left for this feature", { paywall: { feature, reason: "No credit left" } });
  try {
    return await work();
  } catch (e) {
    await refundCredit(purchaseId);
    throw e;
  }
}

// ---- Generation log (append-only) -----------------------------------------------------

export async function logGeneration(e: { jobId?: string; userId?: string; courseId?: string; jobType: string; g: Pick<Generated<unknown>, "provenance" | "warnings"> }) {
  const p = e.g.provenance;
  await db().insert(generationLog).values({
    jobId: e.jobId, userId: e.userId, courseId: e.courseId, jobType: e.jobType, model: p.model, promptId: p.promptId,
    promptVersion: p.promptVersion, costUsd: String(p.costUsd ?? 0), builtFrom: p.builtFrom ?? [], warnings: e.g.warnings,
  });
}
