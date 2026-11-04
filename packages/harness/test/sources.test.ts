import { describe, expect, it, vi } from "vitest";
import { FixtureJobSource, FixtureLinkSource } from "../src/sources/fixture.js";
import { YouTubeLinkSource, parseIsoDuration } from "../src/sources/youtube.js";
import { WebSearchJobSource, isBlockedDomain } from "../src/sources/websearch.js";
import { checkAlive } from "../src/sources/alive.js";
import { jsonResponse } from "./helpers.js";

describe("fixture sources", () => {
  it("are deterministic", async () => {
    const j = new FixtureJobSource();
    const q = { keywords: ["requirements", "traceability"], markets: ["India"], days: 90, limit: 5 };
    const a = await j.search(q);
    expect(a).toEqual(await j.search(q));
    expect(a.length).toBeGreaterThan(0);
    expect(a.every((p) => p.location === "India")).toBe(true);
    const l = new FixtureLinkSource();
    expect((await l.youtube({ query: "HIL battery", limit: 1 }))[0]!.title).toMatch(/HIL/);
    expect((await l.youtube({ query: "x", maxDurationSec: 600, limit: 10 })).every((v) => v.durationSec <= 600)).toBe(true);
  });
});

describe("YouTubeLinkSource", () => {
  it("parses ISO 8601 durations", () => {
    expect(parseIsoDuration("PT1H2M3S")).toBe(3723);
    expect(parseIsoDuration("PT9M")).toBe(540);
    expect(parseIsoDuration("P1DT1S")).toBe(86401);
    expect(parseIsoDuration("bogus")).toBe(0);
  });

  it("searches, fetches durations, and filters by max duration", async () => {
    const fetch = vi.fn(async (url: string) => {
      if (url.includes("/search?")) return jsonResponse({ items: [{ id: { videoId: "a" } }, { id: { videoId: "b" } }] });
      return jsonResponse({
        items: [
          { id: "a", snippet: { title: "Short", channelTitle: "C", publishedAt: "2025-01-01T00:00:00Z", description: "d" }, contentDetails: { duration: "PT5M" }, status: { embeddable: true } },
          { id: "b", snippet: { title: "Long", channelTitle: "C", publishedAt: "2025-01-01T00:00:00Z", description: "d" }, contentDetails: { duration: "PT1H" }, status: { embeddable: true } },
        ],
      });
    });
    const yt = new YouTubeLinkSource({ apiKey: "k", fetch });
    const r = await yt.youtube({ query: "v model", maxDurationSec: 1200, limit: 5 });
    expect(r).toEqual([{ title: "Short", url: "https://www.youtube.com/watch?v=a", channel: "C", durationSec: 300, publishedAt: "2025-01-01T00:00:00Z", description: "d" }]);
    expect(fetch.mock.calls[0]![0]).toMatch(/videoDuration=medium/);
    expect(fetch.mock.calls[0]![0]).toMatch(/key=k/);
    expect(await yt.web({ query: "x", limit: 3 })).toEqual([]);
  });

  it("needs YOUTUBE_API_KEY", () => {
    const prev = process.env.YOUTUBE_API_KEY;
    delete process.env.YOUTUBE_API_KEY;
    expect(() => new YouTubeLinkSource()).toThrow(/YOUTUBE_API_KEY/);
    if (prev !== undefined) process.env.YOUTUBE_API_KEY = prev;
  });
});

describe("WebSearchJobSource (stub)", () => {
  it("drops LinkedIn and Naukri results", async () => {
    const provider = vi.fn(async () => [
      { title: "SE job", url: "https://www.linkedin.com/jobs/1", snippet: "" },
      { title: "SE job", url: "https://www.naukri.com/job/2", snippet: "" },
      { title: "SE job", url: "https://careers.example.com/3", snippet: "requirements" },
    ]);
    const r = await new WebSearchJobSource(provider).search({ keywords: ["systems engineering"], markets: ["India"], days: 30, limit: 10 });
    expect(r.map((p) => p.url)).toEqual(["https://careers.example.com/3"]);
    expect(isBlockedDomain("https://in.linkedin.com/x")).toBe(true);
  });

  it("fails clearly without a provider", async () => {
    await expect(new WebSearchJobSource().search({ keywords: ["x"], markets: ["India"], days: 30, limit: 1 })).rejects.toThrow(/open decision/);
  });
});

describe("checkAlive", () => {
  it("uses HEAD, falls back to GET on 405, and treats errors as dead", async () => {
    expect(await checkAlive("https://a.example", { fetch: async () => new Response(null, { status: 200 }) })).toBe(true);
    const f = vi.fn().mockResolvedValueOnce(new Response(null, { status: 405 })).mockResolvedValueOnce(new Response("ok", { status: 200 }));
    expect(await checkAlive("https://b.example", { fetch: f })).toBe(true);
    expect(f.mock.calls.map((c) => (c[1] as RequestInit).method)).toEqual(["HEAD", "GET"]);
    expect(await checkAlive("https://c.example", { fetch: async () => new Response(null, { status: 404 }) })).toBe(false);
    expect(await checkAlive("https://d.example", { fetch: async () => { throw new Error("timeout"); } })).toBe(false);
    expect(await checkAlive("not a url")).toBe(false);
  });
});
