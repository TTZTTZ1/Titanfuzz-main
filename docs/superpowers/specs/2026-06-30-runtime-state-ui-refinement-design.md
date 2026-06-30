# Runtime State UI Refinement Design

## Goal

Make the single-API and bug-replay pages accurately preserve backend state while matching the approved product mockups.

## Single-API behavior

- Completed pipeline stages remain green; the current stage remains blue; failures remain red.
- Qwen, InCoder, and Driver chart tabs are selectable while running or after completion. Pending stages remain disabled.
- Runtime is the cumulative wall-clock duration of the API job. It updates once per second while active and freezes at the terminal status timestamp.
- Candidate collection is shown as an explicit control-row state: pending, collected with cluster count, no high-signal candidate, or failed.
- Results composition uses the approved colored distribution bar and stronger two-column counts.
- GPU monitoring uses latest utilization and memory gauges instead of a second time-series chart.

## Bug-replay behavior

- Selecting a confirmed bug loads that bug's latest reproduction job from persistent backend storage, not a globally limited overview list.
- A newer run becomes the displayed run; older job directories and reports remain immutable history.
- Current environment inventory is loaded independently and remains visible before reproduction.
- Idle, running, reproduced, and review states use distinct, high-contrast treatments.
- Expected and observed evidence remain the basis of the verdict presentation.

## Data flow

The API job status exposes candidate collection counts already written by the pipeline. The frontend derives cluster count from candidate clusters for the selected API. The confirmed-bug detail endpoint includes the latest reproduction job id for that bug. Environment inventory comes from `/api/environment`.

## Verification

Use test-first changes for stage selection, elapsed-time derivation, candidate state, latest reproduction lookup, and persistent environment display. Run Python contract tests, all Vitest tests, the production build, and browser QA at desktop and compact widths.
