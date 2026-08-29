# Task 02.1 - BASIC Loader Decoding / Subtask 01 - Define BASIC loader domain model

## Objective

Create:

## Implementation specification

- `src/zxre/basic/model.py`
- `src/zxre/basic/__init__.py`
- `tests/basic/test_model.py`

Define:
- `BasicProgram`;
- `BasicLine`;
- `BasicStatement`;
- `BasicToken`;
- `BasicExpression`;
- `LoaderOperation`;
- `LoaderOperationKind`;
- `CandidateAddress`;
- `CandidateAddressKind`;
- `BasicDecodeDiagnostic`.

Candidate kinds should include:
- `CLEAR_LIMIT`;
- `LOAD_ADDRESS`;
- `USR_ENTRY`;
- `RUN_LINE`;
- `OTHER`.

Each candidate must carry:
- numeric value;
- source line number;
- source statement location;
- derivation kind;
- deterministic confidence classification such as `EXPLICIT` vs `EVALUATED`, not probabilistic LLM confidence.

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
