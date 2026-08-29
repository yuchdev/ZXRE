# Task 02.1 - BASIC Loader Decoding / Subtask 03 - Extract BASIC program payloads from tape inventory

## Objective

Create `src/zxre/basic/from_tape.py`.

## Implementation specification

Given `TapeImage`, locate standard PROGRAM header/data relationships deterministically.

Rules:
- use explicit standard header metadata;
- tolerate missing/mismatched following data blocks;
- validate declared program length against available payload;
- return one or more candidate BASIC program payloads rather than assuming the first block is the
  loader.

Tests:
- one loader;
- multiple BASIC programs;
- header without data;
- data shorter than declared;
- unrelated CODE blocks around loader.

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
