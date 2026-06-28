import { describe, expect, it } from "vitest";

import { stageDefinitions, type ApiRunJobLike, resolveLiveStageKey } from "./apiRun";

describe("apiRun domain", () => {
  it("keeps the visible stage definitions in the expected order", () => {
    expect(stageDefinitions).toEqual([
      { key: "qwen_seed", label: "Qwen 种子", metricKeys: [["候选", "qwen_raw"], ["有效种子", "qwen_valid"]] },
      {
        key: "ev_generation",
        label: "InCoder 变异",
        metricKeys: [
          ["有效", "valid"],
          ["异常", "exception"],
          ["崩溃", "crash"],
          ["超时", "hangs"],
        ],
      },
      {
        key: "driver",
        label: "差异检测",
        metricKeys: [
          ["已检查程序", "total_files"],
          ["差异 Catch", "trace_hits"],
          ["崩溃", "crash"],
          ["不稳定", "flaky"],
        ],
      },
    ]);
  });

  it("tracks the running backend stage as the live visible stage before completion", () => {
    const job = {
      status: {
        stage: "ev_generation",
        stages: {
          prompt_check: "success",
          qwen_seed: "success",
          ev_generation: "running",
          driver: "pending",
          summary: "pending",
        },
      },
    } satisfies ApiRunJobLike;

    expect(resolveLiveStageKey(job)).toBe("ev_generation");
  });
});
