# Task 03.0 - Disassembly Backend Integration / Subtask 01 - Define disassembly domain model

## Objective

Create:

## Implementation specification

- `src/zxre/disasm/model.py`
- `src/zxre/disasm/__init__.py`
- `tests/disasm/test_model.py`

Define at minimum:
- `InstructionId`;
- `Instruction`;
- `DecodedOperand`;
- `OperandKind`;
- `InstructionBytes`;
- `DecodeDiagnostic`;
- `DisassemblyRegion`;
- `DisassemblyResult`.

Instruction fields:
- platform/architecture ID;
- start address;
- byte length;
- exact original bytes;
- mnemonic;
- normalized operands;
- textual canonical rendering;
- control-flow classification metadata only where deterministically derivable;
- backend ID/version.

Requirements:
- no semantic routine/function names;
- exact bytes must always be retained;
- failed/partial decode is representable without corrupting following address state.

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
