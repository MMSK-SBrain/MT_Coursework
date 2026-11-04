import { redirect } from "next/navigation";
import { TopBar } from "@/components/top-bar";
import { currentUser } from "@/lib/session";
import { ProfileForm } from "./profile-form";

export const dynamic = "force-dynamic";

export default async function Onboarding() {
  const u = await currentUser();
  if (!u) redirect("/signin");
  return (
    <>
      <TopBar email={u.email} />
      <div className="center">
        <div className="card">
          <span className="eyebrow">One step left</span>
          <h1>Tell us about your teaching</h1>
          <p className="muted" style={{ margin: 0 }}>The free tier unlocks as soon as you save this: one course a month, designed end to end.</p>
          <ProfileForm initial={u.profile ?? undefined} />
        </div>
      </div>
    </>
  );
}
