# Task 01.1 - Canonical Reverse-Engineering Project Model / Subtask 01 - Define project domain types

## Objective

Create `src/zxre/project/model.py`.

## Implementation specification

Implement typed immutable/value-oriented domain types, preferably dataclasses with `slots=True` and
frozen where appropriate.

Minimum types:
- `ProjectId`
- `ProjectMetadata`
- `ProjectFormatVersion`
- `InputId`
- `InputDescriptor`
- `Address`
- `AddressRange`
- `SymbolId`
- `Symbol`
- `AnalysisNoteId`
- `AnalysisNote`

Requirements:
- integer address validation is explicit;
- `AddressRange` uses clearly documented half-open `[start, end)` semantics;
- IDs are stable opaque strings/UUID wrappers rather than bare dict keys spread through the code;
- no ZX Spectrum-specific constants in this module;
- no file-system access in value objects.

Create `tests/project/test_model.py` covering validation, equality and range boundaries.

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
