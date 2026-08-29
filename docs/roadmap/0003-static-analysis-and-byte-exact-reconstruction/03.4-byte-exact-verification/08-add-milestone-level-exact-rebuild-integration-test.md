# Task 03.4 - Byte-Exact Verification / Subtask 08 - Add milestone-level exact rebuild integration test

## Objective

Create `tests/integration/test_milestone_0003_rebuild.py`.

## Implementation specification

Scenario:
1. load generated/synthetic snapshot fixture;
2. define mixed code/data control map;
3. disassemble;
4. extract references;
5. generate source;
6. assemble with configured reference assembler;
7. compare reconstructed bytes;
8. assert `EXACT`.

If external assembler unavailable in default CI:
- skip external adapter test clearly;
- maintain an always-on comparator/generator test using a controlled fake assembler result;
- provide a dedicated integration command/profile for full exact rebuild.

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
