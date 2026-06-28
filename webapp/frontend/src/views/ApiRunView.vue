<script setup lang="ts">
import { computed } from "vue";

import ApiSelector from "../components/api/ApiSelector.vue";
import RunTimeline from "../components/api/RunTimeline.vue";
import { useApiRun } from "../composables/useApiRun";

const {
  selectedApi,
  selectedApiDetail,
  selectedJob,
  detailLoading,
  detailError,
  jobLoading,
  jobError,
  runLoading,
  runError,
  mode,
  canRun,
  liveStageKey,
  metricStageKey,
  stageStates,
  metrics,
  resultFiles,
  logs,
  summaryCounts,
  selectApi,
  clearSelection,
  retrySelection,
  setMode,
  selectMetricStage,
  startRun,
} = useApiRun();

const selectedApiLabel = computed(() => selectedApiDetail.value?.api ?? selectedApi.value?.api ?? "");
const latestJobState = computed(() => selectedJob.value?.status.status ?? selectedApiDetail.value?.latest_job?.status ?? "无");
const countsSummary = computed(() => {
  const counts = summaryCounts.value;
  if (counts === null) {
    return "";
  }

  return [
    `候选 ${counts.seed}`,
    `有效 ${counts.valid}`,
    `异常 ${counts.exception}`,
    `崩溃 ${counts.crash}`,
    `超时 ${counts.hangs}`,
    `不稳定 ${counts.flaky}`,
  ].join(" · ");
});

function handleLibraryChange() {
  clearSelection();
}
</script>

<template>
  <section class="api-run-view" aria-labelledby="api-run-view-title">
    <header class="api-run-view__hero">
      <p class="api-run-view__eyebrow">TensorGuard</p>
      <h1 id="api-run-view-title" class="api-run-view__title">单 API 安全检测</h1>
      <p class="api-run-view__summary">
        通过 API 搜索、模式切换、运行状态和阶段轨迹查看单个 API 的检测过程。
      </p>
    </header>

    <div class="api-run-view__body">
      <section class="api-run-view__control-band" aria-labelledby="api-run-controls-title">
        <div class="api-run-view__section-head">
          <h2 id="api-run-controls-title" class="api-run-view__section-title">选择与运行</h2>
          <button type="button" class="api-run-view__run" :disabled="!canRun" @click="startRun">运行</button>
        </div>

        <ApiSelector :selected="selectedApi" @select="selectApi" @library-change="handleLibraryChange" />

        <div class="api-run-view__mode" role="radiogroup" aria-label="运行模式">
          <button
            type="button"
            role="radio"
            class="api-run-view__mode-btn"
            :class="{ 'api-run-view__mode-btn--active': mode === 'demo' }"
            :aria-checked="mode === 'demo'"
            @click="setMode('demo')"
          >
            demo
          </button>
          <button
            type="button"
            role="radio"
            class="api-run-view__mode-btn"
            :class="{ 'api-run-view__mode-btn--active': mode === 'normal' }"
            :aria-checked="mode === 'normal'"
            @click="setMode('normal')"
          >
            normal
          </button>
        </div>
      </section>

      <aside class="api-run-view__summary-panel" aria-labelledby="api-run-summary-title">
        <div class="api-run-view__section-head">
          <h2 id="api-run-summary-title" class="api-run-view__section-title">当前状态</h2>
        </div>

        <div v-if="selectedApi === null" class="api-run-view__state">
          请选择一个 API 后查看最新结果。
        </div>
        <div v-else-if="detailLoading || jobLoading || runLoading" class="api-run-view__state">
          正在读取 API 详情。
        </div>
        <div v-else-if="detailError || jobError || runError" class="api-run-view__state api-run-view__state--error">
          <p class="api-run-view__state-copy">{{ detailError ?? jobError ?? runError }}</p>
          <button type="button" class="api-run-view__retry" @click="retrySelection">重试</button>
        </div>
        <dl v-else class="api-run-view__summary-list">
          <div class="api-run-view__summary-item">
            <dt>API</dt>
            <dd>{{ selectedApiLabel }}</dd>
          </div>
          <div class="api-run-view__summary-item">
            <dt>结果</dt>
            <dd>{{ countsSummary || "暂无结果" }}</dd>
          </div>
          <div class="api-run-view__summary-item">
            <dt>最新作业</dt>
            <dd>{{ latestJobState }}</dd>
          </div>
        </dl>
      </aside>
    </div>

    <RunTimeline
      :stages="stageStates"
      :metric-stage-key="metricStageKey"
      :live-stage-key="liveStageKey"
      :metrics="metrics"
      :logs="logs"
      :result-files="resultFiles"
      @select-metric-stage="selectMetricStage"
    />
  </section>
</template>

<style scoped>
.api-run-view {
  display: grid;
  gap: 1rem;
}

.api-run-view__hero {
  display: grid;
  gap: 0.35rem;
}

.api-run-view__eyebrow {
  margin: 0;
  color: var(--tg-text-soft);
  font-size: 0.82rem;
}

.api-run-view__title {
  margin: 0;
  font-size: 1.8rem;
  line-height: 1.15;
  color: var(--tg-text-strong);
}

.api-run-view__summary {
  margin: 0;
  max-width: 48rem;
  color: var(--tg-text-muted);
}

.api-run-view__body {
  display: grid;
  gap: 1rem;
}

.api-run-view__control-band,
.api-run-view__summary-panel {
  display: grid;
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 1rem;
}

.api-run-view__section-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
}

.api-run-view__section-title {
  margin: 0;
  font-size: 1rem;
  color: var(--tg-text-strong);
}

.api-run-view__run {
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: var(--tg-action);
  color: #ffffff;
  padding: 0.55rem 0.9rem;
}

.api-run-view__run:disabled {
  opacity: 0.45;
}

.api-run-view__mode {
  display: flex;
  gap: 0.45rem;
}

.api-run-view__mode-btn {
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: #ffffff;
  color: var(--tg-text-muted);
  padding: 0.5rem 0.8rem;
}

.api-run-view__mode-btn--active {
  border-color: rgba(25, 86, 209, 0.35);
  background: var(--tg-action-soft);
  color: var(--tg-action);
}

.api-run-view__state {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  padding: 0.95rem;
}

.api-run-view__state--error {
  background: var(--tg-red-bg);
  border-color: var(--tg-red-border);
  color: var(--tg-red-text);
  display: grid;
  gap: 0.65rem;
}

.api-run-view__state-copy {
  margin: 0;
}

.api-run-view__retry {
  justify-self: start;
  border: 1px solid currentColor;
  border-radius: 999px;
  background: #ffffff;
  color: inherit;
  padding: 0.45rem 0.85rem;
}

.api-run-view__summary-list {
  display: grid;
  gap: 0.65rem;
  margin: 0;
}

.api-run-view__summary-item {
  display: grid;
  gap: 0.2rem;
}

.api-run-view__summary-item dt {
  color: var(--tg-text-soft);
  font-size: 0.82rem;
}

.api-run-view__summary-item dd {
  margin: 0;
  color: var(--tg-text-strong);
}

@media (min-width: 960px) {
  .api-run-view__body {
    grid-template-columns: minmax(0, 1.02fr) minmax(22rem, 0.98fr);
    align-items: start;
  }
}
</style>
