# Auditoría SEO / GEO / AEO pre-producción — MarcoZen

Checklist para evaluar si un sitio web o e-commerce está preparado, a nivel técnico,
semántico y de confianza, para que **buscadores y sistemas de IA** puedan rastrearlo,
entenderlo y representarlo. Aplica en el **Modo 2 (pre-producción)** y **Modo 3 (SEO/GEO/AEO)**.

> **Regla de honestidad (repetir al usuario):** MarcoZen **no promete indexación inmediata
> ni resultados garantizados**. Evalúa *preparación*: que el sitio sea rastreable,
> entendible y confiable. El ranking depende de factores externos y del tiempo.

Marca cada punto como ✅ ok · ⚠️ pendiente/parcial · ❌ falta · N/A. Asigna severidad
P0–P3 (ver `SKILL.md`). Solo lectura: no modifiques archivos en la fase de auditoría.

## SEO técnico

- `sitemap.xml` o `sitemap.ts` presente, válido y con las URLs reales.
- `robots.txt` o `robots.ts` correcto (no bloquea lo que debe indexarse; referencia el sitemap).
- **Canonical** por página (evita contenido duplicado).
- **Metadata por página**: no todas heredando el mismo title/description.
- **Titles y descriptions** únicos, descriptivos, con longitud razonable.
- **Open Graph** (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`).
- **Twitter/X cards** si aplica (`twitter:card`, etc.).
- **Redirects** correctos (301 para permanentes; sin cadenas largas).
- **Status codes** correctos (200 en páginas vivas, 404 real en inexistentes, sin 200 "blandos").
- **Páginas huérfanas**: que toda página importante tenga enlaces entrantes.
- **URLs limpias**: legibles, sin parámetros innecesarios, coherentes.
- **Imágenes con `alt`** descriptivo.
- **Performance mobile** razonable.
- **Core Web Vitals** si hay datos (LCP, INP, CLS).

## Estructura semántica

- Un **H1 claro por página** (uno solo, describe la página).
- **H2/H3 ordenados** jerárquicamente (sin saltos arbitrarios).
- **Contenido escaneable** (párrafos cortos, listas, subtítulos).
- **Breadcrumbs** donde aporten navegación.
- **Enlazado interno** coherente entre páginas relacionadas.
- **Páginas fuente** (pilares de contenido) identificables.
- **FAQs** cuando aportan valor real (no relleno).

## Schema (datos estructurados) recomendado

Según el tipo de sitio, evaluar la presencia y validez de:

- `Organization` · `WebSite` · `BreadcrumbList` (base para casi todos).
- `Product` · `Offer` · `ShippingDetails` (e-commerce).
- `FAQPage` · `Article` · `Person` · `Service`.
- `LocalBusiness` (negocio con ubicación física).
- `Review` **solo si es real y verificable**.
- `AggregateRating` **solo si hay reseñas verificables** (no inventar ratings).

Verificar que el schema **refleje el contenido real** de la página y valide sin errores.

## YMYL / E-E-A-T (si aplica)

Para temas sensibles (**salud, finanzas, legal, educación**, u otros que afecten decisiones
importantes de la persona), evaluar señales de experiencia, pericia, autoridad y confianza:

- **Autoría visible** (quién escribe).
- **Revisión profesional** cuando corresponde.
- **Disclaimers** apropiados.
- **Bibliografía o fuentes** citadas cuando corresponda.
- **Páginas legales** completas.
- **Datos de contacto** reales y visibles.
- **Políticas claras** (privacidad, términos, devoluciones).
- **Claims responsables** (sin promesas exageradas o falsas).
- **Fecha de actualización** en contenidos críticos.

## AEO (Answer Engine Optimization)

Preparación para que motores de respuesta y asistentes extraigan respuestas claras:

- **Respuestas breves y directas** a preguntas concretas.
- **Definiciones claras** de conceptos clave.
- **Bloques pregunta/respuesta**.
- **FAQs útiles** (que respondan dudas reales).
- Contenido que **responda la intención de búsqueda**, no solo palabras clave.
- **Fragmentos resumibles** (un párrafo que se sostenga solo).
- Secciones tipo **"qué es"**, **"para qué sirve"**, **"cuándo usar"**, **"precauciones"**.

## GEO / visibilidad en IA

Coherencia de entidad para que los sistemas de IA representen bien la marca:

- **Entidad de marca consistente** en todo el sitio.
- **Nombre comercial consistente** (mismo nombre en todas partes).
- **Fundador/equipo** si aplica.
- **Ubicación/país** si aplica.
- **Páginas fuente claras** (dónde vive la información canónica).
- **`llms.txt` público** (guía para agentes/IA sobre el sitio).
- **`llms-full.txt`** si el sitio es complejo.
- **Contenido canónico y actualizado** (sin versiones contradictorias).
- **Coherencia entre sitio, redes, perfiles y documentación** (misma info clave).
- **No prometer** indexación inmediata ni resultados garantizados.
