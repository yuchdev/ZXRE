# Task 01.2 - Artifact and Provenance Model / Subtask 04 - Persist artifact catalog

## Objective

Create `src/zxre/artifacts/catalog.py`.

## Implementation specification

Persist logical artifact descriptors and provenance records separately from blob storage, e.g.
`artifacts/catalog.json`.

Implement:
- register descriptor;
- get/list by ID;
- filter by kind;
- list producers/sources;
- reject dangling source references unless explicitly importing legacy state in a future migration.

Keep the format versioned.

Tests:
round-trip, duplicate IDs, missing sources, two logical artifacts referencing same digest.

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
