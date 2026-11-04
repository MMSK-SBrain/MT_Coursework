import { describe, expect, it, vi } from "vitest";
import { chatWithFallback, MissingApiKeyError, OpenRouterClient, OpenRouterError } from "../src/openrouter.js";
import { DEFAULT_CONFIG, loadConfig, modelEnvKey } from "../src/config.js";
import { jsonResponse } from "./helpers.js";

const ok = (content: string, model = "qwen/x", cost = 0.0021) => jsonResponse({ model, choices: [{ message: { content } }], usage: { cost, prompt_tokens: 100, completion_tokens: 50 } });

describe("OpenRouterClient", () => {
  it("posts an OpenAI-compatible request and reads cost from usage", async () => {
    const fetch = vi.fn(async () => ok('{"a":1}'));
    const c = new OpenRouterClient({ apiKey: "k", fetch });
    const r = await c.chat({ model: "qwen/x", messages: [{ role: "user", content: "hi" }], json: true });
    expect(r).toMatchObject({ content: '{"a":1}', model: "qwen/x", costUsd: 0.0021, promptTokens: 100 });
    const [url, init] = fetch.mock.calls[0] as unknown as [string, RequestInit];
    expect(url).toBe("https://openrouter.ai/api/v1/chat/completions");
    expect((init.headers as Record<string, string>).Authorization).toBe("Bearer k");
    const body = JSON.parse(init.body as string);
    expect(body).toMatchObject({ model: "qwen/x", usage: { include: true }, response_format: { type: "json_object" } });
  });

  it("throws OpenRouterError on HTTP errors and API errors", async () => {
    const c1 = new OpenRouterClient({ apiKey: "k", fetch: async () => jsonResponse("rate limited", 429) });
    await expect(c1.chat({ model: "m", messages: [] })).rejects.toMatchObject({ name: "OpenRouterError", status: 429 });
    const c2 = new OpenRouterClient({ apiKey: "k", fetch: async () => jsonResponse({ error: { code: 400, message: "bad" } }) });
    await expect(c2.chat({ model: "m", messages: [] })).rejects.toBeInstanceOf(OpenRouterError);
  });

  it("requires an API key", () => {
    const prev = process.env.OPENROUTER_API_KEY;
    delete process.env.OPENROUTER_API_KEY;
    expect(() => new OpenRouterClient()).toThrow(MissingApiKeyError);
    if (prev !== undefined) process.env.OPENROUTER_API_KEY = prev;
  });

  it("falls back to the second model on a transport error", async () => {
    const fetch = vi.fn()
      .mockResolvedValueOnce(jsonResponse("down", 503))
      .mockResolvedValueOnce(ok("{}", "z-ai/glm"));
    const c = new OpenRouterClient({ apiKey: "k", fetch });
    const r = await chatWithFallback(c, { primary: "qwen/x", fallback: "z-ai/glm" }, { messages: [] });
    expect(r.model).toBe("z-ai/glm");
    expect(JSON.parse((fetch.mock.calls[1]![1] as RequestInit).body as string).model).toBe("z-ai/glm");
  });
});

describe("config", () => {
  it("reads per-stage overrides from the environment", () => {
    expect(modelEnvKey("draftOutcomes")).toBe("CG_MODEL_DRAFT_OUTCOMES");
    const cfg = loadConfig({ CG_MODEL_DEFAULT: "a/b", CG_MODEL_DRAFT_OUTCOMES: "c/d, e/f", CG_RUBRIC_THRESHOLD: "0.6" });
    expect(cfg.models.draftOutcomes).toEqual({ primary: "c/d", fallback: "e/f" });
    expect(cfg.models.proposeFit).toEqual({ primary: "a/b" });
    expect(cfg.models.review).toEqual(DEFAULT_CONFIG.models.review); // the reviewer is not swept by DEFAULT
    expect(cfg.rubricThreshold).toBe(0.6);
  });
});
