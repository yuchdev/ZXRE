# Task 05.2 - Hypothesis Lifecycle

## Story

Represent semantic claims explicitly as hypotheses with an auditable lifecycle. A hypothesis may be
proposed, supported, contradicted, rejected, superseded or confirmed, and multiple competing
hypotheses may coexist for the same address/entity/question.  No automatic model reasoning is
implemented here; this is the durable state machine later agents will use.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define hypothesis domain model | [01-define-hypothesis-domain-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/01-define-hypothesis-domain-model.md) | ⬜ Not started |
| 02 | Define hypothesis lifecycle state machine | [02-define-hypothesis-lifecycle-state-machine.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/02-define-hypothesis-lifecycle-state-machine.md) | ⬜ Not started |
| 03 | Attach supporting and contradicting evidence | [03-attach-supporting-and-contradicting-evidence.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/03-attach-supporting-and-contradicting-evidence.md) | ⬜ Not started |
| 04 | Implement competing-hypothesis groups | [04-implement-competing-hypothesis-groups.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/04-implement-competing-hypothesis-groups.md) | ⬜ Not started |
| 05 | Implement hypothesis store and queries | [05-implement-hypothesis-store-and-queries.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/05-implement-hypothesis-store-and-queries.md) | ⬜ Not started |
| 06 | Implement supersession and revision history | [06-implement-supersession-and-revision-history.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/06-implement-supersession-and-revision-history.md) | ⬜ Not started |
| 07 | Integrate confirmed hypotheses with knowledge entities | [07-integrate-confirmed-hypotheses-with-knowledge-entities.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/07-integrate-confirmed-hypotheses-with-knowledge-entities.md) | ⬜ Not started |
| 08 | Document hypothesis lifecycle | [08-document-hypothesis-lifecycle.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/08-document-hypothesis-lifecycle.md) | ⬜ Not started |

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
