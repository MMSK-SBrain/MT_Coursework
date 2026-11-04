"use client";
// Per-item feedback: thumbs, a category and free text, stored with the item's provenance (model, prompt id and version).
import type { Feedback, Provenance } from "@cg/core";
import { useState } from "react";
import { api } from "./api";

const CATEGORIES: [NonNullable<Feedback["category"]>, string][] = [
  ["inaccurate", "Inaccurate"],
  ["lowQuality", "Low quality"],
  ["notRelevant", "Not industry-relevant"],
  ["wrongLevel", "Wrong level"],
  ["missing", "Missing something"],
  ["other", "Other"],
];

const Thumb = ({ down }: { down?: boolean }) => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" style={down ? { transform: "rotate(180deg)" } : undefined}>
    <path d="M7 10v11H4V10h3zm0 0l4-8a2 2 0 0 1 2 2v4h6a2 2 0 0 1 2 2.3l-1.4 8A2 2 0 0 1 17.6 21H7" />
  </svg>
);

export function FeedbackWidget({ courseId, targetPath, provenance, label = "this" }: { courseId?: string; targetPath: string; provenance?: Provenance; label?: string }) {
  const [rating, setRating] = useState<"up" | "down" | null>(null);
  const [category, setCategory] = useState<string>("");
  const [text, setText] = useState("");
  const [state, setState] = useState<"idle" | "open" | "sending" | "sent">("idle");

  const send = async (r: "up" | "down" | null = rating) => {
    setState("sending");
    try {
      await api("/api/feedback", {
        method: "POST",
        json: {
          scope: "item", courseId, targetPath, rating: r ?? undefined, category: category || undefined, text,
          model: provenance?.model, promptId: provenance?.promptId, promptVersion: provenance?.promptVersion, pageUrl: window.location.pathname,
        },
      });
      setState("sent");
    } catch {
      setState("open");
    }
  };

  if (state === "sent") return <span className="fb">Thanks, noted.</span>;
  return (
    <span className="fb" data-feedback={targetPath}>
      <button className="th" aria-label={`Good: ${label}`} aria-pressed={rating === "up"} onClick={() => { setRating("up"); setState("open"); }}><Thumb /></button>
      <button className="th" aria-label={`Needs work: ${label}`} aria-pressed={rating === "down"} onClick={() => { setRating("down"); setState("open"); }}><Thumb down /></button>
      {state !== "idle" && (
        <>
          <select aria-label="What is wrong" value={category} onChange={(e) => setCategory(e.target.value)}>
            <option value="">{rating === "up" ? "Category (optional)" : "What is wrong?"}</option>
            {CATEGORIES.map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select>
          <input aria-label="Feedback text" placeholder="Anything to add?" value={text} onChange={(e) => setText(e.target.value)} onKeyDown={(e) => e.key === "Enter" && send()} />
          <button className="btn sm" onClick={() => send()} disabled={state === "sending"}>Send</button>
          <button className="btn sm" onClick={() => { setState("idle"); setRating(null); }}>Cancel</button>
        </>
      )}
    </span>
  );
}
