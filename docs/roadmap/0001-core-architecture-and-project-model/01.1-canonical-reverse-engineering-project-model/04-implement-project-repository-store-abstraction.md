# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 04 - Implement project repository/store abstraction

## Objective

Create:

## Implementation specification

- `src/zxre/project/repository.py`
- `src/zxre/project/errors.py`
- `tests/project/test_repository.py`

Implement a filesystem-backed `ProjectRepository` responsible for:
- creating a project;
- opening an existing project;
- loading/saving manifest metadata;
- validating required layout;
- rejecting accidental overwrite unless explicitly allowed by a future API.

Provide clear exceptions:
- `ProjectNotFoundError`
- `ProjectAlreadyExistsError`
- `InvalidProjectError`
- `UnsupportedProjectVersionError`

Do not add SQLite yet unless concrete access patterns in this task require it; the canonical store
should begin with the simplest durable format.

Tests must use temporary directories and verify failure behavior.

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
