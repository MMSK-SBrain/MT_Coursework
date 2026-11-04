"use client";
import { useEffect, useRef, useState, type ReactNode } from "react";
import { isHttpUrl } from "@cg/core";

/** Defense in depth: the schema already rejects non-http(s) URLs. */
export const safeHref = (u: string) => (isHttpUrl(u) ? u : "#");

export function Head({ n, title, children, right }: { n: number | string; title: string; children?: ReactNode; right?: ReactNode }) {
  return (
    <div className="head">
      <div>
        <span className="eyebrow">{typeof n === "number" ? `Stage ${n}` : n}</span>
        <h1>{title}</h1>
        {children && <p>{children}</p>}
      </div>
      {right}
    </div>
  );
}

export const Busy = ({ children }: { children: ReactNode }) => <span className="busy" role="status">{children}</span>;

/** A text input that edits locally and commits on blur or Enter, so saves never steal focus. */
export function CommitInput({ value, onCommit, ...rest }: { value: string; onCommit: (v: string) => void } & Omit<React.InputHTMLAttributes<HTMLInputElement>, "value" | "onChange">) {
  const [v, setV] = useState(value);
  const focused = useRef(false);
  useEffect(() => {
    if (!focused.current) setV(value);
  }, [value]);
  const commit = () => {
    focused.current = false;
    if (v !== value) onCommit(v);
  };
  return (
    <input
      {...rest}
      value={v}
      onChange={(e) => setV(e.target.value)}
      onFocus={() => (focused.current = true)}
      onBlur={commit}
      onKeyDown={(e) => e.key === "Enter" && (e.target as HTMLInputElement).blur()}
    />
  );
}

/** Inline-editable text (contenteditable), committed on blur. */
export function EditableText({ value, editable, onCommit, label }: { value: string; editable: boolean; onCommit: (v: string) => void; label: string }) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (ref.current && document.activeElement !== ref.current) ref.current.textContent = value;
  }, [value]);
  return (
    <div
      ref={ref}
      className="txt"
      role="textbox"
      aria-label={label}
      contentEditable={editable}
      suppressContentEditableWarning
      spellCheck
      onBlur={(e) => {
        const t = (e.currentTarget.textContent ?? "").trim();
        if (t && t !== value) onCommit(t);
        else e.currentTarget.textContent = value;
      }}
      onKeyDown={(e) => {
        if (e.key === "Enter") {
          e.preventDefault();
          (e.target as HTMLElement).blur();
        }
      }}
    />
  );
}

export const pad2 = (n: number) => String(n).padStart(2, "0");
