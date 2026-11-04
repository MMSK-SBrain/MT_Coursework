"use client";
import { ESCO_ATTRIBUTION } from "@cg/core";
import { useState } from "react";
import { addOwnRole, toggleRole } from "@/lib/course-logic";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, Head, safeHref } from "../ui";

export function RolesStage() {
  const { course, meta, save, run, busy, go } = useCourse();
  const [kw, setKw] = useState<string[] | null>(null); // edited keywords, until the next search
  const [adding, setAdding] = useState("");
  const [own, setOwn] = useState("");
  const keywords = kw ?? meta.keywords ?? [];
  const n = course.roles.filter((r) => r.selected).length;
  const roles = [...course.roles].sort((a, b) => b.moduleMatch - a.moduleMatch);
  const search = async () => {
    await run({ type: "findRoles", keywords });
    setKw(null);
  };
  const toFit = () => {
    go("fit");
    if (!course.fit.length || course.fit.every((f) => f.decision === "pending")) void run({ type: "proposeFit" });
  };

  return (
    <>
      <Head n={2} title="Job roles" right={busy.findRoles ? <Busy>Searching ESCO occupations…</Busy> : <button className="btn" onClick={search} disabled={!course.modules.length}>Search again</button>}>
        The search starts from your module keywords but stays broad, so it also finds neighbouring roles you might not have thought of. Each role is an ESCO occupation; the match shows how many of its essential skills your modules teach. Pick the roles this course should prepare people for. The fit check in the next step uses only the roles you pick.
      </Head>
      <div className="panel">
        <div className="row between"><h2>Search built from your modules</h2><span className="muted small">Remove or add keywords, then search again</span></div>
        <div className="row" style={{ marginTop: 10, gap: 6 }}>
          {keywords.map((k) => (
            <span key={k} className="chip">{k} <button aria-label={`Remove ${k}`} onClick={() => setKw(keywords.filter((x) => x !== k))}>×</button></span>
          ))}
          {keywords.length < 15 && <input className="kwin" aria-label="Add a keyword" placeholder="+ keyword" maxLength={60} value={adding} onChange={(e) => setAdding(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && adding.trim()) { setKw([...keywords, adding.trim()]); setAdding(""); } }} />}
          {kw && <span className="chip warn">Edited: search again to apply</span>}
        </div>
        <div className="stats" style={{ marginTop: 16 }}>
          <div className="stat"><b>{meta.occupationsRead ?? 0}</b><span>ESCO occupations read</span></div>
          <div className="stat"><b>{course.roles.filter((r) => !r.addedByUser).length}</b><span>Relevant roles</span></div>
        </div>
      </div>
      <div className="row between">
        <h2>Roles found <span className="muted" style={{ fontWeight: 500 }}>· {n} selected</span></h2>
        <div className="row">
          {meta.provenance?.roles && <FeedbackWidget courseId={course.id} targetPath="roles" provenance={meta.provenance.roles} label="role search" />}
        </div>
      </div>
      <div className="roles">
        {roles.map((r) => (
          <div key={r.id} className="role" style={r.selected ? { borderColor: "var(--ink)", boxShadow: "inset 0 0 0 1px var(--ink)" } : undefined}>
            <input type="checkbox" id={`role-${r.id}`} checked={r.selected} onChange={(e) => save((c) => toggleRole(c, r.id, e.target.checked))} />
            <div>
              <label htmlFor={`role-${r.id}`} className="row between" style={{ gap: 6, cursor: "pointer" }}>
                <b>{r.title}</b>{r.addedByUser ? <span className="mono muted">added by you</span> : r.evidence[0] && <a className="small" href={safeHref(r.evidence[0].url)} target="_blank" rel="noreferrer">ESCO ↗</a>}
              </label>
              {!r.addedByUser && (
                <div className="row" style={{ gap: 8, marginTop: 6, flexWrap: "nowrap" }}>
                  <span className="muted small" style={{ whiteSpace: "nowrap" }}>Module match</span>
                  <div className="bar" style={{ flex: 1 }}><i style={{ width: `${r.moduleMatch}%` }} /></div>
                  <span className="mono">{r.moduleMatch}%</span>
                </div>
              )}
              {!r.addedByUser && <span className="muted small">{r.matchedSkills.length} of {r.skills.length} essential skills taught</span>}
              <div className="meta">
                {r.matchedSkills.map((s) => <span key={s} className="chip ok" title="Taught by your modules">✓ {s}</span>)}
                {r.skills.filter((s) => !r.matchedSkills.includes(s)).map((s) => <span key={s} className="chip" title="Not covered yet">{s}</span>)}
              </div>
            </div>
          </div>
        ))}
        <div className="role" style={{ gridTemplateColumns: "1fr" }}>
          <div className="field">
            <label htmlFor="addrole">Add a role yourself</label>
            <input id="addrole" placeholder="e.g. Homologation Engineer" value={own} onChange={(e) => setOwn(e.target.value)}
              onKeyDown={(e) => { if (e.key === "Enter" && own.trim()) { void save((c) => addOwnRole(c, own)); setOwn(""); } }} />
            <span className="muted small">Press Enter to add it, selected.</span>
          </div>
        </div>
      </div>
      <div className="row between">
        <button className="btn" onClick={() => go("inputs")}>← Inputs</button>
        <span className="muted small"><a href="https://esco.ec.europa.eu" target="_blank" rel="noreferrer">{ESCO_ATTRIBUTION}</a></span>
        <button className="btn primary" disabled={!n} onClick={toFit}>Check course–job fit for {n} roles →</button>
      </div>
    </>
  );
}
