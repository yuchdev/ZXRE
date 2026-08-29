# Task 02.3 - Snapshot Memory Inspection and Diff / Subtask 04 - Implement memory export

## Objective

Create `src/zxre/memory/export.py`.

## Implementation specification

Support exporting:
- arbitrary mapped address range;
- full RAM image;
- named platform memory region when fully available.

Export result must be imported into ArtifactStore with provenance:
- source snapshot artifact;
- selected address range/region;
- export format (`raw` initially).

Tests verify exact exported bytes and provenance.

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
