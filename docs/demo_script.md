# TitanFuzz-main Competition Demo Script

## Positioning

This project is not a real-time full-framework scanner. It is an LLM-assisted fuzzing and bug-triage workbench for deep-learning frameworks.

The live demo runs one API end-to-end. Historical high-signal bug candidates are shown through the evidence repository.

## One-Sentence Pitch

We use an offline DeepSeek-distilled API constraint library to guide Qwen seed generation, repair and validate executable seeds, mutate them with InCoder-6B, and finally use TitanFuzz's CPU/GPU differential oracle to discover framework bug candidates.

## Demo Flow

1. Open Dashboard.
   - Show prompt-library coverage.
   - Show candidate bug count.
   - Emphasize that raw trace catches are not directly counted as confirmed bugs.

2. Open Prompt Library.
   - Select `torch.nn.functional.conv1d`.
   - Show `structured_info.txt`.
   - Explain that DeepSeek is used offline to convert API documentation into structured constraints.
   - Explain that runtime does not call DeepSeek.

3. Open Single API Demo.
   - Select:

```text
Library: torch
API: torch.nn.functional.conv1d
Mode: demo
Mutation model: facebook/incoder-6B
```

   - Start the run.
   - Explain the pipeline:

```text
prompt library check
→ Qwen seed generation
→ seed repair and validation
→ InCoder-6B mutation
→ CPU/GPU oracle
→ trace report
```

4. Open Bug Repository.
   - Show curated candidates, not raw catches.
   - Open `PT-N1-002`.
   - Explain why `fractional_max_pool3d` is the strongest current candidate:

```text
C=65535: CPU success, CUDA success
C=65536: CPU success, CUDA invalid argument
```

5. Export report.
   - Show markdown issue-style report.
   - Explain that upstream confirmation is still required before calling a candidate an official PyTorch bug.

## Phrases to Use

Use:

```text
strong bug candidate
CPU/GPU differential oracle
offline prompt/constraint library
single-API end-to-end demo
minimum reproduction evidence
```

Avoid:

```text
real-time full-framework bug scanner
one-click confirmed bug
we found tens of thousands of bugs
DeepSeek is called every time
```

## Backup CLI Demo

If the web page has issues, run the CLI directly:

```bash
bash scripts/run_one_api_demo.sh \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d_demo \
  --mode demo
```

For a quick no-model smoke test:

```bash
bash scripts/run_one_api_demo.sh \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d_demo_dry \
  --mode demo \
  --dry_run \
  --force_redo
```
