import { defineConfig } from "vitest/config";
import { fileURLToPath } from "node:url";

// Unit tests only: pure logic, no database. Integration tests (*.int.test.ts) need docker Postgres: `pnpm test:int`.
export default defineConfig({
  resolve: { alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) } },
  test: { include: ["src/**/*.test.ts"], exclude: ["src/**/*.int.test.ts", "node_modules/**"] },
});
