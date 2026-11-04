import { NextResponse } from "next/server";
import { randomUUID } from "node:crypto";
import { ZodError } from "zod";
import { HttpError } from "./errors";

export { HttpError };

/**
 * Wrap a route handler: HttpError and ZodError become JSON responses. Anything else is logged on the server with a
 * request id, and the client gets only a generic message and that id (no internal error text).
 */
export function route<A extends unknown[]>(fn: (...args: A) => Promise<Response>) {
  return async (...args: A): Promise<Response> => {
    try {
      return await fn(...args);
    } catch (e) {
      if (e instanceof HttpError) return NextResponse.json({ error: e.message, ...e.body }, { status: e.status });
      if (e instanceof ZodError) return NextResponse.json({ error: "Invalid data", issues: e.issues.slice(0, 10) }, { status: 400 });
      const requestId = randomUUID();
      console.error(`[api] request ${requestId} failed`, e);
      return NextResponse.json({ error: `Something went wrong. Reference: ${requestId}`, requestId }, { status: 500 });
    }
  };
}
