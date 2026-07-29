# Changelog

Los cambios relevantes de las skills se registran en este archivo.

## Unreleased

## tech-cleanup-v1.2.0 - 2026-07-29

### Changed

- `tech-cleanup`: la selección de motor del triage pasa a ser un **punto de control bloqueante** — si el perfil requerido es mayor que el del modelo actual, la auditoría no arranca sin autorización explícita.
- `tech-cleanup`: el punto de control se suma a las reglas inviolables de la fase de auditoría.

### Added

- `tech-cleanup`: segundo gatillo del punto de control — dos verificaciones fallidas con el modelo actual detienen el avance en vez de motivar un tercer intento.

## marcozen-v1.2.0 - 2026-07-29

### Changed

- `marcozen`: la selección de motor del triage pasa a ser un **punto de control bloqueante** — si el perfil requerido es mayor que el del modelo actual, la Fase 1 no arranca sin autorización explícita.
- `marcozen`: el punto de control se suma a las reglas inviolables de la primera pasada.

### Added

- `marcozen`: segundo gatillo del punto de control — dos revisiones fallidas con el modelo actual detienen el avance en vez de motivar un tercer intento.

## engineering-workflow-v1.2.0 - 2026-07-29

### Changed

- `engineering-workflow`: la selección de motor deja de ser una sugerencia y pasa a ser un **punto de control bloqueante**. Si el perfil requerido es mayor que el del modelo actual y el riesgo es `MEDIUM` o superior, hay que pedir autorización explícita antes de avanzar, con la misma regla que ya rige para merge y migraciones de producción.
- `engineering-workflow`: nuevo principio obligatorio 11 — no trabajar bajo el perfil de motor requerido.

### Added

- `engineering-workflow`: `references/engine-routing.md` define el formato del punto de control, sus tres salidas (cambiar de modelo, seguir con el desvío registrado, delegar el razonamiento a un subagente) y las condiciones en que **no** debe dispararse, para que no se vuelva ruido.
- `engineering-workflow`: segundo gatillo del punto de control — dos intentos fallidos de la misma subtarea detienen el avance en vez de motivar un tercer intento.

## tech-cleanup-v1.1.0 - 2026-07-28

### Added

- `tech-cleanup`: selección de motor en el triage de la Fase 0, con los perfiles aplicados al juicio de categoría A–E, la redacción del informe y la recolección de evidencia.
- `tech-cleanup`: asignación de modelo por rol en el modo multiagente — roles 1–5 en perfil MEDIO y revisor crítico final en ALTO, para concentrar el costo donde el error es caro.

## marcozen-v1.1.0 - 2026-07-28

### Added

- `marcozen`: selección de motor en el triage de la Fase 0, con los perfiles aplicados al veredicto de la auditoría, la redacción del informe y la Poda Fase 2.
- `marcozen`: línea `Motor sugerido` en la salida del triage rápido.

## engineering-workflow-v1.1.0 - 2026-07-28

### Added

- `engineering-workflow`: `references/engine-routing.md`, política única de selección de motor por perfiles (ALTO/MEDIO/BAJO), con ejes de decisión, regla de los dos intentos y tabla fechada de modelos vigentes. Es la fuente compartida que referencian `marcozen` y `tech-cleanup`.
- `engineering-workflow`: bloque "Selección de motor" en la Fase 0, emitido junto al nivel de riesgo y sin bloquear el trabajo.

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
