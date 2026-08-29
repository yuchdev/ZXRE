# Task 10.6 - Cross-Harness and Companion-Tool Regression Scenarios

## Story

Build a portability benchmark that runs identical bounded goals through supported harnesses, with
and without companion debugger MCPs, then compares canonical evidence/results, cost diagnostics and
reproducibility. Correctness is defined by ZXRE project state, not by matching prose or identical
tool sequences.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define portability benchmark model | [01-define-portability-benchmark-model.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/01-define-portability-benchmark-model.md) | ⬜ Not started |
| 02 | Select benchmark scenarios | [02-select-benchmark-scenarios.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/02-select-benchmark-scenarios.md) | ⬜ Not started |
| 03 | Implement canonical project reset/clone helper | [03-implement-canonical-project-reset-clone-helper.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/03-implement-canonical-project-reset-clone-helper.md) | ⬜ Not started |
| 04 | Implement harness run manifest | [04-implement-harness-run-manifest.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/04-implement-harness-run-manifest.md) | ⬜ Not started |
| 05 | Implement canonical result comparator | [05-implement-canonical-result-comparator.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/05-implement-canonical-result-comparator.md) | ⬜ Not started |
| 06 | Collect portability metrics | [06-collect-portability-metrics.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/06-collect-portability-metrics.md) | ⬜ Not started |
| 07 | Add with/without companion variants | [07-add-with-without-companion-variants.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/07-add-with-without-companion-variants.md) | ⬜ Not started |
| 08 | Generate benchmark report | [08-generate-benchmark-report.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/08-generate-benchmark-report.md) | ⬜ Not started |
| 09 | Add manual/CI benchmark profiles | [09-add-manual-ci-benchmark-profiles.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/09-add-manual-ci-benchmark-profiles.md) | ⬜ Not started |
| 10 | Document portability benchmark | [10-document-portability-benchmark.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.6-cross-harness-and-companion-tool-regression-scenarios/10-document-portability-benchmark.md) | ⬜ Not started |

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
