"use client";
import { useState } from "react";
import { addOwnRole, toggleRole } from "@/lib/course-logic";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, Head } from "../ui";

export function RolesStage() {
  const { course, meta, save, run, busy, go } = useCourse();
  const [sort, setSort] = useState<"match" | "postings">("match");
  const [kw, setKw] = useState<string[] | null>(null); // edited keywords, until the next search
  const [adding, setAdding] = useState("");
  const [own, setOwn] = useState("");
  const keywords = kw ?? meta.keywords ?? [];
  const n = course.roles.filter((r) => r.selected).length;
  const roles = [...course.roles].sort((a, b) => (sort === "match" ? b.moduleMatch - a.moduleMatch : b.postings - a.postings));
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
      <Head n={2} title="Job roles" right={busy.findRoles ? <Busy>Searching postings…</Busy> : <button className="btn" onClick={search} disabled={!course.modules.length}>Search again</button>}>
        The search starts from your module keywords but stays broad, so it also finds neighbouring roles you might not have thought of. Pick the roles this course should prepare people for. The fit check in the next step uses only the roles you pick.
      </Head>
      <div className="panel">
        <div className="row between"><h2>Search built from your modules</h2><span className="muted small">Remove or add keywords, then search again</span></div>
        <div className="row" style={{ marginTop: 10, gap: 6 }}>
          {keywords.map((k) => (
            <span key={k} className="chip">{k} <button aria-label={`Remove ${k}`} onClick={() => setKw(keywords.filter((x) => x !== k))}>×</button></span>
          ))}
          <input className="kwin" aria-label="Add a keyword" placeholder="+ keyword" value={adding} onChange={(e) => setAdding(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && adding.trim()) { setKw([...keywords, adding.trim()]); setAdding(""); } }} />
          {kw && <span className="chip warn">Edited: search again to apply</span>}
        </div>
        <div className="stats" style={{ marginTop: 16 }}>
          <div className="stat"><b>{meta.postingsRead ?? 0}</b><span>Postings read</span></div>
          <div className="stat"><b>{course.roles.filter((r) => !r.addedByUser).length}</b><span>Distinct roles found</span></div>
          <div className="stat"><b>{course.brief.markets.join(", ") || "-"}</b><span>Market</span></div>
          <div className="stat"><b>90 days</b><span>Posting window</span></div>
        </div>
      </div>
      <div className="row between">
        <h2>Roles found <span className="muted" style={{ fontWeight: 500 }}>· {n} selected</span></h2>
        <div className="row">
          {meta.provenance?.roles && <FeedbackWidget courseId={course.id} targetPath="roles" provenance={meta.provenance.roles} label="role search" />}
          <span className="muted small">Sort by</span>
          <select aria-label="Sort roles" value={sort} onChange={(e) => setSort(e.target.value as "match" | "postings")}>
            <option value="match">Match to modules</option>
            <option value="postings">Number of postings</option>
          </select>
        </div>
      </div>
      <div className="roles">
        {roles.map((r) => (
          <div key={r.id} className="role" style={r.selected ? { borderColor: "var(--ink)", boxShadow: "inset 0 0 0 1px var(--ink)" } : undefined}>
            <input type="checkbox" id={`role-${r.id}`} checked={r.selected} onChange={(e) => save((c) => toggleRole(c, r.id, e.target.checked))} />
            <div>
              <label htmlFor={`role-${r.id}`} className="row between" style={{ gap: 6, cursor: "pointer" }}>
                <b>{r.title}</b><span className="mono muted">{r.addedByUser ? "added by you" : `${r.postings} posts`}</span>
              </label>
              {!r.addedByUser && (
                <div className="row" style={{ gap: 8, marginTop: 6, flexWrap: "nowrap" }}>
                  <span className="muted small" style={{ whiteSpace: "nowrap" }}>Module match</span>
                  <div className="bar" style={{ flex: 1 }}><i style={{ width: `${r.moduleMatch}%` }} /></div>
                  <span className="mono">{r.moduleMatch}%</span>
                </div>
              )}
              <div className="meta">
                {r.experience && <span className="chip">{r.experience}</span>}
                {r.skills.map((s) => <span key={s} className="chip">{s}</span>)}
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
        <button className="btn primary" disabled={!n} onClick={toFit}>Check course–job fit for {n} roles →</button>
      </div>
    </>
  );
}
