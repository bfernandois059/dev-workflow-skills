#!/usr/bin/env python3
"""Genera la sección de skills del catálogo de routing desde los SKILL.md.

El catálogo (`docs/agent-skills-catalog.md`) mezcla prosa escrita a mano con una
sección generada. Este script reescribe únicamente la región delimitada por los
marcadores, tomando el `name`, el `description` del frontmatter y el `VERSION` de
cada skill. La prosa fuera de los marcadores no se toca.

    python3 scripts/build_skill_catalog.py           # reescribe el catálogo
    python3 scripts/build_skill_catalog.py --check   # falla si está desincronizado

El `description` del frontmatter es el texto de routing autoritativo: es el que
leen los agentes para decidir si activan la skill. El catálogo lo cita literal
para que ChatGPT y el ejecutor tomen la decisión con el mismo insumo.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
CATALOG = ROOT / "docs" / "agent-skills-catalog.md"

BEGIN = "<!-- BEGIN GENERATED: skills -->"
END = "<!-- END GENERATED: skills -->"


def read_skill(skill_dir):
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not front:
        raise SystemExit(f"{skill_dir.name}: SKILL.md sin frontmatter")

    fields = {}
    for key in ("name", "description"):
        found = re.search(
            rf"^{key}:\s*(.*?)(?=\n[A-Za-z_-]+:|\Z)", front.group(1), re.S | re.M
        )
        if not found:
            raise SystemExit(f"{skill_dir.name}: falta `{key}` en el frontmatter")
        raw = found.group(1)
        # `description` suele venir como bloque YAML plegado (`>-`, `|`, …): el
        # indicador no es parte del valor.
        raw = re.sub(r"^[>|][+-]?\s*\n", "", raw)
        fields[key] = " ".join(raw.split()).strip("\"'")

    version_file = skill_dir / "VERSION"
    fields["version"] = (
        version_file.read_text(encoding="utf-8").strip()
        if version_file.exists()
        else "sin versión"
    )

    if fields["name"] != skill_dir.name:
        raise SystemExit(
            f"{skill_dir.name}: el `name` del frontmatter dice `{fields['name']}`"
        )
    return fields


def render(skills):
    lines = [
        BEGIN,
        "",
        f"# 3. Catálogo cerrado — {len(skills)} skills",
        "",
        "Un nombre que no aparece en esta lista no es una Agent Skill de este workflow.",
        "",
        "```text",
    ]
    lines += [s["name"] for s in skills]
    lines += ["```", ""]

    for skill in skills:
        lines += [
            f"## `{skill['name']}` · v{skill['version']}",
            "",
            skill["description"],
            "",
        ]

    lines.append(END)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    skills = [read_skill(d) for d in sorted(SKILLS_DIR.iterdir()) if d.is_dir()]
    if not skills:
        raise SystemExit("no se encontraron skills en skills/")

    current = CATALOG.read_text(encoding="utf-8")
    if BEGIN not in current or END not in current:
        raise SystemExit(f"{CATALOG}: faltan los marcadores de sección generada")

    updated = re.sub(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        lambda _: render(skills),
        current,
        flags=re.S,
    )

    if args.check:
        if updated != current:
            print(f"{CATALOG} está desincronizado de los SKILL.md", file=sys.stderr)
            return 1
        print(f"{CATALOG}: {len(skills)} skills, sincronizado")
        return 0

    CATALOG.write_text(updated, encoding="utf-8")
    print(f"{CATALOG}: {len(skills)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
