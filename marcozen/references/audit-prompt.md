# Auditoría MarcoZen — detalle operativo y prompt maestro

Este archivo tiene dos partes:
1. **Guía operativa**: qué comandos correr y qué mirar en cada categoría (para ti, el
   agente, cuando ejecutas la auditoría).
2. **Prompt maestro reutilizable**: texto que puedes entregar tal cual a otro
   desarrollador o agente IA para que corra la auditoría por su cuenta.

---

## Parte 1 — Guía operativa por categoría

Recuerda las reglas de la primera pasada: **solo lectura**, no exponer secretos.

### Orden Git y ramas (15 pts)

Comandos útiles (solo lectura):

```bash
git branch -a --sort=-committerdate                 # ramas por actividad reciente
git branch --merged main                            # ramas ya fusionadas (candidatas a borrar)
git branch --no-merged main                         # ramas con trabajo sin integrar
git log --oneline -15                               # últimos commits
git status --porcelain                              # working tree limpio o sucio
git tag --sort=-creatordate | head                  # releases
for b in $(git branch -r | grep -v HEAD); do echo "$b $(git log -1 --format=%cr $b)"; done
```

Penaliza: muchas ramas obsoletas sin cerrar, ramas fusionadas no borradas, working tree
sucio, ausencia de convención de ramas, historia caótica. Premia: pocas ramas vivas y con
propósito claro, `main` estable.

### Documentación (15 pts)

Verifica presencia y **utilidad real** (un README que solo dice `npm install` no vale
mucho): `README.md`, `AGENTS.md`, `PRD.md`/`PRODUCT.md`, `.env.example`, `CHANGELOG.md`,
`docs/`, `docs/adr/`. Marca documentos desactualizados o que se contradicen entre sí.

### Arquitectura (15 pts)

Revisa `package.json` (o `requirements.txt`, `go.mod`, etc.), scripts, estructura de
carpetas, separación de responsabilidades, dependencias duplicadas o abandonadas.
Pregunta clave: ¿la estructura se explica sola?

### Seguridad (15 pts) — máxima prudencia

Detecta **sin exponer** valores:

```bash
git ls-files | grep -E '(^|/)\.env($|\.)' | grep -v example   # .env versionado = P0
grep -rInE '(api[_-]?key|secret|token|password|passwd|bearer|private[_-]?key)' \
  --include=*.{js,ts,json,yml,yaml,env,py,rb,go} . | head       # posibles secretos
```

Si algo aparece, reporta **solo tipo + archivo:línea**, nunca el valor. Revisa también:
`.gitignore` cubre `.env`, `node_modules`, builds; dependencias con CVE evidentes; claves
o endpoints hardcodeados; auth básica.

**Descarta falsos positivos antes de reportar un P0.** Muchos matches del grep no son
credenciales, son código legítimo. Los más comunes:

- **Roles RLS de Supabase/Postgres**: `service_role`, `anon`, `authenticated` en policies
  o `GRANT` (`.sql`, migraciones) son **nombres de rol**, no secretos. No son P0.
- **Nombres de variable de entorno**: `SUPABASE_SERVICE_ROLE_KEY=` en `.env.example` o
  `process.env.STRIPE_SECRET_KEY` en código es el **identificador**, no el valor.
- **`NEXT_PUBLIC_*` / claves publicables**: la Supabase anon key o una publishable key de
  Stripe (`pk_...`) están **diseñadas para exponerse** al cliente. Anótalas como contexto,
  no como P0. El riesgo real es el *service_role key* o *secret key* (`sk_...`) filtrados.
- **JWT de ejemplo/fixtures**: tokens en tests, seeds o docs de ejemplo.

Antes de marcar P0, confirma que el match es un **valor real de un secreto sensible**
comprometido en el repo. Si tras verificar es un rol, un nombre de var o una clave pública,
dilo explícitamente como "falso positivo verificado" para que quien lea confíe en el juicio.

### Calidad técnica (10 pts)

Linter/formatter configurado, tests presentes y que corren, tipado, densidad de
`TODO`/`FIXME`/`HACK`, código muerto o comentado.

```bash
grep -rInE 'TODO|FIXME|HACK|XXX' --include=*.{js,ts,py,go,rb} . | wc -l
```

### Diseño/contenido (10 pts)

Solo si aplica: contenido placeholder ("Lorem ipsum", imágenes de ejemplo), coherencia
visual, assets huérfanos o sin optimizar. Si el proyecto no tiene capa visual, marca N/A.

### Deploy/operación (10 pts)

¿Cómo y dónde se despliega? ¿Variables documentadas? ¿Hay CI/CD, runbook, healthcheck,
rollback? Busca `Dockerfile`, `.github/workflows/`, `vercel.json`, `netlify.toml`,
`Procfile`, `fly.toml`, etc.

### SEO/analítica/conversión (10 pts)

Solo web/e-commerce público: `sitemap.xml`, `robots.txt`, metadatos/OpenGraph, analytics
o tag manager, tracking de conversión. Si no es público, N/A.

### Basura y duplicados

```bash
git ls-files | grep -E 'node_modules/|\.log$|\.DS_Store|\.tmp$|~$'
```

Duplicados de documentación, binarios grandes versionados, carpetas temporales.

---

## Parte 2 — Prompt maestro reutilizable

Entrega este texto tal cual cuando alguien quiera correr la auditoría MarcoZen por su
cuenta.

```
Actúa como auditor técnico y project manager digital.

Objetivo:
Auditar este repositorio bajo el marco MarcoZen de Proyectos, buscando dejarlo limpio,
podado, entendible y mantenible para cualquier desarrollador o agente IA.

No modifiques archivos en esta primera pasada. Solo audita.

Revisa:
- ramas activas
- README.md
- AGENTS.md
- PRD.md / PRODUCT.md si existe
- .env.example
- CHANGELOG.md
- docs/
- package.json
- estructura de carpetas
- scripts
- configuración de build
- variables de entorno
- integraciones
- sitemap/robots si aplica
- analytics si aplica
- seguridad básica
- deployment
- TODOs críticos
- archivos duplicados, obsoletos o basura

Evalúa con puntaje de 0 a 100:

1. Orden Git y ramas — 15 pts
2. Documentación — 15 pts
3. Arquitectura — 15 pts
4. Seguridad — 15 pts
5. Calidad técnica — 10 pts
6. Diseño/contenido — 10 pts
7. Deploy/operación — 10 pts
8. SEO/analítica/conversión — 10 pts

Entrega:
1. Resumen ejecutivo.
2. Puntaje total.
3. Tabla por categoría con puntaje, hallazgos y riesgos.
4. Archivos existentes útiles.
5. Archivos faltantes.
6. Ramas que conviene cerrar, fusionar o revisar.
7. Riesgos P0 críticos.
8. Acciones P1 recomendadas.
9. Mejoras P2.
10. Plan de poda en orden:
   - qué borrar
   - qué documentar
   - qué consolidar
   - qué proteger
   - qué revisar antes de producción
11. Veredicto final:
   - Bonsái premium
   - Ordenado con ajustes
   - Funcional pero dependiente
   - Riesgo operativo
   - Proyecto maleza

Reglas:
- No eliminar archivos.
- No cambiar código.
- No exponer secretos.
- Si encuentras credenciales, no las muestres; solo indica el tipo de secreto y dónde está.
- Si hay documentos duplicados, sugiere consolidación.
- Si falta README, AGENTS, .env.example o deployment docs, márcalo como prioridad.
```
