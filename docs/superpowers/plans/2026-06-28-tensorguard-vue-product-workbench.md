# TensorGuard Vue Product Workbench Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the legacy dependency-free frontend with the approved Vue 3 product-demo workbench while preserving every existing Python API, experiment workflow, result-review action, replay verdict, and report rule.

**Architecture:** Vue source lives under `webapp/frontend/` and builds into the existing `webapp/static/` directory, so `webapp/server.py` and its launch command remain unchanged. Typed service and composable layers reproduce the current `app.js` state machine; view components only render state and emit user intent. The migration is performed in an isolated worktree and switches production static assets only after all three views are connected.

**Tech Stack:** Vue 3, TypeScript, Vite, Arco Design Vue, Apache ECharts, `@lucide/vue`, Vitest, Vue Test Utils, existing Python `unittest`/`pytest` tests.

---

## File Map

### Build and entry files

- Create `webapp/frontend/package.json`: frontend dependencies and scripts.
- Create `webapp/frontend/vite.config.ts`: `/api` development proxy and production output to `webapp/static/`.
- Create `webapp/frontend/tsconfig.json`: strict TypeScript configuration.
- Create `webapp/frontend/index.html`: Vite source entry.
- Create `webapp/frontend/src/main.ts`: Vue bootstrap and global styles.
- Create `webapp/frontend/src/App.vue`: top-level shell and three-view composition.

### Shared frontend files

- Create `webapp/frontend/src/types/tensorguard.ts`: backend payload types.
- Create `webapp/frontend/src/services/http.ts`: typed request and error handling.
- Create `webapp/frontend/src/services/tensorguard.ts`: existing endpoint wrappers.
- Create `webapp/frontend/src/composables/useHashNavigation.ts`: three-view navigation without server-side route fallback.
- Create `webapp/frontend/src/composables/usePolling.ts`: lifecycle-safe polling.
- Create `webapp/frontend/src/composables/useEnvironment.ts`: environment cache and refresh.
- Create `webapp/frontend/src/styles/tokens.css`: approved visual tokens.
- Create `webapp/frontend/src/styles/global.css`: shell, responsive, reduced-motion, and print rules.
- Create `webapp/frontend/src/components/AppHeader.vue`: shared top navigation and environment status.
- Create `webapp/frontend/src/components/EnvironmentDrawer.vue`: live environment details.
- Create `webapp/frontend/src/components/AsyncState.vue`: loading, empty, and retry states.

### Overview files

- Create `webapp/frontend/src/views/OverviewView.vue`.
- Create `webapp/frontend/src/components/overview/CoverageBaseline.vue`.
- Create `webapp/frontend/src/components/overview/DetectionPipeline.vue`.
- Create `webapp/frontend/src/components/overview/ConfirmedEvidenceList.vue`.

### Single-API files

- Create `webapp/frontend/src/composables/useApiCatalog.ts`.
- Create `webapp/frontend/src/composables/useApiRun.ts`.
- Create `webapp/frontend/src/domain/apiRun.ts`: stage definitions and pure metric aggregation.
- Create `webapp/frontend/src/views/ApiRunView.vue`.
- Create `webapp/frontend/src/components/api/ApiSelector.vue`.
- Create `webapp/frontend/src/components/api/RunTimeline.vue`.
- Create `webapp/frontend/src/components/api/StageChart.vue`.
- Create `webapp/frontend/src/components/api/GpuChart.vue`.
- Create `webapp/frontend/src/components/api/RunSnapshot.vue`.
- Create `webapp/frontend/src/components/api/ResultComposition.vue`.
- Create `webapp/frontend/src/components/api/ResultExplorer.vue`.
- Create `webapp/frontend/src/components/api/LiveLog.vue`.
- Create `webapp/frontend/src/domain/chartOptions.ts`: ECharts option builders.

### Bug replay files

- Create `webapp/frontend/src/composables/useBugReplay.ts`.
- Create `webapp/frontend/src/domain/bugEvidence.ts`: objective impact and verdict presentation.
- Create `webapp/frontend/src/domain/markdown.ts`: port of the current local report renderer.
- Create `webapp/frontend/src/views/BugReplayView.vue`.
- Create `webapp/frontend/src/components/bugs/BugNavigator.vue`.
- Create `webapp/frontend/src/components/bugs/VerdictSummary.vue`.
- Create `webapp/frontend/src/components/bugs/BehaviorComparison.vue`.
- Create `webapp/frontend/src/components/bugs/ReproCodeOutput.vue`.
- Create `webapp/frontend/src/components/bugs/ExecutionProfiles.vue`.
- Create `webapp/frontend/src/components/bugs/EvidenceReport.vue`.

### Tests and documentation

- Create `webapp/frontend/src/**/*.test.ts` beside the units they test.
- Create `test/test_frontend_build.py`: production artifact and no-hardcoded-environment contract.
- Modify `test/test_frontend_contract.py`: replace legacy DOM/CSS string assertions with Vue source/build contracts.
- Modify `docs/demo_script.md`: new frontend development/build commands; unchanged production server command.
- Replace `webapp/static/*` with generated Vite artifacts during Task 1 inside the isolated worktree; the user's current branch remains untouched until integration.
- Confirm legacy `webapp/static/app.js`, `charts.js`, `markdown.js`, and `styles.css` remain absent in the final migration task.

---

### Task 1: Scaffold Vue Without Changing Python Routes

**Files:**
- Create: `webapp/frontend/package.json`
- Create: `webapp/frontend/vite.config.ts`
- Create: `webapp/frontend/tsconfig.json`
- Create: `webapp/frontend/index.html`
- Create: `webapp/frontend/src/main.ts`
- Create: `webapp/frontend/src/App.vue`
- Create: `test/test_frontend_build.py`
- Modify: `.gitignore`

- [ ] **Step 1: Write the failing build-contract test**

```python
# test/test_frontend_build.py
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "webapp" / "frontend"


def test_vue_frontend_has_build_contract():
    package = (FRONTEND / "package.json").read_text(encoding="utf-8")
    vite = (FRONTEND / "vite.config.ts").read_text(encoding="utf-8")
    assert '"build": "vue-tsc --noEmit && vite build"' in package
    assert 'outDir: "../static"' in vite
    assert 'base: command === "build" ? "/static/" : "/"' in vite


def test_python_static_root_is_unchanged():
    server = (ROOT / "webapp" / "server.py").read_text(encoding="utf-8")
    assert 'STATIC_ROOT = Path(__file__).resolve().parent / "static"' in server
```

- [ ] **Step 2: Run the test and verify it fails because the Vue project does not exist**

Run: `python -m pytest test/test_frontend_build.py -q`

Expected: FAIL with `FileNotFoundError` for `webapp/frontend/package.json`.

- [ ] **Step 3: Create the package and Vite configuration**

```json
{
  "name": "tensorguard-frontend",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vue-tsc --noEmit && vite build",
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

```ts
// webapp/frontend/vite.config.ts
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig(({ command }) => ({
  plugins: [vue()],
  base: command === "build" ? "/static/" : "/",
  build: { outDir: "../static", emptyOutDir: true },
  server: { proxy: { "/api": "http://127.0.0.1:8008" } },
  test: { environment: "jsdom", globals: true },
}));
```

Create strict `tsconfig.json`, the Vite `index.html`, `main.ts`, and a minimal `App.vue` that renders `TensorGuard` and the three view names. Add `webapp/frontend/node_modules/`, `.vite/`, and `coverage/` to `.gitignore`.

Use these initial files:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "jsx": "preserve",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "esModuleInterop": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "types": ["vitest/globals"]
  },
  "include": ["src/**/*.ts", "src/**/*.vue", "vite.config.ts"]
}
```

```html
<!-- webapp/frontend/index.html -->
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>TensorGuard</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
```

```ts
// webapp/frontend/src/main.ts
import { createApp } from "vue";
import ArcoVue from "@arco-design/web-vue";
import "@arco-design/web-vue/dist/arco.css";
import App from "./App.vue";

createApp(App).use(ArcoVue).mount("#app");
```

```vue
<!-- webapp/frontend/src/App.vue -->
<template>
  <main>
    <h1>TensorGuard</h1>
    <p>系统总览 · 单 API 运行 · Bug 复现</p>
  </main>
</template>
```

- [ ] **Step 4: Install dependencies and generate the lock file**

Run:

```bash
cd webapp/frontend
npm install vue@3 @arco-design/web-vue echarts @lucide/vue
npm install --save-dev vite @vitejs/plugin-vue @vue/test-utils jsdom typescript vitest vue-tsc
```

Expected: `package-lock.json` is created and `npm audit` does not block installation.

- [ ] **Step 5: Run tests and the first production build**

Run: `python -m pytest test/test_frontend_build.py -q && cd webapp/frontend && npm run build`

Expected: Python test PASS; Vite writes `webapp/static/index.html` and `webapp/static/assets/*`.

- [ ] **Step 6: Commit the scaffold**

```bash
git add .gitignore test/test_frontend_build.py webapp/frontend webapp/static
git commit -m "build: scaffold Vue presentation frontend"
```

### Task 2: Define Backend Contracts and Typed Services

**Files:**
- Create: `webapp/frontend/src/types/tensorguard.ts`
- Create: `webapp/frontend/src/services/http.ts`
- Create: `webapp/frontend/src/services/tensorguard.ts`
- Test: `webapp/frontend/src/services/tensorguard.test.ts`

- [ ] **Step 1: Write failing service tests**

```ts
import { afterEach, describe, expect, it, vi } from "vitest";
import { getApis, startApiRun } from "./tensorguard";

afterEach(() => vi.unstubAllGlobals());

it("encodes API search parameters", async () => {
  const fetchMock = vi.fn().mockResolvedValue(new Response("[]", { status: 200 }));
  vi.stubGlobal("fetch", fetchMock);
  await getApis("torch", "Tensor.add", 5000);
  expect(fetchMock).toHaveBeenCalledWith(
    "/api/apis?lib=torch&q=Tensor.add&limit=5000",
    expect.any(Object),
  );
});

it("preserves the existing run-api body", async () => {
  const fetchMock = vi.fn().mockResolvedValue(
    new Response('{"job_id":"job-1"}', { status: 202 }),
  );
  vi.stubGlobal("fetch", fetchMock);
  await startApiRun({ lib: "torch", api: "torch.add", mode: "demo", cuda_device: "0" });
  const init = fetchMock.mock.calls[0][1] as RequestInit;
  expect(JSON.parse(String(init.body))).toEqual({
    lib: "torch", api: "torch.add", mode: "demo", cuda_device: "0",
  });
});
```

- [ ] **Step 2: Run the tests and verify missing service modules fail**

Run: `cd webapp/frontend && npm test -- src/services/tensorguard.test.ts`

Expected: FAIL because `./tensorguard` does not exist.

- [ ] **Step 3: Implement typed errors and all existing endpoints**

```ts
// webapp/frontend/src/services/http.ts
export class ApiError extends Error {
  constructor(
    public status: number,
    public payload: { error?: string },
  ) {
    super(payload.error || `HTTP ${status}`);
  }
}

export async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch(path, {
    ...init,
    headers: { "Content-Type": "application/json", ...(init.headers || {}) },
  });
  const payload = await response.json();
  if (!response.ok) throw new ApiError(response.status, payload);
  return payload as T;
}
```

Define types for overview, environment, API list/detail, API job metrics/results/logs, candidates, confirmed bugs, replay jobs, execution evidence, and reports. Implement wrappers for every currently used route:

```ts
export const endpoints = {
  overview: "/api/overview",
  environment: "/api/environment",
  apis: "/api/apis",
  apiDetail: "/api/api-detail",
  runApi: "/api/run-api",
  apiJob: (id: string) => `/api/api-jobs/${encodeURIComponent(id)}`,
  candidates: "/api/candidates",
  candidate: (id: string) => `/api/candidates/${encodeURIComponent(id)}`,
  candidateStatus: (id: string) => `/api/candidates/${encodeURIComponent(id)}/status`,
  confirmedBugs: "/api/confirmed-bugs",
  confirmedBug: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}`,
  reproduce: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}/reproduce`,
  reproJob: (id: string) => `/api/repro-jobs/${encodeURIComponent(id)}`,
  reproReport: (id: string) => `/api/repro-jobs/${encodeURIComponent(id)}/report`,
};
```

- [ ] **Step 4: Run service tests and type checking**

Run: `cd webapp/frontend && npm test -- src/services/tensorguard.test.ts && npx vue-tsc --noEmit`

Expected: PASS with no TypeScript errors.

- [ ] **Step 5: Commit the typed API layer**

```bash
git add webapp/frontend/src/types webapp/frontend/src/services
git commit -m "feat: add typed TensorGuard API client"
```

### Task 3: Build the Shared Product Shell

**Files:**
- Create: `webapp/frontend/src/styles/tokens.css`
- Create: `webapp/frontend/src/styles/global.css`
- Create: `webapp/frontend/src/composables/useHashNavigation.ts`
- Create: `webapp/frontend/src/composables/useEnvironment.ts`
- Create: `webapp/frontend/src/components/AppHeader.vue`
- Create: `webapp/frontend/src/components/EnvironmentDrawer.vue`
- Create: `webapp/frontend/src/components/AsyncState.vue`
- Modify: `webapp/frontend/src/App.vue`
- Modify: `webapp/frontend/src/main.ts`
- Test: `webapp/frontend/src/components/AppHeader.test.ts`

- [ ] **Step 1: Write failing shell tests**

```ts
import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import AppHeader from "./AppHeader.vue";

it("keeps all three primary navigation items visible", () => {
  const wrapper = mount(AppHeader, {
    props: { activeView: "overview", environmentLabel: "GPU unavailable" },
  });
  expect(wrapper.text()).toContain("系统总览");
  expect(wrapper.text()).toContain("单 API 运行");
  expect(wrapper.text()).toContain("Bug 复现");
  expect(wrapper.find('[aria-current="page"]').text()).toBe("系统总览");
});
```

- [ ] **Step 2: Run the test and verify the missing component fails**

Run: `cd webapp/frontend && npm test -- src/components/AppHeader.test.ts`

Expected: FAIL because `AppHeader.vue` does not exist.

- [ ] **Step 3: Implement tokens, hash navigation, environment state, and shell**

Use these stable view keys and hashes:

```ts
export type ViewKey = "overview" | "api-run" | "bug-replay";
export const viewHashes: Record<ViewKey, string> = {
  overview: "#overview",
  "api-run": "#api-run",
  "bug-replay": "#bug-replay",
};
```

Create the approved bright product shell: white sticky header, visible compact navigation at every breakpoint, live environment trigger, cobalt-blue active state, cold-gray page background, 8px maximum card radius, semantic green/amber/red states, and `prefers-reduced-motion` support. `EnvironmentDrawer` renders only values returned by `/api/environment`.

- [ ] **Step 4: Run component tests and build**

Run: `cd webapp/frontend && npm test -- src/components/AppHeader.test.ts && npm run build`

Expected: PASS; build contains no hardcoded GPU model or CUDA version.

- [ ] **Step 5: Commit the shell**

```bash
git add webapp/frontend/src
git commit -m "feat: add shared TensorGuard product shell"
```

### Task 4: Implement the Live Overview

**Files:**
- Create: `webapp/frontend/src/views/OverviewView.vue`
- Create: `webapp/frontend/src/components/overview/CoverageBaseline.vue`
- Create: `webapp/frontend/src/components/overview/DetectionPipeline.vue`
- Create: `webapp/frontend/src/components/overview/ConfirmedEvidenceList.vue`
- Modify: `webapp/frontend/src/App.vue`
- Test: `webapp/frontend/src/views/OverviewView.test.ts`

- [ ] **Step 1: Write a failing overview test with real payload shape**

```ts
import { mount } from "@vue/test-utils";
import { expect, it } from "vitest";
import OverviewView from "./OverviewView.vue";

it("renders API coverage and confirmed evidence from the overview payload", () => {
  const wrapper = mount(OverviewView, {
    props: {
      overview: {
        api_total: 4608,
        api_by_lib: { torch: 1568, tf: 3040 },
        prompt_ready_total: 0,
        prompt_ready_by_lib: { torch: 0, tf: 0 },
        paper_bug_total: 14,
        paper_bug_by_framework: { PyTorch: 5, TensorFlow: 9 },
        results: {}, latest_api_jobs: [], latest_repro_jobs: [], sources: {},
      },
      bugs: [{ id: "PAPER-PT-004", display_id: "PT-004", api: "torch.sparse.mm", bug_type: "Crash / allocator corruption", status: "confirmed" }],
    },
  });
  expect(wrapper.text()).toContain("4,608");
  expect(wrapper.text()).toContain("1,568");
  expect(wrapper.text()).toContain("3,040");
  expect(wrapper.text()).toContain("PT-004");
  expect(wrapper.text()).not.toContain("PAPER-PT-004");
});
```

- [ ] **Step 2: Run the test and verify it fails**

Run: `cd webapp/frontend && npm test -- src/views/OverviewView.test.ts`

Expected: FAIL because overview components do not exist.

- [ ] **Step 3: Implement the approved compact overview**

Render the page title `框架安全检测概览`, live API total and framework split, confirmed count, constraint status, framework count, environment summary, directional five-node pipeline, and confirmed evidence rows. Percentages use `count / api_total`; when total is zero, render `0%` without division errors. The evidence list shows technical impact and confirmation state, never High/Medium severity.

- [ ] **Step 4: Run tests and build**

Run: `cd webapp/frontend && npm test -- src/views/OverviewView.test.ts && npm run build`

Expected: PASS.

- [ ] **Step 5: Commit the overview**

```bash
git add webapp/frontend/src/views/OverviewView.vue webapp/frontend/src/components/overview
git commit -m "feat: add live coverage overview"
```

### Task 5: Preserve API Search and Job State Logic

**Files:**
- Create: `webapp/frontend/src/domain/apiRun.ts`
- Create: `webapp/frontend/src/composables/usePolling.ts`
- Create: `webapp/frontend/src/composables/useApiCatalog.ts`
- Create: `webapp/frontend/src/composables/useApiRun.ts`
- Create: `webapp/frontend/src/components/api/ApiSelector.vue`
- Create: `webapp/frontend/src/components/api/RunTimeline.vue`
- Create: `webapp/frontend/src/views/ApiRunView.vue`
- Modify: `webapp/frontend/src/App.vue`
- Test: `webapp/frontend/src/domain/apiRun.test.ts`
- Test: `webapp/frontend/src/components/api/ApiSelector.test.ts`

- [ ] **Step 1: Write failing stage and search tests**

```ts
import { expect, it } from "vitest";
import { liveStageKey, stageDefinitions } from "./apiRun";

it("preserves the original three metric stages", () => {
  expect(stageDefinitions.map((stage) => stage.key)).toEqual([
    "qwen_seed", "ev_generation", "driver",
  ]);
});

it("follows a running stage before completed stages", () => {
  expect(liveStageKey({ qwen_seed: "success", ev_generation: "running", driver: "pending" }))
    .toBe("ev_generation");
});
```

Mount `ApiSelector` with three results and assert that an empty query shows all three, a partial query filters the displayed list, and clicking an item emits the exact API object and adds the selected class.

- [ ] **Step 2: Run tests and verify missing domain/components fail**

Run: `cd webapp/frontend && npm test -- src/domain/apiRun.test.ts src/components/api/ApiSelector.test.ts`

Expected: FAIL because the files do not exist.

- [ ] **Step 3: Port the current stage definitions exactly**

```ts
export const stageDefinitions = [
  { key: "qwen_seed", label: "Qwen 种子", metricKeys: [["候选", "qwen_raw"], ["有效种子", "qwen_valid"]] },
  { key: "ev_generation", label: "InCoder 变异", metricKeys: [["有效", "valid"], ["异常", "exception"], ["崩溃", "crash"], ["超时", "hangs"]] },
  { key: "driver", label: "差异检测", metricKeys: [["已检查程序", "total_files"], ["差异 Catch", "trace_hits"], ["崩溃", "crash"], ["不稳定", "flaky"]] },
] as const;
```

Implement debounced `/api/apis` search with `limit=5000`, `/api/api-detail` loading on selection, automatic latest-job hydration, `POST /api/run-api`, polling cleanup on terminal states/unmount, live-stage following, and disabled pending/skipped stage tabs.

- [ ] **Step 4: Run tests and type checking**

Run: `cd webapp/frontend && npm test -- src/domain/apiRun.test.ts src/components/api/ApiSelector.test.ts && npx vue-tsc --noEmit`

Expected: PASS.

- [ ] **Step 5: Commit API selection and run state**

```bash
git add webapp/frontend/src/domain/apiRun.ts webapp/frontend/src/composables webapp/frontend/src/components/api/ApiSelector.vue webapp/frontend/src/components/api/RunTimeline.vue webapp/frontend/src/views/ApiRunView.vue
git commit -m "feat: port API search and run state"
```

### Task 6: Add Stage, Result, Log, and GPU Visualizations

**Files:**
- Create: `webapp/frontend/src/domain/chartOptions.ts`
- Create: `webapp/frontend/src/components/api/StageChart.vue`
- Create: `webapp/frontend/src/components/api/GpuChart.vue`
- Create: `webapp/frontend/src/components/api/RunSnapshot.vue`
- Create: `webapp/frontend/src/components/api/ResultComposition.vue`
- Create: `webapp/frontend/src/components/api/LiveLog.vue`
- Modify: `webapp/frontend/src/views/ApiRunView.vue`
- Test: `webapp/frontend/src/domain/chartOptions.test.ts`

- [ ] **Step 1: Write failing chart-option tests**

```ts
import { expect, it } from "vitest";
import { gpuSeries, stageSeries } from "./chartOptions";

it("keeps missing GPU samples as gaps instead of zero", () => {
  const series = gpuSeries([
    { elapsed_seconds: 0, stage: "ev_generation", gpu: null },
    { elapsed_seconds: 2, stage: "ev_generation", gpu: { utilization_percent: 50, memory_used_mib: 10, memory_total_mib: 20 } },
  ]);
  expect(series[0].data).toEqual([[0, null], [2, 50]]);
});

it("filters metric samples to the selected stage", () => {
  const series = stageSeries([
    { elapsed_seconds: 1, stage: "qwen_seed", qwen_raw: 30 },
    { elapsed_seconds: 2, stage: "driver", total_files: 4 },
  ], "qwen_seed");
  expect(series[0].data).toEqual([[1, 30]]);
});
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `cd webapp/frontend && npm test -- src/domain/chartOptions.test.ts`

Expected: FAIL because `chartOptions.ts` does not exist.

- [ ] **Step 3: Implement ECharts option builders and approved layout**

Use tree-shaken ECharts imports (`LineChart`, `GridComponent`, `TooltipComponent`, `LegendComponent`, `CanvasRenderer`). Build one shared stage chart with three tabs, independent GPU utilization/memory chart, live stage statistics, Results composition, and stage-specific log. The live log and GPU panel must use the same grid tracks as the main chart and right summary column.

- [ ] **Step 4: Run tests and build**

Run: `cd webapp/frontend && npm test -- src/domain/chartOptions.test.ts && npm run build`

Expected: PASS; no empty chart is rendered as a fabricated flat zero line.

- [ ] **Step 5: Commit visualizations**

```bash
git add webapp/frontend/src/domain/chartOptions.ts webapp/frontend/src/components/api webapp/frontend/src/views/ApiRunView.vue
git commit -m "feat: add live experiment visualizations"
```

### Task 7: Restore Results Review and Candidate Actions

**Files:**
- Create: `webapp/frontend/src/components/api/ResultExplorer.vue`
- Modify: `webapp/frontend/src/composables/useApiRun.ts`
- Modify: `webapp/frontend/src/views/ApiRunView.vue`
- Test: `webapp/frontend/src/components/api/ResultExplorer.test.ts`

- [ ] **Step 1: Write failing Results tests**

Mount `ResultExplorer` with all seven categories. Assert that category counts render in this order:

```ts
expect(wrapper.findAll("[data-result-category]").map((node) => node.attributes("data-result-category")))
  .toEqual(["seed", "valid", "exception", "crash", "notarget", "hangs", "flaky"]);
```

Select a recommended crash file and assert that `add-candidate` emits:

```ts
{
  job_id: "job-1",
  lib: "torch",
  api: "torch.add",
  category: "crash",
  source_path: "demo_runs/api_jobs/job-1/Results/torch/crash/torch.add_1.py",
}
```

- [ ] **Step 2: Run the test and verify it fails**

Run: `cd webapp/frontend && npm test -- src/components/api/ResultExplorer.test.ts`

Expected: FAIL because `ResultExplorer.vue` does not exist.

- [ ] **Step 3: Implement exact-source review and candidate status updates**

Render filenames, sizes, recommendation markers, exact `source_excerpt`, add-candidate action, and existing candidate status transitions: `pending_review`, `reproduced`, `needs_review`, `rejected`. Keep the source path from the backend unchanged; never reconstruct it from visible text.

- [ ] **Step 4: Run the test and full frontend suite**

Run: `cd webapp/frontend && npm test`

Expected: PASS.

- [ ] **Step 5: Commit Results review**

```bash
git add webapp/frontend/src/components/api/ResultExplorer.vue webapp/frontend/src/composables/useApiRun.ts webapp/frontend/src/views/ApiRunView.vue
git commit -m "feat: restore result review and candidate actions"
```

### Task 8: Implement Objective Bug Evidence Navigation

**Files:**
- Create: `webapp/frontend/src/domain/bugEvidence.ts`
- Create: `webapp/frontend/src/composables/useBugReplay.ts`
- Create: `webapp/frontend/src/components/bugs/BugNavigator.vue`
- Create: `webapp/frontend/src/components/bugs/VerdictSummary.vue`
- Create: `webapp/frontend/src/components/bugs/BehaviorComparison.vue`
- Create: `webapp/frontend/src/views/BugReplayView.vue`
- Modify: `webapp/frontend/src/App.vue`
- Test: `webapp/frontend/src/domain/bugEvidence.test.ts`
- Test: `webapp/frontend/src/views/BugReplayView.test.ts`

- [ ] **Step 1: Write failing evidence-presentation tests**

```ts
import { expect, it } from "vitest";
import { displayBugId, technicalImpact } from "./bugEvidence";

it("removes the internal paper prefix", () => {
  expect(displayBugId("PAPER-PT-004")).toBe("PT-004");
});

it("derives only objective technical impact labels", () => {
  expect(technicalImpact("Crash / allocator corruption")).toEqual([
    "进程异常终止", "内存分配器破坏",
  ]);
});
```

Mount `BugReplayView` with a confirmed record containing `severity: "High"`; assert the rendered text contains the bug type and does not contain `High`, `高危`, or `PAPER-`.

- [ ] **Step 2: Run tests and verify they fail**

Run: `cd webapp/frontend && npm test -- src/domain/bugEvidence.test.ts src/views/BugReplayView.test.ts`

Expected: FAIL because evidence files do not exist.

- [ ] **Step 3: Implement confirmed/candidate search and conclusion-first detail**

Load `/api/confirmed-bugs` and `/api/candidates`, preserve source tabs and search, fetch selected details, and render display ID, API, objective technical impact, confirmed/minimized/reproducible evidence states, expected behavior, and observed behavior. Do not display or calculate security severity or CVSS.

- [ ] **Step 4: Run tests and type checking**

Run: `cd webapp/frontend && npm test -- src/domain/bugEvidence.test.ts src/views/BugReplayView.test.ts && npx vue-tsc --noEmit`

Expected: PASS.

- [ ] **Step 5: Commit bug navigation and evidence hierarchy**

```bash
git add webapp/frontend/src/domain/bugEvidence.ts webapp/frontend/src/composables/useBugReplay.ts webapp/frontend/src/components/bugs webapp/frontend/src/views/BugReplayView.vue
git commit -m "feat: add objective bug evidence workspace"
```

### Task 9: Restore Replay Execution and Immutable Reports

**Files:**
- Create: `webapp/frontend/src/domain/markdown.ts`
- Create: `webapp/frontend/src/components/bugs/ReproCodeOutput.vue`
- Create: `webapp/frontend/src/components/bugs/ExecutionProfiles.vue`
- Create: `webapp/frontend/src/components/bugs/EvidenceReport.vue`
- Modify: `webapp/frontend/src/composables/useBugReplay.ts`
- Modify: `webapp/frontend/src/views/BugReplayView.vue`
- Test: `webapp/frontend/src/domain/markdown.test.ts`
- Test: `webapp/frontend/src/components/bugs/EvidenceReport.test.ts`

- [ ] **Step 1: Port the existing Markdown test case before the renderer**

Create the exact escaping regression and report-state tests:

```ts
// webapp/frontend/src/domain/markdown.test.ts
import { expect, it } from "vitest";
import { renderSafeMarkdown } from "./markdown";

it("renders headings and lists while escaping raw HTML", () => {
  const html = renderSafeMarkdown("# Report\n\n- one\n\n## Next\n<script>alert(1)</script>");
  expect(html).toContain("</ul><h2>Next</h2>");
  expect(html).not.toContain("<script>");
  expect(html).toContain("&lt;script&gt;");
});
```

```ts
// webapp/frontend/src/components/bugs/EvidenceReport.test.ts
import { mount } from "@vue/test-utils";
import { expect, it } from "vitest";
import EvidenceReport from "./EvidenceReport.vue";

it("uses an existing report without offering overwrite", () => {
  const wrapper = mount(EvidenceReport, {
    props: { reportExists: true, markdown: "# Existing report", canGenerate: true },
  });
  expect(wrapper.text()).toContain("Existing report");
  expect(wrapper.get('[data-action="generate-report"]').attributes("disabled")).toBeDefined();
});
```

- [ ] **Step 2: Run tests and verify missing renderer/components fail**

Run: `cd webapp/frontend && npm test -- src/domain/markdown.test.ts src/components/bugs/EvidenceReport.test.ts`

Expected: FAIL.

- [ ] **Step 3: Implement replay polling, code/output, profiles, and report actions**

Port the existing local Markdown renderer to TypeScript with the same escaping behavior. Start replay through `POST /api/confirmed-bugs/{id}/reproduce`, poll `/api/repro-jobs/{job_id}`, display independent CPU/GPU modes, return code, timeout, signal, actual device, rule reason, and backend `evidence.verdict`. Generate reports only when `report_exists` is false; otherwise render the archived Markdown. Keep Markdown download and print/PDF actions.

- [ ] **Step 4: Run replay/report tests and backend evidence tests**

Run: `cd webapp/frontend && npm test -- src/domain/markdown.test.ts src/components/bugs/EvidenceReport.test.ts && cd ../.. && python -m pytest test/test_repro_evidence.py test/test_confirmed_bugs.py -q`

Expected: all tests PASS.

- [ ] **Step 5: Commit replay and report UI**

```bash
git add webapp/frontend/src/domain/markdown.ts webapp/frontend/src/components/bugs webapp/frontend/src/composables/useBugReplay.ts webapp/frontend/src/views/BugReplayView.vue
git commit -m "feat: restore deterministic bug replay reports"
```

### Task 10: Switch Production Assets and Complete Regression QA

**Files:**
- Modify: `test/test_frontend_contract.py`
- Modify: `docs/demo_script.md`
- Replace: `webapp/static/index.html`
- Create: `webapp/static/assets/*`
- Confirm absent: `webapp/static/app.js`
- Confirm absent: `webapp/static/charts.js`
- Confirm absent: `webapp/static/markdown.js`
- Confirm absent: `webapp/static/styles.css`
- Delete: `test/test_charts.js`
- Delete: `test/test_markdown.js`

- [ ] **Step 1: Replace legacy string tests with Vue/build contracts**

Update `test_frontend_contract.py` to assert:

```python
def test_production_frontend_is_vite_build():
    html = INDEX.read_text(encoding="utf-8")
    assert 'id="app"' in html
    assert '/static/assets/' in html
    assert '/static/app.js' not in html


def test_frontend_source_has_three_views_and_no_hardcoded_environment():
    source = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (ROOT / "webapp" / "frontend" / "src").rglob("*")
        if path.suffix in {".ts", ".vue", ".css"}
    )
    for view in ("OverviewView", "ApiRunView", "BugReplayView"):
        assert view in source
    for forbidden in ("NVIDIA A800", "NVIDIA L40", "CUDA 13.0", "GPU0"):
        assert forbidden not in source
```

- [ ] **Step 2: Run the updated contract test against the current Vue build**

Run: `python -m pytest test/test_frontend_contract.py -q`

Expected: PASS because Task 1 already switched the isolated worktree to Vite assets and Tasks 3-9 now provide all three views.

- [ ] **Step 3: Build final assets and remove legacy modules**

Delete `test/test_charts.js` and `test/test_markdown.js`, whose assertions now live in Vitest. Then run: `cd webapp/frontend && npm run build`

Expected: `emptyOutDir` removes legacy files and writes hashed assets. Confirm with:

```bash
test ! -e webapp/static/app.js
test ! -e webapp/static/charts.js
test ! -e webapp/static/markdown.js
test ! -e webapp/static/styles.css
```

- [ ] **Step 4: Run all automated tests**

Run:

```bash
cd webapp/frontend && npm test && npm run build
cd ../.. && python -m pytest test -q
```

Expected: all frontend and Python tests PASS.

- [ ] **Step 5: Verify the real Python server and browser behavior**

Run: `python webapp/server.py --host 127.0.0.1 --port 8008`

Verify in the browser at `http://127.0.0.1:8008`:

1. Overview uses live counts and environment values.
2. Empty API search opens the complete framework list; partial search filters and selected API highlights.
3. Selecting another API immediately loads its latest status/results.
4. Pending stage tabs are disabled; completed tabs work; live-follow returns to the running stage.
5. Results source and candidate actions work.
6. Confirmed/candidate search works and no `PAPER-` or unsupported severity appears.
7. Replay output uses backend verdicts; existing report is not overwritten.
8. Screenshots at 1366×768, 1440×900, and approximately 760px show visible navigation, stable charts, no overlap, and aligned lower panels.

- [ ] **Step 6: Update demonstration documentation**

Add these commands to `docs/demo_script.md`:

```bash
# Frontend development
cd webapp/frontend
npm install
npm run dev

# Production build
npm run build
cd ../..
python webapp/server.py --host 0.0.0.0 --port 42173
```

State that a repository clone can run the committed production assets without Node; Node is needed only for frontend development or rebuilding.

- [ ] **Step 7: Commit the production migration**

```bash
git add test/test_frontend_contract.py docs/demo_script.md webapp/frontend webapp/static
git commit -m "feat: ship Vue TensorGuard presentation workbench"
```

### Task 11: Final Review and Cleanup

**Files:**
- Review: all files changed by Tasks 1-10

- [ ] **Step 1: Run formatting and static checks**

Run: `cd webapp/frontend && npx vue-tsc --noEmit && npm test && npm run build`

Expected: PASS with no type errors.

- [ ] **Step 2: Run backend regression tests again from a clean process**

Run: `python -m pytest test -q`

Expected: PASS.

- [ ] **Step 3: Inspect repository hygiene**

Run:

```bash
git status --short
git diff --check
find webapp/static -maxdepth 2 -type f | sort
```

Expected: only intentional implementation changes before commit; no `node_modules`, model files, run outputs, preview sessions, or legacy static modules.

- [ ] **Step 4: Request code review**

Use `superpowers:requesting-code-review` against the design document and this implementation plan. Resolve all correctness findings before integration.

- [ ] **Step 5: Present integration options**

Use `superpowers:finishing-a-development-branch` after tests and review pass; offer merge, pull request, keep branch, or discard worktree options without altering the user's main branch automatically.
