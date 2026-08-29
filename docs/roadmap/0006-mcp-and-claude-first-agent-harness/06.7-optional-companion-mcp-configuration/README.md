# Task 06.7 - Optional Companion MCP Configuration

## Story

Document and validate side-by-side ZXRE MCP plus optional low-level debugger MCP configurations,
using `zesarux-mcp` as the reference without creating a mandatory MCP-to-MCP dependency.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define companion-MCP examples directory | [01-define-companion-mcp-examples-directory.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/01-define-companion-mcp-examples-directory.md) | ⬜ Not started |
| 02 | Create Claude Code dual-MCP example | [02-create-claude-code-dual-mcp-example.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/02-create-claude-code-dual-mcp-example.md) | ⬜ Not started |
| 03 | Create second-harness conceptual example | [03-create-second-harness-conceptual-example.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/03-create-second-harness-conceptual-example.md) | ⬜ Not started |
| 04 | Document shared-emulator lifecycle rules | [04-document-shared-emulator-lifecycle-rules.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/04-document-shared-emulator-lifecycle-rules.md) | ⬜ Not started |
| 05 | Define agent usage rules for companion MCP | [05-define-agent-usage-rules-for-companion-mcp.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/05-define-agent-usage-rules-for-companion-mcp.md) | ⬜ Not started |
| 06 | Add configuration validation script where practical | [06-add-configuration-validation-script-where-practical.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/06-add-configuration-validation-script-where-practical.md) | ⬜ Not started |
| 07 | Add fake alternative companion example | [07-add-fake-alternative-companion-example.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/07-add-fake-alternative-companion-example.md) | ⬜ Not started |
| 08 | Document troubleshooting | [08-document-troubleshooting.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.7-optional-companion-mcp-configuration/08-document-troubleshooting.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
