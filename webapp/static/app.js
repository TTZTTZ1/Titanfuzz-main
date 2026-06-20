const state = {
  selectedApi: null,
  selectedBugId: null,
  currentApiJob: null,
  currentReproJob: null,
  apiPollTimer: null,
  reproPollTimer: null,
  confirmedBugs: [],
  apiMatches: [],
  environment: null,
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

function metric(label, value, note = "") {
  return `<div class="metric"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong>${note ? `<small>${escapeHtml(note)}</small>` : ""}</div>`;
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

function modeLabel(value) {
  return value === "normal" ? "完整模式" : "演示模式";
}

function mutationModelLabel(value) {
  if (!value) return "InCoder 变异";
  if (value.includes("incoder-1B")) return "InCoder-1B 变异测试";
  if (value.includes("incoder-6B")) return "InCoder-6B 变异测试";
  return `${value.split("/").pop()} 变异测试`;
}

function renderBars(target, rows) {
  const max = Math.max(...rows.map((row) => Number(row.value || 0)), 1);
  $(target).innerHTML = rows.map((row) => `
    <div class="bar-row">
      <span class="bar-label" title="${escapeHtml(row.label)}">${escapeHtml(row.label)}</span>
      <span class="bar-track"><span class="bar-fill" style="width:${Math.max(2, Number(row.value || 0) / max * 100)}%"></span></span>
      <span class="bar-value">${escapeHtml(row.value)}</span>
    </div>
  `).join("") || `<div class="empty">暂无可展示数据</div>`;
}

async function loadOverview() {
  const [data, bugs] = await Promise.all([
    api("/api/overview"),
    state.confirmedBugs.length ? Promise.resolve(state.confirmedBugs) : api("/api/confirmed-bugs"),
  ]);
  state.confirmedBugs = bugs;
  $("overviewMetrics").innerHTML = [
    metric("API 总覆盖", data.api_total || 0, "目标接口总数"),
    metric("PyTorch", data.api_by_lib?.torch || 0, "API 清单"),
    metric("TensorFlow", data.api_by_lib?.tf || 0, "API 清单"),
    metric("已确认 Bug", data.paper_bug_total || 0, "可复现证据"),
  ].join("");

  renderBars("frameworkDistribution", Object.entries(data.api_by_lib || {}).map(([label, value]) => ({
    label: label === "torch" ? "PyTorch" : "TensorFlow",
    value,
  })));

  const typeCounts = {};
  bugs.forEach((bug) => {
    const type = bug.bug_type || "其他";
    typeCounts[type] = (typeCounts[type] || 0) + 1;
  });
  renderBars("bugTypeDistribution", Object.entries(typeCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 6)
    .map(([label, value]) => ({ label, value })));

  const bugRows = bugs.slice(0, 8).map((bug) => `
    <tr>
      <td><strong>${escapeHtml(bug.display_id || bug.id)}</strong></td>
      <td>${escapeHtml(bug.framework)}</td>
      <td><code>${escapeHtml(bug.api)}</code></td>
      <td>${escapeHtml(bug.bug_type || bug.title || "")}</td>
      <td><button class="text-action" data-open-bug="${escapeHtml(bug.id)}">查看证据</button></td>
    </tr>
  `).join("");
  $("bugSummary").innerHTML = `
    <table>
      <thead><tr><th>编号</th><th>框架</th><th>API</th><th>问题类型</th><th></th></tr></thead>
      <tbody>${bugRows || `<tr><td colspan="5">暂无数据</td></tr>`}</tbody>
    </table>
  `;
  document.querySelectorAll("[data-open-bug]").forEach((button) => {
    button.addEventListener("click", async () => {
      switchView("bugReplay");
      await selectConfirmedBug(button.dataset.openBug);
    });
  });
}

function environmentRow(label, value) {
  return `<div class="environment-row"><span>${escapeHtml(label)}</span><code>${escapeHtml(value ?? "-")}</code></div>`;
}

function populateGpuControls(environment) {
  const gpus = environment.gpus || [];
  const select = $("apiGpuSelect");
  select.innerHTML = gpus.length
    ? gpus.map((gpu) => `<option value="${escapeHtml(gpu.index)}">${escapeHtml(gpu.index)} · ${escapeHtml(gpu.name)}</option>`).join("")
    : `<option value="">未检测到可用 GPU</option>`;
  select.disabled = !gpus.length;
  const gpuLabel = gpus.length ? `设备 ${gpus[0].index} 运行` : "加速器运行";
  $("runGpuRepro").textContent = gpuLabel;
  $("runBothRepro").textContent = gpus.length ? `隐藏加速器 + 设备 ${gpus[0].index}` : "运行两种配置";
}

function renderEnvironment(environment) {
  const platform = environment.platform || {};
  const python = environment.python || {};
  const frameworks = environment.frameworks || {};
  const gpus = environment.gpus || [];
  const gpuRows = gpus.map((gpu) => `
    <div class="environment-group">
      <h3>GPU ${escapeHtml(gpu.index)}</h3>
      ${environmentRow("型号", gpu.name)}
      ${environmentRow("显存", gpu.memory_total_mib == null ? "-" : `${gpu.memory_total_mib} MiB`)}
      ${environmentRow("驱动", gpu.driver_version)}
    </div>
  `).join("");
  const warningRows = (environment.warnings || []).map((warning) => `<li>${escapeHtml(warning)}</li>`).join("");
  $("environmentContent").innerHTML = `
    <div class="environment-group">
      <h3>系统</h3>
      ${environmentRow("平台", [platform.system, platform.release, platform.machine].filter(Boolean).join(" "))}
      ${environmentRow("Python", python.version)}
      ${environmentRow("解释器", python.executable)}
      ${environmentRow("PyTorch", frameworks.torch?.installed ? frameworks.torch.version : "未安装")}
      ${environmentRow("TensorFlow", frameworks.tensorflow?.installed ? frameworks.tensorflow.version : "未安装")}
      ${environmentRow("采集时间", environment.collected_at)}
    </div>
    ${gpuRows || `<div class="environment-group"><h3>GPU</h3><div class="empty">当前服务未获得 GPU 清单。</div></div>`}
    ${warningRows ? `<div class="environment-group"><h3>采集提示</h3><ul class="warning-list">${warningRows}</ul></div>` : ""}
  `;
  $("environmentBrief").textContent = gpus.length ? `${gpus.length} 个 GPU · Python ${python.version || "-"}` : `Python ${python.version || "-"}`;
  $("environmentDot").className = `status-dot ${environment.warnings?.length ? "warn" : ""}`;
  populateGpuControls(environment);
}

async function loadEnvironment(force = false) {
  const endpoint = "/api/environment";
  const environment = await api(`${endpoint}${force ? "?refresh=1" : ""}`);
  state.environment = environment;
  renderEnvironment(environment);
}

function renderApiMatches(items) {
  state.apiMatches = items;
  if (!items.length) {
    $("apiMatches").innerHTML = `<div class="empty">没有匹配的 API。</div>`;
    return;
  }
  $("apiMatches").innerHTML = items.map((item) => {
    const counts = item.result_counts || {};
    const countText = sumCounts(counts) ? `已有结果 ${sumCounts(counts)}` : "暂无结果";
    const active = state.selectedApi?.api === item.api && state.selectedApi?.lib === item.lib;
    return `
      <button class="match-item ${active ? "active" : ""}" data-api="${escapeHtml(item.api)}" aria-pressed="${active ? "true" : "false"}">
        <span><code>${escapeHtml(item.api)}</code></span>
        <small>${item.has_prompt ? "约束就绪" : "缺少约束"} · ${escapeHtml(countText)}</small>
      </button>
    `;
  }).join("");
  document.querySelectorAll("[data-api]").forEach((btn) => {
    btn.addEventListener("click", () => selectApi(btn.dataset.api));
  });
}

function markSelectedApiButton() {
  document.querySelectorAll("[data-api]").forEach((btn) => {
    const active = state.selectedApi?.api === btn.dataset.api;
    btn.classList.toggle("active", active);
    btn.setAttribute("aria-pressed", active ? "true" : "false");
  });
}

async function searchApis(autoSelect = true) {
  const lib = $("apiLib").value;
  const q = $("apiSearch").value.trim();
  const limit = q ? 200 : 5000;
  const data = await api(`/api/apis?lib=${encodeURIComponent(lib)}&q=${encodeURIComponent(q)}&limit=${limit}`);
  renderApiMatches(data);
  if (autoSelect && !state.selectedApi && data.length) {
    await selectApi(data[0].api);
  }
}

function renderApiDetail(detail) {
  const counts = detail.result_counts || {};
  const latest = detail.latest_job;
  const latestText = latest
    ? `${latest.job_id} · ${latest.status}${latest.error ? " · 有错误" : ""}`
    : "暂无运行记录";
  $("apiDetail").innerHTML = `
    <div class="detail-grid">
      <div><span>API</span><code>${escapeHtml(detail.api)}</code></div>
      <div><span>框架</span><strong>${escapeHtml(detail.lib)}</strong></div>
      <div><span>约束状态</span><strong>${detail.has_prompt ? "就绪" : "缺失"}</strong></div>
      <div><span>已有结果</span><strong>${sumCounts(counts)}</strong></div>
    </div>
    <div class="file-row"><span>最近运行</span><code>${escapeHtml(latestText)}</code></div>
    <div class="file-row"><span>API 清单</span><code>${escapeHtml(detail.api_list)}</code></div>
    <div class="file-row"><span>约束路径</span><code>${escapeHtml(detail.prompt_path)}</code></div>
    <div class="file-row"><span>Results</span><code>${escapeHtml(detail.results_path)}</code></div>
    <div class="mini-counts">
      ${Object.entries(counts).map(([name, value]) => `<span>${escapeHtml(name)}: <b>${escapeHtml(value)}</b></span>`).join("")}
    </div>
  `;
}

async function selectApi(apiName, options = {}) {
  const lib = $("apiLib").value;
  if (state.apiPollTimer) {
    clearInterval(state.apiPollTimer);
    state.apiPollTimer = null;
  }
  const detail = await api(`/api/api-detail?lib=${encodeURIComponent(lib)}&api=${encodeURIComponent(apiName)}`);
  state.selectedApi = detail;
  $("startApiRun").disabled = !detail.has_prompt;
  renderApiDetail(detail);
  markSelectedApiButton();

  if (detail.latest_job?.job_id) {
    state.currentApiJob = detail.latest_job.job_id;
    await loadApiJob({ fromSelection: true });
    if (["running", "pending"].includes(detail.latest_job.status)) {
      state.apiPollTimer = setInterval(() => loadApiJob({ fromSelection: true }), 1000);
    }
  } else if (!options.keepJob) {
    state.currentApiJob = null;
    renderApiStages({}, {});
    $("apiJobSummary").innerHTML = `
      <div class="empty">当前 API 暂无运行记录。点击“运行该 API”后，这里会显示任务摘要。</div>
    `;
    $("apiJobLogs").textContent = "";
  }
}

function renderApiStages(status, summary = {}) {
  const stages = status?.stages || {};
  const mutationModel =
    summary.mutation_model ||
    status?.mutation_model ||
    state.selectedApi?.latest_job?.mutation_model ||
    "";
  const names = [
    ["prompt_check", "约束检查"],
    ["qwen_seed", "Qwen 种子生成"],
    ["ev_generation", mutationModelLabel(mutationModel)],
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
    cuda_device: $("apiGpuSelect").value,
  };
  const data = await post("/api/run-api", payload);
  state.currentApiJob = data.job_id;
  $("apiJobSummary").innerHTML = `
    <div class="detail-grid">
      <div><span>Job</span><code>${escapeHtml(data.job_id)}</code></div>
      <div><span>模式</span><strong>${escapeHtml(modeLabel(payload.mode))}</strong></div>
      <div><span>状态</span><strong>running</strong></div>
      <div><span>输出目录</span><code>${escapeHtml(data.out)}</code></div>
    </div>
  `;
  if (state.apiPollTimer) clearInterval(state.apiPollTimer);
  state.apiPollTimer = setInterval(loadApiJob, 1000);
  await loadApiJob();
}

function renderApiJobSummary(data) {
  const summary = data.summary || {};
  const status = data.status || {};
  const counts = summary.result_counts || {};
  const shownStatus = summary.status || status.status || "pending";
  const error = summary.error || status.error || "";
  $("apiJobSummary").innerHTML = `
    <div class="detail-grid">
      <div><span>Job</span><code>${escapeHtml(data.job_id)}</code></div>
      <div><span>模式</span><strong>${escapeHtml(modeLabel(summary.mode || status.mode))}</strong></div>
      <div><span>状态</span><strong>${escapeHtml(shownStatus)}</strong></div>
      <div><span>Qwen valid seed</span><strong>${escapeHtml(summary.qwen_valid_seed_count ?? "-")}</strong></div>
      <div><span>Trace 命中</span><strong>${escapeHtml(summary.catch_count ?? "-")}</strong></div>
      <div><span>输出目录</span><code>${escapeHtml(data.out)}</code></div>
    </div>
    <div class="mini-counts">
      ${Object.entries(counts).map(([name, value]) => `<span>${escapeHtml(name)}: <b>${escapeHtml(value)}</b></span>`).join("") || "<span>暂无结果计数</span>"}
    </div>
    ${error ? `<div class="text-block error-text"><b>错误</b><p>${escapeHtml(error)}</p></div>` : ""}
  `;
}

async function refreshSelectedApiAfterJob() {
  if (!state.selectedApi) return;
  const apiName = state.selectedApi.api;
  const lib = state.selectedApi.lib;
  if ($("apiLib").value !== lib) return;
  const detail = await api(`/api/api-detail?lib=${encodeURIComponent(lib)}&api=${encodeURIComponent(apiName)}`);
  state.selectedApi = detail;
  renderApiDetail(detail);
  await searchApis(false);
  markSelectedApiButton();
}

async function loadApiJob() {
  if (!state.currentApiJob) return;
  const data = await api(`/api/api-jobs/${encodeURIComponent(state.currentApiJob)}`);
  renderApiStages(data.status, data.summary);
  renderApiJobSummary(data);
  $("apiJobLogs").textContent = Object.entries(data.logs || {})
    .map(([name, content]) => `===== ${name} =====\n${content}`)
    .join("\n\n");
  const status = data.status?.status;
  if (status === "success" || status === "failed") {
    clearInterval(state.apiPollTimer);
    state.apiPollTimer = null;
    loadOverview().catch(console.error);
    refreshSelectedApiAfterJob().catch(console.error);
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
  $("openEnvironment").addEventListener("click", () => {
    $("environmentDrawer").hidden = false;
  });
  document.querySelectorAll("[data-close-environment]").forEach((button) => {
    button.addEventListener("click", () => {
      $("environmentDrawer").hidden = true;
    });
  });
  $("refreshEnvironment").addEventListener("click", () => loadEnvironment(true).catch(alertError));
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
  renderApiStages({}, {});
  await Promise.all([
    loadEnvironment(),
    loadOverview(),
    searchApis(),
    loadConfirmedBugs(),
  ]);
}

init().catch(alertError);
