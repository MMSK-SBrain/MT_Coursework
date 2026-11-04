"use client";
// Site-wide feedback button, on every page (rendered by the root layout).
import { useState } from "react";
import { api } from "./api";

export function SiteFeedback() {
  const [open, setOpen] = useState(false);
  const [category, setCategory] = useState("bug");
  const [text, setText] = useState("");
  const [msg, setMsg] = useState<string | null>(null);

  const send = async () => {
    try {
      await api("/api/feedback", { method: "POST", json: { scope: "site", category, text, pageUrl: window.location.pathname } });
      setMsg("Thanks. We read every message.");
      setText("");
      setTimeout(() => { setOpen(false); setMsg(null); }, 1500);
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Could not send");
    }
  };

  return (
    <div className="sitefb">
      {open && (
        <div className="pop" role="dialog" aria-label="Send feedback">
          <h3>Feedback</h3>
          <select aria-label="Feedback type" value={category} onChange={(e) => setCategory(e.target.value)}>
            <option value="bug">Something is broken</option>
            <option value="feature">An idea or a request</option>
            <option value="other">Something else</option>
          </select>
          <textarea rows={4} aria-label="Your feedback" placeholder="What happened, or what would help?" value={text} onChange={(e) => setText(e.target.value)} />
          {msg && <span className="small muted">{msg}</span>}
          <div className="row" style={{ justifyContent: "flex-end" }}>
            <button className="btn sm" onClick={() => setOpen(false)}>Close</button>
            <button className="btn sm primary" onClick={send} disabled={!text.trim()}>Send</button>
          </div>
        </div>
      )}
      <button className="btn" onClick={() => setOpen(!open)} aria-expanded={open}>Feedback</button>
    </div>
  );
}
