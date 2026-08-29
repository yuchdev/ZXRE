# Task 10.5 - Multi-Agent Review Strategies

## Story

Support optional cooperative and competitive semantic review patterns for ambiguous, high-impact
claims: independent analyses, reciprocal criticism and moderator selection. These strategies operate
on hypotheses/evidence and may improve reasoning reliability, but cannot vote a claim into truth or
bypass deterministic promotion rules.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define review-strategy model | [01-define-review-strategy-model.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/01-define-review-strategy-model.md) | ⬜ Not started |
| 02 | Implement independent-analysis strategy | [02-implement-independent-analysis-strategy.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/02-implement-independent-analysis-strategy.md) | ⬜ Not started |
| 03 | Implement reciprocal-critic strategy | [03-implement-reciprocal-critic-strategy.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/03-implement-reciprocal-critic-strategy.md) | ⬜ Not started |
| 04 | Implement moderator/synthesis strategy | [04-implement-moderator-synthesis-strategy.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/04-implement-moderator-synthesis-strategy.md) | ⬜ Not started |
| 05 | Implement diversity and duplicate detection | [05-implement-diversity-and-duplicate-detection.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/05-implement-diversity-and-duplicate-detection.md) | ⬜ Not started |
| 06 | Integrate evidence/policy evaluation | [06-integrate-evidence-policy-evaluation.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/06-integrate-evidence-policy-evaluation.md) | ⬜ Not started |
| 07 | Add collaboration budgets | [07-add-collaboration-budgets.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/07-add-collaboration-budgets.md) | ⬜ Not started |
| 08 | Create multi-agent-review Skill | [08-create-multi-agent-review-skill.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/08-create-multi-agent-review-skill.md) | ⬜ Not started |
| 09 | Add adversarial review regression scenario | [09-add-adversarial-review-regression-scenario.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/09-add-adversarial-review-regression-scenario.md) | ⬜ Not started |
| 10 | Document collaboration strategies | [10-document-collaboration-strategies.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.5-multi-agent-review-strategies/10-document-collaboration-strategies.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/plan.md), this README and the selected
  subtask before implementation.
- Generalize only from concrete requirements demonstrated by supported harnesses/platforms.
- Preserve explicit capability discovery and graceful degradation where implementations differ.
- Canonical correctness is measured from ZXRE project state and deterministic verification, not
  harness prose or external-tool convenience.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is proven against the concrete
implementations selected by the milestone rather than hypothetical future integrations.
