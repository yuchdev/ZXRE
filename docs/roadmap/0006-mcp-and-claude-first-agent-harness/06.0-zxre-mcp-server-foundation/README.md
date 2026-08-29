# Task 06.0 - ZXRE MCP Server Foundation

## Story

Create the first project-aware MCP server over existing ZXRE services. It must validate requests,
resolve project context, delegate to core services, return structured results, and remain harness-
neutral.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Select MCP SDK and define server package layout | [01-select-mcp-sdk-and-define-server-package-layout.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/01-select-mcp-sdk-and-define-server-package-layout.md) | ⬜ Not started |
| 02 | Define MCP server configuration | [02-define-mcp-server-configuration.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/02-define-mcp-server-configuration.md) | ⬜ Not started |
| 03 | Implement stdio server entry point | [03-implement-stdio-server-entry-point.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/03-implement-stdio-server-entry-point.md) | ⬜ Not started |
| 04 | Implement project-context resolver | [04-implement-project-context-resolver.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/04-implement-project-context-resolver.md) | ⬜ Not started |
| 05 | Define MCP error mapping | [05-define-mcp-error-mapping.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/05-define-mcp-error-mapping.md) | ⬜ Not started |
| 06 | Define common result/serialization helpers | [06-define-common-result-serialization-helpers.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/06-define-common-result-serialization-helpers.md) | ⬜ Not started |
| 07 | Add server lifecycle and graceful shutdown tests | [07-add-server-lifecycle-and-graceful-shutdown-tests.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/07-add-server-lifecycle-and-graceful-shutdown-tests.md) | ⬜ Not started |
| 08 | Document MCP server architecture | [08-document-mcp-server-architecture.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.0-zxre-mcp-server-foundation/08-document-mcp-server-architecture.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
