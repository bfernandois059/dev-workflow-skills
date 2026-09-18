# Engine / Capability Routing

Cómo dimensionar la capacidad de razonamiento requerida para una tarea y estructurar su ejecución sin burocracia ni bloqueos artificiales.

Este archivo define el contrato conceptual de capacidad para las skills del repositorio. Establece perfiles y estrategias runtime-agnostic, aplicables en cualquier entorno de ejecución (Claude Code, Codex, Antigravity, ChatGPT u otros), exista o no selector de modelo, soporte de subagentes o conocimiento explícito del modelo actual.

## Principio rector

> **Task risk controls validation depth. Runtime capability influences execution strategy, but never becomes ceremony or an artificial blocker.**

La métrica de eficiencia es el costo total por tarea resuelta (incluyendo iteraciones), pero la capacidad disponible nunca debe convertirse en un bloqueo artificial ni en una ceremonia que detenga el trabajo.

La calidad del software se demuestra mediante **evidencia, pruebas y validación proporcional**, no mediante el nombre o tier supuesto del modelo.

## Perfiles conceptuales de capacidad

Los perfiles representan **necesidades de capacidad de la tarea**, no requisitos de producto ni marcas de modelos:

| Perfil | Necesidad de capacidad | Tareas típicas |
|---|---|---|
| **ALTO** — razonamiento profundo | Sostener múltiples invariantes simultáneos, aislar causas raíz no evidentes, resolver ambigüedad sustantiva y evaluar trade-offs arquitectónicos complejos. | Diagnóstico de bugs sin causa aparente, diseño de arquitectura, refactors estructurales amplios, especificación ambigua, revisión crítica y auditoría de seguridad compleja. |
| **MEDIO** — ejecución guiada | Aplicar un plan ya definido con buen criterio local, siguiendo patrones establecidos del repositorio. | Implementación de planes cerrados, extensión de patrones existentes, tests focalizados, cambios acotados y redacción de documentación o Pull Requests. |
| **BAJO** — mecánico | Transformaciones deterministas, volumen repetitivo y cambios completamente especificados. | Renombres, formato, edición mecánica archivo por archivo, inventarios, extracción, conteo y búsquedas amplias. |

Estos perfiles son **recomendaciones de ejecución interna**, no gates ni condiciones de parada.

## Ejes de decisión

Para estimar internamente si una tarea se beneficia de mayor concentración de razonamiento, evalúa estos cinco ejes:

1. **Ambigüedad de la especificación:** ¿Hay que inferir intención o resolver requisitos contradictorios, o está todo especificado?
2. **Profundidad de razonamiento:** ¿Implica trade-offs reales entre alternativas, o es aplicar una solución estándar del repositorio?
3. **Amplitud de contexto:** Cuántos módulos, servicios o invariantes concurrentes deben mantenerse en mente para no introducir regresiones.
4. **Costo del error:** Impacto si el cambio falla en producción (según `references/change-risk-matrix.md`).
5. **Verificabilidad barata:** ¿Existe un oráculo automático rápido (tests unitarios, typecheck, lint, build) que capture fallos de inmediato?

**El oráculo automático barato es el mayor estabilizador:** cuando la verificación es inmediata y confiable, una ejecución directa es segura porque la máquina cierra la iteración. Cuando el error solo se detectaría en producción o en datos corruptos, prioriza descomposición e inspección rigurosa.

## Ortogonalidad: Riesgo vs Capacidad

El riesgo de la tarea y la capacidad de ejecución son ejes distintos:

- **Riesgo (`LOW / MEDIUM / HIGH / CRITICAL`):** Determina la profundidad obligatoria de validación, atención a seguridad, datos, permisos, planes de rollback y evidencia requerida antes de integrar.
- **Capacidad (`ALTO / MEDIO / BAJO`):** Orientación interna sobre cuánto razonamiento concentrar, qué descomponer, qué tareas son mecánicas o cuándo delegar si el runtime lo soporta.

**No existe una equivalencia rígida como "HIGH siempre exige perfil ALTO":**
- Un cambio de una línea en una política RLS o una regla de autorización es `HIGH` por riesgo, pero su implementación técnica puede ser sumamente directa. Lo obligatorio es la validación exhaustiva (caso permitido, caso denegado, aislamiento, regresión e integridad), no detenerse a exigir un modelo determinado.
- Una tarea mecánica compleja puede involucrar cientos de archivos y alta importancia, pero tener verificación barata por compilador y no requerir capacidad extraordinaria.

## Runtime-Agnostic y Capacidad Desconocida

El workflow debe operar fluidamente en cualquier entorno:

> **Unknown runtime capability is not a failure state.**

- **Si el runtime expone información de capacidades o permite elegir modelo:** selecciona la capacidad conveniente cuando aporte valor real y delega subtareas cuando acelere el trabajo.
- **Si el runtime no expone el modelo, tiene un solo modelo o no permite cambiar:**
  - No intentes adivinar el nombre ni deducir el tier del modelo.
  - No detengas el workflow ni pidas autorización por este motivo.
  - Continúa con la capacidad disponible, compensando con inspección exhaustiva, descomposición en pasos pequeños y validación rigurosa.
- **Nunca detengas una tarea diciendo que "el modelo actual parece inferior al recomendado".** La competencia de la solución se valida con los tests y el diff, no con metadatos del entorno.

## Estrategia de recuperación tras intentos fallidos

No repetir indefinidamente el mismo intento, pero sin acoplar la recuperación al cambio forzoso de modelo.

Si una subtarea falla dos veces consecutivas:

1. **No repetir una tercera vez exactamente el mismo enfoque.**
2. **Revisar la evidencia y el supuesto causal:** releer trazas de error, logs reales e hipótesis iniciales.
3. **Cambiar de estrategia:**
   - Inspeccionar más contexto del código y dependencias.
   - Reducir el problema al caso mínimo reproducible.
   - Escribir una prueba unitaria focalizada para aislar el comportamiento.
   - Explorar una herramienta o enfoque alternativo.
   - Si el entorno ofrece modelos más capaces o delegación, aprovecharlos como opción operativa.

Si existe una limitación técnica demostrada del entorno o herramientas (p. ej., falta de acceso a red, credenciales ausentes o APIs inaccesibles):
- Repórtala con precisión técnica al usuario.
- Entrega todo lo que sí pudo verificarse.
- Registra lo pendiente como no validado (`PARTIALLY VALIDATED`).

## Subagentes y tareas concurrentes (Opcional)

Para tareas extensas con dominios independientes (p. ej., módulos desacoplados, pantallas separadas o tests paralelos):
- **Si el runtime soporta subagentes o ejecución concurrente:** evalúa delegar subtareas independientes para reducir tiempo o aumentar cobertura.
- **Si el runtime es monagente o no ofrece delegación:** resuelve secuencialmente de manera estructurada con el agente actual.

No asumas nombres de herramientas específicas, parámetros particulares de llamada ni la capacidad de fijar el motor de los subagentes. El workflow funciona al 100% con un único agente.

## Salida limpia sin burocracia

El routing de capacidad es una decisión de ejecución interna del agente.

- **No incluyas líneas de motor en la salida estándar** (evita burocracia como `Motor: ALTO (...)`).
- **Menciona capacidades o modelos al usuario únicamente cuando:**
  1. Exista una limitación técnica demostrada que impida avanzar.
  2. El usuario pregunte explícitamente sobre el modelo o configuración.
  3. Recomendar un cambio de configuración en una tarea excepcionalmente difícil represente una ventaja tangible para el usuario.

## Blockers reales vs preferencias

Eliminar gates artificiales de modelo refuerza la seriedad de los blockers reales.

**Bloqueos reales (detienen el trabajo o impiden merge):**
- Falta de datos o especificación indispensable en cambios críticos.
- Falta de permisos o credenciales necesarias para ejecutar una validación sensible.
- Conflicto irresoluble de requisitos que comprometería datos o seguridad.
- Migración destructiva sin plan de rollback acordado.
- CI o tests reales que fallan en el repositorio.
- Defecto funcional reproducible no resuelto.
- Ausencia de autorización explícita para merge.

**Falsos bloqueos (NUNCA detienen el trabajo):**
- "Preferiría un modelo de mayor razonamiento para esta tarea."
- "No conozco el modelo en el que estoy corriendo."
- "El entorno no soporta subagentes."
- "El runtime no me permite cambiar de motor."
