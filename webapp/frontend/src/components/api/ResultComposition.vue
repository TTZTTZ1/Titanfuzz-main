<script setup lang="ts">
import { computed } from "vue";

import { resultCategoryOrder } from "../../domain/chartOptions";
import type { ResultCounts } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    counts: ResultCounts | null;
  }>(),
  {
    counts: null,
  },
);

const headingId = `result-composition-${Math.random().toString(36).slice(2, 10)}`;
const rows = computed(() => {
  if (props.counts === null) {
    return [];
  }

  return resultCategoryOrder.map((category) => ({
    category,
    value: props.counts?.[category] ?? 0,
  }));
});
</script>

<template>
  <section class="result-composition" :aria-labelledby="headingId">
    <header class="result-composition__header">
      <div class="result-composition__heading">
        <p class="result-composition__eyebrow">结果构成</p>
        <h2 :id="headingId" class="result-composition__title">七类结果</h2>
      </div>
    </header>

    <div v-if="rows.length > 0" class="result-composition__grid">
      <div v-for="row in rows" :key="row.category" class="result-composition__item">
        <span class="result-composition__category" data-testid="result-category">{{ row.category }}</span>
        <span class="result-composition__count">{{ row.value }}</span>
      </div>
    </div>
    <p v-else class="result-composition__empty">暂无结果统计</p>
  </section>
</template>

<style scoped>
.result-composition {
  display: grid;
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.95rem;
  min-width: 0;
}

.result-composition__heading {
  display: grid;
  gap: 0.15rem;
}

.result-composition__eyebrow {
  margin: 0;
  font-size: 0.8rem;
  color: var(--tg-text-soft);
}

.result-composition__title {
  margin: 0;
  font-size: 1rem;
  color: var(--tg-text-strong);
}

.result-composition__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.6rem;
}

.result-composition__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  padding: 0.7rem 0.8rem;
  min-width: 0;
}

.result-composition__category {
  color: var(--tg-text-muted);
  word-break: break-word;
}

.result-composition__count {
  font-weight: 700;
  color: var(--tg-text-strong);
}

.result-composition__empty {
  margin: 0;
  border: 1px dashed var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  padding: 1rem;
}

@media (max-width: 720px) {
  .result-composition__grid {
    grid-template-columns: 1fr;
  }
}
</style>
