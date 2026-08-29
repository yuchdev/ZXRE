# Task 03.0 - Disassembly Backend Integration / Subtask 07 - Add backend equivalence regression tests

## Objective

Create `tests/integration/test_disassembly_backend_equivalence.py`.

## Implementation specification

When two backends are available:
- decode selected generated Z80 byte fixtures;
- compare start address, length and exact bytes;
- compare normalized mnemonic/operand semantics where representation allows;
- report differences clearly rather than forcing false equivalence for aliases/undocumented opcode
  spelling.

Mark external-tool portions appropriately.

This is a diagnostic/quality test, not a requirement that textual renderings match byte-for-byte.

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
