# Task 02.2 - Tape-to-Snapshot Execution / Subtask 03 - Implement SkoolKit tap2sna adapter

## Objective

Create:

## Implementation specification

- `src/zxre/adapters/skoolkit/__init__.py`
- `src/zxre/adapters/skoolkit/tap2sna.py`
- `src/zxre/adapters/skoolkit/discovery.py`
- `tests/adapters/skoolkit/test_tap2sna.py`

Implement first backend using installed SkoolKit `tap2sna.py` or its supported executable/API.

Requirements:
- discover executable deterministically from configured path then PATH;
- expose version when available;
- build argv without shell interpolation;
- use project-managed temporary/output paths;
- capture stderr/stdout;
- import successful snapshot into `ArtifactStore`;
- record SkoolKit version + normalized arguments in provenance;
- clean temporary files on success/failure.

Do not add SkoolKit as a mandatory Python import dependency if command-line integration is cleaner;
document it as an optional external tool required for this backend.

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
