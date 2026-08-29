# Task 08.3 - Trace Comparison and Causal Localization

## Story

Compare execution and memory traces from controlled scenarios to localize routines and state that
causally distinguish behavior. The goal is not to declare semantic meaning from trace frequency, but
to identify compact candidate regions/routines for hypotheses and follow-up interventions.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define trace comparison model | [01-define-trace-comparison-model.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/01-define-trace-comparison-model.md) | ⬜ Not started |
| 02 | Implement coverage set comparison | [02-implement-coverage-set-comparison.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/02-implement-coverage-set-comparison.md) | ⬜ Not started |
| 03 | Implement execution-count comparison | [03-implement-execution-count-comparison.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/03-implement-execution-count-comparison.md) | ⬜ Not started |
| 04 | Implement ordered-trace divergence localization | [04-implement-ordered-trace-divergence-localization.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/04-implement-ordered-trace-divergence-localization.md) | ⬜ Not started |
| 05 | Implement memory-access trace comparison | [05-implement-memory-access-trace-comparison.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/05-implement-memory-access-trace-comparison.md) | ⬜ Not started |
| 06 | Implement causal localization ranking | [06-implement-causal-localization-ranking.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/06-implement-causal-localization-ranking.md) | ⬜ Not started |
| 07 | Create compare-scenarios Skill | [07-create-compare-scenarios-skill.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/07-create-compare-scenarios-skill.md) | ⬜ Not started |
| 08 | Expose trace-comparison MCP views | [08-expose-trace-comparison-mcp-views.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/08-expose-trace-comparison-mcp-views.md) | ⬜ Not started |
| 09 | Add synthetic collision/localization scenario | [09-add-synthetic-collision-localization-scenario.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/09-add-synthetic-collision-localization-scenario.md) | ⬜ Not started |
| 10 | Document causal trace analysis | [10-document-causal-trace-analysis.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/10-document-causal-trace-analysis.md) | ⬜ Not started |

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
