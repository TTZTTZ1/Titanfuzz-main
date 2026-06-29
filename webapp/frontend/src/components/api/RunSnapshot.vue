<script setup lang="ts">
import { computed } from "vue";

import { stageDefinitions, type ApiRunStageKey } from "../../domain/apiRun";
import type { ApiJobMetric, ApiJobStatus, ApiRunMode } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    apiLabel: string;
    mode: ApiRunMode;
    liveStageKey: ApiRunStageKey;
    jobStatus: ApiJobStatus | null;
    latestMetric: ApiJobMetric | null;
  }>(),
  {
    jobStatus: null,
    latestMetric: null,
  },
);

const headingId = `run-snapshot-${Math.random().toString(36).slice(2, 10)}`;
const stageLabelByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition.label]));

const hasLiveData = computed(() => props.jobStatus !== null || props.latestMetric !== null);
const liveStatus = computed(() => props.jobStatus?.status ?? "无");
const stageLabel = computed(() => {
  if (!hasLiveData.value) {
    return "暂无";
  }

  if (props.latestMetric !== null) {
    return stageLabelByKey[props.latestMetric.stage] || props.latestMetric.stage;
  }

  return stageLabelByKey[props.liveStageKey] || props.liveStageKey;
});
const elapsedText = computed(() => {
  if (props.latestMetric === null) {
    return "暂无";
  }

  return `${props.latestMetric.elapsed_seconds}s`;
});
const qwenModel = computed(() => props.jobStatus?.qwen_model?.trim() || "");
const mutationModel = computed(() => props.jobStatus?.mutation_model?.trim() || "");

const rows = computed(() => {
  const baseRows = [
    ["当前阶段", stageLabel.value],
    ["当前状态", liveStatus.value],
    ["最新耗时", elapsedText.value],
    ["运行模式", props.mode],
  ] as const;

  const extraRows = [
    qwenModel.value ? (["Qwen 模型", qwenModel.value] as const) : null,
    mutationModel.value ? (["变异模型", mutationModel.value] as const) : null,
  ].filter(Boolean) as Array<readonly [string, string]>;

  return [...baseRows, ...extraRows];
});
</script>

<template>
  <section class="run-snapshot" :aria-labelledby="headingId">
    <header class="run-snapshot__header">
      <span class="run-snapshot__icon">LIVE</span>
      <div class="run-snapshot__heading"><h2 :id="headingId" class="run-snapshot__title">实时摘要</h2><p>{{ apiLabel || "当前任务采样" }}</p></div>
    </header>

    <dl class="run-snapshot__grid">
      <div v-for="[label, value] in rows" :key="label" class="run-snapshot__item">
        <dt class="run-snapshot__label">{{ label }}</dt>
        <dd class="run-snapshot__value">{{ value }}</dd>
      </div>
    </dl>
  </section>
</template>

<style scoped>
.run-snapshot {
  display: grid;
  gap: 0.7rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.85rem;
  box-shadow: var(--tg-shadow);
  min-width: 0;
}

.run-snapshot__header {
  display: flex;
  align-items: center;
  gap: 0.55rem;
}

.run-snapshot__heading {
  display: grid;
  gap: 0.12rem;
}

.run-snapshot__icon {
  width: 1.8rem;
  height: 1.8rem;
  display: grid;
  place-items: center;
  border-radius: 6px;
  background: var(--tg-action-soft);
  color: var(--tg-action-strong);
  box-shadow: inset 0 0 0 1px #d6e4ff;
  font: 800 0.43rem/1 ui-monospace, monospace;
}

.run-snapshot__title {
  margin: 0;
  font-size: 0.72rem;
  color: var(--tg-text-strong);
  word-break: break-word;
}

.run-snapshot__heading p { margin: 0; max-width: 12rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--tg-text-muted); font-size: 0.48rem; }

.run-snapshot__grid {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1px;
  border: 1px solid var(--tg-border);
  background: var(--tg-border);
}

.run-snapshot__item {
  margin: 0;
  background: #fff;
  padding: 0.55rem;
  min-width: 0;
}

.run-snapshot__label {
  margin: 0 0 0.2rem;
  font-size: 0.48rem;
  color: var(--tg-text-soft);
}

.run-snapshot__value {
  margin: 0;
  color: var(--tg-text-strong);
  word-break: break-word;
  font-size: 0.64rem;
  font-weight: 720;
}

@media (max-width: 720px) {
  .run-snapshot__grid {
    grid-template-columns: 1fr;
  }
}
</style>
