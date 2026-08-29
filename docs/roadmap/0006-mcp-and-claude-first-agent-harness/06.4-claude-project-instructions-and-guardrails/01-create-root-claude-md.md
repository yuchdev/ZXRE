# Task 06.4 - Claude Project Instructions and Guardrails / Subtask 01 - Create root CLAUDE.md

## Objective

Create `CLAUDE.md` with project purpose, repo navigation, quality commands, roadmap conventions and
instruction to use canonical ZXRE project state.

## Constraints

- Keep implementation within Milestone 0006 scope.
- ZXRE MCP is the canonical project-aware boundary; reverse-engineering business logic stays in core services.
- Tools/resources stay emulator-neutral and harness-neutral unless this subtask defines a thin adapter.
- `zesarux-mcp` is optional; ZXRE-only operation must remain supported.
- External debugger observations are exploratory until imported/reproduced canonically.
- Agents/Skills may propose hypotheses, but confirmation must pass through Milestone 0005 policy.
- Keep context/tool outputs bounded; reference large artifacts rather than dumping them.
- Update tests/docs with implementation.

## Completion conditions

- Named files/configuration/agent or Skill definitions are implemented.
- Backend-independent MCP tests use temporary projects and fake runtime backend where applicable.
- Optional harness/companion/live checks skip clearly when unavailable.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest` remain green where applicable.
- No direct MCP mutation can bypass canonical evidence/promotion rules.
