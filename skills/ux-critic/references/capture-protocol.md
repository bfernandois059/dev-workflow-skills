# Capture Protocol

Fase 1 de `ux-critic`. Reglas para **ver** la interfaz antes de juzgarla. Un hallazgo sin
captura o sin medición es una opinión con formato de hallazgo.

## Fuentes, por prioridad

1. **Control de navegador** (MCP de browser, Playwright, Puppeteer). Fuente completa:
   capturas, árbol de accesibilidad, estilos computados, estados interactivos y ejecución del
   inventario objetivo.
2. **Capturas entregadas por el usuario.** Permiten juzgar composición, jerarquía, ritmo y
   copy. **No** permiten medir contraste, tamaños reales ni estados. Pide las que falten en
   vez de suponer.
3. **Solo código.** Último recurso. La auditoría se declara **parcial** en el encabezado del
   informe y se enumeran las capas que no pudiste juzgar. Nunca afirmes jerarquía, ritmo ni
   contraste desde el código.

## Antes de capturar

- Usa **contenido real**, no placeholders. Un sitio se ve ordenado con datos falsos y se
  rompe con un nombre de 40 caracteres o un catálogo de un solo producto.
- Cierra devtools y barras que alteren el ancho del viewport.
- Registra la URL exacta y el estado de sesión (anónimo, autenticado, con carrito, vacío).
- Si hay animaciones de entrada, captura **después** de que terminen y anota cuánto tardaron.

## Viewports mínimos

| Viewport | Por qué |
|---|---|
| **375 × 812** | Piso real de móvil. Si el usuario es móvil-dominante, este es el viewport principal, no el secundario |
| **768 × 1024** | Tablet / punto donde se suelen romper las grillas de 2–3 columnas |
| **1280 × 800** | Portátil común. La mayoría de los "se ve bien" se probaron solo aquí |
| **1440 +** | Revela contenedores sin ancho máximo y líneas de texto imposibles de leer |

En cada viewport: captura del primer pantallazo (sin scroll) **y** captura completa de la
página. El primer pantallazo decide si el usuario se queda; la completa revela el ritmo.

## Estados obligatorios

Un estado que no abriste no está auditado. Mínimo:

| Estado | Cómo forzarlo | Qué revela |
|---|---|---|
| Vacío | Sin resultados, sin datos, cuenta nueva | Si la primera experiencia real es una pantalla muerta |
| Carga | Red lenta simulada | Si hay feedback o la interfaz se congela |
| Error | Enviar formulario inválido, cortar la red | Si el mensaje sirve o solo culpa |
| Éxito | Completar la tarea | Si el usuario sabe qué pasó y qué sigue |
| Contenido largo | Texto extenso, nombres largos, muchos ítems | Desbordes, cortes, tarjetas desalineadas |
| Contenido mínimo | Un ítem, un párrafo corto | Bloques vacíos, grillas rotas |
| Foco de teclado | `Tab` desde el inicio | Si el foco es visible y el orden es lógico |
| Hover / activo | Sobre controles | Si el feedback existe y es coherente |

Si un estado no se puede forzar, se anota como `No verificado`. Nunca se asume.

## Inventario objetivo

[`../scripts/ui_inventory.js`](../scripts/ui_inventory.js) se ejecuta sobre la página viva y
devuelve datos medidos, no impresiones. Formas de correrlo:

- **MCP de navegador**: pasar el contenido del archivo a la herramienta de ejecución de
  JavaScript de la página.
- **DevTools**: pegar el contenido en la consola. Devuelve un objeto; `copy(...)` lo lleva al
  portapapeles.
- **Playwright / Puppeteer**: `page.evaluate(fs.readFileSync('ui_inventory.js','utf8'))`.

Qué devuelve y para qué sirve cada bloque:

| Bloque | Señal de problema |
|---|---|
| `typography.sizes` | Más de 6–8 tamaños en una pantalla: no hay escala, hay acumulación |
| `typography.weights` / `families` | Más de 3 pesos o más de 2 familias sin razón declarada |
| `colors` | Paleta dispersa; el color de acción reutilizado en elementos que no son acciones |
| `spacing` | Muchos valores que no pertenecen a ninguna escala: el ritmo es accidental |
| `contrast.failures` | Texto por debajo de 4.5:1 (3:1 si es grande). Hecho, no opinión |
| `tapTargets.small` | Controles bajo 44 × 44 px en móvil |
| `headings.outline` | Saltos de nivel, varios `h1`, encabezados usados como estilo |
| `lineLength` | Párrafos sobre ~85 caracteres por línea o bajo ~40 |
| `rhythm.sections` | Alturas y densidades casi idénticas: la página es monótona |
| `interactive.unnamed` | Controles sin nombre accesible |

El inventario **no juzga**: entrega los hechos con los que se juzga. "Hay 14 tamaños de
fuente" es el dato; "no hay jerarquía tipográfica y tres elementos compiten por ser el
título" es el hallazgo.

## Medición manual cuando no hay navegador

Si solo tienes capturas, puedes seguir midiendo lo suficiente para no inventar:

- Contraste: extrae los colores de la captura y calcula la relación; repórtalo como
  aproximado.
- Jerarquía: aplica desenfoque o escala de grises a la captura y anota qué sobrevive.
- Ritmo: mide alturas de bloque sobre la captura completa y compáralas.
- Todo lo demás (estados, foco, responsive, feedback) se marca `No verificado`.

## Registro de evidencia

Guarda las capturas con nombres que se puedan citar en el informe:

```
<viewport>-<ruta>-<estado>.png     →  375-checkout-error.png
```

Colócalas en un directorio temporal de trabajo o, si el usuario quiere conservar el informe,
en `docs/ux-audit/<fecha>/`. Cada hallazgo cita el archivo o el elemento exacto
(`selector`, texto visible) del que salió.
