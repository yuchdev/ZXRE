# Task 01.2 - Artifact and Provenance Model / Subtask 05 - Define producer/provenance semantics

## Objective

Create `src/zxre/artifacts/provenance.py`.

## Implementation specification

Standardize producer metadata:
- ZXRE component name;
- operation name;
- component/tool version when available;
- normalized parameters;
- source artifact IDs;
- creation timestamp.

Do not capture nondeterministic environment dumps by default.

Implement a helper/context object that later adapters can use to record an operation result without
knowing catalog serialization details.

Tests ensure parameter serialization is deterministic for supported scalar/list/map types.

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
