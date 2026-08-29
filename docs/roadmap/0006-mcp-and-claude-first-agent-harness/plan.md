# Milestone 0006 - MCP Interface and Claude-First Agent Harness

**Status:** not started - see [status.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/status.md).

## Why this milestone exists

Expose the stable deterministic, runtime and knowledge layers to an LLM without coupling them to one
agent harness or one emulator. **ZXRE MCP is the project-aware agent boundary**: it exposes evidence,
hypotheses, experiments and normalized operations. Claude Code is the first proving harness.

Low-level emulator MCPs are optional companions rather than dependencies. For example,
`zesarux-mcp` may be registered alongside ZXRE MCP to let a human or agent inspect ZEsarUX directly,
but ZXRE must remain functional when it is absent and must permit equivalent MCP/debugger tools for
other emulators.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 06.0 | ZXRE MCP server foundation | Expose project-scoped deterministic capabilities with bounded inputs, typed results and safe artifact access. | Runnable local ZXRE MCP server over the existing core. |
| 06.1 | Project-aware deterministic tool surface | Publish project, tape, snapshot, disassembly, runtime, trace, assembler and experiment operations as composable tools. Runtime tools use the generic emulator capability interface rather than ZEsarUX/ZRCP directly. | Stable MCP tool catalog with portable runtime semantics. |
| 06.2 | MCP resource surface | Expose project summary, memory map, routines, variables, traces, hypotheses, evidence, experiments and active backend/capability information. | Context-efficient read interface for agents. |
| 06.3 | External-tool capability and provenance rules | Define how optional emulator/debugger MCPs are treated. Direct actions outside ZXRE are exploratory unless explicitly imported into an experiment/evidence record. | Clear boundary between canonical ZXRE evidence and optional external debugger interactions. |
| 06.4 | Claude project instructions and guardrails | Define rules for provenance, hypothesis handling, deterministic verification, emulator capability gaps and context usage. | Claude Code can investigate without assuming a specific emulator. |
| 06.5 | Core analysis Skills | Define reusable procedures such as loader analysis, routine analysis, code/data classification, runtime hypothesis testing and reconstruction validation. Skills target ZXRE capabilities, not emulator-specific tool names. | Procedure layer portable across emulator backends. |
| 06.6 | Role-based agents | Introduce Investigator, Loader Analyst, Static Analyst, Dynamic Analyst, Asset Analyst, Reconstruction Agent and Critic/Verifier roles as justified. | Claude-first collaborative analysis workflow. |
| 06.7 | Optional companion MCP configuration | Document and validate running ZXRE MCP beside `zesarux-mcp` as the reference setup while keeping the same extension point open for other debugger MCPs. Avoid mandatory MCP-to-MCP proxying. | Supported optional dual-MCP development/debugging setup. |
| 06.8 | Guided end-to-end investigation | Run a bounded goal such as identifying the real entry point and main loop using canonical ZXRE evidence. Optional direct debugger access may assist exploration, but final claims must be reproduced through ZXRE. | First LLM-assisted investigation proving the architecture end to end. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level contract; each numbered subtask is independently assignable to
Copilot or another coding agent while preserving the ZXRE MCP boundary, harness portability, and the
distinction between canonical project evidence and optional external-debugger exploration.

## Milestone completion criteria

Claude can complete a bounded investigation through ZXRE MCP without requiring a specific emulator
MCP. Optional external emulator/debugger MCPs may assist exploration, but canonical evidence and
semantic claims remain portable project state managed by ZXRE.

## Non-goals

- Making one emulator MCP part of the ZXRE protocol.
- Proxying every ZEsarUX/ZRCP operation through ZXRE MCP.
- Full autonomous game reverse engineering.
- Multiple primary LLM harnesses in this milestone.
- A custom orchestration UI.

## Dependency and sequencing notes

Begin after [Milestone 0005](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/plan.md).
The generic emulator capability interface from Milestone 0004 is the runtime dependency; ZEsarUX,
ZRCP and `zesarux-mcp` are concrete integrations behind or beside that boundary.
