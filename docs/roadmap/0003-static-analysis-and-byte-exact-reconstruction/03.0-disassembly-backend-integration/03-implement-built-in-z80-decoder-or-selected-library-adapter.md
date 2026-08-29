# Task 03.0 - Disassembly Backend Integration / Subtask 03 - Implement built-in Z80 decoder or selected library adapter

## Objective

Implement one production-capable Z80 decoding backend.

## Implementation specification

Preferred locations:
- `src/zxre/adapters/z80decoder/` for a library-backed decoder, or
- `src/zxre/disasm/z80_decoder.py` if the decoder is maintained in-tree.

Requirements:
- standard documented Z80 instructions;
- CB/DD/ED/FD prefixed instruction families;
- IX/IY displacement forms;
- undocumented opcodes may be preserved if backend supports them, but support level must be explicit;
- decode length and exact bytes must be correct even where aliases exist;
- invalid/truncated byte sequences produce structured diagnostics.

Do not build a full assembler here.

Tests:
- representative one-byte/multi-byte instructions;
- conditional/unconditional jumps;
- calls/returns;
- indexed instructions;
- prefixed opcodes;
- truncation at memory boundary.

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
