# Development Guide

## Environment setup

```bash
uv sync --group dev
```

## Quality commands

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
```

## Repository layout

- `/src/zxre`: production package.
- `/tests`: test suite.
- `/docs/roadmap`: milestone and task contracts.
- `/docs/architecture`: architectural principles.
- `/docs/development`: contributor workflow and quality gates.

## Roadmap contract rule

Roadmap task/subtask specs are implementation contracts and must be updated with actual evidence/status after completion.
