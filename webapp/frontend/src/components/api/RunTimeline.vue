<script setup lang="ts">
import { computed } from "vue";

import {
  stageDefinitions,
  timelineStages,
  type ApiRunStageKey,
  type ApiTimelineStageKey,
} from "../../domain/apiRun";
import type { ApiJobMetric, ApiResultFile, ApiStageStatus, ResultCategory } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    stages: Record<ApiTimelineStageKey, ApiStageStatus>;
    metricStageKey: ApiRunStageKey;
    liveStageKey: ApiRunStageKey;
    metrics?: ApiJobMetric[];
    logs?: Record<string, string>;
    resultFiles?: Record<ResultCategory, ApiResultFile[]>;
  }>(),
  {
    metrics: () => [],
    logs: () => ({}),
    resultFiles: () => ({
      seed: [],
      valid: [],
      exception: [],
      crash: [],
      notarget: [],
      hangs: [],
      flaky: [],
    }),
  },
);

const emit = defineEmits<{
  selectMetricStage: [ApiRunStageKey];
}>();

const stageDefinitionByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition]));

const selectedDefinition = computed(() => stageDefinitionByKey[props.metricStageKey]);
const selectedMetrics = computed(() => props.metrics.filter((metric) => metric.stage === props.metricStageKey));
const latestMetric = computed(() => selectedMetrics.value[selectedMetrics.value.length - 1] ?? null);
const visibleResultFiles = computed(() =>
  Object.entries(props.resultFiles).filter(([, files]) => files.length > 0) as Array<[ResultCategory, ApiResultFile[]]>,
);
const logEntries = computed(() => Object.entries(props.logs).filter(([, value]) => value.trim().length > 0));

function isSelectable(key: ApiRunStageKey): boolean {
  const state = props.stages[key];
  return state === "success" || state === "failed";
}

function displayValue(key: string): string {
  if (latestMetric.value === null) {
    return "";
  }

  const value = latestMetric.value[key as keyof typeof latestMetric.value];
  return value === null || value === undefined ? "" : String(value);
}
</script>

<template>
  <section class="run-timeline" aria-labelledby="run-timeline-title">
    <header class="run-timeline__header">
      <div>
        <p class="run-timeline__eyebrow">阶段轨迹</p>
        <h2 id="run-timeline-title" class="run-timeline__title">运行链路</h2>
      </div>
      <p class="run-timeline__summary">
        {{ liveStageKey === metricStageKey ? "当前面板跟随运行阶段" : "当前面板保留手动选择" }}
      </p>
    </header>

    <ol class="run-timeline__rail" aria-label="五阶段流水线">
      <li
        v-for="stage in timelineStages"
        :key="stage.key"
        class="run-timeline__rail-item"
        :class="[`run-timeline__rail-item--${stages[stage.key]}`]"
      >
        <span class="run-timeline__rail-label">{{ stage.label }}</span>
        <span class="run-timeline__rail-status">{{ stages[stage.key] }}</span>
      </li>
    </ol>

    <div class="run-timeline__tabs" role="tablist" aria-label="指标阶段">
      <button
        v-for="definition in stageDefinitions"
        :key="definition.key"
        type="button"
        role="tab"
        class="run-timeline__tab"
        :class="{
          'run-timeline__tab--active': metricStageKey === definition.key,
          'run-timeline__tab--live': liveStageKey === definition.key,
        }"
        :aria-selected="metricStageKey === definition.key"
        :disabled="!isSelectable(definition.key)"
        @click="emit('selectMetricStage', definition.key)"
      >
        <span>{{ definition.label }}</span>
      </button>
    </div>

    <div class="run-timeline__panel">
      <div v-if="latestMetric" class="run-timeline__metrics">
        <div class="run-timeline__metrics-head">
          <p class="run-timeline__metrics-title">{{ selectedDefinition.label }}</p>
          <p class="run-timeline__metrics-stage">{{ latestMetric.stage }}</p>
        </div>

        <dl class="run-timeline__metric-grid">
          <div v-for="[label, key] in selectedDefinition.metricKeys" :key="key" class="run-timeline__metric-item">
            <dt class="run-timeline__metric-label">{{ label }}</dt>
            <dd class="run-timeline__metric-value">{{ displayValue(key) }}</dd>
          </div>
        </dl>
      </div>

      <p v-else class="run-timeline__empty">暂无阶段指标</p>

      <div v-if="visibleResultFiles.length > 0" class="run-timeline__result-files">
        <div v-for="[category, files] in visibleResultFiles" :key="category" class="run-timeline__result-group">
          <p class="run-timeline__result-label">{{ category }}</p>
          <p class="run-timeline__result-value">{{ files.length }} 个文件</p>
        </div>
      </div>

      <div v-if="logEntries.length > 0" class="run-timeline__logs">
        <div v-for="[name, value] in logEntries" :key="name" class="run-timeline__log">
          <p class="run-timeline__log-name">{{ name }}</p>
          <pre class="run-timeline__log-body">{{ value }}</pre>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.run-timeline {
  display: grid;
  gap: 0.9rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 1rem;
}

.run-timeline__header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
}

.run-timeline__eyebrow {
  margin: 0;
  color: var(--tg-text-soft);
  font-size: 0.82rem;
}

.run-timeline__title {
  margin: 0.2rem 0 0;
  font-size: 1.15rem;
  color: var(--tg-text-strong);
}

.run-timeline__summary {
  margin: 0;
  color: var(--tg-text-muted);
  font-size: 0.92rem;
}

.run-timeline__rail {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.5rem;
}

.run-timeline__rail-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  padding: 0.65rem 0.8rem;
  background: var(--tg-surface-muted);
}

.run-timeline__rail-item--running {
  border-color: rgba(25, 86, 209, 0.35);
  background: var(--tg-action-soft);
}

.run-timeline__rail-item--success {
  border-color: rgba(43, 136, 73, 0.25);
}

.run-timeline__rail-item--failed {
  border-color: rgba(196, 43, 28, 0.28);
}

.run-timeline__rail-label {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.run-timeline__rail-status {
  flex: none;
  color: var(--tg-text-soft);
  text-transform: lowercase;
}

.run-timeline__tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.run-timeline__tab {
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: #ffffff;
  color: var(--tg-text-muted);
  padding: 0.5rem 0.8rem;
}

.run-timeline__tab--active {
  border-color: rgba(25, 86, 209, 0.35);
  background: var(--tg-action-soft);
  color: var(--tg-action);
}

.run-timeline__tab--live {
  box-shadow: inset 0 0 0 1px rgba(25, 86, 209, 0.16);
}

.run-timeline__tab:disabled {
  opacity: 0.45;
}

.run-timeline__panel {
  display: grid;
  gap: 0.9rem;
}

.run-timeline__metrics-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.6rem;
}

.run-timeline__metrics-title,
.run-timeline__metrics-stage,
.run-timeline__empty,
.run-timeline__result-label,
.run-timeline__result-value,
.run-timeline__log-name {
  margin: 0;
}

.run-timeline__metrics-title {
  color: var(--tg-text-strong);
  font-weight: 600;
}

.run-timeline__metrics-stage {
  color: var(--tg-text-soft);
  text-transform: uppercase;
  font-size: 0.82rem;
}

.run-timeline__metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr));
  gap: 0.6rem;
}

.run-timeline__metric-item {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  padding: 0.7rem 0.8rem;
  background: var(--tg-surface-muted);
}

.run-timeline__metric-label {
  color: var(--tg-text-soft);
  font-size: 0.82rem;
}

.run-timeline__metric-value {
  margin: 0.25rem 0 0;
  color: var(--tg-text-strong);
  font-weight: 600;
}

.run-timeline__empty {
  color: var(--tg-text-muted);
}

.run-timeline__result-files,
.run-timeline__logs {
  display: grid;
  gap: 0.5rem;
}

.run-timeline__result-group,
.run-timeline__log {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  padding: 0.7rem 0.8rem;
  background: var(--tg-surface-muted);
}

.run-timeline__result-label,
.run-timeline__log-name {
  color: var(--tg-text-soft);
  font-size: 0.82rem;
}

.run-timeline__result-value {
  color: var(--tg-text-strong);
  font-weight: 600;
}

.run-timeline__log-body {
  margin: 0.35rem 0 0;
  white-space: pre-wrap;
  color: var(--tg-text);
}

@media (max-width: 720px) {
  .run-timeline__header {
    flex-direction: column;
    align-items: start;
  }
}
</style>
