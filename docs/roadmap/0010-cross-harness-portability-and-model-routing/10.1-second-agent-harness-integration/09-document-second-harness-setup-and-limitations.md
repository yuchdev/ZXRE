# Task 10.1 - Second Agent Harness Integration / Subtask 09 - Document second-harness setup and limitations

## Objective

Create/update `docs/harnesses/<selected>.md` with setup, MCP registration, procedure mapping,
unsupported features and reproducible scenario command.

## Constraints

- Keep implementation within this milestone's scope.
- Preserve all deterministic/evidence/promotion invariants established by Milestones 0001–0009.
- Prefer explicit adapter/plugin boundaries over conditional logic scattered through generic services.
- Do not turn optional harnesses, models, emulators or companion MCP servers into core dependencies.
- Keep large artifacts and harness/model diagnostics referenced rather than copied into canonical semantic state.
- Update tests and documentation together with code/configuration.
- Any external-tool or live-harness test must skip cleanly when its dependency/account is unavailable.

## Completion conditions

- Named files/APIs/configuration/docs are implemented.
- Relevant unit/integration/conformance tests pass.
- Existing ZX Spectrum workflows remain regression-green.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green where applicable.
- Canonical project/evidence semantics do not depend on the selected harness, model, emulator or
  companion debugger.
