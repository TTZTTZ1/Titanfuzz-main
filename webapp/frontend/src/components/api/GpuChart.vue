<script setup lang="ts">
import { LineChart } from "echarts/charts";
import { GridComponent, LegendComponent, TooltipComponent } from "echarts/components";
import { init, use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { computed, onBeforeUnmount, onMounted, ref, watch } from "vue";

import { gpuSeries } from "../../domain/chartOptions";
import type { ApiJobMetric } from "../../types/tensorguard";

use([LineChart, GridComponent, LegendComponent, TooltipComponent, CanvasRenderer]);

const props = withDefaults(
  defineProps<{
    metrics: ApiJobMetric[];
    title?: string;
  }>(),
  {
    title: "GPU 监控",
  },
);

type ChartInstance = {
  setOption: (option: Record<string, unknown>, notMerge?: boolean) => void;
  resize: () => void;
  dispose: () => void;
};

const chartEl = ref<HTMLDivElement | null>(null);
let chart: ChartInstance | null = null;

const series = computed(() => gpuSeries(props.metrics));
const hasData = computed(() => series.value.length > 0);
const headingId = `gpu-chart-${Math.random().toString(36).slice(2, 10)}`;
const summaryText = computed(() => {
  if (!hasData.value) {
    return "暂无 GPU 采样";
  }

  const pointCount = series.value[0]?.data.length ?? 0;
  return `${pointCount} 个采样点`;
});

function buildOption() {
  return {
    animation: false,
    color: ["#2563eb", "#168aa4"],
    grid: { left: 14, right: 14, top: 12, bottom: 20, containLabel: true },
    legend: { show: false },
    tooltip: { trigger: "axis", backgroundColor: "#15213b", borderWidth: 0, textStyle: { color: "#fff" } },
    xAxis: {
      type: "value",
      name: "elapsed s",
      nameLocation: "end",
      boundaryGap: false,
    },
    yAxis: [
      {
        type: "value",
        name: "utilization %",
        min: 0,
        max: 100,
        splitLine: { lineStyle: { color: "#edf1f7" } },
      },
      {
        type: "value",
        name: "memory MiB",
        scale: true,
      },
    ],
    series: series.value.map((item, index) => ({
      name: item.name,
      type: "line",
      data: item.data,
      yAxisIndex: index === 0 ? 0 : 1,
      showSymbol: false,
      smooth: 0.2,
      lineStyle: { width: 2 },
      areaStyle: { opacity: 0.07 },
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

watch(series, syncChart, { deep: true, flush: "post" });

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
  <section class="gpu-chart" :aria-labelledby="headingId">
    <header class="gpu-chart__header">
      <h2 :id="headingId" class="gpu-chart__title">{{ title }}</h2>
      <p class="gpu-chart__summary">{{ summaryText }}</p>
    </header>

    <div v-if="hasData" ref="chartEl" class="gpu-chart__canvas" :aria-label="`${title} 折线图`" role="img" />
    <p v-else class="gpu-chart__empty">暂无 GPU 采样</p>
  </section>
</template>

<style scoped>
.gpu-chart {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  min-width: 0;
  overflow: hidden;
  box-shadow: var(--tg-shadow);
  height: 100%;
}

.gpu-chart__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-height: 2.25rem;
  padding: 0 0.85rem;
  border-bottom: 1px solid #293750;
  background: var(--tg-navy);
}

.gpu-chart__title {
  margin: 0;
  font-size: 0.61rem;
  color: #fff;
}

.gpu-chart__summary {
  margin: 0;
  color: #9cabca;
  font-size: 0.5rem;
}

.gpu-chart__canvas {
  width: 100%;
  height: 8rem;
  min-height: 8rem;
}

.gpu-chart__empty {
  margin: 0;
  height: 8rem;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #ffffff, #f3f7ff);
  color: var(--tg-text-muted);
  padding: 1rem;
  font-size: 0.58rem;
}
</style>
