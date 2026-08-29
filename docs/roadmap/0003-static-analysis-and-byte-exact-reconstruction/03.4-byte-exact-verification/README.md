# Task 03.4 - Byte-Exact Verification

## Story

Establish reconstruction verification as a permanent invariant: generated assembler must be built
and compared against the original analyzed memory bytes, with precise diagnostics for every
difference.  Verification must distinguish assembler/source failure, layout differences and byte
mismatches rather than returning only pass/fail.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define assembler backend contract | [01-define-assembler-backend-contract.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/01-define-assembler-backend-contract.md) | ⬜ Not started |
| 02 | Implement reference assembler adapter | [02-implement-reference-assembler-adapter.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/02-implement-reference-assembler-adapter.md) | ⬜ Not started |
| 03 | Define verification model | [03-define-verification-model.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/03-define-verification-model.md) | ⬜ Not started |
| 04 | Implement binary-to-memory mapping for rebuilt output | [04-implement-binary-to-memory-mapping-for-rebuilt-output.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/04-implement-binary-to-memory-mapping-for-rebuilt-output.md) | ⬜ Not started |
| 05 | Implement byte-exact comparator | [05-implement-byte-exact-comparator.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/05-implement-byte-exact-comparator.md) | ⬜ Not started |
| 06 | Implement reconstruction verification service | [06-implement-reconstruction-verification-service.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/06-implement-reconstruction-verification-service.md) | ⬜ Not started |
| 07 | Add deliberate encoding-ambiguity regression cases | [07-add-deliberate-encoding-ambiguity-regression-cases.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/07-add-deliberate-encoding-ambiguity-regression-cases.md) | ⬜ Not started |
| 08 | Add milestone-level exact rebuild integration test | [08-add-milestone-level-exact-rebuild-integration-test.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/08-add-milestone-level-exact-rebuild-integration-test.md) | ⬜ Not started |
| 09 | Document verification invariant | [09-document-verification-invariant.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/09-document-verification-invariant.md) | ⬜ Not started |

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
