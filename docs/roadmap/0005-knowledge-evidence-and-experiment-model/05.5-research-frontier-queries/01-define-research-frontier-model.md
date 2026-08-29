# Task 05.5 - Research Frontier Queries / Subtask 01 - Define research-frontier model

## Objective

Create `src/zxre/frontier/model.py`, package init and tests. Define `FrontierItemId`,
`FrontierItem`, `FrontierCategory`, `FrontierStatus`, `FrontierReason`, and
`FrontierPrioritySignals`. Categories may include `UNKNOWN_REGION`, `OPEN_HYPOTHESIS`, `CONFLICT`,
`UNRESOLVED_FLOW`, `UNCLASSIFIED_DATA`, `LOW_EVIDENCE_ENTITY`, `BLOCKED_EXPERIMENT`, `OTHER`.

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
