import type { FetchLike } from "../openrouter.js";

export interface AliveOptions {
  fetch?: FetchLike;
  timeoutMs?: number;
}

/**
 * True when the URL resolves (status < 400). Tries HEAD first; falls back to GET for servers
 * that reject HEAD (405/403/501). Network errors and timeouts count as dead.
 */
export async function checkAlive(url: string, opts: AliveOptions = {}): Promise<boolean> {
  const f = opts.fetch ?? ((i, init) => fetch(i, init));
  const timeoutMs = opts.timeoutMs ?? 8000;
  try {
    new URL(url);
  } catch {
    return false;
  }
  const go = (method: "HEAD" | "GET") =>
    f(url, { method, redirect: "follow", signal: AbortSignal.timeout(timeoutMs), headers: { "User-Agent": "ReynlabCourseGenerator/0.1 (link check)" } });
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
