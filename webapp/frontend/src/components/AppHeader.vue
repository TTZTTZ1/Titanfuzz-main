<script setup lang="ts">
import { Bug, LayoutDashboard, PanelRightOpen, SquarePlay } from "@lucide/vue";
import type { Component } from "vue";

import type { ViewKey } from "../composables/useHashNavigation";

withDefaults(
  defineProps<{
    activeKey: ViewKey;
    environmentLabel: string;
    environmentOpen?: boolean;
  }>(),
  {
    environmentOpen: false,
  },
);

const emit = defineEmits<{
  select: [ViewKey];
  toggleEnvironment: [];
}>();

const navItems: Array<{ key: ViewKey; label: string; hash: string; icon: Component }> = [
  { key: "overview", label: "系统总览", hash: "#overview", icon: LayoutDashboard },
  { key: "api-run", label: "单 API 运行", hash: "#api-run", icon: SquarePlay },
  { key: "bug-replay", label: "Bug 复现", hash: "#bug-replay", icon: Bug },
];

function select(key: ViewKey) {
  emit("select", key);
}
</script>

<template>
  <header class="app-header">
    <div class="app-header__brand">
      <span class="app-header__name">TensorGuard</span>
    </div>

    <nav class="app-header__nav" aria-label="TensorGuard 主要视图">
      <a
        v-for="item in navItems"
        :key="item.key"
        class="app-header__nav-item"
        :class="{ 'app-header__nav-item--active': activeKey === item.key }"
        :href="item.hash"
        :aria-current="activeKey === item.key ? 'page' : undefined"
        @click.prevent="select(item.key)"
      >
        <component :is="item.icon" class="app-header__nav-icon" aria-hidden="true" />
        <span>{{ item.label }}</span>
      </a>
    </nav>

    <div class="app-header__actions">
      <button
        type="button"
        class="app-header__environment"
        :aria-label="`环境信息：${environmentLabel}`"
        :aria-expanded="environmentOpen"
        aria-controls="environment-drawer"
        @click="$emit('toggleEnvironment')"
      >
        <PanelRightOpen class="app-header__environment-icon" aria-hidden="true" />
        <span class="app-header__environment-label">{{ environmentLabel }}</span>
      </button>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 20;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 1rem;
  padding: 0.95rem 1.25rem;
  background: rgba(255, 255, 255, 0.98);
  border-bottom: 1px solid var(--tg-border);
  box-shadow: var(--tg-shadow);
}

.app-header__brand {
  display: grid;
  gap: 0.1rem;
}

.app-header__name {
  font-size: 1.02rem;
  font-weight: 700;
  color: var(--tg-text-strong);
}

.app-header__nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  min-width: 0;
  flex-wrap: wrap;
}

.app-header__nav-item {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  border-radius: 999px;
  padding: 0.62rem 0.85rem;
  color: var(--tg-text-muted);
  transition:
    background-color 0.15s ease,
    color 0.15s ease,
    box-shadow 0.15s ease;
  white-space: nowrap;
}

.app-header__nav-item:hover {
  background: var(--tg-surface-soft);
  color: var(--tg-text);
}

.app-header__nav-item--active {
  background: var(--tg-action-soft);
  color: var(--tg-action);
  box-shadow: inset 0 0 0 1px rgba(25, 86, 209, 0.18);
}

.app-header__nav-icon {
  width: 1rem;
  height: 1rem;
  flex: none;
}

.app-header__actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.app-header__environment {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: #ffffff;
  color: var(--tg-action);
  padding: 0.65rem 0.9rem;
  box-shadow: var(--tg-shadow);
}

.app-header__environment:hover {
  border-color: rgba(25, 86, 209, 0.35);
  box-shadow: var(--tg-shadow-raised);
}

.app-header__environment-icon {
  width: 1rem;
  height: 1rem;
  flex: none;
}

.app-header__environment-label {
  max-width: 18rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (max-width: 720px) {
  .app-header {
    grid-template-columns: 1fr;
    align-items: start;
  }

  .app-header__nav {
    justify-content: flex-start;
  }

  .app-header__actions {
    justify-content: flex-start;
  }
}
</style>
