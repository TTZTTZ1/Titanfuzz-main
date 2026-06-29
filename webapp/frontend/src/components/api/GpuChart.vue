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
    grid: { left: 46, right: 46, top: 36, bottom: 36, containLabel: true },
    legend: { top: 6, left: 0 },
    tooltip: { trigger: "axis" },
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
      <div class="gpu-chart__heading">
        <p class="gpu-chart__eyebrow">GPU 监控</p>
        <h2 :id="headingId" class="gpu-chart__title">{{ title }}</h2>
      </div>
      <p class="gpu-chart__summary">{{ summaryText }}</p>
    </header>

    <div v-if="hasData" ref="chartEl" class="gpu-chart__canvas" :aria-label="`${title} 折线图`" role="img" />
    <p v-else class="gpu-chart__empty">暂无 GPU 采样</p>
  </section>
</template>

<style scoped>
.gpu-chart {
  display: grid;
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.95rem;
  min-width: 0;
}

.gpu-chart__header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
}

.gpu-chart__heading {
  display: grid;
  gap: 0.15rem;
}

.gpu-chart__eyebrow {
  margin: 0;
  font-size: 0.8rem;
  color: var(--tg-text-soft);
}

.gpu-chart__title {
  margin: 0;
  font-size: 1rem;
  color: var(--tg-text-strong);
}

.gpu-chart__summary {
  margin: 0;
  color: var(--tg-text-muted);
  font-size: 0.9rem;
}

.gpu-chart__canvas {
  width: 100%;
  height: 19rem;
  min-height: 19rem;
}

.gpu-chart__empty {
  margin: 0;
  border: 1px dashed var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  padding: 1rem;
}
</style>
