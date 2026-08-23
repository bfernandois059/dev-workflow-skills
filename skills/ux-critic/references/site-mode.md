# Site Mode

Modo sitio de `ux-critic`: cómo auditar un proyecto entero sin auditarlo pantalla por
pantalla.

## El problema del uno por uno

En un proyecto maduro, auditar 40 pantallas produce 40 informes con los mismos ocho
hallazgos. Los anti-patrones no viven en las páginas: viven en un puñado de **componentes
compartidos**. La misma tarjeta anidada, el mismo banner que se come el primer pantallazo y
el mismo input con relleno gris aparecen en veinte rutas porque se escribieron una vez.

Auditar de a una además es lento donde no hace falta: la mitad de lo que se mira —contraste,
escala tipográfica, anidamiento, objetivos táctiles— es **medible sin juicio**. Eso se barre
con un script sobre todas las rutas; el ojo se reserva para lo que ninguna herramienta ve.

## Las seis fases

### A · Inventario de rutas

Sacar la lista real de rutas del proyecto, no de la memoria de nadie:

| Stack | Dónde están |
|---|---|
| Next.js App Router | `app/**/page.tsx` |
| Next.js Pages Router | `pages/**/*.tsx` |
| React Router / Vue Router | definición de rutas en el código |
| Sitio publicado | `sitemap.xml`, o rastreo desde la home |

**Rutas dinámicas**: cada plantilla (`/servicios/[id]`) entra con **un id real por estado
relevante**. La misma plantilla en tres estados es, para efectos de crítica, tres pantallas
distintas: no es lo mismo un registro planificado, uno en ejecución y uno cerrado.

**Pídeselos al usuario explícitamente.** No basta con muestrear el primer enlace visible en un
listado: eso entrega el estado que la lista ordenó primero, casi nunca el interesante, y deja
las plantillas de detalle —donde vive el daño estructural— cubiertas por una sola pantalla.
Pregunta por id por estado, con una lista concreta:

```
Para las plantillas de detalle necesito un id real por estado. ¿Me das uno de cada?
  /servicios/[id]  → planificado · en ejecución · entregado · cerrado
  /terreno/[id]    → …
```

Si el usuario no puede darlos todos, **el barrido se declara parcial** y se listan las
plantillas y estados que quedaron sin cubrir, en el alcance y en el bloque de verificación.
Un detalle sin sus estados no está auditado: está visitado.

Deja el resultado en un archivo de rutas, una por línea, para poder repetir el barrido
después de corregir.

### B · Barrido medido

```bash
npm i -D playwright && npx playwright install chromium
node <skill>/scripts/sweep.mjs --base http://localhost:3000 --routes rutas.txt --out .ux-sweep
python3 <skill>/scripts/compare_inventories.py .ux-sweep
```

**Rutas autenticadas.** Playwright arranca un navegador limpio: sin sesión, todas las rutas
privadas devuelven el login y el barrido mide dieciséis veces la misma pantalla. El estado de
sesión se crea así:

```bash
npx playwright open --save-storage=.ux-sweep/state.json http://localhost:3000
```

**Ese comando exige que una persona inicie sesión a mano.** Un agente no puede generarlo solo
y **no debe intentar entrar por su cuenta**: nada de crear usuarios, adivinar credenciales ni
usar datos de prueba encontrados en el repositorio. Si las rutas están detrás de auth, pide al
usuario que corra ese comando y te pase la ruta del archivo. Es un paso de treinta segundos que
desbloquea todo el barrido.

**Fallback declarado.** Si no hay `storageState` pero sí un navegador ya autenticado que puedes
manejar, es una salida válida: recorres las rutas ahí y ejecutas
[`../scripts/ui_inventory.js`](../scripts/ui_inventory.js) en cada una, **guardando el JSON en
disco** con la misma forma que produce `sweep.mjs` para poder pasárselo al comparador. Lo que
**no** es válido es improvisar un inventario propio en silencio: si mediste con otra cosa, se
dice en el bloque de verificación, y las métricas que ese sustituto no produce van a
`No verificado`.

Si tuviste que adaptar el script para que corriera en tu entorno, **descarta las métricas que
la adaptación haya podido alterar** antes de usarlas, y declara la adaptación. Un inventario
que falla ruidosamente se arregla; uno que devuelve números degradados sin avisar contamina la
escala tipográfica, la jerarquía y el contraste a la vez.

## La evidencia va a disco, siempre

Una corrida de modo sitio es larga: veinte rutas, dos viewports, ocho críticas profundas. En
sesiones largas el contexto se compacta, y lo que solo vivía en memoria se pierde a mitad de
camino.

Escribe a medida que avanzas, en un directorio de trabajo propio —nunca dentro del producto
auditado—: un JSON de inventario por ruta y viewport, las capturas con su nombre citable, y
las notas por pantalla de la Fase D. **Solo lectura se refiere al producto auditado, no a tus
propias notas.** Un informe que no se guardó en ninguna parte es un informe que hay que volver
a producir entero si algo se corta.

Corre el barrido **dos veces**, en `1280x800` y en `375x812` (`--viewport`), a dos
directorios distintos. Casi todos los problemas de objetivos táctiles y ancho de línea solo
aparecen en el segundo.

El comparador entrega: métricas por ruta, señales agrupadas por patrón, el sistema visual
real del sitio (qué tamaños, pesos, familias y colores existen de verdad, y cuáles aparecen
en una sola ruta) y una propuesta de muestreo por arquetipo.

**Lo que el barrido NO hace**: no juzga propósito, jerarquía, ritmo ni copy. Mide lo medible
y señala dónde mirar. Confundir el mapa de calor con una auditoría es el mismo error que
confundir un `npm audit` con una revisión de seguridad.

### C · Muestreo por arquetipo

Se eligen **5 a 8 pantallas**, y el criterio no es la importancia: es la **diferencia**. Una
pantalla importante que es idéntica en composición a otra no aporta hallazgos nuevos.

Arquetipos que conviene cubrir:

| Arquetipo | Por qué es distinto |
|---|---|
| **Lista / índice** | Densidad, escaneo, acciones por fila |
| **Detalle de registro** | Jerarquía de datos, acciones destructivas, estado |
| **Formulario largo** | Agrupación, validación, affordance de campos |
| **Flujo multipaso** | Curva de esfuerzo, reversibilidad, progreso |
| **Estado vacío** | Si ofrece o solo explica (A7) |
| **Tabla densa** | Comportamiento al angostarse |
| **Overlay / modal** | Salida, foco, apilamiento |
| **Error o sin permiso** | Si el usuario sabe qué hacer |

Cruza la lista con el muestreo que propuso el comparador y con las rutas que más señales
acumularon. Declara en el informe **qué arquetipos quedaron sin cubrir**.

### D · Crítica profunda de la muestra

Sobre esas 5–8 pantallas, el flujo normal completo: Fase 0 (contexto, una vez para todo el
sitio), Fase 1 (captura y estados), Fase 2 (siete capas), Fase 3, Fase 4 y ficha por hallazgo.
Sin atajos: es aquí donde se gana la auditoría.

**Y se emite.** Cada pantalla de la muestra entrega su tabla de niveles por capa y sus fichas
de hallazgo completas. Colapsar el resultado en una tabla resumen de prioridades no es
resumir: es borrar la auditoría y dejar el barrido.

> **Regla de cierre del modo sitio.** Sin crítica profunda emitida de al menos un
> representante por arquetipo, el resultado **no es una auditoría de sitio: es un barrido**, y
> se rotula así desde el título del informe. Es una entrega legítima y útil —el mapa de calor
> vale por sí solo— pero no se presenta como lo que no es.

**Señal de que la Fase D no ocurrió**: los hallazgos del informe son exactamente los que el
comparador ya entrega solo —scroll horizontal, objetivos táctiles, contraste, saltos de
encabezado— y no aparece ningún anti-patrón `A1`–`A8`. El barrido no ve estructura, jerarquía,
ritmo ni copy. Si el informe tampoco los ve, no hubo ojo: hubo script.

### E · Del hallazgo al componente

Cada hallazgo se rastrea al componente que lo genera, y se cuenta en cuántas rutas aparece:

1. Localiza el componente en el código (ahora sí es útil leerlo: para ubicar, no para juzgar).
2. Busca sus usos en el repositorio.
3. Cruza esa lista con las rutas del barrido que mostraban la misma señal.

Un hallazgo con tres usos es **una** tarea de sistema y una lista de verificación de tres
pantallas. No tres tareas.

Cuando un anti-patrón no viene de un componente sino de una decisión repetida a mano, dilo:
esa es la señal de que falta el componente, y crear el componente es la corrección.

### F · Plan por componente y guardarraíles

El plan del modo sitio se ordena por **componente**, no por pantalla, usando el bloque de
tareas de sistema de la plantilla de plan de corrección. Cada tarea lleva la lista de rutas
donde se verifica.

Y se cierra con los **guardarraíles**: las reglas R1–R8 del catálogo de anti-patrones,
escritas como Definition of Done visual del proyecto, para que lo que se construya mientras
se corrige no vuelva a generar lo mismo. Sin esto, el plan es una carrera contra la
velocidad del equipo.

## Formato de salida del modo sitio

```markdown
# Auditoría de interfaz — <proyecto>

## Alcance del barrido
Rutas medidas: N · Viewports: … · Arquetipos cubiertos: … · Arquetipos sin cubrir: …
Plantillas dinámicas y estados cubiertos: … · Estados sin cubrir: …

## Mapa de calor del barrido
<salida de compare_inventories.py, editada a lo relevante — métricas por ruta y señales
medidas. Son hechos, no hallazgos.>

## Sistema visual real
<qué existe de verdad vs. qué declara el design system, si lo hay>

## Críticas profundas
<una por pantalla de la muestra, con su tabla de niveles por capa y sus fichas de hallazgo
completas. No se colapsan en una tabla de prioridades: eso borra la auditoría.>

## Mapa de patrones
<obligatorio. Por cada anti-patrón encontrado: componente que lo genera, rutas donde aparece,
corrección única. Es el entregable central del modo sitio — si esta sección está vacía, o no
hubo crítica profunda, o el sitio es excepcional y hay que poder explicar por qué.>

| Anti-patrón | Componente que lo genera | Rutas afectadas | Corrección |
|---|---|---|---|
| A1 · cajas anidadas | `<componente>` | `/a`, `/b`, `/c` | … |

## Decisiones que necesitas tomar
<obligatoria si alguna tarea depende de una definición de producto. Antes del plan.>

## Plan de corrección por componente
<olas, tareas de sistema, criterio de aceptación, rutas de verificación>

## Guardarraíles
<R1–R8 como reglas del proyecto, con las excepciones nombradas que apliquen>

## Verificación
<bloque de verificación obligatorio, más las filas propias del modo sitio:>

| Qué | Estado |
|---|---|
| Rutas medidas | N de M del inventario |
| Plantillas dinámicas | N plantillas · estados cubiertos / sin cubrir |
| Autenticación del barrido | storageState / navegador autenticado / sin acceso |
| Herramienta de inventario | `sweep.mjs` / sustituto declarado — cuál y qué métricas no produce |
| **Críticas profundas emitidas** | **N de N arquetipos** |
| Anti-patrones evaluados | A1–A8 · cuáles se buscaron y cuáles no aplican |
```

## Costo y cadencia

- El barrido es barato y repetible: **vuelve a correrlo al cerrar cada ola** y compara. Es la
  única forma de demostrar que la corrección funcionó y no solo movió el problema.
- La crítica profunda es cara: por eso son 5–8 pantallas y no 40.
- En un proyecto vivo, un barrido mensual detecta la deriva antes de que se vuelva rediseño.
