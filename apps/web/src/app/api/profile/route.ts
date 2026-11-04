import { NextResponse } from "next/server";
import { z } from "zod";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import { currentUser } from "@/lib/session";

export const dynamic = "force-dynamic";

const Profile = z.object({
  institution: z.string().trim().min(2).max(200),
  subject: z.string().trim().min(2).max(200),
  role: z.string().trim().min(2).max(100),
});

export const POST = route(async (req: Request) => {
  const u = await currentUser();
  if (!u) throw new HttpError(401, "Sign in first");
  const p = Profile.parse(await req.json());
  await db()
    .insert(schema.profiles)
    .values({ userId: u.id, ...p })
    .onConflictDoUpdate({ target: schema.profiles.userId, set: p });
  return NextResponse.json({ ok: true });
});
