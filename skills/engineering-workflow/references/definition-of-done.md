# Definition of Done

Marca solo lo aplicable, pero no omitas silenciosamente los puntos de riesgo.

## Alcance

- [ ] Problema y resultado esperado están claros.
- [ ] Criterios de aceptación están cumplidos.
- [ ] No se agregaron cambios fuera de alcance.

## Paridad contra referencia externa (cuando aplica)

**Si la tarea es una migración, port o reimplementación de algo existente:** debe existir un inventario de paridad —tabla de capacidad del origen contra estado requerido en el destino— construido inspeccionando el código real del origen, no de memoria. Ese inventario es la referencia de aceptación durante toda la tarea y no se redefine entre rondas. Toda capacidad del origen que quede fuera se declara como reducción funcional explícita y requiere confirmación del usuario; no se asume. La revisión responde primero “¿mantiene paridad con el inventario?” y solo después “¿es técnicamente correcta?”.

## Código

- [ ] Sigue patrones existentes.
- [ ] No contiene logs, secretos ni código temporal.
- [ ] Las dependencias nuevas están justificadas.
- [ ] Los errores y estados vacíos están manejados.

## Datos e integraciones

- [ ] Cambios de esquema tienen migración y rollback.
- [ ] Contratos, tipos y consumidores están actualizados.
- [ ] Se consideraron idempotencia, reintentos y fallos.
- [ ] Variables nuevas están en `.env.example`.

## Seguridad y permisos

- [ ] Autorización validada en servidor.
- [ ] Casos permitidos y denegados fueron probados.
- [ ] No se exponen datos o archivos privados.
- [ ] Entradas y archivos están validados.

## UX y accesibilidad

- [ ] Loading, error, vacío y éxito están considerados.
- [ ] Navegación con teclado y labels son adecuados.
- [ ] El cambio funciona en tamaños relevantes.
- [ ] No se introdujeron animaciones perjudiciales.

## Calidad

- [ ] Formato/lint pasaron.
- [ ] Typecheck pasó.
- [ ] Tests aplicables pasaron.
- [ ] Build de producción pasó.
- [ ] El diff completo fue revisado.

## Documentación

- [ ] Changelog actualizado cuando corresponde, o pendiente no conductual anotado según la Fase 10.
- [ ] Documentos funcionales/técnicos actualizados, o pendiente de estado no conductual anotado según la Fase 10.
- [ ] ADR creado o actualizado si cambió una decisión.
- [ ] Runbook o instrucciones operativas actualizadas.

## Entrega

- [ ] Pull Request explica alcance, pruebas y riesgos.
- [ ] CI está aprobada.
- [ ] Conversaciones están resueltas.
- [ ] Merge autorizado explícitamente.
