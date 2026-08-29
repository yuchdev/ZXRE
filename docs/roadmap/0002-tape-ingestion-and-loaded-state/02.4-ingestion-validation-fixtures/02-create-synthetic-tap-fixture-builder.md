# Task 02.4 - Ingestion Validation Fixtures / Subtask 02 - Create synthetic TAP fixture builder

## Objective

Create `tests/fixture_builders/tap_builder.py`.

## Implementation specification

Provide deterministic helpers to construct:
- standard PROGRAM header block;
- CODE header block;
- data block;
- custom/unknown flag block;
- corrupt parity/checksum block;
- truncated variants.

Use builders in unit tests instead of hand-maintaining opaque base64 blobs.

Add builder unit tests if logic is nontrivial.

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
