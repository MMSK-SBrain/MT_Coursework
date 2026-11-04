import { and, eq } from "drizzle-orm";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import { requireTeacherApi } from "@/lib/session";
import { getFile } from "@/lib/storage";

export const dynamic = "force-dynamic";

/** Download an uploaded or generated file the teacher owns. */
export const GET = route(async (_req: Request, { params }: { params: Promise<{ key: string[] }> }) => {
  const u = await requireTeacherApi();
  const key = (await params).key.map(decodeURIComponent).join("/");
  const row = await db().query.uploads.findFirst({ where: and(eq(schema.uploads.storageKey, key), eq(schema.uploads.ownerId, u.id)) });
  if (!row) throw new HttpError(404, "File not found");
  const bytes = await getFile(key);
  return new Response(new Blob([bytes as BlobPart]), {
    headers: { "content-type": row.mime, "content-disposition": `attachment; filename="${row.filename.replace(/"/g, "")}"` },
  });
});
