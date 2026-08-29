# Task 02.2 - Tape-to-Snapshot Execution / Subtask 01 - Define snapshot domain model

## Objective

Create:

## Implementation specification

- `src/zxre/snapshots/model.py`
- `src/zxre/snapshots/__init__.py`
- `tests/snapshots/test_model.py`

Define:
- `SnapshotId`;
- `SnapshotFormat`;
- `SnapshotDescriptor`;
- `SnapshotProducerInfo`;
- `MachineStateSummary`;
- optional `CpuStateSummary` with only fields available deterministically from parsed snapshot format.

Descriptor fields:
- artifact ID;
- platform ID;
- snapshot format;
- source tape artifact/inventory reference;
- producer backend ID/version;
- normalized operation parameters.

Do not couple snapshot model to SkoolKit-specific classes.

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
