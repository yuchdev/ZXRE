# Task 03.1 - Code/Data Control Map

## Story

Implement an explicit, editable classification map describing how address ranges should be
interpreted during static analysis and reconstruction. The map must separate deterministic region
classification from semantic meaning: code, raw bytes, words, text or unknown are representation
choices, not statements about gameplay purpose.  The control map becomes the authoritative input for
faithful source generation.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define control-map domain model | [01-define-control-map-domain-model.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/01-define-control-map-domain-model.md) | ⬜ Not started |
| 02 | Implement control-map validation and interval operations | [02-implement-control-map-validation-and-interval-operations.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/02-implement-control-map-validation-and-interval-operations.md) | ⬜ Not started |
| 03 | Generate initial control map from explicit loader/snapshot facts | [03-generate-initial-control-map-from-explicit-loader-snapshot-facts.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/03-generate-initial-control-map-from-explicit-loader-snapshot-facts.md) | ⬜ Not started |
| 04 | Import/export SkoolKit control files optionally | [04-import-export-skoolkit-control-files-optionally.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/04-import-export-skoolkit-control-files-optionally.md) | ⬜ Not started |
| 05 | Persist control map | [05-persist-control-map.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/05-persist-control-map.md) | ⬜ Not started |
| 06 | Integrate control map with disassembly service | [06-integrate-control-map-with-disassembly-service.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/06-integrate-control-map-with-disassembly-service.md) | ⬜ Not started |
| 07 | Add manual classification service APIs | [07-add-manual-classification-service-apis.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/07-add-manual-classification-service-apis.md) | ⬜ Not started |
| 08 | Document control-map semantics | [08-document-control-map-semantics.md](/docs/roadmap/0003-static-analysis-and-byte-exact-reconstruction/03.1-code-data-control-map/08-document-control-map-semantics.md) | ⬜ Not started |

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
