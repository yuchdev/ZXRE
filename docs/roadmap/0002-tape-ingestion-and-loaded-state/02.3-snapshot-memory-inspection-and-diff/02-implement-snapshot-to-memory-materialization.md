# Task 02.3 - Snapshot Memory Inspection and Diff / Subtask 02 - Implement snapshot-to-memory materialization

## Objective

Create `src/zxre/memory/from_snapshot.py`.

## Implementation specification

Implement:
`materialize_memory(snapshot_descriptor, artifact_store, platform) -> MemoryImage`

For `.z80` reference snapshots:
- use snapshot parser from Task 02.2;
- map RAM into correct Spectrum address ranges;
- exclude ROM bytes not present in snapshot unless explicitly available;
- fail clearly on missing pages/unsupported formats.

Tests use patterned pages and boundary addresses.

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
