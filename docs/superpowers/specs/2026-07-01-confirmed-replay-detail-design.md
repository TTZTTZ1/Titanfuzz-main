# Confirmed Replay Detail Redesign

## Goal

Improve the confirmed-bug detail view for presentation use while preserving all existing reproduction, environment collection, report caching, and backend data behavior.

## Scope

Only the confirmed-bug branch of `BugReplayView.vue` changes. Candidate review, API execution, backend endpoints, persisted report semantics, and confirmed-bug data formats remain unchanged.

## Layout

### Status header

- Keep the existing title, API, and verdict content.
- Render status badges as visually distinct semantic states rather than identical green tags.
- `confirmed` uses green, `needs review` uses amber, and `minimized` uses blue.
- Badges retain compact dimensions and remain readable at browser zoom levels used for judging.

### Evidence workbench

- Replace the shared two-column code grid with two sibling panels.
- The left panel is `repro.py`; the right panel is the latest current-environment output.
- Both panels have the same fixed height and independent vertical and horizontal scrolling.
- Long source lines or runtime logs must never increase page width or panel height.
- Empty output keeps the existing waiting message inside the output panel.

### Action and environment row

Place three independent panels on one desktop row in this order:

1. Current environment
2. Execution configuration
3. Evidence report

Use content-weighted columns rather than equal thirds. The environment panel receives enough width for a compact two-column key/value grid, execution configuration receives enough width for CPU/GPU choices and the run button, and the report panel receives enough width for report status and report actions.

At narrow widths the panels collapse without changing their order. The current environment remains visible before reproduction and continues to use live backend values.

## Component Behavior

- Device selection and the reproduction button keep their current handlers.
- Report generation remains one-time and existing reports are read without overwrite.
- Environment values continue to come from `getEnvironment()` or the latest reproduction job fallback.
- No status, environment, result, or report content is hard-coded.

## Responsive Behavior

- Desktop: three action panels in one row.
- Medium width: environment spans the available width when necessary; execution and report remain usable without clipped controls.
- Mobile: panels stack in the order environment, execution, report.
- Evidence source and output panels stack on mobile while preserving fixed internal scroll areas.

## Verification

- Add component assertions for the two independent evidence panels, three-panel action row, environment-first ordering, and semantic status classes.
- Verify the new assertions fail before implementation.
- Run the focused `BugReplayView` test, all frontend tests, and the production build.
- Inspect the confirmed-bug page in the in-app browser at desktop and narrow widths for overflow, clipping, state readability, and control behavior.

