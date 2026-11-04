import { FREE_TIER } from "@cg/core";
import { describe, expect, it } from "vitest";
import { gateJob } from "./job-types";
import { checkCourseStart, checkPaidFeature, checkVideo, freeSecondsUsed, freeVideoSecondsLeft, monthKey } from "./quota";

const at = { planId: "p", sessionId: "s" };

describe("quotas", () => {
  it("allows one free course a month, then needs an extraCourse credit", () => {
    expect(checkCourseStart({ coursesStarted: 0, videoSeconds: 0 }, {})).toEqual({ allowed: true, free: true });
    const blocked = checkCourseStart({ coursesStarted: FREE_TIER.coursesPerMonth, videoSeconds: 0 }, {});
    expect(blocked).toMatchObject({ allowed: false, feature: "extraCourse" });
    expect(checkCourseStart({ coursesStarted: 1, videoSeconds: 0 }, { extraCourse: 1 })).toEqual({ allowed: true, free: false, consume: "extraCourse" });
  });

  it("gives 300 free video seconds a month", () => {
    expect(freeVideoSecondsLeft({ coursesStarted: 0, videoSeconds: 120 })).toBe(180);
    const ok = checkVideo({ coursesStarted: 0, videoSeconds: 0 }, {}, 300);
    expect(ok).toEqual({ allowed: true, free: true });
    expect(freeSecondsUsed(ok, 300)).toBe(300);
    expect(checkVideo({ coursesStarted: 0, videoSeconds: 0 }, {}, 301)).toMatchObject({ allowed: false, feature: "extraVideo" });
    expect(checkVideo({ coursesStarted: 0, videoSeconds: 250 }, {}, 60)).toMatchObject({ allowed: false });
    const paid = checkVideo({ coursesStarted: 0, videoSeconds: 250 }, { extraVideo: 1 }, 60);
    expect(paid).toEqual({ allowed: true, free: false, consume: "extraVideo" });
    expect(freeSecondsUsed(paid, 60)).toBe(0);
    expect(checkVideo({ coursesStarted: 0, videoSeconds: 0 }, {}, 0)).toMatchObject({ allowed: false });
  });

  it("keys usage by UTC month", () => {
    expect(monthKey(new Date("2026-11-30T23:59:59Z"))).toBe("2026-11");
  });
});

describe("paywall gating", () => {
  it("locks every always-paid feature without a credit", () => {
    for (const f of ["caseStudy", "slides", "instructorGuideDocx"] as const) {
      expect(checkPaidFeature(f, {})).toMatchObject({ allowed: false, feature: f });
      expect(checkPaidFeature(f, { [f]: 2 })).toMatchObject({ allowed: true, consume: f });
    }
  });

  it("gates jobs: free stages pass, paid ones need credits, video uses the allowance", () => {
    const u = { coursesStarted: 1, videoSeconds: 0 };
    expect(gateJob({ type: "draftHourPlan", ...at }, u, {})).toMatchObject({ allowed: true, free: true });
    expect(gateJob({ type: "findFurtherLearning", ...at }, u, {})).toMatchObject({ allowed: true });
    expect(gateJob({ type: "draftCaseStudy", ...at, label: "composite" }, u, {})).toMatchObject({ allowed: false, feature: "caseStudy" });
    expect(gateJob({ type: "exportSlides", ...at }, u, { slides: 1 })).toMatchObject({ allowed: true, consume: "slides" });
    expect(gateJob({ type: "exportInstructorGuide", ...at }, u, {})).toMatchObject({ allowed: false, feature: "instructorGuideDocx" });
    expect(gateJob({ type: "renderVideo", ...at, seconds: 240 }, u, {})).toMatchObject({ allowed: true, free: true });
    expect(gateJob({ type: "renderVideo", ...at, seconds: 240 }, { ...u, videoSeconds: 240 }, {})).toMatchObject({ allowed: false, feature: "extraVideo" });
  });
});
