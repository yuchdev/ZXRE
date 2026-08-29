# Task 11.1 - Machine/CPU Plugin Boundary

## Story

Generalize the machine and CPU contracts only as required by ZX Spectrum/Z80 plus the chosen second
target. The plugin boundary must cover address spaces/views, CPU decoding metadata, platform memory
regions, input/display descriptors and snapshot/memory materialization without trying to model every
architecture.  Both current ZX support and the second target must implement the same narrow
contracts.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Refine architecture descriptor model | [01-refine-architecture-descriptor-model.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/01-refine-architecture-descriptor-model.md) | ⬜ Not started |
| 02 | Move Z80 metadata into architecture plugin | [02-move-z80-metadata-into-architecture-plugin.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/02-move-z80-metadata-into-architecture-plugin.md) | ⬜ Not started |
| 03 | Define address-space and memory-view model | [03-define-address-space-and-memory-view-model.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/03-define-address-space-and-memory-view-model.md) | ⬜ Not started |
| 04 | Refine platform descriptor/plugin protocol | [04-refine-platform-descriptor-plugin-protocol.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/04-refine-platform-descriptor-plugin-protocol.md) | ⬜ Not started |
| 05 | Define CPU decoder backend registration by architecture | [05-define-cpu-decoder-backend-registration-by-architecture.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/05-define-cpu-decoder-backend-registration-by-architecture.md) | ⬜ Not started |
| 06 | Define source/assembler dialect selection by architecture/platform | [06-define-source-assembler-dialect-selection-by-architecture-platform.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/06-define-source-assembler-dialect-selection-by-architecture-platform.md) | ⬜ Not started |
| 07 | Refine snapshot/memory materializer registry | [07-refine-snapshot-memory-materializer-registry.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/07-refine-snapshot-memory-materializer-registry.md) | ⬜ Not started |
| 08 | Refine input/display plugin descriptors | [08-refine-input-display-plugin-descriptors.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/08-refine-input-display-plugin-descriptors.md) | ⬜ Not started |
| 09 | Add dual-plugin fake conformance tests | [09-add-dual-plugin-fake-conformance-tests.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/09-add-dual-plugin-fake-conformance-tests.md) | ⬜ Not started |
| 10 | Document machine/CPU plugin boundary | [10-document-machine-cpu-plugin-boundary.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/10-document-machine-cpu-plugin-boundary.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0011-platform-generalization-and-second-target/plan.md), this README and the selected
  subtask before implementation.
- Generalize only from concrete requirements demonstrated by supported harnesses/platforms.
- Preserve explicit capability discovery and graceful degradation where implementations differ.
- Canonical correctness is measured from ZXRE project state and deterministic verification, not
  harness prose or external-tool convenience.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is proven against the concrete
implementations selected by the milestone rather than hypothetical future integrations.
