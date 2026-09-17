# Auditoría de Seguridad Pre-Producción — MarcoZen

Checklist de seguridad para el **Modo 2 (pre-producción)** y **Modo 4 (seguridad)**. Objetivo: identificar vulnerabilidades, filtraciones y riesgos que comprometan la integridad, dinero, datos de usuarios o disponibilidad del sistema **antes de publicar**.

> **Regla de oro sobre secretos:**  
> **NUNCA expongas credenciales.** Si encuentras secretos reales en el código o historial, reporta únicamente el **tipo de secreto y su ubicación (`archivo:línea`)**.  
> Descarta falsos positivos (roles RLS en SQL, nombres de variable vacíos en `.env.example`, claves públicas de cliente) antes de declarar un P0.

---

## 1. Controles Required / Críticos (Bloqueadores P0 cuando fallan)

- **Ausencia total de secretos expuestos:** Claves de API privadas, tokens de servicio, contraseñas de bases de datos o connection strings reales ausentes del código y del control de versiones.
- **Gestión de `.env`:** El archivo `.env` con valores reales no está versionado y está cubierto por `.gitignore`.
- **Integridad de pagos y transacciones:** Cualquier flujo de cobro o compra se valida server-to-server; el cliente frontend nunca valida ni confirma por sí solo el éxito de un pago.
- **Integridad de webhooks:** Firmas criptográficas y secretos compartidos verificados server-side antes de procesar eventos externos (Stripe, MercadoPago, PayPal, etc.).
- **Autorización efectiva:** En sistemas con autenticación y perfiles, las operaciones sensibles verifican permisos en el servidor (ej. políticas RLS en base de datos o middleware de autorización de sesión). Un usuario autenticado no debe poder leer ni mutar recursos ajenos.
- **Validación server-side de entradas:** Ninguna mutación crítica confía en la validación del navegador; validación estricta de esquemas, tipos y rangos en el backend.

---

## 2. Controles Contextuales (P1 / P2 según impacto)

- **Plantilla `.env.example`:** Presente con nombres de variables documentados (sin valores) **únicamente si el proyecto maneja variables de entorno**. Si no hay configuración externa, este punto es N/A.
- **Cabeceras de seguridad HTTP:** HSTS, X-Content-Type-Options, X-Frame-Options / frame-ancestors y Referrer-Policy en endpoints web y APIs públicas.
- **Protección de formularios públicos:** Rate limiting o captcha/Turnstile en formularios expuestos (contacto, registro, recuperación de contraseña) para mitigar abuso automatizado.
- **Dependencias vulnerables:** Revisión de dependencias de producción. Si la herramienta de auditoría (`npm audit`, `pip-audit`, etc.) no puede ejecutarse por falta de red o entorno, reportar como **No verificado**, no como fallo asumido.
- **Políticas de privacidad y términos:** Páginas legales visibles si la plataforma recolecta datos personales, cookies analíticas o procesa pagos.

---

## 3. Controles específicos de infraestructura (Contextuales)

### Si el proyecto utiliza Supabase / PostgreSQL con RLS:
- **Row Level Security (RLS) activo** en todas las tablas con datos de usuarios o sensibles.
- **Políticas de storage por bucket:** Comprobar que un usuario no pueda descargar archivos de carpetas privadas de otros usuarios.
- **`service_role key` protegida:** El token de administración nunca debe importarse ni empaquetarse en bundles que viajen al navegador del cliente.

### Si el proyecto utiliza autenticación propia / sesiones:
- Cookies de sesión con flags `HttpOnly`, `Secure` y `SameSite=Lax/Strict`.
- Hashing seguro de contraseñas (bcrypt, argon2, scrypt) sin implementaciones caseras.
