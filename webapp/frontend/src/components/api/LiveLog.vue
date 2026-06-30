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
const stageLogFileByKey: Record<ApiRunStageKey, string> = {
  qwen_seed: "01_qwen_seed.log",
  ev_generation: "02_ev_generation.log",
  driver: "03_driver.log",
};

const stageLabel = computed(() => stageLabelByKey[props.stageKey] || props.stageKey);
const currentLog = computed(() => props.logs[stageLogFileByKey[props.stageKey]] ?? props.logs[props.stageKey] ?? "");
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
      <h2 :id="headingId" class="live-log__title">实时日志 · {{ stageLabel }}</h2>
      <button
        type="button"
        class="live-log__toggle"
        data-testid="auto-scroll-toggle"
        :aria-pressed="autoScroll"
        @click="toggleAutoScroll"
      >
        {{ autoScroll ? "自动跟随" : "已暂停" }}
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
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: #111a2d;
  min-width: 0;
  overflow: hidden;
  box-shadow: var(--tg-shadow);
  height: 100%;
}

.live-log__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-height: 2.25rem;
  padding: 0 0.85rem;
  border-bottom: 1px solid #293750;
  background: var(--tg-navy);
}

.live-log__title {
  margin: 0;
  font-size: 0.61rem;
  color: #fff;
}

.live-log__toggle {
  border: 0;
  background: transparent;
  color: #9cabca;
  padding: 0.3rem;
  font-size: 0.5rem;
}

.live-log__toggle[aria-pressed="true"] {
  color: #c8d5ed;
}

.live-log__body {
  height: 8rem;
  overflow: auto;
  background: #111a2d;
  color: #eef4ff;
  padding: 0.65rem 0.85rem;
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
  font-size: 0.54rem;
  line-height: 1.65;
}

.live-log__empty {
  margin: 0;
  height: 8rem;
  display: grid;
  place-items: center;
  background: #111a2d;
  color: #7888a4;
  padding: 1rem;
  font-size: 0.58rem;
}
</style>
