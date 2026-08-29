# Task 02.2 - Tape-to-Snapshot Execution / Subtask 06 - Validate created snapshot against platform

## Objective

Create `src/zxre/snapshots/validation.py`.

## Implementation specification

Validate:
- snapshot parses successfully;
- declared machine is compatible with project platform;
- expected 48K address-space RAM can be materialized;
- artifact digest exists;
- source/provenance links resolve.

Return structured diagnostics.

Tests:
valid 48K snapshot, wrong/unsupported machine metadata, corrupt compressed page.

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
