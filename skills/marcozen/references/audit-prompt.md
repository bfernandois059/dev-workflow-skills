# Auditoría MarcoZen — Detalle Operativo y Prompt Maestro

Este archivo contiene:
1. **Guía operativa por dominio**: Comandos y señales de inspección para el agente durante la auditoría.
2. **Prompt maestro reutilizable**: Instrucción estructurada para ejecutar una auditoría MarcoZen evidence-first.

---

## Parte 1 — Guía operativa por dominio

Reglas indispensables:
- **Solo lectura estricta:** No modificar archivos, ramas ni configuraciones.
- **Evidencia observable:** Distinguir entre `Verificado OK`, `Hallazgo`, `No verificado` y `N/A`.
- **Máxima prudencia con secretos:** Nunca mostrar el valor de un secreto. Reportar solo tipo y ubicación (`archivo:línea`).
- **El repositorio no es el sistema:** un control aplicable que no se puede verificar leyendo archivos se reporta `No verificado — verificación externa requerida` con el lugar donde se comprueba. Omitirlo es un fallo de auditoría, no un `N/A`. Ver [`external-surface.md`](external-surface.md).

### 1. Git y ramas
Comandos útiles (solo lectura):
```bash
# 1. Detectar y validar la rama base/default real del remoto (sin asumir main, master ni develop, y sin usar la rama checkout local):
BASE_BRANCH=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's@^origin/@@')
[ -z "$BASE_BRANCH" ] && BASE_BRANCH=$(git remote show origin 2>/dev/null | sed -n 's/.*HEAD branch: //p')

# Validar que no esté vacía, que no sea '(unknown)' y que la referencia remota exista realmente:
if [ -n "$BASE_BRANCH" ] && [ "$BASE_BRANCH" != "(unknown)" ] && git show-ref --verify --quiet "refs/remotes/origin/$BASE_BRANCH"; then
  DEFAULT_BRANCH_VERIFIED=true
else
  BASE_BRANCH=""
  DEFAULT_BRANCH_VERIFIED=false
fi

# Si DEFAULT_BRANCH_VERIFIED no es true (ej. origin/HEAD ausente, remoto devuelve (unknown) o referencia inexistente):
# NO inventar un nombre ni sustituir por la rama local actualmente checkout.
# Reportar: "No verificado: no fue posible determinar con certeza la rama base/default del repositorio."
# No ejecutar comparaciones --merged/--no-merged sobre una base incierta (solicitar confirmación al usuario si es indispensable).

# 2. Inspección respecto a la base remota demostrada (solo si DEFAULT_BRANCH_VERIFIED es true):
git branch -a --sort=-committerdate                 # ramas por actividad reciente
[ "$DEFAULT_BRANCH_VERIFIED" = true ] && git branch -r --merged "origin/$BASE_BRANCH"        # ramas remotas fusionadas (candidatas a poda)
[ "$DEFAULT_BRANCH_VERIFIED" = true ] && git branch -r --no-merged "origin/$BASE_BRANCH"     # ramas con trabajo pendiente
git log --oneline -10                               # últimos commits en rama activa
git status --porcelain                              # estado del working tree
git tag --sort=-creatordate | head -5               # releases recientes
```
- **Hallazgo P1/P2:** Decenas de ramas abandonadas sin propósito, commits con mensajes crípticos continuos, ramas fusionadas que saturan el repositorio remoto.
- **Verificado OK:** Poca dispersión de ramas, historial limpio, sincronización regular con la rama base detectada.

### 2. Documentación
Verificar presencia y **utilidad real** según la naturaleza del proyecto:
- Proyectos con equipo/handoff: `README.md` (propósito, setup local, mapa del repo), variables en `.env.example`, runbook de despliegue si aplica.
- Proyectos mantenidos por agentes: `AGENTS.md` o reglas persistentes.
- **Importante:** La falta de un documento solo es hallazgo si existe una necesidad operativa no cubierta. Si el proyecto es mínimo y autoexplicativo, no exigir documentación extensa artificialmente.

### 3. Arquitectura y dependencias
- Inspeccionar manifiestos según stack (`package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, `Gemfile`, `composer.json`).
- Verificar scripts de ejecución, dependencias duplicadas o manifiestos inconsistentes.
- Pregunta clave: ¿la estructura de carpetas expresa claramente los límites y responsabilidades del sistema?

### 4. Seguridad — Detección rigurosa y descarte de falsos positivos
Búsqueda no destructiva de credenciales y variables versionadas:
```bash
git ls-files | grep -E '(^|/)\.env($|\.)' | grep -v example   # posibles .env versionados: inspección prioritaria
grep -rInE '(api[_-]?key|secret|token|password|passwd|bearer|private[_-]?key)' \
  --include=*.{js,ts,json,yml,yaml,env,py,rb,go,php} . | head -20
```

**Inspección de `.env` y descarte de falsos positivos:**
- **Inspección prioritaria de `.env`:** Encontrar un `.env` versionado requiere inspección inmediata del contenido, pero el nombre o presencia del archivo por sí solos no demuestran exposición de secretos.
  - Clasifica como **P0** únicamente cuando se verifique que contiene o contenía credenciales, tokens, passwords, connection strings sensibles u otros secretos reales comprometidos.
  - Un `.env` que solo contiene variables de configuración no sensibles (puertos locales, URLs públicas, flags de entorno) es una mala práctica potencial o hallazgo contextual, pero su severidad depende del riesgo real (P2/P3).
  - **NUNCA muestres los valores encontrados en el informe ni en la conversación.**
- **Descarte obligatorio de falsos positivos antes de alertar P0:**
  - **Roles y permisos SQL/RLS:** Nombres como `service_role`, `anon`, `authenticated` en políticas RLS o archivos `.sql` son roles de base de datos, no secretos.
  - **Identificadores de variables:** `STRIPE_SECRET_KEY=` vacío en `.env.example` o referencias en código `process.env.MI_VARIABLE` son identificadores legítimos.
  - **Claves diseñadas para ser públicas:** `NEXT_PUBLIC_*`, anon keys de Supabase o claves publicables de Stripe (`pk_...`) no son secretos.
  - **Tokens simulados en tests:** Strings aleatorios dentro de suites de prueba, mocks o fixtures.

> **P0 Real:** Un valor auténtico de un secreto sensible o credencial de producción comprometido en el repositorio o en el historial.

### 4.b Superficie alcanzable y controles del proveedor
Aplica en los modos de seguridad y pre-producción, y solo si el producto tiene usuarios o datos de terceros.

1. **Establece el modelo de acceso declarado** (`Público sin cuentas`, `Registro abierto`, `Registro restringido`, `Provisión por administrador`, `Interno`). Si ninguna fuente lo declara, pregúntalo: gobierna la severidad de todo el dominio, y su ausencia es un hallazgo en sí misma.
2. **Enumera la superficie** desde el código —rutas, endpoints, tablas, buckets, webhooks, jobs— y marca cada punto con el control que lo protege.
3. **Evalúa cada punto frente a tres visitantes:** anónimo, autenticado ajeno al recurso (IDOR/BOLA y fugas entre inquilinos) y autenticado con rol menor.
4. **Verifica los controles del proveedor** que no dejan rastro en el código: registro de cuentas y proveedores OAuth activos, estado efectivo de las políticas de base de datos, visibilidad de buckets, protección de entornos de preview, alcance de las claves emitidas. Usa la sonda de solo lectura cuando exista:

```bash
# Configuración pública de autenticación (Supabase/GoTrue). Clave anónima, pública por diseño.
curl -s "$SUPABASE_URL/auth/v1/settings" -H "apikey: $SUPABASE_ANON_KEY"
```

5. **Si hay URL desplegada confirmada por el usuario, ejecuta el pase de sondas de solo lectura** sobre ella: rutas privadas sin sesión, redirecciones con destino parametrizado, cabeceras realmente servidas, métodos aceptados, mensajes de login y recuperación, páginas de error, sourcemaps, DNS y subdominios colgantes. Una petición por control, nada destructivo, nada que cree estado sin autorización. Ver [`deployed-surface.md`](deployed-surface.md).
6. **Lo no verificable se entrega como lista corta de verificación externa**, con el lugar exacto y la respuesta correcta para este producto. Nunca como una advertencia genérica de «revisar la configuración del proveedor»: eso no se puede cerrar.

El catálogo por proveedor, las severidades contra el modelo declarado y los falsos positivos a descartar están en [`external-surface.md`](external-surface.md).

### 5. Calidad técnica y verificación
Adaptar al stack real del proyecto:
- Proyectos con linter/formatter/typecheck: verificar si las herramientas están configuradas y corren limpias.
- **Evaluación contextual de tests rotos:** No declarar automáticamente que tests rotos = P0/P1. Evalúa qué test falla, qué funcionalidad protege, si representa una regresión real, si bloquea build/deploy o si es un test obsoleto o flaky (un E2E de checkout roto por regresión es P0/P1; un snapshot secundario desactualizado o test flaky sin impacto funcional es P2/P3). Si el proyecto es puramente estático o declarativo, **no penalizar por falta de tests unitarios**.
- **Evaluación contextual de dependencias vulnerables (CVEs):** No asumir que CVE detectada = P0/P1 automáticamente. Evalúa severidad oficial, versión afectada, entorno (producción vs dependencias de desarrollo sin impacto en runtime), reachability y si existe fix o mitigación disponible.
- Detección de deuda técnica visible:
```bash
grep -rInE 'TODO|FIXME|HACK|XXX' --include=*.{js,ts,py,go,rb,php} . | wc -l
```

### 6. Despliegue y operación
- Proceso de build y despliegue: verificar si existe un proceso funcional, reproducible y suficientemente documentado según el riesgo y operación del proyecto (automatizado mediante CI/CD cuando el contexto operacional lo justifique; procedimiento manual documentado y reproducible cuando la simplicidad del proyecto lo haga válido).
- ¿Están identificadas las variables de entorno necesarias para operar en producción?
- Para sistemas operacionales: verificar existencia de procedimientos de respaldo y rollback.

### 7. SEO, AEO e identidad visible (solo si es web pública indexable)
- Si el proyecto es una API privada, herramienta interna o librería: marcar este dominio como **N/A**.
- Si es web pública indexable:
  - **`sitemap.xml`:** Evaluar presencia y canonicidad. Su ausencia es un hallazgo importante (P1/P2) en sitios grandes o dinámicos dependientes de captación orgánica continua; en sitios pequeños su impacto es menor.
  - **`robots.txt`:** La ausencia de `robots.txt` no bloquea el crawling (los buscadores rastrean normalmente por defecto sin él); es una recomendación contextual o P3 para declarar sitemap o reglas directivas. En cambio, un `robots.txt` presente que bloquee por error rutas públicas que deban indexarse (`Disallow: /`) sí es un hallazgo crítico P0/P1.
  - Metadatos, OpenGraph y páginas de error (404/500).
- La falta de optimizaciones como `llms.txt` es **P3**, nunca un bloqueador de producción.

---

## Parte 2 — Prompt maestro reutilizable

```
Actúa como auditor técnico sénior bajo el marco MarcoZen de Proyectos.

Principio rector: Evidence and impact > checklist completion.
Audita el proyecto que realmente existe, adaptando la profundidad al stack y contexto del producto.
No modifiques archivos ni ramas durante esta auditoría. Solo audita.

Inspecciona con evidencia verificable:
1. Contexto y stack tecnológico real.
2. Git y ramas: ramas activas, fusionadas y estado de sincronización.
3. Seguridad: detección de secretos reales (sin exponer valores), inspección prioritaria de .env versionados y dependencias críticas evaluadas por explotabilidad real.
3.b Superficie alcanzable (si hay usuarios o datos de terceros): establece el modelo de acceso
    declarado —pregúntalo si nadie lo declaró—, enumera rutas, endpoints, tablas y buckets, y
    evalúa cada punto frente a un visitante anónimo, a uno autenticado ajeno al recurso y a uno
    con rol menor. Verifica los controles que viven en el proveedor (registro de cuentas,
    políticas efectivas, visibilidad de buckets, protección de entornos, alcance de claves).
    Si hay URL desplegada confirmada por el usuario, comprueba contra ella los controles
    observables (cabeceras servidas, métodos aceptados, redirecciones con destino
    parametrizado, mensajes de login y recuperación, páginas de error, sourcemaps, DNS y
    subdominios colgantes) con peticiones individuales de solo lectura. Lo que no se pueda
    verificar se reporta No verificado con el lugar donde se comprueba; omitirlo no es una
    opción.
4. Arquitectura y dependencias: estructura modular, scripts y estado de dependencias.
5. Calidad y verificación: validaciones reales adaptadas al stack (evaluando tests y CVEs según criticidad e impacto real).
6. Operación y deploy: proceso de build y despliegue funcional y reproducible (automatizado o documentado según riesgo).
7. SEO, identidad y errores: sitemap canónico y robots contextualmente evaluados (solo si es web pública).
8. Documentación: evaluar presencia según necesidad operativa real.

Entrega un informe con la siguiente estructura:
1. Resumen ejecutivo y contexto del proyecto.
2. Alcance y tabla de aplicabilidad modular (distinguiendo Aplicable, Contextual, N/A y No verificado).
3. Hallazgos priorizados por severidad:
   - P0: Críticos / Bloqueadores reales.
   - P1: Alto impacto.
   - P2: Mejoras importantes.
   - P3: Optimizaciones.
   (Para cada hallazgo: qué se observó, evidencia concreta, impacto y acción recomendada).
4. Estado de preparación y veredicto (Listo / Listo con observaciones / No listo).
5. Verificación externa pendiente: tabla corta de controles No verificados, dónde se comprueba
   cada uno y qué respuesta sería correcta para este producto (se omite si no quedó ninguno).
6. Próximos pasos recomendados.

(El puntaje /100 es opcional y solo debe incluirse si se solicita expresamente).
```
