import { flushPromises, mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import LiveLog from "./LiveLog.vue";

describe("LiveLog", () => {
  it("filters to stage-specific logs, keeps text safe, and stops auto-scroll after manual scroll", async () => {
    const wrapper = mount(LiveLog, {
      attachTo: document.body,
      props: {
        stageKey: "qwen_seed",
        logs: {
          "01_qwen_seed.log": "seed <strong>safe</strong>",
          "02_ev_generation.log": "ev_generation log",
          "03_driver.log": "driver log",
          extra: "hidden",
        },
      },
    });

    await flushPromises();

    expect(wrapper.text()).toContain("seed <strong>safe</strong>");
    expect(wrapper.text()).not.toContain("ev_generation log");
    expect(wrapper.text()).not.toContain("driver log");
    expect(wrapper.find("strong").exists()).toBe(false);

    const body = wrapper.get("[data-testid='live-log-body']").element as HTMLElement;
    Object.defineProperty(body, "scrollHeight", { value: 500, configurable: true });
    Object.defineProperty(body, "clientHeight", { value: 200, configurable: true });
    Object.defineProperty(body, "scrollTop", { value: 250, writable: true, configurable: true });

    body.dispatchEvent(new Event("scroll"));
    await flushPromises();

    expect(wrapper.get("[data-testid='auto-scroll-toggle']").attributes("aria-pressed")).toBe("false");

    await wrapper.setProps({
      logs: {
        "01_qwen_seed.log": "seed <strong>safe</strong>\nmore",
      },
    });
    await flushPromises();

    expect(body.scrollTop).toBe(250);
  });
});
