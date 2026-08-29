# Task 01.3 - ZX Spectrum 48K Platform Contract / Subtask 01 - Define platform descriptor interfaces

## Objective

Create:

## Implementation specification

- `src/zxre/platforms/model.py`
- `src/zxre/platforms/registry.py`
- `tests/platforms/test_registry.py`

Minimum concepts:
- `PlatformId`
- `PlatformDescriptor`
- `MemoryRegion`
- `MemoryRegionKind`
- display/screen region descriptor sufficient for later rendering;
- CPU architecture identifier as metadata only.

Platform descriptor must expose:
- address width;
- valid address bounds;
- named memory regions;
- optional display-related regions;
- human-readable metadata.

Do not define emulator APIs, instruction decoder APIs or snapshot formats here.

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
