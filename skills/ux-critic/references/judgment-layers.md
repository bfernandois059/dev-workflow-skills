# Judgment Layers

Fase 2 de `ux-critic`. Siete capas en orden fijo. Cada capa trae **pruebas concretas** —cosas
que se hacen, no criterios que se recitan— y las señales de falla que hay que buscar.

Reglas transversales:

- Se juzga contra el contexto de la Fase 0. Una misma observación puede ser un `P0` en una
  landing pública y no ser hallazgo en un panel interno.
- Cada prueba produce **evidencia citable**: una captura, un valor medido, una frase de la
  página.
- **Regla de corte**: si una capa falla estructuralmente, las siguientes se reportan como
  `condicionadas`.
- Los anti-patrones de **estructura y superficie** —cajas anidadas, títulos en eco, contenido
  duplicado, todo-es-una-tarjeta, acciones sin jerarquía, inputs que parecen deshabilitados,
  bloques vacíos que solo se explican, primer pantallazo secuestrado— tienen catálogo propio
  con la corrección prescrita en
  [`container-antipatterns.md`](container-antipatterns.md). Se detectan en las capas 1, 2, 4,
  5 y 6, y se reportan **con el árbol de estructura antes/después**.

---

## Capa 1 — Propósito y promesa

> En cinco segundos: ¿qué es, para quién, y qué se supone que haga aquí?

**Pruebas**

1. **Cinco segundos.** Mira el primer pantallazo una vez. Cierra la captura. Escribe de
   memoria qué es el producto, para quién y cuál es la acción propuesta. Lo que no pudiste
   escribir es lo que el usuario tampoco captó.
2. **Logo intercambiable.** Cambia mentalmente el logo por el de un competidor. Si el
   encabezado sigue teniendo sentido, no dice nada: es una plantilla con tu nombre encima.
3. **El extraño.** Alguien que llegó desde un anuncio, sin contexto: ¿sabe qué pasa si hace
   clic en la acción principal? ¿Sabe cuánto cuesta, cuánto tarda, qué recibe?
4. **Acción única.** ¿Cuál es LA acción de esta pantalla? Si hay tres candidatas al mismo
   nivel visual, no hay ninguna. Y si la única acción ofrecida es destructiva o terminal
   —archivar, eliminar, cancelar—, la pantalla está proponiendo lo contrario de lo que el
   estado del registro pide.
5. **El primer pantallazo.** Mide cuántos píxeles hay entre el borde superior y el primer
   elemento de la tarea principal, y compáralo con la altura del viewport. Si la tarea empieza
   fuera del primer pantallazo por culpa de un aviso, un descargo o un bloque administrativo,
   es hallazgo. Pregunta por cada bloque de arriba: *¿aplica a todos los registros o solo a
   algunos?* Lo que aplica a algunos no se cobra en el espacio de todos (anti-patrón A8,
   regla R8).

**Señales de falla**: titular que describe una categoría en vez de una promesa; la propuesta
de valor escondida bajo el pliegue; jerga interna en la primera línea; la acción principal
compitiendo con "conoce más", "ver video" y el menú.

---

## Capa 2 — Jerarquía

> ¿El orden en que el ojo recorre la pantalla coincide con el orden de importancia de la
> tarea?

Esta es la capa que las auditorías genéricas dan por buena porque el DOM tiene un `h1`. La
jerarquía es perceptual: existe si el ojo la ve.

**Pruebas**

1. **Entrecerrar los ojos.** Aplica desenfoque fuerte o escala de grises a la captura. Anota
   el orden real en que los elementos aparecen. Compáralo con el orden de importancia según
   la tarea. Si no coinciden, es hallazgo — y casi siempre `P1` o `P0`.
2. **Conteo de dominantes.** En un pantallazo debería haber **un** elemento claramente
   dominante. Dos empatados es ambigüedad; tres o más es ruido.
3. **Competencia de acciones.** Cuenta los controles con tratamiento de acción primaria
   visibles a la vez. Más de uno obliga al usuario a decidir antes de entender. Después
   ordena las acciones por frecuencia esperada y por deseabilidad, y compara ese orden con el
   de peso visual: cuando la acción más pesada es la más rara o la más destructiva, la
   interfaz empuja al error (anti-patrón A5).
4. **Elemento borrado.** Tapa el elemento más grande. ¿La pantalla sigue siendo comprensible?
   Si sí, ese elemento es decoración con tamaño de protagonista.
5. **Escala real vs. semántica.** Cruza `headings.outline` con `typography.sizes` del
   inventario: encabezados que se ven más pequeños que texto secundario, `h2` con el mismo
   peso visual que un párrafo, o `div` con aspecto de título.
6. **Contraste de importancia.** Lo importante gana por tamaño, peso, color, espacio o
   posición — idealmente por dos de esos, no por los cinco a la vez.
7. **Profundidad de superficies.** Cuenta los niveles de caja anidada (panel → tarjeta →
   tabla → fila con fondo propio). Por cada uno pregunta: *¿qué separa esta caja que el
   espacio en blanco no podría separar?* Sin respuesta en una frase, sobra. Más de dos
   niveles es hallazgo (anti-patrón A1, regla R1).
8. **Títulos en eco.** Lee en voz alta los títulos anidados en secuencia, incluyendo el
   nombre de la pestaña. Si suenan a la misma frase con un adjetivo agregado —"Documentos" →
   "Documentos técnicos" → "Documentos técnicos obligatorios"— sobra uno (anti-patrón A2).

**Señales de falla**: todo el mismo peso; badges y etiquetas más llamativos que el título;
tarjetas idénticas para cosas de importancia distinta; el precio, el dato o el CTA que la
tarea necesita, escondido en gris al 50 %.

---

## Capa 3 — Ritmo y flujo

> ¿La página tiene cadencia —tensión y respiro— o es una sucesión de bloques del mismo peso?

Es lo que se percibe como "no fluye" y lo que ninguna heurística clásica captura.

**Pruebas**

1. **Mapa de bloques.** Lista las secciones en orden con tres columnas: altura, densidad
   (alta / media / baja) y patrón (`título + texto`, `grilla de tarjetas`, `imagen +
   texto`…). Si el patrón se repite tres veces seguidas, la página es monótona aunque cada
   bloque esté bien resuelto.
2. **Scroll continuo.** Recorre la página completa de una vez. Anota dónde se te fue la
   atención. Ese punto es el hallazgo, aunque el bloque "no tenga nada malo".
3. **Justificación de sección.** Por cada bloque: ¿qué gana el usuario por haber llegado
   hasta aquí y qué lo empuja al siguiente? Un bloque que no responde ninguna de las dos
   sobra — recomendación `Eliminar`.
4. **Respiro antes del momento clave.** Los momentos de decisión (precio, CTA, resumen de
   compra) necesitan espacio alrededor. Si el CTA está apretado entre dos bloques densos, se
   pierde.
5. **Ritmo vertical.** Cruza `rhythm.sections` del inventario: alturas y paddings casi
   idénticos indican que el ritmo es accidental, no compuesto.
6. **Curva de esfuerzo.** En un flujo de varios pasos: ¿el esfuerzo está repartido o hay un
   paso que concentra todo? ¿El paso más caro llega antes de que el usuario tenga motivo para
   pagarlo?

**Señales de falla**: cuatro grillas de tarjetas seguidas; todas las secciones a pantalla
completa; ninguna sección a pantalla completa; el mismo espaciado entre todo; un formulario
de 14 campos en el primer paso.

---

## Capa 4 — Contenido y copy

> ¿Los textos hacen trabajo o rellenan espacio?

**Pruebas**

1. **Prueba del verbo.** Los títulos, ¿afirman algo o etiquetan una categoría? "Servicios" no
   dice nada; "Instalamos en 48 horas" sí. Aplícala a cada título de sección.
2. **Prueba del recorte.** Tacha cada frase que se podría borrar sin pérdida. Lo que queda es
   el contenido real. Si desaparece la mitad, el bloque está inflado.
3. **Microcopy en el punto de decisión.** El botón, ¿dice lo que va a pasar? "Enviar" vs
   "Agendar mi hora". Junto a un campo sensible, ¿está la razón por la que se pide?
4. **Mensajes de error.** ¿Dicen qué pasó, por qué y qué hacer ahora? Un error que dice
   "Error inesperado" o que culpa al usuario ("dato inválido") es hallazgo.
5. **Jerga.** Marca cada término que solo entiende el equipo interno. Contrástalo con la
   capacidad técnica declarada en la Fase 0.
6. **Escaneabilidad.** Párrafos de más de 4–5 líneas, ausencia de subtítulos, listas que
   deberían ser tabla, tabla que debería ser lista.
7. **Ancho de línea.** `lineLength` del inventario: por encima de ~85 caracteres cuesta
   volver al inicio de la línea; por debajo de ~40 se fragmenta la lectura.
8. **Contenido duplicado.** Dos barridos sobre la captura completa: primero los lugares donde
   se comunica el mismo **estado** (etiqueta de encabezado, estado por fila, pie de sección,
   resumen en otra vista); después los **datos** que aparecen dos veces —mismas etiquetas,
   mismos valores, misma fecha, mismo nombre de archivo—. Un bloque entero renderizado dos
   veces en la misma pantalla es el caso más caro y el más difícil de ver auditando por
   partes, porque cada mitad está bien resuelta por separado (anti-patrón A3, regla R3).

**Señales de falla**: tres adjetivos donde va un dato; texto de plantilla nunca reemplazado;
promesas sin prueba; el mismo mensaje repetido en tres bloques con distintas palabras.

---

## Capa 5 — Interacción y estados

> ¿La tarea se completa sin fricción, y qué pasa cuando algo sale mal, está vacío o tarda?

**Pruebas**

1. **Recorrido cronometrado de la tarea.** Complétala de punta a punta contando pasos, clics,
   campos y decisiones. Anota cada punto donde tuviste que releer o retroceder.
2. **Matriz de estados.** Para cada pantalla del flujo: vacío, cargando, error, éxito,
   parcial. Marca los que existen y los que no. Un estado faltante es hallazgo, no un
   pendiente.
3. **Feedback.** Toda acción del usuario necesita respuesta visible inmediata. Cualquier
   espera perceptible necesita indicador. Un botón que no cambia al pulsarse provoca el doble
   envío.
4. **Reversibilidad.** ¿Se puede volver atrás sin perder lo escrito? ¿Hay confirmación antes
   de lo irreversible? ¿La confirmación dice **qué** se va a borrar?
5. **Formularios.** Etiquetas visibles (no solo `placeholder`); validación al salir del campo,
   no al enviar; error junto al campo; tipo de teclado correcto en móvil; `autocomplete`;
   campos opcionales marcados; nada de pedir datos que no se usan.
6. **Teclado.** `Tab` desde el inicio: orden lógico, foco visible, nada inalcanzable, `Esc`
   cierra los diálogos.
7. **Navegación.** ¿Se sabe dónde se está? ¿Se puede volver? ¿El botón atrás del navegador
   hace lo esperado? La navegación no es una acción del flujo: no debe competir en peso con
   las acciones de la tarea.
8. **El vacío ofrece.** Por cada bloque en estado vacío: *¿entrega la acción que lo llena, o
   solo explica por qué está vacío?* Un bloque que solo explica —y cuya acción vive en otro
   bloque— es un callejón sin salida y sobra (anti-patrón A7, regla R7).

**Señales de falla**: el flujo funciona solo en el camino feliz; errores que aparecen recién
al enviar y borran el formulario; modales sin salida; "guardado" que no confirma nada.

---

## Capa 6 — Sistema visual

> ¿Color, tipografía y espaciado significan algo, o son decoración acumulada?

Casi todo aquí se decide con el inventario objetivo: son hechos medidos.

**Pruebas**

1. **Escala tipográfica.** `typography.sizes`. Más de 6–8 tamaños en una pantalla indica
   acumulación, no sistema. Los tamaños deben tener una relación reconocible entre sí.
2. **Pesos y familias.** Más de tres pesos o más de dos familias sin una razón declarada es
   ruido. Un peso debe significar siempre lo mismo.
3. **Paleta real.** `colors`. Cuenta los colores efectivamente usados. Pregunta por cada uno:
   ¿qué significa? Un color sin significado es decoración; un significado con dos colores es
   confusión.
4. **Color de acción.** El color de la acción principal, ¿aparece en elementos que no son
   acciones? Si sí, dejó de señalar.
5. **Contraste medido.** `contrast.failures`. Bajo 4.5:1 en texto normal y 3:1 en texto grande
   es hallazgo objetivo — no admite discusión de gusto. El texto gris claro sobre blanco es el
   caso más común y el más defendido con "es que se ve elegante".
6. **Espaciado.** `spacing`. ¿Los valores pertenecen a una escala (4/8 px o la que sea) o son
   arbitrarios? ¿El espacio separa lo distinto y agrupa lo relacionado, o es uniforme y no
   comunica nada?
7. **Proximidad.** Cada etiqueta, ¿está más cerca del elemento al que pertenece que del
   siguiente? Es el error de agrupación más frecuente y el más invisible.
8. **Radios, bordes y sombras.** Deben ser pocos y consistentes. Tres radios distintos en la
   misma tarjeta es descuido; una sombra por componente es acumulación.
9. **Superficies con función.** Cuenta las superficies apiladas en una pantalla. Más de
   cuatro con el mismo peso visual es hallazgo: cuando todo pesa igual, la pantalla es una
   lista de cajas equivalentes y hay que leerlas todas. Un mensaje que solo informa va como
   texto, no como banner; un input suelto no necesita tarjeta propia (anti-patrón A4, regla
   R6).
10. **Affordance de los campos.** Compara un campo activo con uno deshabilitado del mismo
    formulario. Si se parecen, el sistema gastó su única señal de "no se puede tocar" en
    campos que sí se pueden. Mide el contraste del placeholder y del borde (anti-patrón A6).

**Señales de falla**: dos grises casi iguales; el mismo componente con dos alturas; bordes en
unos elementos y sombras en sus equivalentes; el sistema declarado en el design system y otro
distinto en la pantalla.

---

## Capa 7 — Oficio y detalle

> ¿Se nota una mano decidiendo, o los valores por defecto del framework?

Solo se reporta con nivel de exigencia 2 y sobre todo 3.

**Pruebas**

1. **Alineación óptica.** Íconos con texto, números en columna, contenido dentro de botones.
   Lo matemáticamente centrado a veces se ve descentrado; manda el ojo.
2. **Iconografía.** Mismo grosor de trazo, misma familia, mismo tamaño óptico. Íconos de dos
   sets distintos se detectan de inmediato.
3. **Estados de foco.** Visibles, con contraste suficiente, no eliminados con `outline: none`.
4. **Hover y movimiento.** ¿La animación comunica algo o es adorno? Duraciones sobre ~300 ms
   en microinteracciones se sienten lentas; sin `easing` se sienten mecánicas. Verifica
   `prefers-reduced-motion`.
5. **Imágenes.** Recorte con criterio, relación de aspecto consistente, calidad suficiente,
   peso razonable, nada estirado, nada con marca de agua de banco de imágenes.
6. **Detalles de texto.** Viudas y huérfanas en titulares, comillas rectas donde van
   tipográficas, mayúsculas gritadas, números sin alineación tabular en tablas.
7. **Bordes de la composición.** Márgenes iguales a izquierda y derecha, contenedor con ancho
   máximo, nada pegado al borde en móvil.

---

## Transversal A — Accesibilidad medida

No se supone, se mide. Mínimo verificable:

- Contraste de texto y de controles (`contrast.failures`).
- Nombre accesible en todo control (`interactive.unnamed`); íconos-botón sin etiqueta.
- Orden de tabulación lógico y foco visible.
- Semántica: encabezados en orden, listas como listas, botones que son botones y no `div`.
- `alt` con contenido útil en imágenes informativas y vacío en las decorativas.
- Zoom del navegador al 200 % sin pérdida de contenido.
- Objetivos táctiles de al menos 44 × 44 px en móvil.
- Nada que dependa solo del color para comunicar (errores, estados, categorías).

Lo que no se pudo medir se declara `No verificado`. Una auditoría de accesibilidad completa
es otro trabajo; aquí se cubre lo que es visible y medible en la pantalla auditada.

## Transversal B — Responsive real

- Los cuatro viewports del protocolo de captura, no solo el escritorio.
- Contenido largo y contenido mínimo en cada uno.
- Tablas y grillas: qué hacen al angostarse (¿scroll horizontal? ¿tarjetas? ¿se rompen?).
- Teclado móvil abierto: ¿tapa el campo activo o el botón de envío?
- Elementos fijos (barras, banners de cookies, chat) ocupando la pantalla en móvil.
- Texto que no encoge por debajo de 16 px en campos de formulario (evita el zoom automático
  en iOS).
