# Task 07.5 - Critic and Competing-Hypothesis Review / Subtask 06 - Create review-high-impact-hypothesis Skill

## Objective

Create `skills/review-high-impact-hypothesis/SKILL.md` selecting hypotheses by centrality/promotion
impact, gathering all evidence, requiring at least one alternative when ambiguity remains, and
recording findings.

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
