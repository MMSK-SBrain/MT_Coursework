"use client";
// Paywall dialog for FREE_TIER.paidFeatures. `ask()` resolves true once the teacher has paid (the dev provider pays at once).
import { FREE_TIER } from "@cg/core";
import { createContext, useCallback, useContext, useRef, useState, type ReactNode } from "react";
import { FEATURE_LABEL, type PaidFeature } from "@/lib/quota";
import { api } from "./api";

type Ask = (feature: PaidFeature, reason: string) => Promise<boolean>;
const Ctx = createContext<Ask>(async () => false);
export const usePaywall = () => useContext(Ctx);

export function PaywallProvider({ children }: { children: ReactNode }) {
  const [open, setOpen] = useState<{ feature: PaidFeature; reason: string } | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const resolver = useRef<(ok: boolean) => void>(undefined);

  const ask = useCallback<Ask>((feature, reason) => {
    setError(null);
    setOpen({ feature, reason });
    return new Promise<boolean>((res) => (resolver.current = res));
  }, []);

  const close = (ok: boolean) => {
    resolver.current?.(ok);
    setOpen(null);
  };

  const buy = async () => {
    if (!open) return;
    setBusy(true);
    setError(null);
    try {
      const r = await api<{ status: string; url?: string }>("/api/billing/checkout", {
        method: "POST", json: { feature: open.feature, returnUrl: window.location.pathname + window.location.search },
      });
      if (r.status === "redirect" && r.url) window.location.href = r.url;
      else close(true);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Payment failed");
    } finally {
      setBusy(false);
    }
  };

  return (
    <Ctx.Provider value={ask}>
      {children}
      {open && (
        <div className="modal" role="dialog" aria-modal="true" aria-labelledby="pw-title" onClick={(e) => e.target === e.currentTarget && close(false)}>
          <div className="card">
            <span className="eyebrow">Paid feature</span>
            <h2 id="pw-title">{FEATURE_LABEL[open.feature]}</h2>
            <p className="muted" style={{ margin: 0 }}>{open.reason}</p>
            <p className="small muted" style={{ margin: 0 }}>
              Free every month: {FREE_TIER.coursesPerMonth} course designed end to end, exported as .md, and{" "}
              {Math.round(FREE_TIER.videoSecondsPerMonth / 60)} minutes of video. Case studies, slides, the instructor guide, extra video
              and extra courses are paid per item.
            </p>
            {error && <div className="err">{error}</div>}
            <div className="row" style={{ justifyContent: "flex-end" }}>
              <button className="btn" onClick={() => close(false)}>Not now</button>
              <button className="btn seal" onClick={buy} disabled={busy}>{busy ? "Opening checkout…" : "Unlock"}</button>
            </div>
          </div>
        </div>
      )}
    </Ctx.Provider>
  );
}
