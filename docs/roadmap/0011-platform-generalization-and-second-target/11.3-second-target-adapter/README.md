# Task 11.3 - Second Target Adapter

## Story

Implement one constrained end-to-end second platform. The recommended reference is **Commodore 64 /
MOS 6510**, using simple `.prg` input, a 6510/6502-compatible decoder/assembler stack and VICE as
the reference emulator/debugger if its implementation-time interfaces are suitable.  The goal is
architecture validation, not comprehensive C64 reverse engineering.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Implement MOS 6510 architecture descriptor | [01-implement-mos-6510-architecture-descriptor.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/01-implement-mos-6510-architecture-descriptor.md) | ⬜ Not started |
| 02 | Implement C64 platform descriptor | [02-implement-c64-platform-descriptor.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/02-implement-c64-platform-descriptor.md) | ⬜ Not started |
| 03 | Implement PRG input parser/importer | [03-implement-prg-input-parser-importer.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/03-implement-prg-input-parser-importer.md) | ⬜ Not started |
| 04 | Implement minimal CBM BASIC SYS loader decoding where present | [04-implement-minimal-cbm-basic-sys-loader-decoding-where-present.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/04-implement-minimal-cbm-basic-sys-loader-decoding-where-present.md) | ⬜ Not started |
| 05 | Implement 6510/6502 disassembly backend | [05-implement-6510-6502-disassembly-backend.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/05-implement-6510-6502-disassembly-backend.md) | ⬜ Not started |
| 06 | Implement C64 reconstruction dialect/assembler adapter | [06-implement-c64-reconstruction-dialect-assembler-adapter.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/06-implement-c64-reconstruction-dialect-assembler-adapter.md) | ⬜ Not started |
| 07 | Implement VICE runtime adapter | [07-implement-vice-runtime-adapter.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/07-implement-vice-runtime-adapter.md) | ⬜ Not started |
| 08 | Implement C64 logical input mapping | [08-implement-c64-logical-input-mapping.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/08-implement-c64-logical-input-mapping.md) | ⬜ Not started |
| 09 | Implement basic C64 display/screen capture path | [09-implement-basic-c64-display-screen-capture-path.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/09-implement-basic-c64-display-screen-capture-path.md) | ⬜ Not started |
| 10 | Create legal synthetic C64 fixture | [10-create-legal-synthetic-c64-fixture.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/10-create-legal-synthetic-c64-fixture.md) | ⬜ Not started |
| 11 | Add end-to-end C64 deterministic pipeline test | [11-add-end-to-end-c64-deterministic-pipeline-test.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/11-add-end-to-end-c64-deterministic-pipeline-test.md) | ⬜ Not started |
| 12 | Document C64 reference adapter | [12-document-c64-reference-adapter.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/12-document-c64-reference-adapter.md) | ⬜ Not started |

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
