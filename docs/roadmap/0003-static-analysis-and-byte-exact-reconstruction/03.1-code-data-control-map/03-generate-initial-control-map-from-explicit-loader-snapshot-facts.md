# Task 03.1 - Code/Data Control Map / Subtask 03 - Generate initial control map from explicit loader/snapshot facts

## Objective

Create `src/zxre/control/generate.py`.

## Implementation specification

Generate a **conservative** initial map using only deterministic inputs already available:
- explicit CODE tape block destination addresses from standard headers/load operations;
- known exported memory ranges;
- optional user-specified entry ranges.

Rules:
- do not automatically classify an entire loaded CODE block as executable if evidence only proves it
  was loaded there; prefer `BYTES` or `UNKNOWN` unless a deterministic policy is intentionally
  defined;
- explicit user request may mark code;
- preserve provenance/origin for every generated region.

Tests ensure candidate USR address alone does not magically classify arbitrary surrounding bytes.

## Constraints

- Keep implementation within Milestone 0003 scope.
- Preserve exact original bytes and address ranges whenever transforming code/data into structured
  form or generated source.
- Do not add semantic routine names, gameplay interpretation, runtime execution experiments, LLM
  calls, agents or MCP behavior.
- External tools must stay behind adapters with version/provenance capture and clean skip behavior
  when unavailable.
- Canonical project state is structured ZXRE data; third-party textual listings/reports are not the
  source of truth.
- Prefer conservative classification and explicit `UNKNOWN`/diagnostics over guessing.
- Update/add tests together with production code.

## Completion conditions

- All named files/functions/configuration are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green.
- External-tool tests skip cleanly when required binaries are unavailable.
- For reconstruction-related subtasks, byte fidelity is demonstrated by tests or explicit diagnostic
  behavior rather than visual inspection.
