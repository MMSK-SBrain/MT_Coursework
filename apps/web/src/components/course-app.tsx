"use client";
import { FREE_TIER, type Course } from "@cg/core";
import { STAGES, type StageId } from "@/lib/catalog";
import type { CourseMeta } from "@/lib/course-meta";
import type { MonthUsage } from "@/lib/quota";
import { CourseProvider, useCourse } from "./course-context";
import { BuildStage } from "./stages/build";
import { FitStage } from "./stages/fit";
import { InputsStage } from "./stages/inputs";
import { OutcomesStage } from "./stages/outcomes";
import { PlansStage } from "./stages/plans";
import { RolesStage } from "./stages/roles";
import { TopBar } from "./top-bar";

const VIEWS: Record<StageId, () => React.JSX.Element> = {
  inputs: InputsStage, roles: RolesStage, fit: FitStage, outcomes: OutcomesStage, plans: PlansStage, build: BuildStage,
};

function progress(c: Course): Record<StageId, "done" | "frozen" | ""> {
  return {
    inputs: c.modules.length ? "done" : "",
    roles: c.roles.some((r) => r.selected) ? "done" : "",
    fit: c.structureConfirmedAt ? "frozen" : "",
    outcomes: c.outcomesFrozenAt ? "frozen" : "",
    plans: c.plans.length ? "done" : "",
    build: c.plans.some((p) => p.sessions.some((s) => s.blocks.length)) ? "done" : "",
  };
}

function Rail() {
  const { course, stage, go } = useCourse();
  const st = progress(course);
  return (
    <nav className="rail" aria-label="Course stages">
      {STAGES.map((s, i) => (
        <button key={s.id} className={`stage ${st[s.id]}`} aria-current={s.id === stage ? "step" : undefined} onClick={() => go(s.id)}>
          <span className="n">{st[s.id] === "frozen" ? "🔒" : st[s.id] === "done" ? "✓" : i + 1}</span>
          <span><span className="t">{s.t}</span><br /><span className="s">{s.s}</span></span>
        </button>
      ))}
      <div className="note">
        Download the whole course design as <span className="mono">.md</span> files at any stage; it&apos;s free.
        <div style={{ marginTop: 8 }}><a className="btn sm" href={`/api/courses/${course.id}/export`}>Export .md (zip)</a></div>
      </div>
    </nav>
  );
}

function Workspace({ email, isAdmin, mock }: { email: string; isAdmin: boolean; mock: boolean }) {
  const { course, usage, stage, error, setError } = useCourse();
  const View = VIEWS[stage];
  return (
    <>
      <TopBar crumb={course.brief.title} email={email} isAdmin={isAdmin} mock={mock}
        usage={<span className="usage" title="Free tier this month">{usage.coursesStarted}/{FREE_TIER.coursesPerMonth} course · {usage.videoSeconds}/{FREE_TIER.videoSecondsPerMonth} s video</span>} />
      <div className="shell">
        <Rail />
        <main>
          <div className="wrap">
            {error && <div className="err" role="alert"><span>{error}</span><button className="btn sm" onClick={() => setError(null)}>Dismiss</button></div>}
            <View />
          </div>
        </main>
      </div>
    </>
  );
}

export function CourseApp(props: { initial: { course: Course; meta: CourseMeta }; usage: MonthUsage; stage: StageId; email: string; isAdmin: boolean; mock: boolean }) {
  return (
    <CourseProvider initial={props.initial} usage={props.usage} stage={props.stage}>
      <Workspace email={props.email} isAdmin={props.isAdmin} mock={props.mock} />
    </CourseProvider>
  );
}
