"use client";
import { signIn } from "next-auth/react";
import { useState } from "react";

export function SignInForm({ google, dev, error }: { google: boolean; dev: boolean; error?: string }) {
  const [email, setEmail] = useState("");
  const [devEmail, setDevEmail] = useState("teacher@example.com");
  const [busy, setBusy] = useState(false);
  return (
    <>
      {error && <div className="err">Sign-in failed ({error}). Try again.</div>}
      {google && <button className="btn" onClick={() => signIn("google", { callbackUrl: "/" })}>Continue with Google</button>}
      <form className="field" onSubmit={(e) => { e.preventDefault(); setBusy(true); void signIn("email", { email, callbackUrl: "/" }); }}>
        <label htmlFor="email">Email</label>
        <input id="email" type="email" required placeholder="you@institution.edu" value={email} onChange={(e) => setEmail(e.target.value)} />
        <button className="btn primary" style={{ marginTop: 8 }} disabled={busy}>Email me a sign-in link</button>
      </form>
      {dev && (
        <>
          <div className="divider">development only</div>
          <form className="field" onSubmit={(e) => { e.preventDefault(); void signIn("dev", { email: devEmail, callbackUrl: "/" }); }}>
            <label htmlFor="dev-email">Dev sign-in (no email or OAuth needed)</label>
            <input id="dev-email" type="email" required value={devEmail} onChange={(e) => setDevEmail(e.target.value)} />
            <button className="btn" style={{ marginTop: 8 }}>Sign in as this teacher</button>
          </form>
        </>
      )}
    </>
  );
}
