"use client";
import { FREE_TIER, hourBlockProblems, isHttpUrl, sessionOutcomeProblems, VIDEO_BY_PATH, type CaseStudy, type VideoKind } from "@cg/core";
import { useState } from "react";
import { MODES, SCENES, sceneSeconds, STYLES, VDESC, VIDEO } from "@/lib/catalog";
import { updateSession } from "@/lib/course-logic";
import { freeVideoSecondsLeft } from "@/lib/quota";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, Head, pad2 } from "../ui";
import { PlansStage, RollUp } from "./plans";

// Defense in depth: the schema already rejects non-http(s) URLs.
const safeHref = (u: string) => (isHttpUrl(u) ? u : "#");

const paidChip = <span className="chip seal">Paid</span>;

export function BuildStage() {
  const { course, meta, save, run, busy, usage, planId, setPlanId } = useCourse();
  const [idx, setIdx] = useState(0);
  const [label, setLabel] = useState<CaseStudy["label"]>("composite");
  const plan = course.plans.find((p) => p.id === planId) ?? course.plans[0];
  if (!course.outcomesFrozenAt || !plan) return <PlansStage />;
  const m = MODES[plan.path], isContent = m.fam === "Content";
  const s = plan.sessions[Math.min(idx, plan.sessions.length - 1)]!;
  const at = { planId: plan.id, sessionId: s.id };
  const k = (t: string) => `${t}:${s.id}`;
  const blocks = [...s.blocks].sort((a, b) => a.hour - b.hour || a.startMin - b.startMin);
  const problems = blocks.length ? hourBlockProblems(blocks, s.minutes) : [];
  // Before blocks exist only the SO-level checks apply (every SO "not served" would just be noise).
  const soProblems = blocks.length ? sessionOutcomeProblems(s) : sessionOutcomeProblems({ ...s, blocks: [] }).filter((p) => !p.endsWith("is not served by any block"));
  const warnings = meta.warnings?.[`hourPlan:${s.id}`] ?? [];
  const examples = blocks.filter((b) => b.industryExample);
  const vt = s.video === "none" ? null : s.video;
  const secs = vt ? sceneSeconds(vt) : 0;
  const freeLeft = freeVideoSecondsLeft(usage);
  const unit = isContent ? "Episode" : "Session";
  const hourStatus = s.stale ? <span className="chip warn">Out of date</span> : blocks.length ? <span className="chip ok">Drafted</span> : <span className="chip">Not drafted</span>;

  return (
    <>
      <Head n={`Stage 6 · ${m.t}`} title="Build" right={
        <select aria-label="Plan" value={plan.id} onChange={(e) => { setPlanId(e.target.value); setIdx(0); }}>
          {course.plans.map((x) => <option key={x.id} value={x.id}>{MODES[x.path].t} · {x.name}</option>)}
        </select>
      }>
        Generate and review the assets for each {unit.toLowerCase()}. Approve each one; nothing is final until you do.
      </Head>
      <div className="buildgrid">
        <div className="panel slist">
          {plan.sessions.map((x, i) => (
            <button key={x.id} className="sitem" aria-current={x.id === s.id} onClick={() => setIdx(i)}>
              <span className="mono">{pad2(x.index)}</span>
              <span>{x.title}{x.stale && <> <span className="chip warn">Out of date</span></>}</span>
            </button>
          ))}
        </div>
        <div style={{ display: "flex", flexDirection: "column", gap: 16, minWidth: 0 }}>
          <div className="panel">
            <span className="eyebrow">{unit} {s.index} · {STYLES[s.style]} · {s.minutes} min</span>
            <h2 style={{ marginTop: 4 }}>{s.title}</h2>
            <h3 style={{ margin: "12px 0 0" }}>Session outcomes</h3>
            {s.sessionOutcomes.map((so) => (
              <div key={so.id} className="lo">
                <span className="id">{so.id.split(".").pop()}</span>
                <div>
                  <div>{so.text}</div>
                  <div className="meta">
                    <span className="chip ink">{so.bloom.charAt(0).toUpperCase() + so.bloom.slice(1)}</span>
                    {so.moduleOutcomeIds.map((id) => <span key={id} className="chip ok" title="Serves this module outcome">{id}</span>)}
                    {blocks.length > 0 && !blocks.some((b) => b.sessionOutcomeIds.includes(so.id)) && <span className="chip warn">No block serves it</span>}
                  </div>
                </div>
                <div className="acts"><FeedbackWidget courseId={course.id} targetPath={`plans[${plan.id}].sessions[${s.id}].sessionOutcomes[${so.id}]`} provenance={so.provenance} label={so.id} /></div>
              </div>
            ))}
            {soProblems.map((p) => <div key={p} className="chip warn" style={{ marginTop: 6 }}>{p}</div>)}
            {s.stale && <p className="small" style={{ margin: "6px 0 0", color: "var(--warn)" }}>An outcome or the course structure changed after this {unit.toLowerCase()} was built. Redraft the hour-wise plan to bring it up to date.</p>}
          </div>

          <div className="grid3">
            <div className="deliv">
              <div className="row between"><h3>{isContent ? "Episode plan" : "Hour-wise plan"}</h3>{hourStatus}</div>
              <span className="muted small">Timed blocks traced to {s.outcomeIds.join(", ")}, with industry examples and quick checks</span>
              <div className="row">{busy[k("hour")] ? <Busy>Drafting…</Busy> : <button className="btn sm primary" onClick={() => run({ type: "draftHourPlan", ...at }, k("hour"))}>{blocks.length ? "Redraft" : "Draft"}</button>}</div>
            </div>
            <div className="deliv">
              <div className="row between"><h3>Case study</h3>{paidChip}</div>
              <span className="muted small">Labelled real (sourced, with checkable links) or composite</span>
              <div className="row">
                <select aria-label="Case study kind" value={label} onChange={(e) => setLabel(e.target.value as CaseStudy["label"])}><option value="composite">Composite</option><option value="real">Real, sourced</option></select>
                {busy[k("cs")] ? <Busy>Writing…</Busy> : <button className="btn sm" onClick={() => run({ type: "draftCaseStudy", ...at, label }, k("cs"))}>Draft</button>}
              </div>
            </div>
            <div className="deliv">
              <div className="row between"><h3>Slides (.pptx)</h3>{paidChip}</div>
              <span className="muted small">A deck from the hour-wise plan</span>
              <div className="row">{busy[k("slides")] ? <Busy>Building…</Busy> : <button className="btn sm" disabled={!blocks.length} onClick={() => run({ type: "exportSlides", ...at }, k("slides"))}>Generate</button>}</div>
            </div>
            <div className="deliv">
              <div className="row between"><h3>Instructor guide (.docx)</h3>{paidChip}</div>
              <span className="muted small">Talking points, likely questions, misconceptions</span>
              <div className="row">{busy[k("guide")] ? <Busy>Building…</Busy> : <button className="btn sm" disabled={!blocks.length} onClick={() => run({ type: "exportInstructorGuide", ...at }, k("guide"))}>Generate</button>}</div>
            </div>
          </div>

          <div className="panel blocks">
            <div className="row between"><h2>{isContent ? "Episode plan" : "Hour-wise plan"}</h2>{hourStatus}</div>
            {[...problems, ...(blocks.length ? soProblems : []), ...warnings].map((p) => <div key={p} className="chip warn" style={{ marginTop: 6 }}>{p}</div>)}
            {!blocks.length && <p className="muted" style={{ margin: "8px 0 0" }}>Not drafted yet. Draft it above; it is free.</p>}
            {[...new Set(blocks.map((b) => b.hour))].map((h) => (
              <div key={h}>
                <div className="hour">Hour {h}</div>
                {blocks.filter((b) => b.hour === h).map((b) => (
                  <div key={b.id} className="block">
                    <div><span className="mono muted">{pad2(b.startMin)}–{pad2(b.startMin + b.minutes)}</span><br /><span className="chip">{b.kind}</span></div>
                    <div>
                      <b>{b.title}</b> <span className="muted small">· {b.minutes} min · {STYLES[b.style]}</span>
                      <div className="small">{b.activity}</div>
                      <div className="meta" style={{ display: "flex", gap: 4, marginTop: 4 }}>{b.sessionOutcomeIds.map((o) => <span key={o} className="chip" title={s.sessionOutcomes.find((x) => x.id === o)?.text}>serves {o.split(".").pop()}</span>)}{b.outcomeIds.map((o) => <span key={o} className="chip ink">{o}</span>)}{b.needsSlides && <span className="chip">Slides</span>}</div>
                      {b.check.length > 0 && <ul>{b.check.map((q) => <li key={q}>{q}</li>)}</ul>}
                      <div style={{ marginTop: 6 }}><FeedbackWidget courseId={course.id} targetPath={`plans[${plan.id}].sessions[${s.id}].blocks[${b.id}]`} provenance={b.provenance} label={b.title} /></div>
                    </div>
                  </div>
                ))}
              </div>
            ))}
          </div>

          <div className="panel">
            <h2>Industry examples</h2>
            {!examples.length && <p className="muted" style={{ margin: "8px 0 0" }}>Examples come with the hour-wise plan.</p>}
            {examples.map((b) => (
              <div key={b.id} className="link">
                <div>
                  <span className="muted small">{b.title} · {b.industryExample!.sector}</span>
                  <div>{b.industryExample!.text}</div>
                  {b.industryExample!.sources.map((x) => <a key={x.url} className="small" href={safeHref(x.url)} target="_blank" rel="noreferrer">{x.title}</a>)}
                </div>
                <FeedbackWidget courseId={course.id} targetPath={`plans[${plan.id}].sessions[${s.id}].blocks[${b.id}].industryExample`} provenance={b.provenance} label="example" />
              </div>
            ))}
          </div>

          <div className="panel">
            <div className="row between">
              <h2>Further learning</h2>
              {busy[k("links")] ? <Busy>Searching…</Busy> : <button className="btn sm" onClick={() => run({ type: "findFurtherLearning", ...at }, k("links"))}>{s.links.length ? "Find more" : "Find links"}</button>}
            </div>
            <p className="muted small" style={{ margin: "4px 0 0" }}>Only approved links go into the export.</p>
            {s.links.map((l) => (
              <div key={l.id} className="link">
                <div>
                  <span className="chip">{l.kind}</span> <a href={safeHref(l.url)} target="_blank" rel="noreferrer"><b>{l.title}</b></a>
                  {l.channelOrSite && <span className="muted small"> · {l.channelOrSite}</span>}
                  {!l.alive && <span className="chip bad">Link is dead</span>}
                  <div className="muted small">{l.why}</div>
                  <FeedbackWidget courseId={course.id} targetPath={`plans[${plan.id}].sessions[${s.id}].links[${l.id}]`} provenance={s.provenance} label={l.title} />
                </div>
                <button className="lock" aria-pressed={l.approved} onClick={() => save((c) => updateSession(c, plan.id, s.id, { links: s.links.map((x) => (x.id === l.id ? { ...x, approved: !x.approved } : x)) }))}>{l.approved ? "Approved" : "Approve"}</button>
              </div>
            ))}
          </div>

          {s.caseStudies.length > 0 && (
            <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              <h2>Case studies</h2>
              {s.caseStudies.map((c) => (
                <div key={c.id} className="cs">
                  <div className="row between"><h3>{c.title}</h3><span className={`chip ${c.label === "real" ? "ok" : "ink"}`}>{c.label === "real" ? "Real, sourced" : "Composite"}</span></div>
                  <span className="small">{c.background}</span>
                  {c.data && <pre>{c.data}</pre>}
                  <ol>{c.questions.map((q) => <li key={q}>{q}</li>)}</ol>
                  <span className="muted small"><b>Teaching note:</b> {c.teachingNote}</span>
                  {c.sources.map((x) => <a key={x.url} className="small" href={safeHref(x.url)} target="_blank" rel="noreferrer">{x.title}</a>)}
                  <FeedbackWidget courseId={course.id} targetPath={`plans[${plan.id}].sessions[${s.id}].caseStudies[${c.id}]`} provenance={c.provenance} label="case study" />
                </div>
              ))}
            </div>
          )}

          {s.assets.length > 0 && (
            <div className="panel">
              <h2>Files</h2>
              {s.assets.map((a) => (
                <div key={a.storageKey} className="link">
                  <span>{a.kind === "slides" ? "Slides (.pptx)" : a.kind === "instructorGuide" ? "Instructor guide (.docx)" : "Video"} <span className={`chip ${a.status === "ready" ? "ok" : a.status === "failed" ? "bad" : "warn"}`}>{a.status}</span></span>
                  {a.status === "ready" && a.kind !== "video" ? <a className="btn sm" href={`/api/files/${a.storageKey.split("/").map(encodeURIComponent).join("/")}`}>Download</a> : <span className="muted small">{a.kind === "video" ? "Waiting for the video renderer" : ""}</span>}
                </div>
              ))}
            </div>
          )}

          <RollUp course={course} plan={plan} />

          <div className="panel">
            <div className="row between">
              <h2>Video</h2>
              <span className="muted small">{VIDEO_BY_PATH[plan.path].length === 1 ? "This path has no video" : `Allowed for this path: ${VIDEO_BY_PATH[plan.path].filter((v) => v !== "none").map((v) => VIDEO[v]).join(", ")}`}</span>
            </div>
            <div className="vtypes" style={{ marginTop: 12 }}>
              {VIDEO_BY_PATH[plan.path].map((kind: VideoKind) => (
                <button key={kind} className="opt" aria-pressed={s.video === kind} onClick={() => save((c) => updateSession(c, plan.id, s.id, { video: kind }))}><b>{VIDEO[kind]}</b><span>{VDESC[kind]}</span></button>
              ))}
            </div>
            {vt && (
              <>
                <h3 style={{ margin: "16px 0 4px" }}>Scene plan</h3>
                <p className="muted small" style={{ margin: "0 0 6px" }}>Edit the script and scenes before rendering; it&apos;s the cheapest place to make changes. (Sample scenes until the video planner is connected.)</p>
                {(SCENES[vt] ?? []).map(([tc, kind, w]) => <div key={tc + w} className="scene"><span className="mono">{tc}</span><span className="chip">{kind}</span><span className="what">{w}</span></div>)}
                <p className="muted small" style={{ margin: "10px 0 0" }}>About {Math.round(secs / 60 * 10) / 10} min. Free this month: {freeLeft} of {FREE_TIER.videoSecondsPerMonth} s left{secs > freeLeft ? "; this one needs extra video time" : ""}.</p>
                <div className="row" style={{ marginTop: 12, justifyContent: "flex-end" }}>
                  <button className="btn" disabled title="Arrives with the explainroo render workers">Add asset</button>
                  {busy[k("video")] ? <Busy>Queuing…</Busy> : <button className="btn primary" disabled={!secs} onClick={() => run({ type: "renderVideo", ...at, seconds: secs }, k("video"))}>Render final</button>}
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
