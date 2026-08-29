# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 07 - Add project-service facade

## Objective

Create `src/zxre/project/service.py`.

## Implementation specification

Implement `ProjectService` as the application-facing facade over repository/layout/serialization
operations.

Minimum operations:
- `create_project(path, name, platform_id)`
- `open_project(path)`
- `get_project_info(project)`
- register/list inputs;
- list symbols and analysis notes.

Purpose:
CLI, future MCP and adapters must not manipulate manifest JSON directly.

Tests:
`tests/project/test_service.py` with an end-to-end create/reopen/update scenario.

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
