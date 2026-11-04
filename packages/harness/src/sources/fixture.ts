// Deterministic, network-free data sources for tests and dev.
import type { JobPosting, JobSource, LinkSource, VideoCandidate } from "@cg/core";
import { PAGES, POSTINGS, VIDEOS } from "../fixtures/aezc517.js";

const words = (s: string) => s.toLowerCase().split(/[^a-z0-9&]+/).filter((w) => w.length > 2);

function score(text: string, query: string[]): number {
  const t = new Set(words(text));
  return query.reduce((n, w) => n + (t.has(w) ? 1 : 0), 0);
}

export class FixtureJobSource implements JobSource {
  constructor(private readonly postings: JobPosting[] = POSTINGS) {}

  async search(q: { keywords: string[]; markets: string[]; days: number; limit: number }): Promise<JobPosting[]> {
    const qw = q.keywords.flatMap(words);
    const markets = new Set(q.markets.map((m) => m.toLowerCase()));
    const hits = this.postings
      .filter((p) => !markets.size || markets.has(p.location.toLowerCase()))
      .map((p, i) => ({ p, i, s: score(`${p.title} ${p.skills.join(" ")} ${p.description}`, qw) }));
    // Broad search: keep everything that matches; if nothing does, return all (still deterministic).
    const matched = hits.some((h) => h.s > 0) ? hits.filter((h) => h.s > 0) : hits;
    return matched.sort((a, b) => b.s - a.s || a.i - b.i).slice(0, q.limit).map((h) => h.p);
  }
}

export class FixtureLinkSource implements LinkSource {
  constructor(
    private readonly videos: VideoCandidate[] = VIDEOS,
    private readonly pages: { title: string; url: string; snippet: string }[] = PAGES,
    private readonly dead: Set<string> = new Set(),
  ) {}

  async youtube(q: { query: string; maxDurationSec?: number; limit: number }) {
    const qw = words(q.query);
    return this.videos
      .filter((v) => q.maxDurationSec === undefined || v.durationSec <= q.maxDurationSec)
      .map((v, i) => ({ v, i, s: score(`${v.title} ${v.description}`, qw) }))
      .sort((a, b) => b.s - a.s || a.i - b.i)
      .slice(0, q.limit)
      .map((x) => x.v);
  }

  async web(q: { query: string; limit: number }) {
    const qw = words(q.query);
    return this.pages
      .map((p, i) => ({ p, i, s: score(`${p.title} ${p.snippet}`, qw) }))
      .sort((a, b) => b.s - a.s || a.i - b.i)
      .slice(0, q.limit)
      .map((x) => x.p);
  }

  async isAlive(url: string) {
    return !this.dead.has(url);
  }
}
