import { Feedback } from "@cg/core";
import { NextResponse } from "next/server";
import { randomUUID } from "node:crypto";
import { z } from "zod";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import { currentUser } from "@/lib/session";

export const dynamic = "force-dynamic";

const Body = Feedback.omit({ id: true, userId: true, createdAt: true }).extend({ pageUrl: z.string().max(500).optional() });

/** Item feedback (with the item's provenance) and site-wide feedback. Signed-out visitors can leave site feedback. */
export const POST = route(async (req: Request) => {
  const u = await currentUser();
  const b = Body.parse(await req.json());
  if (b.scope === "item" && !u) throw new HttpError(401, "Sign in first");
  if (b.scope === "site" && !b.text.trim()) throw new HttpError(400, "Say what you would like to tell us");
  const fb = Feedback.parse({ ...b, id: randomUUID(), userId: u?.id, createdAt: new Date().toISOString() });
  await db().insert(schema.feedback).values({
    id: fb.id, userId: fb.userId, courseId: fb.courseId, scope: fb.scope, targetPath: fb.targetPath, rating: fb.rating,
    category: fb.category, text: fb.text, model: fb.model, promptId: fb.promptId, promptVersion: fb.promptVersion,
    pageUrl: b.pageUrl, createdAt: new Date(fb.createdAt),
  });
  return NextResponse.json({ id: fb.id }, { status: 201 });
});
