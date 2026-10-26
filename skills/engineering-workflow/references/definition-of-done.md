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

**Si el cambio agrega superficie alcanzable** (tabla, vista, endpoint, ruta pública, bucket,
webhook o job nuevo):

- [ ] Cada superficie nueva tiene identificado el control que la protege.
- [ ] El estado por defecto niega: control de acceso activo **y** con al menos una regla que filtre por propietario o inquilino.
- [ ] Existe la prueba del caso denegado con un usuario autenticado ajeno al recurso, no solo el camino feliz con la cuenta propia.

**Si el cambio depende de configuración fuera del repositorio** (registro de cuentas,
visibilidad de un bucket, proveedor de identidad, variables de producción, protección de
entornos):

- [ ] Está declarada en la Pull Request: qué se cambió, en qué servicio y quién puede llegar ahora a qué.
- [ ] Está aplicada en el entorno real, no solo prevista.
- [ ] Quedó registrada donde una auditoría posterior pueda verificarla (`.env.example`, documento de seguridad y operación).

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
