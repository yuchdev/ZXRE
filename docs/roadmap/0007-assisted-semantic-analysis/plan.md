# Milestone 0007 - Assisted Semantic Analysis

**Status:** not started - see [status.md](/docs/roadmap/0007-assisted-semantic-analysis/status.md).

## Why this milestone exists

Expand from bounded loader/main-loop discovery into systematic semantic understanding of code and
data. The LLM may propose names, structures and subsystem roles, but the project must keep uncertain
conclusions separate and use existing runtime/static evidence to prioritize analysis.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 07.0 | [Routine semantic analysis](/docs/roadmap/0007-assisted-semantic-analysis/07.0-routine-semantic-analysis/README.md) | Analyze routine inputs/outputs, register usage, callers/callees, memory effects and likely purpose with explicit supporting evidence. | Evidence-backed routine summaries and semantic-name proposals. |
| 07.1 | [Variable and state discovery](/docs/roadmap/0007-assisted-semantic-analysis/07.1-variable-and-state-discovery/README.md) | Correlate memory locations/ranges with runtime changes and code references to propose game-state variables and structures. | Candidate/confirmed variables with typed semantic roles. |
| 07.2 | [Data structure and table analysis](/docs/roadmap/0007-assisted-semantic-analysis/07.2-data-structure-and-table-analysis/README.md) | Recognize jump tables, lookup tables, text, level-like structures and other non-code representations. | Structured data interpretations without corrupting lossless reconstruction. |
| 07.3 | [Graphics and asset analysis](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/README.md) | Render candidate screen/tile/sprite/font regions and use multimodal analysis where useful to classify visual assets. | Address-linked asset catalog and generated visual evidence. |
| 07.4 | [Subsystem map](/docs/roadmap/0007-assisted-semantic-analysis/07.4-subsystem-map/README.md) | Cluster confirmed/probable routines and state into input, player, enemies, collision, rendering, sound, levels and other discovered subsystems. | Evidence-linked architecture graph with uncertainty preserved. |
| 07.5 | [Critic and competing-hypothesis review](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/README.md) | Systematically challenge high-impact semantic conclusions and create unresolved alternatives when evidence is insufficient. | Reduced semantic lock-in and prioritized verification backlog. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level semantic-analysis contract; each numbered subtask is
independently assignable to Copilot or another coding agent while preserving evidence-backed
hypotheses, promotion policy, and the mechanically faithful reconstruction layer.

## Milestone completion criteria

The system can turn a mechanically correct disassembly into a partially semantic model of routines,
variables, assets and subsystems while retaining evidence, alternatives and confidence.

## Non-goals

- Automatically inventing experiments for every ambiguity.
- Refactoring reconstructed assembly into clean modules.
- Cross-platform CPU analysis.

## Dependency and sequencing notes

Begin this milestone after the core outputs required from [Milestone 0006](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md) are available. Later milestones may be designed in parallel,
but implementation should not bypass missing deterministic/evidence foundations from earlier
milestones.
