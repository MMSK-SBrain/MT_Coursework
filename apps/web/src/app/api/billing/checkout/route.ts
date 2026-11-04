import { eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { z } from "zod";
import { db, schema } from "@/lib/db";
import { HttpError, route } from "@/lib/http";
import { getPaymentProvider } from "@/lib/payments";
import { PAID_FEATURES, type PaidFeature } from "@/lib/quota";
import { requireTeacherApi } from "@/lib/session";

export const dynamic = "force-dynamic";

const Body = z.object({ feature: z.enum(PAID_FEATURES as [PaidFeature, ...PaidFeature[]]), quantity: z.number().int().min(1).max(20).default(1), returnUrl: z.string().default("/courses") });

/** Start a checkout for a paid feature. The dev provider marks it paid at once. */
export const POST = route(async (req: Request) => {
  const u = await requireTeacherApi();
  const b = Body.parse(await req.json());
  const provider = getPaymentProvider();
  const [p] = await db().insert(schema.purchases).values({ userId: u.id, feature: b.feature, quantity: b.quantity, provider: provider.id }).returning();
  try {
    const r = await provider.createCheckout({ purchaseId: p!.id, userId: u.id, email: u.email, feature: b.feature, quantity: b.quantity, returnUrl: b.returnUrl });
    if (r.kind === "paid") {
      await db().update(schema.purchases).set({ status: "paid", providerRef: r.providerRef }).where(eq(schema.purchases.id, p!.id));
      return NextResponse.json({ status: "paid" });
    }
    await db().update(schema.purchases).set({ providerRef: r.providerRef }).where(eq(schema.purchases.id, p!.id));
    return NextResponse.json({ status: "redirect", url: r.url });
  } catch (e) {
    await db().update(schema.purchases).set({ status: "failed" }).where(eq(schema.purchases.id, p!.id));
    throw new HttpError(503, e instanceof Error ? e.message : "Payment failed");
  }
});
