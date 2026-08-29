# Task 01.0 - Repository and Development Foundation / Subtask 03 - Add repository hygiene and GitHub metadata

## Objective

Create repository-level hygiene and GitHub collaboration files.

## Implementation specification

Required files:
- `.gitignore`
- `.editorconfig`
- `.gitattributes`
- `LICENSE`
- `README.md`
- `CONTRIBUTING.md`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`

README must include:
- project purpose: LLM-assisted, evidence-driven reverse engineering;
- initial target: ZX Spectrum 48K/Z80 and TAP/TZX, while core is not tied to one emulator/harness;
- explicit separation of deterministic tooling vs semantic/agent analysis;
- quick start with `uv`;
- current roadmap link `/docs/roadmap/README.md`;
- current status: scaffold/foundation only.

Do not claim features not implemented.

LICENSE:
choose a permissive license suitable for an open-source developer tool; default to MIT unless the
repository owner has already selected another license.

Completion:
GitHub renders README and issue forms without broken local links.

## Constraints

- Keep implementation within Milestone 0001 scope.
- Prefer deterministic, typed, testable code.
- Do not add Claude, MCP, SkoolKit, emulator, tape parsing or disassembly dependencies unless this
  subtask explicitly requires them (none in Milestone 0001 do).
- Do not silently expand the project format or public API beyond what this task needs.
- Update/add tests together with production code.
- Preserve absolute-from-repo-root documentation links.

## Completion conditions

- All files/functions/configuration named above are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green once those tools exist after Task 01.0.
- Task documentation/status is updated with actual implementation evidence when completed.
