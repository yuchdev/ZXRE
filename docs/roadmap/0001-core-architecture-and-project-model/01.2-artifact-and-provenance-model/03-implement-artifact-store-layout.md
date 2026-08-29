# Task 01.2 - Artifact and Provenance Model / Subtask 03 - Implement artifact store layout

## Objective

Create `src/zxre/artifacts/store.py`.

## Implementation specification

Use a deterministic project-local storage layout under `artifacts/`.
Prefer digest-derived paths such as:
`artifacts/sha256/ab/cd/<full-digest>`
or another documented collision-safe structure.

Implement:
- `put_file`
- `put_bytes`
- `open`
- `path_for`
- `exists`
- `describe`

Requirements:
- same bytes deduplicate;
- logical artifacts may share physical content;
- never use user filenames as unique identity;
- validate stored bytes against descriptor digest when opening if an explicit verification mode is
  requested.

Tests: dedupe, path safety, reopen from existing project.

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
