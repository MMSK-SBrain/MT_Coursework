// Worker entry point: `pnpm --filter @cg/web worker` (set INLINE_JOBS=0 for the web process when you run this).
import { claimNext, processJob, requeueStuck } from "./lib/jobs";

const IDLE_MS = Number(process.env.WORKER_IDLE_MS ?? 1000);
let stopping = false;
process.on("SIGINT", () => (stopping = true));
process.on("SIGTERM", () => (stopping = true));

async function main() {
  console.log("[worker] started");
  let lastSweep = 0;
  while (!stopping) {
    if (Date.now() - lastSweep > 60_000) {
      await requeueStuck().catch((e) => console.error("[worker] requeue", e));
      lastSweep = Date.now();
    }
    const job = await claimNext().catch((e) => (console.error("[worker] claim", e), null));
    if (job) {
      console.log(`[worker] ${job.type} ${job.id}`);
      await processJob(job);
    } else {
      await new Promise((r) => setTimeout(r, IDLE_MS));
    }
  }
  console.log("[worker] stopped");
  process.exit(0);
}

void main();
