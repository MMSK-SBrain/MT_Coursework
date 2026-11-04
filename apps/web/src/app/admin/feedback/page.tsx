import { desc } from "drizzle-orm";
import { notFound } from "next/navigation";
import { TopBar } from "@/components/top-bar";
import { db, schema } from "@/lib/db";
import { currentUser } from "@/lib/session";
import { feedbackStage, groupFeedback } from "@/lib/feedback-groups";

export const dynamic = "force-dynamic";

/** Admin only (teacher_users.role = "admin" or listed in ADMIN_EMAILS). Others get a 404. */
export default async function AdminFeedback() {
  const u = await currentUser();
  if (!u?.isAdmin) notFound();
  const rows = await db().select().from(schema.feedback).orderBy(desc(schema.feedback.createdAt)).limit(1000);
  const groups = groupFeedback(rows);
  return (
    <>
      <TopBar crumb="Admin · Feedback" email={u.email} isAdmin />
      <div className="shell page">
        <main>
          <div className="wrap">
            <div className="head"><div><span className="eyebrow">Admin</span><h1>Feedback by stage and model</h1><p>{rows.length} items, newest first. Thumbs-down items are candidates for the test set.</p></div></div>
            {groups.map((g) => (
              <div key={g.stage} className="panel">
                <h2>{g.stage}</h2>
                {g.models.map((m) => (
                  <div key={m.model} className="group">
                    <div className="row between">
                      <h3>{m.model}</h3>
                      <span className="row"><span className="chip ok">{m.up} up</span><span className="chip bad">{m.down} down</span><span className="chip">{m.items.length} total</span></span>
                    </div>
                    <div className="tbl">
                      <table>
                        <thead><tr><th>When</th><th>Rating</th><th>Category</th><th>Item</th><th>Prompt</th><th>Text</th></tr></thead>
                        <tbody>
                          {m.items.map((f) => (
                            <tr key={f.id}>
                              <td className="mono">{f.createdAt.toISOString().slice(0, 16).replace("T", " ")}</td>
                              <td>{f.rating ? <span className={`chip ${f.rating === "up" ? "ok" : "bad"}`}>{f.rating}</span> : "-"}</td>
                              <td>{f.category ?? "-"}</td>
                              <td className="mono">{f.targetPath ?? f.pageUrl ?? "-"}</td>
                              <td className="mono">{f.promptId ? `${f.promptId} v${f.promptVersion}` : "-"}</td>
                              <td>{f.text || <span className="muted">-</span>}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                ))}
              </div>
            ))}
            {!rows.length && <div className="panel muted">No feedback yet.</div>}
            <p className="muted small">Stage is taken from the prompt id ({feedbackStage({ promptId: "outcomes.draft", scope: "item" })} for outcomes.draft); site-wide feedback is grouped under “site”.</p>
          </div>
        </main>
      </div>
    </>
  );
}
