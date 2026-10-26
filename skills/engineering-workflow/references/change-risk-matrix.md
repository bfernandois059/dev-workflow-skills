# Change Risk Matrix

## LOW

Ejemplos:

- texto o estilos acotados;
- documentación;
- corrección localizada sin datos;
- test adicional.

Mínimo:

- diff completo;
- lint/typecheck aplicables;
- prueba focalizada;
- documentación si cambia comportamiento.

## MEDIUM

Ejemplos:

- nueva pantalla o flujo;
- formulario;
- email transaccional;
- nueva dependencia;
- API interna;
- generación de PDF no crítica.

Mínimo:

- tests focalizados;
- build;
- manejo de errores;
- revisión de variables de entorno;
- actualización de documentación y changelog.

## HIGH

Ejemplos:

- autenticación o permisos;
- migración de datos;
- pagos;
- archivos privados;
- integraciones externas críticas;
- cambios de contratos públicos;
- infraestructura o despliegue;
- **ampliación de la superficie alcanzable**: una tabla, vista, endpoint, ruta pública, bucket o webhook nuevo; habilitar un proveedor de identidad o una capacidad en la consola de un servicio externo.

Mínimo:

- plan de migración y rollback;
- pruebas positivas y negativas;
- revisión de seguridad;
- ADR o actualización arquitectónica;
- runbook;
- revisión humana obligatoria antes del merge.

## CRITICAL

Ejemplos:

- pérdida o transformación irreversible de datos;
- cambio de autorización global;
- manejo de información altamente sensible;
- producción sin rollback viable;
- rotación o exposición de secretos;
- cambio del modelo de acceso o de registro de cuentas del producto;
- incidente activo.

Requisitos:

- no ejecutar automáticamente;
- autorización explícita;
- respaldo verificado;
- plan de rollback ensayado o claramente operativo;
- doble revisión cuando sea posible;
- ventana y monitoreo de despliegue;
- registro de incidente o decisión.

---

## Controles que acompañan un cambio de superficie

La superficie alcanzable es el conjunto de puntos por los que alguien puede entrar o pedir
datos. Cuando un cambio agrega uno, estos son los controles que viajan **con ese cambio**, no
una batería genérica de seguridad: son pocos, específicos y verificables.

| Lo que agrega el cambio | Controles que lo acompañan |
|---|---|
| **Tabla, vista o colección** | Control de acceso activo en el servidor y al menos una política que filtre por propietario o inquilino; prueba del caso denegado (usuario autenticado ajeno al recurso no la lee ni la muta) |
| **Endpoint, server action o ruta de API** | Autenticación y autorización en el servidor, no solo en la interfaz; prueba de qué devuelve a un visitante anónimo y a uno con rol menor |
| **Página o ruta nueva** | Si muestra datos de terceros, el control va antes de la consulta: comprobar que no se filtran datos en el render previo a un redirect |
| **Bucket o ruta de almacenamiento** | Bucket privado para contenido privado, política por ruta de propietario y URLs firmadas con vigencia acotada en lugar de URLs públicas permanentes |
| **Webhook entrante** | Verificación de firma antes de procesar, idempotencia y rechazo de lo no firmado |
| **Proveedor de identidad o capacidad habilitada en una consola** | Quién puede llegar ahora, y si eso coincide con el modelo de acceso declarado del producto |
| **Ruta que acepta un destino como parámetro** (`?next=`, `?redirect=`, `?returnTo=`) | Validar el destino contra rutas internas permitidas; rechazar hosts externos y rutas protocolo-relativas (`//evil.example`). En un flujo de autenticación es vector de robo de token, no solo de phishing |
| **Variable de entorno nueva** | Entrada en `.env.example`; si el valor es secreto, que no lleve un prefijo que el framework exponga al navegador (`NEXT_PUBLIC_`, `VITE_`, `PUBLIC_`) |

Dos reglas que hacen que esto no se infle:

- **El caso denegado es el control, no la cobertura.** Una prueba del camino feliz con la
  cuenta propia no prueba autorización. Un caso denegado por cada superficie nueva es
  suficiente; no hace falta una matriz completa de roles para agregar una tabla.
- **Default-deny antes de política fina.** Verificar que el estado por defecto niegue es más
  importante que afinar reglas. Dos estados opuestos que se confunden: control activo **sin
  ninguna regla** niega todo (fallo funcional, se nota de inmediato); reglas escritas **sin el
  control activado** no se aplican (fallo de seguridad, no se nota nunca).

Lo que **no** corresponde aquí: auditar la superficie que el cambio no tocó. Eso es una
auditoría de seguridad, y la hace `marcozen` en sus modos de seguridad y pre-producción.

## El cambio sin diff

Un cambio aplicado en la consola de un proveedor —habilitar un registro, cambiar la
visibilidad de un bucket, activar un proveedor social, editar una variable de producción,
desactivar la protección de un entorno— **no aparece en el diff**, no pasa por revisión y no
queda en el historial. Es el punto ciego completo del flujo de Pull Request.

Cuando un cambio depende de configuración externa, esa configuración es parte del cambio:

1. **Se declara en la Pull Request**, con el antes y el después y quién puede llegar ahora a
   qué. Sin esa línea, nadie puede revisarlo ni revertirlo.
2. **Se registra dónde vive**, para que una auditoría posterior pueda verificarlo en vez de
   adivinarlo (`.env.example` para variables, el documento de seguridad y operación para
   políticas y entornos).
3. **La tarea no está terminada mientras la configuración no esté aplicada en el entorno real.**
   Un cambio correcto en el código con el control pendiente en la consola es un cambio que no
   protege nada.
