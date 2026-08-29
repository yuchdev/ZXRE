# Task 04.0 - Emulator Capability Contract / Subtask 02 - Define runtime session and machine-state models

## Objective

Create `src/zxre/runtime/model.py` and `tests/runtime/test_model.py`. Define `RuntimeSessionId`,
`RuntimeBackendId`, `RuntimeSessionInfo`, `RuntimeMachineInfo`, `CpuRegisters`, `RuntimeStopReason`,
`RuntimeStopEvent`, and `RuntimeDiagnostic`. Keep architecture-specific register values in typed
maps/extensions and define normalized stop reasons such as breakpoint, watchpoint, step completion,
pause, timeout and backend error.

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
