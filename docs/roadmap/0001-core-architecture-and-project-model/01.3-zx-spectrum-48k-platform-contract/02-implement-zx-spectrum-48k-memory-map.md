# Task 01.3 - ZX Spectrum 48K Platform Contract / Subtask 02 - Implement ZX Spectrum 48K memory map

## Objective

Create:

## Implementation specification

- `src/zxre/platforms/zx_spectrum_48k.py`
- `tests/platforms/test_zx_spectrum_48k.py`

Define at minimum:
- 16-bit address space `$0000-$FFFF`;
- ROM `$0000-$3FFF`;
- RAM `$4000-$FFFF`;
- screen bitmap `$4000-$57FF`;
- attributes `$5800-$5AFF`;
- system-variable area metadata where useful, but avoid claiming exact semantic ranges not required
  by current contracts.

Use half-open ranges internally and render inclusive hex boundaries in human-facing descriptions.

Register the platform under a stable ID such as `zx-spectrum-48k`.

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
