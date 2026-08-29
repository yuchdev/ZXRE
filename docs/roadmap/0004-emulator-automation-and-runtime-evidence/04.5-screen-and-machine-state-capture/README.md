# Task 04.5 - Screen and Machine-State Capture

## Story

Capture synchronized runtime observations as portable artifacts: screen state, registers, memory and
snapshots. Backend host paths must be imported into the project rather than becoming canonical
references.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define runtime capture model | [01-define-runtime-capture-model.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/01-define-runtime-capture-model.md) | ⬜ Not started |
| 02 | Implement screen capture service | [02-implement-screen-capture-service.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/02-implement-screen-capture-service.md) | ⬜ Not started |
| 03 | Implement register-state capture | [03-implement-register-state-capture.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/03-implement-register-state-capture.md) | ⬜ Not started |
| 04 | Implement RAM/range capture | [04-implement-ram-range-capture.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/04-implement-ram-range-capture.md) | ⬜ Not started |
| 05 | Implement saved-snapshot capture | [05-implement-saved-snapshot-capture.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/05-implement-saved-snapshot-capture.md) | ⬜ Not started |
| 06 | Implement synchronized capture bundle service | [06-implement-synchronized-capture-bundle-service.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/06-implement-synchronized-capture-bundle-service.md) | ⬜ Not started |
| 07 | Add capture consistency tests | [07-add-capture-consistency-tests.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/07-add-capture-consistency-tests.md) | ⬜ Not started |
| 08 | Document capture semantics | [08-document-capture-semantics.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/08-document-capture-semantics.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless the repository state clearly permits safe parallel work.
- Read the Milestone 0004
  [plan.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/plan.md), this README and the
  chosen subtask before implementation.
- Validate generic runtime behavior with the fake backend before relying on live ZEsarUX.
- Keep backend-specific behavior under `src/zxre/adapters/...`.
- Do not pre-implement Milestone 0005 evidence/hypothesis semantics or Milestone 0006 agent/MCP
  orchestration.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is demonstrable through the
generic runtime interface with the fake backend and, where applicable, the configured reference
emulator.
