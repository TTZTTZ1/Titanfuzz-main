import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import AppHeader from "./AppHeader.vue";

describe("AppHeader", () => {
  it("shows the three shell tabs and the environment trigger", () => {
    const wrapper = mount(AppHeader, {
      props: {
        activeKey: "overview",
        environmentLabel: "Python 3.11",
      },
    });

    expect(wrapper.text()).toContain("系统总览");
    expect(wrapper.text()).toContain("单 API 运行");
    expect(wrapper.text()).toContain("Bug 复现");
    expect(wrapper.get('button[aria-label="环境信息"]')).toBeTruthy();
  });
});
