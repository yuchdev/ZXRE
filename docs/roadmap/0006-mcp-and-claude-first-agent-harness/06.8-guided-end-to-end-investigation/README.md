# Task 06.8 - Guided End-to-End Investigation

## Story

Prove the complete architecture on one bounded legal/synthetic Spectrum investigation, such as
finding the actual machine-code entry/main loop behind a bootstrap. Final success is measured from
canonical ZXRE state, not agent prose.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define legal deterministic investigation fixture | [01-define-legal-deterministic-investigation-fixture.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/01-define-legal-deterministic-investigation-fixture.md) | ⬜ Not started |
| 02 | Define investigation goal and acceptance contract | [02-define-investigation-goal-and-acceptance-contract.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/02-define-investigation-goal-and-acceptance-contract.md) | ⬜ Not started |
| 03 | Create initial project setup script | [03-create-initial-project-setup-script.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/03-create-initial-project-setup-script.md) | ⬜ Not started |
| 04 | Create guided investigation procedure | [04-create-guided-investigation-procedure.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/04-create-guided-investigation-procedure.md) | ⬜ Not started |
| 05 | Run canonical evidence workflow | [05-run-canonical-evidence-workflow.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/05-run-canonical-evidence-workflow.md) | ⬜ Not started |
| 06 | Require critic review and promotion evaluation | [06-require-critic-review-and-promotion-evaluation.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/06-require-critic-review-and-promotion-evaluation.md) | ⬜ Not started |
| 07 | Verify result against fixture ground truth | [07-verify-result-against-fixture-ground-truth.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/07-verify-result-against-fixture-ground-truth.md) | ⬜ Not started |
| 08 | Add optional companion-MCP variant | [08-add-optional-companion-mcp-variant.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/08-add-optional-companion-mcp-variant.md) | ⬜ Not started |
| 09 | Record cost/context/tool-use diagnostics | [09-record-cost-context-tool-use-diagnostics.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/09-record-cost-context-tool-use-diagnostics.md) | ⬜ Not started |
| 10 | Document Milestone 0006 demo | [10-document-milestone-0006-demo.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.8-guided-end-to-end-investigation/10-document-milestone-0006-demo.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
