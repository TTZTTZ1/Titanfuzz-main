# Bug Replay Status Badges Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the three Bug replay header counters distinct semantic styling without changing their live data bindings or layout behavior.

**Architecture:** Keep the existing counter container and Vue expressions. Add stable modifier classes to each counter item, then style those modifiers with existing design tokens and small status dots.

**Tech Stack:** Vue 3, scoped CSS, Vitest, Vue Test Utils

---

### Task 1: Add Semantic Counter Variants

**Files:**
- Modify: `webapp/frontend/src/views/BugReplayView.test.ts`
- Modify: `webapp/frontend/src/views/BugReplayView.vue`

- [x] **Step 1: Write the failing component test**

Add an assertion that the three counter elements expose `confirmed`, `candidate`, and `minimize` modifier classes while retaining their rendered values.

```ts
const counters = wrapper.findAll(".bug-replay-view__count-item");
expect(counters).toHaveLength(3);
expect(counters.map((item) => item.classes())).toEqual([
  expect.arrayContaining(["bug-replay-view__count-item--confirmed"]),
  expect.arrayContaining(["bug-replay-view__count-item--candidate"]),
  expect.arrayContaining(["bug-replay-view__count-item--minimize"]),
]);
expect(counters.map((item) => item.get("b").text())).toEqual(["1", "1", "1"]);
```

- [x] **Step 2: Run the focused test and verify RED**

Run: `npm test -- --run src/views/BugReplayView.test.ts`

Expected: FAIL because `.bug-replay-view__count-item` does not exist.

- [x] **Step 3: Add modifier classes and semantic styling**

Use the existing live expressions and add classes:

```vue
<span class="bug-replay-view__count-item bug-replay-view__count-item--confirmed">...</span>
<span class="bug-replay-view__count-item bug-replay-view__count-item--candidate">...</span>
<span class="bug-replay-view__count-item bug-replay-view__count-item--minimize">...</span>
```

Style the shared item as a compact badge with a `::before` status dot. Apply green, amber, and blue border/background/text colors through the modifier classes. Preserve the existing mobile rule that hides the entire counter group below 720px.

- [x] **Step 4: Run focused test and verify GREEN**

Run: `npm test -- --run src/views/BugReplayView.test.ts`

Expected: all `BugReplayView` tests pass.

- [x] **Step 5: Verify the full frontend**

Run: `npm test -- --run`

Expected: all test files pass.

Run: `npm run build`

Expected: Vue type checking and Vite production build succeed.

- [x] **Step 6: Verify the rendered header**

Reload `http://127.0.0.1:8044/#bug-replay`, inspect the three counter badges, and confirm the header has no horizontal overflow or wrapping at the current desktop viewport.
