# Task 02.1 - BASIC Loader Decoding / Subtask 02 - Implement Spectrum BASIC token decoder

## Objective

Create:

## Implementation specification

- `src/zxre/basic/tokens.py`
- `src/zxre/basic/decoder.py`
- `tests/basic/test_decoder.py`

Decode tokenized ZX Spectrum BASIC program bytes into lines/statements.

Support:
- line number and line length;
- Spectrum keyword tokens required for loaders, including at minimum:
  `CLEAR`, `LOAD`, `CODE`, `SCREEN$`, `RANDOMIZE`, `USR`, `RUN`, `GO TO`, `LET`, `POKE`, `BORDER`,
  `PAPER`, `INK`, `CLS`, `REM`, separators/colon;
- ordinary ASCII characters/string literals;
- Spectrum numeric constant representation sufficient to recover literal integers commonly used by
  loaders.

Preserve undecoded token bytes as diagnostics rather than crashing.

Do not attempt a complete BASIC interpreter in this task.

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
