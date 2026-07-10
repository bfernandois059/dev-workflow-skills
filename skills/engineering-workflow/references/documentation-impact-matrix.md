# Documentation Impact Matrix

| Cambio | Documentación mínima |
|---|---|
| Feature visible | `CHANGELOG.md`, requisitos/criterios de aceptación, README si cambia uso |
| Fix relevante | `CHANGELOG.md`; test de regresión |
| Arquitectura | `docs/02-architecture.md` + ADR |
| Esquema o migración | `docs/03-data-and-integrations.md`, migración, rollback, ADR si es sustantivo |
| Roles o permisos | `docs/permissions-matrix.md`, seguridad, tests de acceso |
| API o webhook | `docs/api-contracts.md`, variables, errores e idempotencia |
| Email | proveedor, eventos, remitentes, variables, manejo de fallos |
| PDF | `docs/pdf-specification.md`, campos, plantilla, versionado |
| Archivos | almacenamiento, acceso, retención, límites y borrado |
| CMS | `docs/content-model.md`, roles editoriales y preview |
| Analytics | plan de medición, nombre y propiedades de eventos |
| Infraestructura | arquitectura, runbook, variables, despliegue y rollback |
| Seguridad | `docs/05-security-and-operations.md`, changelog y posible ADR |
| UI pattern nuevo | diseño/componentes, accesibilidad y estados |

## Regla

La documentación afectada se actualiza dentro de la misma branch. No dejar “documentar después” como práctica habitual.
