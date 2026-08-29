# Task 01.0 - Repository and Development Foundation

## Story

Create the initial GitHub repository scaffold for ZXRE so a coding agent can clone the repository,
install all dependencies, run the CLI stub, execute tests, lint/type-check the project, build
documentation-quality checks, and continue development without manual setup.  This is the **repo-
bootstrap story**. It must establish conventions that later stories can rely on, but it must not
prematurely implement reverse-engineering domain behavior.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Initialize Python project and package layout | [01-initialize-python-project-and-package-layout.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/01-initialize-python-project-and-package-layout.md) | ⬜ Not started |
| 02 | Configure Ruff, MyPy and Pytest | [02-configure-ruff-mypy-and-pytest.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/02-configure-ruff-mypy-and-pytest.md) | ⬜ Not started |
| 03 | Add repository hygiene and GitHub metadata | [03-add-repository-hygiene-and-github-metadata.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/03-add-repository-hygiene-and-github-metadata.md) | ⬜ Not started |
| 04 | Create CI workflow | [04-create-ci-workflow.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/04-create-ci-workflow.md) | ⬜ Not started |
| 05 | Establish documentation and roadmap conventions | [05-establish-documentation-and-roadmap-conventions.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/05-establish-documentation-and-roadmap-conventions.md) | ⬜ Not started |
| 06 | Add pre-commit or equivalent local quality hook | [06-add-pre-commit-or-equivalent-local-quality-hook.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/06-add-pre-commit-or-equivalent-local-quality-hook.md) | ⬜ Not started |
| 07 | Bootstrap verification and handoff | [07-bootstrap-verification-and-handoff.md](/docs/roadmap/0001-core-architecture-and-project-model/01.0-repository-and-development-foundation/07-bootstrap-verification-and-handoff.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless the current repository state makes two clearly independent.
- A coding agent should read this task README, the milestone
  [plan.md](/docs/roadmap/0001-core-architecture-and-project-model/plan.md), and the specific subtask
  file before modifying code.
- Do not pre-implement later tasks merely to make an abstraction look more general.
- Every subtask should leave the repository passing all quality gates established by Task 01.0.

## Task completion criteria

All subtasks are complete, their tests and documentation are present, and the task's output described
in the milestone plan is demonstrably usable from a fresh clone.
