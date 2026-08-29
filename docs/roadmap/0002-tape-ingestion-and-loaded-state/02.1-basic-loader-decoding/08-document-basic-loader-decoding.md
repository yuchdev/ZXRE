# Task 02.1 - BASIC Loader Decoding / Subtask 08 - Document BASIC loader decoding

## Objective

Create `docs/architecture/basic-loader-decoding.md`.

## Implementation specification

Document:
- supported token/statement subset;
- restricted evaluator;
- difference between decoded fact, evaluated value and candidate address;
- examples:
  `CLEAR 32767`,
  `LOAD "" CODE 32768`,
  `RANDOMIZE USR 32768`;
- why candidate entry point is not yet a semantic conclusion;
- deferred cases: protected/custom loaders, self-modification, machine-code decompression.

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
