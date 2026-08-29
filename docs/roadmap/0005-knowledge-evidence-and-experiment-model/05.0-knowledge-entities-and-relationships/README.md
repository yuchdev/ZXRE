# Task 05.0 - Knowledge Entities and Relationships

## Story

Implement the durable semantic knowledge model that later agents and humans will populate. The model
must represent reverse-engineering entities—routines, variables, data blocks, assets, symbols and
higher-level concepts—plus typed relationships between them, without confusing these semantic
entities with raw deterministic artifacts or with hypotheses about their meaning.  The knowledge
model is queryable project state, but every semantic assertion that is not a plain deterministic
fact will later be governed by evidence and hypothesis policies from the following tasks.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define knowledge entity identifiers and base model | [01-define-knowledge-entity-identifiers-and-base-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/01-define-knowledge-entity-identifiers-and-base-model.md) | ⬜ Not started |
| 02 | Define routine, variable and data-block entities | [02-define-routine-variable-and-data-block-entities.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/02-define-routine-variable-and-data-block-entities.md) | ⬜ Not started |
| 03 | Define asset and concept entities | [03-define-asset-and-concept-entities.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/03-define-asset-and-concept-entities.md) | ⬜ Not started |
| 04 | Define typed relationship model | [04-define-typed-relationship-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/04-define-typed-relationship-model.md) | ⬜ Not started |
| 05 | Implement knowledge graph store | [05-implement-knowledge-graph-store.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/05-implement-knowledge-graph-store.md) | ⬜ Not started |
| 06 | Implement entity merge/alias semantics | [06-implement-entity-merge-alias-semantics.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/06-implement-entity-merge-alias-semantics.md) | ⬜ Not started |
| 07 | Integrate static-analysis facts as knowledge references | [07-integrate-static-analysis-facts-as-knowledge-references.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/07-integrate-static-analysis-facts-as-knowledge-references.md) | ⬜ Not started |
| 08 | Document knowledge model | [08-document-knowledge-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/08-document-knowledge-model.md) | ⬜ Not started |

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
