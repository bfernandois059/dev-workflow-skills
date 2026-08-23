# Identidad visible y páginas de error — pre-producción

Checklist bloqueante para el **Modo 2 (pre-producción)** de MarcoZen. Cubre dos cosas que casi
nunca están y que se notan el primer día en producción: **las páginas de error** y **los
íconos y la imagen social**.

No son detalles estéticos. Un 404 genérico pierde una visita que ya llegó, y una imagen social
rota convierte cada enlace compartido en texto plano. Ambas cosas cuestan poco antes de
publicar y son caras después, porque **quedan en caché**.

Marca cada punto como ✅ ok · ⚠️ parcial · ❌ falta · N/A, con severidad P0–P3.

---

## Páginas de error

### El estado HTTP

- **Una URL inexistente devuelve 404 real**, no 200 con un cuerpo que dice "no encontrado".
  El 200 blando le dice al buscador que la página existe y hace que indexe basura. `P1`.
- Errores del servidor devuelven **500**, no 200.
- Redirecciones permanentes son **301**, no 302 encadenados.

Se comprueba mirando el estado, no la pantalla:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://dominio/esta-ruta-no-existe
```

### La página que ve la persona

- **Existe una página 404 propia.** Si aparece la pantalla por defecto del framework, del
  servidor o del hosting, es hallazgo: `P1` en un sitio público comercial, `P2` en una
  herramienta interna.
- **Nunca muestra el error crudo**: sin stack trace, sin ruta de archivo, sin versión del
  framework, sin volcado de variables. Eso es `P0` — filtra información del servidor.
- **Conserva encabezado, navegación y marca.** El usuario tiene que saber que sigue dentro del
  sitio y no en una pantalla del navegador.
- **Una línea que dice qué pasó**, en el idioma del sitio y sin jerga. Nada de "Error 404 —
  Not Found" como único contenido.
- **Dos o tres destinos que realmente sirven**, elegidos por negocio: el catálogo, el servicio
  principal, contacto. "Volver al inicio" solo, es rendirse: la persona llegó buscando algo.
- **Buscador** si el sitio tiene catálogo o contenido extenso.
- La página de **error 500** recibe el mismo trato, con la diferencia de que ahí sí conviene
  ofrecer una vía de contacto.

### Verificación

- Visitar una URL inventada en **escritorio y móvil**, no solo en local: en producción el
  hosting puede interceptar antes que la aplicación.
- Comprobar que el 404 no rompe el layout ni pierde la navegación.
- Si hay registro de errores, revisar los 404 acumulados: son enlaces rotos reales o URLs
  antiguas que merecen un 301.

---

## Íconos e imagen social

El problema no es ponerlos, es **ponerlos una vez y bien**. Navegadores, buscadores y redes
cachean estos archivos de forma agresiva y por rutas fijas; corregirlos después tarda días y
en algunas plataformas no se puede forzar.

### Convención de archivos

Todos en el directorio público que se sirve en la raíz del dominio — `public/`, `static/` o
`www/` según el stack — y referenciados desde la raíz (`/archivo.png`).

| Archivo | Tamaño | Formato | Para qué |
|---|---|---|---|
| `/favicon.ico` | 32×32 (o multi 16/32/48) | ICO | Ruta fija que muchos clientes piden a ciegas, sin leer el HTML |
| `/icon.svg` | vectorial | SVG | Ícono nítido a cualquier tamaño; admite variante oscura dentro del propio SVG |
| `/icon-192.png` | 192×192 | PNG | Manifest / Android |
| `/icon-512.png` | 512×512 | PNG | Manifest / splash |
| `/icon-maskable-512.png` | 512×512 | PNG | Variante *maskable*: el arte vive dentro de la zona segura central, el sistema recorta el resto |
| `/apple-touch-icon.png` | 180×180 | PNG **opaco** | iOS al añadir a pantalla de inicio |
| `/og.png` | 1200×630 | PNG o JPG | Imagen al compartir el enlace |
| `/site.webmanifest` | — | JSON | Nombre, colores e íconos de la app |

Notas que evitan los errores más comunes:

- **`apple-touch-icon` sin transparencia y sin esquinas redondeadas.** iOS compone la
  transparencia sobre negro y aplica su propia máscara: un PNG transparente se ve como un
  borrón oscuro, y unas esquinas ya redondeadas se ven recortadas dos veces.
- **La imagen OG debe declararse con URL absoluta y HTTPS**, con el dominio de producción:
  `https://dominio.cl/og.png`, nunca `/og.png`. Es el fallo más frecuente y el más silencioso:
  la etiqueta existe, valida, y no se renderiza en ninguna parte.
- Declarar también `og:image:width` y `og:image:height`: ayuda a que el primer rastreo dibuje
  la tarjeta completa en vez de un enlace desnudo.
- El texto dentro de la imagen OG tiene que sobrevivir al recorte: cada plataforma corta
  distinto, así que lo importante va en el centro y no cerca de los bordes.
- Si el sitio usa `twitter:card`, `summary_large_image` es lo que muestra la imagen grande.

### La regla de caché

**Nunca se sobrescribe uno de estos archivos en su sitio.** Cuando cambie el ícono o la imagen
social, se publica con **nombre nuevo versionado** y se actualiza la etiqueta que lo apunta:

```
og.png        →  og-v2.png
icon.svg      →  icon-v2.svg
```

Cambiar el nombre invalida todas las cachés a la vez: CDN, rastreadores y navegadores. Editar
el archivo dejando el mismo nombre no invalida ninguna.

Dos rutas no se pueden versionar porque los clientes las piden a ciegas: `/favicon.ico` y
`/apple-touch-icon.png`. Se mantienen, y además se declara la versión nueva con `<link>` para
que quien lea el HTML la tome de inmediato.

Algunas plataformas permiten forzar un nuevo rastreo del enlace —Facebook y LinkedIn tienen
herramientas públicas para eso— y otras no ofrecen ninguna. Por eso la versión del nombre no
es opcional: es lo único que funciona en todas.

### Comprobación

- Los archivos existen y responden **200** en las rutas declaradas.
- Ninguna etiqueta apunta a un archivo que no está (un `og:image` roto es peor que ausente).
- El favicon se ve en una pestaña nueva, en claro y en oscuro.
- La tarjeta social se ve completa al compartir el enlace de producción, no el de staging.

### Severidades sugeridas

| Situación | Severidad |
|---|---|
| Página de error muestra stack trace o rutas del servidor | `P0` |
| No hay página 404 propia en un sitio público comercial | `P1` |
| URL inexistente devuelve 200 (404 blando) | `P1` |
| `og:image` con URL relativa, o apuntando a un archivo inexistente | `P1` |
| Sin Open Graph en un sitio cuyos enlaces se comparten | `P1` |
| Sin favicon | `P2` |
| Imagen OG con proporción o tamaño incorrecto, texto recortado | `P2` |
| No hay página 404 propia en una herramienta interna | `P2` |
| Sin `apple-touch-icon` ni íconos del manifest | `P3` |

---

## Nota sobre frameworks

Varios frameworks generan estas etiquetas a partir de archivos con nombre convenido y les
añaden un hash, lo que resuelve la caché solo. Si el stack lo soporta, **usa esa vía en vez de
las etiquetas a mano**: es menos código y elimina el problema de versionado. Verifica igual el
resultado renderizado — lo que importa es la etiqueta que llega al navegador, no la convención
que la produjo.
