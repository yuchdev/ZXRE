"""Import smoke tests for zxre."""

import re

from zxre import __version__


def test_package_exposes_version() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+", __version__)
