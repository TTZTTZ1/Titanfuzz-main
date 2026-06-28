import type { ApiJobPayload, ApiJobStatus, ApiPipelineStage, ApiStage, ApiStageStatus } from "../types/tensorguard";

export const stageDefinitions = [
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
] as const;

export type ApiRunStageKey = (typeof stageDefinitions)[number]["key"];

export const timelineStages = [
  { key: "prompt_check", label: "约束检查" },
  { key: "qwen_seed", label: "Qwen" },
  { key: "ev_generation", label: "InCoder" },
  { key: "driver", label: "CPU/GPU difference" },
  { key: "summary", label: "summary" },
] as const;

export type ApiTimelineStageKey = (typeof timelineStages)[number]["key"];

type StageMap = Record<ApiPipelineStage, ApiStageStatus>;

export interface ApiRunJobLike {
  status: Pick<ApiJobStatus, "stage" | "stages"> &
    Partial<Pick<ApiJobStatus, "status">> & {
    stage: ApiStage;
    stages: StageMap;
  };
  metrics?: ApiJobPayload["metrics"];
  result_files?: ApiJobPayload["result_files"];
  logs?: ApiJobPayload["logs"];
}

const liveStageOrder: ApiRunStageKey[] = ["qwen_seed", "ev_generation", "driver"];

function isVisibleStageKey(value: ApiStage): value is ApiRunStageKey {
  return liveStageOrder.includes(value as ApiRunStageKey);
}

function isActiveStage(status: ApiStageStatus): boolean {
  return status === "running" || status === "success" || status === "failed";
}

export function resolveLiveStageKey(job: ApiRunJobLike): ApiRunStageKey {
  const stage = job.status.stage;
  if (isVisibleStageKey(stage)) {
    return stage;
  }

  for (let index = liveStageOrder.length - 1; index >= 0; index -= 1) {
    const key = liveStageOrder[index];
    if (isActiveStage(job.status.stages[key])) {
      return key;
    }
  }

  return "qwen_seed";
}
