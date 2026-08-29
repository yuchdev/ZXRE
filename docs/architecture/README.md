# Architecture Principles

- Keep a deterministic core independent of Claude, MCP, SkoolKit, or emulator tooling.
- Separate observable facts/evidence from hypotheses and semantic interpretations.
- Isolate external integrations behind adapters.
- Avoid speculative universal abstractions before concrete requirements exist.
