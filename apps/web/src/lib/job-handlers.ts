// What each job does: call a stage, apply the result to the course (pure functions in course-logic), save, log.
import type { AssetRef, Course, Generated, InputFile, Provenance } from "@cg/core";
import { randomUUID } from "node:crypto";
import {
  addPlan, applyCaseStudy, applyFit, applyHourPlan, applyLinks, applyOutcomes, applyParsed, applyRoles, findSession, updateSession,
} from "./course-logic";
import type { CourseMeta } from "./course-meta";
import { db, schema } from "./db";
import { JobRequest, PAID_JOBS } from "./job-types";
import type { JobRow } from "./jobs";
import { eq } from "drizzle-orm";
import { HttpError } from "./errors";
import { assertOwnedSources, loadCourse, logGeneration, saveCourse, withCredit } from "./repo";
import { getExporter, getStages } from "./stages";
import { getFile, putFile, removeFile } from "./storage";

export async function runJob(job: JobRow): Promise<unknown> {
  const req = JobRequest.parse({ ...(job.payload as object), type: job.type });
  if (!job.courseId) throw new Error("Job has no course");
  const { course, meta } = await loadCourse(job.userId, job.courseId);
  const stages = getStages();
  const log = (g: Pick<Generated<unknown>, "provenance" | "warnings">) =>
    logGeneration({ jobId: job.id, userId: job.userId, courseId: course.id, jobType: job.type, g });
  const save = (next: Course, m: CourseMeta = meta) => saveCourse(job.userId, course, next, m);
  const warn = (key: string, w: string[]): CourseMeta => ({ ...meta, warnings: { ...meta.warnings, [key]: w } });

  switch (req.type) {
    case "parseInputs": {
      // Never read a storage key unless the uploads table says this owner uploaded it to this course.
      await assertOwnedSources(job.userId, course);
      const files: InputFile[] = await Promise.all(course.sources.map(async (meta) => ({ meta, bytes: await getFile(meta.storageKey) })));
      if (!files.length) throw new HttpError(400, "Upload a handout or a module sheet first");
      const g = await stages.parseInputs(files);
      const [c, m] = applyParsed(course, warn("inputs", g.warnings), g.value, g.provenance);
      await save(c, m);
      await log(g);
      return { gaps: g.value.gaps, warnings: g.warnings };
    }
    case "findRoles": {
      const g = await stages.findRoles(course.brief, course.modules, req.keywords);
      const [c, m] = applyRoles(course, warn("roles", g.warnings), g.value, g.provenance);
      await save(c, m);
      await log(g);
      return { roles: g.value.roles.length, warnings: g.warnings };
    }
    case "proposeFit": {
      const g = await stages.proposeFit(course);
      await save(applyFit(course, g.value), warn("fit", g.warnings));
      await log(g);
      return { changes: g.value.length, warnings: g.warnings };
    }
    case "draftOutcomes": {
      const g = await stages.draftOutcomes(course);
      const [c, m] = applyOutcomes(course, warn("outcomes", g.warnings), g.value);
      await save(c, m);
      await log(g);
      return { warnings: g.warnings };
    }
    case "suggestOutcomeEdits": {
      // Suggestions are shown next to the original; nothing is replaced until the teacher accepts.
      const out = [];
      for (const id of new Set(req.outcomeIds)) {
        const g = await stages.suggestOutcomeEdit(course, id, req.instruction);
        await log(g);
        out.push({ suggestion: g.value, provenance: g.provenance, warnings: g.warnings });
      }
      return { suggestions: out };
    }
    case "draftPlan": {
      let c = course;
      const ids: string[] = [];
      for (const spec of req.specs) {
        const g = await stages.draftPlan(c, spec);
        c = addPlan(c, g.value);
        ids.push(g.value.id);
        await log(g);
      }
      await save(c);
      return { planIds: ids };
    }
    case "draftHourPlan": {
      const g = await stages.draftHourPlan(course, req.planId, req.sessionId);
      await save(applyHourPlan(course, req.planId, req.sessionId, g.value), warn(`hourPlan:${req.sessionId}`, g.warnings));
      await log(g);
      return { blocks: g.value.length, warnings: g.warnings };
    }
    case "findFurtherLearning": {
      const g = await stages.findFurtherLearning(course, req.planId, req.sessionId);
      await save(applyLinks(course, req.planId, req.sessionId, g.value));
      await log(g);
      return { links: g.value.length };
    }
    case "draftCaseStudy": {
      // The credit is reserved before generating and refunded if anything below fails.
      return withCredit(job.userId, "caseStudy", async () => {
        const g = await stages.draftCaseStudy(course, req.planId, req.sessionId, req.label);
        await save(applyCaseStudy(course, req.planId, req.sessionId, g.value));
        await log(g);
        return { caseStudyId: g.value.id };
      });
    }
    case "exportSlides":
    case "exportInstructorGuide": {
      // Credit first: no file and no uploads row exist unless the credit was taken. On failure the row is removed and the credit refunded.
      return withCredit(job.userId, PAID_JOBS[req.type]!, async () => {
        const exporter = getExporter();
        const isSlides = req.type === "exportSlides";
        const bytes = isSlides
          ? await exporter.slides(course, req.planId, req.sessionId)
          : await exporter.instructorGuide(course, req.planId, req.sessionId);
        const ext = isSlides ? "pptx" : "docx";
        // Server-generated name: plan and session ids come from the client and never reach the path.
        const key = `courses/${course.id}/exports/${isSlides ? "slides" : "instructor-guide"}-${randomUUID()}.${ext}`;
        let recorded = false;
        try {
          await putFile(key, bytes);
          await db().insert(schema.uploads).values({
            storageKey: key, ownerId: job.userId, courseId: course.id, filename: key.split("/").pop()!, bytes: bytes.byteLength,
            mime: isSlides ? "application/vnd.openxmlformats-officedocument.presentationml.presentation" : "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
          });
          recorded = true;
          const provenance: Provenance = { model: "exporter", promptId: `exports.${ext}`, promptVersion: "1", costUsd: 0, createdAt: new Date().toISOString(), builtFrom: [req.sessionId] };
          const asset: AssetRef = { kind: isSlides ? "slides" : "instructorGuide", storageKey: key, status: "ready", provenance };
          const { session } = findSession(course, req.planId, req.sessionId);
          await save(updateSession(course, req.planId, req.sessionId, { assets: [...session.assets, asset] }));
          return { storageKey: key };
        } catch (e) {
          if (recorded) await db().delete(schema.uploads).where(eq(schema.uploads.storageKey, key));
          await removeFile(key);
          throw e;
        }
      });
    }
    case "renderVideo": {
      // ponytail: @cg/video's VideoBuilder (explainroo render workers) is not wired yet; the asset is recorded as queued.
      // Quota was checked and usage recorded when the job was enqueued.
      const { session } = findSession(course, req.planId, req.sessionId);
      const provenance: Provenance = { model: "explainroo", promptId: `video.${session.video}`, promptVersion: "0", costUsd: 0, createdAt: new Date().toISOString(), builtFrom: [session.id] };
      const asset: AssetRef = { kind: "video", storageKey: `pending/${randomUUID()}.mp4`, status: "queued", provenance };
      await save(updateSession(course, req.planId, req.sessionId, { assets: [...session.assets, asset] }));
      return { queued: true, seconds: req.seconds };
    }
  }
}
