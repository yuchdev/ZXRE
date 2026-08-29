# Task 03.1 - Code/Data Control Map / Subtask 04 - Import/export SkoolKit control files optionally

## Objective

Create:

## Implementation specification

- `src/zxre/adapters/skoolkit/control.py`
- `tests/adapters/skoolkit/test_control.py`

If useful, support a documented subset of SkoolKit `.ctl` import/export.

Requirements:
- conversion is through ZXRE `ControlMap`;
- unsupported directives are diagnosed/preserved where feasible;
- round-trip only promised for supported subset;
- no SkoolKit-specific directives leak into core model.

This feature remains optional.

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
