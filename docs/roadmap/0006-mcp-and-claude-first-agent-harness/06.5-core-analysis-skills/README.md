# Task 06.5 - Core Analysis Skills

## Story

Encode reusable reverse-engineering procedures as Skills. Skills orchestrate ZXRE tools/resources;
they do not implement deterministic logic and must avoid emulator-specific tool vocabularies.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Establish Skill packaging convention | [01-establish-skill-packaging-convention.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/01-establish-skill-packaging-convention.md) | ⬜ Not started |
| 02 | Create analyze-tape-loader Skill | [02-create-analyze-tape-loader-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/02-create-analyze-tape-loader-skill.md) | ⬜ Not started |
| 03 | Create locate-real-entry-point Skill | [03-create-locate-real-entry-point-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/03-create-locate-real-entry-point-skill.md) | ⬜ Not started |
| 04 | Create analyze-routine Skill | [04-create-analyze-routine-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/04-create-analyze-routine-skill.md) | ⬜ Not started |
| 05 | Create classify-code-data Skill | [05-create-classify-code-data-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/05-create-classify-code-data-skill.md) | ⬜ Not started |
| 06 | Create test-variable-hypothesis Skill | [06-create-test-variable-hypothesis-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/06-create-test-variable-hypothesis-skill.md) | ⬜ Not started |
| 07 | Create reconstruct-and-verify Skill | [07-create-reconstruct-and-verify-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/07-create-reconstruct-and-verify-skill.md) | ⬜ Not started |
| 08 | Create hypothesis-review Skill | [08-create-hypothesis-review-skill.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/08-create-hypothesis-review-skill.md) | ⬜ Not started |
| 09 | Add Skill validation tests | [09-add-skill-validation-tests.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/09-add-skill-validation-tests.md) | ⬜ Not started |
| 10 | Document Skill authoring guidelines | [10-document-skill-authoring-guidelines.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/06.5-core-analysis-skills/10-document-skill-authoring-guidelines.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is obvious.
- Read the milestone [plan.md](/docs/roadmap/0006-mcp-and-claude-first-agent-harness/plan.md), this README and selected subtask first.
- Keep canonical state in ZXRE services/stores; prompts, Skills and agent conversations are not the database.
- Prefer MCP resources for compact context and tools for bounded operations.
- Do not pre-implement Milestone 0008 autonomous research loops or Milestone 0010 full cross-harness abstraction.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task is usable through Claude Code without introducing a Claude-specific dependency into ZXRE core.
