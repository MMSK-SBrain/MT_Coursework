import type { SourceFile } from "@cg/core";
import { NextResponse } from "next/server";
import { randomUUID } from "node:crypto";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import { loadCourse, saveCourse } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";
import { putFile } from "@/lib/storage";

export const dynamic = "force-dynamic";
type Ctx = { params: Promise<{ id: string }> };

const ALLOWED: Record<"handout" | "moduleSheet", string[]> = { handout: [".docx", ".pdf", ".txt"], moduleSheet: [".xlsx"] };
const MAX_BYTES = 15 * 1024 * 1024;

/** Upload a handout (.docx/.pdf/.txt) or a module sheet (.xlsx). Replaces an earlier file of the same kind. */
export const POST = route(async (req: Request, { params }: Ctx) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  const form = await req.formData();
  const kind = form.get("kind");
  const file = form.get("file");
  if (kind !== "handout" && kind !== "moduleSheet") throw new HttpError(400, "kind must be handout or moduleSheet");
  if (!(file instanceof File)) throw new HttpError(400, "file is required");
  const ext = file.name.slice(file.name.lastIndexOf(".")).toLowerCase();
  if (!ALLOWED[kind].includes(ext)) throw new HttpError(400, `A ${kind === "handout" ? "handout" : "module sheet"} must be ${ALLOWED[kind].join(", ")}`);
  if (file.size > MAX_BYTES) throw new HttpError(400, "Files are limited to 15 MB");

  const { course, meta } = await loadCourse(u.id, id);
  const fileId = randomUUID();
  const storageKey = `uploads/${course.id}/${fileId}${ext}`;
  await putFile(storageKey, new Uint8Array(await file.arrayBuffer()));
  await db().insert(schema.uploads).values({ storageKey, ownerId: u.id, courseId: course.id, filename: file.name, mime: file.type || "application/octet-stream", bytes: file.size });
  const src: SourceFile = { id: fileId, kind, filename: file.name, mime: file.type || "application/octet-stream", storageKey };
  const next = await saveCourse(u.id, course, { ...course, sources: [...course.sources.filter((s) => s.kind !== kind), src] }, meta);
  return NextResponse.json({ course: next, meta, size: file.size });
});
