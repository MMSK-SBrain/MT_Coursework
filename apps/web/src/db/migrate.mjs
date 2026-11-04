// Applies the SQL migrations in ../../drizzle. Plain JS with pure-JS deps so it also runs in the compose `migrate` container.
import { drizzle } from "drizzle-orm/postgres-js";
import { migrate } from "drizzle-orm/postgres-js/migrator";
import postgres from "postgres";
import { fileURLToPath } from "node:url";

const url = process.env.DATABASE_URL ?? "postgres://cg:cg@localhost:54329/cg";
const sql = postgres(url, { max: 1, onnotice: () => {} });
const folder = fileURLToPath(new URL("../../drizzle", import.meta.url));

try {
  await migrate(drizzle(sql), { migrationsFolder: folder });
  console.log(`[migrate] up to date (${url.replace(/:[^:@/]+@/, ":***@")})`);
} catch (e) {
  console.error("[migrate] failed", e);
  process.exitCode = 1;
} finally {
  await sql.end();
}
