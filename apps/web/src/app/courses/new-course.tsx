"use client";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { api, ApiError } from "@/components/api";
import { usePaywall } from "@/components/paywall";
import type { PaidFeature } from "@/lib/quota";

export function NewCourse() {
  const router = useRouter();
  const ask = usePaywall();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const start = async () => {
    setBusy(true);
    setError(null);
    try {
      for (;;) {
        try {
          const { id } = await api<{ id: string }>("/api/courses", { method: "POST", json: {} });
          router.push(`/courses/${id}?stage=inputs`);
          return;
        } catch (e) {
          const pw = e instanceof ApiError ? (e.body.paywall as { feature: PaidFeature; reason: string } | undefined) : undefined;
          if (pw && (await ask(pw.feature, pw.reason))) continue;
          if (!pw) throw e;
          return;
        }
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Could not start a course");
    } finally {
      setBusy(false);
    }
  };
  return (
    <div className="row">
      {error && <span className="chip bad">{error}</span>}
      <button className="btn primary" onClick={start} disabled={busy}>New course</button>
    </div>
  );
}
