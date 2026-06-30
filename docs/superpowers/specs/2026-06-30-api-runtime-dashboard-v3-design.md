# API Runtime Dashboard V3 Design

## Scope

Only the content below the five-stage pipeline changes. The page header, API selector, run controls, and pipeline remain intact.

## Layout

The runtime dashboard uses two columns. The left column is slightly wider and contains the stage chart followed by a compact three-card strip: GPU monitor, live summary, and Results composition. The right column is a full-height live log. At narrower widths the columns stack without horizontal overflow.

## Chart semantics

All stage charts use Chinese axis captions: `阶段运行时间（秒）` on X and `累计数量` on Y. Axis lines and labels are visually restrained and tooltips use Chinese time labels.

The driver chart no longer plots the constant generated-file total as completed work. `tested_cases` is counted incrementally from valid `TitanFuzzTestcase` records in `trace.txt`; the chart displays `已检测程序` and `差异 Catch`. `total_files` remains available as the target total for summary text.

## Log behavior

The live log remains stage-specific and reads the real files `01_qwen_seed.log`, `02_ev_generation.log`, and `03_driver.log`. The larger right panel keeps auto-follow and manual scrolling.

## Run retention

Every new run starts in a unique directory so an in-progress job cannot corrupt the previous result. The frontend immediately follows the new job. Once the new job reaches a terminal state and candidate collection finishes, older terminal jobs for the same library and API are pruned unless their job ID is referenced by the candidate index. Confirmed bug evidence is outside the API-job directory and is never pruned. The frontend continues to show only the newest job.

## Verification

Tests cover incremental driver progress, stage-series semantics, dashboard placement, log-file mapping, search selection, job switching, and retention protection. The production build and rendered page are verified after implementation.
