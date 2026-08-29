# Task 10.0 - Harness-Neutral Workflow Contract

## Story

Extract the minimum workflow contract shared by the proven Claude-first implementation and a second
agent harness. The contract must describe durable inputs, decisions, state transitions, tool/
resource usage and results without depending on Claude prompts, Codex conventions, Copilot syntax or
hidden conversation history.  This is not a new orchestration engine. It is the smallest portable
protocol needed to reproduce the same bounded investigations across harnesses.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define harness-neutral workflow model | [01-define-harness-neutral-workflow-model.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/01-define-harness-neutral-workflow-model.md) | ⬜ Not started |
| 02 | Define harness capability model | [02-define-harness-capability-model.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/02-define-harness-capability-model.md) | ⬜ Not started |
| 03 | Define portable decision/result schemas | [03-define-portable-decision-result-schemas.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/03-define-portable-decision-result-schemas.md) | ⬜ Not started |
| 04 | Define portable context bundle | [04-define-portable-context-bundle.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/04-define-portable-context-bundle.md) | ⬜ Not started |
| 05 | Define workflow checkpoint and handoff semantics | [05-define-workflow-checkpoint-and-handoff-semantics.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/05-define-workflow-checkpoint-and-handoff-semantics.md) | ⬜ Not started |
| 06 | Implement harness adapter protocol | [06-implement-harness-adapter-protocol.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/06-implement-harness-adapter-protocol.md) | ⬜ Not started |
| 07 | Add Claude adapter over existing Milestone 0006 assets | [07-add-claude-adapter-over-existing-milestone-0006-assets.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/07-add-claude-adapter-over-existing-milestone-0006-assets.md) | ⬜ Not started |
| 08 | Add workflow portability conformance tests | [08-add-workflow-portability-conformance-tests.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/08-add-workflow-portability-conformance-tests.md) | ⬜ Not started |
| 09 | Document portable workflow contract | [09-document-portable-workflow-contract.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/09-document-portable-workflow-contract.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/plan.md), this README and the selected
  subtask before implementation.
- Generalize only from concrete requirements demonstrated by supported harnesses/platforms.
- Preserve explicit capability discovery and graceful degradation where implementations differ.
- Canonical correctness is measured from ZXRE project state and deterministic verification, not
  harness prose or external-tool convenience.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is proven against the concrete
implementations selected by the milestone rather than hypothetical future integrations.
