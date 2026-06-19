# TitanFuzz-main Demo Workbench Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete competition-ready demo system around the existing `TitanFuzz-main` code: fixed prompt library, one-command single-API pipeline, web workbench, bug evidence repository, and report export.

**Architecture:** Keep the current fuzzing code unchanged where possible. Add thin wrappers around `qwen_seed.py`, `ev_generation.py`, and `driver.py`; add a local web backend that only invokes whitelisted demo commands; add a static frontend that visualizes prompt constraints, pipeline progress, and bug evidence.

**Tech Stack:** Python 3 standard library backend (`http.server`, `subprocess`, `json`, `threading`), static HTML/CSS/JavaScript frontend, existing TitanFuzz-main scripts, local Qwen model, InCoder-6B via HuggingFace/Transformers.

---

## 0. Important Scope Decisions

This plan assumes:

- `TitanFuzz-main` is the authoritative codebase.
- DeepSeek is offline only. It is used before runtime to produce files under `experiment/<lib>/<api>/prompts/`.
- Runtime never calls DeepSeek.
- The prompt library is treated as a fixed local knowledge base.
- The demo pipeline runs one API at a time.
- The frontend is a workbench, not a marketing page.
- The frontend must not execute arbitrary shell commands from user input.

Recommended first demo API:

```text
torch.nn.functional.conv1d
```

Reason: the local prompt files for this API are present and relatively complete.

## 1. Target File Structure

Create or modify these files:

```text
TitanFuzz-main/
  experiment/
    torch/
      <api>/prompts/
        greedy_prompt.txt
        structured_info.txt
        prompt_0.txt
        prompt_1.txt
        prompt_2.txt
    tf/
      <api>/prompts/
        greedy_prompt.txt
        structured_info.txt

  prompt_library_manifest.json

  scripts/
    build_prompt_manifest.py
    validate_prompt_library.py
    run_one_api_demo.py
    run_one_api_demo.sh

  webapp/
    server.py
    static/
      index.html
      styles.css
      app.js

  reports/
    bug_candidates.json
    bug_candidates/
      fractional_max_pool3d.md
      index_exception_mismatch.md

  demo_runs/
    <generated at runtime>
```

Responsibility split:

- `experiment/`: fixed prompt/constraint library.
- `prompt_library_manifest.json`: indexed prompt library metadata for backend and frontend.
- `scripts/build_prompt_manifest.py`: scans `experiment/` and writes manifest.
- `scripts/validate_prompt_library.py`: checks prompt files before demo.
- `scripts/run_one_api_demo.py`: executes Qwen seed generation, InCoder mutation, and driver oracle for one API.
- `scripts/run_one_api_demo.sh`: small shell entrypoint for humans.
- `webapp/server.py`: local backend and static file server.
- `webapp/static/*`: frontend workbench.
- `reports/bug_candidates.json`: curated bug evidence index.
- `reports/bug_candidates/*.md`: detailed evidence pages.

## 2. Prompt Library: How to "Write It Dead"

### Principle

The prompt library is not generated at demo time. It is committed as local files:

```text
experiment/<lib>/<api>/prompts/greedy_prompt.txt
experiment/<lib>/<api>/prompts/structured_info.txt
```

For example:

```text
experiment/torch/torch.nn.functional.conv1d/prompts/greedy_prompt.txt
experiment/torch/torch.nn.functional.conv1d/prompts/structured_info.txt
```

DeepSeek's role is already completed when these files exist.

Runtime behavior:

```text
API selected
→ look up prompt library
→ if found, continue
→ if missing, fail clearly with "prompt library missing"
```

Do not silently call DeepSeek online. Do not silently downgrade unless this is an explicit mode.

### Task 1: Build Prompt Manifest

**Files:**

- Create: `TitanFuzz-main/scripts/build_prompt_manifest.py`
- Create/update: `TitanFuzz-main/prompt_library_manifest.json`

Implementation behavior:

1. Scan `experiment/torch/*/prompts/` and `experiment/tf/*/prompts/`.
2. Include APIs only when `structured_info.txt` exists.
3. Mark whether `greedy_prompt.txt` exists.
4. Store file paths, sha256 hashes, and modified time.
5. Write one JSON file used by web UI and runner.

Manifest shape:

```json
{
  "version": "2026-06-16",
  "libraries": {
    "torch": {
      "torch.nn.functional.conv1d": {
        "api": "torch.nn.functional.conv1d",
        "structured_info": "experiment/torch/torch.nn.functional.conv1d/prompts/structured_info.txt",
        "greedy_prompt": "experiment/torch/torch.nn.functional.conv1d/prompts/greedy_prompt.txt",
        "has_greedy_prompt": true,
        "structured_sha256": "...",
        "greedy_sha256": "...",
        "updated_at": "2026-06-16T00:00:00"
      }
    }
  }
}
```

Acceptance checks:

```bash
cd /workspace/TitanFuzz-main
python scripts/build_prompt_manifest.py
python -m json.tool prompt_library_manifest.json >/dev/null
grep -n "torch.nn.functional.conv1d" prompt_library_manifest.json
```

### Task 2: Validate Prompt Library

**Files:**

- Create: `TitanFuzz-main/scripts/validate_prompt_library.py`

Implementation behavior:

1. Read `prompt_library_manifest.json`.
2. For each API, verify paths exist.
3. Verify `structured_info.txt` is non-empty.
4. For `structured_info.txt`, reuse the schema ideas already present in `constraint.py`:
   - top-level may include `params`
   - top-level should include `constraints`
   - parameter fields should be one of `dtype`, `range`, `structure`, `shape`, `default`
5. Print summary:

```text
Prompt library validation
torch total: 4608
torch ok: 4520
torch warning: 88
tf total: ...
```

Acceptance checks:

```bash
cd /workspace/TitanFuzz-main
python scripts/validate_prompt_library.py --manifest prompt_library_manifest.json
```

The validator may report warnings, but the demo API must pass:

```bash
python scripts/validate_prompt_library.py \
  --manifest prompt_library_manifest.json \
  --lib torch \
  --api torch.nn.functional.conv1d
```

Expected:

```text
OK torch.nn.functional.conv1d
```

## 3. One-Command Single API Demo

### Principle

The one-command demo is a wrapper over existing code:

```text
qwen_seed.py
→ ev_generation.py
→ driver.py
→ summary.json / summary.md
```

It should not rewrite the fuzzing algorithms.

### InCoder-6B Change Scope

Changing InCoder from 1B to 6B does not require a large code rewrite.

Current `ev_generation.py` already exposes:

```text
--model_name
```

So the implementation should pass:

```bash
--model_name facebook/incoder-6B
```

instead of relying on the default:

```text
facebook/incoder-1B
```

No core changes are needed in:

```text
ev_generation.py
model.py
util/
torch2cuda.py
driver.py
```

The only practical adjustment is resource control. InCoder-6B is much larger than InCoder-1B, so demo mode should use conservative generation settings:

```text
batch_size: 1
max_valid: 5
timeout: 300
```

Normal mode can try:

```text
batch_size: 2
max_valid: 20
timeout: 600
```

If the GPU has more memory and the run is stable, `batch_size` can be increased later. For a competition demo, prefer stable small-batch execution over aggressive throughput.

The wrapper script must make the mutation model explicit:

```bash
python ev_generation.py \
  --model_name "$MUT_MODEL" \
  ...
```

with default:

```text
MUT_MODEL=facebook/incoder-6B
```

### Task 3: Add Python Demo Runner

**Files:**

- Create: `TitanFuzz-main/scripts/run_one_api_demo.py`

Command interface:

```bash
python scripts/run_one_api_demo.py \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --constraints_dir experiment/torch \
  --qwen_model ../Qwen2.5-Coder-7B-Instruct \
  --mut_model facebook/incoder-6B \
  --out demo_runs/conv1d_demo \
  --mode demo \
  --cuda_device 0
```

Arguments:

```text
--lib              torch or tf
--api              target API
--constraints_dir  experiment/torch or experiment/tf
--qwen_model       local Qwen model path
--mut_model        facebook/incoder-6B by default
--out              output root
--mode             demo or normal
--cuda_device      GPU id
--force_redo       delete/rebuild this demo output
```

Demo mode parameters:

```text
qwen n_samples: 5
qwen min_valid: 2
qwen max_rounds: 1
qwen per_api_budget: 300
qwen validate_timeout: 30
ev max_valid: 5
ev batch_size: 1
ev timeout: 300
```

Normal mode parameters:

```text
qwen n_samples: 10
qwen min_valid: 5
qwen max_rounds: 2
qwen per_api_budget: 600
qwen validate_timeout: 30
ev max_valid: 20
ev batch_size: 2
ev timeout: 600
```

Pipeline steps:

1. Verify `experiment/<lib>/<api>/prompts/structured_info.txt`.
2. Create output folders.
3. Run `qwen_seed.py`.
4. Count `qwen_seed/fix/<api>/*.py`.
5. If zero valid seeds, stop with clear summary.
6. Run `ev_generation.py`.
7. Run `driver.py`; add `--tf` only for TensorFlow.
8. Create `summary.json`.
9. Create `summary.md`.

Output layout:

```text
demo_runs/conv1d_demo/
  status.json
  summary.json
  summary.md
  logs/
    01_qwen_seed.log
    02_ev_generation.log
    03_driver.log
  qwen_seed/
    raw/
    fix/
    qwen_seed_summary_full.json
  Results/
    torch/
      seed/
      valid/
      exception/
      crash/
      notarget/
      hangs/
      flaky/
      outputs.json
      trace.txt
```

`status.json` should update after each stage:

```json
{
  "job_id": "manual",
  "lib": "torch",
  "api": "torch.nn.functional.conv1d",
  "stage": "driver",
  "status": "running",
  "started_at": "2026-06-16T10:00:00",
  "updated_at": "2026-06-16T10:03:00",
  "stages": {
    "prompt_check": "success",
    "qwen_seed": "success",
    "ev_generation": "success",
    "driver": "running"
  }
}
```

`summary.json` should contain:

```json
{
  "lib": "torch",
  "api": "torch.nn.functional.conv1d",
  "prompt_library": "found",
  "qwen_valid_seed_count": 2,
  "ev_seed_count": 2,
  "ev_valid_count": 5,
  "ev_exception_count": 3,
  "ev_crash_count": 0,
  "trace_path": "demo_runs/conv1d_demo/Results/torch/trace.txt",
  "catch_count": 1,
  "status": "success"
}
```

Acceptance checks:

```bash
cd /workspace/TitanFuzz-main
python scripts/run_one_api_demo.py \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --constraints_dir experiment/torch \
  --qwen_model ../Qwen2.5-Coder-7B-Instruct \
  --mut_model facebook/incoder-6B \
  --out demo_runs/conv1d_demo \
  --mode demo \
  --cuda_device 0 \
  --force_redo

cat demo_runs/conv1d_demo/summary.md
ls demo_runs/conv1d_demo/Results/torch/trace.txt
```

### Task 4: Add Human-Friendly Shell Wrapper

**Files:**

- Create: `TitanFuzz-main/scripts/run_one_api_demo.sh`

Behavior:

1. `cd` to repo root.
2. Forward all arguments to `python scripts/run_one_api_demo.py`.
3. Fail if not run from a valid `TitanFuzz-main` tree.

Usage:

```bash
bash scripts/run_one_api_demo.sh \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d_demo \
  --mode demo
```

This is the command to show in PPT and frontend.

## 4. Curated Bug Evidence Repository

### Task 5: Add Candidate Bug Index

**Files:**

- Create: `TitanFuzz-main/reports/bug_candidates.json`
- Create: `TitanFuzz-main/reports/bug_candidates/fractional_max_pool3d.md`
- Create: `TitanFuzz-main/reports/bug_candidates/index_exception_mismatch.md`

Initial `bug_candidates.json` shape:

```json
[
  {
    "id": "PT-N1-002",
    "framework": "PyTorch",
    "api": "torch.nn.functional.fractional_max_pool3d",
    "type": "CPU success / CUDA invalid argument",
    "severity": "High",
    "status": "Strong Candidate",
    "version": "PyTorch 2.11.0+cu130",
    "minimized": true,
    "reproducible": true,
    "detail": "reports/bug_candidates/fractional_max_pool3d.md"
  },
  {
    "id": "PT-N1-003",
    "framework": "PyTorch",
    "api": "torch.Tensor.gather / torch.Tensor.take",
    "type": "CPU RuntimeError vs CUDA device-side assert",
    "severity": "Medium",
    "status": "Candidate",
    "version": "PyTorch 2.11.0+cu130",
    "minimized": true,
    "reproducible": true,
    "detail": "reports/bug_candidates/index_exception_mismatch.md"
  }
]
```

Do not include alias/out candidates as accepted bug candidates.

Acceptance checks:

```bash
cd /workspace/TitanFuzz-main
python -m json.tool reports/bug_candidates.json >/dev/null
```

## 5. Local Web Backend

### Design Choice

Use Python standard library instead of FastAPI/Flask for the first version. The current project has minimal dependencies, and the demo server only needs a few JSON endpoints.

### Task 6: Add Backend Server

**Files:**

- Create: `TitanFuzz-main/webapp/server.py`

Server command:

```bash
python webapp/server.py --host 127.0.0.1 --port 8008
```

Static pages:

```text
GET /
GET /static/styles.css
GET /static/app.js
```

API endpoints:

```text
GET  /api/dashboard
GET  /api/apis?lib=torch
GET  /api/prompt?lib=torch&api=torch.nn.functional.conv1d
POST /api/run-demo
GET  /api/jobs/<job_id>
GET  /api/bugs
GET  /api/bugs/<bug_id>
GET  /api/file?path=<safe-relative-path>
```

Endpoint behavior:

- `/api/dashboard` reads manifest and reports counts.
- `/api/apis` lists APIs from `prompt_library_manifest.json`.
- `/api/prompt` returns `structured_info.txt` and `greedy_prompt.txt`.
- `/api/run-demo` starts `scripts/run_one_api_demo.py` in a background process.
- `/api/jobs/<job_id>` returns `status.json`, `summary.json`, and log tails.
- `/api/bugs` returns `reports/bug_candidates.json`.
- `/api/bugs/<bug_id>` returns JSON metadata plus markdown detail.

Security rules:

- API name must exist in manifest.
- Output path must be under `demo_runs/`.
- Backend must not accept arbitrary command strings.
- `/api/file` must reject absolute paths and `..`.

Acceptance checks:

```bash
cd /workspace/TitanFuzz-main
python webapp/server.py --host 127.0.0.1 --port 8008
```

Then in another terminal:

```bash
curl http://127.0.0.1:8008/api/dashboard
curl "http://127.0.0.1:8008/api/apis?lib=torch" | head
curl "http://127.0.0.1:8008/api/prompt?lib=torch&api=torch.nn.functional.conv1d"
```

## 6. Static Frontend

### Task 7: Build Workbench UI

**Files:**

- Create: `TitanFuzz-main/webapp/static/index.html`
- Create: `TitanFuzz-main/webapp/static/styles.css`
- Create: `TitanFuzz-main/webapp/static/app.js`

Layout:

```text
Left sidebar:
  Dashboard
  Single API Demo
  Prompt Library
  Bug Repository

Main area:
  Active page
```

Do not build a landing page. First screen is Dashboard.

### Dashboard page

Display:

```text
Prompt APIs
Bug candidates
Strong candidates
Latest demo run
```

Cards:

```text
Prompt Library Coverage
Seed Generation
Mutation Results
Candidate Bugs
```

### Single API Demo page

Controls:

```text
Library select: torch / tf
API autocomplete
Mode select: demo / normal
Run button
```

Progress:

```text
Prompt Library
Qwen Seed
Seed Repair
InCoder Mutation
CPU/GPU Oracle
Summary
```

Each stage has status:

```text
pending / running / success / failed
```

Show log tail from backend.

### Prompt Library page

Controls:

```text
Library select
API autocomplete
```

Display two panels:

```text
structured_info.txt
greedy_prompt.txt
```

Also show:

```text
file hash
file path
```

### Bug Repository page

Table columns:

```text
ID
Framework
API
Type
Severity
Status
Minimized
Reproducible
```

Clicking a row opens detail:

```text
summary
markdown evidence
copy reproduction command
export report
```

Acceptance checks:

```bash
cd /workspace/TitanFuzz-main
python webapp/server.py --host 127.0.0.1 --port 8008
```

Open:

```text
http://127.0.0.1:8008/
```

Verify:

- Dashboard loads.
- Prompt Library can show `torch.nn.functional.conv1d`.
- Bug Repository shows candidate rows.
- Single API Demo can start a job and display progress.

## 7. Report Export

### Task 8: Add Markdown Export

**Files:**

- Modify: `TitanFuzz-main/webapp/server.py`
- Modify: `TitanFuzz-main/webapp/static/app.js`

For a bug candidate, export a markdown file containing:

```text
# Title
Environment
Target API
Minimal Reproduction
CPU Output
GPU Output
Expected Behavior
Actual Behavior
Triage Notes
```

For a demo run, export:

```text
# Single API Demo Report
API
Prompt Library Status
Qwen Seed Counts
Mutation Counts
Trace Catch Count
Links to logs
```

Acceptance check:

```bash
curl "http://127.0.0.1:8008/api/export/bug/PT-N1-002"
curl "http://127.0.0.1:8008/api/export/job/<job_id>"
```

## 8. Documentation and Competition Materials

### Task 9: Update Project README

**Files:**

- Modify: `TitanFuzz-main/README.md`

Add a section near the top:

```text
## TensorGuard Workbench Demo

This project extends TitanFuzz with:
- offline DeepSeek-distilled prompt/constraint library
- Qwen seed generation
- four-layer seed repair and validation
- InCoder-6B evolutionary mutation
- CPU/GPU differential oracle
- web-based bug triage workbench
```

Add commands:

```bash
python scripts/build_prompt_manifest.py
python scripts/validate_prompt_library.py --lib torch --api torch.nn.functional.conv1d
bash scripts/run_one_api_demo.sh --lib torch --api torch.nn.functional.conv1d --out demo_runs/conv1d_demo --mode demo
python webapp/server.py --host 127.0.0.1 --port 8008
```

### Task 10: Add Demo Script for Presentation

**Files:**

- Create: `TitanFuzz-main/docs/demo_script.md`

The demo script should say:

```text
1. This is not a real-time full-framework scanner.
2. DeepSeek is used offline to build the local prompt library.
3. The frontend now chooses one API and starts an end-to-end demo run.
4. The bug repository shows previously triaged high-signal candidates.
5. The strongest current PyTorch candidate is fractional_max_pool3d.
```

## 9. Testing Plan

### Unit-level checks

```bash
python scripts/build_prompt_manifest.py
python -m json.tool prompt_library_manifest.json >/dev/null
python scripts/validate_prompt_library.py --lib torch --api torch.nn.functional.conv1d
python -m json.tool reports/bug_candidates.json >/dev/null
```

### Pipeline smoke test

```bash
bash scripts/run_one_api_demo.sh \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d_demo \
  --mode demo \
  --force_redo
```

Expected:

```text
demo_runs/conv1d_demo/summary.json exists
demo_runs/conv1d_demo/summary.md exists
demo_runs/conv1d_demo/logs/01_qwen_seed.log exists
demo_runs/conv1d_demo/Results/torch/trace.txt exists, unless qwen seed generation produced zero valid seeds; in that case summary must explain the failure.
```

### Web smoke test

```bash
python webapp/server.py --host 127.0.0.1 --port 8008
```

Open:

```text
http://127.0.0.1:8008/
```

Verify:

- Dashboard counts load.
- Prompt page loads `conv1d`.
- Bug table loads.
- Run Demo starts a job.
- Job status updates without page refresh.

## 10. Milestones

### Milestone 1: CLI Demo Works

Deliverables:

- `prompt_library_manifest.json`
- prompt validator
- `scripts/run_one_api_demo.py`
- `scripts/run_one_api_demo.sh`
- `demo_runs/conv1d_demo/summary.md`

This is the minimum useful milestone.

### Milestone 2: Evidence Repository Works

Deliverables:

- `reports/bug_candidates.json`
- markdown evidence files
- README section explaining current confirmed candidates vs rejected candidates

### Milestone 3: Web Workbench Works

Deliverables:

- `webapp/server.py`
- static frontend
- Dashboard
- Single API Demo page
- Prompt Library page
- Bug Repository page

### Milestone 4: Competition Packaging

Deliverables:

- README usage instructions
- `docs/demo_script.md`
- screenshots
- PPT integration
- GitHub repository cleanup

## 11. What Not to Build Now

Do not build these in the first version:

- Online DeepSeek calls.
- Arbitrary user-uploaded Python execution.
- Full API fuzzing from the web UI.
- Multi-user auth.
- Database storage.
- Complex task queue.
- Claiming "confirmed official bugs" without upstream confirmation.
- Decorative landing page instead of the workbench.

## 12. Recommended Development Order

1. Freeze prompt library and build manifest.
2. Build one-command CLI demo.
3. Add curated bug candidate repository.
4. Build backend API.
5. Build static frontend.
6. Add report export.
7. Update README and demo script.
8. Record screenshots / short demo video for PPT.

The key risk is not frontend difficulty. The key risk is demo instability from local model loading and GPU memory. Therefore the CLI demo must be finished and stable before the frontend is implemented.
