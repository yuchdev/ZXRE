# Task 06.3 - External-Tool Capability and Provenance Rules

## Story

Formalize how optional external debugger MCPs coexist with ZXRE. Direct companion-tool calls remain
exploratory until observations are imported or reproduced through canonical ZXRE services.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Expose companion integration descriptors through ZXRE | [01-expose-companion-integration-descriptors-through-zxre.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/01-expose-companion-integration-descriptors-through-zxre.md) | ⬜ Not started |
| 02 | Define canonicalization status model | [02-define-canonicalization-status-model.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/02-define-canonicalization-status-model.md) | ⬜ Not started |
| 03 | Implement external observation import tool | [03-implement-external-observation-import-tool.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/03-implement-external-observation-import-tool.md) | ⬜ Not started |
| 04 | Implement reproduce-through-ZXRE workflow helper | [04-implement-reproduce-through-zxre-workflow-helper.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/04-implement-reproduce-through-zxre-workflow-helper.md) | ⬜ Not started |
| 05 | Define Skills-facing preference rules | [05-define-skills-facing-preference-rules.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/05-define-skills-facing-preference-rules.md) | ⬜ Not started |
| 06 | Add zesarux-mcp mapping verification tests | [06-add-zesarux-mcp-mapping-verification-tests.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/06-add-zesarux-mcp-mapping-verification-tests.md) | ⬜ Not started |
| 07 | Add generic second-companion fixture | [07-add-generic-second-companion-fixture.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/07-add-generic-second-companion-fixture.md) | ⬜ Not started |
| 08 | Document provenance boundary | [08-document-provenance-boundary.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.3-external-tool-capability-and-provenance-rules/08-document-provenance-boundary.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
