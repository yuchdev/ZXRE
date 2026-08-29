# Task 08.1 - Differential Memory Experiments

## Story

Automate controlled before/after memory comparisons across repeated scenarios to identify candidate
state locations. The system should support repeated intersections and contrasts—stand still vs move,
left vs right, before vs after collect/death/room change—while keeping semantic interpretation
outside the deterministic diff engine.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define differential experiment model | [01-define-differential-experiment-model.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/01-define-differential-experiment-model.md) | ⬜ Not started |
| 02 | Implement reproducible before/after runner | [02-implement-reproducible-before-after-runner.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/02-implement-reproducible-before-after-runner.md) | ⬜ Not started |
| 03 | Implement repeated-run intersection analysis | [03-implement-repeated-run-intersection-analysis.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/03-implement-repeated-run-intersection-analysis.md) | ⬜ Not started |
| 04 | Implement scenario contrast analysis | [04-implement-scenario-contrast-analysis.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/04-implement-scenario-contrast-analysis.md) | ⬜ Not started |
| 05 | Implement value-delta summaries | [05-implement-value-delta-summaries.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/05-implement-value-delta-summaries.md) | ⬜ Not started |
| 06 | Implement differential candidate ranking | [06-implement-differential-candidate-ranking.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/06-implement-differential-candidate-ranking.md) | ⬜ Not started |
| 07 | Create differential-state-discovery Skill | [07-create-differential-state-discovery-skill.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/07-create-differential-state-discovery-skill.md) | ⬜ Not started |
| 08 | Add MCP tools/resources for differential analysis | [08-add-mcp-tools-resources-for-differential-analysis.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/08-add-mcp-tools-resources-for-differential-analysis.md) | ⬜ Not started |
| 09 | Add synthetic state-variable regression scenario | [09-add-synthetic-state-variable-regression-scenario.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/09-add-synthetic-state-variable-regression-scenario.md) | ⬜ Not started |
| 10 | Document differential-memory methodology | [10-document-differential-memory-methodology.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/10-document-differential-memory-methodology.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone
  [plan.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/plan.md), this README and
  the selected subtask before implementation.
- Prefer the lowest-cost falsifiable experiment that distinguishes current hypotheses.
- Restore controlled state before intervention trials and retain all observations, including failures.
- Autonomous mode must stop cleanly when evidence is insufficient or budget/risk guards are reached.
- Do not pre-implement Milestone 0009 semantic source refactoring or Milestone 0010 cross-harness/model
  routing.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task can be exercised through canonical
ZXRE experiment/evidence state without relying on hidden agent conversation history.
