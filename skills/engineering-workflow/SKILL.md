---
name: engineering-workflow
description: Ejecuta cambios de desarrollo de forma controlada y trazable en repositorios Git. Úsala obligatoriamente cuando el usuario la nombre, el repositorio la exija o la tarea implemente comportamiento, requiera Pull Request o merge, afecte varios archivos, datos, permisos, autenticación, pagos, documentos formales, dependencias, infraestructura o flujos operacionales. Permite una ruta rápida para cambios LOW. Déjala a criterio de la IA para documentación, copy o ajustes locales triviales y reversibles. No la uses por defecto para consultas conceptuales, explicaciones, comandos aislados ni investigación o diagnóstico sin modificaciones.
---

# Engineering Workflow

## Propósito

Convertir cada tarea de desarrollo en un cambio pequeño, revisable, probado, documentado y seguro, evitando que el repositorio se desordene o pierda trazabilidad a medida que trabajan agentes de IA.

Usa el Blueprint existente cuando esté disponible. No bloquees un cambio localizado solo porque el repositorio no tenga Blueprint. Detén la implementación y solicita completar o actualizar `project-blueprint` únicamente cuando falten decisiones necesarias de arquitectura, alcance, criterios de aceptación o reglas de datos que no puedan resolverse con patrones existentes y supuestos reversibles.

## Política de activación híbrida

Decide primero **si corresponde activar la skill** y después **qué profundidad aplicar**. No confundas activación obligatoria con flujo pesado: una tarea obligatoria puede ser `LOW` y usar la ruta rápida.

Aplica este orden:

1. **Obligatoria por autoridad:** el usuario nombra `engineering-workflow`, `AGENTS.md` u otra regla del repositorio la exige, o se solicita preparar/ejecutar un merge.
2. **Obligatoria por alcance o riesgo:** se implementan features, fixes de comportamiento, refactors, migraciones, cambios de seguridad o hotfixes; se requiere branch/commit/push/PR; se afectan varios archivos, contratos públicos, transiciones operacionales, datos o integraciones; o intervienen permisos, autenticación, RLS, pagos, archivos privados, emails, PDFs u otros documentos formales/regulados, dependencias, infraestructura o despliegue.
3. **A criterio de la IA:** documentación pequeña, correcciones de copy, estilos acotados y cambios locales de un archivo, triviales, reversibles y sin impacto en contratos, datos, seguridad u operación. Respeta siempre las reglas Git del repositorio; si exigen branch o PR, vuelve al punto 1.
4. **No activar por defecto:** preguntas conceptuales, comparativas, explicaciones de código, comandos aislados, lectura y reporte, diagnóstico sin modificaciones o revisión de estado. Si la investigación deriva en una solicitud de implementación, reclasifica antes de editar.

Ante duda razonable entre dos categorías, escala una categoría. Una mención explícita o una regla del repositorio siempre prevalece sobre las heurísticas de ahorro.

## Principios obligatorios

1. **Nunca trabajar directamente sobre `main`.** Todo cambio persistente debe realizarse en una branch específica.
2. **Inspeccionar antes de modificar.** Revisar Git, instrucciones del repositorio, documentación y archivos relacionados.
3. **Una branch, un propósito.** No mezclar cambios no relacionados.
4. **No destruir trabajo existente.** No descartar, sobrescribir ni reescribir cambios ajenos sin autorización explícita.
5. **Alcance controlado.** Implementar solo lo necesario para cumplir los criterios de aceptación.
6. **Dependencias justificadas.** No añadir paquetes de producción sin explicar necesidad, mantenimiento, seguridad y alternativa.
7. **Código y documentación viajan juntos.** La documentación afectada debe actualizarse dentro de la misma Pull Request.
8. **Validar antes de declarar terminado.** Ejecutar los comandos reales de lint, typecheck, tests y build que correspondan.
9. **Cambios sensibles requieren mayor rigor.** Datos, permisos, autenticación, pagos, archivos, emails, PDFs, migraciones e infraestructura exigen revisión específica.
10. **No integrar automáticamente.** Preparar la integración, pero realizar merge o squash merge solo con autorización explícita.

## Orden de autoridad

Antes de trabajar, identifica y respeta este orden:

1. Solicitud actual del usuario y criterios de aceptación confirmados.
2. `AGENTS.md` y reglas más cercanas al directorio afectado.
3. `CLAUDE.md`, si aplica.
4. Blueprint, requisitos, arquitectura, ADR y documentos funcionales.
5. Convenciones existentes del repositorio.
6. Supuestos explícitos y reversibles.

Si dos fuentes se contradicen, no elijas silenciosamente. Señala el conflicto y usa la opción de menor riesgo hasta validación.

## Flujo de trabajo

### Fase 0 — Triage de la tarea

Clasifica el cambio:

- `feature`
- `fix`
- `refactor`
- `docs`
- `test`
- `chore`
- `security`
- `migration`
- `hotfix`

Resume:

- problema a resolver;
- resultado esperado;
- alcance incluido;
- fuera de alcance;
- criterios de aceptación;
- riesgos previsibles;
- documentos fuente aplicables.

No implementes una solicitud ambigua si puede alterar datos, permisos, arquitectura o comportamiento de negocio. En cambios pequeños y reversibles, registra el supuesto y continúa.

Asigna el nivel de riesgo desde este momento usando `references/change-risk-matrix.md` (`LOW` / `MEDIUM` / `HIGH` / `CRITICAL`). No esperes a Fase 3 para clasificarlo: este nivel determina cuánto esfuerzo real reciben las Fases 4 a 9. Un cambio `LOW` (texto, copy, estilos acotados, corrección localizada sin datos) usa la **ruta rápida** descrita abajo; el resto de este documento describe la profundidad completa para `MEDIUM`/`HIGH`/`CRITICAL`, no un piso mínimo para todo.

#### Ruta rápida (riesgo LOW)

Si el cambio es LOW según la matriz, comprime el flujo:

1. Branch con nombre claro (Fase 2, sin ceremonia adicional).
2. Edita el archivo.
3. Corre solo lint/typecheck si tocan ese archivo, y una prueba focalizada si existe una relevante. No corras la batería completa de integración, E2E, seguridad, accesibilidad o rendimiento — no aplican a un cambio de copy o estilo.
4. Actualiza `CHANGELOG.md` solo si el cambio es visible para usuarios finales; si no, omítelo.
5. Revisa el diff (`git diff`) antes de PR — este paso no se salta nunca, es barato y evita alcance accidental.
6. PR corta: qué cambió y por qué, sin secciones vacías de riesgos/rollback que no aplican.

No repitas para un cambio LOW el mismo nivel de prueba y documentación que usarías para una migración o un cambio de permisos. Si tienes dudas sobre si algo es realmente LOW, sube un nivel — pero no apliques HIGH por defecto "para estar seguro".

### Fase 1 — Inspección del repositorio

En riesgo `LOW`, basta con el bloque de comandos Git y leer el archivo que vas a tocar. Omite el resto de esta fase.

Para `MEDIUM`/`HIGH`/`CRITICAL`, ejecuta o verifica, según disponibilidad:

```bash
git status --short --branch
git branch --show-current
git remote -v
git log --oneline -n 10
```

Después inspecciona:

- `AGENTS.md`, `CLAUDE.md`, `README.md`;
- manifiestos y lockfiles;
- scripts del proyecto;
- configuración de CI;
- documentación funcional y técnica;
- tests existentes;
- archivos directamente relacionados con la tarea.

#### Reglas de seguridad Git

- No ejecutar `git reset --hard` sin autorización explícita.
- No ejecutar `git clean -fd` sin autorización explícita.
- No hacer force-push por defecto.
- No reescribir historial compartido.
- No eliminar branches remotas sin autorización.
- No usar `git checkout -- <archivo>` para descartar cambios ajenos.
- Si hay cambios no confirmados, identifica su origen y evita mezclarlos.

### Fase 2 — Preparación de branch

La branch debe partir desde la base correcta y estar actualizada.

Convención recomendada:

```text
feature/<descripcion-corta>
fix/<descripcion-corta>
refactor/<descripcion-corta>
docs/<descripcion-corta>
test/<descripcion-corta>
chore/<descripcion-corta>
security/<descripcion-corta>
migration/<descripcion-corta>
hotfix/<descripcion-corta>
```

Ejemplos:

```text
feature/client-signature
fix/pdf-page-break
refactor/service-order-workflow
security/rotate-upload-policy
migration/add-equipment-history
```

Antes de crearla:

1. Confirma la branch base.
2. Actualiza referencias remotas.
3. Evita cambiar de branch si existen cambios no relacionados que puedan perderse.
4. Crea o reutiliza una branch solo si su propósito coincide exactamente.

No uses nombres genéricos como `changes`, `updates`, `test` o `new-feature`.

### Fase 3 — Plan de implementación

Antes de editar, define un plan breve con:

- archivos o dominios afectados;
- secuencia de cambios;
- validaciones requeridas;
- documentación que probablemente cambiará;
- estrategia de rollback si hay datos, migraciones o infraestructura.

Confirma o ajusta el riesgo asignado en Fase 0 usando `references/change-risk-matrix.md`. Si sigue siendo `LOW`, usa la ruta rápida de Fase 0 y omite el resto de esta fase.

A mayor riesgo, mayor profundidad de pruebas, revisión y documentación — la profundidad no es fija, escala con el nivel.

#### Tareas grandes con dominios independientes

Si el cambio es grande pero se descompone en subtareas independientes (p. ej. un módulo de administrador con pantallas, permisos y reportes separados), no lo proceses como un solo bloque secuencial. Divide el plan por dominio y evalúa delegar subtareas auto-contenidas a subagentes en paralelo (Agent tool), especialmente cuando no comparten estado ni archivos. Esto reduce tiempo total sin reducir rigor: cada subagente sigue aplicando el nivel de riesgo que le corresponde a su parte, no el nivel más alto del conjunto.

### Fase 4 — Implementación controlada

Reglas:

- Sigue patrones existentes antes de crear abstracciones nuevas.
- No reformatees archivos no relacionados.
- No mezcles limpieza general con una feature salvo que sea necesaria.
- Mantén cambios pequeños y coherentes.
- Evita duplicación, pero no abstraigas anticipadamente.
- No agregues dependencias si una capacidad existente resuelve el problema.
- No cambies contratos públicos sin identificar consumidores afectados.
- Mantén compatibilidad hacia atrás cuando sea razonable.
- Para TODOs, explica motivo, propietario o condición de cierre.

#### Cambios de datos

Si se modifica esquema, migraciones, seeds o retención:

- documenta la migración;
- define compatibilidad y rollback;
- valida datos existentes;
- evita operaciones destructivas por defecto;
- actualiza modelos, tipos, tests y documentación;
- no ejecutes migraciones de producción sin autorización.

#### Autenticación y permisos

Si se modifican roles o acceso:

- actualiza matriz de permisos;
- valida autorización en servidor, no solo en UI;
- prueba casos permitidos y denegados;
- revisa exposición de datos;
- registra el cambio en seguridad y changelog.

#### Emails y notificaciones

- No enviar correos reales durante desarrollo sin autorización.
- Usar ambientes, remitentes y destinatarios de prueba.
- No incluir datos sensibles innecesarios.
- Manejar errores, reintentos e idempotencia cuando corresponda.
- Documentar proveedor, eventos y variables de entorno.

#### PDFs y archivos

- Validar permisos, tamaño, tipo y almacenamiento.
- Evitar URLs públicas permanentes para contenido privado.
- Probar saltos de página, nombres, descarga y archivado.
- Documentar plantillas y campos formales.

### Fase 5 — Validaciones

Detecta los comandos reales en `package.json`, Makefile, scripts o CI. No inventes comandos que el repositorio no posee.

La lista siguiente es el techo para `HIGH`/`CRITICAL`, no el piso para todo cambio. Ejecuta solo lo que el nivel de riesgo (Fase 3) y el área tocada justifiquen:

- `LOW`: formato/lint/typecheck si tocan el archivo, y una prueba focalizada si existe. Nada más.
- `MEDIUM`: agrega tests unitarios relevantes y build.
- `HIGH`/`CRITICAL`: agrega integración, E2E de flujos críticos, migraciones, seguridad, accesibilidad y rendimiento — los que aplican al área afectada, no todos por defecto.

Catálogo completo de posibles validaciones (usar según lo anterior):

- formato;
- lint;
- typecheck;
- tests unitarios;
- tests de integración;
- tests E2E de flujos críticos;
- build de producción;
- validación de migraciones;
- chequeos de seguridad;
- accesibilidad;
- rendimiento cuando el cambio lo afecte.

Si una validación no puede ejecutarse:

1. Indica exactamente cuál.
2. Explica por qué.
3. Describe el riesgo residual.
4. No declares la tarea completamente validada.

Usa `scripts/pre_pr_check.py` como verificador documental complementario. No reemplaza los tests del proyecto.

### Fase 6 — Impacto documental

Usa `references/documentation-impact-matrix.md`, filtrada por el riesgo de Fase 3: en `LOW`, por defecto solo `CHANGELOG.md` si el cambio es visible para usuarios, y ni eso si es puramente interno. La lista de documentos frecuentes de abajo aplica a `MEDIUM`/`HIGH`/`CRITICAL` según el dominio tocado, no a cada tarea.

La documentación se actualiza antes del merge, dentro de la misma branch y Pull Request.

Documentos frecuentes:

- `CHANGELOG.md`
- `README.md`
- `docs/01-product-requirements.md`
- `docs/02-architecture.md`
- `docs/03-data-and-integrations.md`
- `docs/04-ux-content-and-design-system.md`
- `docs/05-security-and-operations.md`
- `docs/06-quality-and-testing.md`
- `docs/07-delivery-plan.md`
- `docs/permissions-matrix.md`
- `docs/api-contracts.md`
- `docs/pdf-specification.md`
- `docs/runbook.md`
- `docs/decisions/ADR-*.md`
- `.env.example`

#### Changelog

Registra cambios relevantes para producto, operación o desarrolladores bajo `Unreleased`.

No llenes el changelog con:

- reformateos sin impacto;
- cambios internos triviales;
- archivos temporales;
- detalles que solo pertenecen al historial Git.

#### ADR

Crea o actualiza un ADR cuando cambie:

- arquitectura;
- proveedor crítico;
- modelo de datos sustantivo;
- estrategia de autenticación;
- sistema de diseño base;
- generación de documentos;
- integración importante;
- estrategia de despliegue u observabilidad.

### Fase 7 — Revisión del diff

Antes de preparar la Pull Request:

```bash
git status --short
git diff --stat
git diff
```

Revisa:

- archivos inesperados;
- secretos o credenciales;
- logs de depuración;
- código muerto;
- cambios de lockfile no explicados;
- migraciones destructivas;
- texto provisional;
- accesos o permisos incompletos;
- documentación faltante;
- alcance accidental.

No confíes solo en tests automáticos. Lee el diff completo.

### Fase 8 — Commits

Preferencia por commits claros y coherentes. Si el repositorio usa squash merge, no es necesario fragmentar artificialmente, pero cada commit debe dejar un estado comprensible.

Convención sugerida:

```text
feat: add client validation flow
fix: prevent duplicate service notifications
refactor: separate report generation by service type
docs: document upload permission model
security: restrict private file access
```

No incluir secretos, datos personales ni identificadores internos sensibles en mensajes de commit.

### Fase 9 — Pull Request

Usa `assets/templates/pull_request_template.md`.

La Pull Request debe incluir:

- problema y objetivo;
- alcance;
- cambios realizados;
- decisiones relevantes;
- pruebas ejecutadas y resultados;
- documentación actualizada;
- riesgos y limitaciones;
- capturas o evidencia cuando aporten valor;
- pasos de migración y rollback si aplica.

No afirmes que algo fue probado si no se ejecutó.

### Fase 10 — Merge controlado

Método preferido: **squash merge**, salvo que el repositorio defina otra política.

Antes de integrar verifica:

- CI aprobada;
- conversaciones resueltas;
- documentación actualizada;
- changelog correcto;
- migraciones revisadas;
- ausencia de conflictos;
- autorización explícita para merge.

No hagas merge automáticamente solo porque las validaciones pasaron.

Después del squash merge:

1. Cambia a la branch base.
2. Actualiza desde remoto.
3. Verifica que el commit integrado esté presente.
4. Confirma estado limpio.
5. Elimina la branch local solo si ya fue integrada y no contiene trabajo adicional.
6. Elimina la branch remota solo cuando la política o autorización lo permita.
7. Verifica despliegue o migraciones si eran parte del alcance.

### Fase 11 — Cierre

Entrega un resumen con:

1. Qué se cambió.
2. Branch y estado de integración.
3. Validaciones ejecutadas.
4. Documentación actualizada.
5. Riesgos o pendientes.
6. Próximo paso único recomendado.

## Definition of Done

Usa `references/definition-of-done.md`.

Una tarea no está terminada solo porque “funciona en local”. Debe cumplir los puntos aplicables de alcance, código, datos, seguridad, UX, pruebas, documentación y operación.

Estados permitidos:

- `READY FOR REVIEW`
- `READY TO MERGE`
- `MERGED`
- `BLOCKED`
- `PARTIALLY VALIDATED`

## Control de versión de la skill

Lee `VERSION` para identificar la versión instalada. Si el usuario pide confirmar que es la última, o si vas a modificar esta skill, lee `references/versioning-policy.md` y ejecuta `python3 scripts/check_version.py --check-remote` antes de editar. Si no hay red o el origen no es verificable, informa que la versión remota quedó sin confirmar; no presentes la copia local como última versión.

## Formato de respuesta recomendado

```text
Estado: READY FOR REVIEW
Branch: feature/example

Implementado
- ...

Validaciones
- lint: passed
- typecheck: passed
- tests: passed
- build: passed

Documentación
- CHANGELOG.md
- docs/...

Riesgos o pendientes
- ...

Próximo paso
- Abrir/revisar Pull Request.
```

## Criterio de calidad

El workflow es correcto cuando otra persona puede revisar la Pull Request y comprender:

- por qué existe el cambio;
- qué hace y qué no hace;
- qué archivos y datos afecta;
- cómo fue probado;
- qué documentación cambió;
- cómo revertirlo si falla;
- qué riesgos permanecen;
- si está realmente listo para integrar.
