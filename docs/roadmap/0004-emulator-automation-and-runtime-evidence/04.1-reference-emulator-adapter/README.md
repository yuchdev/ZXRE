# Task 04.1 - Reference Emulator Adapter

## Story

Implement the first real backend against the runtime contract. ZEsarUX/ZRCP is the preferred
reference because it exposes the needed debugger surface, but every ZRCP command, lifecycle rule and
quirk stays isolated in the adapter.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Create ZEsarUX adapter package and configuration | [01-create-zesarux-adapter-package-and-configuration.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/01-create-zesarux-adapter-package-and-configuration.md) | ⬜ Not started |
| 02 | Implement ZRCP transport client | [02-implement-zrcp-transport-client.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/02-implement-zrcp-transport-client.md) | ⬜ Not started |
| 03 | Implement ZRCP command layer | [03-implement-zrcp-command-layer.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/03-implement-zrcp-command-layer.md) | ⬜ Not started |
| 04 | Implement optional ZEsarUX process launcher | [04-implement-optional-zesarux-process-launcher.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/04-implement-optional-zesarux-process-launcher.md) | ⬜ Not started |
| 05 | Map ZEsarUX features to runtime capabilities | [05-map-zesarux-features-to-runtime-capabilities.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/05-map-zesarux-features-to-runtime-capabilities.md) | ⬜ Not started |
| 06 | Implement EmulatorBackend adapter | [06-implement-emulatorbackend-adapter.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/06-implement-emulatorbackend-adapter.md) | ⬜ Not started |
| 07 | Add live ZEsarUX integration test marker | [07-add-live-zesarux-integration-test-marker.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/07-add-live-zesarux-integration-test-marker.md) | ⬜ Not started |
| 08 | Document reference adapter | [08-document-reference-adapter.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/08-document-reference-adapter.md) | ⬜ Not started |

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
