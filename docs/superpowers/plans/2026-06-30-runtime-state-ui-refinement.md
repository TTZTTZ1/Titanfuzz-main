# Runtime State UI Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:test-driven-development and implement each task inline without subagents.

**Goal:** Correct job-state persistence and align the API-run and bug-replay workbenches with the approved visual design.

**Architecture:** Keep pipeline output formats stable. Add small backend lookup fields, derive UI state in focused domain helpers, and keep visual components driven by live payloads rather than constants.

**Tech Stack:** Python standard-library HTTP server, Vue 3, TypeScript, Vitest, Vite.

---

### Task 1: Single-API state helpers

- Add failing tests for selecting a running metric stage, cumulative duration, and candidate collection labels.
- Implement pure helpers and extend the API job types.
- Keep pending tabs disabled and completed stages persistent.

### Task 2: Single-API presentation

- Recompose the control row with equal-height fields and a candidate-state field.
- Restyle Results composition to the approved bar/list design.
- Replace the GPU chart with latest-sample utilization and memory gauges.
- Verify the existing stage charts continue to update and switch correctly.

### Task 3: Persistent latest reproduction

- Add a failing backend test proving latest reproduction lookup is scoped by bug id.
- Include the latest job id in confirmed-bug detail.
- Load that job whenever a bug is selected, preserving the latest run across navigation.

### Task 4: Replay environment and evidence styling

- Load `/api/environment` with the page and render it before any reproduction.
- Strengthen idle, running, success, review, and Expected/Observed visual states.
- Preserve immutable reports and historical job directories.

### Task 5: Verification

- Run targeted red/green tests, full Python contract tests, all frontend tests, and the production build.
- Start the local server and use browser QA for API-run and bug-replay pages at desktop and compact viewport widths.
