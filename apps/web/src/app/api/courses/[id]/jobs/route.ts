import { NextResponse } from "next/server";
import { HttpError, route } from "@/lib/http";
import { enqueue } from "@/lib/jobs";
import { gateJob, JobRequest } from "@/lib/job-types";
import { freeSecondsUsed } from "@/lib/quota";
import { addUsage, consumeCredit, credits, loadCourse, monthUsage } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";
type Ctx = { params: Promise<{ id: string }> };

/** Enqueue a generation job. Paid and quota-limited jobs return 402 with a paywall description. */
export const POST = route(async (req: Request, { params }: Ctx) => {
  const u = await requireTeacherApi();
  const { id } = await params;
  const jr = JobRequest.parse(await req.json());
  await loadCourse(u.id, id); // ownership
  const gate = gateJob(jr, await monthUsage(u.id), await credits(u.id));
  if (!gate.allowed) throw new HttpError(402, gate.reason, { paywall: { feature: gate.feature, reason: gate.reason } });
  if (jr.type === "renderVideo") {
    // Video time is reserved when the render is queued.
    if (gate.free) await addUsage(u.id, { videoSeconds: freeSecondsUsed(gate, jr.seconds) });
    else if (gate.consume && !(await consumeCredit(u.id, gate.consume))) throw new HttpError(402, "No credit left", { paywall: { feature: gate.consume, reason: "No credit left" } });
  }
  const jobId = await enqueue(u.id, id, jr);
  return NextResponse.json({ jobId }, { status: 202 });
});
