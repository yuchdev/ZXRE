# Task 08.4 - Information-Gain Research Frontier

## Story

Extend the deterministic research frontier with agent-estimated expected information gain,
experiment cost and dependency unlock value. This lets the Investigator choose productive next work
rather than scanning addresses or hypotheses sequentially.  Model estimates are advisory and
auditable; they do not alter facts, evidence grades or confirmation rules.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define information-gain assessment model | [01-define-information-gain-assessment-model.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/01-define-information-gain-assessment-model.md) | ⬜ Not started |
| 02 | Define experiment-to-frontier linkage | [02-define-experiment-to-frontier-linkage.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/02-define-experiment-to-frontier-linkage.md) | ⬜ Not started |
| 03 | Implement deterministic baseline value signals | [03-implement-deterministic-baseline-value-signals.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/03-implement-deterministic-baseline-value-signals.md) | ⬜ Not started |
| 04 | Implement advisory agent scoring interface | [04-implement-advisory-agent-scoring-interface.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/04-implement-advisory-agent-scoring-interface.md) | ⬜ Not started |
| 05 | Implement composite prioritization policy | [05-implement-composite-prioritization-policy.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/05-implement-composite-prioritization-policy.md) | ⬜ Not started |
| 06 | Implement anti-loop/diversity penalties | [06-implement-anti-loop-diversity-penalties.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/06-implement-anti-loop-diversity-penalties.md) | ⬜ Not started |
| 07 | Create choose-next-investigation Skill | [07-create-choose-next-investigation-skill.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/07-create-choose-next-investigation-skill.md) | ⬜ Not started |
| 08 | Expose ranked frontier MCP resource | [08-expose-ranked-frontier-mcp-resource.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/08-expose-ranked-frontier-mcp-resource.md) | ⬜ Not started |
| 09 | Add ranking regression tests | [09-add-ranking-regression-tests.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/09-add-ranking-regression-tests.md) | ⬜ Not started |
| 10 | Document information-gain frontier | [10-document-information-gain-frontier.md](/docs/roadmap/0008-autonomous-experiments-and-causal-analysis/08.4-information-gain-research-frontier/10-document-information-gain-frontier.md) | ⬜ Not started |

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
