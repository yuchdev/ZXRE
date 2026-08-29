# Task 04.6 - Trace-Assisted Code/Data Refinement

## Story

Use runtime execution evidence to refine the static control map conservatively: an executed PC
proves code starts there, but unexecuted bytes do not become data automatically.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define refinement proposal model | [01-define-refinement-proposal-model.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/01-define-refinement-proposal-model.md) | ⬜ Not started |
| 02 | Map execution coverage to candidate code bytes | [02-map-execution-coverage-to-candidate-code-bytes.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/02-map-execution-coverage-to-candidate-code-bytes.md) | ⬜ Not started |
| 03 | Detect control-map conflicts | [03-detect-control-map-conflicts.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/03-detect-control-map-conflicts.md) | ⬜ Not started |
| 04 | Apply approved refinement proposals | [04-apply-approved-refinement-proposals.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/04-apply-approved-refinement-proposals.md) | ⬜ Not started |
| 05 | Regenerate disassembly/static flow after refinement | [05-regenerate-disassembly-static-flow-after-refinement.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/05-regenerate-disassembly-static-flow-after-refinement.md) | ⬜ Not started |
| 06 | Add regression scenario | [06-add-regression-scenario.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/06-add-regression-scenario.md) | ⬜ Not started |
| 07 | Add refinement report | [07-add-refinement-report.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/07-add-refinement-report.md) | ⬜ Not started |
| 08 | Document runtime refinement policy | [08-document-runtime-refinement-policy.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/08-document-runtime-refinement-policy.md) | ⬜ Not started |

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
