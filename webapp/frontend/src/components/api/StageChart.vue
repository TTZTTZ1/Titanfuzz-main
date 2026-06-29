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
const latestSeriesValues = computed(() =>
  selectedSeries.value.map((series) => ({
    name: series.name,
    value: series.data.at(-1)?.[1] ?? 0,
  })),
);

function buildOption() {
  return {
    animation: false,
    color: ["#2563eb", "#178263", "#d29a43", "#c65362"],
    grid: { left: 22, right: 20, top: 18, bottom: 28, containLabel: true },
    legend: { show: false },
    tooltip: { trigger: "axis", backgroundColor: "#15213b", borderWidth: 0, textStyle: { color: "#fff" } },
    xAxis: {
      type: "value",
      name: "elapsed s",
      nameLocation: "end",
      boundaryGap: false,
    },
    yAxis: {
      type: "value",
      scale: true,
      splitLine: { lineStyle: { color: "#edf1f7" } },
      min: "dataMin",
    },
    series: selectedSeries.value.map((series) => ({
      name: series.name,
      type: "line",
      data: series.data,
      showSymbol: false,
      smooth: 0.2,
      lineStyle: { width: 2.5 },
      areaStyle: { opacity: 0.08 },
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
      <div class="stage-chart__stats">
        <div v-for="item in latestSeriesValues.slice(0, 2)" :key="item.name" class="stage-chart__stat">
          <span>{{ item.name }}</span><b>{{ item.value }}</b>
        </div>
        <p class="stage-chart__summary">{{ summaryText }}</p>
      </div>
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
  padding: 0.85rem 1rem 0.75rem;
  box-shadow: var(--tg-shadow);
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
  font-size: 0.5rem;
  color: var(--tg-text-soft);
}

.stage-chart__title {
  margin: 0;
  font-size: 0.74rem;
  color: var(--tg-text-strong);
}

.stage-chart__summary {
  margin: 0;
  color: var(--tg-text-muted);
  font-size: 0.52rem;
}

.stage-chart__stats {
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.stage-chart__stat {
  min-width: 5.2rem;
  padding: 0.38rem 0.48rem;
  border: 1px solid #d9e2f0;
  border-radius: 5px;
  background: #f8faff;
}

.stage-chart__stat span {
  display: block;
  color: var(--tg-text-muted);
  font-size: 0.48rem;
}

.stage-chart__stat b {
  display: block;
  margin-top: 0.16rem;
  color: var(--tg-text-strong);
  font-size: 0.85rem;
}

.stage-chart__canvas {
  width: 100%;
  height: 12.2rem;
  min-height: 12.2rem;
  border: 1px solid #dce4f0;
  border-radius: 5px;
  background: #fbfdff;
}

.stage-chart__empty {
  margin: 0;
  border: 1px dashed var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  min-height: 12.2rem;
  display: grid;
  place-items: center;
  padding: 1rem;
  font-size: 0.62rem;
}
</style>
