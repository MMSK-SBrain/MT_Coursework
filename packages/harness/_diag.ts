import { writeFileSync } from "node:fs";
import { DEFAULT_CONFIG, loadConfig } from "./src/config.js";
import { OpenRouterClient } from "./src/openrouter.js";
import { OpenRouterStages } from "./src/stages.js";
import { FixtureLinkSource, FixtureOccupationSource } from "./src/sources/fixture.js";
import { ExampleStore } from "./src/examples.js";
import { reviewPrompt, FIT_RUBRIC, OUTCOMES_RUBRIC, HOURPLAN_RUBRIC } from "./src/prompts/review.js";
import { budgetClient } from "./eval/run.js";
import { EVAL_COURSES } from "./eval/briefs.js";
const client = budgetClient(new OpenRouterClient({ apiKey: process.env.OPENROUTER_API_KEY }), 1.0);
const JUDGE = "anthropic/claude-sonnet-5.5";
const c0 = EVAL_COURSES.find((c) => c.id === "aezc516-ice")!;
for (const model of ["z-ai/glm-5.3-flash", "anthropic/claude-sonnet-5.5"]) {
  const base = loadConfig({});
  const config = { ...base, models: Object.fromEntries(Object.keys(base.models).map((k) => [k, k === "review" ? { primary: JUDGE } : { primary: model }])) as typeof DEFAULT_CONFIG.models };
  const st = new OpenRouterStages({ client, config, roles: new FixtureOccupationSource(), links: new FixtureLinkSource(), examples: new ExampleStore() });
  const cases: [string, typeof OUTCOMES_RUBRIC, () => Promise<{ value: unknown }>, typeof c0][] = [
    ["draftOutcomes", OUTCOMES_RUBRIC, () => st.draftOutcomes({ ...c0, objectives: [], outcomes: [], modules: c0.modules.map((m) => ({ ...m, outcomes: [] })) }), c0],
    ["proposeFit", FIT_RUBRIC, () => st.proposeFit(c0), c0],
    ["draftHourPlan", HOURPLAN_RUBRIC, () => { const p = c0.plans[0]!; return st.draftHourPlan(c0, p.id, p.sessions[Math.min(2, p.sessions.length - 1)]!.id); }, c0],
  ];
  for (const [stage, rubric, run, course] of cases) {
    const r = await run();
    const ctx = `Course: ${course.brief.title} (${course.brief.level}, ${course.brief.contactHours} h)\nModules: ${course.modules.map((m) => `${m.id} ${m.title}`).join("; ")}\nOutcomes: ${course.outcomes.map((o) => `${o.id} ${o.text}`).join("; ")}\nRoles: ${course.roles.filter((x) => x.selected).map((x) => x.title).join("; ")}`;
    const res = await client.chat({ model: JUDGE, temperature: 0, maxTokens: 4096, json: true, messages: [{ role: "system", content: reviewPrompt.system }, { role: "user", content: reviewPrompt.user({ rubric, contextText: ctx, draft: r.value }, { examples: "" }) }] });
    const tag = `${model.split("/")[1]}-${stage}`;
    writeFileSync(`eval-results/diag/${tag}.json`, JSON.stringify({ output: r.value, review: res.content, context: ctx }, null, 2));
    let rv: any; try { rv = JSON.parse(res.content.replace(/^```(json)?|```$/g, "")); } catch { rv = { raw: res.content.slice(0, 300) }; }
    console.log(`\n== ${tag}`);
    for (const s of rv.scores ?? []) console.log(`  ${s.criterion}: ${s.score}  ${String(s.comment).slice(0, 150)}`);
    const ids = new Set((rv.scores ?? []).map((s: any) => s.criterion));
    const missing = rubric.criteria.filter((c) => !ids.has(c.id)).map((c) => c.id);
    if (missing.length) console.log("  MISSING criteria (scored as 1):", missing.join(", "));
    for (const i of (rv.issues ?? []).slice(0, 4)) console.log("  issue:", String(i).slice(0, 160));
  }
}
console.log("\nspent", client.spent().toFixed(3));
