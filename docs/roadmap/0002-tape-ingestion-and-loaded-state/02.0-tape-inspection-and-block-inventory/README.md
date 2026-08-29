# Task 02.0 - Tape Inspection and Block Inventory

## Story

Implement deterministic ingestion of ZX Spectrum `.tap` and `.tzx` files into structured project
records. The task must identify container structure, block boundaries, standard header/data
relationships and raw payloads without executing loaders or guessing semantic meaning.  The parser
output becomes canonical input evidence for later BASIC decoding, snapshot generation and reverse
engineering. Parsing must be reproducible, independent of an emulator, and safe against
malformed/truncated input.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define tape domain model | [01-define-tape-domain-model.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/01-define-tape-domain-model.md) | ⬜ Not started |
| 02 | Implement TAP parser | [02-implement-tap-parser.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/02-implement-tap-parser.md) | ⬜ Not started |
| 03 | Implement TZX parser core | [03-implement-tzx-parser-core.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/03-implement-tzx-parser-core.md) | ⬜ Not started |
| 04 | Normalize standard Spectrum header blocks | [04-normalize-standard-spectrum-header-blocks.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/04-normalize-standard-spectrum-header-blocks.md) | ⬜ Not started |
| 05 | Implement tape inventory service | [05-implement-tape-inventory-service.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/05-implement-tape-inventory-service.md) | ⬜ Not started |
| 06 | Implement raw block extraction | [06-implement-raw-block-extraction.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/06-implement-raw-block-extraction.md) | ⬜ Not started |
| 07 | Persist tape inventory metadata | [07-persist-tape-inventory-metadata.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/07-persist-tape-inventory-metadata.md) | ⬜ Not started |
| 08 | Document tape ingestion model | [08-document-tape-ingestion-model.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/08-document-tape-ingestion-model.md) | ⬜ Not started |

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
