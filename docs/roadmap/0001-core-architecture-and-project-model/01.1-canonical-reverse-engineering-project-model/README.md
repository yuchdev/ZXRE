# Task 01.1 - Canonical Reverse-Engineering Project Model

## Story

Implement the canonical project model that all later deterministic tools and agents use. A ZXRE
project must have stable identity, explicit format/version metadata, imported inputs, logical
machine/address-space references, and durable analysis metadata without depending on tape parsers,
disassemblers, emulators, MCP, Claude, or SkoolKit.  This story defines **what a reverse-engineering
project is**, not how artifacts are physically content-addressed; detailed artifact/provenance
storage belongs to Task 01.2.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define project domain types | [01-define-project-domain-types.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/01-define-project-domain-types.md) | ⬜ Not started |
| 02 | Define versioned project manifest schema | [02-define-versioned-project-manifest-schema.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/02-define-versioned-project-manifest-schema.md) | ⬜ Not started |
| 03 | Implement project filesystem layout | [03-implement-project-filesystem-layout.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/03-implement-project-filesystem-layout.md) | ⬜ Not started |
| 04 | Implement project repository/store abstraction | [04-implement-project-repository-store-abstraction.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/04-implement-project-repository-store-abstraction.md) | ⬜ Not started |
| 05 | Model project inputs without parsing them | [05-model-project-inputs-without-parsing-them.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/05-model-project-inputs-without-parsing-them.md) | ⬜ Not started |
| 06 | Define symbol and analysis metadata store | [06-define-symbol-and-analysis-metadata-store.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/06-define-symbol-and-analysis-metadata-store.md) | ⬜ Not started |
| 07 | Add project-service facade | [07-add-project-service-facade.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/07-add-project-service-facade.md) | ⬜ Not started |
| 08 | Document project format | [08-document-project-format.md](/docs/roadmap/0001-core-architecture-and-project-model/01.1-canonical-reverse-engineering-project-model/08-document-project-format.md) | ⬜ Not started |

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
