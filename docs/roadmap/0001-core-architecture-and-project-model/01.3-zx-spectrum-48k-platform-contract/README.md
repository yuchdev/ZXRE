# Task 01.3 - ZX Spectrum 48K Platform Contract

## Story

Define the minimum machine/platform abstraction required by later static and dynamic tools, then
implement the first concrete platform description for ZX Spectrum 48K.  The purpose is to prevent
Spectrum constants from leaking through the project core while avoiding a speculative universal
emulator/CPU framework.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define platform descriptor interfaces | [01-define-platform-descriptor-interfaces.md](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/01-define-platform-descriptor-interfaces.md) | ⬜ Not started |
| 02 | Implement ZX Spectrum 48K memory map | [02-implement-zx-spectrum-48k-memory-map.md](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/02-implement-zx-spectrum-48k-memory-map.md) | ⬜ Not started |
| 03 | Define Z80 architecture metadata | [03-define-z80-architecture-metadata.md](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/03-define-z80-architecture-metadata.md) | ⬜ Not started |
| 04 | Connect project validation to platform registry | [04-connect-project-validation-to-platform-registry.md](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/04-connect-project-validation-to-platform-registry.md) | ⬜ Not started |
| 05 | Add platform-aware address validation helpers | [05-add-platform-aware-address-validation-helpers.md](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/05-add-platform-aware-address-validation-helpers.md) | ⬜ Not started |
| 06 | Document ZX Spectrum 48K platform contract | [06-document-zx-spectrum-48k-platform-contract.md](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/06-document-zx-spectrum-48k-platform-contract.md) | ⬜ Not started |

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
