# Task 09.1 - Source Module Reconstruction

## Story

Organize mechanically faithful assembler into a readable semantic source tree using only
confirmed/high-confidence structure while preserving address/layout constraints required for
reproducibility. Module boundaries are a presentation/organization layer over the same bytes.  This
task improves navigability but does not perform behavior-changing refactors.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define semantic source tree model | [01-define-semantic-source-tree-model.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/01-define-semantic-source-tree-model.md) | ⬜ Not started |
| 02 | Define module-boundary proposal model | [02-define-module-boundary-proposal-model.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/02-define-module-boundary-proposal-model.md) | ⬜ Not started |
| 03 | Implement deterministic module planner | [03-implement-deterministic-module-planner.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/03-implement-deterministic-module-planner.md) | ⬜ Not started |
| 04 | Implement semantic label/comment renderer | [04-implement-semantic-label-comment-renderer.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/04-implement-semantic-label-comment-renderer.md) | ⬜ Not started |
| 05 | Implement include/source tree renderer | [05-implement-include-source-tree-renderer.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/05-implement-include-source-tree-renderer.md) | ⬜ Not started |
| 06 | Preserve unmapped/unresolved regions | [06-preserve-unmapped-unresolved-regions.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/06-preserve-unmapped-unresolved-regions.md) | ⬜ Not started |
| 07 | Implement source-to-lossless mapping manifest | [07-implement-source-to-lossless-mapping-manifest.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/07-implement-source-to-lossless-mapping-manifest.md) | ⬜ Not started |
| 08 | Register semantic source artifacts | [08-register-semantic-source-artifacts.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/08-register-semantic-source-artifacts.md) | ⬜ Not started |
| 09 | Add semantic tree stability tests | [09-add-semantic-tree-stability-tests.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/09-add-semantic-tree-stability-tests.md) | ⬜ Not started |
| 10 | Document module reconstruction policy | [10-document-module-reconstruction-policy.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/10-document-module-reconstruction-policy.md) | ⬜ Not started |

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
