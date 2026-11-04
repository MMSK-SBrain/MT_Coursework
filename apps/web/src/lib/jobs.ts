// A small Postgres-backed job queue: a `jobs` table, SELECT ... FOR UPDATE SKIP LOCKED to claim, and a worker loop.
// Jobs run in the web process (INLINE_JOBS, default in development) or in `pnpm --filter @cg/web worker`.
import { eq, sql } from "drizzle-orm";
import { db, schema } from "./db";
import { runJob } from "./job-handlers";
import type { JobRequest } from "./job-types";

const { jobs } = schema;
export type JobRow = typeof jobs.$inferSelect;

export const inlineJobs = () =>
  process.env.INLINE_JOBS === "1" || (process.env.INLINE_JOBS === undefined && process.env.NODE_ENV !== "production");

export async function enqueue(userId: string, courseId: string, req: JobRequest): Promise<string> {
  const { type, ...payload } = req;
  const [row] = await db().insert(jobs).values({ type, userId, courseId, payload }).returning({ id: jobs.id });
  if (inlineJobs()) void drain();
  return row!.id;
}

/** Claim the oldest runnable job, or null. */
export async function claimNext(): Promise<JobRow | null> {
  const rows = await db().execute<{ id: string }>(sql`
    update jobs set status = 'running', locked_at = now(), attempts = attempts + 1
    where id = (select id from jobs where status = 'queued' and run_after <= now()
                order by created_at limit 1 for update skip locked)
    returning id`);
  const id = rows[0]?.id;
  if (!id) return null;
  return (await db().query.jobs.findFirst({ where: eq(jobs.id, id) })) ?? null;
}

export async function processJob(job: JobRow): Promise<void> {
  try {
    const result = await runJob(job);
    await db().update(jobs).set({ status: "done", result: result ?? null, finishedAt: new Date(), error: null }).where(eq(jobs.id, job.id));
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e);
    console.error(`[jobs] ${job.type} ${job.id} failed: ${msg}`);
    await db().update(jobs).set({ status: "failed", error: msg, finishedAt: new Date() }).where(eq(jobs.id, job.id));
  }
}

/** Put jobs back in the queue whose worker died mid-run. */
export async function requeueStuck(minutes = 10): Promise<void> {
  await db().execute(sql`
    update jobs set status = 'queued', locked_at = null
    where status = 'running' and locked_at < now() - make_interval(mins => ${minutes}) and attempts < 3`);
}

const g = globalThis as unknown as { __cgDraining?: boolean; __cgKick?: boolean };

/** Run queued jobs until none are left. A call during a running drain makes it look again before it stops. */
export async function drain(): Promise<number> {
  g.__cgKick = true;
  if (g.__cgDraining) return 0;
  g.__cgDraining = true;
  let n = 0;
  try {
    while (g.__cgKick) {
      g.__cgKick = false;
      for (let job = await claimNext(); job; job = await claimNext()) {
        await processJob(job);
        n++;
      }
    }
  } catch (e) {
    console.error("[jobs] drain error", e);
  } finally {
    g.__cgDraining = false;
  }
  return n;
}
