# TensorGuard Blue Frontend Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the approved cobalt-blue design the default TensorGuard interface across the overview, single-API, and bug-reproduction views without changing runtime behavior or backend contracts.

**Architecture:** Keep the existing static HTML, DOM IDs, API client, job polling, and chart data flow intact. Replace the visual token layer and component styling in `styles.css`, update the dependency-free SVG chart palette in `charts.js`, and use contract tests to prevent accidental changes to live-data and interaction boundaries.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, dependency-free SVG charts, Python assertion-based contract tests, Node.js assertion tests.

---

## File Map

- Modify `webapp/static/styles.css`: blue design tokens, global shell, all three page surfaces, responsive and print styling.
- Modify `webapp/static/charts.js`: approved blue/violet/cyan chart palette only; chart calculations remain unchanged.
- Modify `webapp/static/index.html` only if a semantic wrapper class is required; preserve every existing ID and script reference.
- Modify `test/test_frontend_contract.py`: visual token and page-structure regression checks.
- Modify `test/test_charts.js`: chart palette and line-gap regression checks.
- Use `docs/design-previews/blue-overview.html` as the visual reference, not as production markup.
- Do not modify `webapp/static/app.js`, `webapp/server.py`, `scripts/run_one_api_demo.py`, Results data, or confirmed bug data unless a failing test proves an existing presentation-only class hook is missing.

### Task 1: Establish The Blue Theme Contract

**Files:**
- Modify: `test/test_frontend_contract.py`
- Modify: `webapp/static/styles.css:1-128`

- [ ] **Step 1: Write the failing blue-theme contract test**

Add `STYLES` beside the existing paths and add this test:

```python
STYLES = ROOT / "webapp" / "static" / "styles.css"


def test_frontend_uses_approved_blue_theme_tokens():
    css = STYLES.read_text(encoding="utf-8")
    for expected in (
        "--primary: #246bfd;",
        "--primary-soft: #eaf1ff;",
        "--shell: #131c2d;",
        "--canvas-start: #f8fbff;",
        "--canvas-mid: #edf4ff;",
        "--canvas-end: #f8f5ff;",
    ):
        assert expected in css, expected
    assert "background: linear-gradient(" in css
    assert "--teal:" not in css
```

Call `test_frontend_uses_approved_blue_theme_tokens()` in the script's `__main__` block.

- [ ] **Step 2: Run the contract test and verify it fails**

Run:

```bash
python3 test/test_frontend_contract.py
```

Expected: `AssertionError: --primary: #246bfd;` because the current production theme still uses teal tokens.

- [ ] **Step 3: Replace the root visual tokens and global shell styles**

Replace the current `:root` token block with:

```css
:root {
  --canvas-start: #f8fbff;
  --canvas-mid: #edf4ff;
  --canvas-end: #f8f5ff;
  --surface: rgba(255, 255, 255, .94);
  --surface-solid: #ffffff;
  --surface-muted: #f5f8fc;
  --shell: #131c2d;
  --shell-active: #202d43;
  --ink: #172033;
  --muted: #68758d;
  --line: #dbe3f0;
  --line-strong: #c7d3e5;
  --primary: #246bfd;
  --primary-hover: #195ce5;
  --primary-soft: #eaf1ff;
  --violet: #8269d6;
  --cyan: #1598bd;
  --amber: #b36f16;
  --amber-soft: #fff1d8;
  --red: #c64756;
  --red-soft: #fbe9ec;
  --green: #168367;
  --green-soft: #e5f5f0;
  --radius: 7px;
  --shadow: 0 14px 34px rgba(47, 73, 117, .07);
}
```

Update the global surfaces without changing layout contracts:

```css
body {
  margin: 0;
  background: linear-gradient(135deg, var(--canvas-start) 0%, var(--canvas-mid) 52%, var(--canvas-end) 100%);
  background-attachment: fixed;
  color: var(--ink);
}

.sidebar {
  background: var(--shell);
  border-right: 1px solid #0b1220;
  box-shadow: 12px 0 32px rgba(28, 46, 84, .08);
}

.nav-item.active {
  color: #fff;
  border-left-color: var(--primary);
  background: var(--shell-active);
}

button.primary {
  border-color: var(--primary);
  background: var(--primary);
  box-shadow: 0 7px 18px rgba(36, 107, 253, .18);
}

button.primary:hover { background: var(--primary-hover); }
```

Replace every use of `var(--teal)` with `var(--primary)` and every use of `var(--teal-soft)` with `var(--primary-soft)`. Preserve `--green`, `--amber`, and `--red` for semantic statuses.

- [ ] **Step 4: Run the contract test and verify it passes**

Run:

```bash
python3 test/test_frontend_contract.py
```

Expected: `ok`.

- [ ] **Step 5: Commit the blue foundation**

```bash
git add test/test_frontend_contract.py webapp/static/styles.css
git commit -m "style: establish TensorGuard blue theme"
```

### Task 2: Restyle The Global Shell And Overview

**Files:**
- Modify: `test/test_frontend_contract.py`
- Modify: `webapp/static/styles.css:30-195`
- Verify: `webapp/static/index.html:11-103`

- [ ] **Step 1: Write a failing overview-structure contract**

Add:

```python
def test_overview_keeps_dense_dashboard_structure():
    html = INDEX.read_text(encoding="utf-8")
    css = STYLES.read_text(encoding="utf-8")
    for expected in ("metric-strip", "overview-grid", "process-line", "evidence-surface"):
        assert expected in html, expected
    for expected in ("var(--shadow)", "backdrop-filter: blur", ".metric-strip", ".process-line"):
        assert expected in css, expected
```

Call it from `__main__`.

- [ ] **Step 2: Run the test and verify the new visual assertion fails**

Run:

```bash
python3 test/test_frontend_contract.py
```

Expected: failure on `var(--shadow)` or `backdrop-filter: blur`.

- [ ] **Step 3: Apply the approved overview hierarchy**

Keep the existing overview HTML and update the corresponding CSS:

```css
.main {
  min-width: 0;
  padding: 30px clamp(24px, 3.2vw, 48px) 52px;
}

.page-head {
  margin-bottom: 18px;
  padding: 14px 0 19px;
  border-bottom: 1px solid rgba(199, 211, 229, .9);
  backdrop-filter: blur(12px);
}

.metric-strip {
  border: 1px solid var(--line-strong);
  border-radius: var(--radius);
  background: var(--surface);
  box-shadow: var(--shadow);
  overflow: hidden;
}

.surface {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.bar-track { background: #edf2fa; }
.bar-fill { background: var(--primary); }
.bar-row:nth-child(2n) .bar-fill { background: var(--violet); }
.process-line div { background: rgba(247, 250, 255, .88); }
.process-line div span { color: var(--primary); }
```

Do not add trend charts or values to the overview. Keep the overview data populated by the existing `/api/overview` and `/api/environment` calls.

- [ ] **Step 4: Run the frontend contracts**

Run:

```bash
python3 test/test_frontend_contract.py
```

Expected: `ok`.

- [ ] **Step 5: Commit the shell and overview**

```bash
git add test/test_frontend_contract.py webapp/static/styles.css
git commit -m "style: polish blue overview workspace"
```

### Task 3: Restyle Single-API Controls, Stages, And Charts

**Files:**
- Modify: `test/test_frontend_contract.py`
- Modify: `test/test_charts.js`
- Modify: `webapp/static/styles.css:174-260`
- Modify: `webapp/static/charts.js:1-115`
- Verify: `webapp/static/index.html:105-153`

- [ ] **Step 1: Write failing single-API and chart-palette tests**

Add to `test/test_frontend_contract.py`:

```python
def test_single_api_uses_blue_focus_and_stage_states():
    css = STYLES.read_text(encoding="utf-8")
    for expected in (
        "border-color: var(--primary)",
        ".stage-tab.active",
        "background: var(--primary);",
        ".match-item.active",
    ):
        assert expected in css, expected
```

Call it from `__main__`.

Replace `test/test_charts.js` with the existing line-gap assertion plus:

```javascript
const { buildPath, COLORS } = global.window.TensorCharts;

assert.deepStrictEqual(
  COLORS.slice(0, 5),
  ["#246bfd", "#8269d6", "#1598bd", "#b36f16", "#c64756"],
);
```

- [ ] **Step 2: Run both tests and verify the chart test fails**

Run:

```bash
python3 test/test_frontend_contract.py
node test/test_charts.js
```

Expected: Python may pass after Task 1 replacements; Node fails because `COLORS` is not exported and still begins with teal.

- [ ] **Step 3: Apply the blue control and stage styles**

Use the following presentation rules while retaining existing selectors:

```css
input:focus, select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(36, 107, 253, .12);
}

.match-item:hover, .bug-item:hover { background: #f0f5ff; }
.match-item.active, .bug-item.active {
  background: var(--primary-soft);
  box-shadow: inset 3px 0 var(--primary);
}

.stage-tab.active {
  color: #fff;
  background: var(--primary);
  box-shadow: 0 4px 10px rgba(36, 107, 253, .18);
}

.chart-frame { background: rgba(248, 251, 255, .9); }
.chart-grid-line { stroke: #e2e9f5; }
.progress-track { background: #eaf0f9; }
.progress-track span { background: var(--primary); }
```

Do not alter `pending`, `running`, `success`, `failed`, or `skipped` class assignment in `app.js`.

- [ ] **Step 4: Replace and export only the chart palette**

In `charts.js`, replace the palette and export it:

```javascript
const COLORS = ["#246bfd", "#8269d6", "#1598bd", "#b36f16", "#c64756", "#68758d", "#168367"];

window.TensorCharts = { COLORS, buildPath, renderLineChart, renderStackedBar, renderProgress };
```

Leave `buildPath`, chart scales, null-gap behavior, totals, and progress calculations unchanged.

- [ ] **Step 5: Run the single-API and chart tests**

Run:

```bash
python3 test/test_frontend_contract.py
node test/test_charts.js
node --check webapp/static/charts.js
```

Expected: each command prints `ok` or exits with code 0.

- [ ] **Step 6: Commit the single-API visual update**

```bash
git add test/test_frontend_contract.py test/test_charts.js webapp/static/styles.css webapp/static/charts.js
git commit -m "style: update single API workspace palette"
```

### Task 4: Restyle Bug Evidence And Reports

**Files:**
- Modify: `test/test_frontend_contract.py`
- Modify: `webapp/static/styles.css:250-321`
- Verify: `webapp/static/index.html:155-211`

- [ ] **Step 1: Write the failing bug-workspace visual contract**

Add:

```python
def test_bug_workspace_preserves_evidence_hierarchy():
    html = INDEX.read_text(encoding="utf-8")
    css = STYLES.read_text(encoding="utf-8")
    for expected in ("bug-layout", "behavior-grid", "code-evidence-surface", "report-surface"):
        assert expected in html, expected
    for expected in (
        ".behavior-panel.observed",
        "border-left: 3px solid var(--red)",
        ".behavior-panel.expected",
        "border-left: 3px solid var(--primary)",
        "background: rgba(248, 251, 255, .88)",
    ):
        assert expected in css, expected
```

Call it from `__main__`.

- [ ] **Step 2: Run the test and verify the expected panel assertion fails**

Run:

```bash
python3 test/test_frontend_contract.py
```

Expected: failure because the evidence panels do not yet use the approved translucent blue-white surface.

- [ ] **Step 3: Apply the blue evidence hierarchy**

Update only presentation selectors:

```css
.behavior-panel {
  border: 1px solid var(--line);
  background: rgba(248, 251, 255, .88);
}
.behavior-panel.observed { border-left: 3px solid var(--red); }
.behavior-panel.expected { border-left: 3px solid var(--primary); }
.code-evidence-surface pre, .terminal {
  color: #dfe8f6;
  background: #111827;
  border-color: #26344d;
}
.evidence-disclosure summary, .report-surface a { color: var(--primary); }
```

Preserve report print rules, report content, reproduction buttons, candidate states, and all existing IDs.

- [ ] **Step 4: Run the frontend contract and reproduction tests**

Run:

```bash
python3 test/test_frontend_contract.py
python3 test/test_repro_evidence.py
python3 test/test_confirmed_bugs.py
```

Expected: all three print `ok`.

- [ ] **Step 5: Commit the bug workspace update**

```bash
git add test/test_frontend_contract.py webapp/static/styles.css
git commit -m "style: refine blue bug evidence workspace"
```

### Task 5: Responsive, Print, And End-To-End Verification

**Files:**
- Modify: `test/test_frontend_contract.py`
- Modify: `webapp/static/styles.css:322-380`
- Verify: `docs/demo_script.md`

- [ ] **Step 1: Add a responsive and print contract**

Add:

```python
def test_blue_theme_keeps_responsive_and_print_boundaries():
    css = STYLES.read_text(encoding="utf-8")
    for expected in (
        "@media (max-width: 1060px)",
        "@media (max-width: 720px)",
        "@media print",
        "@media (prefers-reduced-motion: reduce)",
    ):
        assert expected in css, expected
```

Call it from `__main__`.

- [ ] **Step 2: Run the frontend contract before responsive refinement**

Run:

```bash
python3 test/test_frontend_contract.py
```

Expected: `ok`; this is a characterization test proving the existing breakpoints remain present before visual refinement.

- [ ] **Step 3: Refine responsive blue surfaces without changing breakpoints**

At `max-width: 1060px`, retain single-column overview and bug layouts. At `max-width: 720px`, retain the top navigation conversion and add:

```css
@media (max-width: 720px) {
  body { background: linear-gradient(150deg, var(--canvas-start), var(--canvas-mid)); }
  .sidebar { box-shadow: 0 8px 22px rgba(28, 46, 84, .12); }
  .metric-strip { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .metric:nth-child(2n) { border-right: 0; }
  .surface { box-shadow: 0 9px 24px rgba(47, 73, 117, .06); }
}
```

Keep `@media print` on a white background with no sidebar, gradient, or decorative shadow. Keep reduced-motion behavior disabling view animation.

- [ ] **Step 4: Run the complete automated verification suite**

Run each command and require exit code 0:

```bash
python3 test/test_demo_pipeline_behavior.py
python3 test/test_runtime_data.py
python3 test/test_demo_metrics.py
python3 test/test_candidates.py
python3 test/test_confirmed_bugs.py
python3 test/test_job_results.py
python3 test/test_repro_evidence.py
python3 test/test_frontend_contract.py
python3 test/test_data_provenance.py
node test/test_charts.js
node test/test_markdown.js
python3 -m py_compile webapp/server.py webapp/runtime_data.py webapp/candidates.py webapp/confirmed_bugs.py webapp/repro_evidence.py scripts/run_one_api_demo.py scripts/demo_metrics.py
node --check webapp/static/app.js
node --check webapp/static/charts.js
node --check webapp/static/markdown.js
git diff --check
```

Expected: test scripts print `ok`; syntax and diff checks exit silently with code 0.

- [ ] **Step 5: Perform real-page visual verification**

Start the local server:

```bash
python3 webapp/server.py --host 127.0.0.1 --port 8012
```

Verify at desktop width near 1440px and narrow width near 760px:

1. Overview shows the blue gradient, live counts, environment drawer, and no hardcoded GPU.
2. Single API selector, disabled stage tabs, empty charts, Results, candidates, and logs remain readable.
3. Bug list, expected/observed comparison, code/output panels, and report preview do not overlap.
4. Semantic success, warning, and failure colors remain distinguishable from the blue primary action.
5. Browser console has no JavaScript errors.

Stop the local server after verification.

- [ ] **Step 6: Commit responsive refinement and verification contracts**

```bash
git add test/test_frontend_contract.py webapp/static/styles.css
git commit -m "test: verify blue frontend presentation"
```

## Final Review Checklist

- [ ] `webapp/static/app.js`, backend Python, Results, and confirmed bug data have no behavior changes.
- [ ] `docs/design-previews/green-overview.html` remains available as the green reference.
- [ ] The production page contains no fixed A800, L40, CUDA, framework-version, API-count, or Bug-count values.
- [ ] The blue theme is visible by default when `webapp/server.py` starts.
- [ ] All automated tests and visual checks pass before reporting completion.
