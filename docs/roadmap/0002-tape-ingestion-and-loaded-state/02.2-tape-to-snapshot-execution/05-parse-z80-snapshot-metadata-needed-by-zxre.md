# Task 02.2 - Tape-to-Snapshot Execution / Subtask 05 - Parse Z80 snapshot metadata needed by ZXRE

## Objective

Create:

## Implementation specification

- `src/zxre/snapshots/z80.py`
- `tests/snapshots/test_z80.py`

Implement deterministic parsing for the subset of `.z80` snapshot versions produced/accepted by the
chosen backend, sufficient to recover:
- machine/version metadata;
- PC/SP/register summary where encoded;
- RAM pages / 48K memory image;
- compression decoding where applicable.

Be explicit about supported Z80 snapshot versions.

Do not implement emulator execution.

Tests use generated/minimal fixtures and known memory patterns.

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
