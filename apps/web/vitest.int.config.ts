import { defineConfig } from "vitest/config";
import { fileURLToPath } from "node:url";

// Integration tests: require `docker compose up -d` (Postgres on 54329) and DATABASE_URL.
export default defineConfig({
  resolve: { alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) } },
  test: { include: ["src/**/*.int.test.ts"], testTimeout: 20000 },
});
