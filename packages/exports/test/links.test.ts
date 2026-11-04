import { describe, expect, it } from "vitest";
import { mdLink } from "../src/markdown.js";

describe("mdLink", () => {
  it("escapes titles and URLs and drops unsafe schemes", () => {
    expect(mdLink("a](javascript:x)", "https://e.org/x")).toBe("[a\\](javascript:x)](https://e.org/x)");
    expect(mdLink("t", "https://e.org/a (b)")).toBe("[t](https://e.org/a%20%28b%29)");
    expect(mdLink("t", "javascript:alert(1)")).toBe("t");
  });
});
