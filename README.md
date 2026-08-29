# ZXRE

ZXRE is an LLM-assisted, evidence-driven reverse-engineering toolkit project.

Current foundation focus:
- Deterministic tooling and repeatable analysis pipelines are kept separate from semantic/agent analysis.
- Initial target platforms are ZX Spectrum 48K/Z80 and TAP/TZX workflows.
- The core architecture is scaffolded to remain independent from any single emulator or harness.

## Status

This repository currently contains scaffold/foundation setup only (Task 01.0).

## Quick start

```bash
uv sync --group dev
uv run zxre --help
uv run python -m zxre --help
uv run pytest
```

## Roadmap

See `/docs/roadmap/README.md`.
