# Task 09.2 - Semantic Rebuild Verification

## Story

Continuously verify that the readable semantic source still reconstructs the analyzed program.
Verification must distinguish byte-exact equality, layout-only changes and explicitly allowed
intentional transformations, and must never let semantic readability silently alter behavior.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define semantic verification model | [01-define-semantic-verification-model.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/01-define-semantic-verification-model.md) | ⬜ Not started |
| 02 | Reuse assembler backend and mapping pipeline | [02-reuse-assembler-backend-and-mapping-pipeline.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/02-reuse-assembler-backend-and-mapping-pipeline.md) | ⬜ Not started |
| 03 | Implement semantic-tree build service | [03-implement-semantic-tree-build-service.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/03-implement-semantic-tree-build-service.md) | ⬜ Not started |
| 04 | Implement exact semantic-vs-source comparison | [04-implement-exact-semantic-vs-source-comparison.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/04-implement-exact-semantic-vs-source-comparison.md) | ⬜ Not started |
| 05 | Implement intentional-transformation registry | [05-implement-intentional-transformation-registry.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/05-implement-intentional-transformation-registry.md) | ⬜ Not started |
| 06 | Implement mismatch attribution | [06-implement-mismatch-attribution.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/06-implement-mismatch-attribution.md) | ⬜ Not started |
| 07 | Add continuous verification command | [07-add-continuous-verification-command.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/07-add-continuous-verification-command.md) | ⬜ Not started |
| 08 | Add semantic rebuild integration fixtures | [08-add-semantic-rebuild-integration-fixtures.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/08-add-semantic-rebuild-integration-fixtures.md) | ⬜ Not started |
| 09 | Add regression guard against semantic drift | [09-add-regression-guard-against-semantic-drift.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/09-add-regression-guard-against-semantic-drift.md) | ⬜ Not started |
| 10 | Document semantic verification pipeline | [10-document-semantic-verification-pipeline.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/10-document-semantic-verification-pipeline.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone
  [plan.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/plan.md), this
  README and the selected subtask first.
- Treat semantic source/documentation as projections over canonical project state.
- Never trade byte fidelity for readability without an explicit recorded transformation.
- Preserve unresolved/competing interpretations in documentation and handoff.
- Do not pre-implement Milestone 0010 cross-harness/model routing or Milestone 0011 platform
  generalization.

## Task completion criteria

All subtasks are complete, tests/docs are present, semantic source continuously verifies against the
original analyzed memory, and another human/agent can resume from generated handoff without hidden
conversation context.
