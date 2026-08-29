# Task 01.2 - Artifact and Provenance Model / Subtask 08 - Document artifact/provenance format

## Objective

Create `docs/architecture/artifacts-and-provenance.md`.

## Implementation specification

Document:
- logical artifact vs physical blob;
- digest policy;
- provenance chain;
- deduplication;
- how later tape/snapshot/trace adapters should register outputs;
- explicit boundary: provenance is deterministic production history, not Milestone 0005 semantic
  evidence.

Add a small provenance DAG example.

## Constraints

- Keep implementation within Milestone 0001 scope.
- Prefer deterministic, typed, testable code.
- Do not add Claude, MCP, SkoolKit, emulator, tape parsing or disassembly dependencies unless this
  subtask explicitly requires them (none in Milestone 0001 do).
- Do not silently expand the project format or public API beyond what this task needs.
- Update/add tests together with production code.
- Preserve absolute-from-repo-root documentation links.

## Completion conditions

- All files/functions/configuration named above are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green once those tools exist after Task 01.0.
- Task documentation/status is updated with actual implementation evidence when completed.
