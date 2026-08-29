# Task 01.4 - Project Inspection CLI / Subtask 05 - Implement platform show command

## Objective

Implement:

## Implementation specification

`zxre platform show zx-spectrum-48k [--json]`

Human output:
- platform name/ID;
- CPU architecture ID;
- address width;
- named memory regions and hex ranges;
- display/screen regions.

The command reads the platform registry; do not duplicate constants in CLI code.

Tests verify expected region names and JSON schema shape.

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
