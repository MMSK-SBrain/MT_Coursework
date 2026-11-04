import { lookup as dnsLookup, type LookupAddress } from "node:dns";
import http from "node:http";
import https from "node:https";
import { BlockList, isIP } from "node:net";
import { isHttpUrl } from "@cg/core";

// Links come from teachers and web search and are checked from our servers, so this is an SSRF surface.
// Rules: only http(s); every address is checked against BLOCKED (net.BlockList also matches IPv4-mapped
// IPv6 such as ::ffff:7f00:1 against the IPv4 rules); the check runs inside the socket's DNS lookup, so the
// connection uses exactly the address that was checked (no DNS-rebinding window); redirects are followed by
// hand and each hop is checked again.

const BLOCKED = new BlockList();
for (const [net, bits] of [
  ["0.0.0.0", 8], ["10.0.0.0", 8], ["100.64.0.0", 10], ["127.0.0.0", 8], ["169.254.0.0", 16], ["172.16.0.0", 12],
  ["192.0.0.0", 24], ["192.0.2.0", 24], ["192.168.0.0", 16], ["198.18.0.0", 15], ["198.51.100.0", 24], ["203.0.113.0", 24],
  ["224.0.0.0", 3], // multicast and reserved, up to 255.255.255.255
] as const) BLOCKED.addSubnet(net, bits, "ipv4");
for (const [net, bits] of [
  ["::", 96], // unspecified, loopback and IPv4-compatible addresses
  // IPv4-mapped (::ffff:0:0/96) needs no rule: BlockList checks those against the IPv4 rules above.
  // Adding it would block every IPv4 address, because IPv4 addresses are also matched in mapped form.
  ["64:ff9b::", 96], ["64:ff9b:1::", 48], // NAT64: can reach internal IPv4
  ["100::", 64], // discard
  ["2001::", 32], // Teredo: embeds an IPv4 address
  ["2001:db8::", 32], // documentation
  ["2002::", 16], // 6to4: embeds an IPv4 address
  ["fc00::", 7], // unique local
  ["fe80::", 10], // link-local
  ["fec0::", 10], // site-local (deprecated)
  ["ff00::", 8], // multicast
] as const) BLOCKED.addSubnet(net, bits, "ipv6");

/** True for any address a link check must never reach. Anything that isn't an IP literal is refused too. */
export function isBlockedAddress(addr: string): boolean {
  const a = addr.replace(/^\[|\]$/g, "");
  const family = isIP(a);
  if (family === 0) return true;
  return BLOCKED.check(a, family === 4 ? "ipv4" : "ipv6");
}

type Resolver = (host: string, cb: (err: NodeJS.ErrnoException | null, addrs: LookupAddress[]) => void) => void;
const systemResolver: Resolver = (host, cb) => dnsLookup(host, { all: true, verbatim: true }, cb);

/**
 * A `lookup` for http(s).request that resolves the host and refuses it if any address is blocked.
 * Because Node connects to the address this returns, the checked address is the one used for the socket.
 */
export function safeLookup(resolve: Resolver = systemResolver) {
  return (host: string, opts: { all?: boolean }, cb: (...args: unknown[]) => void) => {
    resolve(host, (err, addrs) => {
      if (err) return cb(err);
      if (!addrs.length || addrs.some((x) => isBlockedAddress(x.address))) {
        return cb(Object.assign(new Error(`blocked host ${host}`), { code: "EBLOCKED" }));
      }
      if (opts?.all) cb(null, addrs);
      else cb(null, addrs[0]!.address, addrs[0]!.family);
    });
  };
}

export interface HopResult {
  status: number;
  location: string | null;
}
/** Sends one request without following redirects and without reading the body. */
export type Transport = (url: string, method: "HEAD" | "GET", timeoutMs: number) => Promise<HopResult>;

export const pinnedTransport: Transport = (url, method, timeoutMs) =>
  new Promise((resolve, reject) => {
    const u = new URL(url);
    // IP literals skip DNS, so check them here; hostnames are checked by safeLookup at connect time.
    if (isIP(u.hostname.replace(/^\[|\]$/g, "")) && isBlockedAddress(u.hostname)) return reject(new Error(`blocked host ${u.hostname}`));
    const mod = u.protocol === "https:" ? https : http;
    const req = mod.request(u, {
      method,
      lookup: safeLookup() as never,
      timeout: timeoutMs,
      headers: { "User-Agent": "ReynlabCourseGenerator/0.1 (link check)" },
    }, (res) => {
      res.resume(); // discard the body
      resolve({ status: res.statusCode ?? 0, location: res.headers.location ?? null });
      res.destroy();
    });
    req.on("timeout", () => req.destroy(new Error("timeout")));
    req.on("error", reject);
    req.end();
  });

export interface AliveOptions {
  transport?: Transport;
  timeoutMs?: number;
  maxRedirects?: number;
}

/**
 * True when the URL resolves (status < 400). Tries HEAD first; falls back to GET for servers
 * that reject HEAD (405/403/501). Network errors, timeouts and blocked hosts count as dead.
 */
export async function checkAlive(url: string, opts: AliveOptions = {}): Promise<boolean> {
  const send = opts.transport ?? pinnedTransport;
  const timeoutMs = opts.timeoutMs ?? 8000;
  const maxRedirects = opts.maxRedirects ?? 5;
  if (!isHttpUrl(url)) return false;

  const go = async (method: "HEAD" | "GET"): Promise<number> => {
    let current = url;
    for (let hop = 0; hop <= maxRedirects; hop++) {
      const host = new URL(current).hostname;
      if (isIP(host.replace(/^\[|\]$/g, "")) && isBlockedAddress(host)) throw new Error(`blocked host ${host}`);
      const res = await send(current, method, timeoutMs);
      if (res.status >= 300 && res.status < 400 && res.location) {
        current = new URL(res.location, current).toString();
        if (!isHttpUrl(current)) throw new Error("redirect to a non-http(s) URL");
        continue;
      }
      return res.status;
    }
    throw new Error("too many redirects");
  };

  try {
    const head = await go("HEAD");
    if (head < 400) return true;
    if (![403, 405, 501].includes(head)) return false;
    return (await go("GET")) < 400;
  } catch {
    return false;
  }
}
