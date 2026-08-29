# ZXRE Roadmap

Planning and progress tracking for the LLM-assisted reverse-engineering platform, organised as a
three-tier hierarchy: **Milestone → Task → Subtask**.

The roadmap deliberately starts with one concrete target — **ZX Spectrum 48K / Z80 with TAP/TZX
inputs** — and postpones multi-platform generalization until one complete deterministic + agentic
workflow has been proven.

## Hierarchy & vocabulary

| Tier | Meaning | Lives in |
|---|---|---|
| **Milestone** | A large strategic initiative / development direction. | `docs/roadmap/{NNNN}-{milestone-slug}/` |
| **Task** | One deliverable unit of a milestone. Listed in the milestone's `## Tasks` table. | A future subfolder `…/{TT.t}-{task-slug}/` with a `README.md`. |
| **Subtask** | An atomic implementable specification. | A future file `…/{TT.t}-{task-slug}/{NN}-{subtask-slug}.md`. |

A *subtask* is part of a *task*; a *task* is part of a *milestone*.

This archive intentionally defines **milestones and tasks only**. Task folders and subtask files
should be created when an individual task is ready for detailed design, so file/class/config/agent
choices are made against the repository state that actually exists at that point.

## File & folder convention

```text
docs/roadmap/
  README.md
  {NNNN}-{milestone-slug}/
    plan.md
    status.md
    {TT.t}-{task-slug}/          # created only when that task is specified
      README.md
      {NN}-{subtask-slug}.md
```

- `{NNNN}` — zero-padded milestone number (`0001`, `0002`, …).
- `{TT.t}` — task number from the milestone's `## Tasks` table.
- `{NN}` — zero-padded subtask order.
- Slugs are kebab-case.
- Use **Milestone**, **Task** and **Subtask** consistently; reserve *Phase* for a possible
  higher-level product-vision grouping.
- References to specific repository documents use absolute-from-repository-root Markdown links.
- Template paths containing `{...}` remain code spans rather than links.

## Sequencing principles

1. Establish durable project state and provenance before integrating external tools.
2. Build deterministic tape → snapshot → disassembly → assembler verification before LLM semantics.
3. Add an emulator-neutral runtime capability interface before asking an agent to reason from runtime behavior; use one concrete emulator as the reference adapter.
4. Define evidence/hypothesis/experiment semantics before allowing agents to persist conclusions.
5. Use ZXRE MCP as the stable project-aware cross-harness boundary; treat emulator/debugger MCPs such as `zesarux-mcp` as optional companions.
6. Add semantic automation incrementally: assisted interpretation first, autonomous experiments later.
7. Keep mechanically faithful source separate from semantic reconstruction.
8. Generalize to other platforms only after the ZX Spectrum path works end to end.

## Milestones

| # | Milestone | Spec | Status |
|---|---|---|---|
| 0001 | Core Architecture and Project Model | [plan.md](/docs/roadmap/0001-core-architecture-and-project-model/plan.md) | [status.md](/docs/roadmap/0001-core-architecture-and-project-model/status.md) |
| 0002 | Tape Ingestion and Loaded Machine State | [plan.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/plan.md) | [status.md](/docs/roadmap/0002-tape-ingestion-and-loaded-state/status.md) |
| 0003 | Static Analysis and Byte-Exact Reconstruction | [plan.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/plan.md) | [status.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/status.md) |
| 0004 | Emulator Automation and Runtime Evidence | [plan.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/plan.md) | [status.md](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/status.md) |
| 0005 | Knowledge, Evidence and Experiment Model | [plan.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/plan.md) | [status.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/status.md) |
| 0006 | MCP Interface and Claude-First Agent Harness | [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md) | [status.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/status.md) |
| 0007 | Assisted Semantic Analysis | [plan.md](/docs/roadmap/0007-assisted-semantic-analysis/plan.md) | [status.md](/docs/roadmap/0007-assisted-semantic-analysis/status.md) |
| 0008 | Autonomous Experiments and Causal Analysis | [plan.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/plan.md) | [status.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/status.md) |
| 0009 | Semantic Source Reconstruction and Documentation | [plan.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/plan.md) | [status.md](/docs/roadmap/0009-semantic-source-reconstruction-and-documentation/status.md) |
| 0010 | Cross-Harness Portability and Model Routing | [plan.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/plan.md) | [status.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/status.md) |
| 0011 | Platform Generalization and Second Target | [plan.md](/docs/roadmap/0011-platform-generalization-and-second-target/plan.md) | [status.md](/docs/roadmap/0011-platform-generalization-and-second-target/status.md) |

## Intended capability progression

```text
project model
  ↓
TAP/TZX inspection + loaded snapshot
  ↓
static disassembly + byte-exact rebuild
  ↓
emulator capability interface + reference backend + traces
  ↓
evidence / hypotheses / experiments
  ↓
MCP + Claude Skills/agents
  ↓
semantic routine/data/asset analysis
  ↓
autonomous causal experiments
  ↓
semantic ASM + documentation
  ↓
cross-harness/model routing
  ↓
second platform
```
