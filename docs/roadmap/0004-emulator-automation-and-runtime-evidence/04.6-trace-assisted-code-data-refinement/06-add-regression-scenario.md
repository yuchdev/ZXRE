# Task 04.6 - Trace-Assisted Code/Data Refinement / Subtask 06 - Add regression scenario

## Objective

Create `tests/integration/test_trace_refines_control_map.py` showing sparse executed addresses
promote only proven code and leave other bytes unchanged.

## Constraints

- Keep implementation within Milestone 0004 scope.
- Generic runtime modules must not expose ZEsarUX/ZRCP or `zesarux-mcp` syntax, slot IDs, sockets or
  process objects.
- ZEsarUX is the preferred reference backend, not a required core dependency.
- `zesarux-mcp` and other debugger MCPs are optional companions, not required runtime providers.
- Persisted runtime outputs use ArtifactStore/provenance.
- Do not add LLM calls, agents, hypotheses, gameplay semantics or causal experiment planning.
- External/live emulator tests must skip cleanly when dependencies are unavailable.
- Update tests together with implementation.

## Completion conditions

- All named files/APIs are implemented.
- Backend-independent tests pass with the deterministic fake backend.
- Optional live ZEsarUX tests pass when configured and skip clearly otherwise.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green.
- No core dependency on one emulator, MCP server or agent harness is introduced.
