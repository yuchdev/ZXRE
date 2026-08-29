# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 05 - Model project inputs without parsing them

## Objective

Create `src/zxre/project/inputs.py`.

## Implementation specification

Implement operations to register an input descriptor in project state without interpreting TAP/TZX
contents.

Support metadata:
- logical ID;
- original filename;
- media type / declared kind;
- size;
- optional checksum reference placeholder compatible with Task 01.2;
- imported timestamp;
- optional user description.

Do not:
- parse tape headers;
- identify machine code;
- copy files into content-addressed artifact storage yet unless Task 01.2 has already landed.

Tests:
multiple inputs, duplicate identity rules, metadata round-trip.

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
