import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

const services = vi.hoisted(() => ({
  getConfirmedBugs: vi.fn(),
  getConfirmedBug: vi.fn(),
  getCandidates: vi.fn(),
  getCandidateClusters: vi.fn(),
  getOverview: vi.fn(),
  getEnvironment: vi.fn(),
  getCandidate: vi.fn(),
  getCandidateCluster: vi.fn(),
  updateCandidateClusterStatus: vi.fn(),
  reproduceConfirmedBug: vi.fn(),
  getReproJob: vi.fn(),
  getReproReport: vi.fn(),
  generateReproReport: vi.fn(),
}));

vi.mock("../services/tensorguard", () => services);

import BugReplayView from "./BugReplayView.vue";

const summary = {
  id: "PAPER-PT-004",
  display_id: "PT-004",
  title: "Malformed sparse tensor triggers invalid free",
  framework: "PyTorch",
  api: "torch.sparse.mm",
  related_apis: [],
  bug_type: "allocator corruption",
  status: "confirmed",
  source: { document: "internal", section: "appendix" },
  trigger: "malformed sparse structure",
  expected: "Reject invalid sparse indices with a Python exception.",
  observed: "The child process aborts with SIGABRT.",
  reproducible: true,
  minimized: true,
  files: { repro: "repro.py", report: "report.md" },
  tags: ["sparse"],
  path: "reports/confirmed/PT-004",
  meta_path: "reports/confirmed/PT-004/meta.json",
};

const candidateCluster = {
  cluster_id: "torch_quantile_exception_mismatch_001",
  lib: "torch",
  api: "torch.quantile",
  job_id: "api_torch_quantile_1",
  category: "exception",
  bug_pattern: "CPU/GPU exception mismatch / CUDA device-side assert",
  cluster_status: "needs_minimize",
  confidence: "high",
  member_count: 37,
  excluded_count: 5,
  representative: {
    candidate_id: "CAND-0001",
    source_path: "demo_runs/api_jobs/api_torch_quantile_1/Results/torch/exception/torch.quantile_1.py",
    source_name: "torch.quantile_1.py",
    error_summary: "CPU RuntimeError GPU CUDA device-side assert triggered",
    score: 0.95,
  },
  created_at: "2026-06-30T10:00:00+08:00",
  updated_at: "2026-06-30T10:00:00+08:00",
};

const candidateClusterDetail = {
  ...candidateCluster,
  members: [
    {
      candidate_id: "CAND-0001",
      source_path: "demo_runs/api_jobs/api_torch_quantile_1/Results/torch/exception/torch.quantile_1.py",
      source_name: "torch.quantile_1.py",
      error_summary: "CPU RuntimeError GPU CUDA device-side assert triggered",
      score: 0.95,
      status: "pending_review",
    },
  ],
  excluded: [
    {
      candidate_id: "CAND-0002",
      source_path: "demo_runs/api_jobs/api_torch_quantile_1/Results/torch/exception/torch.quantile_2.py",
      source_name: "torch.quantile_2.py",
      reason: "generated_code_error",
      error_summary: "SyntaxError: unterminated triple-quoted string literal",
    },
  ],
  representative_source_code: "import torch\nq = torch.tensor([1.0, 2.5])\ntorch.quantile(torch.ones(4), q)",
  minimization_draft: "import torch\n# TODO: minimize candidate\n",
};

describe("BugReplayView", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    services.getConfirmedBugs.mockResolvedValue([summary]);
    services.getCandidates.mockResolvedValue([]);
    services.getCandidateClusters.mockResolvedValue([candidateCluster]);
    services.getOverview.mockResolvedValue({ latest_repro_jobs: [] });
    services.getEnvironment.mockResolvedValue({
      collected_at: "2026-06-30T10:00:00+08:00",
      platform: { system: "Linux", release: "6.8", machine: "x86_64" },
      python: { version: "3.10.20", executable: "/env/bin/python" },
      frameworks: {
        torch: { installed: true, version: "2.11.0+cu130" },
        tensorflow: { installed: true, version: "2.21.0" },
      },
      cuda: { available: true, driver_version: "590.00" },
      gpus: [{ index: 0, name: "NVIDIA GeForce RTX 5090", driver_version: "590.00", memory_total_mib: 32640 }],
      warnings: [],
    });
    services.getConfirmedBug.mockResolvedValue({
      index: summary,
      meta: summary,
      display_id: "PT-004",
      bug_dir: "reports/confirmed/PT-004",
      repro_path: "reports/confirmed/PT-004/repro.py",
      report_path: "reports/confirmed/PT-004/report.md",
      repro_code: "import torch\ntorch.sparse.mm(a, b)",
      report_markdown: "",
      latest_repro_job_id: null,
    });
    services.getCandidateCluster.mockResolvedValue(candidateClusterDetail);
    services.updateCandidateClusterStatus.mockResolvedValue({ ...candidateCluster, cluster_status: "needs_minimize" });
  });

  it("shows current environment before any reproduction has run", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    expect(services.getEnvironment).toHaveBeenCalledTimes(1);
    expect(wrapper.text()).toContain("当前环境");
    expect(wrapper.text()).toContain("NVIDIA GeForce RTX 5090");
    expect(wrapper.text()).toContain("3.10.20");
    expect(wrapper.text()).toContain("等待当前环境复现");
  });

  it("renders the approved evidence workbench from live confirmed-bug data", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    expect(wrapper.get(".bug-replay-view__page-symbol").text()).toBe("!");
    expect(wrapper.findAll(".bug-replay-view__layout")).toHaveLength(1);
    expect(wrapper.text()).toContain("PT-004");
    expect(wrapper.text()).toContain("torch.sparse.mm");
    expect(wrapper.text()).toContain("Reject invalid sparse indices");
    expect(wrapper.text()).toContain("SIGABRT");
    expect(wrapper.text()).not.toContain("PAPER");
    expect(wrapper.text()).not.toContain("严重性");
  });

  it("filters the evidence list without discarding the selected detail", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    await wrapper.get('input[type="search"]').setValue("not-found");
    expect(wrapper.text()).toContain("未找到匹配证据");
    expect(wrapper.text()).toContain("torch.sparse.mm");
  });

  it("reuses an existing current-environment report instead of generating over it", async () => {
    services.getConfirmedBug.mockResolvedValueOnce({
      index: summary,
      meta: summary,
      display_id: "PT-004",
      bug_dir: "reports/confirmed/PT-004",
      repro_path: "reports/confirmed/PT-004/repro.py",
      report_path: "reports/confirmed/PT-004/report.md",
      repro_code: "import torch\ntorch.sparse.mm(a, b)",
      report_markdown: "",
      latest_repro_job_id: "repro-1",
    });
    services.getReproJob.mockResolvedValueOnce({
      job_id: "repro-1",
      out: "demo_runs/repro-1",
      status: {
        job_id: "repro-1",
        bug_id: summary.id,
        status: "finished",
        started_at: "2026-06-29T08:00:00",
        updated_at: "2026-06-29T08:00:02",
        out: "demo_runs/repro-1",
        timeout_seconds: 60,
        modes: {
          "gpu:0": {
            status: "finished",
            returncode: -6,
            timed_out: false,
            log: "gpu:0.log",
            started_at: "2026-06-29T08:00:00",
            finished_at: "2026-06-29T08:00:02",
            execution_profile: "visible_gpu_0",
            actual_device: "cuda:0",
            evidence: {
              verdict: "reproduced",
              outcome: "signal",
              reason: "SIGABRT reproduced",
              signal: "SIGABRT",
              signal_number: 6,
            },
          },
        },
        report: "report.md",
        error: null,
      },
      logs: {},
      environment: {},
      report_exists: true,
      report_path: "demo_runs/repro-1/report.md",
      report_markdown: "# current environment evidence",
    });
    services.getReproReport.mockResolvedValueOnce({
      job_id: "repro-1",
      report_path: "demo_runs/repro-1/report.md",
      report_markdown: "# current environment evidence",
      immutable: true,
    });

    const wrapper = mount(BugReplayView);
    await flushPromises();

    expect(wrapper.text()).toContain("报告已归档");
    expect(wrapper.text()).toContain("当前环境复现成功");
    expect(services.getReproJob).toHaveBeenCalledWith("repro-1");
    const reportButton = wrapper.findAll("button").find((button) => button.text() === "查看报告");
    expect(reportButton).toBeDefined();
    await reportButton?.trigger("click");
    await flushPromises();

    expect(services.getReproReport).toHaveBeenCalledWith("repro-1");
    expect(services.generateReproReport).not.toHaveBeenCalled();
  });

  it("renders searchable candidate clusters instead of raw candidate files", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    expect(candidateTab).toBeDefined();
    await candidateTab?.trigger("click");
    await flushPromises();

    expect(services.getCandidateClusters).toHaveBeenCalledTimes(1);
    expect(services.getCandidateCluster).toHaveBeenCalledWith(candidateCluster.cluster_id);
    expect(wrapper.text()).toContain("CPU/GPU exception mismatch");
    expect(wrapper.text()).toContain("同类程序 37");
    expect(wrapper.text()).toContain("已过滤 5");
    expect(wrapper.text()).toContain("聚类依据");
    expect(wrapper.text()).toContain("人工整理 repro.py");

    await wrapper.get('input[type="search"]').setValue("device assert");
    expect(wrapper.text()).toContain("torch.quantile");
    await wrapper.get('input[type="search"]').setValue("sparse");
    expect(wrapper.text()).toContain("暂无候选簇");
  });

  it("updates candidate cluster review state from the review actions", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    await candidateTab?.trigger("click");
    await flushPromises();

    const reproducedButton = wrapper.findAll("button").find((button) => button.text() === "标记可复现");
    expect(reproducedButton).toBeDefined();
    await reproducedButton?.trigger("click");
    await flushPromises();

    expect(services.updateCandidateClusterStatus).toHaveBeenCalledWith(candidateCluster.cluster_id, {
      status: "reproduced",
      note: "人工标记为可复现",
    });
    expect(services.getCandidateClusters).toHaveBeenCalledTimes(2);
  });
});
