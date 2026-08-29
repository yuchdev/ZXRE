# Task 05.5 - Research Frontier Queries

## Story

Expose a structured investigation backlog derived from current project knowledge, hypotheses,
evidence and analysis gaps. The frontier should tell later orchestrators what is confirmed, likely,
unknown, contradicted, blocked or especially valuable to investigate without itself using an LLM to
choose the next task.  This is a deterministic query/ranking substrate, not autonomous research
planning.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define research-frontier model | [01-define-research-frontier-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/01-define-research-frontier-model.md) | ⬜ Not started |
| 02 | Derive open hypothesis frontier items | [02-derive-open-hypothesis-frontier-items.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/02-derive-open-hypothesis-frontier-items.md) | ⬜ Not started |
| 03 | Derive static-analysis gap items | [03-derive-static-analysis-gap-items.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/03-derive-static-analysis-gap-items.md) | ⬜ Not started |
| 04 | Derive runtime/evidence gap items | [04-derive-runtime-evidence-gap-items.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/04-derive-runtime-evidence-gap-items.md) | ⬜ Not started |
| 05 | Define deterministic priority signals | [05-define-deterministic-priority-signals.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/05-define-deterministic-priority-signals.md) | ⬜ Not started |
| 06 | Implement frontier service and filters | [06-implement-frontier-service-and-filters.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/06-implement-frontier-service-and-filters.md) | ⬜ Not started |
| 07 | Persist frontier snapshots or regenerate on demand | [07-persist-frontier-snapshots-or-regenerate-on-demand.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/07-persist-frontier-snapshots-or-regenerate-on-demand.md) | ⬜ Not started |
| 08 | Add frontier report and CLI view | [08-add-frontier-report-and-cli-view.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/08-add-frontier-report-and-cli-view.md) | ⬜ Not started |
| 09 | Document research-frontier semantics | [09-document-research-frontier-semantics.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/09-document-research-frontier-semantics.md) | ⬜ Not started |

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
