// Teacher sign-in: Google or email magic link (NextAuth v4), plus a dev-only sign-in when NODE_ENV=development.
import { and, eq } from "drizzle-orm";
import type { NextAuthOptions } from "next-auth";
import type { Adapter, AdapterAccount, AdapterUser } from "next-auth/adapters";
import CredentialsProvider from "next-auth/providers/credentials";
import EmailProvider from "next-auth/providers/email";
import GoogleProvider from "next-auth/providers/google";
import { createTransport } from "nodemailer";
import { db, schema } from "./db";

const { users, accounts, verificationTokens } = schema;

type UserRow = typeof users.$inferSelect;
const toAdapterUser = (u: UserRow): AdapterUser => ({ id: u.id, email: u.email, emailVerified: u.emailVerified, name: u.name, image: u.image });

export const isDevSignInEnabled = () => process.env.NODE_ENV === "development";

export function adminEmails(): Set<string> {
  return new Set((process.env.ADMIN_EMAILS ?? "").split(",").map((s) => s.trim().toLowerCase()).filter(Boolean));
}

/** Minimal Drizzle adapter for the teacher_* tables (JWT sessions, so no session table). */
export function teacherAdapter(): Adapter {
  return {
    async createUser(u: Omit<AdapterUser, "id">) {
      const email = u.email.toLowerCase();
      const [row] = await db()
        .insert(users)
        .values({ email, name: u.name, image: u.image, emailVerified: u.emailVerified, role: adminEmails().has(email) ? "admin" : "teacher" })
        .returning();
      return toAdapterUser(row!);
    },
    async getUser(id) {
      const row = await db().query.users.findFirst({ where: eq(users.id, id) });
      return row ? toAdapterUser(row) : null;
    },
    async getUserByEmail(email) {
      const row = await db().query.users.findFirst({ where: eq(users.email, email.toLowerCase()) });
      return row ? toAdapterUser(row) : null;
    },
    async getUserByAccount({ provider, providerAccountId }) {
      const [row] = await db()
        .select({ u: users })
        .from(accounts)
        .innerJoin(users, eq(users.id, accounts.userId))
        .where(and(eq(accounts.provider, provider), eq(accounts.providerAccountId, providerAccountId)));
      return row ? toAdapterUser(row.u) : null;
    },
    async updateUser(u) {
      const [row] = await db()
        .update(users)
        .set({ name: u.name, image: u.image, emailVerified: u.emailVerified, ...(u.email ? { email: u.email.toLowerCase() } : {}) })
        .where(eq(users.id, u.id))
        .returning();
      return toAdapterUser(row!);
    },
    async linkAccount(a: AdapterAccount) {
      await db().insert(accounts).values({
        userId: a.userId, type: a.type, provider: a.provider, providerAccountId: a.providerAccountId,
        refresh_token: a.refresh_token, access_token: a.access_token, expires_at: a.expires_at, token_type: a.token_type,
        scope: a.scope, id_token: a.id_token, session_state: a.session_state as string | undefined,
      });
    },
    async createVerificationToken(t) {
      await db().insert(verificationTokens).values(t);
      return t;
    },
    async useVerificationToken({ identifier, token }) {
      const [row] = await db()
        .delete(verificationTokens)
        .where(and(eq(verificationTokens.identifier, identifier), eq(verificationTokens.token, token)))
        .returning();
      return row ?? null;
    },
  };
}

async function upsertDevUser(email: string) {
  const adapter = teacherAdapter();
  const existing = await adapter.getUserByEmail!(email);
  return existing ?? adapter.createUser!({ id: "", email, emailVerified: new Date(), name: email.split("@")[0] ?? email } as AdapterUser);
}

export function authOptions(): NextAuthOptions {
  const providers: NextAuthOptions["providers"] = [];
  if (process.env.GOOGLE_CLIENT_ID && process.env.GOOGLE_CLIENT_SECRET) {
    providers.push(GoogleProvider({ clientId: process.env.GOOGLE_CLIENT_ID, clientSecret: process.env.GOOGLE_CLIENT_SECRET }));
  }
  providers.push(
    EmailProvider({
      server: process.env.EMAIL_SERVER ?? "",
      from: process.env.EMAIL_FROM ?? "Course Generator <no-reply@reynlab.com>",
      async sendVerificationRequest({ identifier, url, provider }) {
        if (!process.env.EMAIL_SERVER) {
          // Never log sign-in links outside development: they are bearer credentials.
          if (!isDevSignInEnabled()) throw new Error("EMAIL_SERVER is not configured");
          // Development without SMTP: print the magic link.
          console.log(`\n[auth] Magic sign-in link for ${identifier}:\n${url}\n`);
          return;
        }
        await createTransport(provider.server).sendMail({
          to: identifier, from: provider.from, subject: "Sign in to Course Generator",
          text: `Sign in to Course Generator:\n${url}\n\nIf you did not ask for this, ignore this email.`,
        });
      },
    }),
  );
  if (isDevSignInEnabled()) {
    providers.push(
      CredentialsProvider({
        id: "dev", name: "Dev sign-in", credentials: { email: { label: "Email", type: "email" } },
        async authorize(c) {
          const email = String(c?.email ?? "").trim().toLowerCase();
          if (!/^\S+@\S+$/.test(email)) return null;
          const u = await upsertDevUser(email);
          return { id: u.id, email: u.email, name: u.name };
        },
      }),
    );
  }
  return {
    adapter: teacherAdapter(),
    session: { strategy: "jwt" },
    secret: process.env.NEXTAUTH_SECRET ?? (process.env.NODE_ENV !== "production" ? "dev-only-secret-change-me" : undefined),
    providers,
    pages: { signIn: "/signin", verifyRequest: "/signin?sent=1" },
    callbacks: {
      async session({ session, token }) {
        if (session.user && token.sub) session.user.id = token.sub;
        return session;
      },
    },
  };
}
