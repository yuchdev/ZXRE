# Task 01.2 - Artifact and Provenance Model / Subtask 07 - Add artifact integrity verification

## Objective

Create `src/zxre/artifacts/verify.py`.

## Implementation specification

Implement project-level verification:
- every catalog entry resolves;
- stored blob exists;
- optional full digest recheck;
- provenance source references resolve.

Return structured diagnostics, not only printed strings.

Tests include deliberate missing/corrupted blobs in temporary projects.

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
