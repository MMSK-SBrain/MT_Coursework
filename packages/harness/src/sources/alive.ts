import { lookup as dnsLookup } from "node:dns/promises";
import { isIP } from "node:net";
import { isHttpUrl } from "@cg/core";
import type { FetchLike } from "../openrouter.js";

export type LookupLike = (host: string) => Promise<{ address: string; family: number }[]>;

export interface AliveOptions {
  fetch?: FetchLike;
  lookup?: LookupLike;
  timeoutMs?: number;
  maxRedirects?: number;
}

/** True for addresses a link check must never reach: loopback, private, link-local (cloud metadata), CGNAT, multicast, ULA, unspecified. */
export function isBlockedAddress(addr: string): boolean {
  const a = addr.toLowerCase().replace(/^\[|\]$/g, "");
  const v4mapped = a.match(/^::ffff:(\d+\.\d+\.\d+\.\d+)$/);
  if (v4mapped) return isBlockedAddress(v4mapped[1]!);
  if (isIP(a) === 4) {
    const [p, q] = a.split(".").map(Number) as [number, number];
    return (
      p === 0 || p === 10 || p === 127 || p >= 224 || // this-network, private, loopback, multicast/reserved
      (p === 100 && q >= 64 && q <= 127) || // CGNAT
      (p === 169 && q === 254) || // link-local, incl. 169.254.169.254 metadata
      (p === 172 && q >= 16 && q <= 31) ||
      (p === 192 && q === 168) ||
      (p === 192 && q === 0) || (p === 198 && (q === 18 || q === 19)) // IETF protocol assignments, benchmarking
    );
  }
  if (isIP(a) === 6) {
    return a === "::" || a === "::1" || /^f[cd]/.test(a) || /^fe[89ab]/.test(a) || /^ff/.test(a);
  }
  return true; // not an IP at all: refuse
}

/** Resolves the host and refuses it if any of its addresses is internal. */
async function assertPublicHost(host: string, lookup: LookupLike): Promise<void> {
  const h = host.replace(/^\[|\]$/g, "");
  const addrs = isIP(h) ? [{ address: h, family: isIP(h) }] : await lookup(h);
  if (!addrs.length || addrs.some((x) => isBlockedAddress(x.address))) throw new Error(`blocked host ${host}`);
}

const defaultLookup: LookupLike = (host) => dnsLookup(host, { all: true, verbatim: true });

/**
 * True when the URL resolves (status < 400). Tries HEAD first; falls back to GET for servers
 * that reject HEAD (405/403/501). Network errors, timeouts and blocked hosts count as dead.
 *
 * Links come from teachers and web search, so this is an SSRF surface: only http(s), every hop's
 * host is resolved and refused if internal, and redirects are followed by hand so each Location is checked too.
 * ponytail: the connection isn't pinned to the checked IP, so a DNS-rebinding host could still slip
 * between lookup and connect; in production run link checks through an egress proxy that blocks internal ranges.
 */
export async function checkAlive(url: string, opts: AliveOptions = {}): Promise<boolean> {
  const f = opts.fetch ?? ((i, init) => fetch(i, init));
  const lookup = opts.lookup ?? defaultLookup;
  const timeoutMs = opts.timeoutMs ?? 8000;
  const maxRedirects = opts.maxRedirects ?? 5;
  if (!isHttpUrl(url)) return false;

  const go = async (method: "HEAD" | "GET"): Promise<Response> => {
    let current = url;
    for (let hop = 0; hop <= maxRedirects; hop++) {
      await assertPublicHost(new URL(current).hostname, lookup);
      const res = await f(current, {
        method,
        redirect: "manual",
        signal: AbortSignal.timeout(timeoutMs),
        headers: { "User-Agent": "ReynlabCourseGenerator/0.1 (link check)" },
      });
      const loc = res.headers.get("location");
      if (res.status >= 300 && res.status < 400 && loc) {
        await res.body?.cancel().catch(() => {});
        current = new URL(loc, current).toString();
        if (!isHttpUrl(current)) throw new Error("redirect to a non-http(s) URL");
        continue;
      }
      return res;
    }
    throw new Error("too many redirects");
  };

  try {
    const head = await go("HEAD");
    if (head.status < 400) return true;
    if (![403, 405, 501].includes(head.status)) return false;
    const get = await go("GET");
    // Don't download the body of a page we only wanted to check.
    await get.body?.cancel().catch(() => {});
    return get.status < 400;
  } catch {
    return false;
  }
}
