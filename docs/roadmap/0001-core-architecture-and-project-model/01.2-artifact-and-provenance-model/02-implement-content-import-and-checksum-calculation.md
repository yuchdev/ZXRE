# Task 01.2 - Artifact and Provenance Model / Subtask 02 - Implement content import and checksum calculation

## Objective

Create `src/zxre/artifacts/importer.py`.

## Implementation specification

Implement:
- streaming SHA-256;
- import from an existing file;
- import from bytes for small generated artifacts;
- metadata capture: size, original name if any, media type if known.

Use temp files + atomic rename where writing project-managed artifacts.

Tests in `tests/artifacts/test_importer.py`:
- known digest;
- duplicate contents;
- large-ish streamed fixture;
- interrupted/failed write leaves no corrupt committed artifact.

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
