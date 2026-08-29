# Task 05.3 - Confidence and Promotion Policy / Subtask 01 - Define evidence grade scale

## Objective

Create `src/zxre/policy/evidence_grade.py` and tests. Implement an ordinal grade scheme such as
`UNKNOWN`, `SEMANTIC_RESEMBLANCE`, `STATIC_STRUCTURAL`, `DYNAMIC_CORRELATION`,
`CONTROLLED_INTERVENTION`, `DETERMINISTIC_PROOF`. Document exact meaning and admissible evidence
kinds for each grade.

## Constraints

- Keep implementation within Milestone 0005 scope.
- Do not add model-specific prompts, LLM calls, agents, Skills, autonomous hypothesis generation or
  autonomous experiment design.
- Preserve historical/audit state; avoid destructive mutation of hypotheses, evidence or promotion
  history.
- Evidence must reference immutable/durable source identities where possible.
- Floating-point model confidence must not become the canonical promotion mechanism.
- Use existing ArtifactStore, runtime, trace, capture, static-analysis and project abstractions rather
  than duplicating them.
- Update tests together with production code.

## Completion conditions

- All named files/APIs are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green.
- Project state can be reopened with knowledge/evidence/hypothesis/experiment history intact.
- No unsupported semantic claim can be promoted merely by setting a high confidence value.
