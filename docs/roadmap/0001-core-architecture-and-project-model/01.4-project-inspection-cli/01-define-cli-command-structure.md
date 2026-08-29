# Task 01.4 - Project Inspection CLI / Subtask 01 - Define CLI command structure

## Objective

Refactor `src/zxre/cli.py` and, if needed, add `src/zxre/commands/`.

## Implementation specification

Required command tree:
- `zxre project create`
- `zxre project info`
- `zxre input add`
- `zxre input list`
- `zxre artifact list`
- `zxre artifact verify`
- `zxre symbol list`
- `zxre platform show`

Use stable exit codes and centralized error rendering.
No color requirement; outputs must remain usable in non-interactive agent shells.

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
