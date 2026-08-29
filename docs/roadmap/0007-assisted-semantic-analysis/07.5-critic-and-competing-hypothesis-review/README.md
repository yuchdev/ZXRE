# Task 07.5 - Critic and Competing-Hypothesis Review

## Story

Systematically challenge high-impact semantic conclusions before they harden into project knowledge.
The Critic/Verifier should surface weak provenance, circular reasoning, alternative interpretations
and missing discriminating evidence, and feed those gaps back into the research frontier.  This task
improves epistemic quality without yet introducing Milestone 0008's autonomous information- gain
experiment planner.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define semantic review model | [01-define-semantic-review-model.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/01-define-semantic-review-model.md) | ⬜ Not started |
| 02 | Implement deterministic review prechecks | [02-implement-deterministic-review-prechecks.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/02-implement-deterministic-review-prechecks.md) | ⬜ Not started |
| 03 | Implement competing-alternative helper | [03-implement-competing-alternative-helper.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/03-implement-competing-alternative-helper.md) | ⬜ Not started |
| 04 | Implement Critic review service | [04-implement-critic-review-service.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/04-implement-critic-review-service.md) | ⬜ Not started |
| 05 | Extend Critic/Verifier agent definition | [05-extend-critic-verifier-agent-definition.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/05-extend-critic-verifier-agent-definition.md) | ⬜ Not started |
| 06 | Create review-high-impact-hypothesis Skill | [06-create-review-high-impact-hypothesis-skill.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/06-create-review-high-impact-hypothesis-skill.md) | ⬜ Not started |
| 07 | Integrate reviews with research frontier | [07-integrate-reviews-with-research-frontier.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/07-integrate-reviews-with-research-frontier.md) | ⬜ Not started |
| 08 | Expose semantic-review MCP tools/resources | [08-expose-semantic-review-mcp-tools-resources.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/08-expose-semantic-review-mcp-tools-resources.md) | ⬜ Not started |
| 09 | Add adversarial semantic-analysis regression cases | [09-add-adversarial-semantic-analysis-regression-cases.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/09-add-adversarial-semantic-analysis-regression-cases.md) | ⬜ Not started |
| 10 | Add Milestone 0007 semantic acceptance scenario | [10-add-milestone-0007-semantic-acceptance-scenario.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/10-add-milestone-0007-semantic-acceptance-scenario.md) | ⬜ Not started |
| 11 | Document semantic review process | [11-document-semantic-review-process.md](/docs/roadmap/0007-assisted-semantic-analysis/07.5-critic-and-competing-hypothesis-review/11-document-semantic-review-process.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0007-assisted-semantic-analysis/plan.md), this README and
  the selected subtask first.
- Start from deterministic/static/runtime facts and canonical evidence; let agents add interpretation as
  explicit hypotheses.
- Keep confirmed and proposed semantic state visibly distinct in services, MCP resources and reports.
- Do not pre-implement autonomous research loops or semantic source refactoring from later milestones.

## Task completion criteria

All subtasks are complete, tests/docs are present, and semantic outputs are reproducible as canonical
ZXRE hypotheses/knowledge state with evidence and uncertainty preserved.
