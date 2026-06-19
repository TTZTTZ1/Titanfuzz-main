const state = {
  selectedApi: null,
  selectedBugId: null,
  currentApiJob: null,
  currentReproJob: null,
  apiPollTimer: null,
  reproPollTimer: null,
  confirmedBugs: [],
};

const $ = (id) => document.getElementById(id);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function api(path, options = {}) {
  const res = await fetch(path, options);
  const text = await res.text();
  let data;
  try {
    data = JSON.parse(text);
  } catch {
    data = text;
  }
  if (!res.ok) {
    throw new Error(data.error || text || `HTTP ${res.status}`);
  }
  return data;
}

function post(path, payload = {}) {
  return api(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}

function switchView(name) {
  document.querySelectorAll(".view").forEach((el) => el.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach((el) => el.classList.remove("active"));
  $(name).classList.add("active");
  document.querySelector(`[data-view="${name}"]`).classList.add("active");
}

function metric(label, value) {
  return `<div class="metric"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></div>`;
}

function source(label, value) {
  return `<div class="source-item"><span>${escapeHtml(label)}</span><code>${escapeHtml(value || "")}</code></div>`;
}

function statusText(value) {
  return `<span class="pill status-${escapeHtml(value || "pending")}">${escapeHtml(value || "pending")}</span>`;
}

function verdictText(value) {
  const labels = {
    reproduced: "复现成功",
    not_reproduced: "未复现",
    timeout: "超时",
    needs_review: "需人工确认",
    pending: "等待中",
  };
  const key = value || "pending";
  return `<span class="pill verdict-${escapeHtml(key)}">${escapeHtml(labels[key] || key)}</span>`;
}

function sumCounts(counts = {}) {
  return Object.values(counts).reduce((acc, n) => acc + Number(n || 0), 0);
}

async function loadOverview() {
  const data = await api("/api/overview");
  $("overviewMetrics").innerHTML = [
    metric("PyTorch 覆盖", data.api_by_lib?.torch || 0),
    metric("TensorFlow 覆盖", data.api_by_lib?.tf || 0),
    metric("API 总覆盖", data.api_total || 0),
    metric("约束就绪", data.prompt_ready_total || 0),
    metric("已确认 Bug", data.paper_bug_total || 0),
  ].join("");

  const bugRows = Object.entries(data.paper_bug_by_framework || {}).map(([framework, count]) => `
    <tr><td>${escapeHtml(framework)}</td><td>${escapeHtml(count)}</td></tr>
  `).join("");
  $("bugSummary").innerHTML = `
    <table>
      <thead><tr><th>来源框架</th><th>确认 Bug 数</th></tr></thead>
      <tbody>${bugRows || `<tr><td colspan="2">暂无数据</td></tr>`}</tbody>
    </table>
  `;

  $("overviewSources").innerHTML = [
    source("PyTorch API 清单", data.sources?.torch_api_list),
    source("TensorFlow API 清单", data.sources?.tf_api_list),
    source("Prompt 约束目录", data.sources?.prompt_library),
    source("单 API 运行", data.sources?.api_jobs),
    source("Bug 复现", data.sources?.repro_jobs),
  ].join("");
}

function renderApiMatches(items) {
  if (!items.length) {
    $("apiMatches").innerHTML = `<div class="empty">没有匹配的 API。</div>`;
    return;
  }
  $("apiMatches").innerHTML = items.map((item) => {
    const counts = item.result_counts || {};
    const countText = sumCounts(counts) ? `已有结果 ${sumCounts(counts)}` : "暂无结果";
    return `
      <button class="match-item" data-api="${escapeHtml(item.api)}">
        <span><code>${escapeHtml(item.api)}</code></span>
        <small>${item.has_prompt ? "约束就绪" : "缺少约束"} · ${escapeHtml(countText)}</small>
      </button>
    `;
  }).join("");
  document.querySelectorAll("[data-api]").forEach((btn) => {
    btn.addEventListener("click", () => selectApi(btn.dataset.api));
  });
}

async function searchApis() {
  const lib = $("apiLib").value;
  const q = $("apiSearch").value.trim();
  const data = await api(`/api/apis?lib=${encodeURIComponent(lib)}&q=${encodeURIComponent(q)}&limit=80`);
  renderApiMatches(data);
  if (!state.selectedApi && data.length) {
    await selectApi(data[0].api);
  }
}

async function selectApi(apiName) {
  const lib = $("apiLib").value;
  const detail = await api(`/api/api-detail?lib=${encodeURIComponent(lib)}&api=${encodeURIComponent(apiName)}`);
  state.selectedApi = detail;
  $("startApiRun").disabled = !detail.has_prompt;
  const counts = detail.result_counts || {};
  $("apiDetail").innerHTML = `
    <div class="detail-grid">
      <div><span>API</span><code>${escapeHtml(detail.api)}</code></div>
      <div><span>框架</span><strong>${escapeHtml(detail.lib)}</strong></div>
      <div><span>约束状态</span><strong>${detail.has_prompt ? "就绪" : "缺失"}</strong></div>
      <div><span>已有结果</span><strong>${sumCounts(counts)}</strong></div>
    </div>
    <div class="file-row"><span>API 清单</span><code>${escapeHtml(detail.api_list)}</code></div>
    <div class="file-row"><span>约束路径</span><code>${escapeHtml(detail.prompt_path)}</code></div>
    <div class="file-row"><span>Results</span><code>${escapeHtml(detail.results_path)}</code></div>
    <div class="mini-counts">
      ${Object.entries(counts).map(([name, value]) => `<span>${escapeHtml(name)}: <b>${escapeHtml(value)}</b></span>`).join("")}
    </div>
  `;
}

function renderApiStages(status) {
  const stages = status?.stages || {};
  const names = [
    ["prompt_check", "约束检查"],
    ["qwen_seed", "Qwen 种子生成"],
    ["ev_generation", "InCoder-6B 变异测试"],
    ["driver", "CPU/GPU 差异检测"],
    ["summary", "摘要生成"],
  ];
  $("apiStages").innerHTML = names.map(([name, label]) => {
    const value = stages[name] || "pending";
    return `<div class="stage"><b>${escapeHtml(label)}</b><small>${escapeHtml(name)}</small>${statusText(value)}</div>`;
  }).join("");
}

async function startApiRun() {
  if (!state.selectedApi) return;
  const payload = {
    lib: state.selectedApi.lib,
    api: state.selectedApi.api,
    mode: $("apiMode").value,
    cuda_device: "0",
  };
  const data = await post("/api/run-api", payload);
  state.currentApiJob = data.job_id;
  $("apiJobSummary").textContent = `Job started: ${data.job_id}\nOutput: ${data.out}`;
  if (state.apiPollTimer) clearInterval(state.apiPollTimer);
  state.apiPollTimer = setInterval(loadApiJob, 1000);
  await loadApiJob();
}

async function loadApiJob() {
  if (!state.currentApiJob) return;
  const data = await api(`/api/api-jobs/${encodeURIComponent(state.currentApiJob)}`);
  renderApiStages(data.status);
  $("apiJobSummary").textContent = JSON.stringify(data.summary || data.status || {}, null, 2);
  $("apiJobLogs").textContent = Object.entries(data.logs || {})
    .map(([name, content]) => `===== ${name} =====\n${content}`)
    .join("\n\n");
  const status = data.status?.status;
  if (status === "success" || status === "failed") {
    clearInterval(state.apiPollTimer);
    state.apiPollTimer = null;
    loadOverview().catch(console.error);
  }
}

function renderConfirmedBugList() {
  $("confirmedBugList").innerHTML = state.confirmedBugs.map((bug) => `
    <button class="bug-item" data-bug="${escapeHtml(bug.id)}">
      <strong>${escapeHtml(bug.display_id || bug.id)}</strong>
      <span>${escapeHtml(bug.framework)} · ${escapeHtml(bug.api)}</span>
      <small>${escapeHtml(bug.bug_type || bug.title || "")}</small>
    </button>
  `).join("");
  document.querySelectorAll("[data-bug]").forEach((btn) => {
    btn.addEventListener("click", () => selectConfirmedBug(btn.dataset.bug));
  });
}

async function loadConfirmedBugs() {
  state.confirmedBugs = await api("/api/confirmed-bugs");
  renderConfirmedBugList();
  if (state.confirmedBugs.length) {
    await selectConfirmedBug(state.confirmedBugs[0].id);
  }
}

async function selectConfirmedBug(id) {
  const detail = await api(`/api/confirmed-bugs/${encodeURIComponent(id)}`);
  state.selectedBugId = id;
  $("runCpuRepro").disabled = false;
  $("runGpuRepro").disabled = false;
  $("runBothRepro").disabled = false;
  $("generateReport").disabled = true;
  const meta = detail.meta || {};
  $("confirmedBugDetail").innerHTML = `
    <div class="detail-grid">
      <div><span>ID</span><strong>${escapeHtml(detail.display_id || meta.id)}</strong></div>
      <div><span>框架</span><strong>${escapeHtml(meta.framework)}</strong></div>
      <div><span>API</span><code>${escapeHtml(meta.api)}</code></div>
      <div><span>严重程度</span><strong>${escapeHtml(meta.severity)}</strong></div>
    </div>
    <div class="file-row"><span>缺陷类型</span><code>${escapeHtml(meta.bug_type)}</code></div>
    <div class="file-row"><span>触发原因</span><code>${escapeHtml(meta.trigger)}</code></div>
    <div class="text-block"><b>已确认现象</b><p>${escapeHtml(meta.observed)}</p></div>
    <div class="text-block"><b>预期行为</b><p>${escapeHtml(meta.expected)}</p></div>
  `;
  $("reproCode").textContent = detail.repro_code || "";
  $("reproStatus").textContent = "尚未启动复现。";
  $("reproLogs").textContent = "";
  $("generatedReport").textContent = "复现后可生成当前环境报告。";
}

async function startRepro(modes) {
  if (!state.selectedBugId) return;
  const data = await post(`/api/confirmed-bugs/${encodeURIComponent(state.selectedBugId)}/reproduce`, { modes });
  state.currentReproJob = data.job_id;
  $("reproStatus").textContent = `Job started: ${data.job_id}\nOutput: ${data.out}`;
  $("generateReport").disabled = false;
  if (state.reproPollTimer) clearInterval(state.reproPollTimer);
  state.reproPollTimer = setInterval(loadReproJob, 1000);
  await loadReproJob();
}

function reproStatusSummary(status) {
  if (!status || !status.modes) return "尚未启动复现。";
  const rows = Object.entries(status.modes).map(([mode, item]) => `
    <tr>
      <td>${escapeHtml(mode)}</td>
      <td>${statusText(item.status)}</td>
      <td>${verdictText(item.verdict)}</td>
      <td>${escapeHtml(item.returncode)}</td>
      <td>${escapeHtml(item.timed_out)}</td>
      <td><code>${escapeHtml(item.log)}</code></td>
    </tr>
  `).join("");
  return `
    <div class="file-row"><span>Job</span><code>${escapeHtml(status.job_id)}</code></div>
    <div class="file-row"><span>输出目录</span><code>${escapeHtml(status.out)}</code></div>
    <table>
      <thead><tr><th>模式</th><th>状态</th><th>判定</th><th>返回码</th><th>超时</th><th>日志</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}

async function loadReproJob() {
  if (!state.currentReproJob) return;
  const data = await api(`/api/repro-jobs/${encodeURIComponent(state.currentReproJob)}`);
  $("reproStatus").innerHTML = reproStatusSummary(data.status);
  $("reproLogs").textContent = Object.entries(data.logs || {})
    .map(([name, content]) => `===== ${name} =====\n${content}`)
    .join("\n\n");
  if (data.report_markdown) {
    $("generatedReport").textContent = data.report_markdown;
  }
  const done = data.status?.status === "finished" || data.status?.status === "failed";
  if (done) {
    clearInterval(state.reproPollTimer);
    state.reproPollTimer = null;
    $("generateReport").disabled = false;
  }
}

async function generateCurrentReport() {
  if (!state.currentReproJob) return;
  const data = await post(`/api/repro-jobs/${encodeURIComponent(state.currentReproJob)}/report`, {});
  $("generatedReport").textContent = data.report_markdown || "";
  $("generateReport").disabled = false;
}

function debounce(fn, delay = 250) {
  let timer = null;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function bindEvents() {
  document.querySelectorAll(".nav-item").forEach((btn) => {
    btn.addEventListener("click", () => switchView(btn.dataset.view));
  });
  document.querySelectorAll("[data-jump]").forEach((btn) => {
    btn.addEventListener("click", () => switchView(btn.dataset.jump));
  });
  $("refreshOverview").addEventListener("click", () => loadOverview().catch(alertError));
  $("apiLib").addEventListener("change", async () => {
    state.selectedApi = null;
    $("apiSearch").value = "";
    $("startApiRun").disabled = true;
    await searchApis();
  });
  $("apiSearch").addEventListener("input", debounce(() => searchApis().catch(alertError)));
  $("startApiRun").addEventListener("click", () => startApiRun().catch(alertError));
  $("runCpuRepro").addEventListener("click", () => startRepro(["cpu"]).catch(alertError));
  $("runGpuRepro").addEventListener("click", () => startRepro(["gpu0"]).catch(alertError));
  $("runBothRepro").addEventListener("click", () => startRepro(["cpu", "gpu0"]).catch(alertError));
  $("generateReport").addEventListener("click", () => generateCurrentReport().catch(alertError));
}

function alertError(err) {
  alert(err.message || String(err));
}

async function init() {
  bindEvents();
  renderApiStages({});
  await Promise.all([
    loadOverview(),
    searchApis(),
    loadConfirmedBugs(),
  ]);
}

init().catch(alertError);
