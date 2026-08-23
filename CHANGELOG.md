# Changelog

Los cambios relevantes de las skills se registran en este archivo.

## Unreleased

### Added

- Nueva skill `ux-critic` (1.0.0): crítica de UX/UI sobre la interfaz **renderizada** —sitio en local, URL, flujo, pantalla o bloque—, no sobre el código ni la documentación.
- `ux-critic`: contexto bloqueante en Fase 0 (producto, usuario real, tarea, criterio de éxito, etapa, restricciones, alcance) y tres niveles de exigencia que cambian qué cuenta como hallazgo.
- `ux-critic`: juicio en siete capas con orden fijo y regla de corte —propósito, jerarquía, ritmo, copy, interacción y estados, sistema visual, oficio— más accesibilidad y responsive como transversales.
- `ux-critic`: `scripts/ui_inventory.js`, inventario objetivo ejecutable sobre la página viva (escala tipográfica en uso, paleta real, espaciados, contrastes medidos, tamaños de toque, esquema de encabezados, ancho de línea y ritmo vertical).
- `ux-critic`: pasada de refutación obligatoria antes de entregar el informe, con la distinción explícita entre `OK` verificado y `Sin verificar`.
- `ux-critic`: referencias de contexto, protocolo de captura, capas de juicio, refutación, formato de informe y política de versionado; `evals/evals.json` con tres casos.
- `ux-critic` 1.1.0: `references/container-antipatterns.md`, catálogo prescriptivo de anti-patrones de estructura y superficie —cajas anidadas sin función, títulos en eco, estado repetido, todo-es-una-tarjeta, acciones sin jerarquía, inputs que parecen deshabilitados y bloques vacíos que solo se explican— con siete reglas y el árbol de contenedores antes/después de cada corrección.
- `ux-critic` 1.1.0: nuevas pruebas en las capas 2, 4, 5 y 6 para detectar esos anti-patrones (profundidad de superficies, títulos en eco, estado repetido, peso de acciones por frecuencia × deseabilidad, superficies con función, affordance de campos, vacío que ofrece).
- `ux-critic` 1.1.0: el informe termina en un **plan de corrección** reutilizable como tareas, agrupado en olas y con criterio de aceptación verificable, con plantilla en `assets/templates/fix-plan.template.md`.
- `ux-critic` 1.1.0: los hallazgos de estructura exigen el árbol antes/después; entregar el informe sin plan de corrección pasa a ser anti-patrón declarado de la skill.
- `README.md`: `ux-critic` incorporada al flujo, a la tabla de versionado, a la instalación, a la tabla de uso y a la estructura del repositorio.

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
