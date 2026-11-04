"use client";
import { signOut } from "next-auth/react";
import Link from "next/link";
import { useEffect, useState, type ReactNode } from "react";

function ThemeToggle() {
  const [t, setT] = useState<"auto" | "light" | "dark">("auto");
  useEffect(() => {
    const d = document.documentElement.dataset.theme;
    setT(d === "light" || d === "dark" ? d : "auto");
  }, []);
  const next = () => {
    const n = t === "auto" ? "light" : t === "light" ? "dark" : "auto";
    setT(n);
    if (n === "auto") delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = n;
    try { localStorage.setItem("cg-theme", n); } catch { /* private mode */ }
  };
  return <button className="iconbtn" onClick={next} title="Theme: auto, light or dark">Theme: {t}</button>;
}

export function TopBar({ crumb, email, isAdmin, usage, mock }: { crumb?: ReactNode; email?: string; isAdmin?: boolean; usage?: ReactNode; mock?: boolean }) {
  return (
    <header className="top">
      <Link className="brand" href="/courses">COURSE GENERATOR</Link>
      <nav className="crumb" aria-label="Breadcrumb">
        <Link href="/courses">Courses</Link>
        {crumb && <><span>/</span><b>{crumb}</b></>}
      </nav>
      <span className="spacer" />
      {mock && <span className="ex" title="Generation uses the local mock until @cg/harness is connected">Mock AI · example data</span>}
      {usage}
      {isAdmin && <Link className="iconbtn" href="/admin/feedback">Admin</Link>}
      <ThemeToggle />
      {email && (
        <>
          <span className="muted small">{email}</span>
          <button className="iconbtn" onClick={() => signOut({ callbackUrl: "/signin" })}>Sign out</button>
        </>
      )}
    </header>
  );
}
