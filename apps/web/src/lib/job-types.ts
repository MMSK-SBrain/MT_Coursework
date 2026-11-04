// Job requests the UI can enqueue, and which ones are gated. Client-safe (no I/O).
import { EditInstruction, PlanSpec } from "@cg/core";
import { z } from "zod";
import { checkPaidFeature, checkVideo, type Credits, type Gate, type MonthUsage, type PaidFeature } from "./quota";

const at = { planId: z.string(), sessionId: z.string() };

export const JobRequest = z.discriminatedUnion("type", [
  z.object({ type: z.literal("parseInputs") }),
  z.object({ type: z.literal("findRoles"), keywords: z.array(z.string()).optional() }),
  z.object({ type: z.literal("proposeFit") }),
  z.object({ type: z.literal("draftOutcomes") }),
  z.object({ type: z.literal("suggestOutcomeEdits"), outcomeIds: z.array(z.string()).min(1), instruction: EditInstruction }),
  z.object({ type: z.literal("draftPlan"), specs: z.array(PlanSpec).min(1).max(4) }),
  z.object({ type: z.literal("draftHourPlan"), ...at }),
  z.object({ type: z.literal("findFurtherLearning"), ...at }),
  z.object({ type: z.literal("draftCaseStudy"), ...at, label: z.enum(["real", "composite"]) }),
  z.object({ type: z.literal("exportSlides"), ...at }),
  z.object({ type: z.literal("exportInstructorGuide"), ...at }),
  z.object({ type: z.literal("renderVideo"), ...at, seconds: z.number().int().positive().max(3600) }),
]);
export type JobRequest = z.infer<typeof JobRequest>;
export type JobType = JobRequest["type"];

/** Always-paid job types and the feature credit each one uses. */
export const PAID_JOBS: Partial<Record<JobType, PaidFeature>> = {
  draftCaseStudy: "caseStudy",
  exportSlides: "slides",
  exportInstructorGuide: "instructorGuideDocx",
};

/** Paywall check for a job. Free jobs are always allowed. */
export function gateJob(req: JobRequest, usage: MonthUsage, credits: Credits): Gate {
  if (req.type === "renderVideo") return checkVideo(usage, credits, req.seconds);
  const feature = PAID_JOBS[req.type];
  return feature ? checkPaidFeature(feature, credits) : { allowed: true, free: true };
}

export interface JobStatus {
  id: string;
  type: JobType;
  status: "queued" | "running" | "done" | "failed";
  result?: unknown;
  error?: string | null;
}
