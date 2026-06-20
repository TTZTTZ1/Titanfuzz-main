# TensorGuard Competition UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将现有 TensorGuard 演示页改造为数据可追溯、单 API 过程可视化、候选可审查、Bug 可复现并生成不可覆盖报告的作品赛工作台。

**Architecture:** 保留 Python `ThreadingHTTPServer` 和原生 HTML/CSS/JS。后端增加环境采集、Job 指标、候选索引和确定性报告模块；前端通过 JSON API 轮询真实数据，用 SVG 绘制小型实时图表，不引入需要网络的 CDN 依赖。

**Tech Stack:** Python 3.10+ standard library, HTML5, CSS, vanilla JavaScript, SVG, JSON/JSONL, `nvidia-smi` subprocess.

---

### Task 1: Preserve and verify the current single-API baseline

**Files:**
- Modify: `test/test_demo_pipeline_behavior.py`
- Existing baseline: `scripts/run_one_api_demo.py`
- Existing baseline: `webapp/server.py`
- Existing baseline: `webapp/static/app.js`
- Existing baseline: `webapp/static/index.html`

- [ ] **Step 1: Extend the baseline test to assert actual model metadata and canonical publication**

```python
def test_status_records_actual_mutation_model():
    with tempfile.TemporaryDirectory() as tmp:
        run = demo.DemoRun(make_args(), Path(tmp))
        assert run.status["mutation_model"] == make_args().mut_model
```

- [ ] **Step 2: Run the baseline tests**

Run: `python3 test/test_demo_pipeline_behavior.py`

Expected: `ok`.

- [ ] **Step 3: Verify Python and JavaScript syntax**

Run: `python3 -m py_compile webapp/server.py scripts/run_one_api_demo.py`

Expected: exit code 0.

Run: `node --check webapp/static/app.js`

Expected: exit code 0.

- [ ] **Step 4: Commit the already verified baseline changes**

```bash
git add scripts/run_one_api_demo.py webapp/server.py webapp/static/app.js webapp/static/index.html test/test_demo_pipeline_behavior.py
git commit -m "feat: align single API results and model metadata"
```

### Task 2: Add truthful runtime environment inventory

**Files:**
- Create: `webapp/runtime_data.py`
- Create: `test/test_runtime_data.py`
- Modify: `webapp/server.py`

- [ ] **Step 1: Write failing environment parser tests**

```python
def test_parse_nvidia_smi_inventory():
    text = "0, NVIDIA A800, 550.54.15, 81920\n1, NVIDIA L40, 550.54.15, 46068\n"
    assert parse_gpu_inventory(text) == [
        {"index": 0, "name": "NVIDIA A800", "driver_version": "550.54.15", "memory_total_mib": 81920},
        {"index": 1, "name": "NVIDIA L40", "driver_version": "550.54.15", "memory_total_mib": 46068},
    ]


def test_inventory_failure_returns_warning_not_fake_gpu():
    data = collect_environment(run=lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError()))
    assert data["cuda"]["available"] is False
    assert data["gpus"] == []
    assert data["warnings"]
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python3 test/test_runtime_data.py`

Expected: import failure because `webapp.runtime_data` does not exist.

- [ ] **Step 3: Implement the environment collector**

`webapp/runtime_data.py` must expose:

```python
def parse_gpu_inventory(text: str) -> list[dict]: ...
def parse_gpu_sample(text: str) -> list[dict]: ...
def collect_environment(run=subprocess.run) -> dict: ...
def collect_gpu_sample(run=subprocess.run) -> dict: ...
```

Use `importlib.metadata.version()` for package versions and a 3-second `nvidia-smi` subprocess for GPU data. Return `collected_at`, `platform`, `python`, `frameworks`, `cuda`, `gpus`, and `warnings`; never return example GPU names.

- [ ] **Step 4: Add `/api/environment`**

Add a 30-second mtime/time cache in `webapp/server.py` and route:

```python
if path == "/api/environment":
    send_json(self, environment_payload())
    return
```

- [ ] **Step 5: Run environment tests and syntax checks**

Run: `python3 test/test_runtime_data.py`

Expected: all tests print `ok`.

Run: `python3 -m py_compile webapp/runtime_data.py webapp/server.py`

Expected: exit code 0.

- [ ] **Step 6: Commit**

```bash
git add webapp/runtime_data.py webapp/server.py test/test_runtime_data.py
git commit -m "feat: expose live runtime environment inventory"
```

### Task 3: Emit structured job metrics and GPU samples

**Files:**
- Create: `scripts/demo_metrics.py`
- Create: `test/test_demo_metrics.py`
- Modify: `scripts/run_one_api_demo.py`
- Modify: `webapp/server.py`

- [ ] **Step 1: Write failing JSONL and filesystem snapshot tests**

```python
def test_snapshot_counts_job_results():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "valid").mkdir()
        (root / "valid" / "torch.add_1.py").write_text("pass")
        sample = snapshot_results(root)
        assert sample["valid"] == 1
        assert sample["crash"] == 0


def test_append_metric_writes_one_json_object_per_line():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "metrics.jsonl"
        append_metric(path, {"stage": "ev_generation", "valid": 1})
        assert json.loads(path.read_text().strip())["valid"] == 1
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python3 test/test_demo_metrics.py`

Expected: import failure because `scripts.demo_metrics` does not exist.

- [ ] **Step 3: Implement metrics primitives**

`scripts/demo_metrics.py` exposes `append_metric`, `read_metrics`, `snapshot_qwen`, `snapshot_results`, and `MetricSampler`. `MetricSampler` writes once per second while a child process runs and records stage, elapsed time, directory counts, and optional GPU samples.

- [ ] **Step 4: Replace blocking `subprocess.run` with monitored `Popen`**

In `DemoRun.run_command`, start `subprocess.Popen`, poll every second, append a metric snapshot, then return the child return code. Store `metrics_path` in `status.json`. Dry runs write no simulated metrics.

- [ ] **Step 5: Expose job metrics through the existing job endpoint**

`api_job_payload()` returns:

```python
payload["metrics"] = read_metrics(out / "metrics.jsonl", limit=2000)
payload["environment"] = read_json(out / "environment.json", {})
```

- [ ] **Step 6: Run metrics and existing pipeline tests**

Run: `python3 test/test_demo_metrics.py`

Expected: `ok`.

Run: `python3 test/test_demo_pipeline_behavior.py`

Expected: `ok`.

- [ ] **Step 7: Commit**

```bash
git add scripts/demo_metrics.py scripts/run_one_api_demo.py webapp/server.py test/test_demo_metrics.py test/test_demo_pipeline_behavior.py
git commit -m "feat: stream structured single API metrics"
```

### Task 4: Add candidate recommendation and persistent candidate index

**Files:**
- Create: `webapp/candidates.py`
- Create: `test/test_candidates.py`
- Modify: `webapp/server.py`

- [ ] **Step 1: Write failing candidate tests**

```python
def test_candidate_references_exact_job_source_and_deduplicates_hash():
    store = CandidateStore(root)
    first = store.add(job_id="job1", lib="torch", api="torch.add", category="crash", source=source)
    second = store.add(job_id="job1", lib="torch", api="torch.add", category="crash", source=source)
    assert first["id"] == second["id"]
    assert first["source_path"].endswith("torch.add_1.py")


def test_recommendation_excludes_notarget_and_plain_exception():
    assert recommend_category("crash", "") is True
    assert recommend_category("exception", "ValueError: invalid argument") is False
    assert recommend_category("notarget", "") is False
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python3 test/test_candidates.py`

Expected: import failure because `webapp.candidates` does not exist.

- [ ] **Step 3: Implement candidate storage**

Store records in `demo_runs/candidates/index.json`. Each record contains ID, Job ID, API, framework, category, immutable Job Results source path, SHA-256, status, created time, original error summary, and notes. Allowed states are `pending_review`, `reproduced`, `needs_review`, `rejected`, and `promoted`.

- [ ] **Step 4: Add candidate APIs**

Implement:

```text
GET  /api/candidates
POST /api/candidates
POST /api/candidates/<id>/status
```

Reject paths outside `demo_runs/api_jobs`, missing `.py` files, and API/category mismatches.

- [ ] **Step 5: Run tests and commit**

Run: `python3 test/test_candidates.py`

Expected: `ok`.

```bash
git add webapp/candidates.py webapp/server.py test/test_candidates.py
git commit -m "feat: add candidate review index"
```

### Task 5: Make reproduction verdicts and reports deterministic and immutable

**Files:**
- Create: `webapp/repro_evidence.py`
- Create: `test/test_repro_evidence.py`
- Modify: `webapp/server.py`

- [ ] **Step 1: Write failing classification tests**

```python
def test_negative_sigfpe_returncode_is_reproduced_without_log_text():
    result = classify_execution(returncode=-8, timed_out=False, log_text="")
    assert result["verdict"] == "reproduced"
    assert result["signal"] == "SIGFPE"


def test_unknown_nonzero_exit_needs_review():
    result = classify_execution(returncode=23, timed_out=False, log_text="unclassified")
    assert result["verdict"] == "needs_review"


def test_existing_report_is_returned_without_overwrite():
    path.write_text("original")
    assert write_report_once(path, "replacement") == "original"
    assert path.read_text() == "original"
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python3 test/test_repro_evidence.py`

Expected: import failure because `webapp.repro_evidence` does not exist.

- [ ] **Step 3: Implement structured evidence classification**

Support normal exit, timeout, negative POSIX signals, allocator corruption, internal/fatal assertions, CUDA device-side assertions, OOM, ordinary exceptions, backend mismatch, and unknown exits. Templates describe observations only and never infer root cause, exploitability, CVSS, or severity.

- [ ] **Step 4: Capture an environment snapshot when the reproduction starts**

Write `environment.json` in the Repro Job directory before spawning child processes. Record execution profile (`cuda_hidden` or selected visible GPU) separately from `actual_device`; use `unknown` unless the testcase explicitly reports its device.

- [ ] **Step 5: Replace report generation**

Generate one immutable `report.md` with report ID, conclusion, expected/observed behavior, execution table, source/output excerpt, environment snapshot, limitations, SHA-256 hashes, and attachment paths. Do not show Job ID or meta severity in report body.

- [ ] **Step 6: Run tests and commit**

Run: `python3 test/test_repro_evidence.py`

Expected: `ok`.

```bash
git add webapp/repro_evidence.py webapp/server.py test/test_repro_evidence.py
git commit -m "feat: generate immutable evidence-based repro reports"
```

### Task 6: Rebuild the global shell and static overview

**Files:**
- Modify: `webapp/static/index.html`
- Modify: `webapp/static/styles.css`
- Modify: `webapp/static/app.js`
- Create: `test/test_frontend_contract.py`

- [ ] **Step 1: Write failing frontend contract tests**

```python
def test_frontend_has_no_hardcoded_gpu_or_environment_examples():
    source = APP_JS.read_text() + INDEX.read_text()
    for forbidden in ("NVIDIA A800", "NVIDIA L40", "PyTorch 2.11.0", "CUDA 13.0", "GPU0"):
        assert forbidden not in source


def test_frontend_has_three_primary_views():
    html = INDEX.read_text()
    assert 'id="overview"' in html
    assert 'id="apiRun"' in html
    assert 'id="bugReplay"' in html
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python3 test/test_frontend_contract.py`

Expected: failure on the current hardcoded `GPU0` controls.

- [ ] **Step 3: Implement the Graphite + Signal shell**

Use a graphite sidebar, cool-white workspace, teal/amber/red semantic colors, 6px radii, restrained borders, and no gradients. Replace the marketing-like hero and source-path disclosure with the static overview: live API counts, confirmed Bug count, framework distribution, failure-type distribution, process strip, and evidence table.

- [ ] **Step 4: Bind the live environment drawer**

Fetch `/api/environment`, render actual package/GPU data, populate GPU selectors, and show collection warnings. Before a Job exists, the mutation stage label is generic `InCoder 变异`; after loading a Job, use its actual model value.

- [ ] **Step 5: Run contract and syntax tests**

Run: `python3 test/test_frontend_contract.py`

Expected: `ok`.

Run: `node --check webapp/static/app.js`

Expected: exit code 0.

- [ ] **Step 6: Commit**

```bash
git add webapp/static/index.html webapp/static/styles.css webapp/static/app.js test/test_frontend_contract.py
git commit -m "feat: redesign TensorGuard overview and runtime shell"
```

### Task 7: Implement stage-aware charts, Results explorer, and candidate actions

**Files:**
- Create: `webapp/static/charts.js`
- Modify: `webapp/static/index.html`
- Modify: `webapp/static/styles.css`
- Modify: `webapp/static/app.js`
- Modify: `test/test_frontend_contract.py`

- [ ] **Step 1: Add failing DOM contract assertions**

```python
def test_single_api_workspace_contains_stage_tabs_and_live_surfaces():
    html = INDEX.read_text()
    for expected in ("apiStageTabs", "apiStageChart", "apiResultComposition", "gpuMonitor", "candidateResults"):
        assert f'id="{expected}"' in html
```

- [ ] **Step 2: Run and verify RED**

Run: `python3 test/test_frontend_contract.py`

Expected: missing stage/chart element assertions.

- [ ] **Step 3: Implement dependency-free SVG charts**

`charts.js` exposes `renderLineChart`, `renderStackedBar`, and `renderProgress`. Empty series render a truthful no-data state. Line charts use SVG `viewBox`, stable colors, legends, and accessible labels.

- [ ] **Step 4: Implement stage state interaction**

Pending/skipped tabs are disabled; running is selected automatically; success/failed tabs remain inspectable. Historical inspection does not force navigation back to the running stage; a `返回实时阶段` action restores follow mode.

- [ ] **Step 5: Implement Results and candidate review surfaces**

Show all seven category counts with their correct semantics. List exact `.py` files for a selected category, mark system recommendations, show source/error excerpts, and POST the selected Job file to `/api/candidates` only after the user clicks `加入候选`.

- [ ] **Step 6: Implement the collapsible GPU monitor**

Render utilization and memory series from Job metrics. Missing samples create gaps, not zero values.

- [ ] **Step 7: Run tests and commit**

Run: `python3 test/test_frontend_contract.py`

Expected: `ok`.

Run: `node --check webapp/static/app.js`

Expected: exit code 0.

Run: `node --check webapp/static/charts.js`

Expected: exit code 0.

```bash
git add webapp/static/charts.js webapp/static/index.html webapp/static/styles.css webapp/static/app.js test/test_frontend_contract.py
git commit -m "feat: add live stage charts and candidate review"
```

### Task 8: Rebuild Bug reproduction and report presentation

**Files:**
- Modify: `webapp/static/index.html`
- Modify: `webapp/static/styles.css`
- Modify: `webapp/static/app.js`
- Modify: `test/test_frontend_contract.py`

- [ ] **Step 1: Add failing evidence UI assertions**

```python
def test_repro_workspace_has_explanation_evidence_and_report_regions():
    html = INDEX.read_text()
    for expected in ("bugExplanation", "reproEvidence", "reproEnvironment", "reportPreview"):
        assert f'id="{expected}"' in html
    assert "严重程度" not in html
```

- [ ] **Step 2: Run and verify RED**

Run: `python3 test/test_frontend_contract.py`

Expected: missing evidence region assertions.

- [ ] **Step 3: Implement master-detail reproduction workspace**

Add confirmed/candidate tabs, search/filter list, expected-vs-observed explanation, source/output split, structured signal/return-code table, actual-device field, environment snapshot, and independent execution-profile controls generated from `/api/environment`.

- [ ] **Step 4: Implement immutable report interaction**

After the first report generation, replace the action with `查看报告`. Render Markdown as safe HTML using a small allowlisted renderer, retain a raw Markdown download, and provide `window.print()` with report-only print CSS.

- [ ] **Step 5: Run frontend tests and syntax checks**

Run: `python3 test/test_frontend_contract.py`

Expected: `ok`.

Run: `node --check webapp/static/app.js`

Expected: exit code 0.

Run: `node --check webapp/static/charts.js`

Expected: exit code 0.

- [ ] **Step 6: Commit**

```bash
git add webapp/static/index.html webapp/static/styles.css webapp/static/app.js test/test_frontend_contract.py
git commit -m "feat: present reproducible bug evidence and reports"
```

### Task 9: Integration and visual verification

**Files:**
- Modify: `test/test_demo_pipeline_behavior.py`
- Modify: `test/test_frontend_contract.py`
- Modify: `docs/demo_script.md`

- [ ] **Step 1: Run the complete local test set**

Run:

```bash
python3 test/test_demo_pipeline_behavior.py
python3 test/test_runtime_data.py
python3 test/test_demo_metrics.py
python3 test/test_candidates.py
python3 test/test_repro_evidence.py
python3 test/test_frontend_contract.py
python3 -m py_compile webapp/server.py webapp/runtime_data.py webapp/candidates.py webapp/repro_evidence.py scripts/run_one_api_demo.py scripts/demo_metrics.py
node --check webapp/static/app.js
node --check webapp/static/charts.js
```

Expected: every script prints `ok`; syntax checks exit 0.

- [ ] **Step 2: Start the local server**

Run: `python3 webapp/server.py --host 127.0.0.1 --port 8011`

Expected: server reports `http://127.0.0.1:8011`.

- [ ] **Step 3: Verify through the in-app browser**

Check desktop and mobile widths for overview, API search/selection, disabled future-stage tabs, live/no-data chart states, environment drawer, Bug list/detail, reproduction verdict, report preview, and print CSS. Confirm no overlap, clipping, stale selected API state, fake GPU values, or console errors.

- [ ] **Step 4: Verify data provenance manually**

Compare `/api/environment` with `python --version`, package metadata, and `nvidia-smi`. Compare overview API counts with `wc -l data/torch_apis.txt data/tf_apis.txt`. Compare chart terminal points with Job Results directory counts.

- [ ] **Step 5: Update the demo script**

Document the judge flow: overview facts → run one API → inspect live stages → review Results/candidate → reproduce confirmed Bug → open immutable report.

- [ ] **Step 6: Commit**

```bash
git add test/test_demo_pipeline_behavior.py test/test_frontend_contract.py docs/demo_script.md
git commit -m "test: verify TensorGuard competition workflow"
```
