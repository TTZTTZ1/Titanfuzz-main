<script setup lang="ts">
import { computed } from "vue";

import ApiSelector from "../components/api/ApiSelector.vue";
import GpuChart from "../components/api/GpuChart.vue";
import LiveLog from "../components/api/LiveLog.vue";
import ResultComposition from "../components/api/ResultComposition.vue";
import RunSnapshot from "../components/api/RunSnapshot.vue";
import RunTimeline from "../components/api/RunTimeline.vue";
import StageChart from "../components/api/StageChart.vue";
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
  pollError,
  mode,
  canRun,
  liveStageKey,
  metricStageKey,
  stageStates,
  metrics,
  resultFiles,
  logs,
  summaryCounts,
  retryPollingNow,
  selectApi,
  clearSelection,
  retrySelection,
  setMode,
  selectMetricStage,
  startRun,
} = useApiRun();

const selectedApiLabel = computed(() => selectedApiDetail.value?.api ?? selectedApi.value?.api ?? "");
const selectedJobStatus = computed(() => selectedJob.value?.status ?? null);
const latestMetric = computed(() => selectedJob.value?.metrics?.at(-1) ?? null);

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

      <RunTimeline
        :stages="stageStates"
        :metric-stage-key="metricStageKey"
        :live-stage-key="liveStageKey"
        :metrics="metrics"
        :logs="logs"
        :result-files="resultFiles"
        @select-metric-stage="selectMetricStage"
      />

      <section class="api-run-view__visual-grid" aria-label="阶段图表与摘要">
        <StageChart :metrics="metrics" :stage-key="metricStageKey" />
        <div class="api-run-view__visual-stack">
          <RunSnapshot
            :api-label="selectedApiLabel"
            :mode="mode"
            :live-stage-key="liveStageKey"
            :job-status="selectedJobStatus"
            :latest-metric="latestMetric"
          />
          <ResultComposition :counts="summaryCounts" />
        </div>
      </section>

      <section class="api-run-view__visual-grid" aria-label="实时日志与 GPU 监控">
        <LiveLog :stage-key="liveStageKey" :logs="logs" />
        <GpuChart :metrics="metrics" />
      </section>

      <div
        class="api-run-view__sync"
        :class="{ 'api-run-view__sync--loading': selectedApi !== null && (detailLoading || jobLoading || runLoading) }"
        aria-live="polite"
      >
        <p v-if="selectedApi === null" class="api-run-view__sync-copy">请选择一个 API 后查看实时图表与日志。</p>
        <p v-else-if="detailLoading || jobLoading || runLoading" class="api-run-view__sync-copy">正在读取 API 详情。</p>
        <div v-else-if="detailError || jobError || runError" class="api-run-view__sync-row">
          <p class="api-run-view__sync-copy api-run-view__sync-copy--error">
            {{ detailError ?? jobError ?? runError }}
          </p>
          <button type="button" class="api-run-view__retry" @click="retrySelection">重试</button>
        </div>
        <div v-else-if="pollError" class="api-run-view__sync-row">
          <p class="api-run-view__sync-copy">同步作业状态遇到暂时错误，自动重试中。</p>
          <button type="button" class="api-run-view__retry" @click="retryPollingNow">立即重试</button>
        </div>
      </div>
    </div>
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

.api-run-view__control-band {
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

.api-run-view__visual-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(18rem, 0.95fr);
  gap: 1rem;
  align-items: start;
}

.api-run-view__visual-stack {
  display: grid;
  gap: 1rem;
  min-width: 0;
}

.api-run-view__sync {
  display: grid;
  gap: 0.75rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.95rem 1rem;
}

.api-run-view__sync--loading {
  background: var(--tg-surface-muted);
}

.api-run-view__sync-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
}

.api-run-view__sync-copy {
  margin: 0;
  color: var(--tg-text-muted);
}

.api-run-view__sync-copy--error {
  color: var(--tg-red-text);
}

.api-run-view__retry {
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: #ffffff;
  color: var(--tg-action);
  padding: 0.48rem 0.82rem;
}

@media (max-width: 1000px) {
  .api-run-view__visual-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 720px) {
  .api-run-view__mode {
    flex-wrap: wrap;
  }

  .api-run-view__section-head,
  .api-run-view__sync-row {
    flex-direction: column;
    align-items: start;
  }
}
</style>
