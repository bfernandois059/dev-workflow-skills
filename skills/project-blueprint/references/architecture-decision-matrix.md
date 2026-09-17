# Architecture Decision Matrix

Esta matriz proporciona **señales de decisión y criterios analíticos**, no recetas universales ni respuestas automáticas. Su objetivo es ayudar al arquitecto o agente a estructurar cada recomendación respondiendo:

1. **Necesidad:** Problema técnico, operativo o de negocio que se debe resolver.
2. **Opción recomendada:** Solución técnica o patrón propuesto.
3. **Motivo:** Justificación frente al contexto y restricciones reales.
4. **Alternativa razonable:** Segunda opción viable analizada y por qué se descartó (sin forzar alternativas irrelevantes).
5. **Disparador de cambio:** Condición objetiva bajo la cual convendría migrar a otra solución.

---

## 1. Framework y entrega (Rendering / Hosting)

- **Señal: Contenido estático, bajo mantenimiento, sin usuarios ni transacciones.**
  - *Recomendación:* HTML/CSS puro, Astro, Vite estático o generador estático ligero.
  - *Motivo:* Complejidad mínima, costo casi nulo, máxima seguridad y rendimiento inmediato.
  - *Alternativa razonable:* Framework con SSR/Node.js (descartado por sobrecoste operativo y superficie de ataque innecesaria).
  - *Disparador de cambio:* Requerir autenticación dinámica o renderizado por usuario en servidor.

- **Señal: Requerimiento estricto de SEO dinámico + interactividad React enriquecida + rutas híbridas.**
  - *Recomendación:* Next.js o framework SSR full-stack similar.
  - *Motivo:* Unifica renderizado de servidor para indexación y cliente para reactividad.
  - *Alternativa razonable:* SPA desacoplada con backend REST/GraphQL (descartada si penaliza SEO o encarece el setup inicial).
  - *Disparador de cambio:* Si la aplicación no requiere SEO público y se convierte en herramienta puramente interna.

- **Señal: Aplicación o panel interno detrás de autenticación (sin requisito de SEO).**
  - *Recomendación:* SPA (Vite + React/Vue/Svelte) sobre hosting estático (CDN) con API backend desacoplada.
  - *Motivo:* Despliegue simple, costos bajos, caché agresiva y aislamiento entre frontend y servicios de datos.
  - *Alternativa razonable:* Framework SSR unificado (descartado si añade complejidad de servidor sin ventaja operativa).
  - *Disparador de cambio:* Necesidad de renderizado server-side para tiempos de carga inicial ultrarrápidos en redes móviles degradadas.

---

## 2. Persistencia y base de datos

- **Señal: Sin persistencia de usuarios, formularios ni transacciones.**
  - *Recomendación:* No agregar base de datos.
  - *Motivo:* Evita costos, mantenimiento de esquemas, respaldos y vectores de ataque.
  - *Alternativa:* Base de datos embebida (descartada por innecesaria).

- **Señal: Modelo relacional, transacciones, integridad referencial y permisos estructurados.**
  - *Recomendación:* PostgreSQL administrado.
  - *Motivo:* Estándar de la industria, consistencia ACID, ecosistema maduro y soporte para extensiones (JSONB, pgvector, full-text).
  - *Alternativa razonable:* MySQL o SQLite en disco local (descartada según soporte de hosting y concurrencia requerida).
  - *Disparador de cambio:* Requerir un esquema de documentos no estructurados con patrones de consulta ultra-particionados.

- **Señal: Postgres relacional + Auth + Storage + funciones/realtime en un único proveedor.**
  - *Recomendación:* Supabase.
  - *Motivo:* Reduce significativamente el tiempo de puesta en marcha unificando capas esenciales sobre Postgres estándar.
  - *Alternativa razonable:* Servicios independientes (Postgres en Neon/RDS + Auth0/Clerk + S3) (descartada si aumenta dispersión administrativa en etapas tempranas).
  - *Disparador de cambio:* Requerir control a nivel de kernel/infraestructura de base de datos o modelos de pricing incompatibles.

- **Señal: Prototipo local, herramienta de escritorio, script de un solo nodo o volumen muy bajo.**
  - *Recomendación:* SQLite.
  - *Motivo:* Cero configuración, portabilidad total y latencia mínima sin dependencias de red.
  - *Alternativa razonable:* Base de datos cliente-servidor (descartada si complica el despliegue de una herramienta mononodo).
  - *Disparador de cambio:* Múltiples nodos de escritura concurrentes o arquitectura serverless multiregión sin replicación distribuida (Litestream/Turso).

---

## 3. CMS y gestión editorial

- **Señal: El contenido cambia con los despliegues de desarrollo y no hay editores no técnicos.**
  - *Recomendación:* Archivos de contenido en repositorio (Markdown / MDX / JSON).
  - *Motivo:* Trazabilidad total en Git, control de cambios, sin infraestructura adicional.
  - *Disparador de cambio:* Usuarios de marketing o redacción necesitan publicar autónomamente sin pasar por Git.

- **Señal: Editores no técnicos publican regularmente páginas, noticias o artículos.**
  - *Recomendación:* Headless CMS (Sanity, Strapi, Decap, Payload) o CMS tradicional según equipo.
  - *Motivo:* Separa ciclo de vida del contenido del ciclo de desarrollo de código; interfaz amigable para no técnicos.
  - *Alternativa razonable:* CMS tradicional tipo WordPress (válido si el cliente ya cuenta con soporte y experiencia previa).
  - *Disparador de cambio:* Contenido altamente interconectado con datos operativos y transaccionales del core de negocio.

---

## 4. Autenticación y control de acceso

- **Señal: Plataforma pública sin personalización ni áreas restringidas.**
  - *Recomendación:* Sin autenticación.
  - *Motivo:* Máxima privacidad y simplicidad.

- **Señal: Usuarios con cuentas propias, panel privado y equipo técnico reducido.**
  - *Recomendación:* Proveedor de identidad administrado (Supabase Auth, Clerk, Auth0, Lucia/AuthKit).
  - *Motivo:* Mitiga riesgos críticos de seguridad (hashing, sesiones seguras, recuperación de contraseña, MFA).
  - *Alternativa razonable:* Autenticación manual con bcrypt y cookies (descartada si el equipo no cuenta con experiencia en seguridad de sesiones).
  - *Disparador de cambio:* Requerir protocolos corporativos federados (SAML/SCIM) o aislamiento estricto en infraestructura propia.

- **Señal: Múltiples perfiles de usuario con permisos diferenciados.**
  - *Recomendación:* RBAC (Role-Based Access Control) por defecto. Mantener roles planos y mapear acciones.
  - *Alternativa:* ABAC (Attribute-Based Access Control) solo si existen reglas contextuales complejas (ej. "acceso solo en horario laboral y desde sucursal asignada").

---

## 5. Almacenamiento y procesamiento de archivos

- **Señal: Assets estáticos de diseño (logos, íconos, banners de interfaz).**
  - *Recomendación:* CDN del proveedor de hosting / bundle estático.

- **Señal: Documentos privados de usuarios, contratos, comprobantes o fotos subidas.**
  - *Recomendación:* Object storage privado (S3, Cloudflare R2, Supabase Storage) con URLs firmadas temporales.
  - *Motivo:* Evita almacenar binarios en la base de datos o el disco del servidor de aplicaciones; control de acceso granular.
  - *Disparador de cambio:* Requerimiento legal de almacenamiento físico on-premise.

---

## 6. Documentos formales y PDFs

- **Señal: Documentos fijos o excepcionales.**
  - *Recomendación:* Diseño manual o pregenerado. No automatizar prematuramente.

- **Señal: Facturas, certificados, comprobantes u órdenes generadas dinámicamente.**
  - *Recomendación:* Renderizado HTML/CSS server-side a PDF (ej. Chromium headless, Typst, react-pdf) o servicio transaccional.
  - *Motivo:* Reutiliza habilidades web para maquetar documentos dinámicos con precisión visual.
  - *Disparador de cambio:* Volumen masivo (miles por hora) que exija motores binarios optimizados para no saturar memoria.

---

## 7. Comunicaciones transaccionales (Email / SMS / Push)

- **Señal: Notificaciones esenciales (registro, recuperación de clave, alertas).**
  - *Recomendación:* Proveedor transaccional vía API (Resend, Postmark, SendGrid).
  - *Motivo:* Entregabilidad garantizada, reputación de IP administrada y logs de entrega.
  - *Disparador de cambio:* Flujos transaccionales de alto volumen que requieran encolamiento asíncrono, reintentos idempotentes y circuit breakers.

---

## 8. Verificación y estrategia de calidad

*No imponer listas rígidas ni herramientas universales donde no aporten valor real. Definir las verificaciones según el stack, riesgo y runtime:*

- **Proyectos estáticos / contenido (L0/L1):**
  - Verificación de enlaces rotos, sintaxis/formato, accesibilidad fundamental (a11y) y métricas Web Vitals. No exigir unit tests ficticios si no hay lógica ejecutable.
- **Proyectos con JavaScript / TypeScript (L2+):**
  - Typecheck si el proyecto usa TypeScript.
  - Linter si existen convenciones de código compartidas.
  - Tests unitarios: enfocados en lógica de negocio, cálculo financiero, validadores de esquemas y transformaciones complejas.
  - Tests de integración: rutas de API críticas, autenticación y transacciones con la base de datos.
  - Tests E2E: reservados para los 2-3 flujos troncales de usuario (ej. checkout, registro, onboarding).
  - Verificación de build: siempre que el stack requiera compilación antes del despliegue.
- **Seguridad y dependencias:**
  - Auditoría de dependencias conocidas si el proyecto usa gestor de paquetes externo.
  - Detección de secretos si el proyecto maneja variables de entorno o credenciales.
  - Verificación de permisos y autorización si el sistema implementa múltiples roles.

---

## 9. Señales que justifican aumentar complejidad

Solo escalar la arquitectura ante la presencia de señales concretas:
- Múltiples organizaciones con aislamiento estricto de datos (multi-tenant).
- Cumplimiento regulatorio vinculante (GDPR, PCI-DSS, HIPAA, normativas financieras).
- Cargas asíncronas pesadas que degraden peticiones HTTP sincrónicas (requiere colas y workers).
- Concurrencia masiva real comprobada (no hipotética).
- Múltiples equipos autónomos desplegando subsistemas en ciclos independientes (justifica desacoplar servicios).
