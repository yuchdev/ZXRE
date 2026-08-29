# Task 01.0 - Repository and Development Foundation / Subtask 07 - Bootstrap verification and handoff

## Objective

Perform and document the final clean-clone verification for the scaffold.

## Implementation specification

Update:
- `README.md` quick start;
- `CONTRIBUTING.md`;
- milestone `status.md` evidence once the task is actually implemented.

Verify:
- `uv sync`;
- CLI help;
- tests;
- lint;
- formatting check;
- MyPy;
- CI workflow paths;
- roadmap links.

Do not implement any domain model in this subtask.

Completion:
the repository is ready for Task 01.1 to start without additional structural setup.

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
