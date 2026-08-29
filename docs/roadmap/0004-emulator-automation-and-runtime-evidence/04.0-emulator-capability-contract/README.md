# Task 04.0 - Emulator Capability Contract

## Story

Define the runtime/debugger abstraction that separates ZXRE from any specific emulator, remote
protocol, MCP server or process lifecycle. The contract covers deterministic session control,
snapshot load/save, memory/register access, execution control, breakpoints/watchpoints, tracing,
input, screen capture and explicit capability discovery.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define runtime capability taxonomy | [01-define-runtime-capability-taxonomy.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/01-define-runtime-capability-taxonomy.md) | ⬜ Not started |
| 02 | Define runtime session and machine-state models | [02-define-runtime-session-and-machine-state-models.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/02-define-runtime-session-and-machine-state-models.md) | ⬜ Not started |
| 03 | Define emulator/debugger backend protocol | [03-define-emulator-debugger-backend-protocol.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/03-define-emulator-debugger-backend-protocol.md) | ⬜ Not started |
| 04 | Define runtime configuration model | [04-define-runtime-configuration-model.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/04-define-runtime-configuration-model.md) | ⬜ Not started |
| 05 | Define runtime service facade | [05-define-runtime-service-facade.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/05-define-runtime-service-facade.md) | ⬜ Not started |
| 06 | Add fake deterministic runtime backend for tests | [06-add-fake-deterministic-runtime-backend-for-tests.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/06-add-fake-deterministic-runtime-backend-for-tests.md) | ⬜ Not started |
| 07 | Define runtime artifact/provenance conventions | [07-define-runtime-artifact-provenance-conventions.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/07-define-runtime-artifact-provenance-conventions.md) | ⬜ Not started |
| 08 | Document runtime capability contract | [08-document-runtime-capability-contract.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/08-document-runtime-capability-contract.md) | ⬜ Not started |

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
