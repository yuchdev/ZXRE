# Task 03.0 - Disassembly Backend Integration / Subtask 06 - Persist structured disassembly

## Objective

Create `src/zxre/disasm/serialization.py`.

## Implementation specification

Persist a versioned representation, suggested:
`analysis/disassembly.json` or partitioned files when size warrants it.

Requirements:
- instruction address, bytes, mnemonic, operands, backend metadata;
- source snapshot ID/artifact;
- diagnostics;
- deterministic ordering;
- no duplication of large memory bytes beyond instruction bytes actually needed for reconstruction;
- explicit format version.

Tests:
round-trip, unknown future version, large instruction list ordering.

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
