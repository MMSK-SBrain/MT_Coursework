"use client";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { api } from "@/components/api";

const ROLES = ["Lecturer / Assistant professor", "Professor / HoD", "Corporate trainer", "Vocational instructor", "Course designer", "Other"];

export function ProfileForm({ initial }: { initial?: { institution: string; subject: string; role: string } }) {
  const router = useRouter();
  const [f, setF] = useState(initial ?? { institution: "", subject: "", role: ROLES[0]! });
  const [error, setError] = useState<string | null>(null);
  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api("/api/profile", { method: "POST", json: f });
      router.push("/courses");
      router.refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not save");
    }
  };
  return (
    <form onSubmit={submit} style={{ display: "flex", flexDirection: "column", gap: 12 }}>
      <div className="field"><label htmlFor="inst">Institution</label><input id="inst" required minLength={2} placeholder="e.g. BITS Pilani WILP" value={f.institution} onChange={(e) => setF({ ...f, institution: e.target.value })} /></div>
      <div className="field"><label htmlFor="subj">Subject you teach</label><input id="subj" required minLength={2} placeholder="e.g. Automotive systems engineering" value={f.subject} onChange={(e) => setF({ ...f, subject: e.target.value })} /></div>
      <div className="field"><label htmlFor="role">Your role</label>
        <select id="role" value={f.role} onChange={(e) => setF({ ...f, role: e.target.value })}>{ROLES.map((r) => <option key={r}>{r}</option>)}</select>
      </div>
      {error && <div className="err">{error}</div>}
      <button className="btn primary">Save and start</button>
    </form>
  );
}
