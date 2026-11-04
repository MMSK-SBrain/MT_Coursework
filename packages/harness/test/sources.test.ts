import { describe, expect, it, vi } from "vitest";
import { FixtureOccupationSource, FixtureLinkSource } from "../src/sources/fixture.js";
import { YouTubeLinkSource, parseIsoDuration } from "../src/sources/youtube.js";
import { EscoOccupationSource } from "../src/sources/esco.js";
import { checkAlive, isBlockedAddress, pinnedTransport, safeLookup, type Transport } from "../src/sources/alive.js";
import { jsonResponse } from "./helpers.js";

describe("fixture sources", () => {
  it("are deterministic", async () => {
    const j = new FixtureOccupationSource();
    const q = { keywords: ["requirements", "traceability"], limit: 5 };
    const a = await j.search(q);
    expect(a).toEqual(await j.search(q));
    expect(a[0]!.title).toBe("Requirements Engineer");
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

describe("EscoOccupationSource", () => {
  const occ = (n: number) => `http://data.europa.eu/esco/occupation/${n}`;
  const fetch = vi.fn(async (url: string) => {
    const u = new URL(url);
    expect(u.origin + u.pathname).toMatch(/^https:\/\/ec\.europa\.eu\/esco\/api\//);
    if (u.pathname.endsWith("/search")) {
      const t = u.searchParams.get("text");
      const hits = t === "battery" ? [occ(1), occ(2)] : [occ(2), occ(3)];
      return { ok: true, status: 200, json: async () => ({ _embedded: { results: hits.map((uri) => ({ uri, title: uri })) } }) };
    }
    const uri = u.searchParams.get("uri")!;
    if (uri === occ(3)) return { ok: false, status: 500, json: async () => ({}) };
    return { ok: true, status: 200, json: async () => ({ title: `occ ${uri.slice(-1)}`, description: { en: { literal: "d" } }, _links: { hasEssentialSkill: [{ title: "battery chemistry" }], hasOptionalSkill: [] } }) };
  });

  it("interleaves keywords, dedupes, drops failed lookups and caches details", async () => {
    const s = new EscoOccupationSource({ fetch });
    const r = await s.search({ keywords: ["battery", "test"], limit: 10 });
    expect(r.map((o) => o.title)).toEqual(["occ 1", "occ 2"]); // occ 3 failed
    expect(r[0]).toMatchObject({ essentialSkills: ["battery chemistry"], source: "esco" });
    expect(r[0]!.url).toMatch(/^https:\/\/esco\.ec\.europa\.eu\/en\/classification\/occupation\?uri=/);
    const calls = fetch.mock.calls.length;
    await s.search({ keywords: ["battery"], limit: 10 });
    expect(fetch.mock.calls.length).toBe(calls + 1); // only the search call; details came from the cache
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
