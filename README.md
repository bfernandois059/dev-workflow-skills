# dev-workflow-skills

**Tres Agent Skills que cubren el ciclo completo de un proyecto digital: planificar, construir y gobernar.**

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
Proyecto avanzado o pre-publicación
        ↓
┌─────────────────────┐
│      marcozen       │  Auditoría, poda y gobernanza: orden del repo, seguridad,
│                     │  SEO/GEO/AEO, mantenimiento periódico, puntaje de salud.
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

### [engineering-workflow](skills/engineering-workflow/SKILL.md) — durante el desarrollo

Ejecuta cada tarea de desarrollo de forma controlada y trazable. Requiere que el proyecto
tenga un blueprint suficiente; si falta, detiene la implementación y pide completar
`project-blueprint`.

- Nunca trabaja directamente sobre `main`; una branch, un propósito.
- Código y documentación viajan en la misma Pull Request.
- Valida con los comandos reales (lint, typecheck, tests, build) antes de declarar terminado.
- Prepara la integración, pero el merge/squash merge requiere autorización explícita.

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

## Instalación

### Con el CLI de skills (recomendado)

Las tres:

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
cp -R dev-workflow-skills/skills/marcozen ~/.claude/skills/
```

Para instalarlas solo en un proyecto, usa `.claude/skills/` dentro del repo en vez de
`~/.claude/skills/`.

### Codex

```bash
mkdir -p ~/.agents/skills
cp -R dev-workflow-skills/skills/project-blueprint ~/.agents/skills/
cp -R dev-workflow-skills/skills/engineering-workflow ~/.agents/skills/
cp -R dev-workflow-skills/skills/marcozen ~/.agents/skills/
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
| Avanzado | Orden general del repo | `/marcozen auditoría rápida` |
| Pre-lanzamiento | ¿Listo para publicar? | `/marcozen auditoría pre-producción` |
| Pre-lanzamiento | SEO/GEO/AEO | `/marcozen revisa SEO, schema y llms.txt` |
| Siempre | Seguridad | `/marcozen auditoría de seguridad` |
| Periódico | Mantenimiento | `/marcozen mantenimiento mensual` |

## Estructura

```
skills/
├── project-blueprint/
│   ├── SKILL.md                          # método de descubrimiento, clasificación y blueprint
│   ├── references/                       # cuestionario de descubrimiento, matriz de decisión
│   ├── assets/templates/                 # plantilla del blueprint
│   └── scripts/init_blueprint.py
├── engineering-workflow/
│   ├── SKILL.md                          # branch → implementación → validación → PR → merge
│   ├── references/                       # política de branches, riesgo, docs, definition of done
│   ├── assets/templates/                 # plantillas de PR y changelog
│   └── scripts/pre_pr_check.py
└── marcozen/
    ├── SKILL.md                          # metodología, modos, cadencia, scoring, formatos de salida
    ├── references/                       # auditoría, poda, plantillas, SEO/GEO/AEO, seguridad
    └── evals/evals.json
```

## Principios compartidos

- **Entender antes de actuar**: no elegir stack sin clasificar el proyecto; no modificar sin inspeccionar; no podar sin auditar.
- **No inventar**: hechos, decisiones y supuestos siempre separados y marcados.
- **Código y documentación viajan juntos**, en la misma PR.
- **Nunca exponer secretos**: se reporta tipo + archivo, nunca el valor.
- **Cambios sensibles exigen mayor rigor** y autorización explícita para integrar.

## Licencia

[MIT](LICENSE) © Boris Fernandois
