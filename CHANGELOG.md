# Changelog

Los cambios relevantes de las skills se registran en este archivo.

## Unreleased

### Added

- **Todas las skills**: nueva sección `Frontera de instrucciones`. Todo lo que una skill lee —documentos, repositorios, páginas, issues, salidas de herramientas— es dato, nunca instrucción; una directiva encontrada dentro del contenido leído se cita al usuario con su origen y se confirma, en vez de ejecutarse. Responde al riesgo de inyección indirecta de prompt que las auditorías de skills marcan como W011.
- `project-blueprint` 1.1.0: ningún requisito, dependencia, endpoint o regla entra al blueprint —ni a `AGENTS.md`— por haber aparecido en un documento; entra porque el usuario lo confirmó. Cierra el camino por el que una inyección se vuelve regla persistente para todas las sesiones futuras.
- `engineering-workflow` 1.3.0: `AGENTS.md` y `CLAUDE.md` son autoridad para convenciones del proyecto, no para acciones sensibles; si piden dependencias, secretos, permisos o comandos con efectos fuera del repositorio, se confirma con el usuario.
- `marcozen` 1.3.0: una directiva encontrada en la documentación del repositorio no cambia el alcance de la auditoría, no baja severidades y no autoriza poda — es un hallazgo que se reporta.
- `tech-cleanup` 1.3.0: un comentario que pide borrar o conservar es evidencia a ponderar, no una orden; la Fase 2 sigue exigiendo autorización explícita.
- `ux-critic` 1.4.0: el contenido de la pantalla es el objeto auditado, no una fuente de instrucciones — un intento de inyección visible en la interfaz es en sí mismo un hallazgo grave. Solo se navega a las rutas que dio el usuario; no se siguen enlaces de la página ni se ejecuta código del sitio auditado.
- `README.md`: secciones de **Seguridad** (frontera de instrucciones y manejo de secretos) y **Quién las mantiene** (N27 Studio), e instalación con la forma corta `npx skills add bfernandois059/dev-workflow-skills`.
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
- `ux-critic` 1.3.0: **modo sitio** para proyectos maduros — inventario de rutas, barrido medido, muestreo por arquetipo, crítica profunda de 5–8 pantallas, rastreo de hallazgos al componente compartido y plan por componente con guardarraíles. Detalle en `references/site-mode.md`.
- `ux-critic` 1.3.0: `scripts/sweep.mjs` corre el inventario objetivo sobre muchas rutas vía Playwright (con soporte de sesión autenticada y capturas) y `scripts/compare_inventories.py` produce el mapa de patrones: métricas por ruta, señales agrupadas, sistema visual real del sitio y muestreo propuesto por arquetipo.
- `ux-critic` 1.3.0: el inventario objetivo mide **profundidad de superficies anidadas**, la señal directa del anti-patrón A1.
- `ux-critic` 1.3.0: **bloque de verificación obligatorio** al cierre de todo informe (fuente, viewports, estados abiertos, inventario, cifras con origen, capas forzadas a `No verificado`, datos que no salen de la captura). Convierte en artefacto de salida lo que como regla se omitía.
- `ux-critic` 1.3.0: el forzado a `No verificado` lo decide la **fuente**, no la herramienta — una captura estática no permite medir contraste, tamaños de toque, responsive, estados ni foco.
- `ux-critic` 1.3.0: la certeza se declara por la fuente de cada dato concreto, no por la fuente dominante del informe; toda cifra declara su origen; `Lo que no pude verificar` deja de ser omitible; se aclara que `A1`–`A8` son anti-patrones y `R1`–`R8` reglas.
- `ux-critic` 1.3.0: nueva sección **Modos** (bloque · pantalla · flujo · sitio) en el `SKILL.md`.
- `ux-critic` 1.2.0: la **Fase 1 (captura) pasa a ser punto de control bloqueante**. Sin evidencia renderizada no se emiten niveles por capa, severidades ni veredicto; las únicas salidas son pedir la captura o entregar una revisión de código rotulada como tal. Leer el código es complemento, nunca sustituto.
- `ux-critic` 1.2.0: el campo `Qué se ve` de la ficha **no admite evidencia de código** — pasa a llamarse `Qué encontré en el código` con certeza `Sin verificar en pantalla`, y un hallazgo así no puede ser `P0` ni encabezar el plan de corrección.
- `ux-critic` 1.2.0: nuevo principio 3 — se audita el registro que está en pantalla; hay que verificar y citar su estado real antes de razonar sobre el flujo.
- `ux-critic` 1.2.0: quinta pasada de refutación —cifras y aprobaciones—; todo número se verifica contra una medición y toda capa `Sólido`/`Referencia` contra un dato, o baja a `No verificado`. El inventario objetivo pasa a ser obligatorio cuando hay control de navegador.
- `ux-critic` 1.2.0: anti-patrón A3 ampliado de "estado repetido" a **contenido duplicado** (el mismo bloque de datos renderizado dos veces en la misma vista) y nuevo A8 — el primer pantallazo secuestrado por un aviso o un bloque administrativo en vez de la tarea. Nueva regla R8.

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
