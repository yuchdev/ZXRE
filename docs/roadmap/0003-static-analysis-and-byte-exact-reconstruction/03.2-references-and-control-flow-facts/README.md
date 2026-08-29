# Task 03.2 - References and Control-Flow Facts

## Story

Extract deterministic reference and control-flow facts from structured instructions: direct
branches, calls, returns and address references that can be proven from decoded operands. Build
conservative basic-block and routine-candidate views without pretending that indirect jumps or
semantic function boundaries are known.  This task provides queryable facts for later human/agent
analysis.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define reference/control-flow domain model | [01-define-reference-control-flow-domain-model.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/01-define-reference-control-flow-domain-model.md) | ⬜ Not started |
| 02 | Classify Z80 control-flow instructions | [02-classify-z80-control-flow-instructions.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/02-classify-z80-control-flow-instructions.md) | ⬜ Not started |
| 03 | Extract direct address references | [03-extract-direct-address-references.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/03-extract-direct-address-references.md) | ⬜ Not started |
| 04 | Build conservative basic blocks | [04-build-conservative-basic-blocks.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/04-build-conservative-basic-blocks.md) | ⬜ Not started |
| 05 | Build routine candidates | [05-build-routine-candidates.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/05-build-routine-candidates.md) | ⬜ Not started |
| 06 | Persist static reference graph | [06-persist-static-reference-graph.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/06-persist-static-reference-graph.md) | ⬜ Not started |
| 07 | Implement static-analysis query service | [07-implement-static-analysis-query-service.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/07-implement-static-analysis-query-service.md) | ⬜ Not started |
| 08 | Document static-flow guarantees | [08-document-static-flow-guarantees.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/08-document-static-flow-guarantees.md) | ⬜ Not started |

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
