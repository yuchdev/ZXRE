# Task 07.4 - Subsystem Map

## Story

Build an evidence-linked architecture view that groups routines, state, data and assets into
probable subsystems such as input, player update, enemies, collision, rendering, sound and levels.
The map must preserve uncertainty and permit overlapping/competing subsystem assignments until
evidence is strong enough to confirm them.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define subsystem model | [01-define-subsystem-model.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/01-define-subsystem-model.md) | ⬜ Not started |
| 02 | Define subsystem taxonomy as extensible concepts | [02-define-subsystem-taxonomy-as-extensible-concepts.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/02-define-subsystem-taxonomy-as-extensible-concepts.md) | ⬜ Not started |
| 03 | Implement graph-feature aggregation | [03-implement-graph-feature-aggregation.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/03-implement-graph-feature-aggregation.md) | ⬜ Not started |
| 04 | Implement subsystem membership proposal service | [04-implement-subsystem-membership-proposal-service.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/04-implement-subsystem-membership-proposal-service.md) | ⬜ Not started |
| 05 | Implement subsystem architecture graph queries | [05-implement-subsystem-architecture-graph-queries.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/05-implement-subsystem-architecture-graph-queries.md) | ⬜ Not started |
| 06 | Add architecture clustering Skill | [06-add-architecture-clustering-skill.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/06-add-architecture-clustering-skill.md) | ⬜ Not started |
| 07 | Add subsystem MCP resource | [07-add-subsystem-mcp-resource.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/07-add-subsystem-mcp-resource.md) | ⬜ Not started |
| 08 | Add synthetic subsystem fixture | [08-add-synthetic-subsystem-fixture.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/08-add-synthetic-subsystem-fixture.md) | ⬜ Not started |
| 09 | Generate architecture diagram data | [09-generate-architecture-diagram-data.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/09-generate-architecture-diagram-data.md) | ⬜ Not started |
| 10 | Document subsystem mapping | [10-document-subsystem-mapping.md](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/10-document-subsystem-mapping.md) | ⬜ Not started |

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
