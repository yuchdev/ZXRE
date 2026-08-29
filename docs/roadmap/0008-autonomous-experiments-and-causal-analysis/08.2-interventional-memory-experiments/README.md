# Task 08.2 - Interventional Memory Experiments

## Story

Add controlled memory interventions that modify candidate state from a reproducible snapshot and
observe downstream machine/screen behavior. Interventions provide stronger causal evidence than
passive correlation, but must be tightly bounded, restored between trials and recorded in full.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define intervention model | [01-define-intervention-model.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/01-define-intervention-model.md) | ⬜ Not started |
| 02 | Define writable-scope safety policy | [02-define-writable-scope-safety-policy.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/02-define-writable-scope-safety-policy.md) | ⬜ Not started |
| 03 | Implement snapshot-restore trial runner | [03-implement-snapshot-restore-trial-runner.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/03-implement-snapshot-restore-trial-runner.md) | ⬜ Not started |
| 04 | Implement scalar poke sweep | [04-implement-scalar-poke-sweep.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/04-implement-scalar-poke-sweep.md) | ⬜ Not started |
| 05 | Implement paired intervention/control trials | [05-implement-paired-intervention-control-trials.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/05-implement-paired-intervention-control-trials.md) | ⬜ Not started |
| 06 | Implement causal evidence generator | [06-implement-causal-evidence-generator.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/06-implement-causal-evidence-generator.md) | ⬜ Not started |
| 07 | Create poke-candidate-variable Skill | [07-create-poke-candidate-variable-skill.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/07-create-poke-candidate-variable-skill.md) | ⬜ Not started |
| 08 | Expose bounded intervention MCP tools | [08-expose-bounded-intervention-mcp-tools.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/08-expose-bounded-intervention-mcp-tools.md) | ⬜ Not started |
| 09 | Add synthetic causal-variable scenario | [09-add-synthetic-causal-variable-scenario.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/09-add-synthetic-causal-variable-scenario.md) | ⬜ Not started |
| 10 | Document intervention rules | [10-document-intervention-rules.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.2-interventional-memory-experiments/10-document-intervention-rules.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone
  [plan.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/plan.md), this README and
  the selected subtask before implementation.
- Prefer the lowest-cost falsifiable experiment that distinguishes current hypotheses.
- Restore controlled state before intervention trials and retain all observations, including failures.
- Autonomous mode must stop cleanly when evidence is insufficient or budget/risk guards are reached.
- Do not pre-implement Milestone 0009 semantic source refactoring or Milestone 0010 cross-harness/model
  routing.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task can be exercised through canonical
ZXRE experiment/evidence state without relying on hidden agent conversation history.
