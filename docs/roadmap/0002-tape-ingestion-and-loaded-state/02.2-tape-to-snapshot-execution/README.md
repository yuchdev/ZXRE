# Task 02.2 - Tape-to-Snapshot Execution

## Story

Produce a reproducible loaded machine snapshot from TAP/TZX input using a deterministic
loader/snapshot backend behind a stable ZXRE adapter. The initial backend may use SkoolKit
`tap2sna`, but project/core APIs must not depend on SkoolKit command-line details.  This task is
about obtaining a machine state after deterministic loading, not analyzing unpackers, game loops or
runtime semantics.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define snapshot domain model | [01-define-snapshot-domain-model.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/01-define-snapshot-domain-model.md) | ⬜ Not started |
| 02 | Define loader/snapshot backend interface | [02-define-loader-snapshot-backend-interface.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/02-define-loader-snapshot-backend-interface.md) | ⬜ Not started |
| 03 | Implement SkoolKit tap2sna adapter | [03-implement-skoolkit-tap2sna-adapter.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/03-implement-skoolkit-tap2sna-adapter.md) | ⬜ Not started |
| 04 | Implement snapshot creation service | [04-implement-snapshot-creation-service.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/04-implement-snapshot-creation-service.md) | ⬜ Not started |
| 05 | Parse Z80 snapshot metadata needed by ZXRE | [05-parse-z80-snapshot-metadata-needed-by-zxre.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/05-parse-z80-snapshot-metadata-needed-by-zxre.md) | ⬜ Not started |
| 06 | Validate created snapshot against platform | [06-validate-created-snapshot-against-platform.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/06-validate-created-snapshot-against-platform.md) | ⬜ Not started |
| 07 | Record reproducible snapshot recipe | [07-record-reproducible-snapshot-recipe.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/07-record-reproducible-snapshot-recipe.md) | ⬜ Not started |
| 08 | Document snapshot backend architecture | [08-document-snapshot-backend-architecture.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/08-document-snapshot-backend-architecture.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless the repository state clearly permits safe parallel work.
- Read the Milestone 0002
  [plan.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/plan.md), this README, and the
  selected subtask before implementation.
- Treat original tape bytes and generated snapshots as artifacts with provenance; do not create
  untracked side-channel files.
- Parser/decoder code must preserve unknown or unsupported input where possible rather than turning
  uncertainty into invented semantics.
- Do not pre-implement Milestone 0003 disassembly or Milestone 0004 emulator runtime behavior.

## Task completion criteria

All subtasks are complete, tests and documentation are present, and the task output in the milestone
plan is reproducible from a fresh clone using only documented local dependencies.
