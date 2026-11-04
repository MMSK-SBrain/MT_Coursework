import { NextResponse } from "next/server";
import { ZodError } from "zod";

import { HttpError } from "./errors";

export { HttpError };

/** Wrap a route handler: HttpError and ZodError become JSON responses. */
export function route<A extends unknown[]>(fn: (...args: A) => Promise<Response>) {
  return async (...args: A): Promise<Response> => {
    try {
      return await fn(...args);
    } catch (e) {
      if (e instanceof HttpError) return NextResponse.json({ error: e.message, ...e.body }, { status: e.status });
      if (e instanceof ZodError) return NextResponse.json({ error: "Invalid data", issues: e.issues.slice(0, 10) }, { status: 400 });
      console.error(e);
      return NextResponse.json({ error: e instanceof Error ? e.message : "Server error" }, { status: 500 });
    }
  };
}
