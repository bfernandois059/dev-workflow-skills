# Changelog

Los cambios relevantes de las skills se registran en este archivo.

## Unreleased

### Added

- `engineering-workflow`: `references/engine-routing.md`, política única de selección de motor por perfiles (ALTO/MEDIO/BAJO), con ejes de decisión, regla de los dos intentos y tabla fechada de modelos vigentes.
- `engineering-workflow`: bloque "Selección de motor" en la Fase 0, emitido junto al nivel de riesgo y sin bloquear el trabajo.
- `marcozen`: selección de motor en el triage de la Fase 0 y línea `Motor sugerido` en su salida.
- `tech-cleanup`: selección de motor en el triage de la Fase 0 y asignación de modelo por rol en el modo multiagente (roles 1–5 en MEDIO, revisor crítico en ALTO).

### Changed

- `engineering-workflow`: la delegación a subagentes de la Fase 3 ahora asigna modelo por subtarea en vez de correr todo en el perfil más alto del conjunto.

## tech-cleanup-v1.0.0 - 2026-07-25

### Added

- `tech-cleanup`: nueva skill para detección de código, archivos, dependencias y assets sin uso, con clasificación A–E por riesgo, dificultad, triage inicial y limpieza por etapas.
- `tech-cleanup`: modo multiagente opcional (arquitectura/rutas, componentes/estilos, assets, dependencias/config, tests/docs, y un revisor crítico final) para auditorías profundas en repos grandes.
- `tech-cleanup`: control de versión SemVer, política de publicación y comprobación opcional contra el repositorio canónico.

## project-blueprint-v1.0.0 - 2026-07-17

### Added

- `project-blueprint`: control de versión SemVer, política de publicación y comprobación opcional contra el repositorio canónico.

## marcozen-v1.0.0 - 2026-07-17

### Added

- `marcozen`: control de versión SemVer, política de publicación y comprobación opcional contra el repositorio canónico.

### Changed

- `marcozen`: descripción de activación condensada al límite del estándar Agent Skills sin perder sus modos ni disparadores principales.

## engineering-workflow-v1.0.0 - 2026-07-17

### Added

- `engineering-workflow`: control de versión SemVer por skill, política de publicación y comprobación opcional contra el repositorio canónico.

### Changed

- `engineering-workflow`: política híbrida que separa los disparadores obligatorios, los casos a criterio de la IA y las tareas donde no corresponde activarla.
- `engineering-workflow`: ausencia de Blueprint deja de bloquear cambios localizados cuando existen patrones y supuestos reversibles suficientes.
