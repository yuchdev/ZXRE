# Task 02.0 - Tape Inspection and Block Inventory / Subtask 05 - Implement tape inventory service

## Objective

Create:

## Implementation specification

- `src/zxre/tape/service.py`
- `tests/tape/test_service.py`

Implement `TapeService` over the project/artifact layer.

Responsibilities:
- accept an existing project input artifact;
- detect TAP vs TZX by declared type and/or validated signature/structure;
- parse the tape;
- register normalized tape inventory metadata under project analysis/generated metadata;
- preserve source artifact provenance;
- return structured `TapeImage`.

Do not copy raw blocks into separate artifacts yet unless explicitly requested by extraction APIs.

Define clear errors:
- unsupported format;
- parse failure;
- source artifact missing;
- inconsistent declared/detected format.

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
