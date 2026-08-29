# Task 03.3 - Lossless Assembler Source Generation / Subtask 03 - Generate deterministic labels for direct targets

## Objective

Create `src/zxre/reconstruct/labels.py`.

## Implementation specification

Generate mechanical labels such as:
- `L8000`;
- `L83AF`;
- `DATA_A200` only if kind-specific prefix is deterministic.

Requirements:
- every direct branch/call target inside reconstructed address space gets stable label where useful;
- labels derive only from address/classification;
- user symbols from Milestone 0001 may override display names if explicitly configured;
- semantic names are not invented.

Tests:
stable naming, collision avoidance, external target handling.

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
