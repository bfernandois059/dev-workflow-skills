# Identidad Visible y Páginas de Error — Pre-Producción

Guía de verificación para el **Modo 2 (pre-producción)** de MarcoZen. Cubre dos elementos críticos de experiencia e indexabilidad que suelen olvidarse antes de salir a producción: **las páginas de error del sistema** y **las piezas de identidad visible en red**.

> **Aplicabilidad:** Aplica principalmente a **sitios web y aplicaciones públicas accesibles por navegadores**. Para APIs backend puras, librerías o herramientas de terminal, este apartado es **N/A**.

---

## 1. Páginas de error

### Estado HTTP y manejo de errores crudos
- **HTTP 404 real:** URLs inexistentes devuelven código de estado 404 real, nunca 200 con mensaje de texto ("soft 404"). En sitios públicos que dependen de buscadores, el 200 blando contamina la indexación (`P1`).
- **Errores del servidor (HTTP 500):** Devuelven código 500, no 200.
- **Prohibición de errores crudos (P0 de seguridad):** La página de error **NUNCA debe exponer volcados de memoria, stack traces, rutas absolutas del servidor ni variables de entorno**. La exposición de trazas es un hallazgo crítico P0.

### Experiencia de usuario en página 404
- **Página personalizada que preserva marca:** La página 404 mantiene encabezado, navegación y estética del producto, evitando la pantalla por defecto del framework o servidor (`P1` en e-commerce/web comercial; `P2` en aplicaciones internas).
- **Destinos de rescate útiles:** Ofrece 2 o 3 enlaces directos a áreas principales (catálogo, inicio, contacto) en lugar de un mensaje aislado sin salida.

---

## 2. Íconos e identidad social

El objetivo es asegurar que las piezas clave de identidad estén configuradas con rutas definitivas antes de que los navegadores y plataformas sociales las almacenen en caché agresivamente:

- `/favicon.ico` (32×32 o multi-icono) y `/icon.svg` presentes.
- `/apple-touch-icon.png` (180×180 opaco) para accesos directos móviles.
- `/og.png` (1200×630 referenciada con URL absoluta y HTTPS) para previews en WhatsApp, LinkedIn, X, Slack.
- **Regla de versión por cambio:** Cuando se actualice una imagen de identidad en el futuro, debe publicarse con un nombre versionado nuevo (`og-v2.png`) para invalidar cachés de redes sociales de inmediato.

---

## 3. Severidad contextual

- Falta de 404 personalizado o imagen OG en web pública comercial: `P1`/`P2` según impacto en negocio.
- Falta de 404 personalizado en portal interno de empleados: `P2`/`P3`.
- Ausencia de imagen OG en intranet privada no compartible: `N/A`.
- Stack trace expuesto en cualquier 404 o 500: `P0` (riesgo de seguridad).
