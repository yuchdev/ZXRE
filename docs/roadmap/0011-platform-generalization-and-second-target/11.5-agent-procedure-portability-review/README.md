# Task 11.5 - Agent Procedure Portability Review

## Story

Run every major canonical procedure and role against the second target to identify what is
architecture-neutral, parameterizable or genuinely platform-specific. The result should be a
taxonomy and concrete procedure variants, not awkward generic instructions full of target
conditionals.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Create procedure portability matrix | [01-create-procedure-portability-matrix.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/01-create-procedure-portability-matrix.md) | ⬜ Not started |
| 02 | Review loader/media procedures | [02-review-loader-media-procedures.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/02-review-loader-media-procedures.md) | ⬜ Not started |
| 03 | Review routine/static-analysis procedures | [03-review-routine-static-analysis-procedures.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/03-review-routine-static-analysis-procedures.md) | ⬜ Not started |
| 04 | Review runtime/causal procedures | [04-review-runtime-causal-procedures.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/04-review-runtime-causal-procedures.md) | ⬜ Not started |
| 05 | Review graphics/asset procedures | [05-review-graphics-asset-procedures.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/05-review-graphics-asset-procedures.md) | ⬜ Not started |
| 06 | Review role definitions | [06-review-role-definitions.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/06-review-role-definitions.md) | ⬜ Not started |
| 07 | Implement procedure selection by platform | [07-implement-procedure-selection-by-platform.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/07-implement-procedure-selection-by-platform.md) | ⬜ Not started |
| 08 | Add cross-platform procedure lint/tests | [08-add-cross-platform-procedure-lint-tests.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/08-add-cross-platform-procedure-lint-tests.md) | ⬜ Not started |
| 09 | Document procedure taxonomy | [09-document-procedure-taxonomy.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.5-agent-procedure-portability-review/09-document-procedure-taxonomy.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0011-platform-generalization-and-second-target/plan.md), this README and the selected
  subtask before implementation.
- Generalize only from concrete requirements demonstrated by supported harnesses/platforms.
- Preserve explicit capability discovery and graceful degradation where implementations differ.
- Canonical correctness is measured from ZXRE project state and deterministic verification, not
  harness prose or external-tool convenience.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is proven against the concrete
implementations selected by the milestone rather than hypothetical future integrations.
