# Task 03.0 - Disassembly Backend Integration / Subtask 02 - Define disassembler backend contract

## Objective

Create:

## Implementation specification

- `src/zxre/disasm/backend.py`
- `tests/disasm/test_backend_contract.py`

Define a protocol/ABC such as `DisassemblerBackend` with:
- `backend_id`;
- `architecture_id`;
- capability metadata;
- `decode_one(memory, address)`;
- `decode_range(memory, address_range, options)`.

Define `DisassemblyOptions`:
- stop-on-error vs preserve-as-data/unknown;
- maximum instruction count;
- optional canonical numeric style if rendering needs it.

The contract returns structured instructions, never requires consumers to parse human text.

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
