# Task 11.6 - Cross-Platform Reconstruction Benchmark

## Story

Run comparable bounded reverse-engineering goals on ZX Spectrum and the second target to prove that
project/evidence/hypothesis/experiment/agent semantics survive a CPU, media format and emulator
change. The benchmark must also prove byte-exact mechanical reconstruction for both targets.
Success is architectural reuse with explicit platform plugins, not identical implementation details.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define cross-platform benchmark schema | [01-define-cross-platform-benchmark-schema.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/01-define-cross-platform-benchmark-schema.md) | ⬜ Not started |
| 02 | Prepare matched ZX and C64 synthetic fixtures | [02-prepare-matched-zx-and-c64-synthetic-fixtures.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/02-prepare-matched-zx-and-c64-synthetic-fixtures.md) | ⬜ Not started |
| 03 | Benchmark deterministic ingestion/loading | [03-benchmark-deterministic-ingestion-loading.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/03-benchmark-deterministic-ingestion-loading.md) | ⬜ Not started |
| 04 | Benchmark static analysis/reconstruction | [04-benchmark-static-analysis-reconstruction.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/04-benchmark-static-analysis-reconstruction.md) | ⬜ Not started |
| 05 | Benchmark runtime evidence | [05-benchmark-runtime-evidence.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/05-benchmark-runtime-evidence.md) | ⬜ Not started |
| 06 | Benchmark semantic hypothesis workflow | [06-benchmark-semantic-hypothesis-workflow.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/06-benchmark-semantic-hypothesis-workflow.md) | ⬜ Not started |
| 07 | Benchmark portable procedures/harnesses | [07-benchmark-portable-procedures-harnesses.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/07-benchmark-portable-procedures-harnesses.md) | ⬜ Not started |
| 08 | Compare architecture-specific code footprint | [08-compare-architecture-specific-code-footprint.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/08-compare-architecture-specific-code-footprint.md) | ⬜ Not started |
| 09 | Generate cross-platform benchmark report | [09-generate-cross-platform-benchmark-report.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/09-generate-cross-platform-benchmark-report.md) | ⬜ Not started |
| 10 | Add regression/CI profiles | [10-add-regression-ci-profiles.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/10-add-regression-ci-profiles.md) | ⬜ Not started |
| 11 | Finalize generalization documentation | [11-finalize-generalization-documentation.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.6-cross-platform-reconstruction-benchmark/11-finalize-generalization-documentation.md) | ⬜ Not started |

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
