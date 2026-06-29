import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import type { ApiJobMetric, ApiJobStatus } from "../../types/tensorguard";

import RunSnapshot from "./RunSnapshot.vue";

describe("RunSnapshot", () => {
  it("shows the live api, mode, stage, status, elapsed, and returned model values", () => {
    const jobStatus: ApiJobStatus = {
      job_id: "job-1",
      lib: "torch",
      api: "torch.add",
      mode: "demo",
      qwen_model: "../Qwen2.5-Coder-7B-Instruct",
      mutation_model: "facebook/incoder-1B",
      cuda_device: "0",
      status: "running",
      stage: "ev_generation",
      stages: {
        prompt_check: "success",
        qwen_seed: "success",
        ev_generation: "running",
        driver: "pending",
        summary: "pending",
      },
      error: null,
      updated_at: "2026-06-28T17:00:00",
    };
    const latestMetric: ApiJobMetric = {
      timestamp: "2026-06-28T17:00:02",
      stage: "ev_generation",
      elapsed_seconds: 12,
      qwen_raw: 8,
      qwen_valid: 3,
      total_files: 9,
      trace_hits: 2,
      seed: 0,
      valid: 7,
      exception: 1,
      crash: 0,
      notarget: 0,
      hangs: 0,
      flaky: 0,
    };

    const wrapper = mount(RunSnapshot, {
      props: {
        apiLabel: "torch.add",
        mode: "demo",
        liveStageKey: "ev_generation",
        jobStatus,
        latestMetric,
      },
    });

    expect(wrapper.text()).toContain("torch.add");
    expect(wrapper.text()).toContain("demo");
    expect(wrapper.text()).toContain("InCoder 变异");
    expect(wrapper.text()).toContain("running");
    expect(wrapper.text()).toContain("12");
    expect(wrapper.text()).toContain("../Qwen2.5-Coder-7B-Instruct");
    expect(wrapper.text()).toContain("facebook/incoder-1B");
  });

  it("shows only live job data instead of stale latest-job details", () => {
    const wrapper = mount(RunSnapshot, {
      props: {
        apiLabel: "torch.add",
        mode: "demo",
        liveStageKey: "qwen_seed",
        jobStatus: null,
        latestMetric: null,
      },
    });

    expect(wrapper.text()).toContain("当前阶段暂无");
    expect(wrapper.text()).toContain("当前状态无");
    expect(wrapper.text()).toContain("最新耗时暂无");
    expect(wrapper.text()).not.toContain("Qwen 模型");
    expect(wrapper.text()).not.toContain("变异模型");
  });
});
