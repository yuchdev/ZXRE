# Task 09.0 - Confirmed-Symbol Promotion

## Story

Promote only policy-approved semantic names, constants, comments and structural annotations into a
dedicated semantic source layer. Promotion must preserve provenance back to confirmed
hypotheses/evidence and must never overwrite the mechanically faithful symbol/source representation.
The semantic symbol layer is a controlled projection of confirmed knowledge, not a free-form rename
workspace.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define semantic symbol model | [01-define-semantic-symbol-model.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/01-define-semantic-symbol-model.md) | ⬜ Not started |
| 02 | Define promotion eligibility adapter | [02-define-promotion-eligibility-adapter.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/02-define-promotion-eligibility-adapter.md) | ⬜ Not started |
| 03 | Implement semantic naming rules | [03-implement-semantic-naming-rules.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/03-implement-semantic-naming-rules.md) | ⬜ Not started |
| 04 | Implement symbol overlay store | [04-implement-symbol-overlay-store.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/04-implement-symbol-overlay-store.md) | ⬜ Not started |
| 05 | Implement conflict detection with mechanical symbols | [05-implement-conflict-detection-with-mechanical-symbols.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/05-implement-conflict-detection-with-mechanical-symbols.md) | ⬜ Not started |
| 06 | Implement promotion transaction service | [06-implement-promotion-transaction-service.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/06-implement-promotion-transaction-service.md) | ⬜ Not started |
| 07 | Expose semantic-symbol MCP tools/resources | [07-expose-semantic-symbol-mcp-tools-resources.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/07-expose-semantic-symbol-mcp-tools-resources.md) | ⬜ Not started |
| 08 | Add promotion regression tests | [08-add-promotion-regression-tests.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/08-add-promotion-regression-tests.md) | ⬜ Not started |
| 09 | Document semantic symbol layering | [09-document-semantic-symbol-layering.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/09-document-semantic-symbol-layering.md) | ⬜ Not started |

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
