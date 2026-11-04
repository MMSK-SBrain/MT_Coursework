// Free-tier quotas and paywall gating. Pure functions: the callers load usage and credits from the database.
import { FREE_TIER } from "@cg/core";

export type PaidFeature = (typeof FREE_TIER.paidFeatures)[number];
export const PAID_FEATURES: readonly PaidFeature[] = FREE_TIER.paidFeatures;

export function isPaidFeature(x: unknown): x is PaidFeature {
  return typeof x === "string" && (PAID_FEATURES as readonly string[]).includes(x);
}

export interface MonthUsage {
  coursesStarted: number;
  videoSeconds: number;
}

/** Remaining paid units per feature (bought and not yet used). */
export type Credits = Partial<Record<PaidFeature, number>>;

export type Gate =
  | { allowed: true; consume?: PaidFeature; free: boolean }
  | { allowed: false; feature: PaidFeature; reason: string };

export const FEATURE_LABEL: Record<PaidFeature, string> = {
  caseStudy: "Case study",
  slides: "Slide deck (.pptx)",
  instructorGuideDocx: "Instructor guide (.docx)",
  extraVideo: "Extra video time",
  extraCourse: "Extra course this month",
};

/** "YYYY-MM" in UTC; usage rows are keyed by it. */
export function monthKey(d: Date = new Date()): string {
  return d.toISOString().slice(0, 7);
}

/** Starting a new course: free up to FREE_TIER.coursesPerMonth, then one extraCourse credit per course. */
export function checkCourseStart(usage: MonthUsage, credits: Credits): Gate {
  if (usage.coursesStarted < FREE_TIER.coursesPerMonth) return { allowed: true, free: true };
  if ((credits.extraCourse ?? 0) > 0) return { allowed: true, free: false, consume: "extraCourse" };
  return {
    allowed: false,
    feature: "extraCourse",
    reason: `The free tier includes ${FREE_TIER.coursesPerMonth} course a month, and you have started ${usage.coursesStarted} this month.`,
  };
}

export function freeVideoSecondsLeft(usage: MonthUsage): number {
  return Math.max(0, FREE_TIER.videoSecondsPerMonth - usage.videoSeconds);
}

/** Rendering a video of `seconds`: free while it fits in the monthly allowance, otherwise one extraVideo credit. */
export function checkVideo(usage: MonthUsage, credits: Credits, seconds: number): Gate {
  if (!(seconds > 0)) return { allowed: false, feature: "extraVideo", reason: "Video length must be positive." };
  if (seconds <= freeVideoSecondsLeft(usage)) return { allowed: true, free: true };
  if ((credits.extraVideo ?? 0) > 0) return { allowed: true, free: false, consume: "extraVideo" };
  return {
    allowed: false,
    feature: "extraVideo",
    reason: `This video is ${seconds} s and ${freeVideoSecondsLeft(usage)} s of your free ${FREE_TIER.videoSecondsPerMonth} s this month are left.`,
  };
}

/** Seconds to add to the free usage counter for an allowed video (paid videos do not use the allowance). */
export function freeSecondsUsed(gate: Gate, seconds: number): number {
  return gate.allowed && gate.free ? seconds : 0;
}

/** Features that are always paid (case study, slides, instructor guide): one credit per item. */
export function checkPaidFeature(feature: PaidFeature, credits: Credits): Gate {
  if ((credits[feature] ?? 0) > 0) return { allowed: true, free: false, consume: feature };
  return { allowed: false, feature, reason: `${FEATURE_LABEL[feature]} is a paid feature.` };
}
