# Milestone 0003 - Static Analysis and Byte-Exact Reconstruction

**Status:** not started - see [status.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/status.md).

## Why this milestone exists

Build the deterministic static-analysis backbone before any semantic agent is allowed to rename or
restructure code. The system must be able to disassemble known memory, record instruction and
reference structure, classify regions conservatively, generate assembler and prove lossless round-
tripping where supported.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 03.0 | [Disassembly backend integration](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.0-disassembly-backend-integration/README.md) | Wrap SkoolKit and/or a Z80 decoder behind normalized instruction, region and disassembly contracts. | Structured Z80 disassembly tied to snapshot addresses and artifacts. |
| 03.1 | [Code/data control map](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/README.md) | Support explicit and generated control maps for code, bytes, words, text and unclassified regions. | Editable deterministic classification layer independent of semantic labels. |
| 03.2 | [References and control-flow facts](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.2-references-and-control-flow-facts/README.md) | Extract direct CALL/JP/JR targets, basic reference relationships and conservative routine candidates. | Query surface for callers, callees, branches and address references. |
| 03.3 | [Lossless assembler source generation](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.3-lossless-assembler-source-generation/README.md) | Generate mechanically faithful assembler from the classified snapshot without semantic refactoring. | Generated source artifact/tree that preserves analyzed bytes. |
| 03.4 | [Byte-exact verification](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.4-byte-exact-verification/README.md) | Assemble/rebuild generated source and compare it against the source memory image with address-level mismatch reports. | Permanent reconstruction invariant and regression command. |
| 03.5 | [Static analysis reports](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/README.md) | Produce human-readable maps of code/data coverage, unresolved regions and reconstruction status. | Baseline static-analysis report usable by humans and agents. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level contract; each numbered subtask is intended to be independently
assignable to Copilot or another coding agent while preserving byte fidelity, deterministic analysis,
and separation from later semantic/runtime reasoning.

## Milestone completion criteria

A loaded snapshot can be conservatively disassembled, classified, converted into mechanically
faithful assembler and rebuilt with byte-exact verification or an explicit diagnostic explaining
every difference.

## Non-goals

- Claiming semantic routine names from opcode patterns.
- Automated gameplay experiments.
- Refactored or human-friendly source modules.

## Dependency and sequencing notes

Begin this milestone after the core outputs required from [Milestone 0002](/docs/roadmap/0002-tape-ingestion-and-loaded-state/plan.md) are available. Later milestones may be designed in parallel, but
implementation should not bypass missing deterministic/evidence foundations from earlier milestones.
