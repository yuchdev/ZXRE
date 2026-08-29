# Task 06.1 - Project-Aware Deterministic Tool Surface

## Story

Expose bounded, composable MCP tools over deterministic ZXRE services. Runtime operations use the
generic emulator interface; no raw ZRCP or monolithic reverse-engineer-game tool is allowed.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define MCP tool naming and schema conventions | [01-define-mcp-tool-naming-and-schema-conventions.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/01-define-mcp-tool-naming-and-schema-conventions.md) | ⬜ Not started |
| 02 | Implement project and artifact tools | [02-implement-project-and-artifact-tools.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/02-implement-project-and-artifact-tools.md) | ⬜ Not started |
| 03 | Implement tape and loader tools | [03-implement-tape-and-loader-tools.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/03-implement-tape-and-loader-tools.md) | ⬜ Not started |
| 04 | Implement snapshot and memory tools | [04-implement-snapshot-and-memory-tools.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/04-implement-snapshot-and-memory-tools.md) | ⬜ Not started |
| 05 | Implement static-analysis and reconstruction tools | [05-implement-static-analysis-and-reconstruction-tools.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/05-implement-static-analysis-and-reconstruction-tools.md) | ⬜ Not started |
| 06 | Implement runtime and trace tools | [06-implement-runtime-and-trace-tools.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/06-implement-runtime-and-trace-tools.md) | ⬜ Not started |
| 07 | Implement evidence, hypothesis, experiment and frontier tools | [07-implement-evidence-hypothesis-experiment-and-frontier-tools.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/07-implement-evidence-hypothesis-experiment-and-frontier-tools.md) | ⬜ Not started |
| 08 | Add tool authorization/safety boundaries | [08-add-tool-authorization-safety-boundaries.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/08-add-tool-authorization-safety-boundaries.md) | ⬜ Not started |
| 09 | Add MCP tool contract tests | [09-add-mcp-tool-contract-tests.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/09-add-mcp-tool-contract-tests.md) | ⬜ Not started |
| 10 | Document tool catalog | [10-document-tool-catalog.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.1-project-aware-deterministic-tool-surface/10-document-tool-catalog.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
