#!/usr/bin/env python3
"""Lightweight pre-PR repository checks.

This script does not replace project lint, tests, typecheck, build, or security scans.
It checks common workflow/documentation conditions without modifying the repository.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROTECTED_BRANCHES = {"main", "master", "develop", "production"}
SECRET_PATTERNS = (
    "BEGIN PRIVATE KEY",
    "AWS_SECRET_ACCESS_KEY=",
    "SUPABASE_SERVICE_ROLE_KEY=",
    "RESEND_API_KEY=",
    "STRIPE_SECRET_KEY=",
)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Git command failed")
    return result.stdout.strip()


def main() -> int:
    root = Path.cwd()
    failures: list[str] = []
    warnings: list[str] = []

    try:
        branch = git("branch", "--show-current")
        status = git("status", "--short")
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 2

    if not branch:
        failures.append("Detached HEAD: work must be on a named task branch.")
    elif branch in PROTECTED_BRANCHES:
        failures.append(f"Current branch '{branch}' is protected; create a task branch.")

    changed = [line[3:] for line in status.splitlines() if len(line) > 3]
    if not changed:
        warnings.append("No working-tree changes detected. Review committed diff against base separately.")

    for relative in changed:
        path = root / relative
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern in text:
                failures.append(f"Possible secret pattern '{pattern}' in {relative}.")

    if any(p.startswith(("src/", "app/", "pages/", "lib/", "api/")) for p in changed):
        if not any(Path(name).exists() for name in ("CHANGELOG.md", "docs")):
            warnings.append("Application code changed but no CHANGELOG.md or docs directory exists.")

    print(f"Branch: {branch or '(detached)'}")
    print(f"Changed paths: {len(changed)}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")

    if failures:
        print("Result: NOT READY FOR PR")
        return 1

    print("Result: BASIC WORKFLOW CHECK PASSED")
    print("Run the repository's real lint, typecheck, tests and build before opening the PR.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
