# Task 01.0 - Repository and Development Foundation / Subtask 02 - Configure Ruff, MyPy and Pytest

## Objective

Add static-analysis and test configuration to `pyproject.toml`.

## Implementation specification

Required:
- Ruff lint + format.
- MyPy strict-enough baseline suitable for a typed core library.
- Pytest configuration.
- Development dependency groups for test/type/lint tooling.

Add:
- `tests/test_quality_config.py` only if useful to assert import/config invariants; do not test tool
  internals merely for coverage.

Recommended Ruff selections:
`E`, `F`, `I`, `N`, `UP`, `B`, `SIM`, `RUF`, with narrow documented ignores only where necessary.

MyPy:
- type-check `src/zxre`;
- disallow untyped definitions in production modules;
- no blanket `ignore_missing_imports = true` unless a specific third-party adapter later requires it.

Define documented developer commands:
- `uv run ruff check .`
- `uv run ruff format --check .`
- `uv run mypy src`
- `uv run pytest`

Completion:
all four commands pass on the scaffold.

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
