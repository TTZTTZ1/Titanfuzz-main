# Live Log and Candidate Minimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the runtime log a stable viewport with coherent terminal progress and provide a persistent, editable CPU/GPU candidate-minimization workflow.

**Architecture:** Normalize log output at the HTTP boundary without mutating raw files. Extend `CandidateStore` with server-owned workspace paths and atomic draft persistence, then add an isolated validation runner and expose it through focused endpoints. The Vue candidate workbench edits the persisted draft, starts validation, polls structured results, and keeps the final Bug decision human-controlled.

**Tech Stack:** Python standard library HTTP server and subprocesses, Vue 3, TypeScript, Vitest, Python unittest

---

### Task 1: Terminal Log Normalization and Fixed Viewport

**Files:**
- Modify: `webapp/server.py`
- Modify: `test/test_runtime_data.py`
- Modify: `webapp/frontend/src/components/api/LiveLog.vue`
- Modify: `webapp/frontend/src/components/api/LiveLog.test.ts`
- Modify: `webapp/frontend/src/views/ApiRunView.vue`
- Modify: `webapp/frontend/src/views/ApiRunView.test.ts`

- [x] **Step 1: Add failing normalization and layout tests**

Add Python assertions that ANSI sequences are removed, ordinary lines remain, and `Loading weights: 0%\r...100%` returns only the final frame. Add Vue assertions for a fixed log-card class and internal vertical scrolling contract.

- [x] **Step 2: Run focused tests and verify RED**

Run: `python -m unittest test.test_runtime_data -v && cd webapp/frontend && npm test -- --run src/components/api/LiveLog.test.ts src/views/ApiRunView.test.ts`

Expected: FAIL because terminal normalization and fixed-height contracts do not exist.

- [x] **Step 3: Implement normalization and fixed sizing**

Add `normalize_terminal_output(text)` and call it from `tail()`. Strip CSI ANSI sequences and interpret each carriage return as replacing the current terminal line. Give the desktop log column/card a fixed `24rem` height and narrow layouts an `18rem` height; retain `overflow-y:auto` on the body and no horizontal overflow.

- [x] **Step 4: Run focused tests and verify GREEN**

Run the commands from Step 2 and confirm both suites pass.

### Task 2: Persistent Candidate Drafts

**Files:**
- Modify: `webapp/candidates.py`
- Modify: `test/test_candidates.py`
- Modify: `webapp/server.py`

- [x] **Step 1: Add failing draft persistence tests**

Create a candidate cluster fixture, assert that an unsaved draft equals the representative source, `save_cluster_draft()` persists edited code under the server-owned workspace, and `reset_cluster_draft()` restores the representative. Assert traversal-like cluster IDs cannot select arbitrary paths.

- [x] **Step 2: Run tests and verify RED**

Run: `python -m unittest test.test_candidates -v`

Expected: FAIL because draft persistence methods do not exist.

- [x] **Step 3: Implement atomic workspace storage**

Add bounded UTF-8 draft validation, a hashed server-owned workspace directory, atomic `repro.py` and `metadata.json` writes, saved-draft metadata in `get_cluster()`, and server payload handlers for `/draft` and `/draft/reset`.

- [x] **Step 4: Run tests and verify GREEN**

Run the command from Step 2 and confirm all candidate tests pass.

### Task 3: Isolated CPU/GPU Candidate Validation

**Files:**
- Create: `webapp/candidate_validation.py`
- Create: `test/test_candidate_validation.py`
- Modify: `webapp/server.py`
- Modify: `webapp/frontend/src/types/tensorguard.ts`
- Modify: `webapp/frontend/src/services/tensorguard.ts`
- Modify: `webapp/frontend/src/services/tensorguard.test.ts`

- [x] **Step 1: Add failing validation-runner tests**

Test CPU and GPU environment construction, separate log paths, timeout classification, return-code/signal capture, and polling payloads using short temporary Python programs.

- [x] **Step 2: Run tests and verify RED**

Run: `python -m unittest test.test_candidate_validation -v`

Expected: FAIL because the validation runner is absent.

- [x] **Step 3: Implement runner and endpoints**

Run the saved draft with `shell=False`, `sys.executable`, `CUDA_VISIBLE_DEVICES=""` and `"0"`, a 60-second timeout, core dumps disabled, and separate logs. Add start/poll endpoints plus matching TypeScript contracts and service methods.

- [x] **Step 4: Run Python and service tests and verify GREEN**

Run: `python -m unittest test.test_candidate_validation -v && cd webapp/frontend && npm test -- --run src/services/tensorguard.test.ts`

Expected: PASS.

### Task 4: Editable Candidate Minimization UI

**Files:**
- Modify: `webapp/frontend/src/views/BugReplayView.vue`
- Modify: `webapp/frontend/src/views/BugReplayView.test.ts`

- [x] **Step 1: Add failing UI workflow tests**

Assert that the minimization panel contains an editable code field, save/reset/CPU+GPU validation controls, unsaved-state feedback, validation polling, and separate CPU/GPU outputs. Assert validation state survives a detail reload through the backend payload.

- [x] **Step 2: Run test and verify RED**

Run: `cd webapp/frontend && npm test -- --run src/views/BugReplayView.test.ts`

Expected: FAIL because the draft is read-only and no validation actions exist.

- [x] **Step 3: Implement the workflow**

Bind a local draft to the selected cluster, save and reset through the new services, start CPU+GPU validation, poll until finished, render fixed scrollable output panes, explain the delete-and-retest loop, and enable final collection only after a completed validation record while preserving human review.

- [x] **Step 4: Run test and verify GREEN**

Run the command from Step 2 and confirm all BugReplayView tests pass.

### Task 5: Full Verification and Production Build

**Files:**
- Regenerate: `webapp/static/index.html`
- Regenerate: `webapp/static/assets/*`

- [x] **Step 1: Run all Python tests**

Run: `python -m unittest discover -s test -v`

- [x] **Step 2: Run all frontend tests**

Run: `cd webapp/frontend && npm test -- --run`

- [x] **Step 3: Build production assets**

Run: `cd webapp/frontend && npm run build`

- [x] **Step 4: Verify in the browser**

Confirm fixed log height, internal scrolling, one coherent loading-progress frame, editable persisted candidate draft, and separate CPU/GPU validation results without page-level horizontal overflow.
