# Confirmed Replay Detail Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the confirmed-bug evidence detail so source/output are bounded independent panels and environment/execution/report form one compact environment-first row.

**Architecture:** Keep the existing `BugReplayView` data flow and event handlers. Change only the confirmed-detail markup and scoped CSS, using semantic class names that tests can assert without depending on visual pixel values.

**Tech Stack:** Vue 3, TypeScript, Vitest, Vue Test Utils, scoped CSS, Vite

---

### Task 1: Lock the confirmed-detail structure with tests

**Files:**
- Modify: `webapp/frontend/src/views/BugReplayView.test.ts`

- [ ] Add assertions that the confirmed view renders two `.bug-replay-view__evidence-pane` elements labeled `repro.py` and `CURRENT RUN OUTPUT`.
- [ ] Add assertions that `.bug-replay-view__confirmed-tools` contains environment, execution, and report panels in that order.
- [ ] Add assertions for distinct confirmed and minimized status badge classes.
- [ ] Run `npm test -- --run src/views/BugReplayView.test.ts` and confirm the new assertions fail because the classes do not exist.

### Task 2: Implement the confirmed evidence and tool layout

**Files:**
- Modify: `webapp/frontend/src/views/BugReplayView.vue`

- [ ] Replace the shared code-grid wrapper with two sibling evidence panes while retaining `detail.repro_code` and `currentOutput` bindings.
- [ ] Replace the separate actions and environment sections with a three-panel `.bug-replay-view__confirmed-tools` row ordered environment, execution, report.
- [ ] Preserve device selection, run, report generation, download, and environment bindings unchanged.
- [ ] Add scoped styles for semantic status badges, fixed evidence panes with internal scrolling, compact environment values, and responsive stacking.
- [ ] Run `npm test -- --run src/views/BugReplayView.test.ts` and confirm all focused tests pass.

### Task 3: Verify and build

**Files:**
- Regenerate: `webapp/static/index.html`
- Regenerate: `webapp/static/assets/*`

- [ ] Run `npm test -- --run` and confirm the complete frontend suite passes.
- [ ] Run `npm run build` and confirm TypeScript and Vite production build pass.
- [ ] Refresh `http://127.0.0.1:8044/#bug-replay` and inspect desktop and narrow widths for overflow, fixed panel sizing, status colors, and preserved controls.
- [ ] Run `git diff --check` and review the final working-tree scope.

