import { NextResponse } from "next/server";
import { z } from "zod";
import { CourseMeta } from "@/lib/course-meta";
import { route } from "@/lib/http";
import { loadCourse, saveCourse } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";
type Ctx = { params: Promise<{ id: string }> };

export const GET = route(async (_req: Request, { params }: Ctx) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  return NextResponse.json(await loadCourse(u.id, id));
});

/** Teacher decisions: the client sends the whole course; the server validates it, enforces video rules and marks stale sessions. */
export const PUT = route(async (req: Request, { params }: Ctx) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  const body = z.object({ course: z.unknown(), meta: CourseMeta.optional() }).parse(await req.json());
  const prev = await loadCourse(u.id, id);
  const meta = body.meta ?? prev.meta;
  const course = await saveCourse(u.id, prev.course, body.course, meta);
  return NextResponse.json({ course, meta });
});
