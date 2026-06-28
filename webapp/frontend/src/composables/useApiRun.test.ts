import { defineComponent } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { ApiDetailPayload, ApiJobPayload, ApiListItem } from "../types/tensorguard";

const { getApiDetail, getApiJob, startApiRun } = vi.hoisted(() => ({
  getApiDetail: vi.fn(),
  getApiJob: vi.fn(),
  startApiRun: vi.fn(),
}));

vi.mock("../services/tensorguard", () => ({
  getApiDetail,
  getApiJob,
  startApiRun,
}));

import { useApiRun } from "./useApiRun";

function apiItem(api: string, lib: "torch" | "tf", valid = 0): ApiListItem {
  return {
    api,
    lib,
    has_prompt: true,
    prompt_path: `experiment/${lib}/${api}/prompts/structured_info.txt`,
    result_counts: { seed: 0, valid, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
    has_results: valid > 0,
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

function detailItem(api: string, lib: "torch" | "tf", jobId: string | null, valid = 0): ApiDetailPayload {
  return {
    ...apiItem(api, lib, valid),
    api_list: `data/${lib}_apis.txt`,
    prompt_exists: true,
    results_path: `Results/${lib}`,
    latest_job:
      jobId === null
        ? null
        : {
            job_id: jobId,
            out: `demo_runs/${jobId}`,
            status: "success",
            stage: "summary",
            updated_at: "2026-06-28T17:00:00",
            summary_status: "success",
            mutation_model: "facebook/incoder-1B",
            error: null,
          },
  };
}

function jobPayload(jobId: string, api: string, lib: "torch" | "tf", status: "success" | "running" | "pending"): ApiJobPayload {
  return {
    job_id: jobId,
    out: `demo_runs/${jobId}`,
    status: {
      job_id: jobId,
      lib,
      api,
      mode: "demo",
      qwen_model: "../Qwen2.5-Coder-7B-Instruct",
      mutation_model: "facebook/incoder-1B",
      cuda_device: "0",
      status,
      stage: status === "success" ? "summary" : "qwen_seed",
      stages: {
        prompt_check: "success",
        qwen_seed: status === "pending" ? "running" : "success",
        ev_generation: status === "success" ? "success" : "pending",
        driver: status === "success" ? "success" : "pending",
        summary: status === "success" ? "success" : "pending",
      },
      error: null,
      updated_at: "2026-06-28T17:00:00",
    },
    summary: {},
    metrics: [],
    environment: {},
    result_files: {
      seed: [],
      valid: [],
      exception: [],
      crash: [],
      notarget: [],
      hangs: [],
      flaky: [],
    },
    logs: {},
  };
}

function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;
  const promise = new Promise<T>((res, rej) => {
    resolve = res;
    reject = rej;
  });

  return { promise, resolve, reject };
}

const Harness = defineComponent({
  template: `
    <div>
      <span data-testid="selected">{{ selectedApi?.api ?? "" }}</span>
      <span data-testid="detail-valid">{{ selectedApiDetail?.result_counts.valid ?? "" }}</span>
      <span data-testid="detail-loading">{{ detailLoading }}</span>
      <span data-testid="detail-error">{{ detailError ?? "" }}</span>
      <span data-testid="job-id">{{ selectedJob?.job_id ?? "" }}</span>
      <span data-testid="job-status">{{ selectedJob?.status.status ?? "" }}</span>
      <span data-testid="mode">{{ mode }}</span>
      <span data-testid="can-run">{{ canRun }}</span>
      <button type="button" data-testid="select-alpha" @click="selectApi(alpha)">alpha</button>
      <button type="button" data-testid="select-beta" @click="selectApi(beta)">beta</button>
      <button type="button" data-testid="mode-normal" @click="setMode('normal')">normal</button>
      <button type="button" data-testid="run" @click="startRun">run</button>
    </div>
  `,
  setup() {
    const run = useApiRun();
    const alpha = apiItem("torch.add", "torch", 1);
    const beta = apiItem("torch.matmul", "torch", 9);
    return { ...run, alpha, beta };
  },
});

afterEach(() => {
  vi.clearAllMocks();
  vi.useRealTimers();
});

beforeEach(() => {
  vi.useFakeTimers();
});

describe("useApiRun", () => {
  it("ignores stale selection responses and hydrates the latest job after selection", async () => {
    const alpha = deferred<ApiDetailPayload>();
    const beta = deferred<ApiDetailPayload>();

    getApiDetail.mockImplementationOnce(() => alpha.promise);
    getApiDetail.mockImplementationOnce(() => beta.promise);
    getApiJob.mockResolvedValue(jobPayload("job-beta", "torch.matmul", "torch", "success"));

    const wrapper = mount(Harness);

    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await wrapper.get('[data-testid="select-beta"]').trigger("click");

    alpha.resolve(detailItem("torch.add", "torch", "job-alpha", 1));
    await flushPromises();

    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.matmul");
    expect(wrapper.get('[data-testid="detail-loading"]').text()).toBe("true");

    beta.resolve(detailItem("torch.matmul", "torch", "job-beta", 9));
    await flushPromises();

    expect(getApiJob).toHaveBeenCalledWith("job-beta");
    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.matmul");
    expect(wrapper.get('[data-testid="detail-valid"]').text()).toBe("9");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-beta");
    expect(wrapper.get('[data-testid="job-status"]').text()).toBe("success");
    expect(wrapper.get('[data-testid="detail-loading"]').text()).toBe("false");
  });

  it("starts a run with the exact backend payload and updates the selected job", async () => {
    getApiDetail.mockResolvedValue(detailItem("torch.add", "torch", null, 2));
    getApiJob.mockResolvedValue(jobPayload("job-run", "torch.add", "torch", "success"));
    startApiRun.mockResolvedValue({ job_id: "job-run", out: "demo_runs/job-run" });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    await wrapper.get('[data-testid="mode-normal"]').trigger("click");
    await wrapper.get('[data-testid="run"]').trigger("click");
    await flushPromises();

    expect(startApiRun).toHaveBeenCalledWith({ lib: "torch", api: "torch.add", mode: "normal" });
    expect(getApiJob).toHaveBeenCalledWith("job-run");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-run");
    expect(wrapper.get('[data-testid="job-status"]').text()).toBe("success");
    expect(wrapper.get('[data-testid="can-run"]').text()).toBe("false");
  });
});
