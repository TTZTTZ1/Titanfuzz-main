<script setup lang="ts">
import { computed, ref } from "vue";

import AppHeader from "./components/AppHeader.vue";
import EnvironmentDrawer from "./components/EnvironmentDrawer.vue";
import { useEnvironment } from "./composables/useEnvironment";
import { type ViewKey, useHashNavigation } from "./composables/useHashNavigation";

const { activeKey, selectKey } = useHashNavigation();
const { environment, loading, error, environmentLabel, refresh } = useEnvironment();
const environmentOpen = ref(false);

const viewContent: Record<ViewKey, { title: string; summary: string; lines: string[] }> = {
  overview: {
    title: "系统总览",
    summary: "查看当前采集到的整体状态、近况和环境信息。",
    lines: ["这里会放总体运行概况与关键指标。", "当前版本先保留清晰的占位结构，方便后续接入真实数据。"],
  },
  "api-run": {
    title: "单 API 运行",
    summary: "围绕一个 API 的选择、执行与结果确认展开。",
    lines: ["这里会放 API 搜索、模式选择和运行状态。", "现在只保留足够清楚的布局骨架。"],
  },
  "bug-replay": {
    title: "Bug 复现",
    summary: "围绕已确认问题的复现与回放工作流展开。",
    lines: ["这里会放复现任务、回放状态和结果摘要。", "当前页面仅展示稳定的入口与分区。"],
  },
};

const currentView = computed(() => viewContent[activeKey.value]);

function toggleEnvironment() {
  environmentOpen.value = !environmentOpen.value;
}

function closeEnvironment() {
  environmentOpen.value = false;
}

function handleRefresh() {
  void refresh().catch(() => undefined);
}
</script>

<template>
  <div class="app-shell">
    <AppHeader
      :active-key="activeKey"
      :environment-label="environmentLabel"
      :environment-open="environmentOpen"
      @select="selectKey"
      @toggle-environment="toggleEnvironment"
    />

    <div class="app-shell__frame">
      <main class="app-shell__main">
        <section class="view-shell">
          <p class="view-shell__eyebrow">TensorGuard</p>
          <h1 class="view-shell__title">{{ currentView.title }}</h1>
          <p class="view-shell__summary">{{ currentView.summary }}</p>

          <div class="view-shell__panel">
            <p v-for="line in currentView.lines" :key="line" class="view-shell__line">
              {{ line }}
            </p>
          </div>
        </section>
      </main>

      <EnvironmentDrawer
        :open="environmentOpen"
        :environment="environment"
        :loading="loading"
        :error="error"
        :environment-label="environmentLabel"
        @close="closeEnvironment"
        @refresh="handleRefresh"
      />
    </div>
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  background: var(--tg-bg);
}

.app-shell__frame {
  position: relative;
  min-height: calc(100vh - var(--tg-header-height));
  padding: 1.25rem;
}

.app-shell__main {
  max-width: var(--tg-content-width);
  margin: 0 auto;
  padding-right: min(29rem, 42vw);
}

.view-shell {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  box-shadow: var(--tg-shadow);
  padding: 1.4rem 1.5rem;
}

.view-shell__eyebrow {
  margin: 0;
  color: var(--tg-text-soft);
  font-size: 0.82rem;
}

.view-shell__title {
  margin: 0.4rem 0 0;
  font-size: 1.75rem;
  line-height: 1.2;
  color: var(--tg-text-strong);
}

.view-shell__summary {
  margin: 0.65rem 0 0;
  max-width: 42rem;
  color: var(--tg-text-muted);
}

.view-shell__panel {
  margin-top: 1.1rem;
  display: grid;
  gap: 0.75rem;
  border-top: 1px solid var(--tg-border);
  padding-top: 1rem;
}

.view-shell__line {
  margin: 0;
  color: var(--tg-text);
}

@media (max-width: 720px) {
  .app-shell__frame {
    padding: 0.75rem;
  }

  .app-shell__main {
    padding-right: 0;
  }

  .view-shell__title {
    font-size: 1.4rem;
  }
}
</style>
