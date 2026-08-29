# Task 01.2 - Artifact and Provenance Model / Subtask 06 - Integrate project inputs with artifact storage

## Objective

Update project input handling from Task 01.1 so an imported original file can be represented as a

## Implementation specification

project input whose bytes are managed by `ArtifactStore`.

Update:
- `src/zxre/project/inputs.py`
- `src/zxre/project/service.py`
- relevant serialization/schema
- tests

Requirements:
- original filename remains metadata;
- checksum/content identity comes from artifact store;
- importing identical content twice does not duplicate physical storage;
- input identity remains distinct from blob identity.

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
