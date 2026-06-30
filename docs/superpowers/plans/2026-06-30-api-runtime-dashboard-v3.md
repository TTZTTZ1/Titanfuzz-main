# API Runtime Dashboard V3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved V3 runtime dashboard with meaningful driver progress and safe latest-run retention.

**Architecture:** Extend the structured metric snapshot with incremental driver progress, then consume that field through the existing Vue domain layer. Recompose only the lower runtime dashboard and prune superseded ordinary jobs after candidate collection while protecting candidate-linked jobs.

**Tech Stack:** Python 3, Vue 3, TypeScript, ECharts, Vitest.

---

### Task 1: Incremental driver metrics

**Files:**
- Modify: `scripts/demo_metrics.py`
- Modify: `test/test_demo_metrics.py`
- Modify: `webapp/frontend/src/types/tensorguard.ts`
- Modify: `webapp/frontend/src/domain/apiRun.ts`
- Modify: `webapp/frontend/src/domain/chartOptions.test.ts`

- [ ] Add a failing test where two valid `TitanFuzzTestcase` records produce `tested_cases == 2`.
- [ ] Count valid trace summaries and expose `tested_cases` in every result snapshot.
- [ ] Replace the driver chart's `total_files`, `crash`, and `flaky` series with `tested_cases` and `trace_hits`.
- [ ] Verify Python metric tests and chart-domain tests.

### Task 2: Chart styling and V3 dashboard layout

**Files:**
- Modify: `webapp/frontend/src/components/api/StageChart.vue`
- Modify: `webapp/frontend/src/components/api/StageChart.test.ts`
- Modify: `webapp/frontend/src/views/ApiRunView.vue`
- Modify: `webapp/frontend/src/views/ApiRunView.test.ts`
- Modify: `webapp/frontend/src/components/api/GpuChart.vue`

- [ ] Add failing assertions for Chinese axis captions and V3 component placement.
- [ ] Restyle axes, tooltip, grid, and chart proportions without changing the upper page.
- [ ] Place chart above the `GPU → summary → Results` strip and make the live log the full right column.
- [ ] Verify focused component and view tests.

### Task 3: Safe latest-run retention

**Files:**
- Modify: `scripts/run_one_api_demo.py`
- Modify: `test/test_demo_pipeline_behavior.py`

- [ ] Add failing tests proving superseded terminal jobs are removed and candidate-linked or active jobs are protected.
- [ ] Add a same-API pruning helper called only after candidate collection and final status persistence.
- [ ] Verify pipeline behavior tests.

### Task 4: Integrated verification

**Files:**
- Modify generated assets under `webapp/static/`

- [ ] Run all Python regression scripts relevant to jobs, metrics, candidates, and frontend contracts.
- [ ] Run all frontend tests.
- [ ] Build production assets.
- [ ] Verify the rendered API page at desktop and compact widths with no console errors or horizontal overflow.
