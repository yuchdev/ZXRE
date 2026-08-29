# Task 03.5 - Static Analysis Reports

## Story

Produce concise deterministic reports that summarize what static analysis knows: classified
coverage, unresolved ranges, direct references, routine candidates and reconstruction verification.
Reports should help humans and later agents navigate the project without becoming a second source of
truth.  Canonical data remains in structured project state; reports are generated views.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define report summary model | [01-define-report-summary-model.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/01-define-report-summary-model.md) | ⬜ Not started |
| 02 | Implement coverage statistics | [02-implement-coverage-statistics.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/02-implement-coverage-statistics.md) | ⬜ Not started |
| 03 | Implement static-analysis textual report | [03-implement-static-analysis-textual-report.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/03-implement-static-analysis-textual-report.md) | ⬜ Not started |
| 04 | Implement machine-readable report | [04-implement-machine-readable-report.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/04-implement-machine-readable-report.md) | ⬜ Not started |
| 05 | Register reports as generated artifacts | [05-register-reports-as-generated-artifacts.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/05-register-reports-as-generated-artifacts.md) | ⬜ Not started |
| 06 | Add report consistency tests | [06-add-report-consistency-tests.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/06-add-report-consistency-tests.md) | ⬜ Not started |
| 07 | Add Milestone 0003 inspection command extensions | [07-add-milestone-0003-inspection-command-extensions.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/07-add-milestone-0003-inspection-command-extensions.md) | ⬜ Not started |
| 08 | Update documentation and milestone status | [08-update-documentation-and-milestone-status.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.5-static-analysis-reports/08-update-documentation-and-milestone-status.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless repository state makes safe parallel work obvious.
- Read the Milestone 0003
  [plan.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/plan.md), this
  README and the selected subtask before implementation.
- Static analysis may produce candidates (e.g. routine starts) only when the candidate nature is
  explicit. Do not turn heuristics into confirmed semantics.
- Generated assembly must favor exact byte reconstruction over readability.
- Do not pre-implement Milestone 0004 runtime evidence or Milestone 0007 semantic analysis.

## Task completion criteria

All subtasks are complete, tests and docs are present, and the task output is reproducible from a
fresh clone with documented optional external tools.
