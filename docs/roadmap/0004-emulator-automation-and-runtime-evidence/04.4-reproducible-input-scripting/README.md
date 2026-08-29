# Task 04.4 - Reproducible Input Scripting

## Story

Represent input as replayable logical scenarios independent of an emulator's key-code API, providing
deterministic building blocks for later experiments.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define input event/scenario model | [01-define-input-event-scenario-model.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/01-define-input-event-scenario-model.md) | ⬜ Not started |
| 02 | Define ZX Spectrum logical key map | [02-define-zx-spectrum-logical-key-map.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/02-define-zx-spectrum-logical-key-map.md) | ⬜ Not started |
| 03 | Implement input scenario serialization | [03-implement-input-scenario-serialization.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/03-implement-input-scenario-serialization.md) | ⬜ Not started |
| 04 | Implement input execution service | [04-implement-input-execution-service.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/04-implement-input-execution-service.md) | ⬜ Not started |
| 05 | Implement ZEsarUX key mapping | [05-implement-zesarux-key-mapping.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/05-implement-zesarux-key-mapping.md) | ⬜ Not started |
| 06 | Add deterministic BASIC input scenario fixture | [06-add-deterministic-basic-input-scenario-fixture.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/06-add-deterministic-basic-input-scenario-fixture.md) | ⬜ Not started |
| 07 | Add scenario replay regression tests | [07-add-scenario-replay-regression-tests.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/07-add-scenario-replay-regression-tests.md) | ⬜ Not started |
| 08 | Document input scripting | [08-document-input-scripting.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/08-document-input-scripting.md) | ⬜ Not started |

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
