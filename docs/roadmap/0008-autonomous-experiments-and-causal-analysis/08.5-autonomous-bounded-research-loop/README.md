# Task 08.5 - Autonomous Bounded Research Loop

## Story

Allow the Investigator to iterate hypothesis → experiment design → feasibility validation →
execution → evidence → critic review → policy evaluation for a narrowly stated goal under explicit
budgets and stopping rules.  The loop must be resumable from canonical project state, safe against
repeated destructive mutation, and able to terminate with `unresolved` rather than manufacturing a
conclusion.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define autonomous research goal and budget model | [01-define-autonomous-research-goal-and-budget-model.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/01-define-autonomous-research-goal-and-budget-model.md) | ⬜ Not started |
| 02 | Define research-loop state machine | [02-define-research-loop-state-machine.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/02-define-research-loop-state-machine.md) | ⬜ Not started |
| 03 | Implement budget accounting | [03-implement-budget-accounting.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/03-implement-budget-accounting.md) | ⬜ Not started |
| 04 | Implement canonical checkpoint/resume | [04-implement-canonical-checkpoint-resume.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/04-implement-canonical-checkpoint-resume.md) | ⬜ Not started |
| 05 | Implement Investigator loop coordinator | [05-implement-investigator-loop-coordinator.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/05-implement-investigator-loop-coordinator.md) | ⬜ Not started |
| 06 | Define agent decision schema | [06-define-agent-decision-schema.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/06-define-agent-decision-schema.md) | ⬜ Not started |
| 07 | Implement loop safety/stop rules | [07-implement-loop-safety-stop-rules.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/07-implement-loop-safety-stop-rules.md) | ⬜ Not started |
| 08 | Extend Investigator and Critic roles for autonomous mode | [08-extend-investigator-and-critic-roles-for-autonomous-mode.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/08-extend-investigator-and-critic-roles-for-autonomous-mode.md) | ⬜ Not started |
| 09 | Create bounded-research-loop Skill | [09-create-bounded-research-loop-skill.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/09-create-bounded-research-loop-skill.md) | ⬜ Not started |
| 10 | Expose autonomy MCP tools/resources | [10-expose-autonomy-mcp-tools-resources.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/10-expose-autonomy-mcp-tools-resources.md) | ⬜ Not started |
| 11 | Add autonomous player-X acceptance scenario | [11-add-autonomous-player-x-acceptance-scenario.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/11-add-autonomous-player-x-acceptance-scenario.md) | ⬜ Not started |
| 12 | Add autonomous collision-routine acceptance scenario | [12-add-autonomous-collision-routine-acceptance-scenario.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/12-add-autonomous-collision-routine-acceptance-scenario.md) | ⬜ Not started |
| 13 | Add failure/unresolved acceptance scenarios | [13-add-failure-unresolved-acceptance-scenarios.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/13-add-failure-unresolved-acceptance-scenarios.md) | ⬜ Not started |
| 14 | Document autonomous research operation | [14-document-autonomous-research-operation.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.5-autonomous-bounded-research-loop/14-document-autonomous-research-operation.md) | ⬜ Not started |

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
