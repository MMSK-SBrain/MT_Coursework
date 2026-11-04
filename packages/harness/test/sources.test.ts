import { describe, expect, it, vi } from "vitest";
import { FixtureJobSource, FixtureLinkSource } from "../src/sources/fixture.js";
import { YouTubeLinkSource, parseIsoDuration } from "../src/sources/youtube.js";
import { WebSearchJobSource, isBlockedDomain } from "../src/sources/websearch.js";
import { checkAlive, isBlockedAddress, pinnedTransport, safeLookup, type Transport } from "../src/sources/alive.js";
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
  const ok: Transport = async () => ({ status: 200, location: null });
  it("uses HEAD, falls back to GET on 405, and treats errors as dead", async () => {
    expect(await checkAlive("https://a.example", { transport: ok })).toBe(true);
    const t = vi.fn<Transport>().mockResolvedValueOnce({ status: 405, location: null }).mockResolvedValueOnce({ status: 200, location: null });
    expect(await checkAlive("https://b.example", { transport: t })).toBe(true);
    expect(t.mock.calls.map((c) => c[1])).toEqual(["HEAD", "GET"]);
    expect(await checkAlive("https://c.example", { transport: async () => ({ status: 404, location: null }) })).toBe(false);
    expect(await checkAlive("https://d.example", { transport: async () => { throw new Error("timeout"); } })).toBe(false);
    expect(await checkAlive("not a url")).toBe(false);
  });

  it("refuses internal IP literals in every spelling, unsafe schemes, and redirects into internal hosts", async () => {
    const spy = vi.fn(ok);
    for (const u of ["http://169.254.169.254/latest/meta-data", "http://127.0.0.1:5432", "http://[::1]/", "http://[::ffff:127.0.0.1]/",
      "http://[::ffff:7f00:1]/", "http://[64:ff9b::a9fe:a9fe]/", "http://[2002:7f00:1::]/", "http://0.0.0.0/", "javascript:alert(1)"]) {
      expect(await checkAlive(u, { transport: spy }), u).toBe(false);
    }
    expect(spy).not.toHaveBeenCalled();
    const redirect = vi.fn<Transport>(async () => ({ status: 302, location: "http://192.168.1.1/admin" }));
    expect(await checkAlive("https://e.example", { transport: redirect })).toBe(false);
    expect(redirect).toHaveBeenCalledTimes(1);
  });

  it("checks resolved addresses at connect time", async () => {
    const lookup = (addr: string) => safeLookup((_h, cb) => cb(null, [{ address: addr, family: addr.includes(":") ? 6 : 4 }]));
    const run = (addr: string) => new Promise<unknown>((res) => lookup(addr)("x.example", {}, (err: unknown) => res(err)));
    expect(await run("10.0.0.5")).toMatchObject({ code: "EBLOCKED" });
    expect(await run("::ffff:a9fe:a9fe")).toMatchObject({ code: "EBLOCKED" });
    expect(await run("93.184.216.34")).toBeNull();
    // The real transport refuses a loopback literal without opening a socket.
    await expect(pinnedTransport("http://127.0.0.1:9/", "HEAD", 1000)).rejects.toThrow(/blocked/);
  });

  it("classifies addresses", () => {
    for (const a of ["10.1.2.3", "172.20.0.1", "192.168.0.1", "127.0.0.1", "169.254.169.254", "100.64.0.1", "0.0.0.0", "::", "::1", "fd00::1", "fe80::1",
      "::ffff:10.0.0.1", "::ffff:7f00:1", "64:ff9b::7f00:1", "2002:a00:1::", "2001:0:4136::1", "ff02::1", "localhost"]) expect(isBlockedAddress(a), a).toBe(true);
    for (const a of ["93.184.216.34", "8.8.8.8", "2606:4700::1111"]) expect(isBlockedAddress(a), a).toBe(false);
  });
});
