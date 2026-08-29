# Task 03.3 - Lossless Assembler Source Generation / Subtask 04 - Render CODE regions

## Objective

Create `src/zxre/reconstruct/code.py`.

## Implementation specification

Render structured instructions from CODE regions.

Requirements:
- labels substituted only where operand role/target is known;
- retain comment/address metadata useful for verification;
- unsupported/ambiguous instruction encoding may fall back to byte directives if textual assembly
  cannot guarantee original bytes;
- exact original bytes remain associated in reconstruction model.

Tests:
branches, calls, undocumented/alias fallback where applicable.

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
