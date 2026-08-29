# Task 05.1 - Evidence and Provenance / Subtask 05 - Implement human assertion evidence

## Objective

Create `src/zxre/evidence/human.py`. Allow a human-authored observation/assertion with author label,
text, optional entity/address links and timestamp. Mark source type explicitly as human assertion;
do not give it deterministic strength automatically.

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
