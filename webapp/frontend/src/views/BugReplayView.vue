<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

import {
  generateReproReport,
  getCandidateCluster,
  getCandidateClusters,
  getConfirmedBug,
  getConfirmedBugs,
  getOverview,
  getReproJob,
  getReproReport,
  reproduceConfirmedBug,
  updateCandidateClusterStatus,
} from "../services/tensorguard";
import type {
  CandidateClusterDetail,
  CandidateClusterSummary,
  ConfirmedBugDetail,
  ConfirmedBugSummary,
  ExecutionMode,
  ReproExecution,
  ReproJobPayload,
  LatestReproJobSummary,
} from "../types/tensorguard";

type SourceKind = "confirmed" | "candidate";

const sourceKind = ref<SourceKind>("confirmed");
const query = ref("");
const confirmed = ref<ConfirmedBugSummary[]>([]);
const candidateClusters = ref<CandidateClusterSummary[]>([]);
const selectedConfirmedId = ref<string | null>(null);
const selectedCandidateClusterId = ref<string | null>(null);
const detail = ref<ConfirmedBugDetail | null>(null);
const candidateClusterDetail = ref<CandidateClusterDetail | null>(null);
const loading = ref(true);
const detailLoading = ref(false);
const error = ref<string | null>(null);
const actionError = ref<string | null>(null);
const selectedModes = ref<ExecutionMode[]>(["cpu", "gpu:0"]);
const job = ref<ReproJobPayload | null>(null);
const jobRunning = ref(false);
const reportMarkdown = ref("");
const reportOpen = ref(false);
const reportLoading = ref(false);
const latestReproJobs = ref<LatestReproJobSummary[]>([]);
let pollTimer: ReturnType<typeof setTimeout> | null = null;
let selectionRevision = 0;

function describeError(value: unknown, fallback: string) {
  return value instanceof Error ? value.message : fallback;
}

function clusterStatusLabel(status: string) {
  const labels: Record<string, string> = {
    pending_review: "待审核",
    needs_review: "待分析",
    reproduced: "可复现",
    needs_minimize: "待最小化",
    rejected: "已忽略",
    promoted: "已收录",
  };
  return labels[status] ?? status;
}

const filteredConfirmed = computed(() => {
  const needle = query.value.trim().toLowerCase();
  if (!needle) return confirmed.value;
  return confirmed.value.filter((item) =>
    [item.display_id, item.title, item.api, item.bug_type, item.framework].some((value) => value.toLowerCase().includes(needle)),
  );
});

const filteredCandidateClusters = computed(() => {
  const needle = query.value.trim().toLowerCase();
  if (!needle) return candidateClusters.value;
  return candidateClusters.value.filter((item) =>
    [
      item.cluster_id,
      item.api,
      item.lib,
      item.category,
      item.bug_pattern,
      item.cluster_status,
      item.confidence,
      item.representative.source_name,
      item.representative.error_summary,
    ].some((value) => value.toLowerCase().includes(needle)),
  );
});

const candidateClusterStats = computed(() => {
  const total = candidateClusters.value.length;
  const needsMinimize = candidateClusters.value.filter((item) => item.cluster_status === "needs_minimize").length;
  return { total, needsMinimize };
});

const activeExecution = computed<ReproExecution | null>(() => {
  const modes = job.value?.status.modes;
  return modes?.["gpu:0"] ?? modes?.cpu ?? null;
});
const currentOutput = computed(() => {
  if (job.value === null) return "尚未在当前环境执行复现。";
  const chunks = Object.entries(job.value.logs).map(([name, value]) => `===== ${name} =====\n${value}`);
  return chunks.length ? chunks.join("\n\n") : "复现进程已启动，等待输出。";
});
const verdict = computed(() => {
  const executions = Object.values(job.value?.status.modes ?? {}).filter(Boolean) as ReproExecution[];
  if (executions.some((item) => item.evidence?.verdict === "reproduced")) {
    return { state: "reproduced", title: "当前环境复现成功", code: "REPRODUCED", detail: executions.find((item) => item.evidence?.verdict === "reproduced")?.evidence?.reason ?? "执行证据与归档缺陷特征一致。" };
  }
  if (jobRunning.value || job.value?.status.status === "running" || job.value?.status.status === "pending") {
    return { state: "running", title: "正在执行独立进程", code: "RUNNING", detail: "CPU 与 GPU 配置按所选模式依次运行。" };
  }
  if (job.value?.status.status === "finished") {
    return { state: "review", title: "复现结果需要复核", code: "NEEDS REVIEW", detail: activeExecution.value?.evidence?.reason ?? "本次运行未匹配确定性复现规则。" };
  }
  return { state: "idle", title: "等待当前环境复现", code: "NOT RUN", detail: "运行最小程序后，系统将依据返回码、进程信号与输出特征给出证据判定。" };
});
const reportHref = computed(() => `data:text/markdown;charset=utf-8,${encodeURIComponent(reportMarkdown.value)}`);
const environmentRows = computed(() => {
  const env = job.value?.environment;
  if (!env) return [];
  const framework = detail.value?.meta.framework === "TensorFlow" ? env.frameworks?.tensorflow : env.frameworks?.torch;
  return [
    ["Framework", framework?.installed ? framework.version : "unavailable"],
    ["CUDA", env.cuda?.driver_version ?? (env.cuda?.available ? "available" : "unavailable")],
    ["Device", env.gpus?.[0]?.name ?? "CPU only"],
    ["Python", env.python?.version ?? "unknown"],
  ];
});

function clearPoll() {
  if (pollTimer !== null) clearTimeout(pollTimer);
  pollTimer = null;
}

async function pollJob(jobId: string) {
  clearPoll();
  try {
    const payload = await getReproJob(jobId);
    job.value = payload;
    reportMarkdown.value = payload.report_markdown || reportMarkdown.value;
    jobRunning.value = payload.status.status !== "finished";
    if (jobRunning.value) pollTimer = setTimeout(() => void pollJob(jobId), 1500);
  } catch (cause) {
    actionError.value = describeError(cause, "复现状态读取失败");
    jobRunning.value = false;
  }
}

async function selectConfirmed(item: ConfirmedBugSummary) {
  selectionRevision += 1;
  const revision = selectionRevision;
  selectedConfirmedId.value = item.id;
  detailLoading.value = true;
  actionError.value = null;
  job.value = null;
  reportMarkdown.value = "";
  reportOpen.value = false;
  clearPoll();
  try {
    const payload = await getConfirmedBug(item.id);
    if (revision !== selectionRevision) return;
    detail.value = payload;
    reportMarkdown.value = "";
    const previous = latestReproJobs.value.find(
      (jobSummary) => jobSummary.bug_id === item.id || jobSummary.bug_id === payload.meta.id,
    );
    if (previous) {
      const previousPayload = await getReproJob(previous.job_id);
      if (revision !== selectionRevision) return;
      job.value = previousPayload;
      reportMarkdown.value = previousPayload.report_markdown;
    }
  } catch (cause) {
    if (revision === selectionRevision) actionError.value = describeError(cause, "证据详情加载失败");
  } finally {
    if (revision === selectionRevision) detailLoading.value = false;
  }
}

async function selectCandidateCluster(item: CandidateClusterSummary) {
  selectionRevision += 1;
  const revision = selectionRevision;
  selectedCandidateClusterId.value = item.cluster_id;
  detailLoading.value = true;
  actionError.value = null;
  try {
    const payload = await getCandidateCluster(item.cluster_id);
    if (revision === selectionRevision) candidateClusterDetail.value = payload;
  } catch (cause) {
    if (revision === selectionRevision) actionError.value = describeError(cause, "候选簇详情加载失败");
  } finally {
    if (revision === selectionRevision) detailLoading.value = false;
  }
}

async function refreshCandidateCluster(clusterId: string) {
  const [clusterList, payload] = await Promise.all([getCandidateClusters(), getCandidateCluster(clusterId)]);
  candidateClusters.value = clusterList;
  candidateClusterDetail.value = payload;
}

async function updateClusterReview(status: "pending_review" | "reproduced" | "needs_review" | "rejected", note: string) {
  if (!candidateClusterDetail.value) return;
  actionError.value = null;
  try {
    const clusterId = candidateClusterDetail.value.cluster_id;
    await updateCandidateClusterStatus(clusterId, { status, note });
    await refreshCandidateCluster(clusterId);
  } catch (cause) {
    actionError.value = describeError(cause, "候选簇状态更新失败");
  }
}

function switchSource(next: SourceKind) {
  sourceKind.value = next;
  query.value = "";
  if (next === "candidate" && selectedCandidateClusterId.value === null && candidateClusters.value[0]) void selectCandidateCluster(candidateClusters.value[0]);
}

function toggleMode(mode: ExecutionMode) {
  selectedModes.value = selectedModes.value.includes(mode)
    ? selectedModes.value.filter((item) => item !== mode)
    : [...selectedModes.value, mode];
}

async function startRepro() {
  if (!detail.value || selectedModes.value.length === 0) return;
  actionError.value = null;
  jobRunning.value = true;
  try {
    const started = await reproduceConfirmedBug(detail.value.meta.id, { modes: selectedModes.value, timeout: 60 });
    await pollJob(started.job_id);
  } catch (cause) {
    actionError.value = describeError(cause, "复现任务启动失败");
    jobRunning.value = false;
  }
}

async function openOrGenerateReport() {
  if (!job.value || job.value.status.status !== "finished") return;
  reportLoading.value = true;
  actionError.value = null;
  try {
    const payload = job.value.report_exists
      ? await getReproReport(job.value.job_id)
      : await generateReproReport(job.value.job_id);
    reportMarkdown.value = payload.report_markdown;
    reportOpen.value = true;
    job.value = { ...job.value, report_exists: true, report_markdown: payload.report_markdown, report_path: payload.report_path };
  } catch (cause) {
    actionError.value = describeError(cause, "证据报告读取失败");
  } finally {
    reportLoading.value = false;
  }
}

async function load() {
  loading.value = true;
  error.value = null;
  try {
    const [bugList, clusterList, overview] = await Promise.all([getConfirmedBugs(), getCandidateClusters(), getOverview()]);
    confirmed.value = bugList;
    candidateClusters.value = clusterList;
    latestReproJobs.value = overview.latest_repro_jobs;
    if (bugList[0]) await selectConfirmed(bugList[0]);
  } catch (cause) {
    error.value = describeError(cause, "证据库加载失败");
  } finally {
    loading.value = false;
  }
}

onMounted(() => void load());
onBeforeUnmount(clearPoll);
</script>

<template>
  <section class="bug-replay-view" aria-labelledby="bug-replay-title">
    <header class="bug-replay-view__page-head">
      <div class="bug-replay-view__title-lockup">
        <span class="bug-replay-view__page-symbol" aria-hidden="true">!</span>
        <div class="bug-replay-view__title-copy">
          <p class="bug-replay-view__eyebrow">Evidence Validation · Deterministic Replay</p>
          <h1 id="bug-replay-title">缺陷复现与证据验证</h1>
          <p>在当前环境执行最小程序，核对框架行为并固化运行证据</p>
        </div>
      </div>
      <div class="bug-replay-view__count">
        <span>已确认 <b>{{ confirmed.length }}</b></span>
        <span>候选簇 <b>{{ candidateClusterStats.total }}</b></span>
        <span>待最小化 <b>{{ candidateClusterStats.needsMinimize }}</b></span>
      </div>
    </header>

    <div v-if="loading" class="bug-replay-view__message">正在读取证据库</div>
    <div v-else-if="error" class="bug-replay-view__message bug-replay-view__message--error">{{ error }} <button type="button" @click="load">重试</button></div>

    <div v-else class="bug-replay-view__layout">
      <aside class="bug-replay-view__master">
        <div class="bug-replay-view__source-tabs" role="tablist" aria-label="证据来源">
          <button type="button" :class="{ active: sourceKind === 'confirmed' }" @click="switchSource('confirmed')">已确认</button>
          <button type="button" :class="{ active: sourceKind === 'candidate' }" @click="switchSource('candidate')">候选审核</button>
        </div>
        <input v-model="query" type="search" placeholder="搜索 API / 错误类型 / 状态" aria-label="搜索证据" />

        <div v-if="sourceKind === 'confirmed'" class="bug-replay-view__list">
          <button v-for="item in filteredConfirmed" :key="item.id" type="button" :class="{ active: selectedConfirmedId === item.id }" @click="selectConfirmed(item)">
            <span><small>{{ item.display_id }}</small><em>{{ item.framework }}</em></span>
            <b>{{ item.api }}</b><i>{{ item.bug_type }}</i>
          </button>
          <p v-if="filteredConfirmed.length === 0">未找到匹配证据</p>
        </div>
        <div v-else class="bug-replay-view__list">
          <button v-for="item in filteredCandidateClusters" :key="item.cluster_id" type="button" :class="{ active: selectedCandidateClusterId === item.cluster_id }" @click="selectCandidateCluster(item)">
            <span><small>{{ item.api }}</small><em>{{ item.member_count }} files</em></span>
            <b>{{ item.bug_pattern }}</b><i>代表程序 {{ item.representative.source_name }}</i>
            <strong :class="`bug-replay-view__cluster-badge bug-replay-view__cluster-badge--${item.cluster_status}`">{{ clusterStatusLabel(item.cluster_status) }}</strong>
          </button>
          <p v-if="filteredCandidateClusters.length === 0">暂无候选簇</p>
        </div>
      </aside>

      <main class="bug-replay-view__detail">
        <p v-if="detailLoading" class="bug-replay-view__message">正在读取详情</p>

        <template v-else-if="sourceKind === 'confirmed' && detail">
          <section class="bug-replay-view__panel bug-replay-view__case-head">
            <div class="bug-replay-view__case-title">
              <div><small>{{ detail.display_id }} · {{ detail.meta.framework }}</small><h2>{{ detail.meta.title }}</h2><code>{{ detail.meta.api }}</code></div>
              <div class="bug-replay-view__tags"><span>已确认</span><span v-if="detail.meta.minimized">已最小化</span></div>
            </div>
            <div class="bug-replay-view__verdict" :class="`bug-replay-view__verdict--${verdict.state}`">
              <strong>{{ verdict.state === "reproduced" ? "✓" : verdict.state === "running" ? "…" : "i" }}</strong>
              <div><b>{{ verdict.title }}</b><p>{{ verdict.detail }}</p></div><code>{{ verdict.code }}</code>
            </div>
          </section>

          <section class="bug-replay-view__panel bug-replay-view__reason">
            <header><span>WHY</span><div><b>问题依据</b><small>预期行为与实际行为对照</small></div><em>{{ detail.meta.bug_type }}</em></header>
            <div class="bug-replay-view__behavior">
              <article><small>Expected · 预期行为</small><b>框架应当给出可处理结果</b><p>{{ detail.meta.expected }}</p></article>
              <article class="observed"><small>Observed · 实际行为</small><b>当前归档异常行为</b><p>{{ detail.meta.observed }}</p></article>
            </div>
          </section>

          <section class="bug-replay-view__panel bug-replay-view__code-panel">
            <header><b>最小复现程序与实际输出</b><span>归档代码 · 当前运行</span></header>
            <div class="bug-replay-view__code-grid">
              <div><small>repro.py</small><pre>{{ detail.repro_code }}</pre></div>
              <div><small>CURRENT RUN OUTPUT</small><pre>{{ currentOutput }}</pre></div>
            </div>
          </section>

          <section class="bug-replay-view__panel bug-replay-view__actions">
            <div>
              <b>执行配置</b>
              <div class="bug-replay-view__profiles">
                <button type="button" :class="{ active: selectedModes.includes('cpu') }" @click="toggleMode('cpu')"><b>CPU 独立进程</b><small>CUDA_VISIBLE_DEVICES=""</small></button>
                <button type="button" :class="{ active: selectedModes.includes('gpu:0') }" @click="toggleMode('gpu:0')"><b>GPU 0 独立进程</b><small>CUDA_VISIBLE_DEVICES="0"</small></button>
              </div>
              <button type="button" class="bug-replay-view__primary" :disabled="jobRunning || selectedModes.length === 0" @click="startRepro">{{ jobRunning ? "复现运行中" : "运行当前复现" }}</button>
            </div>
            <div>
              <b>证据报告</b>
              <p class="bug-replay-view__report-state">{{ reportMarkdown ? "报告已归档，后续读取不会覆盖" : "完成一次当前环境复现后生成报告" }}</p>
              <div class="bug-replay-view__report-actions">
                <button type="button" :disabled="!job || job.status.status !== 'finished' || reportLoading" @click="openOrGenerateReport">{{ reportMarkdown ? "查看报告" : "生成报告" }}</button>
                <a v-if="reportMarkdown" :href="reportHref" :download="`${detail.display_id}-report.md`">下载 Markdown</a>
              </div>
            </div>
          </section>

          <section v-if="environmentRows.length" class="bug-replay-view__panel bug-replay-view__environment">
            <b>当前环境 · 实时采集</b><dl><div v-for="[label, value] in environmentRows" :key="label"><dt>{{ label }}</dt><dd>{{ value }}</dd></div></dl>
          </section>
          <section v-if="reportOpen" class="bug-replay-view__panel bug-replay-view__report"><header><b>当前环境证据报告</b><button type="button" @click="reportOpen = false">收起</button></header><pre>{{ reportMarkdown }}</pre></section>
          <p v-if="actionError" class="bug-replay-view__action-error">{{ actionError }}</p>
        </template>

        <template v-else-if="sourceKind === 'candidate' && candidateClusterDetail">
          <section class="bug-replay-view__panel bug-replay-view__case-head bug-replay-view__cluster-head">
            <div class="bug-replay-view__case-title">
              <div>
                <small>{{ candidateClusterDetail.cluster_id }} · {{ candidateClusterDetail.lib }}</small>
                <h2>{{ candidateClusterDetail.api }} 候选问题簇</h2>
                <code>{{ candidateClusterDetail.bug_pattern }}</code>
              </div>
              <div class="bug-replay-view__tags">
                <span>同类程序 {{ candidateClusterDetail.member_count }}</span>
                <span>已过滤 {{ candidateClusterDetail.excluded_count }}</span>
              </div>
            </div>
            <div class="bug-replay-view__cluster-pipeline">
              <article class="done"><small>01 聚类</small><b>完成</b></article>
              <article class="done"><small>02 复现</small><b>{{ candidateClusterDetail.confidence === "high" ? "高置信" : "待确认" }}</b></article>
              <article class="current"><small>03 最小化</small><b>人工处理</b></article>
              <article><small>04 收录</small><b>未确认</b></article>
            </div>
          </section>

          <section class="bug-replay-view__panel bug-replay-view__candidate-reason">
            <article><small>聚类依据</small><b>同一 API + 同一异常模式</b><p>{{ candidateClusterDetail.bug_pattern }}</p></article>
            <article><small>代表选择</small><b>优先推荐、代码短、日志清晰</b><p>当前代表程序 {{ candidateClusterDetail.representative.source_name }}，评分 {{ candidateClusterDetail.representative.score }}。</p></article>
            <article><small>确认条件</small><b>repro.py 独立验证通过</b><p>候选不会自动升级为已确认 Bug，需要人工裁剪最小复现并重新运行。</p></article>
          </section>

          <section class="bug-replay-view__candidate-workbench">
            <section class="bug-replay-view__panel bug-replay-view__code-panel">
              <header><b>候选代表源码</b><span>{{ candidateClusterDetail.representative.source_path }}</span></header>
              <div class="bug-replay-view__candidate-code"><pre>{{ candidateClusterDetail.representative_source_code || "源文件当前不可用" }}</pre></div>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__code-panel">
              <header><b>人工整理 repro.py</b><span>草稿 · 保存后运行验证</span></header>
              <div class="bug-replay-view__candidate-code"><pre>{{ candidateClusterDetail.minimization_draft || candidateClusterDetail.representative_source_code || "等待人工整理最小复现代码" }}</pre></div>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__review-card">
              <header><b>审核与收录</b><span>状态流转，不物理删除</span></header>
              <div>
                <article class="bug-replay-view__candidate-note">
                  <b>当前状态：{{ clusterStatusLabel(candidateClusterDetail.cluster_status) }}</b>
                  <p>系统已完成候选聚类；确认前需要人工判断、整理 repro.py，并运行验证。</p>
                </article>
                <label>Bug 标题</label><p>{{ candidateClusterDetail.api }} · {{ candidateClusterDetail.bug_pattern }}</p>
                <label>问题类型</label><p>{{ candidateClusterDetail.category }} / {{ candidateClusterDetail.confidence }} confidence</p>
                <label>人工判断说明</label><p>{{ candidateClusterDetail.representative.error_summary || "等待人工补充判断依据。" }}</p>
                <div class="bug-replay-view__review-actions">
                  <button type="button" @click="updateClusterReview('rejected', '人工忽略候选')">忽略候选</button>
                  <button type="button" @click="updateClusterReview('needs_review', '人工标记为待分析')">标记待分析</button>
                  <button type="button" @click="updateClusterReview('reproduced', '人工标记为可复现')">标记可复现</button>
                  <button type="button" class="bug-replay-view__primary" disabled title="需要先保存最小复现代码并生成标准归档">收录为确认 Bug</button>
                </div>
              </div>
            </section>
          </section>
          <p v-if="actionError" class="bug-replay-view__action-error">{{ actionError }}</p>
        </template>
      </main>
    </div>
  </section>
</template>

<style scoped>
.bug-replay-view { display: grid; gap: .75rem; }
.bug-replay-view__page-head { display:flex;align-items:center;justify-content:space-between;gap:1.1rem;margin-bottom:.1rem }.bug-replay-view__title-lockup{display:flex;align-items:center;gap:.8rem}.bug-replay-view__page-symbol{width:2.75rem;height:2.75rem;display:grid;place-items:center;flex:none;border:1px solid #f2d0d6;border-radius:8px;background:var(--tg-red-bg);color:var(--tg-red-text);font:820 .82rem/1 ui-monospace,monospace;box-shadow:inset 0 0 0 4px rgba(255,255,255,.66),0 7px 16px rgba(189,63,82,.07)}.bug-replay-view__title-copy{padding-left:.75rem;border-left:2px solid var(--tg-red-text)}.bug-replay-view__eyebrow{margin:0 0 .3rem;color:var(--tg-red-text);font:760 .5rem/1 ui-monospace,monospace;text-transform:uppercase}.bug-replay-view h1{margin:0;font-size:1.45rem;line-height:1.15;font-weight:790}.bug-replay-view__title-copy>p:last-child{margin:.3rem 0 0;color:var(--tg-text-muted);font-size:.63rem}.bug-replay-view__count{display:flex;align-items:center;gap:.55rem;padding:.5rem .65rem;border:1px solid var(--tg-border);border-radius:6px;background:#fff}.bug-replay-view__count span{color:var(--tg-text-muted);font-size:.5rem}.bug-replay-view__count b{font-size:1rem}
.bug-replay-view__layout{display:grid;grid-template-columns:15.6rem minmax(0,1fr);gap:.75rem;align-items:start}.bug-replay-view__master,.bug-replay-view__panel{border:1px solid var(--tg-border);border-radius:var(--tg-radius);background:#fff;box-shadow:var(--tg-shadow)}.bug-replay-view__master{position:sticky;top:calc(var(--tg-header-height) + .75rem);padding:.75rem}.bug-replay-view__source-tabs{display:grid;grid-template-columns:1fr 1fr;gap:3px;padding:3px;border:1px solid var(--tg-border);border-radius:6px;background:#f5f7fb}.bug-replay-view__source-tabs button{height:1.95rem;border:0;border-radius:4px;background:transparent;color:var(--tg-text-muted);font-size:.56rem;font-weight:740}.bug-replay-view__source-tabs button.active{background:#fff;color:var(--tg-action-strong);box-shadow:0 2px 8px rgba(36,58,98,.08)}.bug-replay-view__master>input{width:100%;height:2.1rem;margin:.55rem 0;border:1px solid #d6deeb;border-radius:5px;padding:0 .65rem;outline:none;font-size:.61rem}.bug-replay-view__master>input:focus{border-color:var(--tg-action);box-shadow:0 0 0 3px rgba(37,99,235,.1)}.bug-replay-view__list{display:grid;gap:.2rem;max-height:calc(100vh - 15rem);overflow:auto}.bug-replay-view__list>button{width:100%;display:grid;gap:.3rem;padding:.62rem;border:0;border-left:3px solid transparent;border-radius:4px;background:transparent;text-align:left}.bug-replay-view__list>button:hover{background:#f7f9fd}.bug-replay-view__list>button.active{border-left-color:var(--tg-action);background:var(--tg-action-soft)}.bug-replay-view__list span{display:flex;justify-content:space-between;gap:.4rem;color:var(--tg-text-muted);font:.45rem/1 ui-monospace,monospace}.bug-replay-view__list em{font-style:normal}.bug-replay-view__list b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font:.66rem/1.3 ui-monospace,monospace}.bug-replay-view__list i{color:var(--tg-text-muted);font-size:.5rem;font-style:normal}.bug-replay-view__list>p{margin:.8rem;text-align:center;color:var(--tg-text-muted);font-size:.58rem}.bug-replay-view__detail{display:grid;gap:.75rem;min-width:0}.bug-replay-view__message{padding:1rem;border:1px solid var(--tg-border);border-radius:8px;background:#fff;color:var(--tg-text-muted);font-size:.65rem}.bug-replay-view__message--error,.bug-replay-view__action-error{color:var(--tg-red-text)}
.bug-replay-view__case-head,.bug-replay-view__reason{padding:1rem 1.1rem}.bug-replay-view__case-title{display:flex;align-items:flex-start;justify-content:space-between;gap:.9rem}.bug-replay-view__case-title small{color:var(--tg-action);font:.5rem/1 ui-monospace,monospace}.bug-replay-view__case-title h2{margin:.38rem 0 .32rem;font-size:1.05rem}.bug-replay-view__case-title code{color:var(--tg-text-muted);font:.62rem/1.3 ui-monospace,monospace}.bug-replay-view__tags{display:flex;gap:.35rem}.bug-replay-view__tags span{padding:.3rem .45rem;border-radius:4px;background:var(--tg-green-bg);color:var(--tg-green-text);font-size:.5rem;font-weight:730}.bug-replay-view__verdict{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:.75rem;margin-top:.85rem;padding:.7rem .8rem;border:1px solid #d9e2f0;border-left:4px solid #8b98ad;border-radius:5px;background:#f7f9fc}.bug-replay-view__verdict>strong{width:2rem;height:2rem;display:grid;place-items:center;border-radius:50%;background:#8491a5;color:#fff}.bug-replay-view__verdict b{font-size:.68rem}.bug-replay-view__verdict p{margin:.22rem 0 0;color:var(--tg-text-muted);font-size:.55rem}.bug-replay-view__verdict>code{padding:.3rem .42rem;border-radius:4px;background:#fff;color:var(--tg-text-muted);font:.5rem/1 ui-monospace,monospace}.bug-replay-view__verdict--reproduced{border-color:#cce7dc;border-left-color:var(--tg-green);background:#f2faf7}.bug-replay-view__verdict--reproduced>strong{background:var(--tg-green)}.bug-replay-view__verdict--reproduced>code{color:var(--tg-green)}.bug-replay-view__verdict--running{border-color:#cbdcfb;border-left-color:var(--tg-action);background:var(--tg-action-soft)}.bug-replay-view__verdict--running>strong{background:var(--tg-action)}
.bug-replay-view__reason>header{display:flex;align-items:center;gap:.55rem;margin-bottom:.72rem}.bug-replay-view__reason>header>span{width:1.8rem;height:1.8rem;display:grid;place-items:center;border-radius:6px;background:var(--tg-red-bg);color:var(--tg-red-text);font:800 .45rem/1 ui-monospace,monospace}.bug-replay-view__reason header b{font-size:.72rem}.bug-replay-view__reason header small{display:block;margin-top:.15rem;color:var(--tg-text-muted);font-size:.48rem}.bug-replay-view__reason header em{margin-left:auto;padding:.3rem .42rem;border-radius:4px;background:var(--tg-amber-bg);color:var(--tg-amber-text);font-size:.5rem;font-style:normal;font-weight:730}.bug-replay-view__behavior{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}.bug-replay-view__behavior article{min-height:6rem;padding:.72rem .78rem;border:1px solid var(--tg-border);border-top:3px solid var(--tg-action);border-radius:6px;background:var(--tg-surface-soft)}.bug-replay-view__behavior article.observed{border-top-color:var(--tg-red-text)}.bug-replay-view__behavior small{display:block;margin-bottom:.38rem;color:var(--tg-text-muted);font-size:.48rem;font-weight:760;text-transform:uppercase}.bug-replay-view__behavior b{display:block;margin-bottom:.32rem;font-size:.66rem}.bug-replay-view__behavior p{margin:0;color:#5e687a;font-size:.55rem;line-height:1.55}
.bug-replay-view__code-panel{overflow:hidden}.bug-replay-view__code-panel>header{display:flex;align-items:center;justify-content:space-between;padding:.65rem .85rem;border-bottom:1px solid #293750;background:var(--tg-navy);color:#fff}.bug-replay-view__code-panel>header b{font-size:.61rem}.bug-replay-view__code-panel>header span{color:#a9b6d0;font-size:.48rem}.bug-replay-view__code-grid{display:grid;grid-template-columns:1fr 1fr;background:#111a2d}.bug-replay-view__code-grid>div:first-child{border-right:1px solid #2c3952}.bug-replay-view__code-grid small{display:block;padding:.5rem .8rem;border-bottom:1px solid #293750;color:#8291ac;font:.45rem/1 ui-monospace,monospace}.bug-replay-view__code-grid pre,.bug-replay-view__candidate-code pre{height:13.6rem;margin:0;padding:.68rem .8rem;overflow:auto;color:#dce6f7;font:.53rem/1.52 ui-monospace,monospace;white-space:pre-wrap;word-break:break-word}.bug-replay-view__candidate-code{background:#111a2d}
.bug-replay-view__actions{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(17.5rem,.65fr);gap:1px;overflow:hidden;background:var(--tg-border)}.bug-replay-view__actions>div{padding:.85rem 1rem;background:#fff}.bug-replay-view__actions>div>b,.bug-replay-view__environment>b{font-size:.62rem}.bug-replay-view__profiles{display:flex;gap:.42rem;margin:.55rem 0}.bug-replay-view__profiles button{flex:1;padding:.5rem .55rem;border:1px solid var(--tg-border);border-radius:5px;background:#fff;text-align:left}.bug-replay-view__profiles button.active{border-color:var(--tg-action);background:var(--tg-action-soft)}.bug-replay-view__profiles b{display:block;font-size:.55rem}.bug-replay-view__profiles small{display:block;margin-top:.18rem;color:var(--tg-text-muted);font-size:.43rem}.bug-replay-view__primary,.bug-replay-view__report-actions button,.bug-replay-view__report-actions a{height:2.1rem;display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--tg-border);border-radius:5px;background:#fff;color:var(--tg-text-strong);padding:0 .68rem;font-size:.55rem;font-weight:720;text-decoration:none}.bug-replay-view__primary{border-color:var(--tg-action);background:var(--tg-action);color:#fff}.bug-replay-view__report-state{margin:.55rem 0;padding:.55rem;border:1px solid #cde7dd;border-radius:5px;background:var(--tg-green-bg);color:#58736a;font-size:.5rem}.bug-replay-view__report-actions{display:flex;gap:.4rem}.bug-replay-view__environment{padding:.8rem 1rem}.bug-replay-view__environment dl{display:grid;grid-template-columns:repeat(4,1fr);gap:.42rem;margin:.55rem 0 0}.bug-replay-view__environment dl>div{padding:.5rem;border:1px solid var(--tg-border);border-radius:4px;background:var(--tg-surface-soft)}.bug-replay-view__environment dt{color:var(--tg-text-muted);font-size:.45rem}.bug-replay-view__environment dd{margin:.2rem 0 0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.52rem;font-weight:720}.bug-replay-view__report{overflow:hidden}.bug-replay-view__report header{display:flex;justify-content:space-between;padding:.7rem .8rem;border-bottom:1px solid var(--tg-border)}.bug-replay-view__report pre{max-height:22rem;margin:0;padding:1rem;overflow:auto;white-space:pre-wrap;font:.6rem/1.6 ui-monospace,monospace}.bug-replay-view__candidate-note{margin-top:.8rem;padding:.7rem;border:1px solid var(--tg-border);border-left:4px solid var(--tg-amber-text);border-radius:5px;background:var(--tg-amber-bg)}.bug-replay-view__candidate-note b{font-size:.65rem}.bug-replay-view__candidate-note p{margin:.25rem 0 0;color:var(--tg-text-muted);font-size:.55rem}
.bug-replay-view__cluster-badge{width:max-content;padding:.24rem .36rem;border-radius:4px;background:var(--tg-amber-bg);color:var(--tg-amber-text);font-size:.46rem;font-style:normal;font-weight:780}.bug-replay-view__cluster-badge--promoted,.bug-replay-view__cluster-badge--reproduced{background:var(--tg-green-bg);color:var(--tg-green-text)}.bug-replay-view__cluster-badge--rejected{background:var(--tg-red-bg);color:var(--tg-red-text)}
.bug-replay-view__cluster-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(18rem,.58fr);gap:.9rem;align-items:start}.bug-replay-view__cluster-pipeline{display:grid;grid-template-columns:repeat(4,1fr);gap:.35rem}.bug-replay-view__cluster-pipeline article{min-height:3.6rem;padding:.55rem;border:1px solid var(--tg-border);border-radius:6px;background:var(--tg-surface-soft)}.bug-replay-view__cluster-pipeline article.done{border-color:#c9e8d9;background:var(--tg-green-bg)}.bug-replay-view__cluster-pipeline article.current{border-color:#f1d49e;background:var(--tg-amber-bg)}.bug-replay-view__cluster-pipeline small{display:block;color:var(--tg-text-muted);font:.45rem/1 ui-monospace,monospace}.bug-replay-view__cluster-pipeline b{display:block;margin-top:.38rem;font-size:.58rem}
.bug-replay-view__candidate-reason{padding:.85rem 1rem;display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:.58rem}.bug-replay-view__candidate-reason article{min-height:5.2rem;padding:.68rem .72rem;border:1px solid var(--tg-border);border-top:3px solid var(--tg-action);border-radius:6px;background:var(--tg-surface-soft)}.bug-replay-view__candidate-reason article:nth-child(2){border-top-color:var(--tg-amber-text)}.bug-replay-view__candidate-reason article:nth-child(3){border-top-color:var(--tg-green)}.bug-replay-view__candidate-reason small{display:block;margin-bottom:.34rem;color:var(--tg-text-muted);font:.46rem/1 ui-monospace,monospace;text-transform:uppercase}.bug-replay-view__candidate-reason b{display:block;margin-bottom:.26rem;font-size:.64rem}.bug-replay-view__candidate-reason p{margin:0;color:#5e687a;font-size:.53rem;line-height:1.5}
.bug-replay-view__candidate-workbench{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr) minmax(17rem,.62fr);gap:.75rem;align-items:stretch}.bug-replay-view__candidate-workbench>.bug-replay-view__panel{min-width:0}.bug-replay-view__review-card{overflow:hidden;display:grid;grid-template-rows:auto minmax(0,1fr)}.bug-replay-view__review-card>header{display:flex;align-items:center;justify-content:space-between;padding:.65rem .85rem;border-bottom:1px solid #293750;background:var(--tg-navy);color:#fff}.bug-replay-view__review-card>header b{font-size:.61rem}.bug-replay-view__review-card>header span{color:#a9b6d0;font-size:.48rem}.bug-replay-view__review-card>div{display:grid;gap:.55rem;align-content:start;padding:.78rem;overflow:auto}.bug-replay-view__review-card label{color:var(--tg-text-muted);font-size:.48rem;font-weight:780}.bug-replay-view__review-card p{margin:0;padding:.5rem .55rem;border:1px solid var(--tg-border);border-radius:5px;background:#fff;color:#4f5c70;font-size:.52rem;line-height:1.45}.bug-replay-view__review-actions{display:grid;grid-template-columns:1fr 1fr;gap:.4rem}.bug-replay-view__review-actions button{height:2rem;border:1px solid var(--tg-border);border-radius:5px;background:#fff;color:var(--tg-text-strong);font-size:.52rem;font-weight:730}.bug-replay-view__review-actions .bug-replay-view__primary{border-color:var(--tg-action);background:var(--tg-action);color:#fff}
@media(max-width:900px){.bug-replay-view__layout{grid-template-columns:13.5rem minmax(0,1fr)}.bug-replay-view__actions{grid-template-columns:1fr 15rem}.bug-replay-view__cluster-head,.bug-replay-view__candidate-workbench{grid-template-columns:1fr}.bug-replay-view__candidate-reason{grid-template-columns:1fr}}
@media(max-width:720px){.bug-replay-view__count{display:none}.bug-replay-view__layout{grid-template-columns:1fr}.bug-replay-view__master{position:static}.bug-replay-view__list{max-height:14rem}.bug-replay-view__behavior,.bug-replay-view__code-grid,.bug-replay-view__actions,.bug-replay-view__cluster-pipeline{grid-template-columns:1fr}.bug-replay-view__code-grid>div:first-child{border-right:0;border-bottom:1px solid #2c3952}.bug-replay-view__environment dl{grid-template-columns:1fr 1fr}}
</style>
