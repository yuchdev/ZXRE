# Task 02.1 - BASIC Loader Decoding / Subtask 05 - Implement restricted deterministic expression evaluator

## Objective

Create `src/zxre/basic/evaluator.py`.

## Implementation specification

Support a deliberately small expression subset needed by real-world loaders:
- integer literals;
- parentheses;
- unary `+`/`-`;
- `+`, `-`, `*`, `/` with integer-result validation;
- previously defined numeric `LET` variables where value is deterministically known;
- simple hexadecimal representations only if Spectrum BASIC syntax/input justifies them.

Return an explicit `UnknownValue`/non-evaluable result instead of guessing.

Do not:
- execute arbitrary BASIC;
- evaluate `PEEK`, `IN`, random functions, string-dependent expressions or user input;
- simulate machine state.

Tests:
literal/evaluable cases, variable propagation, unsupported dynamic expressions, division edge cases.

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
