# Task 02.1 - BASIC Loader Decoding / Subtask 06 - Derive candidate loader addresses

## Objective

Create `src/zxre/basic/candidates.py`.

## Implementation specification

From normalized operations derive deterministic candidates:
- CLEAR memory limit;
- explicit `LOAD ... CODE <address>` destinations;
- `RANDOMIZE USR <address>` / `USR` entry candidates.

Each candidate must reference its source operation and evaluation derivation.

Important:
- `USR` is a **candidate entry point**, not proof of the game's real entry point;
- `LOAD CODE` address is a declared destination, not proof that final executable code remains there;
- preserve multiple candidates.

Tests:
multiple loads, chained variables, missing addresses, multiple USRs.

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
