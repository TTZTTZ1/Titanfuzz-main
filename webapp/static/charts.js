(function () {
  "use strict";

  const NS = "http://www.w3.org/2000/svg";
  const COLORS = ["#087f73", "#2f67a6", "#a76505", "#b52a35", "#6a5aa3", "#657178", "#18794e"];

  function targetElement(target) {
    return typeof target === "string" ? document.getElementById(target) : target;
  }

  function empty(target, message) {
    const element = targetElement(target);
    if (!element) return;
    element.innerHTML = `<div class="chart-empty">${message || "当前阶段尚无指标数据"}</div>`;
  }

  function node(name, attributes = {}) {
    const element = document.createElementNS(NS, name);
    Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
    return element;
  }

  function renderLineChart(target, series, options = {}) {
    const element = targetElement(target);
    const visible = (series || []).filter((item) => Array.isArray(item.points) && item.points.length);
    if (!element || !visible.length) {
      empty(element, options.emptyMessage);
      return;
    }

    const width = 760;
    const height = 260;
    const pad = { top: 22, right: 22, bottom: 38, left: 48 };
    const points = visible.flatMap((item) => item.points).filter((point) => Number.isFinite(point.x) && Number.isFinite(point.y));
    if (!points.length) {
      empty(element, options.emptyMessage);
      return;
    }
    const xMax = Math.max(...points.map((point) => point.x), 1);
    const yMax = Math.max(...points.map((point) => point.y), 1);
    const x = (value) => pad.left + value / xMax * (width - pad.left - pad.right);
    const y = (value) => height - pad.bottom - value / yMax * (height - pad.top - pad.bottom);

    element.innerHTML = "";
    const svg = node("svg", { viewBox: `0 0 ${width} ${height}`, role: "img", "aria-label": options.label || "运行指标折线图" });
    [0, .25, .5, .75, 1].forEach((ratio) => {
      const lineY = y(yMax * ratio);
      svg.appendChild(node("line", { x1: pad.left, y1: lineY, x2: width - pad.right, y2: lineY, class: "chart-grid-line" }));
      const text = node("text", { x: pad.left - 9, y: lineY + 4, class: "chart-axis-label", "text-anchor": "end" });
      text.textContent = String(Math.round(yMax * ratio * 100) / 100);
      svg.appendChild(text);
    });
    visible.forEach((item, index) => {
      const usable = item.points.filter((point) => Number.isFinite(point.x) && Number.isFinite(point.y));
      const path = usable.map((point, pointIndex) => `${pointIndex ? "L" : "M"}${x(point.x)},${y(point.y)}`).join(" ");
      svg.appendChild(node("path", { d: path, fill: "none", stroke: item.color || COLORS[index % COLORS.length], class: "chart-series-line" }));
      usable.forEach((point) => svg.appendChild(node("circle", { cx: x(point.x), cy: y(point.y), r: 2.6, fill: item.color || COLORS[index % COLORS.length] })));
    });
    const xLabel = node("text", { x: width - pad.right, y: height - 11, class: "chart-axis-label", "text-anchor": "end" });
    xLabel.textContent = options.xLabel || "elapsed seconds";
    svg.appendChild(xLabel);
    element.appendChild(svg);
    const legend = document.createElement("div");
    legend.className = "chart-legend";
    legend.innerHTML = visible.map((item, index) => `<span><i style="background:${item.color || COLORS[index % COLORS.length]}"></i>${item.label}</span>`).join("");
    element.appendChild(legend);
  }

  function renderStackedBar(target, values, options = {}) {
    const element = targetElement(target);
    if (!element) return;
    const items = (values || []).filter((item) => Number(item.value) > 0);
    const total = items.reduce((sum, item) => sum + Number(item.value), 0);
    if (!total) {
      empty(element, options.emptyMessage || "当前尚未生成结果文件");
      return;
    }
    element.innerHTML = `
      <div class="stacked-bar" role="img" aria-label="${options.label || "结果文件构成"}">
        ${items.map((item, index) => `<span style="width:${Number(item.value) / total * 100}%;background:${item.color || COLORS[index % COLORS.length]}" title="${item.label}: ${item.value}"></span>`).join("")}
      </div>
      <div class="chart-legend">${items.map((item, index) => `<span><i style="background:${item.color || COLORS[index % COLORS.length]}"></i>${item.label} · ${item.value}</span>`).join("")}</div>
    `;
  }

  function renderProgress(target, value, max, options = {}) {
    const element = targetElement(target);
    if (!element) return;
    const safeMax = Math.max(Number(max) || 0, 1);
    const safeValue = Math.max(0, Math.min(Number(value) || 0, safeMax));
    const percent = safeValue / safeMax * 100;
    element.innerHTML = `
      <div class="progress-label"><span>${options.label || "进度"}</span><b>${safeValue} / ${safeMax}</b></div>
      <div class="progress-track"><span style="width:${percent}%"></span></div>
    `;
  }

  window.TensorCharts = { renderLineChart, renderStackedBar, renderProgress };
})();
