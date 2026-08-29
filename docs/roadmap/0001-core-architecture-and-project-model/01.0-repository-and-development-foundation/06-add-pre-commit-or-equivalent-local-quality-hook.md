# Task 01.0 - Repository and Development Foundation / Subtask 06 - Add pre-commit or equivalent local quality hook

## Objective

Add lightweight local quality automation.

## Implementation specification

Preferred:
- `.pre-commit-config.yaml` using Ruff and basic whitespace/EOF checks,
or an equally simple repo-native hook if dependency policy favors avoiding pre-commit.

Document installation/usage in `CONTRIBUTING.md`.

The hook must not:
- modify generated roadmap status automatically;
- invoke networked/LLM tools;
- launch emulators;
- perform slow integration tests.

Completion:
a developer can run one documented command to execute the same fast formatting/lint checks before a
commit.

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
