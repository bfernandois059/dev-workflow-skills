---
name: project-blueprint
description: Diseña el blueprint técnico, funcional y documental de un proyecto digital antes de implementar. Úsala al iniciar o reestructurar sitios web, landing pages, intranets, portales, SaaS, plataformas internas, dashboards, ecommerce, APIs o automatizaciones. Debe entrevistar, clasificar el proyecto, recomendar el stack mínimo suficiente, definir arquitectura, datos, seguridad, documentos, reglas para IA y plan de implementación. No debe comenzar a construir el producto ni inventar requisitos no confirmados.
---

# Project Blueprint

## Propósito

Convertir una idea, solicitud comercial o repositorio inmaduro en una base de proyecto clara, validable y lista para implementación, evitando comenzar a programar con supuestos dispersos.

La salida principal es un **Blueprint de Proyecto** acompañado por documentos iniciales y reglas persistentes para agentes. Esta skill trabaja antes del diseño visual final y antes de la implementación sustantiva.

## Principios obligatorios

1. **Entender antes de elegir tecnología.** No recomendar un stack hasta clasificar usuarios, flujos, datos, contenido, integraciones, seguridad, operación y restricciones.
2. **Complejidad mínima suficiente.** No agregar CMS, base de datos, autenticación, colas, microservicios, animaciones, IA, almacenamiento o infraestructura si no existe una necesidad concreta.
3. **Separar hechos, decisiones y supuestos.** Todo elemento debe quedar marcado como `Confirmado`, `Recomendado`, `Supuesto` o `Pendiente de validar`.
4. **No inventar.** No crear roles, normas, integraciones, capacidades, métricas, datos de negocio ni reglas legales no entregadas.
5. **Decisiones explicables.** Cada tecnología recomendada debe responder a una necesidad identificada e incluir por qué se elige y qué alternativa fue descartada.
6. **Documentación viva.** Los documentos deben tener propietario, estado y criterio de actualización.
7. **Diseñar para operación real.** Considerar quién administra, publica, revisa, mantiene, respalda y atiende incidentes después del lanzamiento.
8. **No implementar todavía.** Durante esta skill solo se permite inspeccionar, preguntar, documentar, crear estructura vacía y preparar contratos/interfaces de alto nivel. No desarrollar funcionalidades completas.

## Flujo de trabajo

### Fase 0 — Inspección inicial

Determina si el trabajo ocurre en:

- un proyecto nuevo sin repositorio;
- un repositorio recién creado;
- un proyecto existente que necesita ordenarse;
- una migración o reemplazo.

Si existe repositorio, inspecciona primero estructura, manifiestos, dependencias, configuración, documentación, esquema de datos, rutas, tests y estado de Git. Resume lo encontrado sin asumir que representa decisiones correctas.

Busca material de negocio o marca disponible: brief, Brand Master, documentación funcional, diseños, contratos, PDFs, hojas de cálculo o repositorios anteriores. Nunca reemplaces la validación del usuario con inferencias silenciosas.

### Fase 1 — Descubrimiento guiado

Usa `references/discovery-questionnaire.md`.

Reglas de entrevista:

- Pregunta por bloques cortos, no como formulario interminable.
- No repitas información ya entregada o encontrada.
- Prioriza preguntas que cambien arquitectura o alcance.
- Cuando el usuario no sepa una respuesta, propone una opción preliminar claramente marcada.
- Para proyectos pequeños puede bastar una ronda reducida.
- Para sistemas con usuarios, datos sensibles, pagos, archivos, workflows o integraciones, completa todas las áreas críticas.

No avances a una recomendación definitiva mientras falten decisiones bloqueantes. Cuando no sea posible preguntar, trabaja con supuestos explícitos y conservadores.

### Fase 2 — Clasificación del proyecto

Clasifica una o más categorías:

1. Landing page o micrositio.
2. Sitio corporativo o institucional.
3. Sitio de contenidos / blog / biblioteca técnica.
4. Ecommerce o reservas con pago.
5. Portal de clientes o proveedores.
6. Intranet o plataforma interna.
7. Aplicación operativa / workflow / tickets / órdenes.
8. Dashboard o sistema de reportes.
9. SaaS multiempresa.
10. API, integración o automatización.
11. Migración o modernización.
12. Prototipo validable.

Asigna nivel de complejidad:

- **L0 — Estático:** contenido controlado por desarrollo, sin datos persistentes.
- **L1 — Contenido administrable:** CMS, formularios, analítica, SEO.
- **L2 — Aplicación simple:** base de datos, autenticación o workflow acotado.
- **L3 — Aplicación crítica:** permisos, auditoría, archivos, integraciones, reportes, operación continua.
- **L4 — Plataforma escalable:** multiempresa, alta disponibilidad, regulación, alto volumen o integración profunda.

Explica qué evidencia sustenta la clasificación.

### Fase 3 — Matriz de decisiones

Usa `references/architecture-decision-matrix.md`.

Evalúa, al menos:

- framework y estrategia de renderizado;
- hosting y ambientes;
- base de datos;
- autenticación y autorización;
- CMS y administración de contenido;
- almacenamiento de archivos;
- emails y notificaciones;
- generación de PDF;
- búsqueda;
- analítica y observabilidad;
- integraciones y automatizaciones;
- testing;
- seguridad, respaldos y recuperación;
- accesibilidad, SEO, GEO/AEO cuando corresponda;
- motion o animación;
- sistema de diseño y estrategia de componentes.

#### Reglas específicas de decisión

- **Next.js no es una respuesta automática.** Puede ser recomendado por SEO, rendering híbrido, rutas, React y ecosistema, pero compara con soluciones estáticas, CMS tradicional, framework más simple o backend independiente cuando corresponda.
- **Supabase** se recomienda cuando PostgreSQL administrado, autenticación, storage, realtime o funciones simplifican el producto. No usarlo solo por costumbre.
- **CMS** se recomienda cuando personas no técnicas deben publicar o mantener contenido frecuente. Define modelo editorial, roles y preview; no basta decir “usar CMS”.
- **PDF** se recomienda solo si existe un artefacto formal para imprimir, firmar, archivar, enviar o integrar. Define si es plantilla HTML, generación server-side, servicio externo o documento manual.
- **Motion** debe ser funcional: jerarquía, feedback o comprensión. Evitarla si afecta rendimiento, accesibilidad o credibilidad.
- **Atomic Design** es una referencia útil, no una obligación. Para proyectos pequeños, usar componentes por dominio o feature puede ser más claro. Elige una estrategia y documenta límites.
- **Microservicios** quedan descartados por defecto salvo evidencia de equipos, escalado, dominios o despliegues independientes.
- **IA generativa** no se incluye salvo caso de uso, datos, evaluación, costos, privacidad y fallback definidos.

### Fase 4 — Blueprint y artefactos

Genera primero `docs/00-project-blueprint.md` usando `assets/templates/00-project-blueprint.template.md`.

Después crea solo los documentos aplicables de esta lista:

#### Núcleo obligatorio

- `README.md`: propósito, estado, instalación y rutas de documentación.
- `docs/00-project-blueprint.md`: fuente principal de decisiones.
- `docs/01-product-requirements.md`: problema, objetivos, usuarios, alcance, requisitos y criterios de aceptación.
- `docs/02-architecture.md`: arquitectura, límites, diagramas Mermaid y decisiones.
- `docs/03-data-and-integrations.md`: entidades, datos, archivos, integraciones y retención.
- `docs/04-ux-content-and-design-system.md`: arquitectura de información, flujos, contenido y componentes.
- `docs/05-security-and-operations.md`: amenazas, permisos, secretos, respaldos, monitoreo e incidentes.
- `docs/06-quality-and-testing.md`: estrategia de pruebas, accesibilidad, rendimiento y definición de terminado.
- `docs/07-delivery-plan.md`: fases, dependencias, riesgos y backlog inicial.
- `docs/decisions/ADR-0001-initial-architecture.md`: primera decisión formal.
- `AGENTS.md`: reglas persistentes para Codex.
- `CLAUDE.md`: reglas persistentes para Claude Code.
- `.env.example`: nombres de variables sin secretos.

#### Condicionales

- `docs/content-model.md` para CMS o contenido estructurado.
- `docs/permissions-matrix.md` para más de un rol.
- `docs/api-contracts.md` para APIs o integraciones.
- `docs/pdf-specification.md` para PDFs formales.
- `docs/analytics-measurement-plan.md` para productos con conversión o KPIs.
- `docs/migration-plan.md` para proyectos existentes.
- `docs/compliance-and-privacy.md` para datos personales, pagos, salud, educación u otros contextos sensibles.
- `docs/runbook.md` para aplicaciones operativas.

No crees documentos vacíos para inflar la estructura. Si un tema no aplica, indícalo en el Blueprint.

### Fase 5 — Reglas persistentes para IA

Genera `AGENTS.md` y `CLAUDE.md` desde una misma fuente conceptual, adaptando sintaxis solo cuando sea necesario.

Deben ser breves y contener:

- propósito del producto y usuarios;
- documentos fuente y orden de autoridad;
- stack confirmado;
- comandos reales del repositorio;
- convenciones de arquitectura;
- reglas de datos y seguridad;
- reglas de diseño y contenido;
- validaciones obligatorias antes de cerrar una tarea;
- prohibiciones contra invenciones y cambios de alcance;
- protocolo para actualizar documentación cuando cambia una decisión.

No copies todo el Blueprint dentro de estos archivos. Enlaza a documentos específicos.

Usa estas frases normativas:

- “No inventes datos, requisitos, credenciales, endpoints, roles ni reglas de negocio.”
- “Cuando falte información, registra el supuesto y solicita validación o elige la opción reversible de menor riesgo.”
- “No agregues dependencias de producción sin justificar necesidad, mantenimiento, seguridad y alternativa.”
- “No cambies arquitectura, esquema de datos o alcance sin actualizar el ADR y los documentos afectados.”
- “Antes de implementar, identifica criterios de aceptación y archivos fuente aplicables.”
- “Después de implementar, ejecuta las validaciones definidas y documenta cualquier limitación.”

### Fase 6 — Puerta de aprobación

Termina con un **Architecture Readiness Check**:

- Problema y resultado esperado definidos.
- Usuarios, roles y flujos principales definidos.
- Alcance inicial y fuera de alcance explícitos.
- Stack mínimo justificado.
- Modelo de datos preliminar definido.
- Integraciones y responsables identificados.
- Seguridad y privacidad evaluadas.
- Estrategia de contenido/CMS resuelta.
- Estrategia de diseño/componentes resuelta.
- Pruebas y criterios de aceptación definidos.
- Operación, despliegue y respaldos resueltos.
- Supuestos y pendientes visibles.

Asigna resultado:

- `READY`: se puede iniciar diseño técnico detallado e implementación.
- `READY WITH RISKS`: se puede avanzar con riesgos aceptados y reversibles.
- `NOT READY`: existen vacíos bloqueantes.

No comiences implementación sustantiva sin mostrar este resultado.

## Formato de respuesta al usuario

Presenta:

1. Resumen ejecutivo del proyecto.
2. Clasificación y nivel de complejidad.
3. Stack recomendado en tabla: necesidad, elección, motivo, alternativa y disparador de cambio.
4. Arquitectura propuesta.
5. Documentos creados o por crear.
6. Riesgos, supuestos y pendientes.
7. Readiness Check.
8. Próximo paso único recomendado.

## Criterio de calidad

El Blueprint es correcto cuando otro agente o desarrollador puede abrir el repositorio y comprender:

- qué se construye y para quién;
- qué no se construye todavía;
- cómo se organiza;
- por qué se eligió cada componente;
- qué datos existen y quién puede verlos;
- cómo se prueba, despliega, opera y mantiene;
- qué información sigue pendiente;
- qué reglas no debe romper la IA.
