import { drizzle, type PostgresJsDatabase } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "../db/schema";

export type Db = PostgresJsDatabase<typeof schema>;
const g = globalThis as unknown as { __cgDb?: Db };

export const DEFAULT_DATABASE_URL = "postgres://cg:cg@localhost:54329/cg";

/** Lazily connected (postgres-js connects on the first query), cached across dev hot reloads. */
export function db(): Db {
  if (!g.__cgDb) {
    const sql = postgres(process.env.DATABASE_URL ?? DEFAULT_DATABASE_URL, { max: 5, onnotice: () => {} });
    g.__cgDb = drizzle(sql, { schema });
  }
  return g.__cgDb;
}

export { schema };
