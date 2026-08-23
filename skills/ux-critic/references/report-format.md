# Report Format

Fase 5 de `ux-critic`. Estructura fija del informe, formato de ficha y reglas de redacción.

El informe se entrega en la conversación. Guárdalo además como archivo
(`docs/ux-audit/<fecha>-<alcance>.md`) solo si el usuario lo pide o si la auditoría es de un
sitio completo.

---

## Estructura

```markdown
# Crítica de interfaz — <alcance>

**Contexto usado**
Producto: … · Usuario: … · Tarea: … · Etapa: …
Exigencia: nivel N — <confirmado por el usuario | supuesto: con nivel N+1 cambiaría …>
Registro auditado: <id> · Estado en pantalla: <badge o etiqueta literal>
Capturas: <viewports y estados revisados>
Inventario objetivo: <corrido / no corrido y por qué>
Alcance real: <qué se auditó y qué quedó fuera>

## Veredicto
<Una frase. Honesta. Sin colchón.>

## Nivel por capa

| Capa | Nivel | En una línea |
|---|---|---|
| 1 · Propósito y promesa | Roto / Mediocre / Sólido / Referencia | … |
| 2 · Jerarquía | … | … |
| 3 · Ritmo y flujo | … | … |
| 4 · Contenido y copy | … | … |
| 5 · Interacción y estados | … | … |
| 6 · Sistema visual | … | … |
| 7 · Oficio y detalle | … | … |
| Accesibilidad (transversal) | … | … |
| Responsive (transversal) | … | … |

**Global:** <nivel> — <por qué ese y no el siguiente>

## Lo que sí funciona
<Máximo cinco. Cada uno con evidencia. Si hay menos de cinco reales, hay menos.>

## Hallazgos
<Fichas ordenadas por severidad: P0 → P3.>

## Preguntas incómodas
<3 a 5. Observación → hipótesis → qué cambia la respuesta.>

## Lo que replantearía de cero
<Obligatorio en pre-producción. 1 a 3 movimientos estructurales, como alternativa real.>

## Orden de ataque
<Secuencia numerada. Estructura antes que detalle.>

## Lo que no pude verificar
<Lista explícita. Y qué haría falta para verificarlo.>

## Refutación
<Qué se degradó de OK a hallazgo, qué hallazgo se retiró y por qué.>

## Decisiones que necesitas tomar
<Obligatoria si el plan tiene alguna. Preguntas redactadas como preguntas, con opciones y con
la tarea que cada una desbloquea. Va ANTES del plan porque lo bloquea.>

## Plan de corrección
<Tareas autocontenidas, agrupadas en olas. Ver plantilla.>

## Verificación
<Bloque obligatorio. Tabla completa más abajo en este documento.>
```

---

## Ficha de hallazgo

```
### [P1 · Jerarquía · Rediseño de bloque · Esfuerzo medio] Título del hallazgo en una línea

**Qué se ve** — SOLO evidencia visual: captura, elemento en pantalla, valor medido.
**Por qué falla** — para este usuario, en esta tarea. No en abstracto.
**Qué cuesta** — confusión / paso extra / error / abandono / desconfianza.
**Corrección** — concreta, con valores o texto propuesto.
**Certeza** — Hecho observado | Juicio del crítico | Supuesto por confirmar | Sin verificar en pantalla
```

La línea de encabezado lleva siempre los cuatro campos en ese orden:
`severidad · capa · nivel de intervención · esfuerzo`.

**El campo "Qué se ve" no admite evidencia de código.** Si el hallazgo salió de leer el
componente y no de mirar la pantalla, el campo se llama **"Qué encontré en el código"**, la
certeza es `Sin verificar en pantalla`, y el hallazgo **no puede ser `P0` ni encabezar el plan
de corrección** hasta confirmarse renderizado. Un componente puede existir en el árbol y no
renderizarse, renderizarse distinto, o no aplicar al estado del registro que el usuario tiene
delante.

**La certeza se declara por la fuente de ese dato concreto, no por la fuente dominante del
informe.** Un hallazgo puede verse en la captura y citar además un valor que salió de la base
de datos, del código o de una conversación previa: eso no es `Hecho observado en captura`. Si
un acordeón está cerrado en la imagen, su contenido no se vio; se sabe por otra vía y hay que
decirlo. Mezclar fuentes sin declararlo es lo que convierte un informe correcto en uno que no
se puede auditar.

**Toda cifra declara su origen**: del inventario objetivo, de una captura (indicando su alto
total), o de un conteo. Un porcentaje de viewport sobre una captura de página completa no
tiene origen posible — ahí no hay viewport que medir.

**En hallazgos de estructura y superficie** —los del catálogo
[`container-antipatterns.md`](container-antipatterns.md)— la corrección **debe incluir el
árbol antes/después**. Sin el árbol, "simplificar la jerarquía de contenedores" vuelve a ser
una recomendación tibia; el árbol es la instrucción:

```
❌ Antes                                  ✅ Después
Panel "Documentos técnicos"               "Obligatorios" (título de sección, sin caja)
  Tarjeta "Documentos … obligatorios"       Kick Off y OT antes de finalizar.
    Tabla                                   ── una superficie, dos filas ──
      Fila con fondo propio ×2
  Pie "Documentación lista para finalizar"  (estado, una sola vez, junto a Finalizar)
```

### Ejemplo correcto

```
### [P1 · Jerarquía · Ajuste · Esfuerzo bajo] El precio pierde contra el badge de descuento

**Qué se ve** — En la tarjeta de producto, el badge "-30%" está en 20 px / peso 700 sobre
rojo, y el precio final en 16 px / peso 400 en gris #767676. Captura: 375-catalogo.png.
**Por qué falla** — La tarea es comparar productos y decidir. El dato que decide es el precio
final; el que domina la tarjeta es el descuento, que solo tiene sentido después de haber
leído el precio.
**Qué cuesta** — El usuario compara descuentos en vez de precios y vuelve atrás al descubrir
el precio real en la ficha. Paso extra y desconfianza.
**Corrección** — Precio final a 20 px / peso 600 en el color de texto principal; badge a
12 px / peso 600 y contenido dentro del flujo de la tarjeta, no encima de la imagen.
**Certeza** — Hecho observado (valores medidos).
```

### Ejemplo incorrecto

```
Se recomienda revisar la jerarquía visual de las tarjetas de producto, ya que actualmente
podría no ser del todo clara para el usuario. Considerar destacar mejor el precio.
```

Sin evidencia, sin costo, sin valores, sin certeza, y en condicional. No es un hallazgo: es
una sensación con formato de informe.

---

## Niveles

**Por capa y global:**

| Nivel | Qué significa |
|---|---|
| **Roto** | No cumple su función. Un usuario real falla, se confunde o se va |
| **Funciona pero mediocre** | Cumple, se nota que nadie decidió. Se sostiene por inercia |
| **Sólido** | Decidido, consistente, sin fricciones relevantes. No sorprende |
| **Referencia** | Se puede mostrar como ejemplo. Cada decisión tiene intención |
| **No verificado** | No se pudo observar o medir. **No es aprobación**: es una casilla vacía |

`No verificado` se aplica a lo que de verdad exigió interacción o medición. Lo que una captura
estática sí muestra —composición, jerarquía, copy, datos duplicados, el estado por defecto de
un colapsable, el peso de las acciones— se juzga normalmente. Barrer capas enteras a
`No verificado` porque la fuente fue estática es el error inverso a aprobar sin medir: deja
hallazgos reales sin reportar. Ver la tabla de la Fase 1 en `SKILL.md`.

Sin puntajes numéricos. Un "72/100" en una crítica de interfaz es precisión falsa: sugiere
una medición que no existe.

Una capa o transversal solo puede declararse `Sólido` o `Referencia` si hay una medición o una
observación concreta detrás. "Contraste correcto" sin ratio medido, o "responsive sólido" sin
haber renderizado a 375 px, van a `No verificado` — que un framework sea responsive no es
evidencia de comportamiento. La Fase 4 recorre estas casillas una por una.

---

## Reglas de redacción

- **Duro con el trabajo, respetuoso con la persona.** Nunca "quien hizo esto no pensó";
  siempre "esta decisión cuesta X".
- **Toda crítica trae propuesta.** Sin propuesta es opinión.
- **Específico o no se dice.** Valores, textos, selectores, capturas.
- **Nada de lenguaje de colchón**: *podría considerarse*, *tal vez sería recomendable*, *en
  general está bien pero*, *no está mal del todo*, *se sugiere evaluar*.
- **Nada de sándwich de elogios.** Lo bueno tiene su sección.
- **Nada de jerga vacía**: *sinergia visual*, *storytelling de marca*, *experiencia
  inmersiva*.
- **Nada de números inventados.** Ni conversión, ni segundos, ni porcentajes de mejora.
- **Separa hecho de juicio** con la línea de certeza. El usuario puede discutir los juicios;
  los hechos no se discuten, se corrigen.
- **El veredicto va primero.** Nadie debería tener que leer treinta hallazgos para saber si
  la pantalla está bien o mal.

---

## Decisiones que necesitas tomar

Sección obligatoria cuando alguna tarea depende de una definición de producto o de negocio.
Va **antes** del plan, porque lo bloquea.

```markdown
## Decisiones que necesitas tomar

| # | Pregunta | Bloquea | Opciones |
|---|---|---|---|
| D1 | ¿Cuál es la acción primaria de un ticket `Planificado` para Jefatura? | UX-03 | A: hay una acción vigente — ¿cuál? · B: Jefatura no actúa aquí y la pantalla debe decirlo |
| D2 | Una visita de varios días, ¿se agrupa por fecha de inicio o por rango? | UX-02 | A: por inicio · B: por rango con barra de duración |
```

Reglas:

1. **Redactadas como preguntas.** Un diagnóstico en tercera persona —"nadie definió qué cuatro
   datos importan en móvil"— se lee y se sigue de largo. Una pregunta directa se contesta.
2. **Con opciones concretas.** El usuario tiene que poder responder con una letra, no redactar
   una especificación.
3. **Con la tarea que desbloquean**, para que se vea el costo de no decidir.
4. **Una tarea cuyo `Depende de` sea una decisión de producto no arranca.** La decisión sube a
   esta tabla y la tarea se marca `Bloqueada por D<n>`. Dejar la decisión enterrada en una fila
   de metadatos de la ficha es disfrazarla de tarea, y el usuario nunca la ve.
5. **No se confunde con las preguntas incómodas.** Aquellas cuestionan una decisión ya tomada
   —"¿por qué está así?"— y son parte del diagnóstico. Estas piden una decisión que todavía no
   existe y sin la cual nadie puede ejecutar.

---

## Bloque de verificación

Cierra todo informe. Es el mecanismo que impide aprobar lo que no se miró: una regla que pide
"haz una pasada" se omite, una tabla que hay que rellenar no.

```markdown
## Verificación

| Qué | Estado |
|---|---|
| Fuente de evidencia | captura propia / captura del usuario / ambas |
| Viewports observados | 1280×800, 375×812 … |
| Estados abiertos | vacío, error, carga, éxito … (y cuáles no) |
| Inventario objetivo | corrido / no corrido — por qué |
| Cifras del informe | N cifras, todas con origen declarado |
| Capas forzadas a `No verificado` | … |
| Datos citados que NO salen de la captura | … (código, base de datos, conversación previa) |

La última fila es para datos traídos de **otra fuente**: el código, la base de datos, una
conversación anterior, la documentación del proyecto. Lo que salió del inventario ejecutado
sobre la página viva —contraste, dimensiones, conteos— **sí es evidencia de la interfaz**: va
en `Inventario objetivo`, no ahí.
```

Reglas:

- Si una fila no se puede completar con honestidad, el informe **no está listo**.
- La fila de capas forzadas debe coincidir con la tabla de niveles. Si la tabla dice
  `Responsive: Sólido` y aquí dice que solo hubo una captura desktop, hay una contradicción
  que el lector va a encontrar.
- En modo sitio, se añaden dos filas: rutas medidas y arquetipos sin cubrir.

---

## Plan de corrección

Última sección del informe y **entregable en sí mismo**: la lista de tareas con la que se
arregla lo encontrado, sin tener que releer el informe. Plantilla completa en
[`../assets/templates/fix-plan.template.md`](../assets/templates/fix-plan.template.md).

Reglas:

1. **Una tarea es autocontenida y se emite con ficha.** Se puede tomar suelta, pasar a
   `engineering-workflow` o entregar a otro agente sin el resto del informe.

   ```
   ### UX-01 · <título imperativo, una línea>
   Capa · Severidad · Intervención · Esfuerzo · Riesgo · Depende de

   Dónde        → componente o archivo. Sin acceso al repositorio: el bloque de la interfaz
                   identificado sin ambigüedad (título visible + posición) y marcado como
                   "falta localizar el componente".
   Qué cambia   → los cambios concretos, uno por línea.
   Criterio     → casillas verificables mirando la pantalla. Una por resultado.
   Fuera de     → lo que esta tarea NO toca, para que no crezca.
   ```

   En hallazgos de estructura, la ficha incluye además el árbol antes/después.

2. **Sin `Dónde` y sin criterio verificable no es una tarea, es un deseo.** "Ninguna superficie
   anidada a más de dos niveles en la pestaña" se puede marcar hecho o no hecho mirando la
   pantalla; "mejorar la jerarquía" no. Una tarea que no llegue a esa forma se queda como
   hallazgo, no se disfraza de plan.
3. **Agrupadas en olas, no en una lista plana**: estructura → jerarquía y acciones →
   contenido y estados → detalle. No se empieza una ola sin cerrar la anterior, porque pulir
   antes de reestructurar es trabajo que se tira.
4. **Un anti-patrón repetido es una sola tarea de sistema**, con la lista de pantallas donde
   se verifica. Seis tareas de pantalla para el mismo problema es la forma de garantizar que
   quede a medias.
5. **Riesgo declarado.** Marca qué tareas son solo presentación y cuáles tocan comportamiento
   o datos: define si pueden ir por la ruta rápida de `engineering-workflow` o exigen el flujo
   completo.
6. **Lo que no es tarea, es decisión.** Lo que requiere una definición de producto o negocio
   va en una tabla aparte de decisiones pendientes, indicando qué tarea bloquea. No se
   disfraza de tarea.
7. **El criterio de aceptación vive en su tarea, nunca agrupado al final.** Una lista global de
   "cómo validar" al cierre del plan no sirve: quien tome `UX-03` suelta no puede saber cuál de
   esas casillas le toca. Cada tarea lleva las suyas.
8. **Verificación final incluida**: repetir el inventario objetivo y el recorrido limpio sobre
   la interfaz corregida, y comparar capturas antes/después. Eso es *además* de los criterios
   por tarea, no en su lugar.

---

## Longitud

Proporcional al alcance, no al esfuerzo invertido:

| Alcance | Extensión razonable |
|---|---|
| Bloque | Veredicto + 3 a 6 hallazgos |
| Pantalla | Informe completo, 8 a 15 hallazgos |
| Flujo | Informe completo + mapa del recorrido paso a paso |
| Sitio | Informe por pantalla clave + una sección de patrones transversales que se repiten |

En un sitio completo, el hallazgo transversal vale más que el mismo hallazgo repetido en seis
pantallas: repórtalo una vez, lista dónde aparece.
