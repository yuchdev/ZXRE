# Task 07.0 - Routine Semantic Analysis

## Story

Implement a systematic evidence-backed workflow for turning mechanically identified routine
candidates into semantic hypotheses about purpose, inputs, outputs and side effects. The LLM may
propose names and roles, but every proposal must remain a hypothesis until supported by explicit
static/runtime evidence and promotion policy.  This task extends the existing `analyze-routine`
Skill and role-based agent setup rather than adding a new orchestration mechanism.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define routine semantic summary model | [01-define-routine-semantic-summary-model.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/01-define-routine-semantic-summary-model.md) | ⬜ Not started |
| 02 | Implement routine context aggregator | [02-implement-routine-context-aggregator.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/02-implement-routine-context-aggregator.md) | ⬜ Not started |
| 03 | Derive deterministic routine interface facts | [03-derive-deterministic-routine-interface-facts.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/03-derive-deterministic-routine-interface-facts.md) | ⬜ Not started |
| 04 | Implement routine semantic proposal service | [04-implement-routine-semantic-proposal-service.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/04-implement-routine-semantic-proposal-service.md) | ⬜ Not started |
| 05 | Extend analyze-routine Skill with structured output | [05-extend-analyze-routine-skill-with-structured-output.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/05-extend-analyze-routine-skill-with-structured-output.md) | ⬜ Not started |
| 06 | Add routine-name proposal validation | [06-add-routine-name-proposal-validation.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/06-add-routine-name-proposal-validation.md) | ⬜ Not started |
| 07 | Add routine semantic MCP/resource views | [07-add-routine-semantic-mcp-resource-views.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/07-add-routine-semantic-mcp-resource-views.md) | ⬜ Not started |
| 08 | Add routine-analysis integration fixtures | [08-add-routine-analysis-integration-fixtures.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/08-add-routine-analysis-integration-fixtures.md) | ⬜ Not started |
| 09 | Document routine semantic workflow | [09-document-routine-semantic-workflow.md](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/09-document-routine-semantic-workflow.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0007-assisted-semantic-analysis/plan.md), this README and
  the selected subtask first.
- Start from deterministic/static/runtime facts and canonical evidence; let agents add interpretation as
  explicit hypotheses.
- Keep confirmed and proposed semantic state visibly distinct in services, MCP resources and reports.
- Do not pre-implement autonomous research loops or semantic source refactoring from later milestones.

## Task completion criteria

All subtasks are complete, tests/docs are present, and semantic outputs are reproducible as canonical
ZXRE hypotheses/knowledge state with evidence and uncertainty preserved.
