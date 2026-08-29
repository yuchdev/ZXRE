# Task 05.1 - Evidence and Provenance

## Story

Implement first-class evidence records that attach immutable observations and artifacts to claims.
Evidence may come from static analysis, runtime traces, memory diffs, screenshots, rebuild
verification or explicit human assertions. Evidence must preserve provenance and must not itself
assert that a semantic conclusion is true.  This task bridges deterministic artifacts from
Milestones 0001–0004 into the semantic knowledge layer.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define evidence domain model | [01-define-evidence-domain-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/01-define-evidence-domain-model.md) | ⬜ Not started |
| 02 | Define immutable source references | [02-define-immutable-source-references.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/02-define-immutable-source-references.md) | ⬜ Not started |
| 03 | Implement evidence store | [03-implement-evidence-store.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/03-implement-evidence-store.md) | ⬜ Not started |
| 04 | Implement evidence creation helpers for deterministic outputs | [04-implement-evidence-creation-helpers-for-deterministic-outputs.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/04-implement-evidence-creation-helpers-for-deterministic-outputs.md) | ⬜ Not started |
| 05 | Implement human assertion evidence | [05-implement-human-assertion-evidence.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/05-implement-human-assertion-evidence.md) | ⬜ Not started |
| 06 | Implement external observation evidence | [06-implement-external-observation-evidence.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/06-implement-external-observation-evidence.md) | ⬜ Not started |
| 07 | Define evidence serialization and integrity checks | [07-define-evidence-serialization-and-integrity-checks.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/07-define-evidence-serialization-and-integrity-checks.md) | ⬜ Not started |
| 08 | Document evidence semantics | [08-document-evidence-semantics.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/08-document-evidence-semantics.md) | ⬜ Not started |

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
