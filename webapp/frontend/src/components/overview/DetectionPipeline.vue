<script setup lang="ts">
import { BadgeCheck, ChevronDown, ChevronRight, Replace, Search, ShieldCheck, Sparkles } from "@lucide/vue";

import AsyncState from "../AsyncState.vue";
import type { OverviewPayload } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    overview: OverviewPayload | null;
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

const steps = [
  { label: "约束检查", icon: ShieldCheck },
  { label: "Qwen 种子", icon: Sparkles },
  { label: "InCoder 变异", icon: Replace },
  { label: "差异检测", icon: Search },
  { label: "已确认证据", icon: BadgeCheck },
] as const;
</script>

<template>
  <section class="detection-pipeline" aria-labelledby="detection-pipeline-title">
    <header class="detection-pipeline__header">
      <p class="detection-pipeline__eyebrow">检测链路</p>
      <h2 id="detection-pipeline-title" class="detection-pipeline__title">检测管线</h2>
    </header>

    <AsyncState :loading="loading" :error="error" :empty="!loading && !error && overview === null" @retry="$emit('retry')">
      <template #loading>
        <p class="detection-pipeline__state-copy">正在读取检测链路。</p>
      </template>

      <template #error="{ error: errorText }">
        <p class="detection-pipeline__state-copy">{{ errorText }}</p>
      </template>

      <template #empty>
        <p class="detection-pipeline__state-copy">后端暂未返回检测数据。</p>
      </template>

      <ol class="detection-pipeline__chain" aria-label="TensorGuard 检测链路">
        <li v-for="(step, index) in steps" :key="step.label" class="detection-pipeline__node">
          <component :is="step.icon" class="detection-pipeline__node-icon" aria-hidden="true" />
          <span class="detection-pipeline__node-label">{{ step.label }}</span>
          <ChevronRight v-if="index < steps.length - 1" class="detection-pipeline__separator detection-pipeline__separator--horizontal" aria-hidden="true" />
          <ChevronDown v-if="index < steps.length - 1" class="detection-pipeline__separator detection-pipeline__separator--vertical" aria-hidden="true" />
        </li>
      </ol>
    </AsyncState>
  </section>
</template>

<style scoped>
.detection-pipeline {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  box-shadow: var(--tg-shadow);
}

.detection-pipeline__header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1rem 0.85rem;
  border-bottom: 1px solid var(--tg-border);
}

.detection-pipeline__eyebrow {
  margin: 0;
  font-size: 0.74rem;
  color: var(--tg-text-soft);
}

.detection-pipeline__title {
  margin: 0;
  font-size: 1.08rem;
  color: var(--tg-text-strong);
}

.detection-pipeline__state-copy {
  margin: 0;
}

.detection-pipeline__chain {
  margin: 0;
  list-style: none;
  display: flex;
  align-items: stretch;
  gap: 0.55rem;
  padding: 1rem;
}

.detection-pipeline__node {
  min-width: 0;
  flex: 1 1 0;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  min-height: 3rem;
  padding: 0.75rem 0.8rem;
  border-radius: var(--tg-radius-sm);
  border: 1px solid var(--tg-border);
  background: var(--tg-surface-muted);
  color: var(--tg-text-strong);
}

.detection-pipeline__node-icon {
  width: 1rem;
  height: 1rem;
  flex: none;
  color: var(--tg-action);
}

.detection-pipeline__node-label {
  min-width: 0;
  font-weight: 600;
}

.detection-pipeline__separator {
  width: 1rem;
  height: 1rem;
  flex: none;
  align-self: center;
  color: var(--tg-text-soft);
}

.detection-pipeline__separator--vertical {
  display: none;
}

@media (max-width: 719px) {
  .detection-pipeline__header {
    align-items: flex-start;
    flex-direction: column;
  }

  .detection-pipeline__chain {
    flex-direction: column;
  }

  .detection-pipeline__node {
    width: 100%;
  }

  .detection-pipeline__separator--horizontal {
    display: none;
  }

  .detection-pipeline__separator--vertical {
    display: block;
    margin-inline: auto;
  }
}
</style>
