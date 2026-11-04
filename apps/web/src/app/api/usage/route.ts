import { FREE_TIER } from "@cg/core";
import { NextResponse } from "next/server";
import { route } from "@/lib/http";
import { credits, monthUsage } from "@/lib/repo";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";

export const GET = route(async () => {
  const u = await requireTeacherApi();
  return NextResponse.json({ usage: await monthUsage(u.id), credits: await credits(u.id), limits: FREE_TIER });
});
