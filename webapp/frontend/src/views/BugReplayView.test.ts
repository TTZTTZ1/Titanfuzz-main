import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

const services = vi.hoisted(() => ({
  getConfirmedBugs: vi.fn(),
  getConfirmedBug: vi.fn(),
  getCandidates: vi.fn(),
  getOverview: vi.fn(),
  getCandidate: vi.fn(),
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

describe("BugReplayView", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    services.getConfirmedBugs.mockResolvedValue([summary]);
    services.getCandidates.mockResolvedValue([]);
    services.getOverview.mockResolvedValue({ latest_repro_jobs: [] });
    services.getConfirmedBug.mockResolvedValue({
      index: summary,
      meta: summary,
      display_id: "PT-004",
      bug_dir: "reports/confirmed/PT-004",
      repro_path: "reports/confirmed/PT-004/repro.py",
      report_path: "reports/confirmed/PT-004/report.md",
      repro_code: "import torch\ntorch.sparse.mm(a, b)",
      report_markdown: "",
    });
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
    services.getOverview.mockResolvedValueOnce({
      latest_repro_jobs: [{ job_id: "repro-1", bug_id: summary.id, status: "finished" }],
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
        modes: {},
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
    const reportButton = wrapper.findAll("button").find((button) => button.text() === "查看报告");
    expect(reportButton).toBeDefined();
    await reportButton?.trigger("click");
    await flushPromises();

    expect(services.getReproReport).toHaveBeenCalledWith("repro-1");
    expect(services.generateReproReport).not.toHaveBeenCalled();
  });
});
