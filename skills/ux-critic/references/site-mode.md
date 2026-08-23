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
distintas: no es lo mismo un registro planificado, uno en ejecución y uno cerrado. Elige los
ids con el usuario y anótalos.

Deja el resultado en un archivo de rutas, una por línea, para poder repetir el barrido
después de corregir.

### B · Barrido medido

```bash
npm i -D playwright && npx playwright install chromium
node <skill>/scripts/sweep.mjs --base http://localhost:3000 --routes rutas.txt --out .ux-sweep
python3 <skill>/scripts/compare_inventories.py .ux-sweep
```

Rutas autenticadas: crea el estado de sesión una vez y pásalo con `--storage`.

```bash
npx playwright open --save-storage=.ux-sweep/state.json http://localhost:3000
```

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
sitio), Fase 1 (captura y estados), Fase 2 (siete capas), Fase 3, Fase 4 y ficha por
hallazgo. Sin atajos: es aquí donde se gana la auditoría.

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

## Mapa de patrones
<salida de compare_inventories.py, editada a lo relevante>

## Sistema visual real
<qué existe de verdad vs. qué declara el design system, si lo hay>

## Críticas profundas
<una por pantalla de la muestra, formato normal, resumidas a sus hallazgos>

## Patrones transversales
<cada anti-patrón: componente que lo genera, rutas afectadas, corrección única>

## Plan de corrección por componente
<olas, tareas de sistema, criterio de aceptación, rutas de verificación>

## Guardarraíles
<R1–R8 como reglas del proyecto, con las excepciones nombradas que apliquen>

## Verificación
<bloque de verificación obligatorio: qué se midió, qué no, qué quedó en No verificado>
```

## Costo y cadencia

- El barrido es barato y repetible: **vuelve a correrlo al cerrar cada ola** y compara. Es la
  única forma de demostrar que la corrección funcionó y no solo movió el problema.
- La crítica profunda es cara: por eso son 5–8 pantallas y no 40.
- En un proyecto vivo, un barrido mensual detecta la deriva antes de que se vuelva rediseño.
