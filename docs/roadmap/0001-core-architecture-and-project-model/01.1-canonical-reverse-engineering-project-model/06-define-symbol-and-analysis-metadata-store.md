# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 06 - Define symbol and analysis metadata store

## Objective

Create:

## Implementation specification

- `src/zxre/project/analysis.py`
- `tests/project/test_analysis.py`

Implement minimal project-level APIs for:
- adding/updating/removing a `Symbol`;
- querying symbols by address/range/name;
- adding analysis notes tied to an address or range.

Important:
- symbols at this milestone are neutral labels, not evidence-backed semantic claims;
- do not implement hypotheses/confidence/evidence lifecycle from Milestone 0005;
- distinguish user-authored/imported/generated origin in lightweight metadata if needed, but do not
  invent the future evidence model.

Persist this data in a simple versioned analysis JSON file under `analysis/` unless implementation
experience strongly justifies another format.

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
