// Integration tests against docker Postgres: `cd apps/web && docker compose up -d && pnpm test:int`.
import { FREE_TIER } from "@cg/core";
import { and, eq } from "drizzle-orm";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { reserveVideo, startCourse } from "./billing";
import { newCourse } from "./course-logic";
import { db, schema } from "./db";
import { runJob } from "./job-handlers";
import { insertCourse, assertOwnedSources, credits, monthUsage, saveCourse } from "./repo";
import { sampleCourse } from "./test-fixtures";

process.env.STORAGE_DIR = `/tmp/cg-web-int-${process.pid}`;
const tag = `int-${Date.now()}`;
let alice = "", bob = "";

async function user(name: string) {
  const [u] = await db().insert(schema.users).values({ email: `${name}-${tag}@example.com` }).returning();
  return u!.id;
}
async function grant(userId: string, feature: string, quantity = 1) {
  await db().insert(schema.purchases).values({ userId, feature, quantity, provider: "test", status: "paid" });
}

beforeAll(async () => {
  alice = await user("alice");
  bob = await user("bob");
});
afterAll(async () => {
  await db().delete(schema.users).where(eq(schema.users.id, alice));
  await db().delete(schema.users).where(eq(schema.users.id, bob));
});

describe("quota races", () => {
  it("parallel course starts take only the free slots", async () => {
    const results = await Promise.allSettled(Array.from({ length: 6 }, (_, i) => startCourse(alice, `c-${tag}-${i}`, "Race")));
    const ok = results.filter((r) => r.status === "fulfilled").length;
    expect(ok).toBe(FREE_TIER.coursesPerMonth);
    expect(results.filter((r) => r.status === "rejected").every((r) => (r as PromiseRejectedResult).reason.status === 402)).toBe(true);
    const owned = await db().select().from(schema.courses).where(eq(schema.courses.ownerId, alice));
    expect(owned).toHaveLength(FREE_TIER.coursesPerMonth);
    expect((await monthUsage(alice)).coursesStarted).toBe(FREE_TIER.coursesPerMonth);
  });

  it("an extraCourse credit pays for exactly one more course", async () => {
    await grant(alice, "extraCourse");
    const results = await Promise.allSettled([startCourse(alice, `c-${tag}-x1`, "Paid"), startCourse(alice, `c-${tag}-x2`, "Paid")]);
    expect(results.filter((r) => r.status === "fulfilled")).toHaveLength(1);
    expect((await credits(alice)).extraCourse).toBe(0);
  });

  it("parallel video reservations never exceed the free allowance", async () => {
    const results = await Promise.allSettled(Array.from({ length: 5 }, () => reserveVideo(bob, 120, async () => "queued")));
    expect(results.filter((r) => r.status === "fulfilled")).toHaveLength(Math.floor(FREE_TIER.videoSecondsPerMonth / 120));
    expect((await monthUsage(bob)).videoSeconds).toBeLessThanOrEqual(FREE_TIER.videoSecondsPerMonth);
  });
});

describe("paid exports reserve the credit first", () => {
  it("a failed export leaves no file record and refunds the credit", async () => {
    const { course: sample } = await sampleCourse();
    const course = await insertCourse(bob, { ...sample, id: `c-${tag}-exp`, slug: `c-${tag}-exp` });
    await saveCourse(bob, course, sample.plans.length ? { ...course, plans: sample.plans } : course, {});
    await grant(bob, "slides");
    const plan = sample.plans[0]!, s = plan.sessions[0]!;
    // The exporter throws for a session that does not exist.
    const [bad] = await db().insert(schema.jobs).values({ type: "exportSlides", userId: bob, courseId: course.id, payload: { planId: plan.id, sessionId: "missing" } }).returning();
    await expect(runJob(bad!)).rejects.toThrow();
    expect((await credits(bob)).slides).toBe(1);
    const files = () => db().select().from(schema.uploads).where(and(eq(schema.uploads.ownerId, bob), eq(schema.uploads.courseId, course.id)));
    expect(await files()).toHaveLength(0);
    // A good export takes the credit and records exactly one file.
    const [good] = await db().insert(schema.jobs).values({ type: "exportSlides", userId: bob, courseId: course.id, payload: { planId: plan.id, sessionId: s.id } }).returning();
    await runJob(good!);
    expect((await credits(bob)).slides).toBe(0);
    expect(await files()).toHaveLength(1);
  });

  it("refuses to start without a credit", async () => {
    const { course: sample } = await sampleCourse();
    const course = await insertCourse(alice, { ...newCourse(`c-${tag}-nc`, alice), plans: sample.plans });
    const plan = sample.plans[0]!;
    const [job] = await db().insert(schema.jobs).values({ type: "exportInstructorGuide", userId: alice, courseId: course.id, payload: { planId: plan.id, sessionId: plan.sessions[0]!.id } }).returning();
    await expect(runJob(job!)).rejects.toMatchObject({ status: 402 });
  });
});

describe("source ownership", () => {
  it("rejects a source that is another teacher's upload", async () => {
    const theirs = await insertCourse(bob, newCourse(`c-${tag}-bob`, bob));
    await db().insert(schema.uploads).values({ storageKey: `uploads/${theirs.id}/secret.pdf`, ownerId: bob, courseId: theirs.id, filename: "secret.pdf", mime: "application/pdf", bytes: 1 });
    const mine = newCourse(`c-${tag}-alice`, alice);
    const forged = { ...mine, sources: [{ id: "s", kind: "handout" as const, filename: "x.pdf", mime: "application/pdf", storageKey: `uploads/${theirs.id}/secret.pdf` }] };
    await expect(assertOwnedSources(alice, forged)).rejects.toMatchObject({ status: 403 });
    await expect(assertOwnedSources(bob, { ...theirs, sources: forged.sources })).resolves.toBeUndefined();
  });
});
