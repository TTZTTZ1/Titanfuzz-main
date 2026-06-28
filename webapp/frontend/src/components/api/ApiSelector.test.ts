import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { ApiListItem } from "../../types/tensorguard";

const { getApis } = vi.hoisted(() => ({
  getApis: vi.fn(),
}));

vi.mock("../../services/tensorguard", () => ({
  getApis,
}));

import ApiSelector from "./ApiSelector.vue";

function apiItem(api: string, lib: "torch" | "tf"): ApiListItem {
  return {
    api,
    lib,
    has_prompt: true,
    prompt_path: `experiment/${lib}/${api}/prompts/structured_info.txt`,
    result_counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
    has_results: false,
    manifest_entry: {
      api,
      library: lib,
      structured_info: `experiment/${lib}/${api}/prompts/structured_info.txt`,
      structured_sha256: "a".repeat(64),
      has_greedy_prompt: false,
      greedy_prompt: null,
      greedy_sha256: null,
      updated_at: "2026-06-28T17:00:00",
    },
  };
}

const fixtures = [apiItem("torch.add", "torch"), apiItem("torch.matmul", "torch"), apiItem("torch.special.Add", "torch")];

function filteredApis(query: string) {
  const normalized = query.toLowerCase();
  return fixtures.filter((item) => item.api.toLowerCase().includes(normalized));
}

afterEach(() => {
  vi.clearAllMocks();
  vi.useRealTimers();
});

beforeEach(() => {
  vi.useFakeTimers();
});

describe("ApiSelector", () => {
  it("shows all APIs for an empty query, filters partial matches, and emits the selected item", async () => {
    getApis.mockImplementation(async (_lib: string, query: string) => filteredApis(query));

    const wrapper = mount(ApiSelector, {
      props: {
        selected: fixtures[0],
      },
    });

    await vi.runAllTimersAsync();
    await flushPromises();

    expect(wrapper.find('[role="combobox"]').exists()).toBe(true);
    expect(wrapper.find('[role="listbox"]').exists()).toBe(true);
    expect(wrapper.get('[role="option"][aria-selected="true"]').text()).toContain("torch.add");
    expect(wrapper.get('[role="option"][aria-selected="true"]').classes()).toContain("api-selector__option--selected");
    expect(wrapper.text()).toContain("torch.add");
    expect(wrapper.text()).toContain("torch.matmul");
    expect(wrapper.text()).toContain("torch.special.Add");

    await wrapper.get('[role="combobox"]').setValue("ADD");
    await vi.advanceTimersByTimeAsync(250);
    await flushPromises();

    expect(wrapper.text()).toContain("torch.add");
    expect(wrapper.text()).toContain("torch.special.Add");
    expect(wrapper.text()).not.toContain("torch.matmul");

    await wrapper.get('[role="option"]').trigger("click");

    expect(wrapper.emitted("select")).toHaveLength(1);
    expect(wrapper.emitted("select")?.[0]).toEqual([fixtures[0]]);
  });
});
