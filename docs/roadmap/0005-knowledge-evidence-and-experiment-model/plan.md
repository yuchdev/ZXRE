# Milestone 0005 - Knowledge, Evidence and Experiment Model

**Status:** not started - see [status.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/status.md).

## Why this milestone exists

Create the epistemic boundary between deterministic observations and LLM conclusions. Before agents
are introduced, the project must represent facts, hypotheses, competing interpretations,
confidence/evidence levels, experiments and promotion/rejection history as durable data.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 05.0 | [Knowledge entities and relationships](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.0-knowledge-entities-and-relationships/README.md) | Model routines, variables, data blocks, assets, symbols, concepts and their typed relationships. | Queryable reverse-engineering knowledge model. |
| 05.1 | [Evidence and provenance](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.1-evidence-and-provenance/README.md) | Attach static observations, traces, memory diffs, screenshots, rebuild results and human assertions to claims. | Evidence records with immutable artifact references. |
| 05.2 | [Hypothesis lifecycle](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.2-hypothesis-lifecycle/README.md) | Represent proposed, competing, supported, contradicted, rejected, superseded and confirmed hypotheses. | Auditable semantic-claim lifecycle. |
| 05.3 | [Confidence and promotion policy](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.3-confidence-and-promotion-policy/README.md) | Define evidence grades and deterministic rules controlling when semantic names/claims may enter confirmed project state. | Machine-checkable guardrails against unsupported LLM assertions. |
| 05.4 | [Experiment specification and results](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/README.md) | Represent setup snapshot, interventions/stimuli, observations, expected discriminators and reproducible outcomes. | First-class experiment records independent of any LLM. |
| 05.5 | [Research frontier queries](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.5-research-frontier-queries/README.md) | Expose confirmed/likely/unknown/blocked/high-value regions and unresolved hypotheses for later orchestration. | Structured investigation backlog derived from project state. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level contract; each numbered subtask is independently assignable to
Copilot or another coding agent while preserving the distinction between deterministic observations,
evidence, hypotheses, experiments and confirmed knowledge.

## Milestone completion criteria

The project can distinguish facts from hypotheses, explain why every confirmed semantic claim is
believed, retain competing hypotheses, and reproduce the experiment/evidence history that led to a
conclusion.

## Non-goals

- Automatic hypothesis generation.
- Model-specific prompting.
- A general probabilistic inference engine.

## Dependency and sequencing notes

Begin this milestone after the core outputs required from [Milestone
0004](/docs/roadmap/0004-emulator-automation-and-runtime-evidence/plan.md) are available. Later
milestones may be designed in parallel, but implementation should not bypass missing
deterministic/evidence foundations from earlier milestones.
