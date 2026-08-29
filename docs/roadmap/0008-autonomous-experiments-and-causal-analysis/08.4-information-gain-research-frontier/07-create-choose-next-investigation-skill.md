# Task 08.4 - Information-Gain Research Frontier / Subtask 07 - Create choose-next-investigation Skill

## Objective

Create `skills/choose-next-investigation/SKILL.md` to compare top frontier items/proposals by
discrimination, unlock value, cost, risk and recent failures, then select one bounded action.

## Constraints

- Keep implementation within Milestone 0008 scope.
- Every experiment must compile to the deterministic Milestone 0005 experiment model before execution.
- Every mutable/interventional trial starts from an explicit reproducible snapshot unless the experiment
  model explicitly defines another controlled baseline.
- Do not let model confidence replace evidence grades, critic review or promotion policy.
- Autonomous decisions must be structured, persisted and bounded by explicit resource/risk limits.
- Direct emulator mutation outside the experiment/intervention APIs is not part of autonomous operation.
- Preserve failed, contradicted and unresolved outcomes; do not optimize tests/workflows toward forced
  confirmation.
- Reuse Milestone 0006 MCP/Skills/agents and Milestone 0007 semantic services rather than creating a
  separate orchestration stack.
- Update tests/docs together with implementation.

## Completion conditions

- Named files/APIs/Skills/agent updates are implemented.
- Relevant deterministic/fake-backend unit and integration tests pass.
- Live-emulator tests remain optional and skip clearly when unavailable.
- Experiments and research runs persist enough state to reproduce/audit their decisions and observations.
- Budget/stop guards prevent unbounded autonomous execution.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green where applicable.
