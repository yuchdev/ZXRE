# Task 01.4 - Project Inspection CLI / Subtask 07 - Add end-to-end CLI integration test

## Objective

Create `tests/integration/test_milestone_0001_cli.py`.

## Implementation specification

Scenario:
1. create temporary ZX Spectrum 48K project;
2. add a small binary input;
3. reopen project;
4. inspect info/platform;
5. list artifacts;
6. list symbols;
7. verify artifact integrity;
8. assert project can still be reopened.

Use only local generated fixture bytes; no copyrighted ROM/game fixture and no network.

This test is the Milestone 0001 functional acceptance test.

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
