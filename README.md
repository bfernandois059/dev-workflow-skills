# MarcoZen de Proyectos

**Sistema de auditoría, poda y gobernanza para repositorios web, e-commerce y apps.**

MarcoZen es una [Agent Skill](https://code.claude.com/docs/en/skills) reutilizable que permite
a un desarrollador o a un agente IA **auditar, ordenar y podar** un repositorio para que
cualquier profesional pueda tomarlo sin preguntar diez veces dónde está cada cosa.

> Concepto central: un proyecto sano no es el que tiene más ramas, más documentos o más
> features. Es el que **otro profesional puede tomar sin preguntar diez veces dónde está cada
> cosa**.

## Qué hace

Cinco modos de uso sobre la misma metodología:

1. **Auditoría rápida** — orden general del repo, documentación, ramas y riesgos (puntaje 0–100).
2. **Auditoría pre-producción** — ¿el sitio/app está listo para publicarse?
3. **Auditoría SEO/GEO/AEO** — indexación, metadata, schema, `llms.txt`, preparación para
   buscadores e IA.
4. **Auditoría de seguridad** — secretos, headers, formularios, webhooks, pagos, dependencias.
5. **Mantenimiento periódico** — ramas, PRs, `npm audit`/`outdated`, build, lint, con cadencia
   mensual / trimestral / anual.

Entrega informes con puntaje, hallazgos clasificados por severidad (P0–P3), documentos
faltantes, plan de poda y veredicto — y los guarda como archivo Markdown fechado para comparar
la evolución en el tiempo.

## Instalación

### Con el CLI de skills (recomendado)

```bash
npx skills add https://github.com/bfernandois059/marcozen-skill --skill marcozen
```

### Claude Code (manual)

Copia la carpeta `marcozen/` a tu directorio de skills:

```bash
# a nivel usuario (disponible en todos tus proyectos)
git clone https://github.com/bfernandois059/marcozen-skill
cp -R marcozen-skill/marcozen ~/.claude/skills/marcozen
```

Luego invócala con `/marcozen` o con frases como *"audita este repo"* / *"¿está listo para
producción?"*.

### Otros agentes (Codex, Antigravity, etc.)

El formato Agent Skills es markdown portable. Si tu agente no auto-carga skills, apúntalo al
archivo [`marcozen/SKILL.md`](marcozen/SKILL.md) como instrucciones de método, o usa el
**prompt maestro reutilizable** incluido en
[`marcozen/references/audit-prompt.md`](marcozen/references/audit-prompt.md).

## Uso

| Quiero… | Cómo iniciarlo |
|---------|----------------|
| Orden general del repo | `/marcozen auditoría rápida` |
| ¿Listo para publicar? | `/marcozen auditoría pre-producción` |
| SEO/GEO/AEO | `/marcozen revisa SEO, schema y llms.txt` |
| Seguridad | `/marcozen auditoría de seguridad` |
| Mantenimiento | `/marcozen mantenimiento mensual` |

## Estructura

```
marcozen/
├── SKILL.md                              # metodología, modos, cadencia, scoring, formatos de salida
├── references/
│   ├── audit-prompt.md                   # guía operativa + prompt maestro reutilizable
│   ├── pruning-phase1.md                 # poda de documentación (fase de cambios seguros)
│   ├── doc-templates.md                  # plantillas (README, AGENTS, .env.example, docs…)
│   ├── preprod-seo-geo-aeo.md            # checklist SEO / GEO / AEO pre-producción
│   ├── preprod-security.md               # checklist de seguridad pre-producción
│   └── maintenance-and-branches.md       # cadencias, poda de ramas y gotchas
└── evals/evals.json                      # casos de prueba
```

## Principios

- **Solo lectura en la auditoría**: un diagnóstico no cambia el paciente.
- **Nunca expone secretos**: reporta tipo + archivo, nunca el valor; descarta falsos positivos.
- **No promete indexación inmediata**: evalúa *preparación* técnica, semántica y de confianza.
- **Claridad, mantenibilidad y seguridad por sobre cantidad** de documentos.

## Licencia

[MIT](LICENSE) © Boris Fernandois
