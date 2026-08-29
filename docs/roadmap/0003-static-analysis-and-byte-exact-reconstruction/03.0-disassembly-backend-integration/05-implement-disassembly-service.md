# Task 03.0 - Disassembly Backend Integration / Subtask 05 - Implement disassembly service

## Objective

Create `src/zxre/disasm/service.py`.

## Implementation specification

Responsibilities:
- choose backend by configured/default ID;
- materialize snapshot memory via Milestone 0002 memory service;
- validate requested range against platform;
- decode one/range;
- persist resulting structured disassembly metadata/artifact;
- attach provenance to source snapshot/memory artifact and backend/version.

No CLI parsing logic in this service.

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
