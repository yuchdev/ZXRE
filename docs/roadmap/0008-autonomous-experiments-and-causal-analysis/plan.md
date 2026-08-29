# Milestone 0008 - Autonomous Experiments and Causal Analysis

**Status:** not started - see [status.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/status.md).

## Why this milestone exists

Make the LLM useful where deterministic tools alone cannot choose the next observation. Agents
design low-cost falsifiable experiments, replay them from stable snapshots and use differential or
interventional evidence to distinguish competing hypotheses.

## Tasks

| Task | Name | Scope | Output |
|---|---|---|---|
| 08.0 | [Experiment designer](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.0-experiment-designer/README.md) | Generate discriminating experiments from one or more unresolved hypotheses and available emulator controls. | Structured experiment plans with expected observations and falsification criteria. |
| 08.1 | [Differential memory experiments](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.1-differential-memory-experiments/README.md) | Automate before/after and repeated-intersection analysis for input, events and gameplay transitions. | Candidate state-variable discovery from controlled memory differences. |
| 08.2 | [Interventional memory experiments](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/README.md) | Safely poke candidate variables/ranges from reproducible snapshots and observe resulting machine/screen behavior. | Stronger causal evidence than passive correlation. |
| 08.3 | [Trace comparison and causal localization](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.3-trace-comparison-and-causal-localization/README.md) | Compare execution/memory traces between scenarios to localize routines responsible for observed behavior. | Scenario-linked causal candidates for code and state. |
| 08.4 | [Information-gain research frontier](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/README.md) | Rank unresolved questions/experiments by expected value, cost and ability to unlock additional structure. | Agent chooses productive next work rather than scanning addresses sequentially. |
| 08.5 | [Autonomous bounded research loop](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/README.md) | Allow the Investigator to iterate hypothesis → experiment → evidence → verification under explicit budgets and stopping rules. | Safe autonomous semantic discovery for narrowly stated goals. |

Task folders and implementation-ready subtask specifications for this milestone are now defined.
Each task `README.md` is a story-level causal-analysis contract; each numbered subtask is independently
assignable to Copilot or another coding agent while preserving reproducible snapshot restore,
falsifiable experiments, bounded intervention, evidence policy and explicit autonomous stopping rules.

## Milestone completion criteria

For a bounded question such as locating player X/Y or identifying a collision routine, the system
can autonomously design and run reproducible experiments, update competing hypotheses and reach an
evidence-backed result or explicitly report that the question remains unresolved.

## Non-goals

- Unbounded unattended reverse engineering.
- Replacing deterministic verification with model confidence.
- Arbitrary emulator mutation without restore/reproducibility rules.

## Dependency and sequencing notes

Begin this milestone after the core outputs required from [Milestone
0007](/docs/roadmap/0007-assisted-semantic-analysis/plan.md) are available. Later milestones may be
designed in parallel, but implementation should not bypass missing deterministic/evidence
foundations from earlier milestones.
