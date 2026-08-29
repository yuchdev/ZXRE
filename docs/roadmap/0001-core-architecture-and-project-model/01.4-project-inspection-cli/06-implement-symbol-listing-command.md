# Task 01.4 - Project Inspection CLI / Subtask 06 - Implement symbol listing command

## Objective

Implement:

## Implementation specification

`zxre symbol list PROJECT [--range START:END] [--json]`

Requirements:
- list symbols in stable address/name order;
- optional range filter;
- parse hex forms consistently (`0x4000`, `$4000`, possibly bare hex only if documented).

Centralize address parsing in a helper module such as `src/zxre/cli_types.py`.

Tests:
range filtering, invalid address syntax, empty symbol set.

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
