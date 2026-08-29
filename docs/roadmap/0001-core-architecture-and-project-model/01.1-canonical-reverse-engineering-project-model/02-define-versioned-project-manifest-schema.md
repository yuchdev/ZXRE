# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 02 - Define versioned project manifest schema

## Objective

Create:

## Implementation specification

- `src/zxre/project/schema.py`
- `src/zxre/project/serialization.py`
- `tests/project/test_serialization.py`

Define the on-disk project manifest `project.json` or `project.toml`; prefer JSON if schema evolution
and machine-generated data dominate, TOML only if human editing materially benefits the design.

Manifest must include:
- schema/format version;
- project ID;
- display name;
- created/updated timestamps;
- target platform identifier;
- input descriptors;
- project-level metadata.

Implement:
- `load_manifest(path) -> ProjectManifest`
- `save_manifest(path, manifest) -> None`
- version validation;
- deterministic serialization ordering where practical;
- useful errors for malformed/unsupported versions.

Do not silently migrate unknown future versions.

Tests:
round trip; missing required fields; unknown version; invalid IDs/addresses.

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
