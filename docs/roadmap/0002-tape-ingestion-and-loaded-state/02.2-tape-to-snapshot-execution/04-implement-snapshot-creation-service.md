# Task 02.2 - Tape-to-Snapshot Execution / Subtask 04 - Implement snapshot creation service

## Objective

Create `src/zxre/snapshots/service.py`.

## Implementation specification

Responsibilities:
- choose a configured backend;
- validate platform/backend compatibility;
- invoke snapshot creation;
- register artifact/provenance;
- persist descriptor under project analysis metadata;
- return structured diagnostics.

Default backend may be `skoolkit-tap2sna` when installed, but no core module outside adapter/service
selection should import SkoolKit-specific code.

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
