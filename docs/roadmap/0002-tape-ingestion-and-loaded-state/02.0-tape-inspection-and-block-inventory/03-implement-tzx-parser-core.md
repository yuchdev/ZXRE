# Task 02.0 - Tape Inspection and Block Inventory / Subtask 03 - Implement TZX parser core

## Objective

Create:

## Implementation specification

- `src/zxre/tape/tzx.py`
- `src/zxre/tape/tzx_blocks.py`
- `tests/tape/test_tzx.py`

Implement enough TZX parsing to support deterministic inventory of common Spectrum game images.

Required initial block support:
- TZX header/signature/version;
- standard speed data block `0x10`;
- turbo speed data block `0x11`;
- pure tone `0x12`;
- pulse sequence `0x13`;
- pure data `0x14`;
- direct recording `0x15`;
- pause/stop `0x20`;
- group start/end `0x21`/`0x22`;
- text description `0x30`;
- archive info `0x32`;
- hardware type `0x33`;
- custom info `0x35`.

For unsupported block IDs:
- fail with a structured `UnsupportedTapeBlockError` only when length cannot be safely skipped;
- otherwise preserve block metadata and raw payload as an opaque/unknown block.

Parsing must be table/handler driven rather than a single unmaintainable switch body.

Tests:
- minimal valid TZX;
- multiple supported block types;
- malformed signature/version;
- truncated variable-length blocks;
- unknown/skippable block preservation.

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
