# Task 02.1 - BASIC Loader Decoding / Subtask 04 - Implement loader statement recognizer

## Objective

Create:

## Implementation specification

- `src/zxre/basic/loader.py`
- `tests/basic/test_loader.py`

Convert decoded BASIC statements into normalized `LoaderOperation` records.

Recognize at minimum:
- `CLEAR <expr>`;
- `LOAD ""`;
- `LOAD "" CODE`;
- `LOAD "" CODE <expr>`;
- `LOAD "<name>" CODE [<expr>]`;
- `LOAD "" SCREEN$`;
- `RANDOMIZE USR <expr>`;
- direct `USR <expr>` where syntactically relevant;
- `RUN [line]`;
- `POKE <address>,<value>` as explicit loader-side memory mutation metadata.

Preserve statement order and line/statement location.

Do not assume each `LOAD` corresponds to a specific physical tape block yet unless it can be matched
deterministically from tape order/header metadata.

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
