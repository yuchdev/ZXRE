# Task 10.2 - Portable Skill/Procedure Packaging

## Story

Separate reusable investigation procedures from Claude-specific Skill packaging. Canonical
procedures should express goals, prerequisites, required ZXRE capabilities, steps, evidence rules
and exit conditions; each harness receives only a thin representation appropriate to its native
mechanism.  Procedure definitions must not depend on raw emulator-MCP vocabulary.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define canonical procedure schema | [01-define-canonical-procedure-schema.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/01-define-canonical-procedure-schema.md) | ⬜ Not started |
| 02 | Create canonical procedure source tree | [02-create-canonical-procedure-source-tree.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/02-create-canonical-procedure-source-tree.md) | ⬜ Not started |
| 03 | Implement Claude Skill renderer | [03-implement-claude-skill-renderer.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/03-implement-claude-skill-renderer.md) | ⬜ Not started |
| 04 | Implement second-harness procedure renderer | [04-implement-second-harness-procedure-renderer.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/04-implement-second-harness-procedure-renderer.md) | ⬜ Not started |
| 05 | Implement procedure portability linter | [05-implement-procedure-portability-linter.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/05-implement-procedure-portability-linter.md) | ⬜ Not started |
| 06 | Implement procedure versioning | [06-implement-procedure-versioning.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/06-implement-procedure-versioning.md) | ⬜ Not started |
| 07 | Add procedure equivalence tests | [07-add-procedure-equivalence-tests.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/07-add-procedure-equivalence-tests.md) | ⬜ Not started |
| 08 | Migrate Milestone 0006/0008 Skills to canonical procedures | [08-migrate-milestone-0006-0008-skills-to-canonical-procedures.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/08-migrate-milestone-0006-0008-skills-to-canonical-procedures.md) | ⬜ Not started |
| 09 | Document portable procedure authoring | [09-document-portable-procedure-authoring.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.2-portable-skill-procedure-packaging/09-document-portable-procedure-authoring.md) | ⬜ Not started |

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
