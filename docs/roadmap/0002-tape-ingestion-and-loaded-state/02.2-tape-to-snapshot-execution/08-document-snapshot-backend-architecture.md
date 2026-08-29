# Task 02.2 - Tape-to-Snapshot Execution / Subtask 08 - Document snapshot backend architecture

## Objective

Create `docs/architecture/snapshot-generation.md`.

## Implementation specification

Document:
- backend interface;
- initial SkoolKit adapter;
- external dependency installation expectations;
- provenance/recipe model;
- `.z80` parsing support;
- distinction between file-byte reproducibility and machine-state reproducibility;
- deferred emulator-backed loading and dynamic analysis.

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
