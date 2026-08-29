# Task 02.0 - Tape Inspection and Block Inventory / Subtask 02 - Implement TAP parser

## Objective

Create:

## Implementation specification

- `src/zxre/tape/tap.py`
- `tests/tape/test_tap.py`

Implement a deterministic parser for standard ZX Spectrum TAP files.

Requirements:
- parse little-endian 16-bit block lengths;
- preserve exact block payload bytes;
- expose flag byte and trailing parity/checksum byte where present;
- detect standard header blocks (`flag == 0x00`, expected header payload structure);
- distinguish data blocks (`flag == 0xFF`) from unknown/nonstandard flags;
- validate truncation and impossible lengths;
- do not assume every header is followed by a matching data block;
- preserve unknown blocks rather than rejecting valid-but-unrecognized content.

Implement pure parsing APIs such as:
- `parse_tap(data: bytes, source_artifact_id: ArtifactId) -> TapeImage`
- optionally a streaming/file variant if useful, but keep one canonical implementation.

Tests must cover:
- one header + data pair;
- multiple pairs;
- data-only TAP;
- empty TAP;
- truncated length prefix;
- truncated payload;
- unknown flag;
- checksum/parity mismatch diagnostics.

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
