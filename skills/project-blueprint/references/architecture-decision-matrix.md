# Architecture Decision Matrix

## Framework / entrega
- Sitio pequeño, contenido estable, sin administración: HTML/SSG o framework estático.
- SEO fuerte, contenido dinámico, React, rutas híbridas: Next.js.
- Aplicación interna sin SEO: React/Vite u otro frontend adecuado; evaluar backend separado.
- CMS existente y presupuesto limitado: mejorar CMS antes de reescribir.
- Backend intensivo o dominio complejo: servicio dedicado con API tipada.

## Base de datos
- Ninguna persistencia: no agregar DB.
- Datos relacionales, permisos, reportes: PostgreSQL.
- Supabase: PostgreSQL administrado + Auth/Storage/Realtime útiles en conjunto.
- SQLite: prototipo/local/volumen bajo con despliegue compatible.
- NoSQL: solo con patrón de acceso que lo justifique.

## CMS
- Sin editor no técnico: contenido en código/MDX puede bastar.
- Editor frecuente, workflow simple: headless CMS o CMS tradicional.
- Omnicanal, contenido estructurado, preview: headless CMS.
- Catálogo técnico complejo: modelar taxonomías y relaciones antes de elegir proveedor.

## Autenticación
- Sitio público: ninguna.
- Equipo pequeño: proveedor administrado.
- B2B corporativo: SSO/OIDC/SAML según clientes.
- Autorización: RBAC por defecto; ABAC solo si reglas realmente lo requieren.

## Archivos
- Assets de frontend: CDN del hosting.
- Cargas privadas: object storage con URLs firmadas y políticas.
- Evidencia crítica: versionado, checksum, auditoría y retención.

## PDF
- Pocas piezas manuales: diseño externo/manual.
- Documento dinámico simple: HTML/CSS a PDF server-side.
- Alto volumen o layouts complejos: motor/servicio especializado y pruebas visuales.
- Documento legal: validar firma, inmutabilidad, numeración y archivo.

## Email / notificaciones
- Formularios simples: proveedor transaccional.
- Flujos críticos: cola, reintentos, idempotencia, logs y plantillas versionadas.
- Mensajería omnicanal: consentimiento, preferencias y fallback.

## Diseño de componentes
- Proyecto pequeño: componentes base + componentes por sección.
- Producto mediano: primitives + componentes de dominio + patrones.
- Suite grande: design tokens, biblioteca y documentación.
- Atomic Design solo si el equipo comprende y mantiene sus niveles; no fragmentar componentes sin beneficio.

## Motion
- Usar para feedback, transición de estado, orientación y jerarquía.
- Respetar prefers-reduced-motion.
- No bloquear interacción, SEO, rendimiento ni lectura.

## Testing
- Siempre: lint, typecheck, unit tests donde aportan, build.
- Flujos críticos: integración y E2E.
- UI importante: visual regression.
- APIs/integraciones: contract tests.
- Seguridad: dependency scan, secret scan y revisión de permisos.

## Señales para aumentar complejidad
- múltiples organizaciones;
- roles y permisos finos;
- datos sensibles;
- pagos;
- integraciones críticas;
- procesamiento asíncrono;
- auditoría legal;
- alto volumen;
- operación 24/7;
- varios equipos desplegando de forma independiente.
