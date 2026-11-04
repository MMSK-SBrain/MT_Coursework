import { redirect } from "next/navigation";
import { TopBar } from "@/components/top-bar";
import { isDevSignInEnabled } from "@/lib/auth";
import { currentUser } from "@/lib/session";
import { SignInForm } from "./sign-in-form";

export const dynamic = "force-dynamic";

export default async function SignInPage({ searchParams }: { searchParams: Promise<{ sent?: string; error?: string }> }) {
  if (await currentUser()) redirect("/");
  const { sent, error } = await searchParams;
  return (
    <>
      <TopBar />
      <div className="center">
        <div className="card">
          <span className="eyebrow">For teachers · free</span>
          <h1>Sign in to Course Generator</h1>
          <p className="muted" style={{ margin: 0 }}>Design courses that are relevant to industry and still meet academic requirements: from a handout or module list to hour-wise lesson plans.</p>
          {sent ? (
            <div className="info">Check your email for a sign-in link.</div>
          ) : (
            <SignInForm google={!!(process.env.GOOGLE_CLIENT_ID && process.env.GOOGLE_CLIENT_SECRET)} dev={isDevSignInEnabled()} error={error} />
          )}
          <p className="muted small" style={{ margin: 0 }}>Teacher accounts are separate from Reynlab learner accounts.</p>
        </div>
      </div>
    </>
  );
}
