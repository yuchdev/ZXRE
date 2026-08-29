# Task 05.4 - Experiment Specification and Results

## Story

Represent reproducible reverse-engineering experiments independently of any LLM. An experiment
specifies a starting machine state, controlled stimuli/interventions, observations, expected
discriminators and actual results. The model must support later automated experiment design while
already being useful to humans and deterministic test harnesses.  This task models experiments; it
does not autonomously invent them.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define experiment domain model | [01-define-experiment-domain-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/01-define-experiment-domain-model.md) | ⬜ Not started |
| 02 | Define setup and starting-state model | [02-define-setup-and-starting-state-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/02-define-setup-and-starting-state-model.md) | ⬜ Not started |
| 03 | Define stimulus/intervention model | [03-define-stimulus-intervention-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/03-define-stimulus-intervention-model.md) | ⬜ Not started |
| 04 | Define expected discriminator/assertion model | [04-define-expected-discriminator-assertion-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/04-define-expected-discriminator-assertion-model.md) | ⬜ Not started |
| 05 | Implement experiment runner | [05-implement-experiment-runner.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/05-implement-experiment-runner.md) | ⬜ Not started |
| 06 | Implement experiment result serialization | [06-implement-experiment-result-serialization.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/06-implement-experiment-result-serialization.md) | ⬜ Not started |
| 07 | Link experiment results to evidence and hypotheses | [07-link-experiment-results-to-evidence-and-hypotheses.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/07-link-experiment-results-to-evidence-and-hypotheses.md) | ⬜ Not started |
| 08 | Add deterministic fake-backend experiment tests | [08-add-deterministic-fake-backend-experiment-tests.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/08-add-deterministic-fake-backend-experiment-tests.md) | ⬜ Not started |
| 09 | Document experiment model | [09-document-experiment-model.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/05.4-experiment-specification-and-results/09-document-experiment-model.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless the repository state clearly permits safe parallel work.
- Read the Milestone 0005
  [plan.md](/docs/roadmap/0005-knowledge-evidence-and-experiment-model/plan.md), this README and the
  chosen subtask before implementation.
- Treat deterministic observations, evidence, hypotheses and confirmed knowledge as distinct layers.
- Prefer explicit state transitions and audit records over mutable status flags with hidden history.
- Do not pre-implement Milestone 0006 agent/MCP behavior or Milestone 0008 autonomous experiment
  planning.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output can be demonstrated entirely
without an LLM or agent harness.
