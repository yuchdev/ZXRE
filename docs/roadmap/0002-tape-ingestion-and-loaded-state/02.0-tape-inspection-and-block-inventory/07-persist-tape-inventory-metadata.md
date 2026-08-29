# Task 02.0 - Tape Inspection and Block Inventory / Subtask 07 - Persist tape inventory metadata

## Objective

Create a versioned serialized representation, for example:

## Implementation specification

- `src/zxre/tape/serialization.py`
- project file `analysis/tape-inventory.json`
- `tests/tape/test_serialization.py`

Requirements:
- persist block order and stable IDs;
- include source artifact identity;
- include normalized headers and diagnostics;
- avoid embedding large raw payloads in JSON when artifact/source slices already identify them;
- deterministic round-trip;
- version field and explicit unsupported-version error.

Integrate with `TapeService` so reopening a project can load the inventory without reparsing unless the
source artifact changed.

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
