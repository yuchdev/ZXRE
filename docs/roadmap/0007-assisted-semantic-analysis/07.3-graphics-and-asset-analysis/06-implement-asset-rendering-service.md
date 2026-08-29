# Task 07.3 - Graphics and Asset Analysis / Subtask 06 - Implement asset rendering service

## Objective

Create `src/zxre/assets/service.py`. Register render outputs in ArtifactStore with source
snapshot/range/layout parameters and deterministic provenance.

## Constraints

- Keep implementation within Milestone 0007 scope.
- Semantic names, roles, structures and subsystem assignments are hypotheses unless Milestone 0005
  policy has promoted them.
- Preserve mechanical labels, exact bytes, control-map state and byte-exact reconstruction independently
  from semantic overlays.
- Reuse Milestone 0006 MCP/Skills/agent architecture; do not create a second orchestration framework.
- Deterministic analyzers may describe patterns/features but must not embed gameplay-specific semantic
  conclusions.
- Do not introduce Milestone 0008 autonomous experiment design/information-gain loops.
- Keep large disassembly/trace/image data as referenced artifacts/resources rather than duplicated state.
- Update tests/docs with implementation.

## Completion conditions

- Named files/APIs/Skills/agent updates are implemented.
- Relevant unit/integration tests pass.
- Semantic proposals retain evidence/hypothesis links and cannot bypass promotion policy.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green where applicable.
- Lossless reconstruction remains unaffected by uncertain semantic overlays.
