# Task 06.4 - Claude Project Instructions and Guardrails

## Story

Create Claude Code-specific project instructions that teach correct ZXRE usage while keeping all
critical policy enforcement in the core rather than prompts.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Create root CLAUDE.md | [01-create-root-claude-md.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/01-create-root-claude-md.md) | ⬜ Not started |
| 02 | Define epistemic guardrails section | [02-define-epistemic-guardrails-section.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/02-define-epistemic-guardrails-section.md) | ⬜ Not started |
| 03 | Define runtime/debugger guardrails | [03-define-runtime-debugger-guardrails.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/03-define-runtime-debugger-guardrails.md) | ⬜ Not started |
| 04 | Define context-efficiency rules | [04-define-context-efficiency-rules.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/04-define-context-efficiency-rules.md) | ⬜ Not started |
| 05 | Define verification-before-write rules | [05-define-verification-before-write-rules.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/05-define-verification-before-write-rules.md) | ⬜ Not started |
| 06 | Define repository modification rules | [06-define-repository-modification-rules.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/06-define-repository-modification-rules.md) | ⬜ Not started |
| 07 | Add Claude instruction lint/check | [07-add-claude-instruction-lint-check.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/07-add-claude-instruction-lint-check.md) | ⬜ Not started |
| 08 | Document Claude adapter status | [08-document-claude-adapter-status.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.4-claude-project-instructions-and-guardrails/08-document-claude-adapter-status.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
