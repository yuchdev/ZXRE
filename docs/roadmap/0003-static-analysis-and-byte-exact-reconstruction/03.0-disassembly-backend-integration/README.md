# Task 03.0 - Disassembly Backend Integration

## Story

Introduce a deterministic static-disassembly layer over normalized snapshot memory. ZXRE must be
able to decode Z80 instructions from known addresses, preserve exact instruction bytes, record
decode failures, and switch between concrete disassembly backends without leaking backend syntax
into project state.  The initial implementation may use an internal decoder, SkoolKit, or both. The
canonical output is ZXRE's structured instruction model, not a third-party text listing.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define disassembly domain model | [01-define-disassembly-domain-model.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/01-define-disassembly-domain-model.md) | ⬜ Not started |
| 02 | Define disassembler backend contract | [02-define-disassembler-backend-contract.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/02-define-disassembler-backend-contract.md) | ⬜ Not started |
| 03 | Implement built-in Z80 decoder or selected library adapter | [03-implement-built-in-z80-decoder-or-selected-library-adapter.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/03-implement-built-in-z80-decoder-or-selected-library-adapter.md) | ⬜ Not started |
| 04 | Implement optional SkoolKit disassembly adapter | [04-implement-optional-skoolkit-disassembly-adapter.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/04-implement-optional-skoolkit-disassembly-adapter.md) | ⬜ Not started |
| 05 | Implement disassembly service | [05-implement-disassembly-service.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/05-implement-disassembly-service.md) | ⬜ Not started |
| 06 | Persist structured disassembly | [06-persist-structured-disassembly.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/06-persist-structured-disassembly.md) | ⬜ Not started |
| 07 | Add backend equivalence regression tests | [07-add-backend-equivalence-regression-tests.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/07-add-backend-equivalence-regression-tests.md) | ⬜ Not started |
| 08 | Document disassembly architecture | [08-document-disassembly-architecture.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/08-document-disassembly-architecture.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless repository state makes safe parallel work obvious.
- Read the Milestone 0003
  [plan.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/plan.md), this
  README and the selected subtask before implementation.
- Static analysis may produce candidates (e.g. routine starts) only when the candidate nature is
  explicit. Do not turn heuristics into confirmed semantics.
- Generated assembly must favor exact byte reconstruction over readability.
- Do not pre-implement Milestone 0004 runtime evidence or Milestone 0007 semantic analysis.

## Task completion criteria

All subtasks are complete, tests and docs are present, and the task output is reproducible from a
fresh clone with documented optional external tools.
