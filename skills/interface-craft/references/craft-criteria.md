# Craft Criteria

Criterios de consulta de `interface-craft`. Cada sección trae **pruebas concretas** —cosas que se
hacen mirando la pantalla— y las señales de falla que hay que buscar.

> **No es necesario recorrer todos los criterios en cada tarea.** Lee únicamente las secciones
> relevantes al problema que tienes delante. Esto es una guía de criterio, no una lista de
> verificación obligatoria: una tarea de tipografía no necesita abrir la sección de tablas.

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

**Pruebas**

1. **Entrecerrar los ojos.** Desenfoca la pantalla —o míralas en miniatura. Lo que sigue
   destacando es la jerarquía real. Si no destaca nada, o destaca lo secundario, ahí está el
   problema.
2. **El primer elemento.** Nombra el elemento que el ojo toca primero. ¿Coincide con lo más
   importante de la pantalla? Si el ojo va a un badge de color o a una ilustración decorativa, el
   peso está mal repartido.
3. **Prueba de tres niveles.** Clasifica cada bloque en primario / secundario / terciario. Si una
   buena parte de los bloques compite como primario, no hay jerarquía: hay una lista.
4. **Quitar el color.** En escala de grises, ¿sigue habiendo orden? Si la jerarquía desaparece,
   estaba sostenida solo por color.

**Herramientas de jerarquía** — no es solo `font-size`:

posición · escala · peso · espacio alrededor · agrupación · contraste · densidad · color ·
imagen · ritmo · disclosure progresivo.

**Señales de falla**: todo con el mismo peso visual; jerarquía construida únicamente subiendo
`font-weight` mientras composición y spacing siguen planos; dos o tres CTA compitiendo al mismo
nivel; metadata con el mismo tratamiento que el dato principal; el título de la página más grande
que el contenido que importa.

---

## Composición

**Pruebas**

1. **¿Responde al contenido?** Dibuja los bloques como rectángulos, sin texto. ¿Esa distribución
   dice algo sobre lo que contiene, o serviría igual para cualquier otra pantalla?
2. **Contenido dominante.** ¿Hay un elemento que merece dominar —una tabla, un gráfico, una
   imagen, un formulario? Si lo hay y está compitiendo en una grilla de iguales, la composición no
   lo reconoce.
3. **Simetría injustificada.** Tres tarjetas iguales para tres cosas de importancia distinta es
   una decisión que niega el contenido.
4. **Prueba de recorte.** Tapa la mitad inferior. ¿Lo que queda arriba es lo que debía quedar?

**Recursos disponibles cuando corresponden**: asimetría, ritmo editorial, contraste de escala,
contenido dominante, agrupaciones no uniformes, disclosure, navegación contextual, visualización
de datos, imagen, espacios de descanso, densidad intencional.

**Señales de falla**: la estructura por defecto (badge → título → párrafo → dos botones → tres
tarjetas; o título → KPI → gráfico → tabla) aplicada sin que el contenido la pida; cada bloque en
su propia superficie; anidamiento de contenedores para separar cosas que el espacio ya separaba.

---

## Tipografía

**Antes de introducir un tamaño nuevo**, en este orden:

1. Revisa `docs/ui-system.md`.
2. Revisa los roles tipográficos que el producto ya usa.
3. Decide si el tamaño nuevo representa **realmente un rol nuevo**, o solo "un poquito más" para
   esta pantalla.

Escalas accidentales como `15 / 16 / 17 / 18 / 19 / 20` no se diseñaron: se acumularon, un
"poquito más" por vez. Prefiere **roles semánticos** —título de pantalla, título de sección,
cuerpo, apoyo, metadata— sobre una lista de píxeles.

**Pruebas**

1. **Cuenta los niveles en uso** en la vista. Más de cinco o seis en una pantalla suele indicar
   que dos son el mismo rol con distinto valor.
2. **Distancia perceptual.** Dos niveles que se distinguen por 2 px no son dos niveles: quien mira
   no los diferencia, y quien implementa los confunde.
3. **Ancho de línea.** El texto corrido se lee mejor en columnas estrechas —del orden de 45 a 75
   caracteres como referencia orientativa, no como umbral de aprobación—. Lo que se juzga es si
   el ojo encuentra el inicio de la línea siguiente: un párrafo a todo el ancho de un contenedor
   grande no se lee, se recorre.

**Se revisan en conjunto**, no aislados: `font-size`, `line-height`, `weight`, `tracking`, ancho
de línea, contraste y la relación entre niveles. Subir el tamaño sin bajar el `line-height`
proporcional produce títulos que flotan.

**Señales de falla**: un tamaño nuevo por pantalla; jerarquía apoyada solo en `weight`;
`line-height` heredado del cuerpo aplicado a un título grande; mayúsculas con `tracking` por
defecto; texto de apoyo tan claro que deja de leerse.

---

## Spacing

El spacing **expresa relaciones**. Dos elementos cerca se leen como uno; separados, como dos. Esa
es toda su función; decorar no lo es.

**Distingue funciones antes de elegir un valor**: separación entre secciones · entre grupos ·
entre elementos relacionados · padding interno · entre controles · densidad de datos.

**Pruebas**

1. **Ley de proximidad.** ¿La distancia entre un label y su valor es menor que la distancia al
   siguiente par? Si es igual o mayor, los pares se leen cruzados.
2. **Revisa la escala existente** antes de agregar un valor. Un `gap-[22px]` nuevo junto a un
   `gap-6` existente casi siempre es el mismo rol con otro número.
3. **Consistencia no es igualdad.** Valores distintos son correctos cuando expresan relaciones
   distintas. No impongas el mismo gap en toda la pantalla: eso destruye la agrupación.

**Señales de falla**: series como `gap-[18px] / gap-[22px] / gap-[26px] / gap-[30px]` sin razón
perceptual; espacio uniforme entre todo, que aplana los grupos; padding grande usado para
compensar la falta de jerarquía; márgenes que dependen del orden de los elementos en vez de su
relación.

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

**Pruebas**

1. **Una acción principal por vista.** Nómbrala. Si hay tres candidatas con el mismo peso, no hay
   ninguna.
2. **Peso proporcional a la frecuencia y a la consecuencia.** Lo que se hace siempre es visible;
   lo destructivo no compite en el mismo peso que lo constructivo.
3. **Ubicación previsible.** La acción de una fila, de una tarjeta o de un panel vive donde ya
   vive en el resto del producto.
4. **Etiqueta que dice el resultado.** "Guardar cambios" sobre "Aceptar".

**Señales de falla**: el mismo CTA repetido tres veces en la misma vista sin cambio de contexto;
botones secundarios con el mismo peso que el primario; acciones destructivas con el tratamiento
más llamativo; una barra de acciones con seis botones donde cinco son excepcionales.

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

**Señales de falla**: una columna de campos idénticos sin agrupación; labels dentro del campo que
desaparecen al escribir; validación que solo aparece al enviar; acción primaria deshabilitada sin
decir qué falta; formularios metidos dentro de tarjetas que no aportan separación.

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

**Sobre la librería**: los ejes, escalas, tooltips, leyendas y series múltiples los resuelve una
librería de gráficos —la que el proyecto ya use—. Se integra al sistema visual del producto:
colores del sistema, tipografía del sistema, grillas discretas. Un gráfico con la paleta por
defecto de la librería se ve como un widget pegado.

**Señales de falla**: seis KPI del mismo tamaño; gráficos sin unidades; leyendas que obligan a
mirar dos veces cuando la etiqueta cabía junto a la serie; ejes truncados que exageran la
variación; un gráfico donde bastaba un número.

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

**Sobre la librería**: sorting, filtering, paginación y selección múltiple no se construyen desde
cero cuando el producto necesita una tabla avanzada y ya existe una solución adecuada.

**Señales de falla**: convertir una tabla en tarjetas y perder la comparación entre filas; ocho
columnas con el mismo peso; celdas con texto largo sin truncado ni tooltip; una tabla con
paginación de diez filas en una pantalla que cabía treinta.

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
