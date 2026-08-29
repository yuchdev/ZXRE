# Task 04.0 - Emulator Capability Contract / Subtask 01 - Define runtime capability taxonomy

## Objective

Create `src/zxre/runtime/capabilities.py`, `src/zxre/runtime/__init__.py`, and
`tests/runtime/test_capabilities.py`. Define serializable capability enums/value objects for session
control, snapshots, memory/register access, step/run/pause, breakpoints/watchpoints, execution
history, coverage, transaction logging, keyboard input, screen capture and T-state counters.
Distinguish required and optional capabilities; keep generic identifiers free of ZEsarUX/ZRCP
terminology.

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
