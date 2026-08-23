# dev-workflow-skills

**Cinco Agent Skills que cubren el ciclo completo de un proyecto digital: planificar, construir, criticar, gobernar y podar.**

Skills reutilizables para Claude Code, Codex y otros agentes compatibles con el estándar
[Agent Skills](https://code.claude.com/docs/en/skills). Juntas forman un flujo de trabajo
real de desarrollo, desde la idea hasta el repositorio listo para entregar o publicar.

## El flujo

```
Idea o requerimiento
        ↓
┌─────────────────────┐
│  project-blueprint  │  Entrevista, clasifica el proyecto, define arquitectura,
│                     │  stack mínimo suficiente, datos, seguridad y documentación.
└─────────────────────┘
        ↓
Proyecto documentado y arquitectura aprobada
        ↓
┌───────────────────────┐
│  engineering-workflow │  Cada tarea: branch → implementación → validaciones →
│                       │  documentación → changelog → PR → squash merge → limpieza.
└───────────────────────┘
        ↓
Hay algo que mirar en pantalla
        ↓
┌─────────────────────┐
│      ux-critic      │  Crítica de la interfaz real: propósito, jerarquía, ritmo,
│                     │  copy, estados, sistema visual y oficio. Solo lectura.
└─────────────────────┘
        ↓
Proyecto avanzado o pre-publicación
        ↓
┌─────────────────────┐
│      marcozen       │  Auditoría, poda y gobernanza: orden del repo, seguridad,
│                     │  SEO/GEO/AEO, mantenimiento periódico, puntaje de salud.
└─────────────────────┘
        ↓
Sitio en producción (o a punto de estarlo)
        ↓
┌─────────────────────┐
│    tech-cleanup     │  Código, archivos, dependencias y assets sin uso: detección
│                     │  con evidencia y eliminación segura por etapas.
└─────────────────────┘
```

## Skills

### [project-blueprint](skills/project-blueprint/SKILL.md) — antes de programar

Convierte una idea, solicitud comercial o repositorio inmaduro en una base de proyecto
clara y validable. Entrevista, clasifica el proyecto, recomienda el stack mínimo
suficiente y define arquitectura, datos, seguridad, documentos y reglas persistentes
para agentes. No construye: prepara.

- Salida principal: **Blueprint de Proyecto** + documentos iniciales.
- Separa `Confirmado` / `Recomendado` / `Supuesto` / `Pendiente de validar`.
- Cada tecnología recomendada explica por qué se elige y qué alternativa se descartó.
- Mantiene versión SemVer propia en `skills/project-blueprint/VERSION`.

### [engineering-workflow](skills/engineering-workflow/SKILL.md) — durante el desarrollo

Ejecuta cada tarea de desarrollo de forma controlada y trazable. Requiere que el proyecto
tenga decisiones suficientes para el cambio; solo exige completar `project-blueprint`
cuando faltan definiciones necesarias de arquitectura, alcance o datos.

- Usa una política híbrida: obligatoria para implementación, PR/merge y cambios sensibles;
  opcional para documentación, copy y ajustes triviales; innecesaria para consultas o lectura.
- Nunca trabaja directamente sobre `main`; una branch, un propósito.
- Código y documentación viajan en la misma Pull Request.
- Valida con los comandos reales (lint, typecheck, tests, build) antes de declarar terminado.
- Prepara la integración, pero el merge/squash merge requiere autorización explícita.
- Mantiene versión SemVer propia en `skills/engineering-workflow/VERSION`.

### [ux-critic](skills/ux-critic/SKILL.md) — crítica de interfaz

Crítico de UX/UI que audita la interfaz **renderizada** —un sitio en local, una URL, un
flujo, una pantalla o un bloque— en vez de deducirla del código o de la documentación.
Existe porque las auditorías de usabilidad genéricas fallan siempre igual: aprueban por
ausencia de error obvio, juzgan el DOM en lugar de la pantalla y proponen parches tímidos
sobre lo ya construido.

- **Sin contexto no hay veredicto**: producto, usuario real, tarea y criterio de éxito son
  entrada obligatoria y bloqueante. La misma pantalla puede estar bien para un operador
  diario y ser inservible para alguien que llega desde un anuncio.
- **Tres niveles de exigencia** (que funcione / profesional / referencia) que cambian qué
  cuenta como hallazgo, para que no reporte lo mismo en un panel interno y en una landing.
- **Juicio en siete capas en orden fijo** —propósito, jerarquía, ritmo, copy, interacción y
  estados, sistema visual, oficio— con regla de corte: no se pule un `padding` si la
  jerarquía está rota.
- **Inventario objetivo** ejecutable sobre la página viva (`scripts/ui_inventory.js`):
  escala tipográfica en uso, paleta real, espaciados, contrastes medidos, tamaños de toque,
  esquema de encabezados y ritmo vertical. Convierte "siento que no hay jerarquía" en datos.
- **Pasada de refutación obligatoria**: antes de entregar, el crítico intenta destruir su
  propio informe. "No encontré nada" no es `OK`, es `Sin verificar`.
- Nada de números de impacto inventados. Fase de auditoría en solo lectura; corregir es una
  fase aparte que pasa por `engineering-workflow`.
- Mantiene versión SemVer propia en `skills/ux-critic/VERSION`.

### [marcozen](skills/marcozen/SKILL.md) — auditoría y gobernanza

Sistema de auditoría, poda y gobernanza para repositorios web, e-commerce y apps.
Cinco modos sobre la misma metodología:

1. **Auditoría rápida** — orden general, documentación, ramas y riesgos (puntaje 0–100).
2. **Auditoría pre-producción** — ¿listo para publicarse?
3. **Auditoría SEO/GEO/AEO** — indexación, metadata, schema, `llms.txt`, preparación para buscadores e IA.
4. **Auditoría de seguridad** — secretos, headers, formularios, webhooks, pagos, dependencias.
5. **Mantenimiento periódico** — ramas, PRs, `npm audit`/`outdated`, build, lint.

> Concepto central: un proyecto sano no es el que tiene más ramas, más documentos o más
> features. Es el que **otro profesional puede tomar sin preguntar diez veces dónde está
> cada cosa**.

- Mantiene versión SemVer propia en `skills/marcozen/VERSION`.

### [tech-cleanup](skills/tech-cleanup/SKILL.md) — código y archivos sin uso

Detecta código muerto, componentes sin uso, rutas obsoletas, imágenes/assets duplicados,
dependencias innecesarias, scripts sin uso y documentación desactualizada, y produce un plan
de eliminación segura clasificado por riesgo. Framework-agnostic: adapta los comandos al
stack real del proyecto en vez de asumir uno.

- Cada hallazgo requiere evidencia (imports, referencias dinámicas, convenciones del
  framework, metadata, build) antes de clasificarse — nunca "sin import = sin uso".
- Clasificación A–E (seguro de borrar → archivar) y dificultad Baja/Media/Alta.
- Modo multiagente opcional para repos grandes: varios agentes especializados en paralelo
  (rutas, componentes, assets, dependencias, tests/docs) más un revisor crítico final que
  cuestiona los hallazgos antes de confirmarlos. Consume más tokens — solo para cuando el
  triage inicial lo justifique.
- Fase 1 (auditoría) es siempre de solo lectura; la limpieza real es una Fase 2 aparte, por
  etapas y con aprobación explícita del usuario.
- Mantiene versión SemVer propia en `skills/tech-cleanup/VERSION`.

## Versionado

Cada skill tiene una versión SemVer y un tag independiente:

| Skill | Archivo | Tag |
|---|---|---|
| `project-blueprint` | `skills/project-blueprint/VERSION` | `project-blueprint-vX.Y.Z` |
| `engineering-workflow` | `skills/engineering-workflow/VERSION` | `engineering-workflow-vX.Y.Z` |
| `ux-critic` | `skills/ux-critic/VERSION` | `ux-critic-vX.Y.Z` |
| `marcozen` | `skills/marcozen/VERSION` | `marcozen-vX.Y.Z` |
| `tech-cleanup` | `skills/tech-cleanup/VERSION` | `tech-cleanup-vX.Y.Z` |

Consultar una versión instalada y compararla con el repositorio canónico:

```bash
python3 skills/<nombre>/scripts/check_version.py
python3 skills/<nombre>/scripts/check_version.py --check-remote
```

## Instalación

### Con el CLI de skills (recomendado)

Las cinco:

```bash
npx skills add https://github.com/bfernandois059/dev-workflow-skills
```

Una en particular:

```bash
npx skills add https://github.com/bfernandois059/dev-workflow-skills --skill marcozen
```

### Claude Code (manual)

```bash
git clone https://github.com/bfernandois059/dev-workflow-skills
mkdir -p ~/.claude/skills
cp -R dev-workflow-skills/skills/project-blueprint ~/.claude/skills/
cp -R dev-workflow-skills/skills/engineering-workflow ~/.claude/skills/
cp -R dev-workflow-skills/skills/ux-critic ~/.claude/skills/
cp -R dev-workflow-skills/skills/marcozen ~/.claude/skills/
cp -R dev-workflow-skills/skills/tech-cleanup ~/.claude/skills/
```

Para instalarlas solo en un proyecto, usa `.claude/skills/` dentro del repo en vez de
`~/.claude/skills/`.

### Codex

```bash
mkdir -p ~/.agents/skills
cp -R dev-workflow-skills/skills/project-blueprint ~/.agents/skills/
cp -R dev-workflow-skills/skills/engineering-workflow ~/.agents/skills/
cp -R dev-workflow-skills/skills/ux-critic ~/.agents/skills/
cp -R dev-workflow-skills/skills/marcozen ~/.agents/skills/
cp -R dev-workflow-skills/skills/tech-cleanup ~/.agents/skills/
```

### Otros agentes

El formato Agent Skills es markdown portable. Si tu agente no auto-carga skills, apúntalo
al `SKILL.md` de cada skill como instrucciones de método. Para auditorías, marcozen incluye
un **prompt maestro reutilizable** en
[`skills/marcozen/references/audit-prompt.md`](skills/marcozen/references/audit-prompt.md).

## Uso

| Momento | Quiero… | Cómo iniciarlo |
|---------|---------|----------------|
| Inicio | Planificar un proyecto nuevo | `/project-blueprint` o *"tengo una idea para un sitio…"* |
| Desarrollo | Implementar una tarea | `/engineering-workflow` o *"implementa este fix"* |
| Desarrollo | Criticar lo que se ve en pantalla | `/ux-critic` o *"tengo esto en localhost, dime qué está mal"* |
| Pre-entrega | ¿La interfaz aguanta que la vea el cliente? | `/ux-critic` sobre el flujo principal |
| Avanzado | Orden general del repo | `/marcozen auditoría rápida` |
| Pre-lanzamiento | ¿Listo para publicar? | `/marcozen auditoría pre-producción` |
| Pre-lanzamiento | SEO/GEO/AEO | `/marcozen revisa SEO, schema y llms.txt` |
| Siempre | Seguridad | `/marcozen auditoría de seguridad` |
| Periódico | Mantenimiento | `/marcozen mantenimiento mensual` |
| En producción | Código/archivos sin uso | `/tech-cleanup` o *"hay código muerto, límpialo"* |

## Estructura

```
skills/
├── project-blueprint/
│   ├── SKILL.md                          # método de descubrimiento, clasificación y blueprint
│   ├── VERSION                           # versión SemVer de la skill
│   ├── references/                       # cuestionario de descubrimiento, matriz de decisión
│   ├── assets/templates/                 # plantilla del blueprint
│   └── scripts/                          # inicialización y comprobación de versión
├── engineering-workflow/
│   ├── SKILL.md                          # branch → implementación → validación → PR → merge
│   ├── VERSION                           # versión SemVer de la skill
│   ├── references/                       # política de branches, riesgo, motor, docs, definition of done
│   ├── assets/templates/                 # plantillas de PR y changelog
│   └── scripts/                          # pre-PR y comprobación de versión
├── ux-critic/
│   ├── SKILL.md                          # principios, niveles de exigencia, 7 capas de juicio, refutación
│   ├── VERSION                           # versión SemVer de la skill
│   ├── references/                       # contexto, captura, capas de juicio, refutación, formato de informe
│   ├── scripts/                          # inventario objetivo del DOM y comprobación de versión
│   └── evals/evals.json
├── marcozen/
│   ├── SKILL.md                          # metodología, modos, cadencia, scoring, formatos de salida
│   ├── VERSION                           # versión SemVer de la skill
│   ├── references/                       # auditoría, poda, plantillas, SEO/GEO/AEO, seguridad
│   ├── scripts/                          # comprobación de versión
│   └── evals/evals.json
└── tech-cleanup/
    ├── SKILL.md                          # triage, auditoría A–E, modo multiagente, limpieza por etapas
    ├── VERSION                           # versión SemVer de la skill
    ├── references/                       # evidencia, modo multiagente, ejecución de limpieza
    └── scripts/                          # comprobación de versión
```

## Principios compartidos

- **Entender antes de actuar**: no elegir stack sin clasificar el proyecto; no modificar sin inspeccionar; no podar sin auditar.
- **No inventar**: hechos, decisiones y supuestos siempre separados y marcados.
- **Lo documentado no prueba que esté bien**: se audita el resultado, no la intención.
- **Código y documentación viajan juntos**, en la misma PR.
- **Nunca exponer secretos**: se reporta tipo + archivo, nunca el valor.
- **Cambios sensibles exigen mayor rigor** y autorización explícita para integrar.

## Licencia

[MIT](LICENSE) © Boris Fernandois
