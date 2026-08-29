# Task 01.2 - Artifact and Provenance Model / Subtask 01 - Define artifact domain model

## Objective

Create `src/zxre/artifacts/model.py` and `tests/artifacts/test_model.py`.

## Implementation specification

Minimum types:
- `ArtifactId`
- `ArtifactKind`
- `ArtifactDescriptor`
- `ArtifactDigest`
- `ArtifactProducer`
- `ProvenanceRecord`

Artifact kinds should cover current/future deterministic classes without encoding tools:
`input`, `binary`, `snapshot`, `trace`, `screen`, `report`, `source`, `metadata`, `other`.

Requirements:
- digest algorithm explicit, default SHA-256;
- identity semantics documented;
- descriptors separate logical metadata from physical path;
- provenance links source artifact IDs and producer metadata.

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
