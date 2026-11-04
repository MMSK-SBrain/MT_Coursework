// Groups feedback rows for the admin page: by stage (from the prompt id or the item path), then by model.

interface Row {
  scope: string;
  promptId?: string | null;
  targetPath?: string | null;
  model?: string | null;
  rating?: string | null;
}

export function feedbackStage(f: Row): string {
  if (f.scope === "site") return "site";
  const head = (f.promptId ?? "").split(".")[0] || (f.targetPath ?? "").replace(/[[.].*$/, "");
  return head || "unknown";
}

export function groupFeedback<T extends Row>(rows: T[]) {
  const stages = new Map<string, Map<string, T[]>>();
  for (const r of rows) {
    const s = feedbackStage(r);
    const m = r.model ?? (r.scope === "site" ? "-" : "unknown");
    if (!stages.has(s)) stages.set(s, new Map());
    const byModel = stages.get(s)!;
    byModel.set(m, [...(byModel.get(m) ?? []), r]);
  }
  return [...stages.entries()]
    .sort(([a], [b]) => (a === "site" ? 1 : b === "site" ? -1 : a.localeCompare(b)))
    .map(([stage, models]) => ({
      stage,
      models: [...models.entries()].map(([model, items]) => ({
        model, items, up: items.filter((i) => i.rating === "up").length, down: items.filter((i) => i.rating === "down").length,
      })),
    }));
}
