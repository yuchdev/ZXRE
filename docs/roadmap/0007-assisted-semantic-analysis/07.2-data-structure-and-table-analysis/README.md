# Task 07.2 - Data Structure and Table Analysis

## Story

Interpret non-code regions as candidate structured data while preserving the underlying lossless
bytes and control map. The system should recognize common structural patterns—jump tables, pointer
tables, lookup tables, text, level-like records—without rewriting the canonical memory image or
claiming semantic purpose without evidence.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define data interpretation model | [01-define-data-interpretation-model.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/01-define-data-interpretation-model.md) | ⬜ Not started |
| 02 | Implement pointer/jump-table detector | [02-implement-pointer-jump-table-detector.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/02-implement-pointer-jump-table-detector.md) | ⬜ Not started |
| 03 | Implement lookup-table pattern analyzer | [03-implement-lookup-table-pattern-analyzer.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/03-implement-lookup-table-pattern-analyzer.md) | ⬜ Not started |
| 04 | Implement text/string detector | [04-implement-text-string-detector.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/04-implement-text-string-detector.md) | ⬜ Not started |
| 05 | Implement record-layout candidate analyzer | [05-implement-record-layout-candidate-analyzer.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/05-implement-record-layout-candidate-analyzer.md) | ⬜ Not started |
| 06 | Implement data interpretation service | [06-implement-data-interpretation-service.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/06-implement-data-interpretation-service.md) | ⬜ Not started |
| 07 | Integrate with control-map presentation only | [07-integrate-with-control-map-presentation-only.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/07-integrate-with-control-map-presentation-only.md) | ⬜ Not started |
| 08 | Add data-analysis Skill | [08-add-data-analysis-skill.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/08-add-data-analysis-skill.md) | ⬜ Not started |
| 09 | Add synthetic table/record fixtures | [09-add-synthetic-table-record-fixtures.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/09-add-synthetic-table-record-fixtures.md) | ⬜ Not started |
| 10 | Document data interpretation | [10-document-data-interpretation.md](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/10-document-data-interpretation.md) | ⬜ Not started |

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
