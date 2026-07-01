# Live Log and Candidate Minimization Design

## Goal

Keep single-API logs inside a stable panel, render terminal progress coherently, and make candidate minimization a real human-in-the-loop workflow rather than a read-only preview.

## Live Log

- The desktop live-log card has a fixed height of approximately `24rem`; its body scrolls vertically inside the card.
- At narrow breakpoints the card remains fixed but uses a smaller height so it does not dominate the page.
- Page-level horizontal overflow is forbidden.
- The backend normalizes log tails before returning them:
  - remove ANSI terminal control sequences;
  - interpret carriage returns as terminal line replacement;
  - retain only the latest progress frame instead of concatenating every `tqdm` refresh;
  - preserve ordinary newline-delimited log messages.
- Raw log files remain unchanged on disk. Normalization affects only the web response.

## Candidate Artifact Layout

Each candidate cluster may have a mutable review workspace under:

```text
demo_runs/candidates/workspaces/<cluster_id>/
  repro.py
  metadata.json
  runs/
    <run_id>/
      cpu.log
      gpu0.log
      status.json
```

The original generated source under `demo_runs/api_jobs` remains immutable. When no saved draft exists, `repro.py` is initialized from the cluster representative source.

## Candidate APIs

- `POST /api/candidate-clusters/<id>/draft`
  - validates that the submitted draft is text Python source within a size limit;
  - writes `repro.py` atomically;
  - records its hash and update time in `metadata.json`.
- `POST /api/candidate-clusters/<id>/draft/reset`
  - replaces the draft with the immutable representative source.
- `POST /api/candidate-clusters/<id>/validate`
  - saves the submitted draft first;
  - starts CPU and GPU 0 executions in separate child processes;
  - applies a fixed timeout and disables core dumps;
  - writes separate logs and a structured status record.
- `GET /api/candidate-validation-jobs/<run_id>`
  - returns running/finished state, return codes, timeout state, signals, and bounded logs.

Cluster detail responses include the persisted draft, whether it differs from the representative, the latest validation run, and whether a validation record exists.

## Candidate Review UI

- The representative source remains read-only.
- The `repro.py` panel becomes an editable monospace text area with fixed dimensions and internal scrolling.
- Controls: `保存草稿`, `恢复原始代码`, and `CPU + GPU 验证`.
- Validation runs CPU and GPU 0 by default and displays their outputs side by side beneath the editor.
- The UI explains the minimization loop: remove one unrelated statement, run validation, keep the deletion only when the target behavior still reproduces.
- Draft and validation state survive page reloads.
- `收录为确认 Bug` stays disabled until at least one validation run has completed. Final Bug judgment remains human; return codes alone do not establish a framework defect.

## Error Handling and Safety

- Draft paths are derived from server-owned cluster IDs; clients cannot provide filesystem paths.
- Cluster IDs are resolved through the candidate store before any read or write.
- Draft writes are atomic and bounded in size.
- Validation runs with `shell=False`, a fixed Python executable, controlled environment variables, timeout, and isolated output files.
- A failed or timed-out run is evidence shown to the reviewer, not an automatic Bug verdict.

## Verification

- Unit tests cover terminal-progress normalization, draft persistence/reset, path safety, and validation status parsing.
- Vue tests cover editable draft state, save/reset actions, validation polling, and fixed log layout contracts.
- Full Python and frontend test suites run before production assets are rebuilt.
- Browser verification checks fixed log height, internal scrolling, coherent progress output, and persisted candidate drafts.
