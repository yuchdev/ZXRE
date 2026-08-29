# Task 03.2 - References and Control-Flow Facts / Subtask 04 - Build conservative basic blocks

## Objective

Create `src/zxre/analysis/blocks.py`.

## Implementation specification

Algorithm:
- entry candidates from explicitly classified CODE region starts and direct branch targets;
- terminate at unconditional control transfer, return, or before known target boundary;
- conditional branch creates target + fallthrough;
- unresolved indirect jump terminates block;
- never cross control-map region boundaries.

Output deterministic `BasicBlock` records.

Tests:
linear code, conditional branch, loops, call fallthrough, indirect jump.

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
