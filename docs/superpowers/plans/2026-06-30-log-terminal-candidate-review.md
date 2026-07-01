# Log Terminal And Candidate Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a fixed, stage-switchable log terminal and a polished aligned candidate review workbench.

**Architecture:** Keep the existing API payloads and review actions. Add local stage selection inside `LiveLog`, constrain all terminal/code overflow at component boundaries, and restructure only the candidate workbench markup and CSS.

**Tech Stack:** Vue 3, TypeScript, scoped CSS, Vitest.

---

### Task 1: Stage-switchable fixed log terminal

**Files:**
- Modify: `webapp/frontend/src/components/api/LiveLog.vue`
- Modify: `webapp/frontend/src/components/api/LiveLog.test.ts`
- Modify: `webapp/frontend/src/views/ApiRunView.vue`

- [ ] Write failing tests for Qwen/InCoder/driver tab switching and unavailable-stage disabling.
- [ ] Replace the auto-follow control with stage tabs while retaining automatic tail behavior internally.
- [ ] Constrain terminal width and height and keep both scroll directions inside the body.
- [ ] Key the terminal by job ID so stage selection resets for a new run.

### Task 2: Candidate review visual workbench

**Files:**
- Modify: `webapp/frontend/src/views/BugReplayView.vue`
- Modify: `webapp/frontend/src/views/BugReplayView.test.ts`

- [ ] Write failing structure assertions for aligned columns, wrapping source metadata, file headers, and review footer.
- [ ] Recompose the two code headers and review card without changing status actions.
- [ ] Use identical grid tracks for evidence and workbench sections.
- [ ] Constrain code and evidence overflow and preserve the existing responsive stack.

### Task 3: Verification and build

**Files:**
- Modify generated assets under `webapp/static/`

- [ ] Run focused component and view tests.
- [ ] Run the complete frontend test suite.
- [ ] Build production assets.
- [ ] Verify desktop and compact browser widths have no horizontal page overflow.
