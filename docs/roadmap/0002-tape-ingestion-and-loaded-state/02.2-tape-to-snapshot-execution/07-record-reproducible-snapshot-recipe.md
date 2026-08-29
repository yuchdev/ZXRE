# Task 02.2 - Tape-to-Snapshot Execution / Subtask 07 - Record reproducible snapshot recipe

## Objective

Persist a machine-readable recipe alongside snapshot descriptor, either within existing snapshot

## Implementation specification

metadata serialization or a dedicated `analysis/snapshots.json`.

Recipe must include:
- source artifact IDs;
- backend ID/version;
- normalized backend options;
- requested snapshot format;
- resulting artifact ID/digest;
- operation timestamp.

Provide a service operation capable of re-running the recipe and comparing resulting RAM/digest where
backend determinism permits.

Do not claim byte-identical full snapshot files if timestamps/backend metadata make only RAM-state
equivalence deterministic; distinguish those cases explicitly.

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
