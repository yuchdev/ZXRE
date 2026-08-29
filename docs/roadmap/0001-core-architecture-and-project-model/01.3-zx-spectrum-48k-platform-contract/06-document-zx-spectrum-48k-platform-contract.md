# Task 01.3 - ZX Spectrum 48K Platform Contract / Subtask 06 - Document ZX Spectrum 48K platform contract

## Objective

Create `docs/architecture/platforms.md`.

## Implementation specification

Document:
- generic descriptor responsibilities;
- intentionally excluded responsibilities;
- ZX Spectrum 48K implementation;
- why ZEsarUX, SkoolKit and MCP do not belong in this layer;
- how future second-platform work is expected to extend the registry without changing project model
  semantics.

Completion:
the rest of Milestone 0001 can refer to the platform by stable ID and query its memory map without
hard-coded Spectrum constants.

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
