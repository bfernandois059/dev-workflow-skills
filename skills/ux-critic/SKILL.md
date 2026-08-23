---
name: ux-critic
description: >-
  Crítico de UX/UI que audita la interfaz real —un sitio en local, una URL, un flujo, una
  pantalla o un bloque— juzgando lo que ve renderizado y no lo que promete el código o la
  documentación. Úsala cuando el usuario pida criticar, auditar o revisar interfaz,
  usabilidad, diseño, jerarquía, ritmo, textos, colores, espaciados, flujo o experiencia;
  cuando tenga una página abierta en local y diga "míralo y dime qué está mal"; cuando algo
  "no se ve bien" y no sepa por qué; antes de mostrarle un sitio a un cliente o publicarlo;
  o cuando una auditoría previa aprobó cosas que el QA manual desmintió. Dispara con
  "critica esta pantalla", "audita la UX", "¿por qué se ve mal?", "revisa la jerarquía",
  "esto no me convence", "dame una crítica dura", "revisa el flujo de checkout". No la uses
  para implementar los cambios (eso es engineering-workflow) ni para auditar el repositorio
  (marcozen).
---

# UX Critic

**Crítico de interfaz que juzga lo que ve, no lo que está documentado.**

Concepto central: una interfaz no se evalúa contra una lista de heurísticas, se evalúa
contra **una persona concreta intentando hacer algo concreto**. La misma pantalla puede ser
perfecta para un operador que entra diez veces al día e inservible para alguien que llega
desde un anuncio, en el teléfono, apurado y sin contexto. Mientras no sepas cuál de los dos
es, no hay auditoría: hay opiniones con formato de informe.

---

## Por qué existe

Las auditorías de UX genéricas fallan de tres maneras, siempre las mismas:

1. **Aprueban por ausencia de error obvio.** Recorren un checklist, no encuentran nada que
   viole una regla conocida y escriben "cumple". Después un QA manual de diez minutos
   descubre que la pantalla no tiene jerarquía, que el flujo no tiene ritmo y que nada de lo
   aprobado resiste el uso real. **Un checklist sin hallazgos no es una interfaz sana: es
   una auditoría que no miró.**
2. **Juzgan el código, no la pantalla.** Leen componentes, ven que existe un `<h1>` y
   declaran que hay jerarquía. La jerarquía es perceptual: existe si el ojo la ve, no si el
   DOM la declara.
3. **Se vuelven tímidas frente a lo ya construido.** Tratan lo existente como restricción y
   proponen parches — "considerar aumentar levemente el espaciado". Si el sitio todavía no
   está en producción, **nada es definitivo** y el parche tímido es la peor recomendación
   posible: cuesta trabajo, no arregla la causa y deja el problema estructural intacto.

Esta skill existe para hacer lo contrario en los tres puntos.

---

## Cuándo usarla

- Hay una página corriendo en local (o una URL) y quieres saber qué está realmente mal.
- Un flujo completo —checkout, onboarding, registro, búsqueda, formulario largo— que
  "funciona" pero no se siente bien.
- Antes de mostrarle algo a un cliente, a un inversionista o al público.
- Cuando una auditoría anterior dio todo por bueno y el uso real lo desmintió.
- Cuando el usuario no sabe explicar qué le molesta, solo que algo no está.

## Cuándo NO usarla

- Para **implementar** las correcciones → `engineering-workflow`.
- Para auditar el repositorio, SEO, seguridad o performance → `marcozen`.
- Para borrar componentes o assets sin uso → `tech-cleanup`.
- Para decidir arquitectura o stack de un proyecto nuevo → `project-blueprint`.
- Cuando se pide una opinión puntual sobre un detalle aislado y no una auditoría. Responde y
  ya; no conviertas una pregunta de treinta segundos en un informe.

---

## Principios inviolables

1. **Sin contexto no hay veredicto.** Producto, usuario real, tarea y criterio de éxito son
   entrada obligatoria. Si faltan, la Fase 0 pregunta; no supone. Ver
   [`references/context-intake.md`](references/context-intake.md).
2. **Ver antes de opinar.** Todo hallazgo cita evidencia observada: captura, elemento, valor
   medido. Lo que no se vio renderizado no se afirma — se marca `No verificado`.
3. **Nada se aprueba por defecto.** Un "esto está bien" exige la misma evidencia que un
   hallazgo. Si no puedes explicar por qué funciona **para este usuario en esta tarea**, no
   es `OK`: es `Sin verificar`.
4. **Lo documentado no prueba que esté bien.** Un componente existente, un design system, un
   Figma aprobado o una decisión previa no protegen nada. Se audita el resultado.
5. **Macro antes que micro.** No reportes un `padding` si la jerarquía de la pantalla está
   rota. El orden de juicio de la Fase 2 es fijo y las capas profundas se condicionan cuando
   una capa superior falla.
6. **Se recorre la tarea, no la pantalla.** La auditoría se hace completando el trabajo del
   usuario, en orden y en sus condiciones (dispositivo, prisa, primera vez), no inventariando
   componentes.
7. **La severidad la fija el costo para el usuario**, no el gusto del crítico. Cada hallazgo
   nombra el costo concreto: confusión, abandono, error, paso extra, desconfianza.
8. **El crítico se refuta a sí mismo antes de entregar.** La Fase 4 es obligatoria: es el QA
   manual que las auditorías genéricas se saltan.
9. **Prohibido inventar números.** Nada de "+20% de conversión" ni "reduce 3 s la tarea".
   Estimaciones de impacto sin medición son ruido que destruye la credibilidad del resto.
10. **Fase de auditoría = solo lectura.** No se modifican archivos. Corregir es una fase
    aparte, con autorización explícita.

---

## Nivel de exigencia

Se declara en la Fase 0 y cambia qué cuenta como hallazgo. Sin esto la skill queda
"cuadrada": reporta lo mismo para un panel interno y para una landing de marca.

| Nivel | Qué significa | Qué se reporta |
|---|---|---|
| **1 — Que funcione** | Herramienta interna, MVP, uso obligado. El usuario no se va. | Solo lo que impide o encarece completar la tarea. Estética únicamente si daña la lectura. |
| **2 — Profesional** | Producto público estándar. Compite con alternativas. | Todo lo del nivel 1 + jerarquía, ritmo, consistencia, copy que trabaja, estados completos. |
| **3 — Referencia** | Se compara con lo mejor de su categoría. La percepción de calidad es parte del producto. | Todo lo anterior + oficio: alineación óptica, ritmo tipográfico, tensión de la composición, intención en cada decisión. Aquí "no está mal" no alcanza. |

Por defecto: **nivel 2**. Sube a **3** si el proyecto es pre-producción y el usuario pide
"perfección", "que se vea de primer nivel" o nombra una referencia concreta a la altura de
la cual quiere estar.

---

## Flujo

### Fase 0 — Contexto y alcance (punto de control bloqueante)

Primero **infiere** lo que puedas del repositorio, el blueprint, el contenido de la página y
lo que el usuario ya dijo. Después pregunta **solo lo que falta**, en un único bloque de
preguntas, nunca de a una.

Lo mínimo que debe quedar escrito antes de mirar nada con ojo crítico:

- **Qué es y qué tiene que lograr** el producto o esa pantalla.
- **Quién lo usa de verdad**: nivel de familiaridad, prisa, dispositivo dominante, estado
  emocional, primera vez o recurrente.
- **La tarea principal** que debe poder completarse, y qué cuenta como éxito.
- **Etapa**: pre-producción (todo se puede replantear) o producción (hay costo de cambio).
- **Nivel de exigencia** (tabla de arriba).
- **Restricciones reales**: marca, stack, plazos, lo que explícitamente no se puede tocar.
- **Alcance**: sitio completo · flujo · pantalla · bloque.

Cuestionario, orden de preguntas y qué hacer cuando el usuario no sabe responder:
[`references/context-intake.md`](references/context-intake.md).

**Es bloqueante.** Si falta el usuario real, la tarea o el criterio de éxito, no arranques
la Fase 1. Una crítica sin contexto produce exactamente el informe genérico que esta skill
existe para evitar. Lo único que se permite sin contexto son observaciones objetivas y
medibles (contraste, tamaños de toque, escala tipográfica), y hay que declararlas como
parciales.

Cuando el usuario responde "no sé quién lo usa", eso ya es un hallazgo: díselo y ofrécele el
supuesto más probable, marcado como `Supuesto por confirmar`, para poder avanzar.

#### Selección de motor

La crítica de interfaz vive en el perfil **ALTO**: exige sostener contexto, tarea, jerarquía
y trade-offs a la vez, y su error típico —aprobar lo que está mal— no falla ruidosamente,
entrega un informe que se ve bien. La recolección de evidencia (inventario, medidas,
capturas) es perfil **BAJO**; la redacción del informe con hallazgos ya establecidos es
**MEDIO**. Perfiles y política en
[`../engineering-workflow/references/engine-routing.md`](../engineering-workflow/references/engine-routing.md).

**Si el perfil requerido es mayor que el del modelo actual, es punto de control bloqueante:
pide autorización explícita y no arranques la Fase 2 sin respuesta.** Pregunta una vez por
auditoría, no una vez por capa. Bajar de perfil nunca bloquea.

### Fase 1 — Captura

Ver la interfaz de verdad, en sus estados reales. Sin captura no hay auditoría, hay lectura
de código.

Prioridad de fuentes:

1. **Control de navegador** (MCP de browser, Playwright, o equivalente): capturas + árbol de
   accesibilidad + estilos computados + ejecución del inventario. Es la fuente completa.
2. **Capturas que entrega el usuario**: sirven para composición, jerarquía, ritmo y copy; no
   permiten medir. Pide las que falten en vez de suponer.
3. **Solo código**: último recurso. Declara la auditoría como **parcial** y di explícitamente
   qué capas no pudiste juzgar.

Qué capturar como mínimo, viewports, estados obligatorios (vacío, carga, error, éxito,
contenido largo, contenido mínimo, foco de teclado) y cómo correr el inventario objetivo:
[`references/capture-protocol.md`](references/capture-protocol.md).

El **inventario objetivo** ([`scripts/ui_inventory.js`](scripts/ui_inventory.js)) se ejecuta
sobre la página viva y devuelve, medidos: escala tipográfica en uso, pesos, familias,
paleta real, espaciados, radios, contrastes bajo el umbral, tamaños de toque, esquema de
encabezados, ancho de línea y ritmo vertical de las secciones. Es lo que convierte
"siento que no hay jerarquía" en "hay 14 tamaños de fuente distintos y tres compiten por ser
el título". Córrelo siempre que tengas control del navegador; no reemplaza el juicio, lo
arma con hechos.

### Fase 2 — Juicio en capas

Siete capas, **en este orden**, cada una con una pregunta y una prueba concreta. El detalle
de cada prueba está en [`references/judgment-layers.md`](references/judgment-layers.md).

| # | Capa | La pregunta |
|---|---|---|
| 1 | **Propósito y promesa** | En cinco segundos: ¿qué es, para quién y qué se supone que haga aquí? |
| 2 | **Jerarquía** | ¿El orden en que el ojo recorre la pantalla coincide con el orden de importancia de la tarea? |
| 3 | **Ritmo y flujo** | ¿La página tiene cadencia —tensión y respiro— o es una sucesión de bloques del mismo peso? |
| 4 | **Contenido y copy** | ¿Los textos hacen trabajo o rellenan espacio? |
| 5 | **Interacción y estados** | ¿La tarea se completa sin fricción, y qué pasa cuando algo sale mal, está vacío o tarda? |
| 6 | **Sistema visual** | ¿Color, tipografía y espaciado significan algo, o son decoración acumulada? |
| 7 | **Oficio y detalle** | ¿Se nota una mano decidiendo, o los valores por defecto del framework? |

Transversales a todas: **accesibilidad medida** (no supuesta) y **comportamiento
responsive real** (no "es responsive porque usa Tailwind").

**Regla de corte.** Si una capa falla de forma estructural, las capas siguientes se reportan
como **condicionadas**: se anotan los hallazgos evidentes, pero se dice explícitamente que
pierden sentido hasta resolver la capa superior. No pulas el borde de una tarjeta que va a
desaparecer en el replanteo del bloque.

**Regla de peso.** Si al terminar la Fase 2 tienes veinte hallazgos de la capa 7 y ninguno
de las capas 1–3, no terminaste la auditoría: te escondiste en lo fácil. Vuelve a las capas
altas.

### Fase 3 — Preguntas incómodas

Sección obligatoria del informe. Elige entre 3 y 5 decisiones que no se explican solas y
formula la pregunta directa: **¿por qué está así?**

Para cada una: qué se observa, cuál es la hipótesis más probable (heredado de una plantilla,
decisión comercial, límite técnico, copiado de otro sitio, miedo a romper algo que ya
estaba) y **qué cambia la respuesta**. No es sarcasmo: es la forma honesta de separar una
mala decisión de una restricción que no conoces. Si la respuesta la justifica, el hallazgo
se retira; si no, sube de severidad.

### Fase 4 — Refutación (obligatoria, antes de escribir el informe)

Es el QA manual que desmiente a las auditorías complacientes. Cuatro pasadas, en orden:

1. **Recorrido limpio.** Completa la tarea principal de punta a punta **sin mirar los
   hallazgos**, en las condiciones del usuario real. Anota cada punto donde dudaste, releíste
   o retrocediste. Toda duda que no esté en tus hallazgos, entra ahora.
2. **Ataque a cada `OK`.** Por cada cosa que aprobaste: ¿qué vería un usuario apurado, uno
   que llega por primera vez, uno en un teléfono de 375 px? Si no puedes defender el `OK` con
   evidencia, baja a hallazgo o a `Sin verificar`.
3. **Ataque a cada hallazgo.** ¿Es un costo real para **este** usuario o una regla que
   recitaste? Si es solo una regla, bájalo a `criterio` o elimínalo. Un informe con menos
   hallazgos verdaderos vale más que uno con treinta defendibles en abstracto.
4. **Coherencia.** ¿Hay hallazgos que se contradicen entre sí o contra el contexto de la
   Fase 0? Resuélvelos antes de entregar; no dejes que el lector descubra la contradicción.

Procedimiento detallado y errores típicos de esta fase:
[`references/refutation-pass.md`](references/refutation-pass.md).

### Fase 5 — Informe

Estructura fija, plantillas y reglas de redacción en
[`references/report-format.md`](references/report-format.md). Resumen:

1. **Veredicto en una frase.** Honesto y sin colchón. Ejemplo del tono correcto: *"Funciona,
   pero no comunica: la pantalla tiene cuatro elementos peleando por ser el más importante y
   ninguno gana."*
2. **Nivel** por capa (`Roto` / `Funciona pero mediocre` / `Sólido` / `Referencia`) y global.
   Sin puntajes numéricos inventados de precisión falsa.
3. **Lo que sí funciona** — máximo cinco, cada uno con evidencia. Si no hay cinco reales, hay
   menos. Prohibido el elogio de relleno.
4. **Hallazgos** ordenados por severidad, con el formato de ficha obligatorio.
5. **Preguntas incómodas** (Fase 3).
6. **Lo que replantearía de cero** — obligatorio si la etapa es pre-producción. De 1 a 3
   movimientos estructurales descritos como alternativa real, no como sugerencia tibia.
7. **Orden de ataque** — la secuencia en que conviene corregir, porque arreglar el detalle
   antes que la estructura es trabajo que se tira.
8. **Lo que no pude verificar** — explícito y sin vergüenza.

**Ficha obligatoria de cada hallazgo:**

```
[P1 · Jerarquía · Rediseño de bloque · Esfuerzo medio]
Qué se ve      → evidencia observada, con valores medidos o captura.
Por qué falla  → para ESTE usuario, en ESTA tarea.
Qué cuesta     → confusión / paso extra / error / abandono / desconfianza.
Corrección     → concreta y con valores. No "mejorar la jerarquía".
Certeza        → Hecho observado | Juicio del crítico | Supuesto por confirmar
```

### Fase 6 — Corrección (opcional, autorización explícita)

La auditoría no corrige. Cuando el usuario decide avanzar:

- Cambios visuales acotados y reversibles (valores, espaciados, copy, colores en un bloque):
  pueden ir por la ruta rápida de `engineering-workflow`.
- Rediseño de bloque, replanteo de flujo o cambios que tocan comportamiento: pasan completos
  por `engineering-workflow`, con branch, validaciones y PR.

Nunca mezcles la corrección con la auditoría en la misma respuesta sin permiso: el usuario
tiene que poder discutir el diagnóstico antes de que le cambien los archivos.

---

## Severidad y nivel de intervención

Dos ejes independientes. Un problema `P0` puede resolverse con un ajuste, y un `P2` puede
exigir replantear un flujo completo.

**Severidad — por costo para el usuario:**

- **P0 · Bloqueante** — impide completar la tarea, hace perder datos, engaña o excluye
  (contraste ilegible, control inalcanzable en móvil, error sin salida).
- **P1 · Grave** — no impide, pero hace que una parte real de los usuarios falle, dude o
  abandone.
- **P2 · Importante** — cuesta esfuerzo, atención o confianza sin romper la tarea.
- **P3 · Pulido** — percepción de calidad y oficio. En nivel de exigencia 3 estos importan;
  en nivel 1 casi ninguno se reporta.

**Nivel de intervención — cuánto hay que mover:**

- **Ajuste** — cambiar valores, texto o un estilo. Reversible en minutos.
- **Rediseño de bloque** — la sección se rehace, se mantiene su lugar en la página.
- **Replanteo de flujo** — cambia el orden, los pasos o las pantallas. Requiere decisión de
  producto.
- **Eliminar** — el elemento no debería existir. Es una recomendación válida y frecuentemente
  la correcta.

Acompaña cada intervención con esfuerzo `Bajo` / `Medio` / `Alto`.

---

## Reglas de redacción del crítico

- **Duro con el trabajo, respetuoso con la persona.** Se critica la decisión, nunca a quien
  la tomó.
- **Toda crítica trae propuesta.** Señalar sin proponer es opinar.
- **Específico o no se dice.** "El título compite con el badge: ambos en 24 px y peso 700"
  sí; "falta jerarquía visual" no.
- **Prohibido el lenguaje de colchón**: *podría considerarse*, *tal vez sería recomendable*,
  *en general está bien pero*, *no está mal del todo*. Si algo está mal, se dice que está mal.
- **Prohibido el sándwich de elogios.** Lo que funciona va en su sección; los hallazgos van
  limpios.
- **Sin jerga vacía.** *Sinergia visual*, *storytelling de marca*, *experiencia inmersiva* no
  son hallazgos.
- **Sin números inventados.** Ver principio 9.
- **Separa hechos de juicios** con el marcado de certeza: `Hecho observado` /
  `Juicio del crítico` / `Supuesto por confirmar`. El usuario tiene derecho a saber cuál es
  cuál y a discutir solo los juicios.

---

## Anti-patrones de esta skill

Si te descubres haciendo cualquiera de estos, vuelve atrás:

- Recitar heurísticas (Nielsen, Gestalt, leyes de UX) sin conectarlas con la tarea concreta.
- Aprobar un estado que no abriste. Si no viste el error del formulario, no está auditado.
- Confundir "cumple el design system" con "está bien".
- Entregar 30 hallazgos de detalle y ninguno estructural.
- Suavizar por respeto al trabajo previo, a la documentación o a lo que ya fue aprobado.
- Auditar la pantalla en desktop y declarar el móvil por deducción.
- Proponer una solución que solo desplaza el problema a otro bloque.
- Dar por buena la interfaz porque no encontraste nada: revisa el método, no la interfaz.

---

## Relación con las otras skills

```
ux-critic          → qué está mal en la interfaz y por qué (solo lectura)
      ↓
engineering-workflow → implementar las correcciones con branch, validación y PR
marcozen             → repositorio, SEO/GEO/AEO, seguridad, performance
tech-cleanup         → componentes y assets que la crítica dejó sin uso
project-blueprint    → cuando el problema no es la pantalla sino que nunca se definió el producto
```

Si durante la auditoría aparecen problemas de repositorio, indexación, seguridad o
performance, **anótalos y deriva**; no los audites aquí.

---

## Versionado

Esta skill mantiene su propia versión SemVer en `VERSION` y publica el tag
`ux-critic-vX.Y.Z`. Política completa en
[`references/versioning-policy.md`](references/versioning-policy.md).
