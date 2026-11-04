import { NextResponse } from "next/server";
import { reserveVideo } from "@/lib/billing";
import { HttpError, route } from "@/lib/http";
import { enqueue, insertJob, kick } from "@/lib/jobs";
import { gateJob, JobRequest } from "@/lib/job-types";
import { credits, loadCourse, monthUsage } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";
type Ctx = { params: Promise<{ id: string }> };

/** Enqueue a generation job. Paid and quota-limited jobs return 402 with a paywall description. */
export const POST = route(async (req: Request, { params }: Ctx) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  const jr = JobRequest.parse(await req.json());
  await loadCourse(u.id, id); // ownership: 404 unless the caller owns the course
  if (jr.type === "renderVideo") {
    // Atomic: the allowance (or an extraVideo credit) is reserved in the same transaction that queues the job.
    const jobId = await reserveVideo(u.id, jr.seconds, (tx) => insertJob(tx, u.id, id, jr));
    kick();
    return NextResponse.json({ jobId }, { status: 202 });
  }
  // Early paywall answer for the UI. The credit itself is reserved atomically by the job (withCredit) before any work.
  const gate = gateJob(jr, await monthUsage(u.id), await credits(u.id));
  if (!gate.allowed) throw new HttpError(402, gate.reason, { paywall: { feature: gate.feature, reason: gate.reason } });
  return NextResponse.json({ jobId: await enqueue(u.id, id, jr) }, { status: 202 });
});
