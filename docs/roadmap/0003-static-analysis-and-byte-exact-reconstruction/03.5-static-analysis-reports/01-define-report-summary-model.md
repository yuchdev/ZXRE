# Task 03.5 - Static Analysis Reports / Subtask 01 - Define report summary model

## Objective

Create:

## Implementation specification

- `src/zxre/reports/static_model.py`
- `tests/reports/test_static_model.py`

Define deterministic summary structures:
- address-space coverage by control kind;
- instruction count;
- decode diagnostics count;
- direct reference counts;
- basic block/routine candidate counts;
- unresolved indirect flow count;
- reconstruction verification status;
- unresolved/gap ranges.

No semantic labels beyond existing user/mechanical symbols.

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
