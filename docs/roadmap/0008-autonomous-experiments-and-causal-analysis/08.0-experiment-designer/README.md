# Task 08.0 - Experiment Designer

## Story

Implement a structured experiment-design layer that converts unresolved hypotheses and available
runtime capabilities into low-cost, falsifiable experiment candidates. The designer may use an LLM
to propose plans, but every plan must compile into the deterministic experiment model from Milestone
0005 before execution.  The designer must prefer experiments that discriminate between competing
hypotheses, explicitly state what outcome would support or falsify each hypothesis, and respect
runtime capability and mutation constraints.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define experiment-design request and proposal models | [01-define-experiment-design-request-and-proposal-models.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/01-define-experiment-design-request-and-proposal-models.md) | ⬜ Not started |
| 02 | Define experiment-design capability context | [02-define-experiment-design-capability-context.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/02-define-experiment-design-capability-context.md) | ⬜ Not started |
| 03 | Implement deterministic feasibility validator | [03-implement-deterministic-feasibility-validator.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/03-implement-deterministic-feasibility-validator.md) | ⬜ Not started |
| 04 | Implement experiment proposal compiler | [04-implement-experiment-proposal-compiler.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/04-implement-experiment-proposal-compiler.md) | ⬜ Not started |
| 05 | Define cost and risk heuristics | [05-define-cost-and-risk-heuristics.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/05-define-cost-and-risk-heuristics.md) | ⬜ Not started |
| 06 | Create design-discriminating-experiment Skill | [06-create-design-discriminating-experiment-skill.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/06-create-design-discriminating-experiment-skill.md) | ⬜ Not started |
| 07 | Extend Investigator and Dynamic Analyst roles | [07-extend-investigator-and-dynamic-analyst-roles.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/07-extend-investigator-and-dynamic-analyst-roles.md) | ⬜ Not started |
| 08 | Expose experiment-design MCP tools/resources | [08-expose-experiment-design-mcp-tools-resources.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/08-expose-experiment-design-mcp-tools-resources.md) | ⬜ Not started |
| 09 | Add synthetic discrimination fixtures | [09-add-synthetic-discrimination-fixtures.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/09-add-synthetic-discrimination-fixtures.md) | ⬜ Not started |
| 10 | Document experiment design contract | [10-document-experiment-design-contract.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/10-document-experiment-design-contract.md) | ⬜ Not started |

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
