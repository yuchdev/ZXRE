# Milestone 0004 - Emulator Automation and Runtime Evidence

**Status:** not started - see [status.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/status.md).

## Why this milestone exists

Add the laboratory layer required to distinguish actual execution from plausible static code. ZXRE
needs deterministic runtime capabilities — machine-state inspection, breakpoints, watchpoints, input
replay, traces, snapshots and screen capture — but those capabilities must be expressed through an
**emulator-neutral interface**, not hard-wired to one emulator.

The first implementation should use one concrete backend to prove the contract. **ZEsarUX via ZRCP
is the recommended reference backend**, but it is not an architectural dependency. A different
emulator may satisfy the same contract if it provides equivalent deterministic behavior.

`zesarux-mcp` is an **optional companion integration** for direct interactive access from Claude,
Codex or another MCP-capable harness. ZXRE must not require an MCP-to-MCP chain for its runtime
evidence pipeline.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 04.0 | [Emulator capability contract](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.0-emulator-capability-contract/README.md) | Define the minimum runtime/debugger interface: session control, snapshots, memory/register access, stepping/running, breakpoints/watchpoints, input, traces/coverage and screen capture. Separate required capabilities from optional backend extensions. | Stable emulator-neutral runtime interface and capability discovery model. |
| 04.1 | [Reference emulator adapter](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.1-reference-emulator-adapter/README.md) | Implement one complete adapter against the contract. Prefer ZEsarUX/ZRCP initially, while isolating backend-specific commands and quirks. | First working backend proving the generic interface. |
| 04.2 | [Breakpoints, watchpoints and execution control](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.2-breakpoints-watchpoints-and-execution-control/README.md) | Normalize breakpoints, memory watches, pause/step/run semantics and stop reasons. Define explicit graceful degradation for unsupported optional features. | Deterministic runtime observation/control primitives independent of emulator brand. |
| 04.3 | [Execution, memory and coverage tracing](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.3-execution-memory-and-coverage-tracing/README.md) | Normalize execution history, code coverage and selected memory/I/O observations into ZXRE trace artifacts. | Portable trace model populated by the reference emulator. |
| 04.4 | [Reproducible input scripting](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.4-reproducible-input-scripting/README.md) | Represent keyboard/input stimuli independently of a particular emulator API and replay them from defined machine states. | Backend-neutral input scenarios usable by experiments. |
| 04.5 | [Screen and machine-state capture](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.5-screen-and-machine-state-capture/README.md) | Normalize screenshots/raw display state, registers, RAM and snapshots into ZXRE artifacts. Import backend-created host files rather than retaining unstable external paths. | Synchronized visual and machine-state artifacts with provenance. |
| 04.6 | [Trace-assisted code/data refinement](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.6-trace-assisted-code-data-refinement/README.md) | Feed runtime execution evidence into the static control map without treating unexecuted bytes as proven data. | Evidence-backed refinement of the disassembly map. |
| 04.7 | [Optional external debugger/MCP bridge](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/04.7-optional-external-debugger-mcp-bridge/README.md) | Define how a human or agent harness may use an external low-level debugger integration in parallel with ZXRE. `zesarux-mcp` is the reference example, but other emulator/debugger MCPs must fit the same extension point. Direct external actions are exploratory unless explicitly imported into ZXRE evidence. | Optional interoperability path for `zesarux-mcp` and future debugger MCPs without making them core dependencies. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level contract; each numbered subtask is independently assignable to
Copilot or another coding agent while preserving the emulator-neutral boundary and the distinction
between canonical ZXRE evidence and optional external debugger integrations.

## Milestone completion criteria

ZXRE can execute a deterministic runtime-analysis scenario through the generic emulator capability
interface using at least one concrete ZX Spectrum backend. The scenario can restore state, apply
controlled input, observe execution/memory behavior, capture visual/machine state and persist portable
evidence artifacts. Replacing the reference emulator must not require changes to the
knowledge/evidence model or agent-facing contracts.

## Non-goals

- Requiring ZEsarUX specifically.
- Requiring `zesarux-mcp` for automated ZXRE operation.
- Implementing an emulator inside ZXRE.
- Supporting several production-quality emulator backends in this milestone.
- Hiding backend capability gaps.

## Dependency and sequencing notes

Begin after [Milestone 0003](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/plan.md).
Validate the interface immediately against one real backend rather than generalizing speculatively.
ZEsarUX/ZRCP is the preferred first adapter; `zesarux-mcp` may be used to prototype workflows or
inspect emulator behavior, but canonical evidence collection should pass through the ZXRE runtime
interface.
