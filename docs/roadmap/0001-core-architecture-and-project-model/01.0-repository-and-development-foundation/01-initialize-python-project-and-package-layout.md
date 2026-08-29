# Task 01.0 - Repository and Development Foundation / Subtask 01 - Initialize Python project and package layout

## Objective

Create the repository root project metadata and source/test layout.

## Implementation specification

Required files:
- `pyproject.toml`
- `.python-version`
- `src/zxre/__init__.py`
- `src/zxre/__main__.py`
- `src/zxre/cli.py`
- `tests/__init__.py`
- `tests/test_imports.py`
- `tests/test_cli_smoke.py`

Requirements:
- Use `uv` as the package/project manager.
- Target Python 3.12 unless repository constraints discovered during implementation justify a newer
  compatible baseline.
- Use a `src/` layout.
- Define package name `zxre`.
- `python -m zxre --help` and `uv run zxre --help` must both work.
- Implement a minimal CLI using `argparse` or Typer; prefer the smaller dependency surface unless
  later requirements clearly justify Typer.
- CLI must expose only a root help/version surface at this stage; no fake reverse-engineering logic.
- `src/zxre/__init__.py` exposes `__version__`.
- `pyproject.toml` defines console script `zxre = "zxre.cli:main"`.

Tests:
- package imports cleanly;
- module execution returns help;
- console entry point smoke-testable through the callable `main()`.

Completion:
`uv sync`, `uv run python -m zxre --help`, and `uv run pytest` succeed from a fresh clone.

## Constraints

- Keep implementation within Milestone 0001 scope.
- Prefer deterministic, typed, testable code.
- Do not add Claude, MCP, SkoolKit, emulator, tape parsing or disassembly dependencies unless this
  subtask explicitly requires them (none in Milestone 0001 do).
- Do not silently expand the project format or public API beyond what this task needs.
- Update/add tests together with production code.
- Preserve absolute-from-repo-root documentation links.

## Completion conditions

- All files/functions/configuration named above are implemented.
- Relevant unit/integration tests pass.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green once those tools exist after Task 01.0.
- Task documentation/status is updated with actual implementation evidence when completed.
