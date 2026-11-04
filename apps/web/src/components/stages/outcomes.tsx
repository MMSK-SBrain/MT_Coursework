"use client";
import { outcomeVerbProblem, type EditInstruction, type ModuleOutcome, type Objective, type Outcome, type OutcomeSuggestion, type Provenance } from "@cg/core";
import { useState } from "react";
import { cap, QUICK } from "@/lib/catalog";
import { acceptSuggestion, editOutcomeText, freezeOutcomes, setLocked, unfreezeOutcomes } from "@/lib/course-logic";
import { staleSessionCount } from "@/lib/stale";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, EditableText, Head } from "../ui";

type Prop = { suggestion: OutcomeSuggestion; provenance: Provenance; instruction: EditInstruction };

const srcChip = (s: Outcome["origin"]) =>
  s === "handout" ? <span className="chip">From handout</span> : s === "fit" ? <span className="chip ok">From job fit</span> : s === "user" ? <span className="chip">Yours</span> : <span className="chip ink">New</span>;

export function OutcomesStage() {
  const { course, save, run, busy, go } = useCourse();
  const [sugOpen, setSugOpen] = useState<Record<string, boolean>>({});
  const [sugText, setSugText] = useState<Record<string, string>>({});
  const [props, setProps] = useState<Record<string, Prop>>({});
  const [bulkOpen, setBulkOpen] = useState(false);
  const [bulkText, setBulkText] = useState("");
  const frozen = !!course.outcomesFrozenAt;
  const confirmed = !!course.structureConfirmedAt;
  const roleTitle = (id: string) => course.roles.find((r) => r.id === id)?.title;

  const suggest = async (ids: string[], instruction: EditInstruction, key: string) => {
    const st = await run({ type: "suggestOutcomeEdits", outcomeIds: ids, instruction }, key);
    const res = st?.status === "done" ? (st.result as { suggestions: { suggestion: OutcomeSuggestion; provenance: Provenance }[] }) : null;
    if (!res) return;
    setProps((p) => ({ ...p, ...Object.fromEntries(res.suggestions.map((s) => [s.suggestion.targetId, { ...s, instruction }])) }));
  };
  const drop = (id: string) => {
    setProps(({ [id]: _, ...rest }) => rest);
    setSugOpen((s) => ({ ...s, [id]: false }));
  };

  type Kind = "co" | "lo" | "mo";
  const item = (o: Objective | Outcome | ModuleOutcome, kind: Kind, moduleId?: string) => {
    const lo = kind === "lo" ? (o as Outcome) : null;
    const mo = kind === "mo" ? (o as ModuleOutcome) : null;
    const locked = frozen || o.locked;
    const p = props[o.id];
    const problem = lo ? outcomeVerbProblem(lo) : mo ? outcomeVerbProblem(mo) : null;
    const path = kind === "lo" ? `outcomes[${o.id}]` : kind === "mo" ? `modules[${moduleId}].outcomes[${o.id}]` : `objectives[${o.id}]`;
    return (
      <div key={o.id} className="lo">
        <span className="id">{o.id}</span>
        <div>
          <EditableText value={o.text} editable={!locked} label={`Text of ${o.id}`} onCommit={(t) => save((c) => editOutcomeText(c, o.id, t))} />
          {lo && (
            <div className="meta">
              <span className="chip ink">{cap(lo.bloom)}</span>
              {lo.moduleIds.map((m) => <span key={m} className="chip">{m}</span>)}
              {lo.roleIds.map(roleTitle).filter(Boolean).map((t) => <span key={t} className="chip ok">{t}</span>)}
              {srcChip(lo.origin)}
              {problem && <span className="chip warn" title={problem}>Check the verb</span>}
            </div>
          )}
          {mo && (
            <div className="meta">
              <span className="chip ink">{cap(mo.bloom)}</span>
              {mo.outcomeIds.map((id) => <span key={id} className="chip ok" title="Serves this learning outcome">{id}</span>)}
              {!mo.outcomeIds.length && <span className="chip warn">Serves no learning outcome</span>}
              {problem && <span className="chip warn" title={problem}>Check the verb</span>}
            </div>
          )}
          {sugOpen[o.id] && !locked && !p && (
            <div className="suggest">
              <span className="small" style={{ fontWeight: 600 }}>How should {o.id} change?</span>
              <div className="row" style={{ gap: 6 }}>
                {QUICK.map(([k, v]) => <button key={k} className="chip" disabled={busy[`sug-${o.id}`]} onClick={() => suggest([o.id], { kind: k, note: "" }, `sug-${o.id}`)}>{v}</button>)}
              </div>
              <div className="row">
                <input className="txtin" aria-label={`Your instruction for ${o.id}`} placeholder="Or say it in your words, e.g. “focus on the BMS capstone”" value={sugText[o.id] ?? ""} onChange={(e) => setSugText({ ...sugText, [o.id]: e.target.value })} style={{ flex: 1, minWidth: 200 }} />
                <button className="btn sm primary" disabled={!sugText[o.id]?.trim() || busy[`sug-${o.id}`]} onClick={() => suggest([o.id], { kind: "free", note: sugText[o.id]!.trim() }, `sug-${o.id}`)}>Suggest</button>
                <button className="btn sm" onClick={() => setSugOpen({ ...sugOpen, [o.id]: false })}>Cancel</button>
                {busy[`sug-${o.id}`] && <Busy>Writing a suggestion…</Busy>}
              </div>
            </div>
          )}
          {p && (
            <div className="prop">
              <span className="eyebrow">Suggested rewrite</span>
              <del>{o.text}</del>
              {p.suggestion.proposed.map((x, i) => <ins key={i}>{i > 0 ? `${o.id}${String.fromCharCode(97 + i)}: ` : ""}{x.text}{(lo ?? mo) && x.bloom !== (lo ?? mo)!.bloom ? ` (${cap(x.bloom)})` : ""}</ins>)}
              <span className="muted small">{p.suggestion.reason}</span>
              <div className="row">
                <button className="btn sm primary" onClick={() => { void save((c) => acceptSuggestion(c, p.suggestion, p.provenance)); drop(o.id); }}>Accept</button>
                <button className="btn sm" disabled={busy[`sug-${o.id}`]} onClick={() => suggest([o.id], p.instruction, `sug-${o.id}`)}>Try again</button>
                <button className="btn sm" onClick={() => drop(o.id)}>Discard</button>
                <FeedbackWidget courseId={course.id} targetPath={`suggestion[${o.id}]`} provenance={p.provenance} label="suggestion" />
              </div>
            </div>
          )}
          <div style={{ marginTop: 6 }}><FeedbackWidget courseId={course.id} targetPath={path} provenance={o.provenance} label={o.id} /></div>
        </div>
        <div className="acts">
          {frozen ? <span className="chip seal">Frozen</span> : (
            <>
              {!locked && <button className="btn sm" onClick={() => setSugOpen({ ...sugOpen, [o.id]: !sugOpen[o.id] })}>Suggest edit</button>}
              <button className="lock" aria-pressed={o.locked} onClick={() => { void save((c) => setLocked(c, o.id, !o.locked)); setSugOpen({ ...sugOpen, [o.id]: false }); }}>{o.locked ? "Locked" : "Lock"}</button>
            </>
          )}
        </div>
      </div>
    );
  };

  if (!confirmed && !course.outcomes.length) {
    return (
      <>
        <Head n={4} title="Outcomes">Outcomes are drafted from the confirmed course structure. Confirm it first.</Head>
        <div className="row"><button className="btn seal" onClick={() => go("fit")}>Go to course–job fit</button></div>
      </>
    );
  }

  const unlocked = course.outcomes.filter((l) => !l.locked);
  const covered = course.modules.every((m) => course.outcomes.some((o) => o.moduleIds.includes(m.id)));
  const selected = new Set(course.roles.filter((r) => r.selected).map((r) => r.id));
  const tied = course.outcomes.every((o) => o.roleIds.some((r) => selected.has(r)));
  const stale = staleSessionCount(course);

  return (
    <>
      <Head n={4} title="Outcomes" right={busy.draftOutcomes ? <Busy>Drafting outcomes…</Busy> : !frozen && <button className="btn" onClick={() => run({ type: "draftOutcomes" })}>{course.outcomes.length ? "Draft again (keeps locked)" : "Draft outcomes"}</button>}>
        Drafted from the confirmed course structure. Edit any text directly, or click <b>Suggest edit</b> on one outcome and say what should change. You see the rewrite next to the original before anything is replaced. Lock what you&apos;re happy with, then freeze the set.
      </Head>
      {!confirmed && <div className="info">The course structure was reopened. Confirm it again before you freeze the outcomes.</div>}
      {stale > 0 && <div className="sealbar" style={{ background: "var(--warn-soft)", color: "var(--warn)" }}><span>{stale} session{stale > 1 ? "s are" : " is"} out of date because outcomes changed after they were built.</span><button className="btn" onClick={() => go("build")}>Rebuild in Build</button></div>}
      {frozen ? (
        <div className="sealbar">
          <span>🔒 Outcomes frozen on {new Date(course.outcomesFrozenAt!).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" })}. Changing them later marks dependent plans out of date.</span>
          <button className="btn" onClick={() => save(unfreezeOutcomes)}>Unfreeze</button>
        </div>
      ) : (
        <div className="panel">
          <div className="row between"><h3>Suggest an edit to all {unlocked.length} unlocked outcomes</h3><button className="btn sm" onClick={() => setBulkOpen(!bulkOpen)}>{bulkOpen ? "Close" : "Open"}</button></div>
          {bulkOpen && (
            <>
              <div className="row" style={{ marginTop: 10, gap: 6 }}>
                {QUICK.slice(0, 4).map(([k, v]) => <button key={k} className="chip" disabled={busy.bulk || !unlocked.length} onClick={() => { void suggest(unlocked.map((l) => l.id), { kind: k, note: "" }, "bulk"); setBulkOpen(false); }}>{v}</button>)}
              </div>
              <div className="row" style={{ marginTop: 8 }}>
                <input className="txtin" aria-label="Instruction for all unlocked outcomes" placeholder="e.g. “Use the BMS capstone as the context in every outcome”" value={bulkText} onChange={(e) => setBulkText(e.target.value)} style={{ flex: 1, minWidth: 200 }} />
                <button className="btn sm primary" disabled={!bulkText.trim() || busy.bulk || !unlocked.length} onClick={() => { void suggest(unlocked.map((l) => l.id), { kind: "free", note: bulkText.trim() }, "bulk"); setBulkOpen(false); }}>Suggest for all</button>
              </div>
              <p className="muted small" style={{ margin: "8px 0 0" }}>Each outcome gets its own suggestion, which you accept or discard one by one.</p>
            </>
          )}
          {busy.bulk && <div style={{ marginTop: 8 }}><Busy>Writing suggestions…</Busy></div>}
        </div>
      )}
      <div className="panel"><h2>Course objectives</h2><div style={{ marginTop: 4 }}>{course.objectives.map((o) => item(o, "co"))}</div></div>
      <div className="panel">
        <div className="row between">
          <h2>Learning outcomes</h2>
          <span className="muted small">{covered ? "Every module covered" : "Some modules have no outcome"} · {tied ? "every outcome tied to a selected role" : "some outcomes are not tied to a selected role"}</span>
        </div>
        <div style={{ marginTop: 4 }}>{course.outcomes.map((o) => item(o, "lo"))}</div>
      </div>
      <div className="panel">
        <div className="row between">
          <h2>Module outcomes</h2>
          <span className="muted small">What each module must achieve · each serves one or more learning outcomes</span>
        </div>
        {course.modules.map((m) => (
          <div key={m.id} style={{ marginTop: 12 }}>
            <h3><span className="mono muted">{m.id}</span> {m.title}</h3>
            {m.outcomes.length ? m.outcomes.map((mo) => item(mo, "mo", m.id)) : <p className="muted small" style={{ margin: "4px 0 0" }}>No module outcomes yet. Draft the outcomes to add them.</p>}
          </div>
        ))}
      </div>
      <div className="row between">
        <button className="btn" onClick={() => go("fit")}>← Course–job fit</button>
        {frozen ? <button className="btn primary" onClick={() => go("plans")}>Design learning plans →</button> : (
          <button className="btn seal" disabled={!course.outcomes.length || !confirmed} onClick={() => { void save(freezeOutcomes); setProps({}); setSugOpen({}); }}>Freeze outcomes</button>
        )}
      </div>
    </>
  );
}
