// Postgres schema (Drizzle). Teacher accounts live in their own tables (teacher_*),
// separate from any Reynlab learner accounts.
import { sql } from "drizzle-orm";
import { bigint, index, integer, jsonb, numeric, pgTable, primaryKey, text, timestamp, uuid } from "drizzle-orm/pg-core";
import type { Course, Feedback } from "@cg/core";
import type { CourseMeta } from "../lib/course-meta";

const id = () => uuid("id").primaryKey().defaultRandom();
const createdAt = () => timestamp("created_at", { withTimezone: true }).notNull().defaultNow();

// ---- Accounts (NextAuth adapter tables + teacher profile) -------------------

export const users = pgTable("teacher_users", {
  id: id(),
  name: text("name"),
  email: text("email").notNull().unique(),
  emailVerified: timestamp("email_verified", { withTimezone: true }),
  image: text("image"),
  /** "teacher" or "admin". Admins see the feedback admin page. */
  role: text("role").notNull().default("teacher"),
  createdAt: createdAt(),
});

export const accounts = pgTable(
  "teacher_accounts",
  {
    userId: uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
    type: text("type").notNull(),
    provider: text("provider").notNull(),
    providerAccountId: text("provider_account_id").notNull(),
    refresh_token: text("refresh_token"),
    access_token: text("access_token"),
    expires_at: integer("expires_at"),
    token_type: text("token_type"),
    scope: text("scope"),
    id_token: text("id_token"),
    session_state: text("session_state"),
  },
  (t) => [primaryKey({ columns: [t.provider, t.providerAccountId] })],
);

export const verificationTokens = pgTable(
  "teacher_verification_tokens",
  {
    identifier: text("identifier").notNull(),
    token: text("token").notNull(),
    expires: timestamp("expires", { withTimezone: true }).notNull(),
  },
  (t) => [primaryKey({ columns: [t.identifier, t.token] })],
);

export const profiles = pgTable("teacher_profiles", {
  userId: uuid("user_id").primaryKey().references(() => users.id, { onDelete: "cascade" }),
  institution: text("institution").notNull(),
  subject: text("subject").notNull(),
  role: text("role").notNull(), // e.g. "Lecturer", "Trainer", "HoD"
  createdAt: createdAt(),
});

// ---- Courses ----------------------------------------------------------------

export const courses = pgTable(
  "courses",
  {
    id: text("id").primaryKey(),
    ownerId: uuid("owner_id").notNull().references(() => users.id, { onDelete: "cascade" }),
    title: text("title").notNull(),
    /** The Course aggregate, validated with the core zod schema on every write. */
    data: jsonb("data").$type<Course>().notNull(),
    /** App-only state the core model has no place for (role search keywords, input gaps, ...). */
    meta: jsonb("meta").$type<CourseMeta>().notNull().default({}),
    createdAt: createdAt(),
    updatedAt: timestamp("updated_at", { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [index("courses_owner_idx").on(t.ownerId)],
);

export const uploads = pgTable("uploads", {
  storageKey: text("storage_key").primaryKey(),
  ownerId: uuid("owner_id").notNull().references(() => users.id, { onDelete: "cascade" }),
  courseId: text("course_id").references(() => courses.id, { onDelete: "cascade" }),
  filename: text("filename").notNull(),
  mime: text("mime").notNull(),
  bytes: integer("bytes").notNull(),
  createdAt: createdAt(),
});

// ---- Usage, payments ---------------------------------------------------------

/** Per user per calendar month (UTC, "YYYY-MM"). */
export const usage = pgTable(
  "usage",
  {
    userId: uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
    month: text("month").notNull(),
    coursesStarted: integer("courses_started").notNull().default(0),
    videoSeconds: integer("video_seconds").notNull().default(0),
  },
  (t) => [primaryKey({ columns: [t.userId, t.month] })],
);

/** One row per paid unit bought (or granted by the dev provider). */
export const purchases = pgTable("purchases", {
  id: id(),
  userId: uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
  feature: text("feature").notNull(), // one of FREE_TIER.paidFeatures
  quantity: integer("quantity").notNull().default(1),
  consumed: integer("consumed").notNull().default(0),
  provider: text("provider").notNull(),
  providerRef: text("provider_ref"),
  status: text("status").notNull().default("pending"), // pending | paid | failed
  createdAt: createdAt(),
});

// ---- Feedback ---------------------------------------------------------------

export const feedback = pgTable(
  "feedback",
  {
    id: text("id").primaryKey(),
    userId: uuid("user_id").references(() => users.id, { onDelete: "set null" }),
    courseId: text("course_id"),
    scope: text("scope").$type<Feedback["scope"]>().notNull(),
    targetPath: text("target_path"),
    rating: text("rating").$type<NonNullable<Feedback["rating"]>>(),
    category: text("category").$type<NonNullable<Feedback["category"]>>(),
    text: text("text").notNull().default(""),
    model: text("model"),
    promptId: text("prompt_id"),
    promptVersion: text("prompt_version"),
    pageUrl: text("page_url"),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull(),
  },
  (t) => [index("feedback_model_idx").on(t.model)],
);

// ---- Jobs and the generation log ---------------------------------------------

export const jobs = pgTable(
  "jobs",
  {
    id: id(),
    type: text("type").notNull(),
    userId: uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
    courseId: text("course_id").references(() => courses.id, { onDelete: "cascade" }),
    payload: jsonb("payload").notNull().default({}),
    status: text("status").notNull().default("queued"), // queued | running | done | failed
    result: jsonb("result"),
    error: text("error"),
    attempts: integer("attempts").notNull().default(0),
    runAfter: timestamp("run_after", { withTimezone: true }).notNull().defaultNow(),
    lockedAt: timestamp("locked_at", { withTimezone: true }),
    createdAt: createdAt(),
    finishedAt: timestamp("finished_at", { withTimezone: true }),
  },
  (t) => [index("jobs_pick_idx").on(t.status, t.runAfter)],
);

/** Append-only: one row per model call that produced content. Never updated or deleted. */
export const generationLog = pgTable(
  "generation_log",
  {
    seq: bigint("seq", { mode: "number" }).primaryKey().generatedAlwaysAsIdentity(),
    jobId: uuid("job_id"),
    userId: uuid("user_id"),
    courseId: text("course_id"),
    jobType: text("job_type").notNull(),
    model: text("model").notNull(),
    promptId: text("prompt_id").notNull(),
    promptVersion: text("prompt_version").notNull(),
    costUsd: numeric("cost_usd", { precision: 12, scale: 6 }).notNull().default("0"),
    builtFrom: jsonb("built_from").$type<string[]>().notNull().default([]),
    warnings: jsonb("warnings").$type<string[]>().notNull().default([]),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().default(sql`now()`),
  },
  (t) => [index("generation_log_course_idx").on(t.courseId)],
);
