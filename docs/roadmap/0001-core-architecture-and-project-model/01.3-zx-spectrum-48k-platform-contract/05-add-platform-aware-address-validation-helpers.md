# Task 01.3 - ZX Spectrum 48K Platform Contract / Subtask 05 - Add platform-aware address validation helpers

## Objective

Create `src/zxre/platforms/validation.py`.

## Implementation specification

Implement helpers to validate:
- single addresses;
- ranges;
- containment in named memory regions.

Project-core `Address` stays generic; platform-aware validation belongs here.

Tests:
ROM/RAM boundary cases, screen ranges, `$FFFF`, out-of-range `$10000`.

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
