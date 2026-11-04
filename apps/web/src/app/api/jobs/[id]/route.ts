import { and, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import type { JobStatus } from "@/lib/job-types";
import { inlineJobs, drain } from "@/lib/jobs";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";

/** Polled by the UI until status is done or failed. */
export const GET = route(async (_req: Request, { params }: { params: Promise<{ id: string }> }) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  const job = await db().query.jobs.findFirst({ where: and(eq(schema.jobs.id, id), eq(schema.jobs.userId, u.id)) });
  if (!job) throw new HttpError(404, "Job not found");
  if (job.status === "queued" && inlineJobs()) void drain(); // in case the kick at enqueue time was lost (dev reloads)
  const body: JobStatus = { id: job.id, type: job.type as JobStatus["type"], status: job.status as JobStatus["status"], result: job.result ?? undefined, error: job.error };
  return NextResponse.json(body);
});
