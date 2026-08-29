# Task 06.2 - MCP Resource Surface

## Story

Expose compact addressable project context through MCP resources so agents can retrieve focused
state without repeatedly dumping large disassemblies, traces or artifact contents.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define resource URI scheme | [01-define-resource-uri-scheme.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/01-define-resource-uri-scheme.md) | ⬜ Not started |
| 02 | Implement project summary resource | [02-implement-project-summary-resource.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/02-implement-project-summary-resource.md) | ⬜ Not started |
| 03 | Implement memory-map and static-analysis resources | [03-implement-memory-map-and-static-analysis-resources.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/03-implement-memory-map-and-static-analysis-resources.md) | ⬜ Not started |
| 04 | Implement knowledge/evidence/hypothesis resources | [04-implement-knowledge-evidence-hypothesis-resources.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/04-implement-knowledge-evidence-hypothesis-resources.md) | ⬜ Not started |
| 05 | Implement trace and experiment resources | [05-implement-trace-and-experiment-resources.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/05-implement-trace-and-experiment-resources.md) | ⬜ Not started |
| 06 | Implement runtime capability resource | [06-implement-runtime-capability-resource.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/06-implement-runtime-capability-resource.md) | ⬜ Not started |
| 07 | Implement resource size limits and pagination | [07-implement-resource-size-limits-and-pagination.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/07-implement-resource-size-limits-and-pagination.md) | ⬜ Not started |
| 08 | Add stale-source/version indicators | [08-add-stale-source-version-indicators.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/08-add-stale-source-version-indicators.md) | ⬜ Not started |
| 09 | Add resource contract tests | [09-add-resource-contract-tests.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/09-add-resource-contract-tests.md) | ⬜ Not started |
| 10 | Document MCP resource catalog | [10-document-mcp-resource-catalog.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.2-mcp-resource-surface/10-document-mcp-resource-catalog.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
