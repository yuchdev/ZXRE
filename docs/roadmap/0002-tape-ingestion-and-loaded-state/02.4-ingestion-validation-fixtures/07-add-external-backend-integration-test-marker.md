# Task 02.4 - Ingestion Validation Fixtures / Subtask 07 - Add external-backend integration test marker

## Objective

Create integration tests for SkoolKit-backed snapshot generation under a marker such as:

## Implementation specification

`@pytest.mark.external_tool`.

Requirements:
- skip with a clear reason when SkoolKit/tap2sna is unavailable;
- never download/install tools during tests;
- run against synthetic TAP fixture;
- verify produced snapshot parses and contains expected RAM marker bytes;
- record backend version in test diagnostics, not expected golden data unless necessary.

Configure marker in `pyproject.toml`.

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
