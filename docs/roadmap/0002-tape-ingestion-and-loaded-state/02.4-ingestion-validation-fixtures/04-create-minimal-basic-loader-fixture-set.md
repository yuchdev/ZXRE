# Task 02.4 - Ingestion Validation Fixtures / Subtask 04 - Create minimal BASIC loader fixture set

## Objective

Generate fixtures for representative loaders:

## Implementation specification

- BASIC-only `RANDOMIZE USR 32768`;
- `CLEAR` + `LOAD "" CODE 32768` + `RANDOMIZE USR 32768`;
- `LOAD "" SCREEN$` then CODE;
- variable-derived address (`LET a=32768 : LOAD "" CODE a : RANDOMIZE USR a`);
- unsupported/dynamic expression that must remain unknown.

Store expected decoded loader JSON under `tests/fixtures/expected/`.

Tests compare normalized output, not incidental object repr.

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
