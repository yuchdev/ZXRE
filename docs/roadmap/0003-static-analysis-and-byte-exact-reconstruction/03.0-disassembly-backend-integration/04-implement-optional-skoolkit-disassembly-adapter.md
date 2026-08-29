# Task 03.0 - Disassembly Backend Integration / Subtask 04 - Implement optional SkoolKit disassembly adapter

## Objective

Create:

## Implementation specification

- `src/zxre/adapters/skoolkit/disasm.py`
- `tests/adapters/skoolkit/test_disasm.py`

If SkoolKit exposes a useful programmatic/CLI disassembly surface, wrap it as an optional secondary
backend.

Requirements:
- isolate command construction/parsing inside adapter;
- normalize to ZXRE `Instruction`;
- preserve exact bytes independently from SkoolKit textual formatting;
- detect installed SkoolKit/version;
- skip integration tests when unavailable.

Purpose:
- provide an independent decoder/backend for comparison and future specialized SkoolKit workflows,
  not make static analysis depend on SkoolKit.

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
