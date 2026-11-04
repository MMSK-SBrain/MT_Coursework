import { describe, expect, it, vi } from "vitest";
import { HttpError } from "./errors";
import { route } from "./http";
import { publicJobError } from "./jobs";
import { prepareCourseWrite } from "./repo";
import { sampleCourse } from "./test-fixtures";

describe("sources are server-managed", () => {
  it("ignores sources supplied with a client write and keeps the stored ones", async () => {
    const { course } = await sampleCourse();
    const stored = { ...course, sources: [{ id: "f1", kind: "handout" as const, filename: "h.docx", mime: "x", storageKey: "uploads/c-test/f1.docx" }] };
    const evil = { ...stored, sources: [{ id: "x", kind: "handout" as const, filename: "x", mime: "x", storageKey: "uploads/someone-else/secret.pdf" }] };
    expect(prepareCourseWrite(stored, evil, "u-test").sources).toEqual(stored.sources);
    expect(prepareCourseWrite(null, evil, "u-test").sources).toEqual([]);
  });

  it("only the explicit option (the upload route) changes sources", async () => {
    const { course } = await sampleCourse();
    const src = [{ id: "f2", kind: "moduleSheet" as const, filename: "m.xlsx", mime: "x", storageKey: "uploads/c-test/f2.xlsx" }];
    expect(prepareCourseWrite(course, course, "u-test", { sources: src }).sources).toEqual(src);
  });

  it("forces the owner on every write", async () => {
    const { course } = await sampleCourse();
    expect(prepareCourseWrite(course, { ...course, ownerId: "someone-else" }, "u-test").ownerId).toBe("u-test");
  });
});

describe("errors do not leak internals", () => {
  it("returns a generic 500 with a request id and logs the details", async () => {
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    const res = await route(async () => {
      throw new Error("connect ECONNREFUSED 10.0.0.5:5432 password=hunter2");
    })();
    const body = (await res.json()) as { error: string; requestId: string };
    expect(res.status).toBe(500);
    expect(body.error).not.toMatch(/ECONNREFUSED|hunter2/);
    expect(body.error).toContain(body.requestId);
    expect(String(log.mock.calls[0]?.[0])).toContain(body.requestId);
    log.mockRestore();
  });

  it("still passes HttpError messages through", async () => {
    const res = await route(async () => {
      throw new HttpError(404, "Course not found");
    })();
    expect(res.status).toBe(404);
    expect(await res.json()).toMatchObject({ error: "Course not found" });
  });

  it("job errors shown to teachers are generic unless meant for them", () => {
    expect(publicJobError(new Error("relation jobs does not exist"), "j1")).toBe("Generation failed. Reference: j1");
    expect(publicJobError(new HttpError(400, "Upload a handout first"), "j1")).toBe("Upload a handout first");
  });
});
