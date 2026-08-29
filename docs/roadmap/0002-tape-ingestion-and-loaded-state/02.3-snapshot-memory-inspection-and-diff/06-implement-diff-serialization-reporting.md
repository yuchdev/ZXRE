# Task 02.3 - Snapshot Memory Inspection and Diff / Subtask 06 - Implement diff serialization/reporting

## Objective

Create:

## Implementation specification

- `src/zxre/memory/serialization.py`
- `src/zxre/memory/report.py`
- tests

Provide:
- JSON-serializable structured diff;
- concise human-readable report with hex addresses;
- optional exported diff artifact for large analyses.

Do not introduce HTML/report framework yet.

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
