# Task 04.7 - Optional External Debugger/MCP Bridge

## Story

Define optional interoperability for low-level emulator/debugger MCP servers. `zesarux-mcp` is the
reference companion, but ZXRE must neither depend on its tool schema nor treat direct companion
calls as canonical evidence unless explicitly imported/reproduced.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define companion debugger descriptor model | [01-define-companion-debugger-descriptor-model.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/01-define-companion-debugger-descriptor-model.md) | ⬜ Not started |
| 02 | Define capability-mapping metadata | [02-define-capability-mapping-metadata.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/02-define-capability-mapping-metadata.md) | ⬜ Not started |
| 03 | Create zesarux-mcp companion descriptor | [03-create-zesarux-mcp-companion-descriptor.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/03-create-zesarux-mcp-companion-descriptor.md) | ⬜ Not started |
| 04 | Define exploratory-vs-canonical provenance policy | [04-define-exploratory-vs-canonical-provenance-policy.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/04-define-exploratory-vs-canonical-provenance-policy.md) | ⬜ Not started |
| 05 | Implement external observation import APIs | [05-implement-external-observation-import-apis.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/05-implement-external-observation-import-apis.md) | ⬜ Not started |
| 06 | Document dual-MCP development configuration | [06-document-dual-mcp-development-configuration.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/06-document-dual-mcp-development-configuration.md) | ⬜ Not started |
| 07 | Add generic companion integration documentation | [07-add-generic-companion-integration-documentation.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/07-add-generic-companion-integration-documentation.md) | ⬜ Not started |
| 08 | Add integration registry tests | [08-add-integration-registry-tests.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/08-add-integration-registry-tests.md) | ⬜ Not started |

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
