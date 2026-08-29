# Task 09.3 - Memory and Symbol Documentation

## Story

Generate living technical reference documents for memory layout, variables, routines, data formats,
assets and semantic symbols directly from canonical project state. Documentation must show
evidence/promotion status and avoid presenting unresolved interpretations as facts.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define documentation projection model | [01-define-documentation-projection-model.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/01-define-documentation-projection-model.md) | ⬜ Not started |
| 02 | Implement memory-map document generator | [02-implement-memory-map-document-generator.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/02-implement-memory-map-document-generator.md) | ⬜ Not started |
| 03 | Implement symbol reference generator | [03-implement-symbol-reference-generator.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/03-implement-symbol-reference-generator.md) | ⬜ Not started |
| 04 | Implement routine reference generator | [04-implement-routine-reference-generator.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/04-implement-routine-reference-generator.md) | ⬜ Not started |
| 05 | Implement variable/state reference generator | [05-implement-variable-state-reference-generator.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/05-implement-variable-state-reference-generator.md) | ⬜ Not started |
| 06 | Implement data-format reference generator | [06-implement-data-format-reference-generator.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/06-implement-data-format-reference-generator.md) | ⬜ Not started |
| 07 | Implement evidence citation/link convention | [07-implement-evidence-citation-link-convention.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/07-implement-evidence-citation-link-convention.md) | ⬜ Not started |
| 08 | Register generated docs as artifacts | [08-register-generated-docs-as-artifacts.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/08-register-generated-docs-as-artifacts.md) | ⬜ Not started |
| 09 | Add documentation consistency tests | [09-add-documentation-consistency-tests.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/09-add-documentation-consistency-tests.md) | ⬜ Not started |
| 10 | Document generated-reference architecture | [10-document-generated-reference-architecture.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/10-document-generated-reference-architecture.md) | ⬜ Not started |

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
