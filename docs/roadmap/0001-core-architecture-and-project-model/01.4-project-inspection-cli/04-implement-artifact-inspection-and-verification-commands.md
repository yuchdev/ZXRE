# Task 01.4 - Project Inspection CLI / Subtask 04 - Implement artifact inspection and verification commands

## Objective

Implement:

## Implementation specification

`zxre artifact list PROJECT [--kind KIND] [--json]`
`zxre artifact verify PROJECT [--full] [--json]`

`--full` triggers digest recomputation; default may validate catalog/path references only.

Exit non-zero when integrity verification finds corruption/missing content.
Machine-readable output must include structured diagnostics.

Tests deliberately corrupt a temp-project blob.

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
