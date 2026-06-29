import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { ApiJobMetric } from "../../types/tensorguard";

const { setOption, resize, dispose, echartsInit } = vi.hoisted(() => {
  const setOption = vi.fn();
  const resize = vi.fn();
  const dispose = vi.fn();
  const echartsInit = vi.fn(() => ({ setOption, resize, dispose }));
  return { setOption, resize, dispose, echartsInit };
});

vi.mock("echarts/core", () => ({
  init: echartsInit,
  use: vi.fn(),
}));

import GpuChart from "./GpuChart.vue";

afterEach(() => {
  vi.clearAllMocks();
  document.body.innerHTML = "";
});

describe("GpuChart", () => {
  it("keeps missing GPU samples as null gaps and reuses one chart instance", async () => {
    const wrapper = mount(GpuChart, {
      props: {
        metrics: [
          {
            timestamp: "2026-06-28T17:00:00",
            stage: "qwen_seed",
            elapsed_seconds: 1,
            qwen_raw: 4,
            qwen_valid: 1,
            total_files: 0,
            trace_hits: 0,
            seed: 0,
            valid: 0,
            exception: 0,
            crash: 0,
            notarget: 0,
            hangs: 0,
            flaky: 0,
          },
          {
            timestamp: "2026-06-28T17:00:01",
            stage: "qwen_seed",
            elapsed_seconds: 2,
            qwen_raw: 8,
            qwen_valid: 3,
            total_files: 0,
            trace_hits: 0,
            seed: 0,
            valid: 0,
            exception: 0,
            crash: 0,
            notarget: 0,
            hangs: 0,
            flaky: 0,
            gpu: {
              collected_at: "2026-06-28T17:00:01",
              index: 0,
              utilization_percent: 50,
              memory_used_mib: 4096,
              memory_total_mib: 8192,
            },
          },
        ] as ApiJobMetric[],
      },
    });

    await flushPromises();

    expect(echartsInit).toHaveBeenCalledTimes(1);
    expect(setOption).toHaveBeenCalledTimes(1);
    expect(setOption.mock.calls[0][0].series[0].data).toEqual([
      [1, null],
      [2, 50],
    ]);

    await wrapper.setProps({
      metrics: [
        {
          timestamp: "2026-06-28T17:00:00",
          stage: "qwen_seed",
          elapsed_seconds: 1,
          qwen_raw: 4,
          qwen_valid: 1,
          total_files: 0,
          trace_hits: 0,
          seed: 0,
          valid: 0,
          exception: 0,
          crash: 0,
          notarget: 0,
          hangs: 0,
          flaky: 0,
          gpu: {
            collected_at: "2026-06-28T17:00:00",
            index: 0,
            utilization_percent: 25,
            memory_used_mib: 2048,
            memory_total_mib: 8192,
          },
        },
      ] as ApiJobMetric[],
    });
    await flushPromises();

    expect(echartsInit).toHaveBeenCalledTimes(1);
    expect(setOption).toHaveBeenCalledTimes(2);

    wrapper.unmount();

    expect(dispose).toHaveBeenCalledTimes(1);
  });

  it("shows an empty state when there are no gpu samples", async () => {
    const wrapper = mount(GpuChart, {
      props: { metrics: [] },
    });

    await flushPromises();

    expect(wrapper.text()).toContain("暂无");
    expect(echartsInit).not.toHaveBeenCalled();
  });
});
