# Task 02.0 - Tape Inspection and Block Inventory / Subtask 04 - Normalize standard Spectrum header blocks

## Objective

Create `src/zxre/tape/spectrum_header.py`.

## Implementation specification

Decode standard 17-byte Spectrum tape headers into a typed representation.

Fields:
- file type (`PROGRAM`, `NUMERIC_ARRAY`, `CHARACTER_ARRAY`, `CODE`, unknown);
- 10-character Spectrum filename preserving raw bytes and normalized display text;
- data length;
- parameter 1;
- parameter 2;
- CODE start address where applicable;
- BASIC autostart line / variable area semantics where applicable.

Requirements:
- keep raw header bytes;
- do not infer semantics beyond the documented header format;
- unknown file-type values remain representable.

Tests:
- BASIC PROGRAM header;
- CODE header;
- array header;
- padded filenames;
- malformed header length.

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
