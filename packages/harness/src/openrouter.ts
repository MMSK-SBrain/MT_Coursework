// Minimal OpenRouter client: OpenAI-compatible chat completions over plain fetch, no SDK.
import type { ModelPair } from "./config.js";

export const OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1";

export type FetchLike = (input: string, init?: RequestInit) => Promise<Response>;

export interface ChatMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface ChatRequest {
  model: string;
  messages: ChatMessage[];
  temperature?: number;
  maxTokens?: number;
  json?: boolean;
}

export interface ChatResult {
  content: string;
  /** The model that actually answered (OpenRouter echoes it back). */
  model: string;
  costUsd: number;
  promptTokens: number;
  completionTokens: number;
}

export class OpenRouterError extends Error {
  /** Spend already incurred by the failed call (e.g. a reply cut off by the token limit). */
  costUsd = 0;
  constructor(message: string, readonly status?: number, readonly model?: string) {
    super(message);
    this.name = "OpenRouterError";
  }
}

export class MissingApiKeyError extends Error {
  constructor() {
    super("OPENROUTER_API_KEY is not set. Set it, or use MockStages for dev and tests.");
    this.name = "MissingApiKeyError";
  }
}

export interface OpenRouterOptions {
  apiKey?: string;
  /** Thinking-token budget for reasoning models (ignored by others). Default 2048, never more than half of max_tokens. */
  reasoningMaxTokens?: number;
  baseUrl?: string;
  fetch?: FetchLike;
  timeoutMs?: number;
  /** Sent as HTTP-Referer / X-Title so usage shows up under the app on openrouter.ai. */
  appUrl?: string;
  appTitle?: string;
}

/** Anything that can answer a chat request. The runner depends on this, so tests can swap it. */
export interface ChatClient {
  chat(req: ChatRequest): Promise<ChatResult>;
}

export class OpenRouterClient implements ChatClient {
  private readonly reasoningMaxTokens: number;
  private readonly apiKey: string;
  private readonly baseUrl: string;
  private readonly fetchFn: FetchLike;
  private readonly timeoutMs: number;
  private readonly appUrl: string;
  private readonly appTitle: string;

  constructor(opts: OpenRouterOptions = {}) {
    const key = opts.apiKey ?? (typeof process !== "undefined" ? process.env.OPENROUTER_API_KEY : undefined);
    if (!key) throw new MissingApiKeyError();
    this.apiKey = key;
    this.baseUrl = (opts.baseUrl ?? OPENROUTER_BASE_URL).replace(/\/$/, "");
    this.fetchFn = opts.fetch ?? ((i, init) => fetch(i, init));
    this.timeoutMs = opts.timeoutMs ?? 120_000;
    this.appUrl = opts.appUrl ?? "https://reynlab.com/course-generator";
    this.appTitle = opts.appTitle ?? "Reynlab Course Generator";
    this.reasoningMaxTokens = opts.reasoningMaxTokens ?? 2048;
  }

  async chat(req: ChatRequest): Promise<ChatResult> {
    const maxTokens = req.maxTokens ?? 8192;
    const body: Record<string, unknown> = {
      model: req.model,
      messages: req.messages,
      temperature: req.temperature ?? 0.3,
      max_tokens: maxTokens,
      usage: { include: true }, // makes OpenRouter return usage.cost in USD
      // Thinking models can spend the whole token budget on reasoning and return no answer.
      // A fixed thinking budget (at most half of max_tokens) always leaves room for the answer.
      reasoning: { max_tokens: Math.min(this.reasoningMaxTokens, Math.floor(maxTokens / 2)) },
    };
    if (req.json) body.response_format = { type: "json_object" };

    let res: Response;
    try {
      res = await this.fetchFn(`${this.baseUrl}/chat/completions`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${this.apiKey}`,
          "Content-Type": "application/json",
          "HTTP-Referer": this.appUrl,
          "X-Title": this.appTitle,
        },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(this.timeoutMs),
      });
    } catch (e) {
      throw new OpenRouterError(`request failed: ${(e as Error).message}`, undefined, req.model);
    }
    const text = await res.text();
    if (!res.ok) throw new OpenRouterError(`HTTP ${res.status}: ${text.slice(0, 300)}`, res.status, req.model);

    let data: any;
    try {
      data = JSON.parse(text);
    } catch {
      throw new OpenRouterError(`non-JSON response: ${text.slice(0, 200)}`, res.status, req.model);
    }
    if (data.error) throw new OpenRouterError(`API error: ${JSON.stringify(data.error).slice(0, 300)}`, data.error.code, req.model);
    const content = data.choices?.[0]?.message?.content;
    if (typeof content !== "string" || !content.trim()) {
      const finish = data.choices?.[0]?.finish_reason ?? "unknown";
      const e = new OpenRouterError(`response has no message content (finish_reason ${finish}, ${data.usage?.completion_tokens ?? "?"} completion tokens)`, res.status, req.model);
      e.costUsd = Number(data.usage?.cost ?? 0) || 0;
      throw e;
    }
    return {
      content,
      model: typeof data.model === "string" ? data.model : req.model,
      costUsd: Number(data.usage?.cost ?? 0) || 0,
      promptTokens: Number(data.usage?.prompt_tokens ?? 0) || 0,
      completionTokens: Number(data.usage?.completion_tokens ?? 0) || 0,
    };
  }
}

/** Call the primary model; on a transport or API error, call the fallback once. */
export async function chatWithFallback(
  client: ChatClient,
  models: ModelPair,
  req: Omit<ChatRequest, "model">,
): Promise<ChatResult> {
  try {
    return await client.chat({ ...req, model: models.primary });
  } catch (e) {
    if (!models.fallback || !(e instanceof OpenRouterError)) throw e;
    return client.chat({ ...req, model: models.fallback });
  }
}
