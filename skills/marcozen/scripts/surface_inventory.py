#!/usr/bin/env python3
"""Inventario determinista de la superficie alcanzable de un repositorio.

Enumera, leyendo solo archivos, lo que una auditoría de seguridad no debe muestrear:
tablas y su estado de RLS declarado, políticas, funciones SECURITY DEFINER, grants,
buckets, endpoints, server actions, edge functions, configuración local de auth y
señales de riesgo en el código.

    python3 scripts/surface_inventory.py [RAIZ]          # informe Markdown
    python3 scripts/surface_inventory.py [RAIZ] --json   # mismo contenido en JSON

Límites, que el informe repite:

- Es solo lectura y no usa la red. No consulta al proveedor ni al despliegue.
- Lee la INTENCIÓN declarada en el repositorio. El estado efectivo en producción
  se comprueba en el proveedor (ver references/external-surface.md).
- Todo resultado es una PISTA para verificar, no un veredicto. La ausencia de una
  señal tampoco prueba nada: el patrón puede estar escrito de otra forma.
- Nunca imprime valores de variables: solo nombres y ubicaciones.
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

SKIP_DIRS = {
    "node_modules", ".git", ".next", ".nuxt", ".svelte-kit", ".vercel", ".netlify",
    "dist", "build", "out", "coverage", ".turbo", ".cache", "vendor", "__pycache__",
    ".venv", "venv",
}
CODE_EXT = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro"}
MAX_BYTES = 1_500_000

IDENT = r'(?:"[^"]+"|[A-Za-z_][\w$]*)'
QNAME = rf'(?:{IDENT}\s*\.\s*)?{IDENT}'

AUTH_SIGNAL = re.compile(
    r"getUser\s*\(|getSession\s*\(|getServerSession\s*\(|getClaims\s*\(|currentUser\s*\(|"
    r"\bauth\s*\(\s*\)|requireAuth|requireUser|requireAdmin|requireRole|verifyToken|"
    r"jwtVerify|withAuth|isAuthenticated|getToken\s*\(|validateRequest|verifySession",
    re.I,
)
SIGNATURE_SIGNAL = re.compile(
    r"constructEvent|verifySignature|createHmac|timingSafeEqual|svix|x-signature|"
    r"stripe-signature|x-hub-signature|webhook[-_]?secret",
    re.I,
)
SENSITIVE_IN_CLIENT = re.compile(
    r"SERVICE_ROLE|service_role|SECRET_KEY|PRIVATE_KEY|ADMIN_KEY|DATABASE_URL"
)
PUBLIC_SECRET_ENV = re.compile(
    r"\b((?:NEXT_PUBLIC_|VITE_|PUBLIC_|EXPO_PUBLIC_|REACT_APP_|NUXT_PUBLIC_)\w*"
    r"(?:SECRET|SERVICE_ROLE|PRIVATE|PASSWORD|ADMIN)\w*)"
)
HTTP_METHODS = re.compile(
    r"export\s+(?:async\s+)?(?:function|const)\s+(GET|POST|PUT|PATCH|DELETE|OPTIONS|HEAD)\b"
)


def norm(name):
    """Normaliza un identificador SQL: sin comillas, sin esquema public."""
    parts = [p.strip().strip('"') for p in name.split(".")]
    if len(parts) == 2 and parts[0].lower() == "public":
        parts = parts[1:]
    return ".".join(p.lower() for p in parts)


def walk(root):
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            entries = sorted(current.iterdir())
        except OSError:
            continue
        for entry in entries:
            if entry.is_symlink():
                continue
            if entry.is_dir():
                if entry.name not in SKIP_DIRS:
                    stack.append(entry)
            elif entry.is_file():
                yield entry


def read(path):
    try:
        if path.stat().st_size > MAX_BYTES:
            return None
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def blank(match):
    """Reemplaza el cuerpo por espacios conservando saltos de línea y posiciones."""
    return re.sub(r"[^\n]", " ", match.group(0))


def scan_sql(root, files, out):
    tables = {}
    for path in files:
        text = read(path)
        if text is None:
            continue
        rel = str(path.relative_to(root))
        clean = re.sub(r"--[^\n]*", blank, text)
        clean = re.sub(r"/\*.*?\*/", blank, clean, flags=re.S)
        clean = re.sub(r"(\$[A-Za-z_]*\$).*?\1", blank, clean, flags=re.S)

        for m in re.finditer(
            rf"create\s+(?:unlogged\s+)?table\s+(?:if\s+not\s+exists\s+)?({QNAME})", clean, re.I
        ):
            name = norm(m.group(1))
            tables.setdefault(
                name, {"tabla": name, "definida_en": f"{rel}:{line_of(clean, m.start())}",
                       "rls_declarado": False, "politicas": 0, "politicas_permisivas": []}
            )
        for m in re.finditer(
            rf"alter\s+table\s+(?:if\s+exists\s+)?(?:only\s+)?({QNAME})\s+"
            r"(enable|disable|force)\s+row\s+level\s+security", clean, re.I
        ):
            name = norm(m.group(1))
            entry = tables.setdefault(
                name, {"tabla": name, "definida_en": "(no encontrada en el repo)",
                       "rls_declarado": False, "politicas": 0, "politicas_permisivas": []}
            )
            entry["rls_declarado"] = m.group(2).lower() != "disable"
        for m in re.finditer(
            rf"create\s+policy\s+({IDENT})\s+on\s+({QNAME})(.*?);", clean, re.I | re.S
        ):
            name = norm(m.group(2))
            entry = tables.setdefault(
                name, {"tabla": name, "definida_en": "(no encontrada en el repo)",
                       "rls_declarado": False, "politicas": 0, "politicas_permisivas": []}
            )
            entry["politicas"] += 1
            body = re.sub(r"\s+", " ", m.group(3)).lower()
            if re.search(r"(using|with check)\s*\(\s*true\s*\)", body):
                entry["politicas_permisivas"].append(
                    f"{m.group(1).strip(chr(34))} ({rel}:{line_of(clean, m.start())})"
                )
        for m in re.finditer(
            rf"create\s+(?:or\s+replace\s+)?function\s+({QNAME})(.*?);", clean, re.I | re.S
        ):
            header = m.group(2).lower()
            if "security definer" in header:
                out["funciones_security_definer"].append({
                    "funcion": norm(m.group(1)),
                    "ubicacion": f"{rel}:{line_of(clean, m.start())}",
                    "fija_search_path": "search_path" in header,
                })
        for m in re.finditer(
            rf"create\s+(?:or\s+replace\s+)?(?:materialized\s+)?view\s+({QNAME})(.*?)\bas\b",
            clean, re.I | re.S
        ):
            out["vistas"].append({
                "vista": norm(m.group(1)),
                "ubicacion": f"{rel}:{line_of(clean, m.start())}",
                "security_invoker": "security_invoker" in m.group(2).lower(),
            })
        for m in re.finditer(
            r"grant\s+([\w\s,]+?)\s+on\s+(.+?)\s+to\s+([^;]+);", clean, re.I | re.S
        ):
            roles = re.sub(r"\s+", " ", m.group(3)).lower()
            if re.search(r"\b(anon|authenticated|public)\b", roles):
                out["grants_a_roles_de_api"].append({
                    "privilegios": re.sub(r"\s+", " ", m.group(1)).strip().lower(),
                    "sobre": re.sub(r"\s+", " ", m.group(2)).strip().lower()[:80],
                    "a": roles.strip()[:60],
                    "ubicacion": f"{rel}:{line_of(clean, m.start())}",
                })
        # Los literales se buscan en el texto original: el enmascarado no los toca,
        # pero un bucket puede crearse dentro de un bloque DO $$ ... $$.
        for m in re.finditer(r"insert\s+into\s+storage\.buckets(.*?);", text, re.I | re.S):
            stmt = m.group(1).lower()
            out["buckets"].append({
                "ubicacion": f"{rel}:{line_of(text, m.start())}",
                "posible_publico": bool(re.search(r"\btrue\b", stmt)),
            })
    out["tablas"] = sorted(tables.values(), key=lambda t: t["tabla"])


def scan_supabase_config(root, out):
    path = root / "supabase" / "config.toml"
    if not path.is_file():
        return
    text = read(path) or ""
    # Lector mínimo por secciones: basta para claves escalares y no depende de la
    # versión de Python (tomllib solo existe desde 3.11).
    wanted = {
        "enable_signup", "enable_anonymous_sign_ins", "enable_confirmations",
        "enable_manual_linking", "site_url", "additional_redirect_urls",
        "verify_jwt", "enabled",
    }
    found = {}
    section = ""
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip() if not re.search(r"""['"].*#""", raw) else raw.strip()
        header = re.match(r"^\[+\s*([^\]]+?)\s*\]+$", line)
        if header:
            section = header.group(1)
            continue
        pair = re.match(r"^([A-Za-z_][\w-]*)\s*=\s*(.+)$", line)
        if not pair or pair.group(1) not in wanted:
            continue
        key, value = pair.group(1), pair.group(2).strip()
        if key == "enabled" and not section.startswith("auth.external."):
            continue
        if not (section == "auth" or section.startswith("auth.") or section.startswith("functions.")):
            continue
        found[f"{section}.{key}"] = value.strip('"')
    out["supabase_config_local"] = found


def route_from_path(rel):
    path = "/" + rel
    path = re.sub(r"^/(src/)?", "/", path)
    path = re.sub(r"^/(app|pages)/", "/", path)
    path = re.sub(r"/route\.\w+$|/\+server\.\w+$|\.\w+$", "", path)
    path = re.sub(r"/\([^/]+\)", "", path)
    path = re.sub(r"/index$", "", path)
    return path or "/"


def scan_code(root, files, out):
    for path in files:
        rel = str(path.relative_to(root)).replace("\\", "/")
        text = read(path)
        if text is None:
            continue
        head = text[:400]
        is_client = bool(re.search(r"""^\s*['"]use client['"]""", head, re.M))
        is_server_action = bool(re.search(r"""['"]use server['"]""", text))
        has_auth = bool(AUTH_SIGNAL.search(text))

        endpoint = None
        if re.search(r"(^|/)app/.*(^|/)route\.(ts|js|mjs)$", rel):
            endpoint = "route handler"
        elif re.search(r"(^|/)pages/api/.+\.(ts|js|mjs)$", rel):
            endpoint = "pages/api"
        elif re.search(r"(^|/)routes/.*\+server\.(ts|js)$", rel):
            endpoint = "sveltekit endpoint"
        elif re.search(r"(^|/)supabase/functions/[^/_][^/]*/index\.(ts|js)$", rel):
            endpoint = "edge function"
        elif re.search(r"(^|/)(netlify/functions|api)/[^/]+\.(ts|js|mjs)$", rel) \
                and "/pages/" not in rel and "/app/" not in "/" + rel:
            endpoint = "función serverless"
        if endpoint:
            methods = sorted(set(HTTP_METHODS.findall(text)))
            item = {
                "tipo": endpoint,
                "ruta": route_from_path(rel),
                "archivo": rel,
                "metodos": ", ".join(methods) or "—",
                "senal_de_auth_en_archivo": has_auth,
            }
            if "webhook" in rel.lower():
                item["senal_de_firma"] = bool(SIGNATURE_SIGNAL.search(text))
            out["endpoints"].append(item)

        if is_server_action and not endpoint:
            actions = re.findall(r"export\s+(?:default\s+)?async\s+function\s+(\w+)", text)
            actions += re.findall(r"export\s+const\s+(\w+)\s*=\s*async", text)
            if actions:
                out["server_actions"].append({
                    "archivo": rel,
                    "acciones": ", ".join(sorted(set(actions))[:12]),
                    "senal_de_auth_en_archivo": has_auth,
                })

        if re.search(r"(^|/)(src/)?middleware\.(ts|js)$", rel):
            matcher = re.search(r"matcher\s*:\s*(\[[^\]]*\]|['\"][^'\"]+['\"])", text, re.S)
            out["middleware"].append({
                "archivo": rel,
                "matcher": re.sub(r"\s+", " ", matcher.group(1))[:160] if matcher else "(sin matcher: aplica a todo)",
            })

        if is_client:
            for m in SENSITIVE_IN_CLIENT.finditer(text):
                out["sensible_en_cliente"].append({
                    "ubicacion": f"{rel}:{line_of(text, m.start())}", "nombre": m.group(0)})
        for m in PUBLIC_SECRET_ENV.finditer(text):
            out["env_publica_con_nombre_sensible"].append({
                "ubicacion": f"{rel}:{line_of(text, m.start())}", "variable": m.group(1)})
        for m in re.finditer(r"\buser_metadata\b|\braw_user_meta_data\b", text):
            out["authz_sobre_user_metadata"].append(f"{rel}:{line_of(text, m.start())}")
        for m in re.finditer(r"dangerouslySetInnerHTML|\bv-html\b|\{@html\b|\.innerHTML\s*=", text):
            out["html_sin_escapar"].append(f"{rel}:{line_of(text, m.start())}")
        for m in re.finditer(r"\.rpc\(\s*['\"`]([\w.]+)['\"`]", text):
            out["rpc_invocadas"][m.group(1)].append(f"{rel}:{line_of(text, m.start())}")
        for m in re.finditer(r"\.from\(\s*['\"`]([\w.]+)['\"`]\s*\)", text):
            out["tablas_usadas_desde_codigo"].add(m.group(1).lower())


def scan_env_files(root, files, out):
    for path in files:
        if not re.match(r"\.env(\..+)?$", path.name):
            continue
        text = read(path) or ""
        rel = str(path.relative_to(root))
        for m in PUBLIC_SECRET_ENV.finditer(text):
            out["env_publica_con_nombre_sensible"].append({
                "ubicacion": f"{rel}:{line_of(text, m.start())}", "variable": m.group(1)})


def tracked_env(root, out):
    try:
        res = subprocess.run(
            ["git", "-C", str(root), "ls-files"], capture_output=True, text=True, timeout=30
        )
    except (OSError, subprocess.SubprocessError):
        out["env_versionados"] = None
        return
    if res.returncode != 0:
        out["env_versionados"] = None
        return
    out["env_versionados"] = [
        f for f in res.stdout.splitlines()
        if re.search(r"(^|/)\.env($|\.)", f) and not re.search(r"example|sample|template", f, re.I)
    ]


def build(root):
    out = {
        "tablas": [], "funciones_security_definer": [], "vistas": [],
        "grants_a_roles_de_api": [], "buckets": [], "supabase_config_local": None,
        "endpoints": [], "server_actions": [], "middleware": [],
        "sensible_en_cliente": [], "env_publica_con_nombre_sensible": [],
        "authz_sobre_user_metadata": [], "html_sin_escapar": [],
        "rpc_invocadas": defaultdict(list), "tablas_usadas_desde_codigo": set(),
        "env_versionados": None,
    }
    files = list(walk(root))
    scan_sql(root, [f for f in files if f.suffix.lower() == ".sql"], out)
    scan_supabase_config(root, out)
    scan_code(root, [f for f in files if f.suffix.lower() in CODE_EXT], out)
    scan_env_files(root, files, out)
    tracked_env(root, out)

    declared = {t["tabla"].split(".")[-1] for t in out["tablas"]}
    out["tablas_usadas_sin_definicion_en_repo"] = sorted(
        t for t in out["tablas_usadas_desde_codigo"] if t.split(".")[-1] not in declared
    ) if out["tablas"] else []
    out["tablas_usadas_desde_codigo"] = sorted(out["tablas_usadas_desde_codigo"])
    out["rpc_invocadas"] = {k: v[:5] for k, v in sorted(out["rpc_invocadas"].items())}
    out["endpoints"].sort(key=lambda e: e["ruta"])
    seen = set()
    unique = []
    for item in out["env_publica_con_nombre_sensible"]:
        if item["ubicacion"] not in seen:
            seen.add(item["ubicacion"])
            unique.append(item)
    out["env_publica_con_nombre_sensible"] = unique
    return out


def yn(value):
    return "sí" if value else "NO"


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def render(root, d):
    p = []
    add = p.append
    add(f"# Inventario de superficie — {root.name}\n")
    add("> Solo lectura, sin red. Refleja la **intención declarada en el repositorio**, no el "
        "estado efectivo en producción. Cada fila es una **pista a verificar**, no un veredicto; "
        "una señal ausente tampoco prueba nada. No se imprimen valores de variables.\n")

    add("## Tablas y RLS declarado\n")
    if d["tablas"]:
        rows = []
        for t in d["tablas"]:
            note = []
            if not t["rls_declarado"]:
                note.append("**sin RLS declarado**")
            elif t["politicas"] == 0:
                note.append("RLS sin políticas: niega todo")
            if t["politicas_permisivas"]:
                note.append("política `true`: " + "; ".join(t["politicas_permisivas"][:3]))
            rows.append([f"`{t['tabla']}`", yn(t["rls_declarado"]), t["politicas"],
                         t["definida_en"], " · ".join(note) or "—"])
        add(table(["Tabla", "RLS declarado", "Políticas", "Definida en", "Revisar"], rows))
        missing = [t["tabla"] for t in d["tablas"] if not t["rls_declarado"]]
        add(f"\n{len(d['tablas'])} tablas; {len(missing)} sin RLS declarado en el repositorio."
            " El estado efectivo se confirma en el catálogo del servidor.")
    else:
        add("No se encontraron `CREATE TABLE` en archivos `.sql`. Si el producto tiene base de "
            "datos, su esquema no está versionado aquí: el inventario de tablas es "
            "`No verificado` desde el repositorio.")
    if d["tablas_usadas_sin_definicion_en_repo"]:
        add("\n**Tablas usadas desde el código sin definición en el repositorio** (creadas por "
            "fuera de las migraciones; su RLS no es deducible aquí): "
            + ", ".join(f"`{t}`" for t in d["tablas_usadas_sin_definicion_en_repo"]))

    if d["funciones_security_definer"]:
        add("\n## Funciones `SECURITY DEFINER`\n")
        add("Se ejecutan con los permisos de su dueño y saltan RLS. Verifica quién puede "
            "invocarlas y que validen al llamante.\n")
        add(table(["Función", "Ubicación", "Fija `search_path`"],
                  [[f"`{f['funcion']}`", f["ubicacion"], yn(f["fija_search_path"])]
                   for f in d["funciones_security_definer"]]))
    if d["vistas"]:
        add("\n## Vistas\n")
        add(table(["Vista", "Ubicación", "`security_invoker`"],
                  [[f"`{v['vista']}`", v["ubicacion"], yn(v["security_invoker"])]
                   for v in d["vistas"]]))
    if d["grants_a_roles_de_api"]:
        add("\n## `GRANT` a roles alcanzables por la API\n")
        add(table(["Privilegios", "Sobre", "A", "Ubicación"],
                  [[g["privilegios"], f"`{g['sobre']}`", g["a"], g["ubicacion"]]
                   for g in d["grants_a_roles_de_api"][:60]]))
    if d["buckets"]:
        add("\n## Buckets creados en SQL\n")
        add(table(["Ubicación", "Posible público"],
                  [[b["ubicacion"], "**revisar**" if b["posible_publico"] else "no aparente"]
                   for b in d["buckets"]]))

    cfg = d["supabase_config_local"]
    if cfg is not None:
        add("\n## Configuración local de Supabase (`supabase/config.toml`)\n")
        add("Es la configuración del entorno **local** y de lo que se despliega con el CLI. "
            "No prueba la configuración del proyecto en producción.\n")
        if cfg:
            add(table(["Clave", "Valor"], [[f"`{k}`", f"`{v}`"] for k, v in cfg.items()]))
        else:
            add("Sin claves de registro, proveedores ni `verify_jwt` declaradas.")

    add("\n## Endpoints\n")
    if d["endpoints"]:
        rows = []
        for e in d["endpoints"]:
            extra = ""
            if "senal_de_firma" in e:
                extra = "firma: " + ("sí" if e["senal_de_firma"] else "**NO**")
            rows.append([e["tipo"], f"`{e['ruta']}`", e["metodos"],
                         yn(e["senal_de_auth_en_archivo"]), extra or "—", e["archivo"]])
        add(table(["Tipo", "Ruta", "Métodos", "Señal de auth en el archivo", "Webhook", "Archivo"],
                  rows))
        no_auth = sum(1 for e in d["endpoints"] if not e["senal_de_auth_en_archivo"])
        add(f"\n{len(d['endpoints'])} endpoints; {no_auth} sin señal de auth en su propio "
            "archivo. Puede estar en middleware o en un helper con otro nombre: léelos.")
    else:
        add("No se detectaron endpoints con los patrones conocidos.")
    if d["server_actions"]:
        add("\n## Server actions\n")
        add(table(["Archivo", "Acciones", "Señal de auth en el archivo"],
                  [[s["archivo"], s["acciones"], yn(s["senal_de_auth_en_archivo"])]
                   for s in d["server_actions"]]))
    if d["middleware"]:
        add("\n## Middleware\n")
        add(table(["Archivo", "Matcher"], [[m["archivo"], f"`{m['matcher']}`"]
                                           for m in d["middleware"]]))

    add("\n## Señales de riesgo en el código\n")
    signals = [
        ("Nombre sensible referenciado en un archivo `use client`",
         [f"{i['ubicacion']} (`{i['nombre']}`)" for i in d["sensible_en_cliente"]]),
        ("Variable con prefijo público y nombre sensible",
         [f"{i['ubicacion']} (`{i['variable']}`)" for i in d["env_publica_con_nombre_sensible"]]),
        ("Uso de `user_metadata` (editable por el propio usuario; no sirve para autorizar)",
         d["authz_sobre_user_metadata"]),
        ("HTML sin escapar", d["html_sin_escapar"]),
    ]
    any_signal = False
    for title, items in signals:
        if items:
            any_signal = True
            add(f"- **{title}:** " + ", ".join(items[:15])
                + (f" … (+{len(items) - 15})" if len(items) > 15 else ""))
    if d["rpc_invocadas"]:
        any_signal = True
        add("- **RPC invocadas desde el código:** "
            + ", ".join(f"`{k}` ({v[0]})" for k, v in d["rpc_invocadas"].items()))
    if d["env_versionados"]:
        any_signal = True
        add("- **`.env` versionados (inspección prioritaria, sin mostrar valores):** "
            + ", ".join(f"`{f}`" for f in d["env_versionados"]))
    elif d["env_versionados"] is None:
        add("- `.env` versionados: no verificado (no es un repositorio Git o `git` falló).")
    if not any_signal:
        add("- Ninguna con los patrones conocidos.")
    add("")
    return "\n".join(p)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("root", nargs="?", default=".", help="raíz del repositorio a inventariar")
    parser.add_argument("--json", action="store_true", help="emitir JSON en vez de Markdown")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"No es un directorio: {root}", file=sys.stderr)
        return 2
    data = build(root)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(render(root, data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
