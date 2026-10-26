# Auditoría de Seguridad Pre-Producción — MarcoZen

Checklist de seguridad para el **Modo 2 (pre-producción)** y **Modo 4 (seguridad)**. Objetivo: identificar vulnerabilidades, filtraciones y riesgos que comprometan la integridad, dinero, datos de usuarios o disponibilidad del sistema **antes de publicar**.

> **Esta referencia cubre lo que se audita leyendo el repositorio.** Las otras dos superficies
> tienen su propia referencia:
>
> - **La consola del proveedor** —registro de cuentas, políticas efectivas en la base de datos,
>   visibilidad de buckets, protección de entornos, alcance de las claves emitidas—:
>   [`external-surface.md`](external-surface.md), que además define el **modelo de acceso
>   declarado**, la premisa sin la cual ningún hallazgo de autorización es formulable.
> - **El despliegue respondiendo** —cabeceras servidas, métodos aceptados, redirecciones,
>   mensajes de login y recuperación, páginas de error, sourcemaps, DNS—:
>   [`deployed-surface.md`](deployed-surface.md). Varios de los controles listados abajo
>   (cabeceras, rate limiting, páginas de error) **solo se verifican ahí**: leer la
>   configuración que pretende producirlos no prueba que se sirvan.

> **Regla de oro sobre secretos y severidad:**  
> **NUNCA expongas credenciales.** Si encuentras secretos reales en el código o historial, reporta únicamente el **tipo de secreto y su ubicación (`archivo:línea`)**.  
> Descarta activamente falsos positivos (roles RLS en SQL, nombres de variable vacíos en `.env.example`, claves públicas de cliente como Stripe pk o Supabase anon, datos de prueba en tests o mocks) antes de declarar un P0. La presencia de un `.env` versionado exige inspección prioritaria pero no equivale mecánicamente a P0 si solo contiene configuración no sensible.

---

## 1. Controles Required / Críticos (Bloqueadores P0 cuando fallan)

- **Ausencia total de secretos reales expuestos:** Claves de API privadas, tokens de servicio, contraseñas de bases de datos o connection strings reales ausentes del código y del control de versiones.
- **Gestión e inspección de `.env`:** Un archivo `.env` versionado requiere inspección prioritaria (sin revelar valores). Si contiene o contenía secretos, credenciales o tokens sensibles reales, constituye un bloqueador **P0**. Si únicamente contiene variables de configuración no sensibles (puertos, URLs públicas o flags locales), se clasifica como hallazgo contextual o mala práctica (P2/P3) para moverlo a `.gitignore`, no como P0 automático.
- **Integridad de pagos y transacciones:** Cualquier flujo de cobro o compra se valida server-to-server; el cliente frontend nunca valida ni confirma por sí solo el éxito de un pago.
- **Integridad de webhooks:** Firmas criptográficas y secretos compartidos verificados server-side antes de procesar eventos externos (Stripe, MercadoPago, PayPal, etc.).
- **Autorización efectiva:** En sistemas con autenticación y perfiles, las operaciones sensibles verifican permisos en el servidor (ej. políticas RLS en base de datos o middleware de autorización de sesión). Un usuario autenticado no debe poder leer ni mutar recursos ajenos.
- **Registro de cuentas coherente con el modelo de acceso declarado:** En un producto de acceso restringido, de provisión por administrador o interno, la creación de cuentas debe estar cerrada o restringida **en el proveedor de identidad**, no solo ausente de la interfaz. Una pantalla de registro que no existe en el frontend no cierra el endpoint de registro del proveedor, que sigue respondiendo.
- **Validación server-side de entradas:** Ninguna mutación crítica confía en la validación del navegador; validación estricta de esquemas, tipos y rangos en el backend.

---

## 1.b Pase de autorización por superficie alcanzable

El modo de falla más caro no es una línea de código mal escrita: es un punto de entrada que
**nadie revisó porque nadie lo listó**. Para que esto sea una verificación y no una impresión,
se enumera; no se muestrea.

1. **Lista la superficie desde el código:** rutas y páginas, endpoints y server actions,
   tablas y vistas expuestas a la API, buckets y rutas de archivos, webhooks entrantes, jobs.
2. **Marca cada punto con el control que lo protege.** Un punto sin control identificado se
   anota como tal: `sin control identificado` es evidencia; *«las rutas protegidas usan
   middleware»* no lo es.
3. **Evalúa cada punto frente a tres visitantes:**

| Visitante | Pregunta | Lo que detecta |
|---|---|---|
| **Anónimo** | Sin sesión, ¿qué obtiene? | Endpoints y tablas abiertos, páginas que filtran datos antes del redirect |
| **Autenticado ajeno** | Con sesión válida pero sin relación con el recurso, ¿puede leerlo o mutarlo cambiando un identificador? | IDOR/BOLA y fugas entre inquilinos |
| **Autenticado con rol menor** | Usuario normal donde se espera administrador: ¿la restricción vive en el servidor o solo en la interfaz? | Autorización implementada únicamente en el frontend |

El segundo visitante es el que más se escapa, porque toda prueba manual se hace con la cuenta
propia y con los datos propios. Un control que solo se probó así no está probado.

4. **Default-deny en superficies de datos nuevas:** una tabla o un bucket que aparece sin
   política no es un caso neutro. Verifica que el estado por defecto niegue. Dos estados que se
   confunden y son opuestos: políticas activas **sin ninguna regla** niegan todo (fallo
   funcional); reglas escritas **sin el control activado** no se aplican (fallo de seguridad).

5. **Dos capas de permisos, no una.** En bases de datos con políticas, el `GRANT` por tabla y
   la política son controles distintos: un `GRANT` de `UPDATE`/`DELETE` al rol autenticado con
   una política mal acotada permite modificar o borrar filas ajenas. Presta atención especial a
   las tablas de bitácora y auditoría, que deberían ser de solo inserción: si se pueden borrar,
   el registro deja de ser evidencia y el borrado destruye el rastro del propio abuso.

6. **Lo que no se pueda verificar desde el repositorio** —estado efectivo de las políticas,
   registro en el proveedor, visibilidad real de un bucket— se reporta `No verificado` con el
   lugar donde se comprueba, según [`external-surface.md`](external-surface.md). No se omite.

---

## 2. Controles Contextuales (P1 / P2 según impacto)

- **Plantilla `.env.example`:** Presente con nombres de variables documentados (sin valores) **únicamente si el proyecto maneja variables de entorno**. Si no hay configuración externa, este punto es N/A.
- **Cabeceras de seguridad HTTP:** HSTS, Content-Security-Policy, X-Content-Type-Options, X-Frame-Options / frame-ancestors, Referrer-Policy y Permissions-Policy en endpoints web y APIs públicas. **Se verifican sobre la respuesta real, no sobre la configuración que las declara.** Son `P2` por defecto y suben a `P1` cuando hay un vector nombrable —sin `X-Frame-Options` ni `frame-ancestors` **sobre el formulario de login**, el clickjacking es ese vector—. No las reportes en un producto que no las necesita.
- **Protección de formularios públicos:** Rate limiting o captcha/Turnstile en formularios expuestos (contacto, registro, recuperación de contraseña) para mitigar abuso automatizado.
- **Dependencias vulnerables (CVEs):** No asumir que toda CVE detectada es P0/P1 automáticamente. Evaluar severidad oficial, versión afectada, alcance (producción vs dependencias dev sin impacto en runtime), reachability y si existe fix o mitigación disponible. Si la herramienta de auditoría (`npm audit`, `pip-audit`, etc.) no puede ejecutarse por falta de red o entorno, reportar como **No verificado**, no como fallo asumido.
- **Políticas de privacidad y términos:** Páginas legales visibles si la plataforma recolecta datos personales, cookies analíticas o procesa pagos.

---

## 3. Controles específicos de infraestructura (Contextuales)

### Si el proyecto utiliza Supabase / PostgreSQL con RLS:
- **Row Level Security (RLS) activo** en todas las tablas con datos de usuarios o sensibles. Las migraciones del repositorio declaran la intención; **no prueban el estado efectivo en producción**. Una tabla creada por SQL directo no hereda la activación que aplica el editor del panel.
- **Alcance de cada política:** una política que filtra por sesión pero no por empresa, expediente o propietario deja ver filas ajenas aun estando activa.
- **Políticas de storage por bucket:** Comprobar que un usuario no pueda descargar archivos de carpetas privadas de otros usuarios.
- **`service_role key` protegida:** El token de administración nunca debe importarse ni empaquetarse en bundles que viajen al navegador del cliente.

### Si el proyecto utiliza autenticación gestionada (Supabase Auth, Clerk, Auth0, Cognito, Firebase):
- **El registro, la confirmación de correo, los proveedores OAuth activos y las redirect URLs permitidas son configuración del proveedor**, no del repositorio. Verifícalos según [`external-surface.md`](external-surface.md) —incluida la sonda de solo lectura— o repórtalos `No verificado`.
- Cerrar el registro por correo y dejar un proveedor social habilitado no cierra el registro: es una puerta paralela.

### Si el proyecto utiliza autenticación propia / sesiones:
- Cookies de sesión con flags `HttpOnly`, `Secure` y `SameSite=Lax/Strict`.
- Hashing seguro de contraseñas (bcrypt, argon2, scrypt) sin implementaciones caseras.
