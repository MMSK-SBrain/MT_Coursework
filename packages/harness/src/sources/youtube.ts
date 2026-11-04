// LinkSource backed by the YouTube Data API v3 (YOUTUBE_API_KEY). Web search is delegated to
// a pluggable provider, because the web-search API is not chosen yet.
import type { LinkSource, VideoCandidate } from "@cg/core";
import type { FetchLike } from "../openrouter.js";
import { checkAlive } from "./alive.js";
import type { WebSearchProvider } from "./websearch.js";

const API = "https://www.googleapis.com/youtube/v3";

/** ISO 8601 duration ("PT1H2M3S", "P1DT2H") -> seconds. */
export function parseIsoDuration(d: string): number {
  const m = d.match(/^P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?$/);
  if (!m) return 0;
  const [, days, h, min, s] = m;
  return Math.round(Number(days ?? 0) * 86400 + Number(h ?? 0) * 3600 + Number(min ?? 0) * 60 + Number(s ?? 0));
}

export interface YouTubeOptions {
  apiKey?: string;
  fetch?: FetchLike;
  web?: WebSearchProvider;
  timeoutMs?: number;
  relevanceLanguage?: string; // e.g. "en"
}

export class YouTubeLinkSource implements LinkSource {
  private readonly apiKey: string;
  private readonly f: FetchLike;
  private readonly timeoutMs: number;

  constructor(private readonly opts: YouTubeOptions = {}) {
    const key = opts.apiKey ?? (typeof process !== "undefined" ? process.env.YOUTUBE_API_KEY : undefined);
    if (!key) throw new Error("YOUTUBE_API_KEY is not set. Use FixtureLinkSource for dev and tests.");
    this.apiKey = key;
    this.f = opts.fetch ?? ((i, init) => fetch(i, init));
    this.timeoutMs = opts.timeoutMs ?? 15_000;
  }

  private async get(path: string, params: Record<string, string>): Promise<any> {
    const qs = new URLSearchParams({ ...params, key: this.apiKey });
    const res = await this.f(`${API}/${path}?${qs}`, { signal: AbortSignal.timeout(this.timeoutMs) });
    if (!res.ok) throw new Error(`YouTube ${path}: HTTP ${res.status} ${(await res.text()).slice(0, 200)}`);
    return res.json();
  }

  async youtube(q: { query: string; maxDurationSec?: number; limit: number }): Promise<VideoCandidate[]> {
    const max = q.maxDurationSec;
    // Coarse server-side filter: short < 4 min, medium 4-20 min, long > 20 min.
    const videoDuration = max === undefined ? "any" : max <= 240 ? "short" : max <= 1200 ? "medium" : "any";
    const search = await this.get("search", {
      part: "snippet",
      type: "video",
      q: q.query,
      maxResults: String(Math.min(50, Math.max(q.limit * 2, 5))),
      videoDuration,
      safeSearch: "strict",
      ...(this.opts.relevanceLanguage ? { relevanceLanguage: this.opts.relevanceLanguage } : {}),
    });
    const ids: string[] = (search.items ?? []).map((i: any) => i.id?.videoId).filter(Boolean);
    if (!ids.length) return [];
    const details = await this.get("videos", { part: "snippet,contentDetails,status", id: ids.join(",") });
    const out: VideoCandidate[] = [];
    for (const v of details.items ?? []) {
      if (v.status?.embeddable === false || v.status?.privacyStatus === "private") continue;
      const durationSec = parseIsoDuration(v.contentDetails?.duration ?? "");
      if (!durationSec || (max !== undefined && durationSec > max)) continue;
      out.push({
        title: v.snippet?.title ?? "",
        url: `https://www.youtube.com/watch?v=${v.id}`,
        channel: v.snippet?.channelTitle ?? "",
        durationSec,
        publishedAt: v.snippet?.publishedAt ?? "",
        description: v.snippet?.description ?? "",
      });
    }
    return out.slice(0, q.limit);
  }

  async web(q: { query: string; limit: number }) {
    return this.opts.web ? this.opts.web(q) : [];
  }

  isAlive(url: string) {
    return checkAlive(url);
  }
}
