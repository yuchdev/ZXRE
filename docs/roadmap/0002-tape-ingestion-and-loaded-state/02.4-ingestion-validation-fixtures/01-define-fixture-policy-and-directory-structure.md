# Task 02.4 - Ingestion Validation Fixtures / Subtask 01 - Define fixture policy and directory structure

## Objective

Create:

## Implementation specification

- `tests/fixtures/README.md`
- `tests/fixtures/tape/`
- `tests/fixtures/snapshots/`
- `tests/fixtures/expected/`

Document:
- all fixtures must be generated in-repo, public-domain/permissively licensed, or tiny synthetic
  binary structures not copyright-significant;
- no ZX Spectrum ROM;
- no commercial game TAP/TZX;
- expected-output files are reviewed deterministic test data.

Define naming convention and provenance/license notes for each non-generated fixture.

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
