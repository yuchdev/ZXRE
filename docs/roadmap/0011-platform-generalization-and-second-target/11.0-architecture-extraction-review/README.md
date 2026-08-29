# Task 11.0 - Architecture Extraction Review

## Story

Audit the completed ZX Spectrum implementation for assumptions that accidentally became global: Z80
address semantics, Spectrum screen layout, TAP/TZX loaders, ZEsarUX/ZRCP behavior, `zesarux-mcp`
naming, assembler dialects and Claude-era procedure assumptions. Classify each assumption as
genuinely generic, ZX-platform-specific, adapter-specific or harness-specific before generalizing
anything.  This review must produce concrete refactoring requirements driven by the selected second
target.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Select the constrained second target | [01-select-the-constrained-second-target.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/01-select-the-constrained-second-target.md) | ⬜ Not started |
| 02 | Create architecture dependency inventory | [02-create-architecture-dependency-inventory.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/02-create-architecture-dependency-inventory.md) | ⬜ Not started |
| 03 | Classify coupling findings | [03-classify-coupling-findings.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/03-classify-coupling-findings.md) | ⬜ Not started |
| 04 | Audit project/artifact/knowledge layers | [04-audit-project-artifact-knowledge-layers.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/04-audit-project-artifact-knowledge-layers.md) | ⬜ Not started |
| 05 | Audit static-analysis/reconstruction layers | [05-audit-static-analysis-reconstruction-layers.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/05-audit-static-analysis-reconstruction-layers.md) | ⬜ Not started |
| 06 | Audit runtime/input/display layers | [06-audit-runtime-input-display-layers.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/06-audit-runtime-input-display-layers.md) | ⬜ Not started |
| 07 | Audit Skills/agents/documentation | [07-audit-skills-agents-documentation.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/07-audit-skills-agents-documentation.md) | ⬜ Not started |
| 08 | Create constrained refactoring RFC | [08-create-constrained-refactoring-rfc.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/08-create-constrained-refactoring-rfc.md) | ⬜ Not started |
| 09 | Add architecture leakage regression checks | [09-add-architecture-leakage-regression-checks.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.0-architecture-extraction-review/09-add-architecture-leakage-regression-checks.md) | ⬜ Not started |

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
