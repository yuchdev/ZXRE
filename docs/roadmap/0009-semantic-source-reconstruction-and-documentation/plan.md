# Milestone 0009 - Semantic Source Reconstruction and Documentation

**Status:** not started - see [status.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/status.md).

## Why this milestone exists

Turn accumulated high-confidence knowledge into useful source and durable human documentation
without sacrificing the mechanically faithful representation. Semantic reconstruction must remain
layered over, and continuously checked against, the lossless build.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 09.0 | [Confirmed-symbol promotion](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.0-confirmed-symbol-promotion/README.md) | Apply only policy-approved names, constants and comments to a semantic source representation. | Semantic symbol layer with provenance back to evidence. |
| 09.1 | [Source module reconstruction](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.1-source-module-reconstruction/README.md) | Organize high-confidence routines/data into meaningful modules while preserving address/layout constraints required for reproducibility. | Readable assembler source tree alongside generated lossless source. |
| 09.2 | [Semantic rebuild verification](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.2-semantic-rebuild-verification/README.md) | Continuously assemble the semantic source and report byte/layout differences separately from intentional transformations. | Trustworthy reconstruction validation pipeline. |
| 09.3 | [Memory and symbol documentation](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.3-memory-and-symbol-documentation/README.md) | Generate human-readable memory maps, variables, data formats and confidence/evidence references. | Living technical reference derived from project state. |
| 09.4 | [Architecture and subsystem documentation](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.4-architecture-and-subsystem-documentation/README.md) | Generate gameplay-loop, rendering, input, entity/state and other discovered subsystem documents from confirmed knowledge. | Evidence-linked software archaeology documentation. |
| 09.5 | [Investigation report and unresolved ledger](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/09.5-investigation-report-and-unresolved-ledger/README.md) | Summarize what is proven, strongly supported, unknown and intentionally deferred. | Reproducible project handoff suitable for another human or agent. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level reconstruction/documentation contract; each numbered subtask is
independently assignable to Copilot or another coding agent while preserving the lossless source as
ground truth, policy-gated semantic promotion, continuous rebuild verification and explicit unresolved
state.

## Milestone completion criteria

The project contains both a mechanically faithful representation and a readable semantic
assembler/documentation layer, with continuous verification and an explicit ledger of unresolved
areas.

## Non-goals

- Modern-language decompilation.
- Behavior-changing refactors or ports.
- Publishing copyrighted game assets.

## Dependency and sequencing notes

Begin this milestone after the core outputs required from [Milestone
0008](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/plan.md) are available. Later
milestones may be designed in parallel, but implementation should not bypass missing
deterministic/evidence foundations from earlier milestones.
