# Task 02.4 - Ingestion Validation Fixtures / Subtask 08 - Add Milestone 0002 end-to-end acceptance test

## Objective

Create `tests/integration/test_milestone_0002_ingestion.py`.

## Implementation specification

Scenario:
1. create project;
2. import synthetic TAP/TZX input;
3. parse inventory;
4. decode BASIC loader;
5. verify candidate load/USR addresses;
6. create snapshot through configured test/backend path;
7. reopen project;
8. materialize RAM;
9. export/diff expected range;
10. verify provenance chain back to original tape artifact.

If external SkoolKit is unavailable in default CI, split acceptance into:
- always-on deterministic parser/model/memory test using generated snapshot fixture;
- optional external-tool test proving tap2sna integration.

Milestone completion must not depend on network access.

## Constraints

- Keep implementation within Milestone 0002 scope.
- All parsing, decoding, snapshot creation, exports and diffs must be deterministic and attributable
  to project artifacts/provenance.
- Do not add semantic reverse-engineering conclusions, LLM calls, agents, MCP integration or emulator
  runtime control.
- External tools such as SkoolKit must remain behind adapters and be optional outside the specific
  backend/integration tests that require them.
- Prefer typed domain objects and structured diagnostics over parsing human-readable command output
  throughout the application.
- Update/add tests together with production code.
- Preserve the Milestone 0001 project/artifact/platform boundaries rather than bypassing services.

## Completion conditions

- All files/functions/configuration named above are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green.
- External-tool tests skip cleanly when the external backend is unavailable.
- Task documentation/status is updated with actual implementation evidence when completed.
