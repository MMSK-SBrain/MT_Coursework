import { redirect } from "next/navigation";
import { currentUser } from "@/lib/session";

export const dynamic = "force-dynamic";

export default async function Home() {
  const u = await currentUser();
  redirect(!u ? "/signin" : !u.profile ? "/onboarding" : "/courses");
}
