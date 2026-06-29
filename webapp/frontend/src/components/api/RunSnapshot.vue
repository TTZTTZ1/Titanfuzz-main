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
    ["API", props.apiLabel || "未选择"],
    ["模式", props.mode],
    ["当前阶段", stageLabel.value],
    ["当前状态", liveStatus.value],
    ["最新耗时", elapsedText.value],
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
      <div class="run-snapshot__heading">
        <p class="run-snapshot__eyebrow">实时概览</p>
        <h2 :id="headingId" class="run-snapshot__title">{{ apiLabel || "未选择 API" }}</h2>
      </div>
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
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.95rem;
  min-width: 0;
}

.run-snapshot__header {
  display: flex;
  align-items: start;
  justify-content: space-between;
  gap: 1rem;
}

.run-snapshot__heading {
  display: grid;
  gap: 0.15rem;
}

.run-snapshot__eyebrow {
  margin: 0;
  font-size: 0.8rem;
  color: var(--tg-text-soft);
}

.run-snapshot__title {
  margin: 0;
  font-size: 1rem;
  color: var(--tg-text-strong);
  word-break: break-word;
}

.run-snapshot__grid {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.7rem;
}

.run-snapshot__item {
  margin: 0;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  padding: 0.75rem 0.8rem;
  min-width: 0;
}

.run-snapshot__label {
  margin: 0 0 0.2rem;
  font-size: 0.78rem;
  color: var(--tg-text-soft);
}

.run-snapshot__value {
  margin: 0;
  color: var(--tg-text-strong);
  word-break: break-word;
}

@media (max-width: 720px) {
  .run-snapshot__grid {
    grid-template-columns: 1fr;
  }
}
</style>
