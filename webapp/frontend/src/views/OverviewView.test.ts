import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import CoverageBaseline from "../components/overview/CoverageBaseline.vue";
import ConfirmedEvidenceList from "../components/overview/ConfirmedEvidenceList.vue";
import type { Library, OverviewPayload, OverviewResultSummary, OverviewSources } from "../types/tensorguard";

const { getOverview, getConfirmedBugs } = vi.hoisted(() => ({
  getOverview: vi.fn(),
  getConfirmedBugs: vi.fn(),
}));

vi.mock("../services/tensorguard", () => ({
  getOverview,
  getConfirmedBugs,
}));

import OverviewView from "./OverviewView.vue";

const overviewPayload = {
  api_total: 4608,
  api_by_lib: { torch: 1568, tf: 3040 },
  prompt_ready_total: 0,
  prompt_ready_by_lib: { torch: 0, tf: 0 },
  paper_bug_total: 14,
  paper_bug_by_framework: { PyTorch: 5, TensorFlow: 9 },
  results: {
    torch: {
      path: "",
      exists: false,
      api_count: 0,
      counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
      trace_path: "",
      trace_exists: false,
      trace_hits: 0,
    },
    tf: {
      path: "",
      exists: false,
      api_count: 0,
      counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
      trace_path: "",
      trace_exists: false,
      trace_hits: 0,
    },
  } satisfies Record<Library, OverviewResultSummary>,
  latest_api_jobs: [],
  latest_repro_jobs: [],
  sources: {
    torch_api_list: "",
    tf_api_list: "",
    prompt_library: "",
    api_jobs: "",
    repro_jobs: "",
  } satisfies OverviewSources,
} satisfies OverviewPayload;

afterEach(() => {
  getOverview.mockReset();
  getConfirmedBugs.mockReset();
});

describe("OverviewView", () => {
  it("renders live overview payload and confirmed bugs", async () => {
    getOverview.mockResolvedValueOnce(overviewPayload);
    getConfirmedBugs.mockResolvedValueOnce([
      {
        id: "PAPER-PT-004",
        display_id: "PT-004",
        api: "torch.sparse.mm",
        bug_type: "Crash / allocator corruption",
        status: "confirmed",
      },
    ]);

    const wrapper = mount(OverviewView);
    await flushPromises();

    expect(wrapper.text()).toContain("框架安全检测概览");
    expect(wrapper.text()).toContain("4,608");
    expect(wrapper.text()).toContain("1,568");
    expect(wrapper.text()).toContain("3,040");
    expect(wrapper.text()).toContain("PT-004");
    expect(wrapper.text()).not.toContain("PAPER-PT-004");
  });

  it("renders zero-total coverage as 0% without infinities", () => {
    const wrapper = mount(CoverageBaseline, {
      props: {
        overview: {
          api_total: 0,
          api_by_lib: { torch: 0, tf: 0 },
          prompt_ready_total: 0,
          prompt_ready_by_lib: { torch: 0, tf: 0 },
          paper_bug_total: 0,
          paper_bug_by_framework: {},
          results: {
            torch: {
              path: "",
              exists: false,
              api_count: 0,
              counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
              trace_path: "",
              trace_exists: false,
              trace_hits: 0,
            },
            tf: {
              path: "",
              exists: false,
              api_count: 0,
              counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
              trace_path: "",
              trace_exists: false,
              trace_hits: 0,
            },
          } satisfies Record<Library, OverviewResultSummary>,
          latest_api_jobs: [],
          latest_repro_jobs: [],
          sources: {
            torch_api_list: "",
            tf_api_list: "",
            prompt_library: "",
            api_jobs: "",
            repro_jobs: "",
          } satisfies OverviewSources,
        } satisfies OverviewPayload,
        environmentSummary: "环境信息暂不可用",
      },
    });

    expect(wrapper.text()).toContain("0%");
    expect(wrapper.text()).not.toContain("NaN");
    expect(wrapper.text()).not.toContain("Infinity");
  });

  it("suppresses raw PAPER ids and fake severity labels in confirmed evidence rows", () => {
    const wrapper = mount(ConfirmedEvidenceList, {
      props: {
        bugs: [
          {
            display_id: "PT-004",
            api: "torch.sparse.mm",
            bug_type: "Crash / allocator corruption",
            status: "confirmed",
          },
        ],
      },
    });

    const text = wrapper.text();

    expect(text).toContain("PT-004");
    expect(text).toContain("torch.sparse.mm");
    expect(text).toContain("Crash / allocator corruption");
    expect(text).not.toContain("PAPER-PT-004");
    expect(text).not.toMatch(/\bpaper\b/i);
    expect(text).not.toContain("论文");
    expect(text).not.toMatch(/\b(High|Medium|Low)\b/);
  });
});
