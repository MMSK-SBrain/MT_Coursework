"use client";
// Client state for one course: optimistic saves (PUT the whole course; the server validates and marks stale sessions)
// and generation jobs (enqueue, then poll until done).
import type { Course } from "@cg/core";
import { createContext, useCallback, useContext, useRef, useState, type ReactNode } from "react";
import type { CourseMeta } from "@/lib/course-meta";
import type { JobRequest, JobStatus } from "@/lib/job-types";
import type { StageId } from "@/lib/catalog";
import type { MonthUsage, PaidFeature } from "@/lib/quota";
import { api, ApiError, sleep } from "./api";
import { usePaywall } from "./paywall";

type Mutator = (c: Course, m: CourseMeta) => Course | [Course, CourseMeta];

export interface CourseCtx {
  course: Course;
  meta: CourseMeta;
  usage: MonthUsage;
  save: (fn: Mutator) => Promise<void>;
  run: (req: JobRequest, key?: string) => Promise<JobStatus | null>;
  busy: Record<string, boolean>;
  error: string | null;
  setError: (e: string | null) => void;
  stage: StageId;
  go: (s: StageId) => void;
  planId: string | null;
  setPlanId: (id: string | null) => void;
  refreshUsage: () => Promise<void>;
}

const Ctx = createContext<CourseCtx | null>(null);
export const useCourse = () => {
  const c = useContext(Ctx);
  if (!c) throw new Error("useCourse outside CourseProvider");
  return c;
};

export function CourseProvider(props: { initial: { course: Course; meta: CourseMeta }; usage: MonthUsage; stage: StageId; children: ReactNode }) {
  const [course, setCourse] = useState(props.initial.course);
  const [meta, setMeta] = useState(props.initial.meta);
  const [usage, setUsage] = useState(props.usage);
  const [busy, setBusy] = useState<Record<string, boolean>>({});
  const [error, setError] = useState<string | null>(null);
  const [stage, setStage] = useState<StageId>(props.stage);
  const [planId, setPlanId] = useState<string | null>(props.initial.course.plans[0]?.id ?? null);
  const ref = useRef({ course, meta });
  ref.current = { course, meta };
  const queue = useRef<Promise<void>>(Promise.resolve());
  const ask = usePaywall();
  const url = `/api/courses/${course.id}`;

  const reload = useCallback(async () => {
    const r = await api<{ course: Course; meta: CourseMeta }>(url);
    setCourse(r.course);
    setMeta(r.meta);
  }, [url]);

  const refreshUsage = useCallback(async () => {
    const r = await api<{ usage: MonthUsage }>("/api/usage");
    setUsage(r.usage);
  }, []);

  const save = useCallback(
    (fn: Mutator) => {
      const p = queue.current.then(async () => {
        const { course: c0, meta: m0 } = ref.current;
        let next: Course, nextMeta: CourseMeta;
        try {
          const r = fn(c0, m0);
          [next, nextMeta] = Array.isArray(r) ? r : [r, m0];
        } catch (e) {
          setError(e instanceof Error ? e.message : String(e));
          return;
        }
        setCourse(next);
        setMeta(nextMeta);
        ref.current = { course: next, meta: nextMeta };
        try {
          const r = await api<{ course: Course; meta: CourseMeta }>(url, { method: "PUT", json: { course: next, meta: nextMeta } });
          setCourse(r.course);
          setMeta(r.meta);
          ref.current = r;
        } catch (e) {
          setError(e instanceof Error ? e.message : "Could not save");
          await reload().catch(() => {});
        }
      });
      queue.current = p;
      return p;
    },
    [url, reload],
  );

  const run = useCallback(
    async (req: JobRequest, key: string = req.type): Promise<JobStatus | null> => {
      setBusy((b) => ({ ...b, [key]: true }));
      setError(null);
      try {
        await queue.current; // let pending saves land first
        let jobId: string;
        for (;;) {
          try {
            jobId = (await api<{ jobId: string }>(`${url}/jobs`, { method: "POST", json: req })).jobId;
            break;
          } catch (e) {
            const pw = e instanceof ApiError ? (e.body.paywall as { feature: PaidFeature; reason: string } | undefined) : undefined;
            if (pw && (await ask(pw.feature, pw.reason))) continue; // paid: try again
            if (pw) return null;
            throw e;
          }
        }
        let st: JobStatus;
        for (let wait = 400; ; wait = Math.min(wait * 1.3, 2000)) {
          await sleep(wait);
          st = await api<JobStatus>(`/api/jobs/${jobId}`);
          if (st.status === "done" || st.status === "failed") break;
        }
        await reload();
        if (req.type === "renderVideo") await refreshUsage();
        if (st.status === "failed") setError(st.error ?? "Generation failed");
        return st;
      } catch (e) {
        setError(e instanceof Error ? e.message : String(e));
        return null;
      } finally {
        setBusy((b) => ({ ...b, [key]: false }));
      }
    },
    [url, ask, reload, refreshUsage],
  );

  const go = useCallback((s: StageId) => {
    setStage(s);
    const u = new URL(window.location.href);
    u.searchParams.set("stage", s);
    window.history.replaceState(null, "", u);
    window.scrollTo(0, 0);
  }, []);

  return (
    <Ctx.Provider value={{ course, meta, usage, save, run, busy, error, setError, stage, go, planId, setPlanId, refreshUsage }}>
      {props.children}
    </Ctx.Provider>
  );
}
