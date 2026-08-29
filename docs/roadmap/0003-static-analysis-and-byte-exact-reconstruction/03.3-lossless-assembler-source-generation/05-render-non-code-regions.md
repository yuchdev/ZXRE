# Task 03.3 - Lossless Assembler Source Generation / Subtask 05 - Render non-code regions

## Objective

Create `src/zxre/reconstruct/data.py`.

## Implementation specification

Render:
- `BYTES` as byte directives;
- `WORDS_LE` as words when safe;
- `TEXT` as assembler strings only when exact bytes survive escaping/encoding; otherwise bytes;
- `FILL` as fill directive only if chosen assembler semantics are byte-exact;
- `UNKNOWN` as bytes by default.

Never sacrifice byte fidelity for prettier source.

Tests include zero bytes, quotes, high-bit bytes, odd word-length region.

## Constraints

- Keep implementation within Milestone 0003 scope.
- Preserve exact original bytes and address ranges whenever transforming code/data into structured
  form or generated source.
- Do not add semantic routine names, gameplay interpretation, runtime execution experiments, LLM
  calls, agents or MCP behavior.
- External tools must stay behind adapters with version/provenance capture and clean skip behavior
  when unavailable.
- Canonical project state is structured ZXRE data; third-party textual listings/reports are not the
  source of truth.
- Prefer conservative classification and explicit `UNKNOWN`/diagnostics over guessing.
- Update/add tests together with production code.

## Completion conditions

- All named files/functions/configuration are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green.
- External-tool tests skip cleanly when required binaries are unavailable.
- For reconstruction-related subtasks, byte fidelity is demonstrated by tests or explicit diagnostic
  behavior rather than visual inspection.
