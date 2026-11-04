import { desc, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { randomUUID } from "node:crypto";
import { newCourse } from "@/lib/course-logic";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import { checkCourseStart } from "@/lib/quota";
import { addUsage, consumeCredit, credits, insertCourse, monthUsage } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";

export const GET = route(async () => {
  const u = await requireTeacherApi();
  const rows = await db()
    .select({ id: schema.courses.id, title: schema.courses.title, updatedAt: schema.courses.updatedAt })
    .from(schema.courses)
    .where(eq(schema.courses.ownerId, u.id))
    .orderBy(desc(schema.courses.updatedAt));
  return NextResponse.json({ courses: rows });
});

/** Start a course. Free tier: FREE_TIER.coursesPerMonth; beyond that one extraCourse credit each. */
export const POST = route(async (req: Request) => {
  const u = await requireTeacherApi();
  const body = (await req.json().catch(() => ({}))) as { title?: string };
  const gate = checkCourseStart(await monthUsage(u.id), await credits(u.id));
  if (!gate.allowed) throw new HttpError(402, gate.reason, { paywall: { feature: gate.feature, reason: gate.reason } });
  if (gate.consume && !(await consumeCredit(u.id, gate.consume))) throw new HttpError(402, "No credit left", { paywall: { feature: gate.consume, reason: "No credit left" } });
  const id = `c-${randomUUID().slice(0, 8)}`;
  const course = await insertCourse(u.id, newCourse(id, u.id, body.title?.trim() || "Untitled course"));
  await addUsage(u.id, { coursesStarted: 1 });
  return NextResponse.json({ id: course.id }, { status: 201 });
});
