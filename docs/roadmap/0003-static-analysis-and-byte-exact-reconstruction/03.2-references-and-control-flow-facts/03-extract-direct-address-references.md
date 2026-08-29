# Task 03.2 - References and Control-Flow Facts / Subtask 03 - Extract direct address references

## Objective

Create `src/zxre/analysis/references.py`.

## Implementation specification

Extract direct references from normalized instructions.

Examples:
- absolute branch/call targets;
- immediate absolute memory operands such as `LD A,(nn)` and `LD (nn),A`;
- word-address operands where decoder representation proves the address role.

Do not treat every 16-bit immediate as an address.

Tests:
address-bearing and non-address immediates, indexed displacement, port numbers not mistaken for RAM.

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
