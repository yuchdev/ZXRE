# Task 02.4 - Ingestion Validation Fixtures

## Story

Create a legal, deterministic fixture corpus and integration suite proving that TAP/TZX ingestion,
BASIC loader decoding, snapshot generation and memory comparison remain stable across refactoring
and external-tool upgrades.  Fixtures must be authored/generated for this project or otherwise
redistributable; do not commit copyrighted commercial game images or ROMs.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define fixture policy and directory structure | [01-define-fixture-policy-and-directory-structure.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/01-define-fixture-policy-and-directory-structure.md) | ⬜ Not started |
| 02 | Create synthetic TAP fixture builder | [02-create-synthetic-tap-fixture-builder.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/02-create-synthetic-tap-fixture-builder.md) | ⬜ Not started |
| 03 | Create synthetic TZX fixture builder | [03-create-synthetic-tzx-fixture-builder.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/03-create-synthetic-tzx-fixture-builder.md) | ⬜ Not started |
| 04 | Create minimal BASIC loader fixture set | [04-create-minimal-basic-loader-fixture-set.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/04-create-minimal-basic-loader-fixture-set.md) | ⬜ Not started |
| 05 | Create deterministic machine-code payload fixtures | [05-create-deterministic-machine-code-payload-fixtures.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/05-create-deterministic-machine-code-payload-fixtures.md) | ⬜ Not started |
| 06 | Create snapshot fixtures without copyrighted ROM content | [06-create-snapshot-fixtures-without-copyrighted-rom-content.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/06-create-snapshot-fixtures-without-copyrighted-rom-content.md) | ⬜ Not started |
| 07 | Add external-backend integration test marker | [07-add-external-backend-integration-test-marker.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/07-add-external-backend-integration-test-marker.md) | ⬜ Not started |
| 08 | Add Milestone 0002 end-to-end acceptance test | [08-add-milestone-0002-end-to-end-acceptance-test.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/08-add-milestone-0002-end-to-end-acceptance-test.md) | ⬜ Not started |
| 09 | Document regression/fixture maintenance | [09-document-regression-fixture-maintenance.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/09-document-regression-fixture-maintenance.md) | ⬜ Not started |

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
