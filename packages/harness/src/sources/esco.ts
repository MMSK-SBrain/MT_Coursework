// Roles come from ESCO, the European Commission's classification of occupations and skills
// (https://esco.ec.europa.eu). Public API, no key. Only this fixed host is called, so there is no SSRF surface.
import type { Occupation, OccupationSource } from "@cg/core";

export const ESCO_API = "https://ec.europa.eu/esco/api";

type Fetch = (url: string) => Promise<{ ok: boolean; status: number; json(): Promise<unknown> }>;

interface SearchHit { uri: string; title: string }
interface Resource {
  title?: string;
  description?: { en?: { literal?: string } };
  _links?: { hasEssentialSkill?: { title: string }[]; hasOptionalSkill?: { title: string }[] };
}

export interface EscoOptions {
  fetch?: Fetch;
  language?: string;
  /** Occupations taken per keyword. */
  perKeyword?: number;
}

export class EscoOccupationSource implements OccupationSource {
  // ponytail: in-process cache, ESCO changes about once a year; move to the db if several workers need it.
  private readonly cache = new Map<string, Promise<Occupation>>();
  private readonly fetch: Fetch;
  private readonly lang: string;
  private readonly perKeyword: number;

  constructor(opts: EscoOptions = {}) {
    this.fetch = opts.fetch ?? ((u) => globalThis.fetch(u, { signal: AbortSignal.timeout(10_000) }));
    this.lang = opts.language ?? "en";
    this.perKeyword = opts.perKeyword ?? 4;
  }

  private async get<T>(path: string, params: Record<string, string>): Promise<T> {
    const res = await this.fetch(`${ESCO_API}/${path}?${new URLSearchParams({ ...params, language: this.lang })}`);
    if (!res.ok) throw new Error(`ESCO ${path} returned ${res.status}`);
    return (await res.json()) as T;
  }

  async search(q: { keywords: string[]; limit: number }): Promise<Occupation[]> {
    const lists = await Promise.all(q.keywords.map((text) =>
      this.get<{ _embedded?: { results?: SearchHit[] } }>("search", { text, type: "occupation", limit: String(this.perKeyword), full: "false" })
        .then((r) => r._embedded?.results ?? [])
        .catch(() => [] as SearchHit[])));
    // Interleave so every keyword contributes before the limit cuts in.
    const uris: string[] = [];
    for (let i = 0; i < this.perKeyword; i++) for (const l of lists) { const h = l[i]; if (h && !uris.includes(h.uri)) uris.push(h.uri); }
    const picked = uris.slice(0, q.limit);
    const occ = await Promise.all(picked.map((u) => this.occupation(u).catch(() => null)));
    return occ.filter((o): o is Occupation => o !== null && o.essentialSkills.length > 0);
  }

  occupation(uri: string): Promise<Occupation> {
    let p = this.cache.get(uri);
    if (!p) {
      p = this.get<Resource>("resource/occupation", { uri }).then((r) => ({
        uri,
        url: `https://esco.ec.europa.eu/en/classification/occupation?uri=${encodeURIComponent(uri)}`,
        title: r.title ?? uri,
        description: r.description?.en?.literal ?? "",
        essentialSkills: (r._links?.hasEssentialSkill ?? []).map((s) => s.title),
        optionalSkills: (r._links?.hasOptionalSkill ?? []).map((s) => s.title),
        source: "esco",
      }));
      p.catch(() => this.cache.delete(uri)); // don't cache failures
      this.cache.set(uri, p);
    }
    return p;
  }
}
