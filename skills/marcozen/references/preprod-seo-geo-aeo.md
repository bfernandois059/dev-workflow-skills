# Auditoría SEO / GEO / AEO pre-producción — MarcoZen

Checklist para evaluar la preparación técnica, semántica y de confianza de sitios web y e-commerce públicos indexables frente a buscadores y sistemas de IA.

> **Regla de aplicabilidad:** Este checklist aplica **exclusivamente a sitios web públicos que buscan indexación y captación orgánica**. Para APIs privadas, intranets, plataformas SaaS detrás de login o librerías de software, este dominio es **N/A** y no debe penalizar la auditoría.

> **Regla de honestidad:** MarcoZen **no promete indexación inmediata ni resultados garantizados**. Evalúa preparación técnica y semántica para que buscadores y agentes de IA puedan rastrear, interpretar y representar el sitio.

---

## Clasificación de Controles y Severidad

Los controles en este dominio se dividen en **Contextuales** y de **Optimización**:

### 1. Controles Contextuales (Importantes según modelo de negocio)
Afectan directamente el rastreo y la indexación de páginas públicas. Su ausencia en un sitio comercial público suele constituir hallazgos **P1** o **P2**:

- **Rastreabilidad básica:**
  - `robots.txt` no bloquea por error rutas públicas que deben indexarse.
  - `sitemap.xml` presente, accesible y con URLs absolutas canónicas.
- **Canonical y duplicidad:**
  - Etiqueta `canonical` por página para prevenir contenido duplicado entre parámetros o protocolos.
- **Status codes correctos:**
  - URLs vivas devuelven HTTP 200.
  - URLs inexistentes devuelven HTTP 404 real (nunca 200 "blando").
  - Redirecciones permanentes utilizan 301 sin cadenas encadenadas.
- **Metadatos esenciales:**
  - `title` y `meta description` únicos y descriptivos en las páginas clave de captación.
  - Open Graph básico (`og:title`, `og:description`, `og:image`, `og:url`) para enlaces compartidos en mensajería y redes sociales.
- **Estructura semántica:**
  - Un encabezado principal `<h1>` claro por página y jerarquía coherente de `<h2>`/`<h3>`.
  - Imágenes principales con atributo `alt` descriptivo.

---

### 2. Controles de Optimización (Nice-to-have / Evolución futura)
Mejoras incrementales de visibilidad, refinamiento semántico o presencia en agentes de IA. Constituyen hallazgos **P3**:

- **Archivos de contexto para IA:**
  - `llms.txt` público con descripción resumida de la entidad y mapa de documentación.
  - `llms-full.txt` para repositorios o catálogos extensos.
- **Datos estructurados avanzados (Schema.org):**
  - Esquemas complementarios (`FAQPage`, `BreadcrumbList`, `Service`). (Nota: `Review` y `AggregateRating` solo deben incluirse si existen testimonios reales verificables; nunca inventar ratings).
- **AEO (Answer Engine Optimization):**
  - Bloques de preguntas frecuentes concisas que respondan intenciones de búsqueda directa.
  - Párrafos de definición autocontenidos tipo "¿qué es X?".
- **Optimizaciones incrementales de Core Web Vitals:**
  - Afinar métricas de rendimiento (LCP, INP, CLS) cuando ya se encuentran en umbrales aceptables.

---

> **Regla estricta:** La ausencia de controles de optimización (como `llms.txt`, esquemas avanzados o micro-mejoras de CWV) **NUNCA debe ser considerada un bloqueador para salir a producción ni justificar un veredicto de "No listo para producción"**.
