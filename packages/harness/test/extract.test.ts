import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { extractText } from "../src/extract.js";

const root = new URL("../../../", import.meta.url).pathname;
const file = (path: string, mime = "application/octet-stream", bytes?: Uint8Array) => ({
  meta: { id: "f", kind: "handout" as const, filename: path.split("/").pop()!, mime, storageKey: path },
  bytes: bytes ?? new Uint8Array(readFileSync(decodeURIComponent(root + path))),
});

describe("extractText", () => {
  it("reads .docx", async () => {
    expect((await extractText(file("legacy/courses/inclusive-management-shop-floor/Training_Proposal_IMSF.docx"))).length).toBeGreaterThan(200);
  });
  it("reads .pdf", async () => {
    expect((await extractText(file("courses/aelzc441-automotive-vehicles/EI Proposal BTC 25 V5.pdf"))).length).toBeGreaterThan(200);
  });
  it("reads .xlsx sheets as tab-separated rows", async () => {
    const t = await extractText(file("courses/aezc516-ice/AEZG516_Course_Template.xlsx"));
    expect(t).toMatch(/^## Sheet: /);
    expect(t).toContain("\t");
  });
  it("reads text and refuses unknown types", async () => {
    expect(await extractText(file("a.txt", "text/plain", new TextEncoder().encode(" hi ")))).toBe("hi");
    await expect(extractText(file("a.exe", "application/x-msdownload", new Uint8Array([1])))).rejects.toThrow(/unsupported/);
    await expect(extractText(file("a.docx", "", new Uint8Array([1, 2, 3])))).rejects.toThrow();
  });
});
