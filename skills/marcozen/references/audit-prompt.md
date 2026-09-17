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

### 1. Git y ramas
Comandos útiles (solo lectura):
```bash
git branch -a --sort=-committerdate                 # ramas por actividad reciente
git branch -r --merged origin/main                  # ramas remotas fusionadas (candidatas a poda)
git branch -r --no-merged origin/main               # ramas con trabajo pendiente
git log --oneline -10                               # últimos commits en rama activa
git status --porcelain                              # estado del working tree
git tag --sort=-creatordate | head -5               # releases recientes
```
- **Hallazgo P1/P2:** Decenas de ramas abandonadas sin propósito, commits con mensajes crípticos continuos, ramas fusionadas que saturan el repositorio remoto.
- **Verificado OK:** Poca dispersión de ramas, historial limpio, sincronización regular con la rama base.

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
git ls-files | grep -E '(^|/)\.env($|\.)' | grep -v example   # .env versionado = P0
grep -rInE '(api[_-]?key|secret|token|password|passwd|bearer|private[_-]?key)' \
  --include=*.{js,ts,json,yml,yaml,env,py,rb,go,php} . | head -20
```

**Descarte obligatorio de falsos positivos antes de alertar P0:**
- **Roles y permisos SQL/RLS:** Nombres como `service_role`, `anon`, `authenticated` en políticas RLS o archivos `.sql` son roles de base de datos, no secretos.
- **Identificadores de variables:** `STRIPE_SECRET_KEY=` vacío en `.env.example` o referencias en código `process.env.MI_VARIABLE` son identificadores legítimos.
- **Claves diseñadas para ser públicas:** `NEXT_PUBLIC_*`, anon keys de Supabase o claves publicables de Stripe (`pk_...`) no son secretos.
- **Tokens simulados en tests:** Strings aleatorios dentro de suites de prueba o fixtures.

> **P0 Real:** Un valor auténtico de un secreto sensible o credencial de producción comprometido en el repositorio o en el historial.

### 5. Calidad técnica y verificación
Adaptar al stack real del proyecto:
- Proyectos con linter/formatter/typecheck: verificar si las herramientas están configuradas y corren limpias.
- Tests automatizados: verificar presencia de pruebas donde aportan valor real (flujos transaccionales, lógica de dominio). Si un proyecto es puramente estático o declarativo, **no penalizar por falta de tests unitarios**.
- Detección de deuda técnica visible:
```bash
grep -rInE 'TODO|FIXME|HACK|XXX' --include=*.{js,ts,py,go,rb,php} . | wc -l
```

### 6. Despliegue y operación
- ¿Existe configuración de hosting y despliegue automatizado? (`Dockerfile`, `.github/workflows/`, `vercel.json`, `fly.toml`, etc.).
- ¿Están identificadas las variables de entorno necesarias para operar en producción?
- Para sistemas operacionales: verificar existencia de procedimientos de respaldo y rollback.

### 7. SEO, AEO e identidad visible (solo si es web pública indexable)
- Si el proyecto es una API privada, herramienta interna o librería: marcar este dominio como **N/A**.
- Si es web pública indexable: verificar `robots.txt`, `sitemap.xml`, metadatos, OpenGraph y páginas de error (404/500).
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
3. Seguridad: detección de secretos reales (sin exponer valores), .env versionados y dependencias críticas.
4. Arquitectura y dependencias: estructura modular, scripts y estado de dependencias.
5. Calidad y verificación: validaciones reales adaptadas al stack (sin imponer tooling innecesario).
6. Operación y deploy: configuración de ambientes, variables y reproducibilidad.
7. SEO, identidad y errores: páginas 404/500, metadatos e indexabilidad (solo si es web pública).
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
5. Próximos pasos recomendados.

(El puntaje /100 es opcional y solo debe incluirse si se solicita expresamente).
```
