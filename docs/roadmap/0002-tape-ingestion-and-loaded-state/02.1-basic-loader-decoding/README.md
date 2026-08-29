# Task 02.1 - BASIC Loader Decoding

## Story

Decode Spectrum BASIC loader programs deterministically enough to expose explicit loader operations
such as `CLEAR`, `LOAD`, `RANDOMIZE USR`, `USR`, and related numeric/string operands. The task must
distinguish syntactically decoded statements from inferred candidate load/entry addresses.  No LLM
interpretation is allowed here: candidates come only from deterministic parsing of BASIC tokens and
simple, documented expression evaluation.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define BASIC loader domain model | [01-define-basic-loader-domain-model.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/01-define-basic-loader-domain-model.md) | ⬜ Not started |
| 02 | Implement Spectrum BASIC token decoder | [02-implement-spectrum-basic-token-decoder.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/02-implement-spectrum-basic-token-decoder.md) | ⬜ Not started |
| 03 | Extract BASIC program payloads from tape inventory | [03-extract-basic-program-payloads-from-tape-inventory.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/03-extract-basic-program-payloads-from-tape-inventory.md) | ⬜ Not started |
| 04 | Implement loader statement recognizer | [04-implement-loader-statement-recognizer.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/04-implement-loader-statement-recognizer.md) | ⬜ Not started |
| 05 | Implement restricted deterministic expression evaluator | [05-implement-restricted-deterministic-expression-evaluator.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/05-implement-restricted-deterministic-expression-evaluator.md) | ⬜ Not started |
| 06 | Derive candidate loader addresses | [06-derive-candidate-loader-addresses.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/06-derive-candidate-loader-addresses.md) | ⬜ Not started |
| 07 | Persist decoded loader analysis | [07-persist-decoded-loader-analysis.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/07-persist-decoded-loader-analysis.md) | ⬜ Not started |
| 08 | Document BASIC loader decoding | [08-document-basic-loader-decoding.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/08-document-basic-loader-decoding.md) | ⬜ Not started |

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
