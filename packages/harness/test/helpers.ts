import type { ChatClient, ChatRequest, ChatResult } from "../src/openrouter.js";
import { DEFAULT_CONFIG, type HarnessConfig } from "../src/config.js";

/** A chat client that answers from a script. Each entry is a reply string or a function of the request. */
export class ScriptedClient implements ChatClient {
  readonly requests: ChatRequest[] = [];
  constructor(private readonly script: (string | object | ((req: ChatRequest) => string | object))[], private readonly costPerCall = 0.001) {}

  async chat(req: ChatRequest): Promise<ChatResult> {
    this.requests.push(req);
    const next = this.script.shift();
    if (next === undefined) throw new Error(`ScriptedClient: no reply scripted for call ${this.requests.length}`);
    const v = typeof next === "function" ? next(req) : next;
    return { content: typeof v === "string" ? v : JSON.stringify(v), model: req.model, costUsd: this.costPerCall, promptTokens: 10, completionTokens: 10 };
  }
}

export const testConfig: HarnessConfig = {
  ...DEFAULT_CONFIG,
  models: Object.fromEntries(Object.keys(DEFAULT_CONFIG.models).map((k) => [k, { primary: `test/${k}`, fallback: `test/${k}-fallback` }])) as HarnessConfig["models"],
};

export const fixedNow = () => new Date("2026-11-04T12:00:00.000Z");

export function jsonResponse(body: unknown, status = 200): Response {
  return new Response(typeof body === "string" ? body : JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
}

/** A passing review for any rubric. */
export const goodReview = (ids: string[]) => ({ scores: ids.map((criterion) => ({ criterion, score: 5, comment: "" })), issues: [] });
export const badReview = (ids: string[]) => ({ scores: ids.map((criterion) => ({ criterion, score: 2, comment: "weak" })), issues: ["LO2 is vague; make it measurable"] });
