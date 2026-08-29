"""Smoke tests for CLI bootstrap behavior."""

from __future__ import annotations

import subprocess
import sys

import pytest

from zxre.cli import main


def test_main_help_exits_cleanly(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])

    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert "usage:" in captured.out


def test_module_help() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "zxre", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0
    assert "usage:" in completed.stdout
