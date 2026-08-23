#!/usr/bin/env python3
"""Compara los inventarios de muchas rutas y produce el mapa de patrones del sitio.

Parte de la skill `ux-critic` (modo sitio). Entrada: el directorio que dejó `sweep.mjs`
(un JSON por ruta). Salida: tabla de métricas, señales agrupadas por ruta, sistema visual
real del sitio y una propuesta de muestreo por arquetipo.

    python3 compare_inventories.py .ux-sweep
    python3 compare_inventories.py .ux-sweep --format json

No juzga: agrupa hechos medidos. El juicio es de la Fase 2 sobre la muestra elegida.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Umbrales. Son puntos de atención, no veredictos: una ruta puede superarlos con razón.
THRESHOLDS = {
    "distinctSizes": (8, "escala tipográfica dispersa"),
    "distinctWeights": (3, "exceso de pesos"),
    "distinctFamilies": (2, "exceso de familias"),
    "maxSurfaceDepth": (2, "cajas anidadas (A1)"),
    "contrastFailures": (0, "contraste bajo el umbral"),
    "tapTargetsBelow": (0, "objetivos táctiles pequeños"),
    "unnamedControls": (0, "controles sin nombre accesible"),
    "headingSkips": (0, "saltos de nivel de encabezado"),
    "offGridSpacing": (4, "espaciado fuera de escala"),
    "longLines": (0, "líneas de texto demasiado anchas"),
    "missingAlt": (0, "imágenes sin alt"),
}

COLUMNS = [
    ("distinctSizes", "tipos"),
    ("distinctWeights", "pesos"),
    ("distinctFamilies", "fam"),
    ("distinctTextColors", "colTxt"),
    ("distinctBackgrounds", "colBg"),
    ("offGridSpacing", "off4"),
    ("maxSurfaceDepth", "anid"),
    ("contrastFailures", "contr"),
    ("tapTargetsBelow", "toque"),
    ("unnamedControls", "sinNom"),
    ("h1Count", "h1"),
    ("headingSkips", "skips"),
    ("sections", "secc"),
]


def dig(data, *keys, default=0):
    cur = data
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur if cur is not None else default


def metrics(inv: dict) -> dict:
    return {
        "distinctSizes": dig(inv, "typography", "distinctSizes"),
        "distinctWeights": dig(inv, "typography", "distinctWeights"),
        "distinctFamilies": dig(inv, "typography", "distinctFamilies"),
        "distinctTextColors": dig(inv, "colors", "distinctText"),
        "distinctBackgrounds": dig(inv, "colors", "distinctBackground"),
        "offGridSpacing": len(dig(inv, "spacing", "offFourGrid", default=[])),
        "maxSurfaceDepth": dig(inv, "surfaces", "maxDepth"),
        "contrastFailures": dig(inv, "contrast", "failures"),
        "tapTargetsBelow": dig(inv, "tapTargets", "belowMinimum"),
        "unnamedControls": dig(inv, "interactive", "unnamedCount"),
        "h1Count": dig(inv, "headings", "h1Count"),
        "headingSkips": len(dig(inv, "headings", "levelSkips", default=[])),
        "sections": len(dig(inv, "rhythm", "sections", default=[])),
        "longLines": len(dig(inv, "lineLength", "tooLong", default=[])),
        "missingAlt": len(dig(inv, "images", "missingAlt", default=[])),
    }


def signature(inv: dict) -> str:
    """Firma de arquetipo: con qué se parece una ruta a otra."""
    sizes = [s["value"] for s in dig(inv, "typography", "sizes", default=[])[:5]]
    sections = len(dig(inv, "rhythm", "sections", default=[]))
    bucket = "1-2" if sections <= 2 else "3-5" if sections <= 5 else "6+"
    depth = dig(inv, "surfaces", "maxDepth")
    nest = "≤2" if depth <= 2 else "3" if depth == 3 else "4+"
    return f"tipos[{','.join(sorted(sizes))}] · secciones[{bucket}] · anidamiento[{nest}]"


def load(directory: Path) -> list[dict]:
    rows = []
    for f in sorted(directory.glob("*.json")):
        if f.name.startswith("_"):
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"aviso: {f.name} no es JSON válido ({exc})", file=sys.stderr)
            continue
        inv = data.get("inventory") or data
        rows.append(
            {
                "route": data.get("route", f.stem),
                "file": f.name,
                "inventory": inv,
                "metrics": metrics(inv),
                "signature": signature(inv),
            }
        )
    return rows


def signals(row: dict) -> list[str]:
    out = []
    for key, (limit, label) in THRESHOLDS.items():
        value = row["metrics"].get(key, 0)
        if value > limit:
            out.append(label)
    if row["metrics"].get("h1Count", 1) != 1:
        out.append("h1 ausente o duplicado")
    return out


def render_markdown(rows: list[dict]) -> str:
    lines: list[str] = []
    add = lines.append

    add("# Barrido de interfaz — mapa de patrones\n")
    add(f"Rutas medidas: **{len(rows)}**\n")
    add("Datos medidos sobre la página viva. No son hallazgos: son los hechos con los que")
    add("se elige qué pantallas criticar a fondo.\n")

    add("## Métricas por ruta\n")
    add("| ruta | " + " | ".join(label for _, label in COLUMNS) + " |")
    add("|---" * (len(COLUMNS) + 1) + "|")
    for row in sorted(rows, key=lambda r: -len(signals(r))):
        cells = [str(row["metrics"].get(key, "")) for key, _ in COLUMNS]
        add(f"| `{row['route']}` | " + " | ".join(cells) + " |")
    add("")
    add("`off4` = valores de espaciado fuera de la escala de 4 px · `anid` = profundidad")
    add("máxima de cajas anidadas · `contr` = textos bajo el umbral de contraste.\n")

    add("## Señales por patrón\n")
    by_signal: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        for s in signals(row):
            by_signal[s].append(row["route"])
    if not by_signal:
        add("Ninguna ruta supera los umbrales.\n")
    else:
        add("| patrón | rutas | dónde |")
        add("|---|---|---|")
        for sig, routes in sorted(by_signal.items(), key=lambda kv: -len(kv[1])):
            shown = ", ".join(f"`{r}`" for r in routes[:6])
            more = f" +{len(routes) - 6}" if len(routes) > 6 else ""
            add(f"| {sig} | {len(routes)}/{len(rows)} | {shown}{more} |")
        add("")
        add("Un patrón presente en varias rutas casi nunca son varios problemas: es **un**")
        add("componente compartido. Rastréalo antes de escribir una tarea por pantalla.\n")

    add("## Sistema visual real del sitio\n")
    for title, path_keys, key in [
        ("Tamaños de fuente", ("typography", "sizes"), "value"),
        ("Pesos", ("typography", "weights"), "value"),
        ("Familias", ("typography", "families"), "value"),
        ("Colores de texto", ("colors", "text"), "value"),
    ]:
        presence = Counter()
        for row in rows:
            for item in dig(row["inventory"], *path_keys, default=[]):
                presence[item[key]] += 1
        if not presence:
            continue
        add(f"**{title}** ({len(presence)} distintos en todo el sitio)\n")
        add("| valor | rutas |")
        add("|---|---|")
        for value, count in presence.most_common(12):
            add(f"| `{value}` | {count}/{len(rows)} |")
        rare = [v for v, c in presence.items() if c == 1]
        if rare:
            add("")
            add(f"Aparecen en una sola ruta ({len(rare)}): " + ", ".join(f"`{v}`" for v in rare[:15]))
        add("")
    add("Lo que aparece en una sola ruta es una excepción: o se justifica, o vuelve al sistema.\n")

    add("## Muestreo propuesto\n")
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        groups[row["signature"]].append(row)
    add(f"{len(groups)} arquetipos detectados por firma de composición. Critica a fondo un")
    add("representante de cada uno — el que más señales acumule — y trata el resto por")
    add("herencia del componente compartido.\n")
    add("| arquetipo | rutas | representante sugerido |")
    add("|---|---|---|")
    for sig, members in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        rep = max(members, key=lambda r: len(signals(r)))
        add(f"| {sig} | {len(members)} | `{rep['route']}` |")
    add("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Mapa de patrones a partir de inventarios por ruta.")
    parser.add_argument("directory", type=Path, help="Directorio con los JSON de sweep.mjs")
    parser.add_argument("--format", choices=("md", "json"), default="md")
    args = parser.parse_args()

    if not args.directory.is_dir():
        print(f"No es un directorio: {args.directory}", file=sys.stderr)
        return 2

    rows = load(args.directory)
    if not rows:
        print(f"Sin inventarios en {args.directory}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(
            [{"route": r["route"], "metrics": r["metrics"], "signals": signals(r), "signature": r["signature"]}
             for r in rows],
            ensure_ascii=False, indent=2,
        ))
    else:
        print(render_markdown(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
