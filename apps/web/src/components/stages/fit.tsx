"use client";
import type { FitChange } from "@cg/core";
import { useState } from "react";
import { addOwnFit, allFitDecided, confirmStructure, decideFit, reopenStructure, roleCoverage } from "@/lib/course-logic";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, Head } from "../ui";

const kindChip = (k: FitChange["kind"]) =>
  k === "add" ? <span className="chip ok">Add</span> : k === "strengthen" ? <span className="chip ink">Strengthen</span> : <span className="chip warn">Trim</span>;
const status = (d: FitChange["decision"]) =>
  ({ accepted: <span className="chip ok">Accepted</span>, changed: <span className="chip ink">Changed</span>, rejected: <span className="chip bad">Rejected</span>, pending: null })[d];

export function FitStage() {
  const { course, meta, save, run, busy, go } = useCourse();
  const [edit, setEdit] = useState<{ id: string; text: string; target: string; hours: string } | null>(null);
  const [own, setOwn] = useState("");
  const roles = course.roles.filter((r) => r.selected);
  const decided = course.fit.filter((f) => f.decision !== "pending").length;
  const all = allFitDecided(course) && course.fit.length > 0;
  const cov = roles.map((r) => [r, roleCoverage(course, r)] as const);
  const avg = (i: 0 | 1) => Math.round(cov.reduce((a, [, c]) => a + c[i], 0) / Math.max(cov.length, 1));
  const applied = course.fit.filter((f) => f.decision === "accepted" || f.decision === "changed").length;
  const confirmed = !!course.structureConfirmedAt;
  const toOutcomes = () => {
    go("outcomes");
    if (meta.outcomesDraftedFor !== course.structureVersion) void run({ type: "draftOutcomes" });
  };

  return (
    <>
      <Head n={3} title="Course–job fit" right={busy.proposeFit ? <Busy>Comparing modules with the roles…</Busy> : <button className="btn" onClick={() => run({ type: "proposeFit" })} disabled={!roles.length}>Propose again</button>}>
        Your modules compared with what the {roles.length} selected roles ask for. Each proposed change says why. Accept it, change it (different module, wording or hours), or reject it, then confirm the course structure.
      </Head>
      {confirmed && (
        <div className="sealbar">
          <span>🔒 Course structure v{course.structureVersion} confirmed: {applied} changes applied.</span>
          <button className="btn" onClick={() => save((c) => reopenStructure(c))}>Reopen</button>
        </div>
      )}
      <div className="panel">
        <div className="row between"><h2>Coverage of selected roles</h2><span className="muted small">Grey: today · Green: after the accepted changes</span></div>
        <div style={{ marginTop: 10 }}>
          {cov.map(([r, [b, a]]) => (
            <div key={r.id} className="cov">
              <span>{r.title}</span>
              <div style={{ display: "flex", flexDirection: "column", gap: 3 }}>
                <div className="bar"><i style={{ width: `${b}%`, background: "var(--muted)" }} /></div>
                <div className="bar"><i className="after" style={{ width: `${a}%` }} /></div>
              </div>
              <span className="mono">{b}% → {a}%</span>
            </div>
          ))}
        </div>
        <p className="muted small" style={{ margin: "10px 0 0" }}>Overall fit {avg(0)}% → {avg(1)}% if every change is accepted.</p>
      </div>
      <div className="panel">
        <div className="row between"><h2>Proposed changes</h2><span className="muted small">{decided} of {course.fit.length} decided</span></div>
        {!course.fit.length && !busy.proposeFit && <p className="muted">No proposals yet.</p>}
        <div style={{ marginTop: 4 }}>
          {course.fit.map((f) => (
            <div key={f.id} className={`change ${f.decision !== "pending" ? "decided" : ""}`}>
              <div className="row" style={{ gap: 4 }}>{kindChip(f.kind)}<span className="chip">{f.targetModuleId === "new" ? "New" : f.targetModuleId}</span></div>
              <div>
                <b>{f.text}</b> <span className="mono muted">{f.hoursDelta > 0 ? "+" : ""}{f.hoursDelta} h</span><br />
                <span className="muted small">{f.reason}</span>
                {f.academicConflict && <div style={{ marginTop: 6 }}><span className="chip seal" title={f.academicConflict}>Academic requirement</span></div>}
                {edit?.id === f.id && (
                  <>
                    <div className="edit">
                      <input className="txtin" aria-label="Change wording" value={edit.text} onChange={(e) => setEdit({ ...edit, text: e.target.value })} />
                      <select aria-label="Target module" value={edit.target} onChange={(e) => setEdit({ ...edit, target: e.target.value })}>
                        {course.modules.map((m) => <option key={m.id} value={m.id}>{m.id} · {m.title.slice(0, 28)}…</option>)}
                        <option value="new">New module</option>
                      </select>
                      <input className="txtin" aria-label="Hours" value={edit.hours} onChange={(e) => setEdit({ ...edit, hours: e.target.value })} />
                    </div>
                    <div className="row" style={{ marginTop: 8 }}>
                      <button className="btn sm primary" onClick={() => {
                        const h = Number.parseFloat(edit.hours);
                        void save((c) => decideFit(c, f.id, "changed", { text: edit.text.trim() || f.text, targetModuleId: edit.target, hoursDelta: Number.isFinite(h) ? h : f.hoursDelta }));
                        setEdit(null);
                      }}>Save change</button>
                      <button className="btn sm" onClick={() => setEdit(null)}>Cancel</button>
                    </div>
                  </>
                )}
                <div style={{ marginTop: 6 }}><FeedbackWidget courseId={course.id} targetPath={`fit[${f.id}]`} provenance={f.provenance} label={f.text} /></div>
              </div>
              <div className="acts">
                {f.decision !== "pending" ? (
                  <>{status(f.decision)}<button className="btn sm" disabled={confirmed} onClick={() => save((c) => decideFit(c, f.id, "pending"))}>Undo</button></>
                ) : (
                  <>
                    <button className="btn sm primary" onClick={() => save((c) => decideFit(c, f.id, "accepted"))}>Accept</button>
                    <button className="btn sm" onClick={() => setEdit({ id: f.id, text: f.text, target: f.targetModuleId, hours: `${f.hoursDelta} h` })}>Change</button>
                    <button className="btn sm" onClick={() => save((c) => decideFit(c, f.id, "rejected"))}>Reject</button>
                  </>
                )}
              </div>
            </div>
          ))}
        </div>
        {!confirmed && (
          <div className="row" style={{ marginTop: 12 }}>
            <input className="txtin" aria-label="Propose your own change" placeholder="Propose your own change, e.g. “Add a session on homologation in M8”" style={{ flex: 1, minWidth: 200 }} value={own} onChange={(e) => setOwn(e.target.value)} />
            <button className="btn" disabled={!own.trim()} onClick={() => { void save((c) => addOwnFit(c, own)); setOwn(""); }}>Add</button>
          </div>
        )}
      </div>
      <div className="row between">
        <button className="btn" onClick={() => go("roles")}>← Job roles</button>
        {confirmed ? (
          <button className="btn primary" onClick={toOutcomes}>Draft outcomes →</button>
        ) : (
          <button className="btn seal" disabled={!all} title={all ? "" : "Decide every change first"} onClick={() => save((c, m) => confirmStructure(c, m))}>Confirm course structure</button>
        )}
      </div>
    </>
  );
}
