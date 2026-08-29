# Milestone 0010 - Cross-Harness Portability and Model Routing

**Status:** not started - see [status.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/status.md).

## Why this milestone exists

Validate ZXRE MCP, the project/evidence model and the emulator capability contract as the true
portability boundaries.

Portability is two-dimensional:

1. **Agent harness portability** — Claude, Codex, Copilot or another MCP-capable harness can operate
   on the same ZXRE project.
2. **Low-level debugger portability** — optional emulator/debugger MCPs may be attached alongside
   ZXRE (for example `zesarux-mcp`), but Skills and canonical evidence must not depend on a specific
   companion server.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 10.0 | [Harness-neutral workflow contract](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.0-harness-neutral-workflow-contract/README.md) | Extract the minimum orchestration, procedure and result contracts portable across agent harnesses. | Documented harness-neutral investigation protocol. |
| 10.1 | [Second agent harness integration](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/README.md) | Integrate one additional MCP-capable harness such as Codex or Copilot and reproduce a bounded investigation on the same project state. | Cross-harness proof over the same evidence model. |
| 10.2 | [Portable Skill/procedure packaging](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/README.md) | Separate canonical procedures from Claude-specific wrappers and prohibit dependencies on a particular emulator MCP tool vocabulary. | Reusable procedures with thin harness adapters. |
| 10.3 | [External debugger/MCP adapter metadata](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/README.md) | Define optional metadata/configuration describing available companion debugger MCPs and capability mappings without making ZXRE depend on their schemas. Validate `zesarux-mcp` as one reference. | Portable optional companion-tool discovery/mapping model. |
| 10.4 | [Model capability and cost routing](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/README.md) | Route routine summarization, difficult reasoning, vision/asset analysis and critic work to appropriate configured models. | Policy-driven model selection with observability and budgets. |
| 10.5 | [Multi-agent review strategies](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/README.md) | Support optional independent analyses, critic passes or consensus for high-impact ambiguous claims. | Controlled cooperative/competitive reasoning without changing deterministic ground truth. |
| 10.6 | [Cross-harness and companion-tool regression scenarios](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/README.md) | Run identical goals through supported harnesses, with and without optional low-level debugger MCPs, and compare evidence quality, cost and reproducibility. | Portability benchmark demonstrating that companion MCPs improve convenience rather than define correctness. |

## Milestone completion criteria

At least two agent harnesses operate on the same project through the same ZXRE MCP/core interfaces.
The canonical workflow succeeds without an external emulator MCP, while a companion such as
`zesarux-mcp` can be enabled without changing project semantics.

## Non-goals

- Supporting every harness or emulator MCP.
- A universal MCP-to-MCP proxy layer.
- Making deterministic core contracts depend on a model or debugger server.

## Dependency and sequencing notes

Begin after [Milestone 0009](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/plan.md).
Use ZEsarUX + optional `zesarux-mcp` as a concrete reference configuration, not as the definition of
the portable interfaces.
