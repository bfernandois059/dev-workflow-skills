# Auditoría de seguridad pre-producción — MarcoZen

Checklist para el **Modo 2 (pre-producción)** y **Modo 4 (seguridad)**. Objetivo: detectar
lo que podría comprometer datos, dinero o disponibilidad **antes** de publicar.

> **Nunca expongas secretos.** Si encuentras credenciales, reporta solo **tipo + archivo:línea**,
> nunca el valor. Descarta falsos positivos antes de marcar P0 (ver la guía de falsos
> positivos en `audit-prompt.md`: roles RLS, nombres de variable, claves públicas).

Marca ✅ / ⚠️ / ❌ / N/A y asigna severidad P0–P3 (ver `SKILL.md`).

## Secretos y variables

- **Secretos expuestos**: buscar claves/tokens/passwords en el código o el historial.
- **`.env` no versionado** (y `.gitignore` lo cubre).
- **`.env.example` con placeholders** (todas las variables que el código usa, sin valores).
- **Variables de producción no escritas en Markdown** ni en docs versionados
  (los runbooks describen *qué* variables, no sus valores).

## Dependencias

- **Dependencias vulnerables**: correr `npm audit` / `pnpm audit` y revisar críticas/altas.
- Sin dependencias abandonadas o de origen dudoso en superficie sensible.

## Cabeceras y transporte

- **Headers de seguridad** (HSTS, X-Content-Type-Options, X-Frame-Options / frame-ancestors,
  Referrer-Policy, Permissions-Policy).
- **CSP** (Content-Security-Policy) si aplica al tipo de sitio.
- HTTPS forzado.

## Formularios y entradas

- **Validación server-side** (no confiar solo en el cliente).
- **Sanitización** de entradas (evitar inyección / XSS almacenado).
- **Rate limiting** en endpoints públicos.
- **Captcha / Turnstile / reCAPTCHA** en formularios públicos cuando corresponda
  (contacto, registro, newsletter) para frenar spam/abuso.

## Webhooks, pagos y eventos

- **Webhooks validados** (firma/secreto verificado antes de procesar).
- **Pagos validados server-to-server** (no confiar en el retorno del cliente).
- **Protección contra duplicidad de eventos** (idempotencia: no procesar dos veces
  el mismo webhook/pago).

## Datos, logs y privacidad

- **Logs sin datos sensibles** (no loggear secretos, tarjetas ni PII).
- **Datos personales protegidos** (acceso mínimo, cifrado en reposo si aplica).
- **Políticas legales** publicadas (privacidad, términos).

## Operación

- **Backups** definidos y con restore probado.
- **Rollback** documentado (ver deployment-runbook).
- **Permisos mínimos** (principio de menor privilegio en BD, storage, servicios, tokens).

## Nota específica Supabase (si aplica)

- **RLS habilitado** en todas las tablas con datos sensibles (no solo algunas).
- Correr los **advisors de seguridad** de Supabase.
- **Policies de storage** por bucket (que un usuario no lea archivos de otro).
- **Tokens de links públicos** aleatorios y expirables (no adivinables ni permanentes).
- **`service_role key`** nunca en el bundle del cliente.
