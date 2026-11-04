import { describe, expect, it } from "vitest";
import { feedbackStage, groupFeedback } from "./feedback-groups";

describe("admin feedback grouping", () => {
  it("groups by stage, then model, with site feedback last", () => {
    const rows = [
      { scope: "item", promptId: "outcomes.draft", model: "qwen", rating: "down" },
      { scope: "item", promptId: "outcomes.edit.split", model: "qwen", rating: "up" },
      { scope: "item", promptId: "outcomes.draft", model: "glm", rating: "down" },
      { scope: "site", rating: null },
      { scope: "item", targetPath: "fit[f1]", model: "mock" },
    ];
    expect(feedbackStage(rows[4]!)).toBe("fit");
    const g = groupFeedback(rows);
    expect(g.map((x) => x.stage)).toEqual(["fit", "outcomes", "site"]);
    const outcomes = g.find((x) => x.stage === "outcomes")!;
    expect(outcomes.models.find((m) => m.model === "qwen")).toMatchObject({ up: 1, down: 1 });
    expect(outcomes.models.find((m) => m.model === "glm")).toMatchObject({ up: 0, down: 1 });
  });
});
