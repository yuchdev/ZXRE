# Task 03.4 - Byte-Exact Verification / Subtask 04 - Implement binary-to-memory mapping for rebuilt output

## Objective

Create `src/zxre/verify/mapping.py`.

## Implementation specification

Map assembler output bytes back to expected origin/ranges using reconstruction manifest and assembler
map metadata where available.

Requirements:
- handle one or multiple source units;
- detect missing/extra ranges;
- do not assume binary always starts at `$0000`;
- surface gaps/overlap.

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
