#!/usr/bin/env python3
"""Inicializa la estructura documental para project-blueprint de forma proporcional.

Principio: Decision completeness > document completeness.
Por defecto crea únicamente la fuente canónica `docs/00-project-blueprint.md`.
El desglose modular se activa solo si la complejidad del proyecto lo justifica.
"""
from pathlib import Path
import argparse

CANONICAL_FILE = {
    "docs/00-project-blueprint.md": "# Project Blueprint\n\nEstado: Draft\n"
}

MODULAR_FILES = {
    "docs/01-product-requirements.md": "# Product Requirements\n",
    "docs/02-architecture.md": "# Architecture\n",
    "docs/03-data-and-integrations.md": "# Data and Integrations\n",
    "docs/04-ux-content-and-design-system.md": "# UX, Content and Design System\n",
    "docs/05-security-and-operations.md": "# Security and Operations\n",
    "docs/06-quality-and-testing.md": "# Quality and Testing\n",
    "docs/07-delivery-plan.md": "# Delivery Plan\n",
}

RETROFIT_FILES = {
    "docs/migration-plan.md": "# Migration Plan\n\n## Actual → Objetivo\n",
}

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inicializa artefactos documentales para project-blueprint de forma proporcional."
    )
    parser.add_argument("path", nargs="?", default=".", help="Ruta base del proyecto (default: '.')")
    parser.add_argument(
        "--modular",
        action="store_true",
        help="Crea la suite modular completa (docs/01 a docs/07) para sistemas complejos (L3/L4).",
    )
    parser.add_argument(
        "--retrofit",
        action="store_true",
        help="Incluye docs/migration-plan.md para proyectos existentes en modo Retrofit.",
    )
    args = parser.parse_args()
    root = Path(args.path).resolve()

    files_to_create = dict(CANONICAL_FILE)
    if args.modular:
        files_to_create.update(MODULAR_FILES)
    if args.retrofit:
        files_to_create.update(RETROFIT_FILES)

    created, skipped = [], []
    for rel, content in files_to_create.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            skipped.append(rel)
            continue
        target.write_text(content, encoding="utf-8")
        created.append(rel)

    print(f"Modo: {'Modular (L3/L4)' if args.modular else 'Canónico proporcional'}")
    print("Created:")
    print("\n".join(f"  - {x}" for x in created) or "  (none)")
    print("Skipped existing:")
    print("\n".join(f"  - {x}" for x in skipped) or "  (none)")

if __name__ == "__main__":
    main()
