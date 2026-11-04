import { desc, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { randomUUID } from "node:crypto";
import { startCourse } from "@/lib/billing";
import { db, schema } from "@/lib/db";
import { route } from "@/lib/http";
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
  const course = await startCourse(u.id, `c-${randomUUID().slice(0, 8)}`, body.title?.trim() || "Untitled course");
  return NextResponse.json({ id: course.id }, { status: 201 });
});
