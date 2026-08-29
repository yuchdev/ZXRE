# Task 01.4 - Project Inspection CLI / Subtask 08 - Update user/developer documentation and milestone status

## Objective

Update:

## Implementation specification

- root `README.md`;
- `docs/development/README.md`;
- `docs/roadmap/0001-core-architecture-and-project-model/status.md` when implementation is complete.

Document exact CLI examples for creating and inspecting a project.

Status evidence must cite concrete test files and actual executed quality commands; do not mark the
milestone complete merely because files exist.

Completion:
the milestone completion criteria can be demonstrated from a fresh clone using documented commands.

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
