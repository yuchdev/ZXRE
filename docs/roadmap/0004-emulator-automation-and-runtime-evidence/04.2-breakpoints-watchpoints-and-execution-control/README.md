# Task 04.2 - Breakpoints, Watchpoints and Execution Control

## Story

Normalize execution control so callers can stop on addresses and memory accesses without knowing
emulator-specific breakpoint syntax, native slot numbering or lifecycle quirks.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define breakpoint/watchpoint models | [01-define-breakpoint-watchpoint-models.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/01-define-breakpoint-watchpoint-models.md) | ⬜ Not started |
| 02 | Implement breakpoint registry/lifecycle | [02-implement-breakpoint-registry-lifecycle.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/02-implement-breakpoint-registry-lifecycle.md) | ⬜ Not started |
| 03 | Implement ZEsarUX breakpoint mapping | [03-implement-zesarux-breakpoint-mapping.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/03-implement-zesarux-breakpoint-mapping.md) | ⬜ Not started |
| 04 | Define execution-control request/result models | [04-define-execution-control-request-result-models.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/04-define-execution-control-request-result-models.md) | ⬜ Not started |
| 05 | Implement step/step-over semantics | [05-implement-step-step-over-semantics.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/05-implement-step-step-over-semantics.md) | ⬜ Not started |
| 06 | Implement bounded run/pause behavior | [06-implement-bounded-run-pause-behavior.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/06-implement-bounded-run-pause-behavior.md) | ⬜ Not started |
| 07 | Add breakpoint/watchpoint acceptance tests | [07-add-breakpoint-watchpoint-acceptance-tests.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/07-add-breakpoint-watchpoint-acceptance-tests.md) | ⬜ Not started |
| 08 | Document execution-control semantics | [08-document-execution-control-semantics.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/08-document-execution-control-semantics.md) | ⬜ Not started |

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
