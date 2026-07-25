# Limpieza por etapas — detalle operativo

Fase 2. Se ejecuta **solo** después de una auditoría Tech Cleanup y con aprobación explícita
del usuario sobre qué etapa abordar. Sigue la disciplina de `engineering-workflow`: branch
dedicada por etapa, nunca directo en `main`, validaciones reales antes de declarar terminado.

## Antes de empezar

- Ten la auditoría a la vista (`docs/tech-cleanup/audit-AAAA-MM-DD.md`): cada eliminación se
  justifica con la fila correspondiente de la tabla maestra, no de memoria.
- Una branch por etapa (ej. `chore/cleanup-etapa-1-assets-sin-uso`), no una branch gigante
  para todas las etapas.
- Si durante la limpieza aparece un secreto o credencial versionada, **no la borres ni la
  muevas en esta fase**: repórtala como riesgo aparte. Remediar secretos es una tarea
  distinta y más sensible que la limpieza de código sin uso.

## Etapa 1 — Limpieza segura (Categoría A, dificultad baja)

- Elimina únicamente lo que la auditoría clasificó como A con dificultad baja.
- Corre las validaciones del proyecto (lint, typecheck, tests, build) después de cada
  bloque de eliminaciones, no solo al final.
- Si una validación falla, esa eliminación no era tan segura como parecía: revierte ese
  cambio puntual, no toda la etapa, y anota por qué en el PR.

## Etapa 2 — Limpieza validada (Categoría B)

- Antes de eliminar, corre exactamente la validación que la auditoría indicó para ese
  elemento (build, test específico, revisión visual en preview, confirmación de uso
  dinámico).
- Si la validación no es concluyente, reclasifica el elemento a Categoría C en vez de
  forzar la eliminación.
- Revisión visual: para componentes o assets con superficie de UI, levanta un preview y
  confirma manualmente antes de mergear — no solo confiar en que el build pasó.

## Etapa 3 — Refactor y consolidación (Categoría C)

- Sigue el orden que la auditoría indicó: primero migrar lo que depende del elemento
  duplicado/antiguo, después eliminar.
- Cada migración es su propio commit (o su propio PR si el volumen lo amerita) para poder
  revertir un paso sin deshacer todo el refactor.
- No mezcles la consolidación con eliminaciones de otras etapas en el mismo PR.

## Etapa 4 — Archivo y documentación (Categoría E)

- No se borra: se mueve a una ubicación de histórico (ej. `docs/_archive/`) o se marca
  explícitamente como archivado, preservando el valor de trazabilidad.
- Actualiza referencias cruzadas si algún documento vigente apuntaba al material archivado.
- Si el usuario pide explícitamente eliminar en vez de archivar, confírmalo antes de hacerlo
  — no es el comportamiento por defecto de esta etapa.

## Etapa 5 — Revisión posterior

- Repite el análisis de referencias, tests y build sobre el estado final, no solo etapa por
  etapa: confirma que la suma de las eliminaciones no dejó nada roto que cada validación
  individual no detectó por separado.
- Compara el resultado de build/bundle contra el estado previo a la limpieza si la
  herramienta lo permite — es la confirmación más concreta de que la limpieza tuvo efecto.

## Checklist de rollback

Antes de mergear cualquier etapa, confirma que puedes responder que sí a todo esto:

- [ ] Cada PR de esta etapa es revertible de forma independiente (no depende de otro PR de
      la misma etapa que aún no se mergeó).
- [ ] Las validaciones reales del proyecto (lint, typecheck, tests, build) pasaron sobre el
      estado final de la etapa, no solo sobre commits intermedios.
- [ ] Si algo de esta etapa toca producción visualmente (componentes, assets, rutas), hubo
      revisión visual en preview antes del merge.
- [ ] Existe un registro (PR, changelog) de qué se eliminó/archivó y por qué, para poder
      diagnosticar rápido si algo se rompe después del merge.
- [ ] No quedaron secretos, credenciales o `.env` reales tocados durante la limpieza.

Al cerrar cada etapa, resume: qué se eliminó/archivó, resultado de las validaciones, y qué
queda pendiente para la etapa siguiente.
