import { eq } from "drizzle-orm";
import { getServerSession } from "next-auth";
import { redirect } from "next/navigation";
import { adminEmails, authOptions } from "./auth";
import { db, schema } from "./db";
import { HttpError } from "./errors";

export interface CurrentUser {
  id: string;
  email: string;
  name: string | null;
  isAdmin: boolean;
  profile: typeof schema.profiles.$inferSelect | null;
}

export async function currentUser(): Promise<CurrentUser | null> {
  const s = await getServerSession(authOptions());
  const id = s?.user?.id;
  if (!id) return null;
  const u = await db().query.users.findFirst({ where: eq(schema.users.id, id) });
  if (!u) return null;
  const profile = (await db().query.profiles.findFirst({ where: eq(schema.profiles.userId, id) })) ?? null;
  return { id: u.id, email: u.email, name: u.name, isAdmin: u.role === "admin" || adminEmails().has(u.email), profile };
}

/** Pages: signed in with a completed profile (the free tier unlocks after the profile). */
export async function requireTeacherPage(): Promise<CurrentUser & { profile: NonNullable<CurrentUser["profile"]> }> {
  const u = await currentUser();
  if (!u) redirect("/signin");
  if (!u.profile) redirect("/onboarding");
  return u as CurrentUser & { profile: NonNullable<CurrentUser["profile"]> };
}

/** API routes: same rule, as HTTP errors. */
export async function requireTeacherApi(): Promise<CurrentUser> {
  const u = await currentUser();
  if (!u) throw new HttpError(401, "Sign in first");
  if (!u.profile) throw new HttpError(403, "Complete your teacher profile first", { needsProfile: true });
  return u;
}
