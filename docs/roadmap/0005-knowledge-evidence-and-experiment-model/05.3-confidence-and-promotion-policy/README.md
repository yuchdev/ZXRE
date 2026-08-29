# Task 05.3 - Confidence and Promotion Policy

## Story

Define machine-checkable guardrails that determine when semantic claims may be promoted into
confirmed project knowledge. The policy should rely on evidence classes and reproducibility, not on
opaque LLM self-confidence.  This task must make it impossible for a later agent to convert an
unsupported guess into a confirmed symbol/entity meaning merely by assigning a high probability.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define evidence grade scale | [01-define-evidence-grade-scale.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/01-define-evidence-grade-scale.md) | ⬜ Not started |
| 02 | Define claim confidence summary | [02-define-claim-confidence-summary.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/02-define-claim-confidence-summary.md) | ⬜ Not started |
| 03 | Define promotion rules by hypothesis kind | [03-define-promotion-rules-by-hypothesis-kind.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/03-define-promotion-rules-by-hypothesis-kind.md) | ⬜ Not started |
| 04 | Implement contradiction/blocking rules | [04-implement-contradiction-blocking-rules.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/04-implement-contradiction-blocking-rules.md) | ⬜ Not started |
| 05 | Implement promotion evaluator | [05-implement-promotion-evaluator.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/05-implement-promotion-evaluator.md) | ⬜ Not started |
| 06 | Implement controlled promotion transaction | [06-implement-controlled-promotion-transaction.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/06-implement-controlled-promotion-transaction.md) | ⬜ Not started |
| 07 | Implement policy audit log | [07-implement-policy-audit-log.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/07-implement-policy-audit-log.md) | ⬜ Not started |
| 08 | Document confidence/promotion policy | [08-document-confidence-promotion-policy.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/08-document-confidence-promotion-policy.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless the repository state clearly permits safe parallel work.
- Read the Milestone 0005
  [plan.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/plan.md), this README and the
  chosen subtask before implementation.
- Treat deterministic observations, evidence, hypotheses and confirmed knowledge as distinct layers.
- Prefer explicit state transitions and audit records over mutable status flags with hidden history.
- Do not pre-implement Milestone 0006 agent/MCP behavior or Milestone 0008 autonomous experiment
  planning.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output can be demonstrated entirely
without an LLM or agent harness.
