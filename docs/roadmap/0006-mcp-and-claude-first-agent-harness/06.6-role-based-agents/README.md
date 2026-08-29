# Task 06.6 - Role-Based Agents

## Story

Define a small set of reasoning roles separated by analytical perspective rather than command
wrapping. Durable hypotheses/evidence remain the shared state between agents.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define canonical agent-role schema | [01-define-canonical-agent-role-schema.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/01-define-canonical-agent-role-schema.md) | ⬜ Not started |
| 02 | Create Investigator role | [02-create-investigator-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/02-create-investigator-role.md) | ⬜ Not started |
| 03 | Create Loader Analyst role | [03-create-loader-analyst-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/03-create-loader-analyst-role.md) | ⬜ Not started |
| 04 | Create Static Analyst role | [04-create-static-analyst-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/04-create-static-analyst-role.md) | ⬜ Not started |
| 05 | Create Dynamic Analyst role | [05-create-dynamic-analyst-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/05-create-dynamic-analyst-role.md) | ⬜ Not started |
| 06 | Create Asset Analyst role | [06-create-asset-analyst-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/06-create-asset-analyst-role.md) | ⬜ Not started |
| 07 | Create Reconstruction Agent role | [07-create-reconstruction-agent-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/07-create-reconstruction-agent-role.md) | ⬜ Not started |
| 08 | Create Critic/Verifier role | [08-create-critic-verifier-role.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/08-create-critic-verifier-role.md) | ⬜ Not started |
| 09 | Create Claude Code agent adapters | [09-create-claude-code-agent-adapters.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/09-create-claude-code-agent-adapters.md) | ⬜ Not started |
| 10 | Add agent-role conformance tests | [10-add-agent-role-conformance-tests.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/10-add-agent-role-conformance-tests.md) | ⬜ Not started |
| 11 | Document multi-agent collaboration pattern | [11-document-multi-agent-collaboration-pattern.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.6-role-based-agents/11-document-multi-agent-collaboration-pattern.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
