# Milestone 0001 - Core Architecture and Project Model

**Status:** not started - see [status.md](/docs/roadmap/0001-core-architecture-and-project-model/status.md).

## Why this milestone exists

Establish the stable foundation that every deterministic tool, agent and harness will share. The
milestone defines the canonical reverse-engineering project, artifact storage, platform-facing
contracts and persistent project state while intentionally supporting only the ZX Spectrum 48K
target in the first implementation. The goal is to make later tools composable without prematurely
building a multi-platform framework.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 01.0 | [Repository and development foundation](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/README.md) | Define the repository/package layout, supported Python/tooling baseline, developer workflow, test strategy and command-line entry point. | Runnable empty application/library skeleton with CI-quality local checks. |
| 01.1 | [Canonical reverse-engineering project model](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/README.md) | Define project identity, inputs, immutable/generated artifacts, snapshots, address ranges, symbols and analysis metadata. | Versioned project format and persistent project store. |
| 01.2 | [Artifact and provenance model](/docs/roadmap/0001-core-architecture-and-project-model/01.2-artifact-and-provenance-model/README.md) | Define how imported binaries, extracted blocks, snapshots, traces, reports and generated sources are stored, checksummed and related to their producers. | Reproducible artifact inventory with provenance. |
| 01.3 | [ZX Spectrum 48K platform contract](/docs/roadmap/0001-core-architecture-and-project-model/01.3-zx-spectrum-48k-platform-contract/README.md) | Define the minimum platform description required by later tools: address space, ROM/RAM regions, screen area, machine metadata and Z80 conventions. | Concrete ZX Spectrum 48K platform adapter behind deliberately narrow interfaces. |
| 01.4 | [Project inspection CLI](/docs/roadmap/0001-core-architecture-and-project-model/01.4-project-inspection-cli/README.md) | Provide deterministic commands to create/open a project and inspect its metadata, artifacts and known address-space state. | Human- and agent-friendly project inspection surface. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level contract; each numbered subtask is intended to be independently
assignable to Copilot or another coding agent while preserving the task's sequencing and acceptance
criteria.

## Milestone completion criteria

A new ZX Spectrum 48K reverse-engineering project can be created, reopened and inspected; all stored
artifacts have stable identity and provenance; the core model has no dependency on Claude, MCP,
SkoolKit or a particular emulator.

## Non-goals

- Tape parsing, disassembly, emulation or LLM integration.
- Generic support for other CPUs or machines beyond interfaces needed to avoid hard-coding ZX assumptions everywhere.
- A GUI or custom agent orchestrator.

## Dependency and sequencing notes

This is the foundation milestone. Its contracts should remain deliberately narrow so later
milestones can refine them from real tool integrations rather than speculative abstraction.
