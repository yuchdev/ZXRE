# Milestone 0011 - Platform Generalization and Second Target

**Status:** not started - see [status.md](/docs/roadmap/0011-platform-generalization-and-second-target/status.md).

## Why this milestone exists

Validate that abstractions discovered through the complete ZX Spectrum workflow are genuinely
reusable. The second target must validate not only CPU/machine abstractions, but also the runtime
tooling boundary: it should be possible to attach a different emulator/debugger implementation and,
optionally, a different companion MCP server without rewriting ZXRE's knowledge, experiment or agent
semantics.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 11.0 | [Architecture extraction review](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/README.md) | Audit ZX-, Z80-, ZEsarUX-, ZRCP- and `zesarux-mcp`-specific assumptions across project, disassembly, emulator, experiment and agent layers. | Concrete list of interfaces requiring generalization and assumptions that remain platform-local. |
| 11.1 | [Machine/CPU plugin boundary](/docs/roadmap/0011-platform-generalization-and-second-target/11.1-machine-cpu-plugin-boundary/README.md) | Generalize only contracts required by a second target: address spaces, instruction decoding, snapshots, input, display and machine metadata. | Stable machine/CPU plugin boundary derived from two implementations. |
| 11.2 | [Runtime debugger/emulator plugin boundary](/docs/roadmap/0011-platform-generalization-and-second-target/11.2-runtime-debugger-emulator-plugin-boundary/README.md) | Validate/refine the Milestone 0004 capability contract with a second emulator/debugger stack. Permit capability discovery and backend extensions without leaking them into canonical evidence semantics. | Emulator-neutral runtime contract proven by two different backends. |
| 11.3 | [Second target adapter](/docs/roadmap/0011-platform-generalization-and-second-target/11.3-second-target-adapter/README.md) | Add one constrained target such as Game Boy, C64/6502 or another well-supported platform. | Second working deterministic analysis path. |
| 11.4 | [Optional companion MCP proof](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/README.md) | If a suitable debugger/emulator MCP exists for the second target, integrate it as an optional companion; otherwise use a minimal mock/reference bridge proving ZXRE does not depend on `zesarux-mcp` conventions. | Evidence that external debugger MCP integration is generic and optional. |
| 11.5 | [Agent procedure portability review](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/README.md) | Identify architecture-neutral Skills/experiments and those needing platform-specialized variants. | Portable and platform-specific procedure taxonomy. |
| 11.6 | [Cross-platform reconstruction benchmark](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/README.md) | Run comparable bounded reverse-engineering goals on ZX Spectrum and the second target using canonical ZXRE evidence. | Evidence that the core generalizes without weakening platform-specific analysis. |

## Milestone completion criteria

The core runs on ZX Spectrum plus one genuinely different target. Each can use a distinct
emulator/debugger backend behind the same capability contract. Optional companion MCP servers can be
different or absent entirely, while knowledge, experiment, evidence and agent layers remain unchanged.

## Non-goals

- Immediate support for modern native binaries or Ghidra-scale targets.
- A universal debugger abstraction covering every architecture.
- A mandatory companion MCP architecture.

## Dependency and sequencing notes

Begin after [Milestone 0010](/docs/roadmap/0010-cross-harness-portability-and-model-routing/plan.md).
Generalize from two concrete implementations, not hypothetical future machines.
