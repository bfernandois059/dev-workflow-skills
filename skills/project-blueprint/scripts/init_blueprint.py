#!/usr/bin/env python3
"""Crea una estructura documental inicial sin sobrescribir archivos existentes."""
from pathlib import Path
import argparse

FILES = {
    "docs/00-project-blueprint.md": "# Project Blueprint\n\nEstado: Draft\n",
    "docs/01-product-requirements.md": "# Product Requirements\n",
    "docs/02-architecture.md": "# Architecture\n",
    "docs/03-data-and-integrations.md": "# Data and Integrations\n",
    "docs/04-ux-content-and-design-system.md": "# UX, Content and Design System\n",
    "docs/05-security-and-operations.md": "# Security and Operations\n",
    "docs/06-quality-and-testing.md": "# Quality and Testing\n",
    "docs/07-delivery-plan.md": "# Delivery Plan\n",
    "docs/decisions/ADR-0001-initial-architecture.md": "# ADR-0001: Initial Architecture\n\nStatus: Proposed\n",
    ".env.example": "# Add variable names only. Never commit secrets.\n",
}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    created, skipped = [], []
    for rel, content in FILES.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            skipped.append(rel)
            continue
        target.write_text(content, encoding="utf-8")
        created.append(rel)
    print("Created:")
    print("\n".join(f"  - {x}" for x in created) or "  (none)")
    print("Skipped existing:")
    print("\n".join(f"  - {x}" for x in skipped) or "  (none)")

if __name__ == "__main__":
    main()
