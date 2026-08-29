# Task 02.3 - Snapshot Memory Inspection and Diff / Subtask 01 - Define normalized memory image model

## Objective

Create:

## Implementation specification

- `src/zxre/memory/model.py`
- `src/zxre/memory/__init__.py`
- `tests/memory/test_model.py`

Define:
- `MemoryImage`;
- `MemorySegment`;
- `MemorySlice`;
- `MemoryDiff`;
- `MemoryDiffRun`.

Requirements:
- addresses use generic `Address`/`AddressRange`;
- immutable bytes;
- explicit platform ID;
- support contiguous 48K RAM now but avoid requiring all future platforms to be contiguous;
- no emulator concepts.

## Constraints

- Keep implementation within Milestone 0002 scope.
- All parsing, decoding, snapshot creation, exports and diffs must be deterministic and attributable
  to project artifacts/provenance.
- Do not add semantic reverse-engineering conclusions, LLM calls, agents, MCP integration or emulator
  runtime control.
- External tools such as SkoolKit must remain behind adapters and be optional outside the specific
  backend/integration tests that require them.
- Prefer typed domain objects and structured diagnostics over parsing human-readable command output
  throughout the application.
- Update/add tests together with production code.
- Preserve the Milestone 0001 project/artifact/platform boundaries rather than bypassing services.

## Completion conditions

- All files/functions/configuration named above are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green.
- External-tool tests skip cleanly when the external backend is unavailable.
- Task documentation/status is updated with actual implementation evidence when completed.
