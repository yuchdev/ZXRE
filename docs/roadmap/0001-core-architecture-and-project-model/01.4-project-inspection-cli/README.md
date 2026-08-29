# Task 01.4 - Project Inspection CLI

## Story

Expose the completed Milestone 0001 foundation through a deterministic CLI useful to both humans and
future agents. The CLI must create/open projects, register original inputs, inspect project
metadata/platform layout, list artifacts/symbols, and verify artifact integrity.  It must remain a
thin application layer over `ProjectService`, `ArtifactStore` and platform registry; no CLI command
may implement domain behavior independently.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define CLI command structure | [01-define-cli-command-structure.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/01-define-cli-command-structure.md) | ⬜ Not started |
| 02 | Implement project create/info commands | [02-implement-project-create-info-commands.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/02-implement-project-create-info-commands.md) | ⬜ Not started |
| 03 | Implement input commands | [03-implement-input-commands.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/03-implement-input-commands.md) | ⬜ Not started |
| 04 | Implement artifact inspection and verification commands | [04-implement-artifact-inspection-and-verification-commands.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/04-implement-artifact-inspection-and-verification-commands.md) | ⬜ Not started |
| 05 | Implement platform show command | [05-implement-platform-show-command.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/05-implement-platform-show-command.md) | ⬜ Not started |
| 06 | Implement symbol listing command | [06-implement-symbol-listing-command.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/06-implement-symbol-listing-command.md) | ⬜ Not started |
| 07 | Add end-to-end CLI integration test | [07-add-end-to-end-cli-integration-test.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/07-add-end-to-end-cli-integration-test.md) | ⬜ Not started |
| 08 | Update user/developer documentation and milestone status | [08-update-user-developer-documentation-and-milestone-status.md](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/08-update-user-developer-documentation-and-milestone-status.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless the current repository state makes two clearly independent.
- A coding agent should read this task README, the milestone
  [plan.md](/docs/roadmap/0001-core-architecture-and-project-model/plan.md), and the specific subtask
  file before modifying code.
- Do not pre-implement later tasks merely to make an abstraction look more general.
- Every subtask should leave the repository passing all quality gates established by Task 01.0.

## Task completion criteria

All subtasks are complete, their tests and documentation are present, and the task's output described
in the milestone plan is demonstrably usable from a fresh clone.
