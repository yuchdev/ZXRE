# Contributing to ZXRE

## Setup

```bash
uv sync --group dev
```

## Quality checks

Run the same commands used by CI:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
```

## Local pre-commit hook

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

## Repository conventions

- Source code uses `src/` layout.
- Task and subtask roadmap specs are implementation contracts.
- After completing work, update roadmap/task status with actual evidence and current status.
- Use absolute-from-repo-root Markdown links in documentation.
