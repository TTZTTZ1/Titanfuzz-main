# Runtime Dashboard and Candidate Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the single-API dashboard stable under long logs, align its controls, give every chart series a complete and consistent legend, and reorganize candidate review into a wider two-code-panel workflow.

**Architecture:** Keep all existing APIs and job state intact. Extend frontend stage metadata with stable colors, render that metadata consistently in the chart header and ECharts series, constrain logs through CSS, and change only the layout classes of the API and candidate workbenches.

**Tech Stack:** Vue 3, TypeScript, ECharts, Vitest, Vue Test Utils, scoped CSS

---

### Task 1: Stable Stage Labels and Series Colors

**Files:**
- Modify: `webapp/frontend/src/domain/apiRun.ts`
- Modify: `webapp/frontend/src/domain/apiRun.test.ts`
- Modify: `webapp/frontend/src/domain/chartOptions.ts`
- Modify: `webapp/frontend/src/domain/chartOptions.test.ts`

- [x] **Step 1: Write failing metadata tests**

Assert that stage labels are `种子生成`, `演化变异`, and `差异检测`, and that generated chart series include stable colors. In particular, Qwen valid seeds and mutation valid programs must both use `#178263`.

- [x] **Step 2: Run domain tests and verify RED**

Run: `npm test -- --run src/domain/apiRun.test.ts src/domain/chartOptions.test.ts`

Expected: FAIL because current labels mention Qwen/InCoder and `ChartSeries` has no color.

- [x] **Step 3: Extend metric metadata and chart series**

Represent each metric as `[label, key, color]`:

```ts
{ key: "qwen_seed", label: "种子生成", metricKeys: [
  ["生成候选", "qwen_raw", "#2563eb"],
  ["有效种子", "qwen_valid", "#178263"],
] }
```

Use green for all valid series, amber for exception, red for crash/difference, gray for timeout, and blue for generated/tested totals. Return the color on every `ChartSeries`.

- [x] **Step 4: Run domain tests and verify GREEN**

Run: `npm test -- --run src/domain/apiRun.test.ts src/domain/chartOptions.test.ts`

Expected: both files pass.

### Task 2: Complete Chart Legend and Compact Chart

**Files:**
- Modify: `webapp/frontend/src/components/api/StageChart.vue`
- Modify: `webapp/frontend/src/components/api/StageChart.test.ts`

- [x] **Step 1: Write failing chart tests**

Assert that mutation renders four `.stage-chart__stat` items, each stat exposes its series color, and the ECharts series uses the same color.

- [x] **Step 2: Run StageChart tests and verify RED**

Run: `npm test -- --run src/components/api/StageChart.test.ts`

Expected: FAIL because the header currently calls `slice(0, 2)` and series colors are positional.

- [x] **Step 3: Render all series and shared swatches**

Remove the two-item slice, render a small line swatch in every metric badge, bind `--series-color`, and use each series color in ECharts `lineStyle`, `itemStyle`, and `areaStyle`. Reduce the chart canvas height from 13rem to approximately 11.5rem.

- [x] **Step 4: Run StageChart tests and verify GREEN**

Run: `npm test -- --run src/components/api/StageChart.test.ts`

Expected: all StageChart tests pass.

### Task 3: Fixed, Wrapped Live Log and Aligned Controls

**Files:**
- Modify: `webapp/frontend/src/components/api/LiveLog.vue`
- Modify: `webapp/frontend/src/components/api/LiveLog.test.ts`
- Modify: `webapp/frontend/src/views/ApiRunView.vue`
- Modify: `webapp/frontend/src/views/ApiRunView.test.ts`
- Modify: `webapp/frontend/src/components/api/RunSnapshot.vue`
- Modify: `webapp/frontend/src/components/api/ResultComposition.vue`

- [x] **Step 1: Write failing component tests**

Assert that log tabs read `种子生成`, `演化变异`, and `差异检测`, and that the API controls expose a shared equal-height class. Preserve stage switching behavior.

- [x] **Step 2: Run focused component tests and verify RED**

Run: `npm test -- --run src/components/api/LiveLog.test.ts src/views/ApiRunView.test.ts`

Expected: FAIL on old labels and missing aligned-control contract.

- [x] **Step 3: Implement constrained log and dashboard proportions**

Set the log body to `overflow-y:auto`, `overflow-x:hidden`; set log text to `width:100%`, `white-space:pre-wrap`, and `overflow-wrap:anywhere`. Give every control a common outer height. Change the dashboard columns to give the log close to half the width, reduce telemetry padding, and keep all containers at `min-width:0`.

- [x] **Step 4: Run focused component tests and verify GREEN**

Run: `npm test -- --run src/components/api/LiveLog.test.ts src/views/ApiRunView.test.ts`

Expected: both files pass.

### Task 4: Candidate Review Two-Row Workbench

**Files:**
- Modify: `webapp/frontend/src/views/BugReplayView.vue`
- Modify: `webapp/frontend/src/views/BugReplayView.test.ts`

- [x] **Step 1: Write failing candidate-layout test**

Assert that the workbench has a two-code-panel row and that the review card carries a full-width modifier below it.

- [x] **Step 2: Run BugReplayView tests and verify RED**

Run: `npm test -- --run src/views/BugReplayView.test.ts`

Expected: FAIL because all three panels currently share one grid row.

- [x] **Step 3: Implement the candidate layout**

Keep both code panels horizontally scrollable with `white-space:pre`, reduce their fixed height, and set the review card to `grid-column:1 / -1` with automatic height. Leave confirmed-Bug markup unchanged.

- [x] **Step 4: Run BugReplayView tests and verify GREEN**

Run: `npm test -- --run src/views/BugReplayView.test.ts`

Expected: all BugReplayView tests pass.

### Task 5: Full Verification

**Files:**
- Regenerate: `webapp/static/index.html`
- Regenerate: `webapp/static/assets/*`

- [x] **Step 1: Run the complete test suite**

Run: `npm test -- --run`

Expected: all test files pass.

- [x] **Step 2: Build production assets**

Run: `npm run build`

Expected: Vue type checking and Vite build succeed.

- [x] **Step 3: Verify in the browser**

Check the current desktop viewport with a synthetic long log: no page-level horizontal overflow, log wraps and scrolls vertically, all chart series are identified, controls align, and candidate review places the full-width review card below the two code panels.
