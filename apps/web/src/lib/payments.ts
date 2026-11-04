// Payments sit behind this interface. The provider is still an open decision (Razorpay is likely for India).
import type { PaidFeature } from "./quota";

export interface CheckoutInput {
  purchaseId: string;
  userId: string;
  email: string;
  feature: PaidFeature;
  quantity: number;
  returnUrl: string;
}

export type CheckoutResult =
  /** Send the teacher to the provider's hosted checkout; the webhook marks the purchase paid. */
  | { kind: "redirect"; url: string; providerRef?: string }
  /** Paid immediately (dev provider). */
  | { kind: "paid"; providerRef?: string };

export interface PaymentProvider {
  readonly id: string;
  createCheckout(input: CheckoutInput): Promise<CheckoutResult>;
  /** Verify and parse a provider webhook. Returns null for events the app ignores. */
  parseWebhook(req: Request): Promise<{ purchaseId: string; status: "paid" | "failed"; providerRef?: string } | null>;
}

/** No-op provider for development: every checkout succeeds at once, nothing is charged. */
export const devPaymentProvider: PaymentProvider = {
  id: "dev",
  async createCheckout(i) {
    return { kind: "paid", providerRef: `dev-${i.purchaseId}` };
  },
  async parseWebhook() {
    return null;
  },
};

/** Used in production until a real provider is configured: paid features stay locked. */
export const disabledPaymentProvider: PaymentProvider = {
  id: "disabled",
  async createCheckout() {
    throw new Error("Payments are not available yet.");
  },
  async parseWebhook() {
    return null;
  },
};

export function getPaymentProvider(env: Record<string, string | undefined> = process.env): PaymentProvider {
  const chosen = env.PAYMENT_PROVIDER ?? (env.NODE_ENV === "production" ? "disabled" : "dev");
  switch (chosen) {
    case "dev":
      return devPaymentProvider;
    // case "razorpay": return razorpayProvider(env.RAZORPAY_KEY_ID, env.RAZORPAY_KEY_SECRET);  // open decision
    default:
      return disabledPaymentProvider;
  }
}
