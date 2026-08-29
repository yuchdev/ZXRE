# Task 01.0 - Repository and Development Foundation / Subtask 05 - Establish documentation and roadmap conventions

## Objective

Integrate the supplied roadmap into the repo and establish documentation rules.

## Implementation specification

Required:
- retain `/docs/roadmap/README.md`;
- retain milestone folders and absolute-from-root Markdown link convention;
- create `docs/architecture/README.md`;
- create `docs/development/README.md`.

`docs/architecture/README.md`:
- state architectural principles only;
- deterministic core independent of Claude/MCP/SkoolKit/emulator;
- facts/evidence later separated from hypotheses;
- adapters isolate external tools;
- no speculative universal abstraction.

`docs/development/README.md`:
- environment setup;
- quality commands;
- repository layout;
- rule that task/subtask roadmap specs are implementation contracts and should be updated with actual
  evidence/status after completion.

If a documentation link checker is added, keep it small and deterministic; do not build a custom docs
framework in this task.

Completion:
all milestone/task links created in this story resolve.

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
