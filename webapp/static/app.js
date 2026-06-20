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
  latestApiPayload: null,
  selectedApiStage: null,
  followLiveStage: true,
  selectedResultCategory: "crash",
  selectedResultFile: null,
  bugSource: "confirmed",
  candidates: [],
  selectedCandidateId: null,
  currentBugDetail: null,
  reportMarkdown: "",
};

const resultCategories = ["seed", "valid", "exception", "crash", "notarget", "hangs", "flaky"];
const resultCategoryLabels = {
  seed: "种子", valid: "有效", exception: "异常", crash: "崩溃",
  notarget: "无目标", hangs: "超时", flaky: "不稳定",
};
const stageDefinitions = [
  { key: "qwen_seed", label: "Qwen 种子", metricKeys: [["候选", "qwen_raw"], ["有效种子", "qwen_valid"]] },
  { key: "ev_generation", label: "InCoder 变异", metricKeys: [["有效", "valid"], ["异常", "exception"], ["崩溃", "crash"], ["超时", "hangs"]] },
  { key: "driver", label: "差异检测", metricKeys: [["已检查程序", "total_files"], ["差异 Catch", "trace_hits"], ["崩溃", "crash"], ["不稳定", "flaky"]] },
];

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

function modelName(value) {
  const text = String(value || "");
  return text ? text.split("/").filter(Boolean).pop() : "未记录";
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
  const expectedTotal = Number(data.api_by_lib?.torch || 0) + Number(data.api_by_lib?.tf || 0);
  const overviewCheck = $("overviewDataCheck");
  overviewCheck.hidden = false;
  overviewCheck.className = `data-check ${expectedTotal === Number(data.api_total) ? "ok" : ""}`;
  overviewCheck.textContent = expectedTotal === Number(data.api_total)
    ? `数据校验通过：${data.api_total} = PyTorch ${data.api_by_lib?.torch || 0} + TensorFlow ${data.api_by_lib?.tf || 0}`
    : `数据校验失败：API 总数 ${data.api_total} 与框架分项 ${expectedTotal} 不一致`;
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

  const reproByBug = new Map();
  (data.latest_repro_jobs || []).forEach((job) => {
    if (!reproByBug.has(job.bug_id)) reproByBug.set(job.bug_id, job);
  });
  const bugRows = bugs.slice(0, 8).map((bug) => {
    const latestRepro = reproByBug.get(bug.id);
    const currentStatusLabels = { finished: "本机已运行", running: "正在复现", pending: "等待复现", failed: "复现任务失败" };
    const currentStatus = latestRepro ? (currentStatusLabels[latestRepro.status] || latestRepro.status) : "尚未在本机运行";
    return `
    <tr>
      <td><strong>${escapeHtml(bug.display_id || bug.id)}</strong></td>
      <td><code>${escapeHtml(bug.api)}</code></td>
      <td>${escapeHtml(bug.bug_type || bug.title || "")}</td>
      <td>${escapeHtml(currentStatus)}</td>
      <td>${bug.status === "confirmed" || !bug.status ? "已确认" : escapeHtml(bug.status)}</td>
      <td><button class="text-action" data-open-bug="${escapeHtml(bug.id)}">查看证据</button></td>
    </tr>
  `; }).join("");
  $("bugSummary").innerHTML = `
    <table>
      <thead><tr><th>编号</th><th>API</th><th>失效类型</th><th>当前环境复现</th><th>证据状态</th><th></th></tr></thead>
      <tbody>${bugRows || `<tr><td colspan="6">暂无数据</td></tr>`}</tbody>
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
  if (state.selectedBugId && state.bugSource === "confirmed") renderReproProfiles();
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
  $("environmentBrief").textContent = gpus.length
    ? `${gpus.map((gpu) => gpu.name).join(" / ")} · Python ${python.version || "-"}`
    : `未检测到 GPU · Python ${python.version || "-"}`;
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
    state.latestApiPayload = null;
    state.selectedApiStage = null;
    state.followLiveStage = true;
    state.selectedResultFile = null;
    $("apiDataCheck").hidden = true;
    renderApiStages({}, {});
    renderApiVisualization();
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

function liveStageKey(status) {
  const stages = status?.stages || {};
  const running = stageDefinitions.find((stage) => stages[stage.key] === "running");
  if (running) return running.key;
  const started = [...stageDefinitions].reverse().find((stage) => ![undefined, "pending", "skipped"].includes(stages[stage.key]));
  return started?.key || "qwen_seed";
}

function renderStageTabs(status) {
  const stages = status?.stages || {};
  const live = liveStageKey(status);
  if (state.followLiveStage || !state.selectedApiStage) state.selectedApiStage = live;
  $("followLiveStage").hidden = state.followLiveStage || state.selectedApiStage === live;
  $("apiStageTabs").innerHTML = stageDefinitions.map((stage) => {
    const value = stages[stage.key] || "pending";
    const disabled = ["pending", "skipped"].includes(value);
    return `<button class="stage-tab ${state.selectedApiStage === stage.key ? "active" : ""}" role="tab" data-stage-tab="${stage.key}" ${disabled ? "disabled" : ""} aria-selected="${state.selectedApiStage === stage.key}">${escapeHtml(stage.label)}<small>${escapeHtml(value)}</small></button>`;
  }).join("");
  document.querySelectorAll("[data-stage-tab]").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedApiStage = button.dataset.stageTab;
      state.followLiveStage = false;
      renderApiVisualization();
    });
  });
}

function stageSeries(metrics, stage) {
  const rows = (metrics || []).filter((row) => row.stage === stage.key);
  return stage.metricKeys.map(([label, key], index) => ({
    label,
    color: ["#087f73", "#2f67a6", "#a76505", "#b52a35"][index],
    points: rows.map((row) => ({ x: Number(row.elapsed_seconds || 0), y: Number(row[key] || 0) })),
  })).filter((series) => series.points.length);
}

function latestResultCounts(data) {
  const metrics = data?.metrics || [];
  const last = metrics[metrics.length - 1] || {};
  const summaryCounts = data?.summary?.result_counts || {};
  return Object.fromEntries(resultCategories.map((category) => [category, Number(summaryCounts[category] ?? last[category] ?? 0)]));
}

function renderApiVisualization() {
  const data = state.latestApiPayload || {};
  const status = data.status || {};
  renderStageTabs(status);
  const stage = stageDefinitions.find((item) => item.key === state.selectedApiStage) || stageDefinitions[0];
  const stageStatus = status.stages?.[stage.key] || "pending";
  $("apiStageChartTitle").textContent = stage.label;
  $("apiStageChartMeta").textContent = `${stageStatus} · ${stageSeries(data.metrics, stage)[0]?.points.length || 0} 次采样`;
  window.TensorCharts.renderLineChart("apiStageChart", stageSeries(data.metrics, stage), {
    label: `${stage.label}指标`,
    xLabel: "阶段耗时（秒）",
    emptyMessage: stageStatus === "pending" ? "该阶段尚未开始" : "该阶段暂无可用采样",
  });

  const counts = latestResultCounts(data);
  window.TensorCharts.renderStackedBar("apiResultComposition", resultCategories.map((category) => ({
    label: resultCategoryLabels[category], value: counts[category],
  })));
  renderGpuChart(data.metrics || []);
  renderResultExplorer(data.result_files || {}, counts);
  renderSelectedStageLog();
}

function renderGpuChart(metrics) {
  const utilization = metrics.map((row, index) => ({
    x: index,
    y: row.gpu && Number.isFinite(Number(row.gpu.utilization_percent)) ? Number(row.gpu.utilization_percent) : null,
  }));
  const memory = metrics.map((row, index) => ({
    x: index,
    y: row.gpu && Number(row.gpu.memory_total_mib) > 0 && Number.isFinite(Number(row.gpu.memory_used_mib))
      ? Number(row.gpu.memory_used_mib) / Number(row.gpu.memory_total_mib) * 100
      : null,
  }));
  window.TensorCharts.renderLineChart("gpuChart", [
    { label: "GPU 利用率 %", color: "#087f73", points: utilization },
    { label: "显存占比 %", color: "#a76505", points: memory },
  ], { label: "GPU 利用率与显存占比", xLabel: "采样序号", emptyMessage: "当前任务尚无 GPU 采样" });
}

function renderResultExplorer(filesByCategory, counts) {
  if (!resultCategories.includes(state.selectedResultCategory)) state.selectedResultCategory = "crash";
  $("resultCategoryTabs").innerHTML = resultCategories.map((category) => `
    <button class="result-category-tab ${state.selectedResultCategory === category ? "active" : ""}" data-result-category="${category}">${resultCategoryLabels[category]}<b>${escapeHtml(counts[category] || 0)}</b></button>
  `).join("");
  document.querySelectorAll("[data-result-category]").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedResultCategory = button.dataset.resultCategory;
      state.selectedResultFile = null;
      renderResultExplorer(filesByCategory, counts);
    });
  });

  const files = filesByCategory[state.selectedResultCategory] || [];
  $("resultFileList").innerHTML = files.map((file, index) => `
    <button class="result-file-button ${state.selectedResultFile?.path === file.path ? "active" : ""}" data-result-file-index="${index}">
      <code title="${escapeHtml(file.name)}">${escapeHtml(file.name)}</code>
      ${file.recommended ? `<span class="recommend-mark">建议审查</span>` : ""}
      <small>${escapeHtml(file.size_bytes)} bytes</small>
    </button>
  `).join("") || `<div class="empty">该分类暂无文件</div>`;
  document.querySelectorAll("[data-result-file-index]").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedResultFile = files[Number(button.dataset.resultFileIndex)];
      renderResultExplorer(filesByCategory, counts);
    });
  });
  const selected = state.selectedResultFile;
  $("resultFileMeta").innerHTML = selected
    ? `<code>${escapeHtml(selected.path)}</code>${selected.recommended ? ` <span class="pill status-running">系统建议审查</span>` : ""}`
    : "请选择结果文件";
  $("resultSourcePreview").textContent = selected?.source_excerpt || "";
  $("addCandidate").textContent = "加入候选";
  $("addCandidate").disabled = !selected || state.selectedResultCategory === "seed";
}

function renderSelectedStageLog() {
  const data = state.latestApiPayload || {};
  const logNames = {
    qwen_seed: "01_qwen_seed.log",
    ev_generation: "02_ev_generation.log",
    driver: "03_driver.log",
  };
  const name = logNames[state.selectedApiStage];
  $("apiLogStageLabel").textContent = name || "当前任务输出";
  $("apiJobLogs").textContent = name && data.logs?.[name]
    ? data.logs[name]
    : Object.entries(data.logs || {}).map(([logName, content]) => `===== ${logName} =====\n${content}`).join("\n\n");
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
  $("startApiRun").disabled = true;
  state.currentApiJob = data.job_id;
  state.latestApiPayload = null;
  state.selectedApiStage = "qwen_seed";
  state.followLiveStage = true;
  state.selectedResultFile = null;
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
  const parameters = status.parameters || {};
  $("apiJobSummary").innerHTML = `
    <div class="detail-grid">
      <div><span>Job</span><code>${escapeHtml(data.job_id)}</code></div>
      <div><span>模式</span><strong>${escapeHtml(modeLabel(summary.mode || status.mode))}</strong></div>
      <div><span>状态</span><strong>${escapeHtml(shownStatus)}</strong></div>
      <div><span>计算设备</span><strong>${escapeHtml(status.cuda_device ?? "-")}</strong></div>
      <div><span>Qwen 模型</span><code title="${escapeHtml(status.qwen_model)}">${escapeHtml(modelName(status.qwen_model))}</code></div>
      <div><span>变异模型</span><code title="${escapeHtml(status.mutation_model)}">${escapeHtml(modelName(status.mutation_model))}</code></div>
      <div><span>Qwen 预算</span><strong>${escapeHtml(parameters.qwen_per_api_budget ?? "-")}s</strong></div>
      <div><span>最大有效程序</span><strong>${escapeHtml(parameters.ev_max_valid ?? "-")}</strong></div>
      <div><span>Batch size</span><strong>${escapeHtml(parameters.ev_batch_size ?? "-")}</strong></div>
      <div><span>Seed pool</span><strong>${escapeHtml(parameters.seed_pool_size ?? "-")}</strong></div>
      <div><span>有效 Qwen 种子</span><strong>${escapeHtml(summary.qwen_valid_seed_count ?? "-")}</strong></div>
      <div><span>Trace 命中</span><strong>${escapeHtml(summary.catch_count ?? "-")}</strong></div>
    </div>
    <div class="mini-counts">
      ${Object.entries(counts).map(([name, value]) => `<span>${escapeHtml(name)}: <b>${escapeHtml(value)}</b></span>`).join("") || "<span>暂无结果计数</span>"}
    </div>
    ${error ? `<div class="text-block error-text"><b>错误</b><p>${escapeHtml(error)}</p></div>` : ""}
  `;
}

function renderApiDataCheck(data) {
  const check = $("apiDataCheck");
  const status = data.status?.status;
  if (!["success", "failed"].includes(status)) {
    check.hidden = true;
    return;
  }
  const summaryCounts = data.summary?.result_counts || {};
  const fileCounts = Object.fromEntries(resultCategories.map((category) => [category, (data.result_files?.[category] || []).length]));
  const lastMetric = (data.metrics || []).at(-1) || {};
  const mismatches = [];
  resultCategories.forEach((category) => {
    if (Number(summaryCounts[category] || 0) !== fileCounts[category]) mismatches.push(`${category}: summary=${summaryCounts[category] || 0}, files=${fileCounts[category]}`);
    if (data.metrics?.length && Number(lastMetric[category] || 0) !== fileCounts[category]) mismatches.push(`${category}: metric=${lastMetric[category] || 0}, files=${fileCounts[category]}`);
  });
  check.hidden = false;
  check.className = `data-check ${mismatches.length ? "" : "ok"}`;
  check.textContent = mismatches.length ? `数据校验警告：${mismatches.join("；")}` : "数据校验通过：最终指标、Summary 与当前 Job 的 Results 文件一致";
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
  state.latestApiPayload = data;
  renderApiStages(data.status, data.summary);
  renderApiJobSummary(data);
  renderApiDataCheck(data);
  renderApiVisualization();
  const status = data.status?.status;
  $("startApiRun").disabled = ["running", "pending"].includes(status) || !state.selectedApi?.has_prompt;
  if (status === "success" || status === "failed") {
    clearInterval(state.apiPollTimer);
    state.apiPollTimer = null;
    loadOverview().catch(console.error);
    refreshSelectedApiAfterJob().catch(console.error);
  }
}

async function addSelectedCandidate() {
  const file = state.selectedResultFile;
  const status = state.latestApiPayload?.status || {};
  if (!file || !state.currentApiJob || !state.selectedApi) return;
  const button = $("addCandidate");
  button.disabled = true;
  const record = await post("/api/candidates", {
    job_id: state.currentApiJob,
    lib: status.lib || state.selectedApi.lib,
    api: status.api || state.selectedApi.api,
    category: state.selectedResultCategory,
    source_path: file.path,
  });
  button.textContent = `${record.id} 已加入候选`;
}

function bugMatches(item, query) {
  const haystack = [item.id, item.display_id, item.api, item.framework, item.bug_type, item.title, item.category, item.status].join(" ").toLowerCase();
  return haystack.includes(query.toLowerCase());
}

function renderBugList() {
  const query = $("bugSearch").value.trim();
  const items = (state.bugSource === "confirmed" ? state.confirmedBugs : state.candidates).filter((item) => bugMatches(item, query));
  $("confirmedBugList").innerHTML = items.map((item) => {
    const id = state.bugSource === "confirmed" ? item.id : item.id;
    const active = state.bugSource === "confirmed" ? state.selectedBugId === id : state.selectedCandidateId === id;
    return `<button class="bug-item ${active ? "active" : ""}" data-evidence-id="${escapeHtml(id)}">
      <strong>${escapeHtml(item.display_id || item.id)}</strong>
      <span>${escapeHtml(item.framework || item.lib)} · ${escapeHtml(item.api)}</span>
      <small>${escapeHtml(item.bug_type || item.category || item.title || "")}</small>
    </button>`;
  }).join("") || `<div class="empty">没有匹配的记录</div>`;
  document.querySelectorAll("[data-evidence-id]").forEach((button) => {
    button.addEventListener("click", () => {
      const action = state.bugSource === "confirmed" ? selectConfirmedBug(button.dataset.evidenceId) : selectCandidate(button.dataset.evidenceId);
      action.catch(alertError);
    });
  });
}

async function loadConfirmedBugs() {
  const [bugs, candidates] = await Promise.all([api("/api/confirmed-bugs"), api("/api/candidates")]);
  state.confirmedBugs = bugs;
  state.candidates = candidates;
  renderBugList();
  if (state.confirmedBugs.length && !state.selectedBugId) await selectConfirmedBug(state.confirmedBugs[0].id);
}

function renderReproProfiles() {
  const gpus = state.environment?.gpus || [];
  const profiles = [
    { mode: "cpu", title: "隐藏 CUDA 设备", detail: "CUDA_VISIBLE_DEVICES 为空" },
    ...gpus.map((gpu) => ({ mode: `gpu:${gpu.index}`, title: `设备 ${gpu.index} 可见`, detail: `${gpu.name} · ${gpu.memory_total_mib ?? "-"} MiB` })),
  ];
  $("reproProfileControls").innerHTML = profiles.map((profile) => `
    <label class="profile-option"><input type="checkbox" value="${escapeHtml(profile.mode)}" checked /><span>${escapeHtml(profile.title)}<small>${escapeHtml(profile.detail)}</small></span></label>
  `).join("");
}

function resetReproRun() {
  if (state.reproPollTimer) clearInterval(state.reproPollTimer);
  state.reproPollTimer = null;
  state.currentReproJob = null;
  state.reportMarkdown = "";
  $("reproLogs").textContent = "";
  $("reproEvidence").innerHTML = `<div class="empty">尚未启动复现</div>`;
  $("reproEnvironment").innerHTML = "";
  $("reportPreview").innerHTML = `<div class="empty">完成复现后可生成报告</div>`;
  $("generateReport").textContent = "生成报告";
  $("generateReport").disabled = true;
  $("downloadReport").disabled = true;
  $("printReport").disabled = true;
}

async function selectConfirmedBug(id) {
  const detail = await api(`/api/confirmed-bugs/${encodeURIComponent(id)}`);
  state.bugSource = "confirmed";
  state.selectedBugId = id;
  state.currentBugDetail = detail;
  document.querySelectorAll("[data-bug-source]").forEach((button) => button.classList.toggle("active", button.dataset.bugSource === "confirmed"));
  renderBugList();
  resetReproRun();
  const meta = detail.meta || {};
  $("confirmedBugDetail").innerHTML = `
    <div class="detail-grid">
      <div><span>编号</span><strong>${escapeHtml(detail.display_id || meta.id)}</strong></div>
      <div><span>框架</span><strong>${escapeHtml(meta.framework)}</strong></div>
      <div><span>API</span><code>${escapeHtml(meta.api)}</code></div>
      <div><span>问题类型</span><strong>${escapeHtml(meta.bug_type)}</strong></div>
    </div>
    <div class="file-row"><span>触发条件</span><code>${escapeHtml(meta.trigger)}</code></div>
  `;
  $("bugExplanation").innerHTML = `
    <div class="behavior-panel expected"><b>预期行为</b><p>${escapeHtml(meta.expected)}</p></div>
    <div class="behavior-panel observed"><b>已知观测</b><p>${escapeHtml(meta.observed)}</p></div>
  `;
  $("reproCode").textContent = detail.repro_code || "";
  renderReproProfiles();
  $("runSelectedRepro").disabled = false;
}

async function selectCandidate(id) {
  const detail = await api(`/api/candidates/${encodeURIComponent(id)}`);
  state.bugSource = "candidates";
  state.selectedCandidateId = id;
  state.currentBugDetail = detail;
  renderBugList();
  resetReproRun();
  $("confirmedBugDetail").innerHTML = `
    <div class="detail-grid">
      <div><span>候选编号</span><strong>${escapeHtml(detail.id)}</strong></div>
      <div><span>状态</span><strong>${escapeHtml(detail.status)}</strong></div>
      <div><span>API</span><code>${escapeHtml(detail.api)}</code></div>
      <div><span>结果分类</span><strong>${escapeHtml(detail.category)}</strong></div>
    </div>
    <div class="button-row candidate-review-actions">
      <button class="secondary" data-candidate-status="needs_review">保留人工复核</button>
      <button class="secondary" data-candidate-status="rejected">排除该候选</button>
    </div>
  `;
  $("bugExplanation").innerHTML = `
    <div class="behavior-panel expected"><b>候选含义</b><p>该记录来自一次具体运行结果，尚未进入已确认问题库。</p></div>
    <div class="behavior-panel observed"><b>当前依据</b><p>${escapeHtml(!detail.source_exists ? "原始 Job 文件已缺失，当前证据不完整。" : detail.recommended ? "命中系统建议审查规则，需要人工最小化与复现。" : "由用户加入候选，需要人工检查其异常语义。")}</p></div>
  `;
  $("reproCode").textContent = detail.source_code || "";
  $("reproProfileControls").innerHTML = `<div class="empty">候选记录需要先完成人工最小化，网页不会直接提升为已确认 Bug。</div>`;
  $("runSelectedRepro").disabled = true;
  document.querySelectorAll("[data-candidate-status]").forEach((button) => {
    button.addEventListener("click", () => updateCandidateStatus(detail.id, button.dataset.candidateStatus).catch(alertError));
  });
}

async function updateCandidateStatus(candidateId, candidateStatus) {
  const updated = await post(`/api/candidates/${encodeURIComponent(candidateId)}/status`, { status: candidateStatus });
  state.candidates = state.candidates.map((item) => item.id === candidateId ? updated : item);
  await selectCandidate(candidateId);
}

function selectedReproModes() {
  return [...document.querySelectorAll("#reproProfileControls input:checked")].map((input) => input.value);
}

async function startRepro() {
  if (!state.selectedBugId || state.bugSource !== "confirmed") return;
  const modes = selectedReproModes();
  if (!modes.length) throw new Error("至少选择一种执行配置");
  const data = await post(`/api/confirmed-bugs/${encodeURIComponent(state.selectedBugId)}/reproduce`, { modes });
  state.currentReproJob = data.job_id;
  $("runSelectedRepro").disabled = true;
  if (state.reproPollTimer) clearInterval(state.reproPollTimer);
  state.reproPollTimer = setInterval(loadReproJob, 1000);
  await loadReproJob();
}

function renderReproEvidence(status) {
  const rows = Object.values(status?.modes || {}).map((item) => {
    const evidence = item.evidence || {};
    return `<tr>
      <td><code>${escapeHtml(item.execution_profile)}</code></td>
      <td>${statusText(item.status)}</td>
      <td>${verdictText(evidence.verdict || item.verdict)}</td>
      <td>${escapeHtml(item.returncode ?? "-")}</td>
      <td>${escapeHtml(evidence.outcome || "-")}</td>
      <td>${escapeHtml(evidence.signal || "-")}</td>
      <td>${escapeHtml(item.actual_device || "unknown")}</td>
      <td>${escapeHtml(evidence.reason || "-")}</td>
    </tr>`;
  }).join("");
  $("reproEvidence").innerHTML = `<table><thead><tr><th>执行配置</th><th>状态</th><th>规则结论</th><th>返回码</th><th>观测类型</th><th>信号</th><th>实际设备</th><th>判定依据</th></tr></thead><tbody>${rows}</tbody></table>`;
}

function renderReproEnvironment(environment) {
  const platform = environment?.platform || {};
  const python = environment?.python || {};
  const frameworks = environment?.frameworks || {};
  $("reproEnvironment").innerHTML = [
    environmentRow("平台", [platform.system, platform.release, platform.machine].filter(Boolean).join(" ")),
    environmentRow("Python", python.version),
    environmentRow("PyTorch", frameworks.torch?.version || "未安装"),
    environmentRow("TensorFlow", frameworks.tensorflow?.version || "未安装"),
    environmentRow("GPU 数量", environment?.gpus?.length || 0),
    environmentRow("采集时间", environment?.collected_at),
  ].join("");
}

function showReport(markdown) {
  state.reportMarkdown = markdown || "";
  $("generatedReport").textContent = state.reportMarkdown;
  $("reportPreview").innerHTML = state.reportMarkdown ? window.TensorMarkdown.renderSafeMarkdown(state.reportMarkdown) : `<div class="empty">报告内容为空</div>`;
  $("generateReport").textContent = "查看报告";
  $("generateReport").disabled = false;
  $("downloadReport").disabled = !state.reportMarkdown;
  $("printReport").disabled = !state.reportMarkdown;
}

async function loadReproJob() {
  if (!state.currentReproJob) return;
  const data = await api(`/api/repro-jobs/${encodeURIComponent(state.currentReproJob)}`);
  renderReproEvidence(data.status);
  renderReproEnvironment(data.environment || {});
  $("reproLogs").textContent = Object.entries(data.logs || {}).map(([name, content]) => `===== ${name} =====\n${content}`).join("\n\n");
  if (data.report_markdown) showReport(data.report_markdown);
  const done = ["finished", "failed"].includes(data.status?.status);
  if (done) {
    clearInterval(state.reproPollTimer);
    state.reproPollTimer = null;
    $("runSelectedRepro").disabled = false;
    $("generateReport").disabled = false;
  }
}

async function generateCurrentReport() {
  if (state.reportMarkdown) {
    $("reportPreview").scrollIntoView({ behavior: "smooth", block: "start" });
    return;
  }
  if (!state.currentReproJob) return;
  const data = await post(`/api/repro-jobs/${encodeURIComponent(state.currentReproJob)}/report`, {});
  showReport(data.report_markdown || "");
}

function downloadCurrentReport() {
  if (!state.reportMarkdown) return;
  const blob = new Blob([state.reportMarkdown], { type: "text/markdown;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = `${state.currentBugDetail?.display_id || state.selectedBugId || "tensorguard"}-report.md`;
  link.click();
  URL.revokeObjectURL(link.href);
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
  $("followLiveStage").addEventListener("click", () => {
    state.followLiveStage = true;
    renderApiVisualization();
  });
  $("addCandidate").addEventListener("click", () => addSelectedCandidate().catch(alertError));
  document.querySelectorAll("[data-bug-source]").forEach((button) => {
    button.addEventListener("click", async () => {
      state.bugSource = button.dataset.bugSource;
      document.querySelectorAll("[data-bug-source]").forEach((tab) => tab.classList.toggle("active", tab === button));
      renderBugList();
      const items = state.bugSource === "confirmed" ? state.confirmedBugs : state.candidates;
      if (items.length) {
        if (state.bugSource === "confirmed") await selectConfirmedBug(items[0].id);
        else await selectCandidate(items[0].id);
      }
    });
  });
  $("bugSearch").addEventListener("input", renderBugList);
  $("runSelectedRepro").addEventListener("click", () => startRepro().catch(alertError));
  $("generateReport").addEventListener("click", () => generateCurrentReport().catch(alertError));
  $("downloadReport").addEventListener("click", downloadCurrentReport);
  $("printReport").addEventListener("click", () => window.print());
}

function alertError(err) {
  alert(err.message || String(err));
}

async function init() {
  bindEvents();
  renderApiStages({}, {});
  renderApiVisualization();
  await Promise.all([
    loadEnvironment(),
    loadOverview(),
    searchApis(),
    loadConfirmedBugs(),
  ]);
}

init().catch(alertError);
