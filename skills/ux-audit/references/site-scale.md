# Auditoría a escala

Referencia de consulta de `ux-audit` para productos con muchas rutas o pantallas. Solo se abre
cuando el alcance excede lo que tiene sentido auditar recorrido por recorrido.

El problema que resuelve: **cuarenta pantallas auditadas una por una producen cuarenta informes
con los mismos ocho hallazgos.** Los problemas repetidos no viven en las páginas; viven en unas
pocas decisiones compartidas —navegación, layout, patrones de listado, formularios, manejo de
estados—.

```text
comprender las tareas principales
→ identificar arquetipos distintos
→ seleccionar representantes
→ auditar recorridos representativos
→ identificar lo repetido
→ rastrear el patrón compartido cuando sea útil
→ declarar cobertura
```

---

## Tareas antes que pantallas

Empieza por lo que la gente viene a hacer, no por el mapa del sitio. Tres o cuatro tareas
principales suelen explicar la mayor parte del uso, y una tarea atraviesa varias pantallas.

Una auditoría a escala que enumera secciones en vez de tareas termina describiendo el producto,
no evaluándolo.

Si las tareas principales no están claras y nadie puede nombrarlas, eso ya es un hallazgo — y
puede ser el más importante.

---

## Arquetipos

Se agrupan las pantallas por **cómo funcionan**, no por importancia. Dos pantallas importantes
con la misma estructura aportan los mismos hallazgos; una secundaria con estructura distinta
aporta hallazgos nuevos.

Arquetipos que suelen diferir de verdad:

| Arquetipo | Por qué es distinto |
|---|---|
| Lista o índice | Escaneo, densidad, acciones por fila, filtros |
| Detalle de registro | Jerarquía de datos, acciones destructivas, estado |
| Formulario largo | Agrupación, validación, recuperación |
| Flujo multipaso | Secuencia, contexto entre pasos, reversibilidad |
| Tabla densa | Comparación, qué ocurre al angostarse |
| Estado vacío o inicial | Si ofrece o solo explica |
| Overlay, modal o panel lateral | Salida, foco, pérdida de contexto |
| Error o sin permiso | Si la persona sabe qué hacer |

La tabla es un punto de partida, no una lista a cubrir. Un producto puede tener arquetipos
propios —un configurador, un calendario, un editor— y puede no tener varios de estos.

---

## Representantes

Se elige un representante por arquetipo relevante para las tareas principales, prefiriendo el
que más se usa o el que más variación de contenido soporta.

**No hay una cantidad obligatoria.** Ni cinco, ni ocho, ni una por sección. La cantidad la fija
la variedad real de arquetipos y el alcance acordado. Si dos arquetipos resultan ser el mismo en
la práctica, se dice y se audita uno.

Un representante se audita **completo**, con su recorrido, sus estados y su costo. Media docena
de auditorías superficiales valen menos que dos recorridos bien hechos.

---

## Local o sistémico

Cada hallazgo se clasifica al emitirlo:

```text
Local     → ocurre en esta pantalla por una decisión propia de esta pantalla
Sistémico → se repite porque una decisión compartida lo produce
```

La señal de que algo es sistémico es haberlo visto en más de un representante, o poder anticipar
dónde más aparecerá. Un hallazgo sistémico es **una** recomendación con su lista de lugares
donde verificarla, no una recomendación por pantalla.

Cuando el patrón no viene de un componente sino de una decisión repetida a mano, decirlo también
es útil: puede ser la señal de que falta un patrón compartido.

---

## Rastrear al patrón compartido

Cuando ayude —no siempre— se puede llegar del hallazgo al origen:

1. identificar el elemento en la interfaz;
2. localizarlo en el código (para ubicar, no para juzgar);
3. ver dónde más se usa;
4. contrastarlo con lo observado en los otros representantes.

`ux-audit` llega hasta aquí: **identifica** el patrón probable y su alcance. La consolidación o
el refactor corresponden a `component-architecture`, y los cambios funcionales a
`engineering-workflow`. No conviertas esto en una revisión de arquitectura del código.

Si no hay acceso al código, el rastreo se queda en la observación —"este mismo bloque aparece en
las tres pantallas revisadas"— y se marca como `Inferido`.

---

## Cobertura declarada

La salida dice explícitamente:

```text
qué tareas se recorrieron
qué arquetipos se auditaron y con qué representante
qué quedó fuera
qué hallazgos parecen sistémicos
qué hallazgos parecen locales
```

Declarar lo que quedó fuera no es una debilidad del informe: es lo que permite decidir si hace
falta otra pasada y sobre qué. Un informe que no declara cobertura se lee como si hubiera
revisado todo.

> **Cobertura no es calidad.** Revisar cuarenta pantallas con cinco minutos cada una produce
> menos valor que recorrer tres tareas completas. La auditoría se gana en el recorrido, no en el
> conteo.

---

## Automatización

Si el entorno ya ofrece control de navegador, capturas, extracción de estilos o recorrido de
rutas, úsalo cuando reduzca trabajo mecánico: localizar rutas, comprobar contrastes, medir
objetivos táctiles, registrar evidencia.

Pero:

- **no es prerrequisito**: la ausencia de herramientas no bloquea la auditoría;
- **no define el método**: un barrido automatizado no ve estructura, recorrido ni comprensión;
- **no se introduce infraestructura nueva** —dependencias, browser automation, scripts propios—
  para poder auditar;
- lo automatizado se reporta como lo que es: medición, no juicio.

Si el resultado son solo señales que una herramienta produce sola —contraste, tamaños táctiles,
saltos de encabezado— y ningún hallazgo de recorrido, no hubo auditoría: hubo barrido. Se rotula
así.
