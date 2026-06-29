<script setup lang="ts">
import { LineChart } from "echarts/charts";
import { GridComponent, LegendComponent, TooltipComponent } from "echarts/components";
import { init, use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { computed, onBeforeUnmount, onMounted, ref, watch } from "vue";

import { stageDefinitions, type ApiRunStageKey } from "../../domain/apiRun";
import { stageSeries } from "../../domain/chartOptions";
import type { ApiJobMetric } from "../../types/tensorguard";

use([LineChart, GridComponent, LegendComponent, TooltipComponent, CanvasRenderer]);

const props = withDefaults(
  defineProps<{
    metrics: ApiJobMetric[];
    stageKey: ApiRunStageKey;
    title?: string;
  }>(),
  {
    title: "",
  },
);

type ChartInstance = {
  setOption: (option: Record<string, unknown>, notMerge?: boolean) => void;
  resize: () => void;
  dispose: () => void;
};

const chartEl = ref<HTMLDivElement | null>(null);
let chart: ChartInstance | null = null;

const stageLabelByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition.label]));
const selectedSeries = computed(() => stageSeries(props.metrics, props.stageKey));
const hasData = computed(() => selectedSeries.value.length > 0);
const headingId = `stage-chart-${Math.random().toString(36).slice(2, 10)}`;
const titleText = computed(() => props.title || stageLabelByKey[props.stageKey] || "阶段曲线");
const summaryText = computed(() => {
  if (!hasData.value) {
    return "暂无采样";
  }

  const pointCount = selectedSeries.value[0]?.data.length ?? 0;
  return `${pointCount} 个采样点`;
});

function buildOption() {
  return {
    animation: false,
    grid: { left: 42, right: 18, top: 36, bottom: 36, containLabel: true },
    legend: { top: 6, left: 0 },
    tooltip: { trigger: "axis" },
    xAxis: {
      type: "value",
      name: "elapsed s",
      nameLocation: "end",
      boundaryGap: false,
    },
    yAxis: {
      type: "value",
      scale: true,
      min: "dataMin",
    },
    series: selectedSeries.value.map((series) => ({
      name: series.name,
      type: "line",
      data: series.data,
      showSymbol: false,
      smooth: 0.2,
      emphasis: { focus: "series" },
    })),
  };
}

function syncChart() {
  if (!hasData.value) {
    chart?.dispose();
    chart = null;
    return;
  }

  if (chart === null) {
    if (chartEl.value === null) {
      return;
    }

    chart = init(chartEl.value) as unknown as ChartInstance;
  }

  chart.setOption(buildOption(), true);
  chart.resize();
}

function handleResize() {
  chart?.resize();
}

watch(selectedSeries, syncChart, { deep: true, flush: "post" });

onMounted(() => {
  syncChart();
  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
  chart?.dispose();
  chart = null;
});
</script>

<template>
  <section class="stage-chart" :aria-labelledby="headingId">
    <header class="stage-chart__header">
      <div class="stage-chart__heading">
        <p class="stage-chart__eyebrow">阶段曲线</p>
        <h2 :id="headingId" class="stage-chart__title">{{ titleText }}</h2>
      </div>
      <p class="stage-chart__summary">{{ summaryText }}</p>
    </header>

    <div v-if="hasData" ref="chartEl" class="stage-chart__canvas" :aria-label="`${titleText} 折线图`" role="img" />
    <p v-else class="stage-chart__empty">暂无阶段采样</p>
  </section>
</template>

<style scoped>
.stage-chart {
  display: grid;
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.95rem;
  min-width: 0;
}

.stage-chart__header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
}

.stage-chart__heading {
  display: grid;
  gap: 0.15rem;
}

.stage-chart__eyebrow {
  margin: 0;
  font-size: 0.8rem;
  color: var(--tg-text-soft);
}

.stage-chart__title {
  margin: 0;
  font-size: 1rem;
  color: var(--tg-text-strong);
}

.stage-chart__summary {
  margin: 0;
  color: var(--tg-text-muted);
  font-size: 0.9rem;
}

.stage-chart__canvas {
  width: 100%;
  height: 19rem;
  min-height: 19rem;
}

.stage-chart__empty {
  margin: 0;
  border: 1px dashed var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  padding: 1rem;
}
</style>
