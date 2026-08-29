# Task 01.4 - Project Inspection CLI / Subtask 02 - Implement project create/info commands

## Objective

Implement:

## Implementation specification

`zxre project create PATH --name NAME --platform zx-spectrum-48k`
`zxre project info PATH`

Output includes:
- project ID;
- name;
- format version;
- platform ID;
- counts of inputs/artifacts/symbols.

Support human-readable default output and a machine-readable `--json` form.

Tests:
`tests/cli/test_project_commands.py` using direct CLI invocation API/subprocess as appropriate.

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
