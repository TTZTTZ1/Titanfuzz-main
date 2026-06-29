<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from "vue";

import { stageDefinitions, type ApiRunStageKey } from "../../domain/apiRun";

const props = withDefaults(
  defineProps<{
    stageKey: ApiRunStageKey;
    logs: Record<string, string>;
  }>(),
  {
    logs: () => ({}),
  },
);

const headingId = `live-log-${Math.random().toString(36).slice(2, 10)}`;
const bodyRef = ref<HTMLDivElement | null>(null);
const autoScroll = ref(true);
const stageLabelByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition.label]));

const stageLabel = computed(() => stageLabelByKey[props.stageKey] || props.stageKey);
const currentLog = computed(() => props.logs[props.stageKey] ?? "");
const hasLog = computed(() => currentLog.value.trim().length > 0);

function isAtBottom() {
  const body = bodyRef.value;
  if (body === null) {
    return true;
  }

  return body.scrollHeight - body.scrollTop - body.clientHeight <= 12;
}

function scrollToBottom() {
  const body = bodyRef.value;
  if (body === null) {
    return;
  }

  body.scrollTop = body.scrollHeight;
}

function handleScroll() {
  autoScroll.value = isAtBottom();
}

function toggleAutoScroll() {
  autoScroll.value = !autoScroll.value;
  if (autoScroll.value) {
    scrollToBottom();
  }
}

watch(
  currentLog,
  async () => {
    if (!autoScroll.value) {
      return;
    }

    await nextTick();
    scrollToBottom();
  },
  { flush: "post" },
);

onMounted(() => {
  if (autoScroll.value) {
    scrollToBottom();
  }
});

onBeforeUnmount(() => {
  autoScroll.value = false;
});
</script>

<template>
  <section class="live-log" :aria-labelledby="headingId">
    <header class="live-log__header">
      <div class="live-log__heading">
        <p class="live-log__eyebrow">实时日志</p>
        <h2 :id="headingId" class="live-log__title">{{ stageLabel }}</h2>
      </div>
      <button
        type="button"
        class="live-log__toggle"
        data-testid="auto-scroll-toggle"
        :aria-pressed="autoScroll"
        @click="toggleAutoScroll"
      >
        自动滚动
      </button>
    </header>

    <div
      v-if="hasLog"
      ref="bodyRef"
      class="live-log__body"
      data-testid="live-log-body"
      @scroll="handleScroll"
    >
      <pre class="live-log__text">{{ currentLog }}</pre>
    </div>
    <p v-else class="live-log__empty">暂无当前阶段日志</p>
  </section>
</template>

<style scoped>
.live-log {
  display: grid;
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.95rem;
  min-width: 0;
}

.live-log__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.live-log__heading {
  display: grid;
  gap: 0.15rem;
}

.live-log__eyebrow {
  margin: 0;
  font-size: 0.8rem;
  color: var(--tg-text-soft);
}

.live-log__title {
  margin: 0;
  font-size: 1rem;
  color: var(--tg-text-strong);
}

.live-log__toggle {
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: var(--tg-surface-soft);
  color: var(--tg-text-muted);
  padding: 0.5rem 0.8rem;
}

.live-log__toggle[aria-pressed="true"] {
  border-color: rgba(25, 86, 209, 0.32);
  background: var(--tg-action-soft);
  color: var(--tg-action);
}

.live-log__body {
  max-height: 21rem;
  overflow: auto;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: #0b1726;
  color: #eef4ff;
  padding: 0.85rem;
}

.live-log__text {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font-family:
    SFMono-Regular,
    ui-monospace,
    "SF Mono",
    Menlo,
    Consolas,
    monospace;
}

.live-log__empty {
  margin: 0;
  border: 1px dashed var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  padding: 1rem;
}
</style>
