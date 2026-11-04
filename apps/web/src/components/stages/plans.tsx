"use client";
import { learningOutcomeCoverage, moduleOutcomeCoverage, uncoveredOutcomes, VIDEO_BY_PATH, type Course, type LearningPath, type LearningPlan, type TeachingStyle, type VideoKind } from "@cg/core";
import { useState } from "react";
import { AUDIENCE_VARIANTS, MODES, STYLE_FAMS, STYLES, VIDEO } from "@/lib/catalog";
import { updateSession } from "@/lib/course-logic";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, Head, pad2 } from "../ui";

export function StyleSelect({ value, onChange, label }: { value: TeachingStyle; onChange: (s: TeachingStyle) => void; label: string }) {
  return (
    <select aria-label={label} value={value} onChange={(e) => onChange(e.target.value as TeachingStyle)}>
      {Object.entries(STYLE_FAMS).map(([f, list]) => (
        <optgroup key={f} label={f}>{list.map(([k, v]) => <option key={k} value={k}>{v}</option>)}</optgroup>
      ))}
    </select>
  );
}

const FAMS = [...new Set(Object.values(MODES).map((m) => m.fam))];

function NewPlan({ onCreated }: { onCreated: (id: string) => void }) {
  const { run, busy } = useCourse();
  const [path, setPath] = useState<LearningPath>("flipped");
  const [style, setStyle] = useState<TeachingStyle | "auto">("auto");
  const [variant, setVariant] = useState("one");
  const create = async () => {
    const vs = AUDIENCE_VARIANTS.find((v) => v.id === variant)!.variants;
    const specs = vs.length ? vs.map((v) => ({ path, style, audienceVariant: v, name: `${MODES[path].t} (${v})` })) : [{ path, style, name: MODES[path].t }];
    const st = await run({ type: "draftPlan", specs }, "draftPlan");
    const ids = st?.status === "done" ? (st.result as { planIds: string[] }).planIds : [];
    if (ids[0]) onCreated(ids[0]);
  };
  return (
    <>
      <div className="panel">
        <h2>Learning path</h2>
        <p className="muted small" style={{ margin: "4px 0 12px" }}>How learners meet the content. The path decides what gets built and which video types are allowed.</p>
        {FAMS.map((f) => (
          <div key={f} className="fam">
            <span className="eyebrow">{f}</span>
            <div className="modes">
              {(Object.entries(MODES) as [LearningPath, (typeof MODES)[LearningPath]][]).filter(([, m]) => m.fam === f).map(([k, m]) => (
                <button key={k} className="mode" aria-pressed={path === k} onClick={() => setPath(k)}>
                  <h3>{m.t}</h3><span className="muted small">{m.d}</span><span className="vid">Video: {m.video.map((v) => VIDEO[v]).join(", ")}</span>
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>
      <div className="panel">
        <h2>Default teaching style</h2>
        <p className="muted small" style={{ margin: "4px 0 12px" }}>Used for every session unless you change it. <b>Auto</b> picks per session from the outcome&apos;s Bloom level: Explain styles for Understand, Apply styles for Apply, Investigate styles for Analyse and Evaluate.</p>
        <div className="styles" style={{ marginBottom: 14 }}><button className="style" aria-pressed={style === "auto"} onClick={() => setStyle("auto")}><b>Auto</b><span>Matched to each outcome</span></button></div>
        {Object.entries(STYLE_FAMS).map(([f, list]) => (
          <div key={f} className="fam">
            <span className="eyebrow">{f}</span>
            <div className="styles">{list.map(([k, v, d]) => <button key={k} className="style" aria-pressed={style === k} onClick={() => setStyle(k)}><b>{v}</b><span>{d}</span></button>)}</div>
          </div>
        ))}
      </div>
      <div className="panel">
        <h2>Audience variant <span className="muted" style={{ fontWeight: 500 }}>· optional</span></h2>
        <p className="muted small" style={{ margin: "4px 0 10px" }}>Make two versions of the same plan for different learners.</p>
        <div className="row">{AUDIENCE_VARIANTS.map((v) => <button key={v.id} className="style" aria-pressed={variant === v.id} onClick={() => setVariant(v.id)}><b>{v.label}</b></button>)}</div>
      </div>
      <div className="row" style={{ justifyContent: "flex-end" }}>
        {busy.draftPlan ? <Busy>Drafting the plan…</Busy> : <button className="btn primary" onClick={create}>Draft {MODES[path].t.toLowerCase()} plan{variant !== "one" ? "s" : ""}</button>}
      </div>
    </>
  );
}

export function PlansStage() {
  const { course, save, go, planId, setPlanId } = useCourse();
  const [tab, setTab] = useState<string>(planId && course.plans.some((p) => p.id === planId) ? planId : course.plans[0]?.id ?? "new");
  if (!course.outcomesFrozenAt) {
    return (
      <>
        <Head n={5} title="Learning plans">Freeze the outcomes first. Plans are built on a fixed set of outcomes so that every session traces back to them.</Head>
        <div className="row"><button className="btn seal" onClick={() => go("outcomes")}>Go to outcomes</button></div>
      </>
    );
  }
  const plan = course.plans.find((p) => p.id === tab);
  const select = (id: string) => { setTab(id); if (id !== "new") setPlanId(id); };

  let body;
  if (!plan) body = <NewPlan onCreated={select} />;
  else {
    const m = MODES[plan.path], isContent = m.fam === "Content";
    const unc = new Set(uncoveredOutcomes(course, plan));
    body = (
      <>
        <div className="panel">
          <div className="row between">
            <div><h2>{plan.name}</h2><span className="muted">{m.d} Default style: <b>{STYLES[plan.defaultStyle]}</b>.{plan.audienceVariant && <> Audience: <b>{plan.audienceVariant}</b>.</>}</span></div>
            <div className="row"><span className="chip">{m.fam} path</span><FeedbackWidget courseId={course.id} targetPath={`plans[${plan.id}]`} provenance={plan.provenance} label="plan" /></div>
          </div>
        </div>
        <div className="panel tbl">
          <table>
            <thead><tr><th>#</th><th>{isContent ? "Episode" : "Session"}</th><th>Outcomes</th><th>Style</th><th>Length</th><th>Video</th></tr></thead>
            <tbody>
              {plan.sessions.map((s) => (
                <tr key={s.id}>
                  <td className="mono">{pad2(s.index)}</td>
                  <td>
                    {s.title} {s.stale && <span className="chip warn">Out of date</span>}
                    <div className="meta" style={{ display: "flex", flexWrap: "wrap", gap: 4, marginTop: 4 }}>
                      {s.sessionOutcomes.map((so) => <span key={so.id} className="chip" title={`${so.text} (${so.bloom}) · serves ${so.moduleOutcomeIds.join(", ") || "no module outcome"}`}>{so.id}</span>)}
                      {!s.sessionOutcomes.length && <span className="chip warn">No session outcomes</span>}
                    </div>
                  </td>
                  <td>{s.outcomeIds.map((l) => <span key={l} className="chip ink" style={{ marginRight: 4 }}>{l}</span>)}</td>
                  <td><StyleSelect label={`Style for ${s.index}`} value={s.style} onChange={(st) => save((c) => updateSession(c, plan.id, s.id, { style: st }))} /></td>
                  <td className="mono">{s.minutes} min</td>
                  <td>
                    <select aria-label={`Video for ${s.index}`} value={s.video} onChange={(e) => save((c) => updateSession(c, plan.id, s.id, { video: e.target.value as VideoKind }))}>
                      {VIDEO_BY_PATH[plan.path].map((k) => <option key={k} value={k}>{VIDEO[k]}</option>)}
                    </select>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="panel">
          <h3>Outcome coverage</h3>
          <div className="row" style={{ marginTop: 8 }}>
            {course.outcomes.map((l) => <span key={l.id} className={`chip ${unc.has(l.id) ? "bad" : "ok"}`}>{l.id} {unc.has(l.id) ? "not covered" : "covered"}</span>)}
          </div>
        </div>
        <RollUp course={course} plan={plan} />
        <div className="row" style={{ justifyContent: "flex-end" }}><button className="btn primary" onClick={() => { setPlanId(plan.id); go("build"); }}>Build assets for this plan →</button></div>
      </>
    );
  }
  return (
    <>
      <Head n={5} title="Learning plans">One course can have several plans. Each has a learning path (how learners meet the content) and a default teaching style (how each session runs). All plans are built from the same frozen outcomes.</Head>
      <div className="tabs" role="tablist">
        {course.plans.map((p) => <button key={p.id} className="tab" role="tab" aria-selected={tab === p.id} onClick={() => select(p.id)}>{MODES[p.path].t} · {p.name}</button>)}
        <button className="tab" role="tab" aria-selected={tab === "new"} onClick={() => select("new")}>+ New plan</button>
      </div>
      {body}
    </>
  );
}

/** Roll-up: session outcomes meet module outcomes (at their Bloom level), which meet the course learning outcomes. */
export function RollUp({ course, plan }: { course: Course; plan: LearningPlan }) {
  const mo = moduleOutcomeCoverage(course, plan);
  const lo = learningOutcomeCoverage(course, plan);
  return (
    <div className="panel">
      <div className="row between">
        <h3>Outcome roll-up</h3>
        <span className="muted small">{mo.filter((m) => m.met).length} of {mo.length} module outcomes met · {lo.filter((l) => l.met).length} of {lo.length} learning outcomes met</span>
      </div>
      <div className="tbl" style={{ marginTop: 8 }}>
        <table>
          <thead><tr><th>Module outcome</th><th>Served by</th><th>Status</th></tr></thead>
          <tbody>
            {mo.map((m) => (
              <tr key={m.moduleOutcomeId}>
                <td className="mono">{m.moduleOutcomeId}</td>
                <td>{m.sessionOutcomeIds.map((id) => <span key={id} className="chip" style={{ marginRight: 4 }}>{id}</span>)}</td>
                <td>{m.met ? <span className="chip ok">Met</span> : <span className="chip bad" title={m.problem}>Not met: {m.problem}</span>}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {!mo.length && <p className="muted small" style={{ margin: 0 }}>No module outcomes yet.</p>}
      </div>
      <div className="row" style={{ marginTop: 10 }}>
        {lo.map((l) => <span key={l.outcomeId} className={`chip ${l.met ? "ok" : "bad"}`} title={l.moduleOutcomeIds.join(", ") || "no module outcomes"}>{l.outcomeId} {l.met ? "met" : "not met"}</span>)}
      </div>
    </div>
  );
}
