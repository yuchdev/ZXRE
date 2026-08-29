"""CLI entry points for zxre."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from zxre import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="zxre",
        description="ZXRE repository bootstrap CLI.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    return 0
