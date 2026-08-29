# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 03 - Implement project filesystem layout

## Objective

Create `src/zxre/project/layout.py`.

## Implementation specification

Define canonical project paths such as:
- `<project>/project.json`
- `<project>/inputs/`
- `<project>/artifacts/`
- `<project>/analysis/`
- `<project>/generated/`
- `<project>/reports/`

Implement `ProjectLayout` with path accessors and `create_directories()`.

Requirements:
- layout logic must be centralized;
- no external tool creates arbitrary top-level project directories;
- paths returned are `pathlib.Path`;
- creation is idempotent;
- project path need not live inside the ZXRE source repo.

Tests in `tests/project/test_layout.py` using `tmp_path`.

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
