# Task 01.3 - ZX Spectrum 48K Platform Contract / Subtask 04 - Connect project validation to platform registry

## Objective

Update:

## Implementation specification

- `src/zxre/project/service.py`
- `src/zxre/project/schema.py`
- tests

Project creation must validate `platform_id` through the registry.

Opening an existing project with an unknown platform:
- must fail with a clear unsupported-platform diagnostic,
or
- may open in an explicitly read-only/degraded mode only if that behavior is deliberately designed
  and tested.

For Milestone 0001, prefer simple explicit failure.

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
