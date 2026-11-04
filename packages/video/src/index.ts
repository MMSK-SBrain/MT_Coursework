import { FREE_TIER, PATH_FAMILY, videoAllowed } from "@cg/core";
import type { Course, VideoBuilder, VideoKind, VideoProject } from "@cg/core";
import { buildProject } from "./compile.js";
import type { RenderableKind } from "./compile.js";
import { findSession, templateOutline, VideoPlanError } from "./outline.js";
import { renderProject } from "./render.js";

export * from "./compile.js";
export * from "./outline.js";
export * from "./render.js";

export interface VideoBuilderOptions {
  /** Limit for plan(). Default: the free tier, 300 s. */
  maxSec?: number;
  /** Target length for template scripts; default depends on the path (shorts 45 s, others 150 s), never above maxSec. */
  targetSec?: number;
  /** Images and clips the user supplied, keyed "assets/<name>". Used by demo and screen videos. */
  media?: Record<string, Uint8Array>;
  draft?: boolean;
}

export class CourseVideoBuilder implements VideoBuilder {
  constructor(private opts: VideoBuilderOptions = {}) {}

  async plan(course: Course, planId: string, sessionId: string): Promise<VideoProject> {
    const { session } = findSession(course, planId, sessionId);
    return this.planKind(course, planId, sessionId, session.video);
  }

  /** Same as plan(), for a kind other than the one saved on the session (still checked against the path). */
  async planKind(course: Course, planId: string, sessionId: string, kind: VideoKind): Promise<VideoProject> {
    const { plan } = findSession(course, planId, sessionId);
    if (kind === "none") throw new VideoPlanError("this session has no video (kind \"none\")");
    if (!videoAllowed(plan.path, kind)) throw new VideoPlanError(`video kind "${kind}" is not allowed on the "${plan.path}" learning path`);
    const maxSec = this.opts.maxSec ?? FREE_TIER.videoSecondsPerMonth;
    const vertical = plan.path === "shorts";
    const targetSec = Math.min(maxSec, this.opts.targetSec ?? (vertical ? 45 : PATH_FAMILY[plan.path] === "content" ? 150 : 120));
    const media = this.opts.media ?? {};
    const outline = templateOutline(course, planId, sessionId, { kind, targetSec, mediaAssets: Object.keys(media) });
    return buildProject(outline, { kind: kind as RenderableKind, path: plan.path, maxSec, media, size: vertical ? "shorts" : "youtube" });
  }

  render(project: VideoProject, opts: { workDir: string; maxSec: number }): Promise<{ mp4Path: string; durationSec: number }> {
    return renderProject(project, { ...opts, draft: this.opts.draft });
  }
}

export const createVideoBuilder = (opts?: VideoBuilderOptions): CourseVideoBuilder => new CourseVideoBuilder(opts);
