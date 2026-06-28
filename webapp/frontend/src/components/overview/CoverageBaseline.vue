<script setup lang="ts">
import { BarChart3, BadgeCheck, Layers3, ShieldCheck } from "@lucide/vue";
import { computed } from "vue";

import AsyncState from "../AsyncState.vue";
import type { OverviewPayload } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    overview: OverviewPayload | null;
    environmentSummary: string;
    loading?: boolean;
    error?: string | null;
  }>(),
  {
    loading: false,
    error: null,
  },
);

const emit = defineEmits<{
  retry: [];
}>();

function formatCount(value: number): string {
  return value.toLocaleString("en-US");
}

function formatPercent(count: number, total: number): string {
  if (!Number.isFinite(count) || !Number.isFinite(total) || total <= 0) {
    return "0%";
  }

  return `${Math.round((count / total) * 100)}%`;
}

const apiTotal = computed(() => props.overview?.api_total ?? 0);
const torchTotal = computed(() => props.overview?.api_by_lib?.torch ?? 0);
const tfTotal = computed(() => props.overview?.api_by_lib?.tf ?? 0);
const promptReadyTotal = computed(() => props.overview?.prompt_ready_total ?? 0);
const paperBugTotal = computed(() => props.overview?.paper_bug_total ?? 0);
const frameworkCount = computed(() => Object.keys(props.overview?.api_by_lib ?? {}).length);

const apiByLibRows = computed(() => [
  { label: "Torch", count: torchTotal.value },
  { label: "TensorFlow", count: tfTotal.value },
]);
</script>

<template>
  <section class="coverage-baseline" aria-labelledby="coverage-baseline-title">
    <header class="coverage-baseline__header">
      <div class="coverage-baseline__title-block">
        <p class="coverage-baseline__eyebrow">基线</p>
        <h2 id="coverage-baseline-title" class="coverage-baseline__title">覆盖基线</h2>
      </div>

      <p class="coverage-baseline__environment">
        {{ environmentSummary }}
      </p>
    </header>

    <AsyncState :loading="loading" :error="error" :empty="!loading && !error && overview === null" @retry="$emit('retry')">
      <template #loading>
        <p class="coverage-baseline__state-copy">正在读取总览数据。</p>
      </template>

      <template #error="{ error: errorText }">
        <p class="coverage-baseline__state-copy">{{ errorText }}</p>
      </template>

      <template #empty>
        <p class="coverage-baseline__state-copy">后端暂未返回总览数据。</p>
      </template>

      <div class="coverage-baseline__content">
        <dl class="coverage-baseline__stats">
          <div class="coverage-baseline__stat">
            <dt class="coverage-baseline__stat-label">
              <BarChart3 class="coverage-baseline__stat-icon" aria-hidden="true" />
              <span>总 API 覆盖</span>
            </dt>
            <dd class="coverage-baseline__stat-value">{{ formatCount(apiTotal) }}</dd>
          </div>

          <div class="coverage-baseline__stat">
            <dt class="coverage-baseline__stat-label">
              <BadgeCheck class="coverage-baseline__stat-icon" aria-hidden="true" />
              <span>已确认 Bug</span>
            </dt>
            <dd class="coverage-baseline__stat-value">{{ formatCount(paperBugTotal) }}</dd>
          </div>

          <div class="coverage-baseline__stat">
            <dt class="coverage-baseline__stat-label">
              <ShieldCheck class="coverage-baseline__stat-icon" aria-hidden="true" />
              <span>约束库状态</span>
            </dt>
            <dd class="coverage-baseline__stat-value">{{ formatCount(promptReadyTotal) }}</dd>
          </div>

          <div class="coverage-baseline__stat">
            <dt class="coverage-baseline__stat-label">
              <Layers3 class="coverage-baseline__stat-icon" aria-hidden="true" />
              <span>框架数</span>
            </dt>
            <dd class="coverage-baseline__stat-value">{{ formatCount(frameworkCount) }}</dd>
          </div>
        </dl>

        <div class="coverage-baseline__split">
          <div v-for="row in apiByLibRows" :key="row.label" class="coverage-baseline__split-row">
            <div class="coverage-baseline__split-head">
              <span class="coverage-baseline__split-label">{{ row.label }}</span>
              <span class="coverage-baseline__split-value">
                {{ formatCount(row.count) }} / {{ formatCount(apiTotal) }}
              </span>
              <span class="coverage-baseline__split-percent">
                {{ formatPercent(row.count, apiTotal) }}
              </span>
            </div>
            <progress
              class="coverage-baseline__progress"
              :value="row.count"
              :max="apiTotal > 0 ? apiTotal : 1"
              :aria-label="`${row.label} 覆盖率 ${formatPercent(row.count, apiTotal)}`"
            />
          </div>

          <div class="coverage-baseline__split-row">
            <div class="coverage-baseline__split-head">
              <span class="coverage-baseline__split-label">约束库状态</span>
              <span class="coverage-baseline__split-value">
                {{ formatCount(promptReadyTotal) }} / {{ formatCount(apiTotal) }}
              </span>
              <span class="coverage-baseline__split-percent">
                {{ formatPercent(promptReadyTotal, apiTotal) }}
              </span>
            </div>
            <progress
              class="coverage-baseline__progress"
              :value="promptReadyTotal"
              :max="apiTotal > 0 ? apiTotal : 1"
              :aria-label="`约束库状态 ${formatPercent(promptReadyTotal, apiTotal)}`"
            />
          </div>
        </div>
      </div>
    </AsyncState>
  </section>
</template>

<style scoped>
.coverage-baseline {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  box-shadow: var(--tg-shadow);
}

.coverage-baseline__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1rem 0.85rem;
  border-bottom: 1px solid var(--tg-border);
}

.coverage-baseline__eyebrow {
  margin: 0;
  font-size: 0.74rem;
  color: var(--tg-text-soft);
}

.coverage-baseline__title {
  margin: 0.15rem 0 0;
  font-size: 1.08rem;
  color: var(--tg-text-strong);
}

.coverage-baseline__environment {
  margin: 0;
  max-width: 20rem;
  color: var(--tg-text-muted);
  text-align: right;
}

.coverage-baseline__state-copy {
  margin: 0;
}

.coverage-baseline__content {
  display: grid;
  gap: 0.95rem;
  padding: 1rem;
}

.coverage-baseline__stats {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0;
  border-top: 1px solid var(--tg-border);
  border-left: 1px solid var(--tg-border);
}

.coverage-baseline__stat {
  padding: 0.85rem 0.9rem;
  border-right: 1px solid var(--tg-border);
  border-bottom: 1px solid var(--tg-border);
  background: transparent;
  border-radius: 0;
}

.coverage-baseline__stat-label {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  margin: 0;
  color: var(--tg-text-muted);
  font-size: 0.84rem;
}

.coverage-baseline__stat-icon {
  width: 0.95rem;
  height: 0.95rem;
  flex: none;
}

.coverage-baseline__stat-value {
  margin: 0.35rem 0 0;
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.1;
  color: var(--tg-text-strong);
}

.coverage-baseline__split {
  display: grid;
  gap: 0.7rem;
}

.coverage-baseline__split-row {
  display: grid;
  gap: 0.35rem;
}

.coverage-baseline__split-head {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto auto;
  align-items: baseline;
  gap: 0.5rem;
}

.coverage-baseline__split-label {
  font-weight: 600;
  color: var(--tg-text-strong);
}

.coverage-baseline__split-value,
.coverage-baseline__split-percent {
  color: var(--tg-text-muted);
  white-space: nowrap;
}

.coverage-baseline__progress {
  width: 100%;
  height: 0.62rem;
  border: 0;
  border-radius: 999px;
  overflow: hidden;
  background: var(--tg-surface-soft);
}

.coverage-baseline__progress::-webkit-progress-bar {
  background: var(--tg-surface-soft);
}

.coverage-baseline__progress::-webkit-progress-value {
  background: var(--tg-action);
}

.coverage-baseline__progress::-moz-progress-bar {
  background: var(--tg-action);
}

@media (max-width: 719px) {
  .coverage-baseline__header {
    flex-direction: column;
  }

  .coverage-baseline__environment {
    text-align: left;
  }

  .coverage-baseline__stats {
    grid-template-columns: 1fr;
  }

  .coverage-baseline__split-head {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
