#!/usr/bin/env python3
"""Report the installed skill version and optionally compare it with a remote."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = SKILL_ROOT.name
DEFAULT_REMOTE_URL = (
    "https://raw.githubusercontent.com/bfernandois059/dev-workflow-skills/"
    f"main/skills/{SKILL_NAME}/VERSION"
)
SEMVER_PATTERN = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def parse_version(raw: str, source: str) -> tuple[int, int, int]:
    value = raw.strip()
    match = SEMVER_PATTERN.fullmatch(value)
    if not match:
        raise ValueError(f"Invalid SemVer in {source}: {value!r}")
    return tuple(int(part) for part in match.groups())


def read_local_version() -> tuple[str, tuple[int, int, int]]:
    version_path = SKILL_ROOT / "VERSION"
    raw = version_path.read_text(encoding="utf-8").strip()
    return raw, parse_version(raw, str(version_path))


def read_remote_version(url: str, timeout: float) -> tuple[str, tuple[int, int, int]]:
    with urlopen(url, timeout=timeout) as response:  # nosec B310: caller selects URL
        raw = response.read(128).decode("utf-8").strip()
    return raw, parse_version(raw, url)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-remote",
        action="store_true",
        help="compare the installed version with the canonical remote VERSION",
    )
    parser.add_argument(
        "--remote-url",
        default=None,
        help="override the remote VERSION URL (implies --check-remote)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="remote request timeout in seconds (default: 5)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        local_raw, local = read_local_version()
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Installed {SKILL_NAME} version: {local_raw}")

    should_check_remote = args.check_remote or args.remote_url is not None
    if not should_check_remote:
        return 0
    if args.timeout <= 0:
        print("ERROR: --timeout must be greater than zero", file=sys.stderr)
        return 2

    try:
        remote_url = args.remote_url or DEFAULT_REMOTE_URL
        remote_raw, remote = read_remote_version(remote_url, args.timeout)
    except (OSError, UnicodeError, URLError, ValueError) as exc:
        print(f"ERROR: unable to verify remote version: {exc}", file=sys.stderr)
        return 2

    print(f"Remote {SKILL_NAME} version: {remote_raw}")
    if local < remote:
        print("UPDATE AVAILABLE: the installed skill is older than the remote version.")
        return 1
    if local > remote:
        print("LOCAL AHEAD: the installed skill is newer than the selected remote.")
        return 0

    print("UP TO DATE: installed and remote versions match.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
