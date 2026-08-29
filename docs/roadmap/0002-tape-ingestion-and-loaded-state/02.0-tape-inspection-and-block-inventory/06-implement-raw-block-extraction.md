# Task 02.0 - Tape Inspection and Block Inventory / Subtask 06 - Implement raw block extraction

## Objective

Create `src/zxre/tape/extract.py`.

## Implementation specification

Implement deterministic extraction of selected blocks as project-managed artifacts.

APIs should support:
- extract one block by `TapeBlockId`;
- extract all payload-bearing blocks;
- choose raw encoded block bytes vs logical data payload when meaningful.

Every extracted artifact must:
- reference the original tape artifact in provenance;
- record operation name and block ID/index;
- preserve exact bytes;
- deduplicate through `ArtifactStore`.

Tests:
- extraction equality to source slices;
- provenance source link;
- duplicate extraction deduplicates content;
- invalid block ID.

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
