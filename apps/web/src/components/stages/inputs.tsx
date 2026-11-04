"use client";
import type { Course, Module } from "@cg/core";
import { useState } from "react";
import type { CourseMeta } from "@/lib/course-meta";
import { api } from "../api";
import { useCourse } from "../course-context";
import { FeedbackWidget } from "../feedback-widget";
import { Busy, CommitInput, Head } from "../ui";

type Kind = "handout" | "moduleSheet";
const OPTS: [NonNullable<CourseMeta["startMode"]>, string, string][] = [
  ["handout", "From a course handout", ".docx, .pdf or .txt"],
  ["moduleSheet", "From a module sheet", ".xlsx list of modules"],
  ["both", "Both", "Merge them and flag differences"],
];

const foundChip = (m: Module) =>
  ({ both: <span className="chip ok">Both</span>, moduleSheet: <span className="chip ink">Sheet</span>, handout: <span className="chip ink">Handout</span>, fit: <span className="chip ok">From job fit</span>, user: <span className="chip">Yours</span>, import: <span className="chip">Imported</span> })[m.foundIn];

function Drop({ kind, course, summary, chip }: { kind: Kind; course: Course; summary?: string; chip?: React.ReactNode }) {
  const { setError } = useCourse();
  const [over, setOver] = useState(false);
  const [busy, setBusy] = useState(false);
  const file = course.sources.find((s) => s.kind === kind);
  const accept = kind === "handout" ? ".docx,.pdf,.txt" : ".xlsx";
  const upload = async (f: File | undefined) => {
    if (!f) return;
    setBusy(true);
    try {
      const fd = new FormData();
      fd.set("kind", kind);
      fd.set("file", f);
      await api(`/api/courses/${course.id}/uploads`, { method: "POST", body: fd });
      window.location.reload(); // simplest way to pick up the new source in all stages
    } catch (e) {
      setError(e instanceof Error ? e.message : "Upload failed");
    } finally {
      setBusy(false);
    }
  };
  const ext = file?.filename.split(".").pop()?.toUpperCase();
  return (
    <div
      className={`drop ${file ? "loaded" : ""} ${over ? "over" : ""}`}
      onDragOver={(e) => { e.preventDefault(); setOver(true); }}
      onDragLeave={() => setOver(false)}
      onDrop={(e) => { e.preventDefault(); setOver(false); void upload(e.dataTransfer.files[0]); }}
    >
      <span className="eyebrow">{kind === "handout" ? "Course handout" : "Module sheet"}</span>
      {file ? (
        <div className="file">
          <span className="ext">{ext}</span>
          <div><b>{file.filename}</b><br /><span className="muted">{summary ?? "Uploaded · not read yet"}</span></div>
        </div>
      ) : (
        <span className="muted small">Drop a file here or choose one ({accept.replaceAll(",", ", ")}).</span>
      )}
      {chip}
      <div className="row">
        <input type="file" accept={accept} aria-label={kind === "handout" ? "Upload handout" : "Upload module sheet"} onChange={(e) => upload(e.target.files?.[0])} disabled={busy} />
        {busy && <Busy>Uploading…</Busy>}
      </div>
    </div>
  );
}

export function InputsStage() {
  const { course, meta, save, run, busy, go } = useCourse();
  const start = meta.startMode ?? "both";
  const showH = start !== "moduleSheet", showX = start !== "handout";
  const b = course.brief;
  const read = !!meta.provenance?.inputs;
  const setBrief = (patch: Partial<Course["brief"]>) => save((c) => ({ ...c, brief: { ...c.brief, ...patch } }));
  const fromHandout = course.modules.filter((m) => m.foundIn === "handout" || m.foundIn === "both").length;
  const fromSheet = course.modules.filter((m) => m.foundIn === "moduleSheet" || m.foundIn === "both").length;
  const toRoles = () => {
    go("roles");
    if (!course.roles.length) void run({ type: "findRoles" });
  };

  return (
    <>
      <Head n={1} title="Inputs">Start from what you have. The app reads the files and builds one module list, flagging anything the two sources disagree on.</Head>
      <div className="startopts">
        {OPTS.map(([k, t, s]) => (
          <button key={k} className="opt" aria-pressed={start === k} onClick={() => save((c, m) => [c, { ...m, startMode: k }])}>
            <b>{t}</b><span>{s}</span>
          </button>
        ))}
      </div>
      <div className="grid2">
        {showH && (
          <Drop kind="handout" course={course}
            summary={read ? `${course.objectives.length} COs · ${course.outcomes.length} LOs · ${fromHandout} modules · ${b.textbooks.length} textbooks found` : undefined}
            chip={read && meta.inputGaps?.length ? meta.inputGaps.map((g) => <span key={g} className="chip warn">{g}</span>) : null} />
        )}
        {showX && (
          <Drop kind="moduleSheet" course={course}
            summary={read ? `${fromSheet} modules read` : undefined}
            chip={read && fromSheet ? <span className="chip ok">Columns mapped automatically</span> : null} />
        )}
      </div>
      <div className="row" style={{ justifyContent: "flex-end" }}>
        {busy.parseInputs ? <Busy>Reading the files…</Busy> : (
          <button className={`btn ${read ? "" : "primary"}`} disabled={!course.sources.length} onClick={() => run({ type: "parseInputs" })}>
            {read ? "Read the files again" : "Read the files"}
          </button>
        )}
      </div>

      <div className="panel">
        <div className="row between"><h2>Course brief</h2><span className="muted small">{read ? "Filled from the handout; edit anything" : "Filled from the files once they are read; edit anything"}</span></div>
        <div className="grid3" style={{ marginTop: 12 }}>
          <div className="field"><label htmlFor="f-title">Course title</label><CommitInput id="f-title" value={b.title} onCommit={(v) => v.trim() && setBrief({ title: v.trim() })} /></div>
          <div className="field"><label htmlFor="f-code">Course code</label><CommitInput id="f-code" value={b.code ?? ""} onCommit={(v) => setBrief({ code: v.trim() || undefined })} /></div>
          <div className="field"><label htmlFor="f-aud">Audience</label><CommitInput id="f-aud" value={b.audience} onCommit={(v) => setBrief({ audience: v })} /></div>
          <div className="field"><label htmlFor="f-hrs">Contact hours</label><CommitInput id="f-hrs" inputMode="decimal" value={String(b.contactHours)} onCommit={(v) => Number(v) > 0 && setBrief({ contactHours: Number(v) })} /></div>
          <div className="field"><label htmlFor="f-ind">Target industry</label><CommitInput id="f-ind" value={b.industry} onCommit={(v) => setBrief({ industry: v })} /></div>
          <div className="field"><label htmlFor="f-reg">Job market to search</label><CommitInput id="f-reg" value={b.markets.join(", ")} onCommit={(v) => { const m = v.split(",").map((s) => s.trim()).filter(Boolean); if (m.length) setBrief({ markets: m }); }} /></div>
        </div>
      </div>

      <div className="panel tbl">
        <div className="row between" style={{ marginBottom: 8 }}>
          <h2>Merged modules</h2>
          {course.modules.length > 0 && <FeedbackWidget courseId={course.id} targetPath="modules" provenance={meta.provenance?.inputs} label="module list" />}
        </div>
        {course.modules.length ? (
          <table>
            <thead><tr><th>#</th><th>Module</th><th>Hours</th><th>Found in</th></tr></thead>
            <tbody>
              {course.modules.map((m) => (
                <tr key={m.id}><td className="mono">{m.id}</td><td>{m.title}</td><td className="mono">{m.hours}</td><td>{foundChip(m)} {m.note && <span className="chip warn">{m.note}</span>}</td></tr>
              ))}
            </tbody>
          </table>
        ) : <p className="muted" style={{ margin: 0 }}>Upload a handout and/or a module sheet, then read the files.</p>}
      </div>
      <div className="row" style={{ justifyContent: "flex-end" }}>
        <button className="btn primary" disabled={!course.modules.length} onClick={toRoles}>Find job roles →</button>
      </div>
    </>
  );
}
