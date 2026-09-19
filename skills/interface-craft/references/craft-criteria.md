# Craft Criteria

Criterios de consulta de `interface-craft`. Cada sección trae **pruebas concretas** —cosas que se
hacen mirando la pantalla— y las señales de falla que hay que buscar.

> **No es necesario recorrer todos los criterios en cada tarea.** Lee únicamente las secciones
> relevantes al problema que tienes delante. Esto es una guía de criterio, no una lista de
> verificación obligatoria: una tarea de tipografía no necesita abrir la sección de tablas.

Los principios de percepción e interacción incorporados en este documento son **herramientas de decisión y preguntas concretas**, nunca un checklist teórico que deba recitarse en la entrega. Su propósito es resolver la interfaz que tienes delante con criterio visual y funcional; no sustituyen a `ux-audit`, que audita funnels, abandono y recorridos transversales de usuario.

Lo que ya está en [`SKILL.md`](../SKILL.md) no se repite aquí: alcance, precedencia de fuentes,
orden de decisión, los dos modos de fallo, regla de librerías, validación visual y derivaciones.
Este archivo entra **después** de esas decisiones, cuando ya sabes qué área tienes que resolver.

| Área | Cuándo abrirla |
|---|---|
| [Jerarquía](#jerarquía) | Todo pesa igual; no se sabe dónde mirar |
| [Composición](#composición) | La estructura es la fórmula por defecto, no una respuesta al contenido |
| [Tipografía](#tipografía) | Aparecen tamaños nuevos; la escala se está dispersando |
| [Spacing](#spacing) | Los grupos no se leen como grupos; valores arbitrarios |
| [Densidad](#densidad) | Panel que "se ve cargado"; landing que se ve vacía |
| [Color](#color) | Hace falta un color que no existe; estados señalados solo por color |
| [Imagen](#imagen-y-media) | La imagen decora en vez de aportar |
| [Acciones](#acciones) | Varios CTA compiten; no se distingue lo primario |
| [Formularios](#formularios) | Alta de datos, filtros, configuración |
| [Dashboards](#dashboards-y-visualización-de-datos) | KPI, gráficos, comparación |
| [Tablas y listados](#tablas-y-listados) | Muchas filas, muchas columnas, acciones por fila |
| [Estados](#estados) | Loading, vacío, error, permisos, datos extremos |
| [Motion](#motion) | Transiciones, entradas, feedback |

---

## Jerarquía

Una interfaz con jerarquía responde sin que nadie la explique: qué importa primero, qué después,
cuál es la acción principal, qué es contexto, qué es metadata y qué puede esperar.

> **El tratamiento distintivo es un recurso escaso** (*distinctive treatment is a scarce resource*).
> El elemento diferente llama la atención solo cuando la mayoría no intenta llamar la atención al mismo
> tiempo. Si todos los elementos rompen simultáneamente el patrón con acentos, badges o fondos especiales,
> ninguno es excepcional. El tratamiento distintivo se reserva para lo que realmente requiere atención
> o acción prioritaria, sin que esto signifique limitar artificialmente a exactamente uno: pueden existir
> dos alertas críticas o ninguna si el estado es nominal.

> **Semejanza: elementos visualmente iguales se perciben como equivalentes.** Acciones con distinta
> prioridad no deben parecer idénticas; controles con el mismo comportamiento deben mantener tratamiento
> coherente; y elementos meramente informativos no deben lucir interactivos.

**Pruebas**

1. **Entrecerrar los ojos.** Desenfoca la pantalla —o mírala en miniatura—. Lo que sigue
   destacando es la jerarquía real. Si no destaca nada, o destaca lo secundario, ahí está el
   problema.
2. **El primer elemento.** Nombra el elemento que el ojo toca primero. ¿Coincide con lo más
   importante de la pantalla? Si el ojo va a un badge de color o a una ilustración decorativa, el
   peso está mal repartido.
3. **Prueba de tres niveles.** Clasifica cada bloque en primario / secundario / terciario. Si una
   buena parte de los bloques compite como primario, no hay jerarquía: hay una lista.
4. **Quitar el color.** En escala de grises, ¿sigue habiendo orden? Si la jerarquía desaparece,
   estaba sostenida solo por color.
5. **Énfasis reservado (Von Restorff).** Antes de usar color de acento, tamaño excepcional, badge,
   borde destacado, sombra o icono llamativo, pregunta: *¿qué elementos merecen realmente romper el
   patrón?* Si múltiples KPI o cards compiten sin justificación, reduce los secundarios a un tratamiento más silencioso.
6. **Prueba de semejanza.** Si intercambio dos elementos visualmente iguales, ¿seguiría entendiendo cuál
   es primario, interactivo, destructivo o meramente informativo? Si no, el tratamiento está ocultando
   diferencias funcionales relevantes.

**Herramientas de jerarquía** — no es solo `font-size`:

posición · escala · peso · espacio alrededor · agrupación · contraste · densidad · color ·
imagen · ritmo · disclosure progresivo.

**Señales de falla**: todo con el mismo peso visual; jerarquía construida únicamente subiendo
`font-weight` mientras composición y spacing siguen planos; dos o tres CTA compitiendo al mismo
nivel; cada bloque o KPI con color propio, badge y fondo decorativo para que "ninguno pase desapercibido";
elementos informativos que parecen botones interactivos; metadata con el mismo tratamiento que el dato principal;
el título de la página más grande que el contenido que importa.

---

## Composición

> **Agrupar no implica contenedores** (*grouping does not imply containers*). Antes de introducir una
> card, borde, fondo, panel o box anidado, comprueba si la relación puede expresarse mediante
> proximidad, alineación, jerarquía, ritmo, espacio o tipografía. La región común (*common region*) es
> útil cuando el límite aporta información que el espaciado por sí solo no puede comunicar: delimitar
> una unidad manipulable, separar contextos disjuntos, diferenciar estados o aislar una región funcional.
> Una card no se justifica simplemente diciendo *"estos elementos van juntos"*: la proximidad ya hace eso.

> **Anti-patrón de anidamiento innecesario**:
> ```text
> sección
> └── card
>     └── card
>         └── título + valor
> ```
> si las superficies anidadas no añaden relación contextual ni comportamiento interactivo real.

> **Composición según información dominante**: antes de elegir una cuadrícula uniforme, decide qué
> información domina, qué necesita comparación, qué lectura secuencial, qué exploración y qué es mero
> contexto. Si la importancia de los bloques es desigual, una grilla simétrica nivela artificialmente el
> contenido. Usa asimetría, contraste de escala, master/detail, layouts editoriales, bloques dominantes,
> agrupaciones secundarias o rail lateral según la tarea.

**Pruebas**

1. **Prueba de genericidad (*Genericity test*).** Si reemplazo el contenido por el de otro producto
   completamente distinto, ¿esta composición seguiría funcionando prácticamente igual? Si la respuesta
   es sí, comprueba qué decisiones de la estructura responden específicamente al contenido, a la tarea
   o al producto actual. Que un patrón sea reutilizable (master/detail, formulario con acciones, tabla con filtros)
   no lo hace genérico; el problema surge cuando ninguna decisión relevante responde al caso concreto.
   *Los patrones familiares son útiles; la composición genérica no es familiaridad.*
2. **Contenido dominante.** ¿Hay un elemento que merece dominar —una tabla, un gráfico, una
   imagen, un formulario? Si lo hay y está compitiendo en una grilla de iguales, la composición no
   lo reconoce.
3. **¿La proximidad basta o hace falta superficie?** Evalúa si el grupo ya se entiende por proximidad,
   alineación y espacio antes de meterlo dentro de una card o borde.
4. **Simetría injustificada.** Tres tarjetas iguales para tres cosas de importancia distinta es
   una decisión que niega el contenido.
5. **Prueba de recorte.** Tapa la mitad inferior. ¿Lo que queda arriba es lo que debía quedar?

**Recursos disponibles cuando corresponden**: asimetría, ritmo editorial, contraste de escala,
contenido dominante, agrupaciones no uniformes, disclosure, navegación contextual, visualización
de datos, imagen, espacios de descanso, densidad intencional, master/detail.

**Señales de falla**: la estructura por defecto (badge → título → párrafo → dos botones → tres
tarjetas; o título → KPI → gráfico → tabla) aplicada sin que el contenido la pida; cards envolviendo
simplemente un label y un valor; cards anidadas dentro de cards sin separación de contexto; cada
bloque en su propia superficie decorativa; grilla perfectamente simétrica para contenidos de peso desigual.

---

## Tipografía

> **Jerarquía por roles, no por nudges**: cuando una jerarquía no funciona, **no la resuelvas automáticamente**
> subiendo cuatro píxeles o engrosando una variante (`40px → 44px`, `font-medium → font-semibold`).
> Revisa antes: posición, espacio alrededor, ancho, contraste, escala relativa, relación título/contenido
> y el peso del bloque completo. Una diferencia tipográfica debe responder a un **rol funcional o semántico**,
> no a un ajuste cosmético aislado.

**Antes de introducir un tamaño nuevo**, en este orden:

1. Revisa `docs/ui-system.md`.
2. Revisa los roles tipográficos que el producto ya usa.
3. Decide si el tamaño nuevo representa **realmente un rol nuevo**, o solo "un poquito más" para
   esta pantalla.

Escalas accidentales como `14 / 15 / 16 / 17 / 18 / 20 / 22 / 24` no se diseñaron: se acumularon, un
"poquito más" por vez. Prefiere **roles semánticos** —título de pantalla, título de sección,
cuerpo, apoyo, metadata— sobre una lista dispersa de píxeles.

**Pruebas**

1. **Cuenta los niveles en uso** en la vista. Si varios niveles tienen diferencias sutiles sin roles
   distinguibles, simplifica hacia los roles existentes del sistema.
2. **Distancia perceptual.** Dos niveles que se distinguen por 2 px no son dos niveles: quien mira
   no los diferencia, y quien implementa los confunde.
3. **Ancho de línea.** El texto corrido se lee mejor en columnas estrechas —del orden de 45 a 75
   caracteres como referencia orientativa, no como umbral de aprobación—. Lo que se juzga es si
   el ojo encuentra el inicio de la línea siguiente: un párrafo a todo el ancho de un contenedor
   grande no se lee, se recorre.
4. **Prueba de rol.** Nombra el rol funcional de cada estilo de texto en la pantalla. Si dos textos
   tienen tamaños o pesos distintos pero el mismo rol, uno de los dos es una desviación.

**Se revisan en conjunto**, no aislados: `font-size`, `line-height`, `weight`, `tracking`, ancho
de línea, contraste y la relación entre niveles. Subir el tamaño sin bajar el `line-height`
proporcional produce títulos que flotan.

**Señales de falla**: un tamaño nuevo por pantalla; jerarquía apoyada solo en `weight` o en micro-nudges
de 2-4 px; `line-height` heredado del cuerpo aplicado a un título grande; mayúsculas con `tracking` por
defecto; texto de apoyo tan claro que deja de leerse; escalas tipográficas accidentales sin roles.

---

## Spacing

El spacing **expresa relaciones**. Dos elementos cerca se leen como uno; separados, como dos. Esa
es toda su función; decorar no lo es.

> **Relación conceptual antes que número**:
> ```text
> distancia dentro de un grupo
> <
> distancia entre grupos
> <
> distancia entre secciones
> ```
> Esta jerarquía espacial es una **relación conceptual**, no una fórmula matemática rígida. Antes de
> ajustar un gap o padding, identifica primero qué relación representa en la jerarquía de la pantalla.
> Evita el *pixel nudging* del agente (`gap-5 → gap-[22px]`, `padding-6 → padding-[26px]`) cuando no
> existe una decisión perceptual nueva que lo fundamente. Si el sistema ya ofrece una expresión equivalente,
> úsala; si no la resuelve, deriva el problema sistémico a `visual-foundation`.

**Distingue funciones antes de elegir un valor**: separación entre secciones · entre grupos ·
entre elementos relacionados · padding interno · entre controles · densidad de datos.

**Pruebas**

1. **Relación conceptual de proximidad.** ¿Se cumple que la distancia dentro de un grupo es menor que
   entre grupos distintos, y esta menor que entre secciones? Si la distancia entre elementos inconexos es
   menor que entre elementos relacionados, la pantalla se leerá invertida.
2. **Ley de proximidad.** ¿La distancia entre un label y su valor es menor que la distancia al
   siguiente par? Si es igual o mayor, los pares se leen cruzados.
3. **Revisa la escala existente** antes de agregar un valor. Un `gap-[22px]` nuevo junto a un
   `gap-6` existente casi siempre es el mismo rol con otro número.
4. **Consistencia no es igualdad.** Valores distintos son correctos cuando expresan relaciones
   distintas. No impongas el mismo gap en toda la pantalla: eso destruye la agrupación.

**Señales de falla**: pixel nudging del agente (`gap-5 → gap-[22px]`, `p-6 → p-[26px]`); series como
`gap-[18px] / gap-[22px] / gap-[26px] / gap-[30px]` sin razón perceptual; espacio uniforme entre todo,
que aplana los grupos; padding grande usado para compensar la falta de jerarquía; márgenes que dependen
del orden de los elementos en vez de su relación.

---

## Densidad

**Pruebas**

1. **¿Cuántas veces al día se usa esta pantalla?** Una vez por cliente nuevo y ocho horas seguidas
   no piden la misma densidad.
2. **¿La tarea es leer o comparar?** Comparar exige ver varias cosas a la vez: el aire que ayuda a
   leer estorba para comparar.
3. **Scroll por dato.** En una herramienta operacional, cuenta cuántos registros caben en un
   viewport. Si caben muy pocos, el diseño está cobrando en scroll lo que gana en aire — y
   cuántos son pocos depende de si la tarea es leer uno o comparar varios.

**Señales de falla**: tarjetas grandes envolviendo una línea de información; en un panel de alta
densidad, padding de landing; información eliminada "para simplificar" cuando el usuario la
necesitaba; al revés, una landing con densidad de tabla y sin espacio de descanso.

Cuando una pantalla operacional "se ve cargada", el orden de intervención es: **jerarquía →
agrupación → disclosure → densidad**. Eliminar información es la última opción, y solo con
evidencia de que nadie la usa.

---

## Color

**Distingue el rol antes de elegir el valor**: identidad de marca · superficie · jerarquía ·
interacción · estado · feedback. Un color de marca no es automáticamente un color de interfaz, y
convertir la paleta completa de marca en roles de UI produce interfaces que gritan.

**Pruebas**

1. **¿Ya existe un rol equivalente?** No introduzcas un color nuevo por conveniencia local si el
   sistema ya tiene uno para esa función.
2. **Grises casi idénticos.** Si dos tonos son prácticamente indistinguibles en pantalla y
   cumplen el mismo rol, son un color mal copiado, no dos niveles del sistema. El criterio es
   perceptual y funcional: ¿alguien nota la diferencia, y significa algo distinto?
3. **Color como única señal.** Un estado señalado solo por color falla para daltonismo, en
   impresión y en pantallas malas. Acompáñalo de forma, texto, icono o posición.
4. **Contraste medido**, no estimado, en texto y en controles.

**Señales de falla**: cinco grises sin función distinta; el color de marca usado como color de
error; semáforos de estado sin etiqueta; superficies diferenciadas por color donde el espacio ya
las separaba.

---

## Imagen y media

**Pruebas**

1. **¿Aporta información o rellena?** Si la imagen se puede sustituir por cualquier otra sin
   pérdida, es decoración con costo de carga.
2. **Recorte y foco.** ¿El punto de interés sobrevive al recorte en distintas proporciones?
3. **Texto sobre imagen.** ¿El contraste se sostiene con la imagen más clara y con la más oscura
   del conjunto, no solo con la de ejemplo?
4. **Ausencia.** ¿Qué se ve cuando no hay imagen? Ver [Estados](#estados).

**Señales de falla**: stock genérico como relleno de una sección sin contenido; ilustraciones
decorativas que compiten con la acción principal; proporción que cambia entre tarjetas del mismo
listado; imagen que carga después y desplaza el contenido.

---

## Acciones

> **Prominencia visual y facilidad de adquisición van juntas**: una acción importante no solo debe
> verse importante, debe ser **fácil de alcanzar y activar**. Considera en conjunto: tamaño del target,
> espacio alrededor (clearance), ubicación en el flujo de la tarea, frecuencia de uso, consecuencia y
> dispositivo. Destacar un botón con color de acento no compensa que su target mida 20 px, que el área
> interactiva se limite al texto visible o que esté ubicado desconectado del punto natural de decisión o
> confirmación de la tarea (considerando el layout, acciones sticky o convenciones del producto).

> **Demasiadas opciones simultáneas con igual peso aumentan el esfuerzo de decisión** (*too many
> simultaneous choices with equal weight increase decision effort*). Cuando múltiples acciones compiten al
> mismo nivel, evalúa su frecuencia, consecuencia y contexto para organizarlas mediante priorización,
> agrupación, progressive disclosure, defaults inteligentes o menús secundarios. **Reducir competencia no
> significa esconder lo frecuente**: en una barra con varias opciones no todas necesitan botones de peso
> primario, pero tampoco se resuelve ocultando operaciones habituales dentro de un menú solo para que la
> interfaz parezca minimalista.

**Pruebas**

1. **Una acción principal por vista.** Nómbrala. Si hay tres candidatas con el mismo peso, no hay
   ninguna. Reserva el énfasis principal para el objetivo central del flujo.
2. **Facilidad de adquisición (Fitts).** ¿La acción principal y las frecuentes tienen un target generoso,
   con área clickeable en todo el elemento y no solo en el texto? ¿Están ubicadas cerca del punto donde se
   completa o confirma la tarea, según el layout, acciones sticky o contexto del producto?
3. **Competencia entre opciones (Hick).** Si una barra o bloque acumula muchas opciones, ¿las acciones
   frecuentes están accesibles de inmediato mientras las excepcionales se agrupan en un menú secundario?
   ¿Las destructivas están separadas en apariencia y espacio de las seguras?
4. **Peso proporcional a la frecuencia y a la consecuencia.** Lo que se hace siempre es visible y
   fácil; lo destructivo no compite en el mismo peso ni en la misma proximidad física que lo constructivo.
5. **Ubicación previsible y etiqueta de resultado.** La acción vive donde ya vive en el producto y su
   etiqueta dice con precisión qué ocurrirá: "Guardar cambios" sobre "Aceptar", "Eliminar cuenta" sobre "Continuar".

**Señales de falla**: barra de herramientas con 6-8 botones del mismo peso visual compitiendo entre sí sin
jerarquía de uso; operaciones frecuentes escondidas bajo menús colapsados para forzar un diseño minimalista;
botón principal con target pequeño o clickeable solo en el texto y ubicado lejos del punto de decisión;
acción secundaria pegada físicamente a una destructiva sin espacio de protección; acciones destructivas con
el tratamiento más vistoso o indistinguible de las ordinarias.

---

## Formularios

**Pruebas**

1. **Agrupación por sentido**, no por tipo de campo. Los campos que se responden juntos van
   juntos.
2. **Un objetivo por pantalla o por paso.** Un formulario que hace tres cosas necesita tres
   secciones claras o tres pasos.
3. **Ancho del campo como pista.** Un código postal no ocupa lo mismo que una dirección.
4. **Errores junto al campo**, con el texto de cómo corregirlo, no solo qué falló.
5. **Qué es obligatorio** se ve antes de enviar, no después.

**Sobre las primitives accesibles**: no recrees a mano controles complejos que involucran accesibilidad delicada —combobox, date pickers, popovers, menús o diálogos modales—. Prefiere las primitives accesibles que el proyecto ya utilice (Radix, React Aria, Headless UI, etc.) para garantizar navegación por teclado, focus trapping y roles ARIA correctos.

**Señales de falla**: una columna de campos idénticos sin agrupación; labels dentro del campo que
desaparecen al escribir; validación que solo aparece al enviar; acción primaria deshabilitada sin
decir qué falta; formularios metidos dentro de tarjetas que no aportan separación; combobox o diálogos
construidos artesanalmente sin soporte de teclado ni foco accesible.

---

## Dashboards y visualización de datos

**Pruebas**

1. **¿Cuál es la pregunta?** Un panel responde preguntas concretas. Si no puedes escribir las tres
   preguntas que responde, no es un panel: es una vitrina de datos.
2. **Prioridad entre métricas.** No todas las métricas importan igual. La que dispara acción va
   primero y más grande; el resto es contexto. Una fila de KPI idénticos es la negación de esa
   decisión.
3. **Comparación, no solo valor.** Un número sin referencia —periodo anterior, objetivo, promedio—
   no permite decidir nada.
4. **Tipo de gráfico según la pregunta**: evolución en el tiempo → línea; comparación entre
   categorías → barras; composición → pocas partes, y casi nunca un anillo con nueve;
   distribución → histograma o caja; correlación → dispersión.
5. **Del dato a la acción.** ¿Qué se puede hacer desde aquí cuando el número está mal?

**Sobre la librería**: si el requisito incluye varios de estos elementos —ejes, escalas, series múltiples,
tooltips enriquecidos, leyendas interactivas, resize reactivo, accesibilidad, zoom/pan o formateo numérico
complejo—, **un SVG artesanal construido a mano debe considerarse una señal para revisar la decisión técnica**,
no la opción por defecto. Reutiliza la librería de gráficos que el proyecto ya tenga instalada; si no existe,
evalúa una dependencia estándar y mantenida. Intégrala siempre al sistema visual del producto: colores del
sistema, tipografía del sistema y grillas discretas, en vez de adoptar la paleta o tipografías por defecto
de la librería.

**Señales de falla**: seis KPI del mismo tamaño; gráficos sin unidades; leyendas que obligan a
mirar dos veces cuando la etiqueta cabía junto a la serie; ejes truncados que exageran la
variación; un gráfico donde bastaba un número; gráficos complejos dibujados a mano en SVG habiendo librerías
adecuadas en el proyecto.

---

## Tablas y listados

**Pruebas**

1. **La columna que importa a la izquierda**, y el resto en orden de uso, no de esquema de base de
   datos.
2. **Alineación por tipo**: números a la derecha, texto a la izquierda, misma cantidad de
   decimales en toda la columna.
3. **Densidad de fila según la tarea.** Escanear cien filas y revisar cinco no piden la misma
   altura.
4. **Encabezado visible** al hacer scroll cuando la tabla es larga.
5. **Acciones por fila** sin abrir cinco iconos por registro: lo frecuente visible, lo demás en un
   menú.

**Sobre la librería**: una tabla simple de consulta puede ser HTML nativo limpio. Sin embargo, si la tarea
exige sorting interactivo, filtros combinados, paginación, selección múltiple, resizing o visibilidad de columnas,
**no debe reconstruirse artesanalmente desde cero** si el proyecto ya cuenta con una solución adecuada o una
librería estándar probada (p. ej. TanStack Table u homólogos) que reduzca significativamente la complejidad.

**Señales de falla**: convertir una tabla en tarjetas y perder la comparación entre filas; ocho
columnas con el mismo peso; celdas con texto largo sin truncado ni tooltip; una tabla con
paginación de diez filas en una pantalla que cabía treinta; lógica de sorting y selección compleja
reprogramada a mano con bugs de estado.

---

## Estados

Una interfaz se diseña completa, no solo en su estado ideal. Cuando formen parte del alcance
existente:

| Estado | Qué revisar |
|---|---|
| Loading | ¿Se mantiene la estructura o la página salta al llegar los datos? |
| Empty | ¿Explica por qué está vacío y qué hacer, o solo dice "sin resultados"? |
| Error | ¿Dice qué pasó, qué se puede hacer, y conserva lo que el usuario escribió? |
| Success | ¿Es visible sin robarse la pantalla, y persiste lo suficiente para leerse? |
| Disabled | ¿Se distingue de un campo normal, y se sabe por qué está deshabilitado? |
| Selected | ¿Se distingue de hover, y sobrevive en escala de grises? |
| Hover / focus | ¿El foco de teclado es visible, y no solo el hover de mouse? |
| Datos largos | Nombres, títulos y etiquetas al doble de longitud: ¿rompe, trunca o se adapta? |
| Contenido corto | Una sola fila, un solo elemento: ¿la composición aguanta o se ve rota? |
| Sin imagen | ¿Hay fallback deliberado o un hueco? |
| Sin permiso | ¿La acción se oculta, se deshabilita con explicación, o falla al hacer clic? |

Dos límites: **no inventes estados funcionales que el producto no tiene**, y **no diseñes solo con
datos perfectos** si el componente ya contempla otros.

---

## Motion

**Pruebas**

1. **¿Qué comunica?** El movimiento explica origen, destino, relación o resultado. Si no explica
   nada, es decoración con costo de espera.
2. **Duración según la distancia y la frecuencia.** Lo que se usa mil veces al día se hace corto o
   se elimina.
3. **Una entrada, no una coreografía.** Animar cada elemento de una lista al cargar retrasa la
   lectura de todos.
4. **`prefers-reduced-motion`** respetado.

**Sobre la herramienta**: transiciones simples —hover, focus, aparición, cambio de color— son CSS.
Gestos, secuencias coordinadas y estados de entrada/salida orquestados van con la solución de
motion que el proyecto ya use. No se escriben cientos de líneas de CSS para evitar una librería ya
instalada, ni se instala una librería para una transición de 150 ms.

**Señales de falla**: animaciones de entrada en contenido que el usuario ya estaba leyendo;
duraciones largas en acciones frecuentes; movimiento que compite con la lectura; efectos distintos
para la misma clase de transición en pantallas distintas.
