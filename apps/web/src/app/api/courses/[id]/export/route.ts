import { strToU8, zipSync } from "fflate";
import { route } from "@/lib/http";
import { loadCourse } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";
import { getExporter } from "@/lib/stages";

export const dynamic = "force-dynamic";

/** Free: the whole course design as a zip of .md files. */
export const GET = route(async (_req: Request, { params }: { params: Promise<{ id: string }> }) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  const { course } = await loadCourse(u.id, id);
  const files = getExporter().markdown(course);
  const zip = zipSync(Object.fromEntries(Object.entries(files).map(([p, c]) => [`${course.slug}/${p}`, strToU8(c)])));
  const name = (course.brief.code ?? course.slug).replace(/[^A-Za-z0-9_-]/g, "_");
  return new Response(new Blob([zip as BlobPart]), {
    headers: { "content-type": "application/zip", "content-disposition": `attachment; filename="${name}-course-design.zip"` },
  });
});
