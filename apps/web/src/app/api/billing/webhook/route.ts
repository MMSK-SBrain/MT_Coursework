import { eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { db, schema } from "@/lib/db";
import { route } from "@/lib/http";
import { getPaymentProvider } from "@/lib/payments";

export const dynamic = "force-dynamic";

/** Payment provider callback (verification is the provider implementation's job). */
export const POST = route(async (req: Request) => {
  const ev = await getPaymentProvider().parseWebhook(req);
  if (ev) await db().update(schema.purchases).set({ status: ev.status, providerRef: ev.providerRef }).where(eq(schema.purchases.id, ev.purchaseId));
  return NextResponse.json({ ok: true });
});
