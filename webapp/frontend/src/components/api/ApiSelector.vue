<script setup lang="ts">
import { computed, ref, watch } from "vue";

import type { ApiListItem, Library } from "../../types/tensorguard";
import { useApiCatalog } from "../../composables/useApiCatalog";

const props = withDefaults(
  defineProps<{
    selected?: ApiListItem | null;
  }>(),
  {
    selected: null,
  },
);

const emit = defineEmits<{
  select: [ApiListItem];
  libraryChange: [Library];
}>();

const { library, query, items, loading, error, setLibrary, refresh } = useApiCatalog();
const isOpen = ref(true);
const activeIndex = ref(-1);
const listboxId = "api-selector-listbox";

function isSelected(item: ApiListItem): boolean {
  return props.selected !== null && props.selected.api === item.api && props.selected.lib === item.lib;
}

const activeDescendantId = computed(() =>
  isOpen.value && activeIndex.value >= 0 && activeIndex.value < items.value.length
    ? `api-selector-option-${activeIndex.value}`
    : undefined,
);

function handleInput(event: Event) {
  query.value = (event.target as HTMLInputElement).value;
  isOpen.value = true;
  activeIndex.value = -1;
}

function handleLibraryChange(nextLibrary: Library) {
  setLibrary(nextLibrary);
  emit("libraryChange", nextLibrary);
  isOpen.value = true;
  activeIndex.value = -1;
}

function setActiveIndex(nextIndex: number) {
  activeIndex.value = nextIndex;
}

function selectItem(item: ApiListItem, index: number) {
  setActiveIndex(index);
  emit("select", item);
  isOpen.value = false;
}

function getNextEnabledIndex(step: 1 | -1) {
  if (items.value.length === 0) {
    return -1;
  }

  if (activeIndex.value < 0) {
    return step > 0 ? 0 : items.value.length - 1;
  }

  return (activeIndex.value + step + items.value.length) % items.value.length;
}

function moveActive(step: 1 | -1) {
  const nextIndex = getNextEnabledIndex(step);
  if (nextIndex < 0) {
    return;
  }

  isOpen.value = true;
  setActiveIndex(nextIndex);
}

function handleKeydown(event: KeyboardEvent) {
  if (event.key === "ArrowDown") {
    event.preventDefault();
    moveActive(1);
    return;
  }

  if (event.key === "ArrowUp") {
    event.preventDefault();
    moveActive(-1);
    return;
  }

  if (event.key === "Home") {
    if (items.value.length === 0) {
      return;
    }

    event.preventDefault();
    isOpen.value = true;
    setActiveIndex(0);
    return;
  }

  if (event.key === "End") {
    if (items.value.length === 0) {
      return;
    }

    event.preventDefault();
    isOpen.value = true;
    setActiveIndex(items.value.length - 1);
    return;
  }

  if (event.key === "Enter") {
    if (activeIndex.value < 0 || activeIndex.value >= items.value.length) {
      return;
    }

    event.preventDefault();
    selectItem(items.value[activeIndex.value], activeIndex.value);
    return;
  }

  if (event.key === "Escape") {
    if (!isOpen.value) {
      return;
    }

    event.preventDefault();
    isOpen.value = false;
  }
}

watch(
  items,
  (nextItems) => {
    if (nextItems.length === 0) {
      activeIndex.value = -1;
      return;
    }

    if (activeIndex.value >= nextItems.length) {
      activeIndex.value = -1;
    }
  },
  { immediate: true },
);
</script>

<template>
  <section class="api-selector" aria-label="API 搜索">
    <div class="api-selector__toolbar" role="radiogroup" aria-label="API 库">
      <button
        type="button"
        role="radio"
        class="api-selector__library"
        :class="{ 'api-selector__library--active': library === 'torch' }"
        :aria-checked="library === 'torch'"
        @click="handleLibraryChange('torch')"
      >
        torch
      </button>
      <button
        type="button"
        role="radio"
        class="api-selector__library"
        :class="{ 'api-selector__library--active': library === 'tf' }"
        :aria-checked="library === 'tf'"
        @click="handleLibraryChange('tf')"
      >
        tf
      </button>

      <label class="api-selector__search">
        <span class="api-selector__search-label">搜索 API</span>
        <input
          class="api-selector__search-input"
          type="search"
          role="combobox"
          aria-autocomplete="list"
          :aria-expanded="isOpen"
          :aria-controls="listboxId"
          :aria-activedescendant="activeDescendantId"
          :value="query"
          @input="handleInput"
          @keydown="handleKeydown"
          @focus="isOpen = true"
        />
      </label>
    </div>

    <div v-if="loading" class="api-selector__state" role="status" aria-live="polite">正在加载 API 列表</div>

    <div v-else-if="error" class="api-selector__state api-selector__state--error" role="alert">
      <p class="api-selector__state-copy">{{ error }}</p>
      <button type="button" class="api-selector__retry" @click="refresh">重试</button>
    </div>

    <ul v-else-if="isOpen" :id="listboxId" class="api-selector__list" role="listbox" aria-label="API 结果">
      <li v-for="(item, index) in items" :key="`${item.lib}:${item.api}`" class="api-selector__item">
        <button
          :id="`api-selector-option-${index}`"
          type="button"
          role="option"
          class="api-selector__option"
          :class="{
            'api-selector__option--selected': isSelected(item),
            'api-selector__option--active': activeIndex === index,
          }"
          :aria-selected="isSelected(item)"
          tabindex="-1"
          @click="selectItem(item, index)"
        >
          <span class="api-selector__option-api">{{ item.api }}</span>
          <span class="api-selector__option-lib">{{ item.lib }}</span>
        </button>
      </li>
    </ul>

    <div v-if="!loading && !error && isOpen && items.length === 0" class="api-selector__state">未找到 API</div>
  </section>
</template>

<style scoped>
.api-selector {
  display: grid;
  gap: 0.85rem;
}

.api-selector__toolbar {
  display: grid;
  grid-template-columns: auto auto minmax(0, 1fr);
  gap: 0.5rem;
  align-items: center;
}

.api-selector__library {
  border: 1px solid var(--tg-border);
  border-radius: 999px;
  background: #ffffff;
  color: var(--tg-text-muted);
  padding: 0.5rem 0.8rem;
}

.api-selector__library--active {
  border-color: rgba(25, 86, 209, 0.28);
  color: var(--tg-action);
  background: var(--tg-action-soft);
}

.api-selector__search {
  display: grid;
  gap: 0.35rem;
  min-width: 0;
}

.api-selector__search-label {
  font-size: 0.82rem;
  color: var(--tg-text-soft);
}

.api-selector__search-input {
  width: 100%;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: #ffffff;
  padding: 0.6rem 0.75rem;
  color: var(--tg-text-strong);
}

.api-selector__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.45rem;
}

.api-selector__option {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.7rem 0.85rem;
  color: var(--tg-text);
  text-align: left;
}

.api-selector__option--selected {
  border-color: rgba(25, 86, 209, 0.35);
  background: var(--tg-action-soft);
  color: var(--tg-action);
}

.api-selector__option--active {
  box-shadow: inset 0 0 0 1px rgba(25, 86, 209, 0.18);
}

.api-selector__option-api {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.api-selector__option-lib {
  flex: none;
  color: var(--tg-text-soft);
  font-size: 0.82rem;
  text-transform: uppercase;
}

.api-selector__state {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface-muted);
  color: var(--tg-text-muted);
  padding: 0.9rem;
}

.api-selector__state--error {
  background: var(--tg-red-bg);
  border-color: var(--tg-red-border);
  color: var(--tg-red-text);
  display: grid;
  gap: 0.65rem;
}

.api-selector__state-copy {
  margin: 0;
}

.api-selector__retry {
  justify-self: start;
  border: 1px solid currentColor;
  border-radius: 999px;
  background: #ffffff;
  color: inherit;
  padding: 0.45rem 0.85rem;
}
</style>
