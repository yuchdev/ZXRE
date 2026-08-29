# Task 03.3 - Lossless Assembler Source Generation

## Story

Generate mechanically faithful assembler source from the classified memory image. The output should
be suitable for reassembly while preserving bytes, addresses and intentionally unclassified data.
Readability is secondary to reproducibility at this stage.  The source generator must not perform
semantic refactoring or invent high-level routine names.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define reconstruction/source model | [01-define-reconstruction-source-model.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/01-define-reconstruction-source-model.md) | ⬜ Not started |
| 02 | Define assembler dialect abstraction | [02-define-assembler-dialect-abstraction.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/02-define-assembler-dialect-abstraction.md) | ⬜ Not started |
| 03 | Generate deterministic labels for direct targets | [03-generate-deterministic-labels-for-direct-targets.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/03-generate-deterministic-labels-for-direct-targets.md) | ⬜ Not started |
| 04 | Render CODE regions | [04-render-code-regions.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/04-render-code-regions.md) | ⬜ Not started |
| 05 | Render non-code regions | [05-render-non-code-regions.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/05-render-non-code-regions.md) | ⬜ Not started |
| 06 | Generate source units and linker/order plan | [06-generate-source-units-and-linker-order-plan.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/06-generate-source-units-and-linker-order-plan.md) | ⬜ Not started |
| 07 | Store generated source as project artifacts | [07-store-generated-source-as-project-artifacts.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/07-store-generated-source-as-project-artifacts.md) | ⬜ Not started |
| 08 | Document lossless source policy | [08-document-lossless-source-policy.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/08-document-lossless-source-policy.md) | ⬜ Not started |

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
