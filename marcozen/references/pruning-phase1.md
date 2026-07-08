# Poda Fase 1 — MarcoZen

Fase de **cambios seguros**. Se ejecuta **solo** después de una auditoría MarcoZen y con
aprobación explícita del usuario. Ordena la documentación y la gobernanza del proyecto
**sin tocar la lógica de negocio ni el comportamiento**.

## Antes de empezar

- Trabaja sobre una rama dedicada, no directo en `main`.
- Ten la auditoría a la vista: la poda se guía por sus hallazgos P0/P1/P2.
- Si al crear `.env.example` descubres que hay un `.env` real versionado, **no lo borres
  ni muevas en esta fase**: márcalo como riesgo P0 pendiente y avisa. La remediación de
  secretos es una tarea aparte y sensible.

## Prompt reutilizable

```
Aplica la fase 1 de poda MarcoZen según la auditoría anterior.

Objetivo:
Ordenar el proyecto sin cambiar funcionalidades.

Permitido:
- actualizar README.md
- crear o actualizar AGENTS.md
- crear .env.example
- crear docs/project-context.md
- crear docs/deployment-runbook.md
- crear docs/security-checklist.md
- actualizar CHANGELOG.md
- agregar enlaces entre documentos
- marcar archivos obsoletos como deprecated si corresponde

No permitido:
- borrar código funcional
- cambiar lógica de negocio
- tocar credenciales reales
- cambiar productos, servicios, precios o contenido crítico
- modificar diseño visual sin instrucción
- hacer refactor profundo

Entrega:
1. Archivos creados.
2. Archivos actualizados.
3. Riesgos que quedan.
4. Próxima fase recomendada.
```

## Notas de ejecución

- `.env.example` se crea a partir de las variables que el código realmente usa, con
  **placeholders** (`STRIPE_SECRET_KEY=`), nunca valores reales.
- Al "marcar como deprecated" un archivo, no lo borres: agrega una nota al inicio
  (`> ⚠️ DEPRECATED: reemplazado por docs/architecture.md`) y regístralo en el
  `CHANGELOG.md`. El borrado real es decisión de una fase posterior.
- Enlaza los documentos entre sí (README → docs/ → AGENTS) para que se naveguen solos.
- Al terminar, resume qué quedó pendiente y cuál sería la Fase 2 (ej: remediar secretos,
  borrar ramas muertas, consolidar duplicados, escribir tests).
