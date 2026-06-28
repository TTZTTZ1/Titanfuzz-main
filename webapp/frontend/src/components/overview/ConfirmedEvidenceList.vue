<script setup lang="ts">
import { BadgeCheck } from "@lucide/vue";

import AsyncState from "../AsyncState.vue";

type ConfirmedEvidenceRow = {
  display_id: string;
  api: string;
  bug_type: string;
  status: "confirmed";
};

const props = withDefaults(
  defineProps<{
    bugs: ConfirmedEvidenceRow[] | null;
    loading?: boolean;
    error?: string | null;
  }>(),
  {
    loading: false,
    error: null,
  },
);

const emit = defineEmits<{
  retry: [];
}>();

function statusLabel(status: ConfirmedEvidenceRow["status"]): string {
  return status === "confirmed" ? "已确认" : status;
}
</script>

<template>
  <section class="confirmed-evidence-list" aria-labelledby="confirmed-evidence-list-title">
    <header class="confirmed-evidence-list__header">
      <div class="confirmed-evidence-list__title-block">
        <p class="confirmed-evidence-list__eyebrow">证据</p>
        <h2 id="confirmed-evidence-list-title" class="confirmed-evidence-list__title">已确认证据</h2>
      </div>

      <p class="confirmed-evidence-list__subtitle">仅展示 display_id、API、技术影响和确认状态。</p>
    </header>

    <AsyncState :loading="loading" :error="error" :empty="!loading && !error && (bugs?.length ?? 0) === 0" @retry="$emit('retry')">
      <template #loading>
        <p class="confirmed-evidence-list__state-copy">正在读取已确认证据。</p>
      </template>

      <template #error="{ error: errorText }">
        <p class="confirmed-evidence-list__state-copy">{{ errorText }}</p>
      </template>

      <template #empty>
        <p class="confirmed-evidence-list__state-copy">后端暂未返回已确认证据。</p>
      </template>

      <table class="confirmed-evidence-list__table">
        <caption class="confirmed-evidence-list__caption">
          TensorGuard 已确认证据列表
        </caption>
        <thead>
          <tr>
            <th scope="col">编号</th>
            <th scope="col">API</th>
            <th scope="col">技术影响</th>
            <th scope="col">状态</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="bug in bugs ?? []" :key="bug.display_id">
            <th scope="row" class="confirmed-evidence-list__row-id">
              <BadgeCheck class="confirmed-evidence-list__row-icon" aria-hidden="true" />
              <span>{{ bug.display_id }}</span>
            </th>
            <td class="confirmed-evidence-list__cell">{{ bug.api }}</td>
            <td class="confirmed-evidence-list__cell confirmed-evidence-list__cell--impact">
              {{ bug.bug_type }}
            </td>
            <td class="confirmed-evidence-list__cell">
              <span class="confirmed-evidence-list__status">{{ statusLabel(bug.status) }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </AsyncState>
  </section>
</template>

<style scoped>
.confirmed-evidence-list {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  box-shadow: var(--tg-shadow);
}

.confirmed-evidence-list__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1rem 0.85rem;
  border-bottom: 1px solid var(--tg-border);
}

.confirmed-evidence-list__eyebrow {
  margin: 0;
  font-size: 0.74rem;
  color: var(--tg-text-soft);
}

.confirmed-evidence-list__title {
  margin: 0.15rem 0 0;
  font-size: 1.08rem;
  color: var(--tg-text-strong);
}

.confirmed-evidence-list__subtitle {
  margin: 0;
  max-width: 18rem;
  color: var(--tg-text-muted);
  text-align: right;
}

.confirmed-evidence-list__state-copy {
  margin: 0;
}

.confirmed-evidence-list__table {
  width: 100%;
  border-collapse: collapse;
}

.confirmed-evidence-list__caption {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.confirmed-evidence-list__table thead th {
  padding: 0.85rem 1rem 0.7rem;
  text-align: left;
  color: var(--tg-text-soft);
  font-size: 0.82rem;
  font-weight: 600;
  border-bottom: 1px solid var(--tg-border);
}

.confirmed-evidence-list__table tbody th,
.confirmed-evidence-list__table tbody td {
  padding: 0.8rem 1rem;
  border-bottom: 1px solid var(--tg-border);
  vertical-align: top;
}

.confirmed-evidence-list__table tbody tr:last-child th,
.confirmed-evidence-list__table tbody tr:last-child td {
  border-bottom: 0;
}

.confirmed-evidence-list__row-id {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-weight: 700;
  color: var(--tg-text-strong);
}

.confirmed-evidence-list__row-icon {
  width: 0.95rem;
  height: 0.95rem;
  flex: none;
  color: var(--tg-action);
}

.confirmed-evidence-list__cell {
  color: var(--tg-text);
}

.confirmed-evidence-list__cell--impact {
  color: var(--tg-text-strong);
}

.confirmed-evidence-list__status {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 0.22rem 0.6rem;
  background: var(--tg-green-bg);
  color: var(--tg-green-text);
  font-size: 0.82rem;
  font-weight: 600;
}

@media (max-width: 719px) {
  .confirmed-evidence-list__header {
    flex-direction: column;
  }

  .confirmed-evidence-list__subtitle {
    text-align: left;
  }

  .confirmed-evidence-list__table thead {
    display: none;
  }

  .confirmed-evidence-list__table,
  .confirmed-evidence-list__table tbody,
  .confirmed-evidence-list__table tr,
  .confirmed-evidence-list__table th,
  .confirmed-evidence-list__table td {
    display: block;
    width: 100%;
  }

  .confirmed-evidence-list__table tbody tr {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid var(--tg-border);
  }

  .confirmed-evidence-list__table tbody th,
  .confirmed-evidence-list__table tbody td {
    padding: 0.15rem 0;
    border-bottom: 0;
  }

  .confirmed-evidence-list__table tbody td::before {
    display: block;
    margin-bottom: 0.15rem;
    color: var(--tg-text-soft);
    font-size: 0.78rem;
  }

  .confirmed-evidence-list__table tbody td:nth-child(2)::before {
    content: "API";
  }

  .confirmed-evidence-list__table tbody td:nth-child(3)::before {
    content: "技术影响";
  }

  .confirmed-evidence-list__table tbody td:nth-child(4)::before {
    content: "状态";
  }
}
</style>
