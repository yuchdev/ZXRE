# Milestone 0002 - Tape Ingestion and Loaded Machine State

**Status:** not started - see [status.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/status.md).

## Why this milestone exists

Turn `.tap`/`.tzx` input into deterministic, inspectable evidence. This milestone wraps existing
tape and loader tooling behind stable application contracts and produces a machine snapshot suitable
for all later analysis. Loader behavior, block metadata and derived snapshots must remain
reproducible and attributable to the original tape.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 02.0 | [Tape inspection and block inventory](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.0-tape-inspection-and-block-inventory/README.md) | Inspect TAP/TZX structure, headers, BASIC blocks and CODE/data blocks and normalize the result into project records. | Structured tape/block inventory with raw extraction support. |
| 02.1 | [BASIC loader decoding](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.1-basic-loader-decoding/README.md) | Decode loader programs and surface CLEAR/LOAD/USR-style semantics and candidate load/entry addresses without treating inference as confirmed fact. | Normalized loader representation and candidate entry-point evidence. |
| 02.2 | [Tape-to-snapshot execution](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.2-tape-to-snapshot-execution/README.md) | Integrate a deterministic loader/snapshot backend such as SkoolKit `tap2sna` behind the project API. | Reproducible loaded `.z80`/supported snapshot artifact. |
| 02.3 | [Snapshot memory inspection and diff](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.3-snapshot-memory-inspection-and-diff/README.md) | Read address ranges, export memory images and compare snapshots or memory regions. | Deterministic RAM inspection/diff primitives used by later static and dynamic analysis. |
| 02.4 | [Ingestion validation fixtures](/docs/roadmap/0002-tape-ingestion-and-loaded-state/02.4-ingestion-validation-fixtures/README.md) | Establish small legal/test fixtures covering representative TAP/TZX layouts, BASIC loaders and CODE blocks. | Regression suite proving import and snapshot generation are stable. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level contract; each numbered subtask is intended to be independently
assignable to Copilot or another coding agent while preserving deterministic ingestion semantics,
artifact provenance, and task ordering.

## Milestone completion criteria

Given a supported TAP/TZX file, the system records its block structure and loader, produces a loaded
machine snapshot, and can reproduce and compare the resulting RAM state without manual emulator
work.

## Non-goals

- Semantic identification of unpackers or the real game loop.
- Instruction-level dynamic tracing.
- LLM interpretation.

## Dependency and sequencing notes

Begin this milestone after the core outputs required from [Milestone 0001](/docs/roadmap/0001-core-architecture-and-project-model/plan.md) are available. Later milestones may be designed in parallel,
but implementation should not bypass missing deterministic/evidence foundations from earlier
milestones.
