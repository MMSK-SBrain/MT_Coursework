// Web-search job source: a STUB behind the JobSource interface.
// The jobs data provider is an open decision (a job-listing API with India coverage, or a web-search
// API). This adapter turns any web-search provider into job postings. It never scrapes job boards:
// it only uses the search provider's titles and snippets, and drops LinkedIn and Naukri results.
import type { JobPosting, JobSource } from "@cg/core";

export type WebSearchProvider = (q: { query: string; limit: number }) => Promise<{ title: string; url: string; snippet: string }[]>;

/** Domains we must not take job data from (terms of service). */
export const BLOCKED_JOB_DOMAINS = ["linkedin.com", "naukri.com"];

export function isBlockedDomain(url: string): boolean {
  try {
    const host = new URL(url).hostname.toLowerCase();
    return BLOCKED_JOB_DOMAINS.some((d) => host === d || host.endsWith("." + d));
  } catch {
    return true;
  }
}

const notConfigured: WebSearchProvider = async () => {
  throw new Error("No web-search provider configured for WebSearchJobSource (jobs data provider is an open decision). Use FixtureJobSource for dev.");
};

export class WebSearchJobSource implements JobSource {
  constructor(private readonly provider: WebSearchProvider = notConfigured, private readonly now: () => Date = () => new Date()) {}

  // `days` cannot be enforced from snippets; a provider that supports date filters should apply it.
  async search(q: { keywords: string[]; markets: string[]; days: number; limit: number }): Promise<JobPosting[]> {
    const out: JobPosting[] = [];
    const seen = new Set<string>();
    const perQuery = Math.max(5, Math.ceil(q.limit / Math.max(1, q.keywords.length * q.markets.length)));
    for (const market of q.markets) {
      for (const kw of q.keywords) {
        const results = await this.provider({ query: `"${kw}" job opening ${market}`, limit: perQuery });
        for (const r of results) {
          if (isBlockedDomain(r.url) || seen.has(r.url)) continue;
          seen.add(r.url);
          out.push({
            title: r.title,
            location: market,
            postedAt: this.now().toISOString().slice(0, 10), // unknown from a snippet; the search date
            skills: [kw],
            description: r.snippet,
            url: r.url,
            source: "websearch",
          });
          if (out.length >= q.limit) return out;
        }
      }
    }
    return out;
  }
}
