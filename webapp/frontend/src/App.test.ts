import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import App from "./App.vue";

describe("App", () => {
  it("renders the product name and primary view labels", () => {
    const text = mount(App).text();

    expect(text).toContain("TensorGuard");
    expect(text).toContain("系统总览");
    expect(text).toContain("单 API 运行");
    expect(text).toContain("Bug 复现");
  });
});
