# Task 02.2 - Tape-to-Snapshot Execution / Subtask 02 - Define loader/snapshot backend interface

## Objective

Create:

## Implementation specification

- `src/zxre/snapshots/backend.py`
- `tests/snapshots/test_backend_contract.py`

Define a protocol/ABC such as `TapeSnapshotBackend` with:
- backend ID;
- capability/format reporting;
- `create_snapshot(request) -> SnapshotDescriptor`.

Define `SnapshotRequest` including:
- project/tape source;
- platform ID;
- desired output format;
- optional deterministic backend parameters.

Requirements:
- external process invocation is hidden behind backend;
- stdout/stderr/exit status can be captured as provenance/diagnostics;
- no shell=True;
- command construction must be testable separately.

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
