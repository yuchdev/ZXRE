# Task 07.1 - Variable and State Discovery

## Story

Build a structured workflow for discovering likely game-state variables and grouped state structures
by combining static memory references, runtime reads/writes, snapshot diffs and controlled
observations. Candidate semantics such as `player_x`, `lives` or `current_room` are hypotheses, not
facts, until policy requirements are met.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define variable/state candidate model | [01-define-variable-state-candidate-model.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/01-define-variable-state-candidate-model.md) | ⬜ Not started |
| 02 | Implement memory-reference aggregation | [02-implement-memory-reference-aggregation.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/02-implement-memory-reference-aggregation.md) | ⬜ Not started |
| 03 | Implement differential-state candidate extraction | [03-implement-differential-state-candidate-extraction.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/03-implement-differential-state-candidate-extraction.md) | ⬜ Not started |
| 04 | Implement value-pattern analyzers | [04-implement-value-pattern-analyzers.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/04-implement-value-pattern-analyzers.md) | ⬜ Not started |
| 05 | Implement state candidate service | [05-implement-state-candidate-service.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/05-implement-state-candidate-service.md) | ⬜ Not started |
| 06 | Implement contiguous/grouped state structure proposals | [06-implement-contiguous-grouped-state-structure-proposals.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/06-implement-contiguous-grouped-state-structure-proposals.md) | ⬜ Not started |
| 07 | Extend test-variable-hypothesis Skill | [07-extend-test-variable-hypothesis-skill.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/07-extend-test-variable-hypothesis-skill.md) | ⬜ Not started |
| 08 | Add variable/state MCP views | [08-add-variable-state-mcp-views.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/08-add-variable-state-mcp-views.md) | ⬜ Not started |
| 09 | Add synthetic state-discovery regression suite | [09-add-synthetic-state-discovery-regression-suite.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/09-add-synthetic-state-discovery-regression-suite.md) | ⬜ Not started |
| 10 | Document variable/state discovery | [10-document-variable-state-discovery.md](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/10-document-variable-state-discovery.md) | ⬜ Not started |

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
