# Adaptive Patterns

Patrones de consulta de `adaptive-layout`. Cada sección responde cuatro cosas: **qué se rompe**
al cambiar el espacio, **qué debe preservarse**, **qué estrategias existen** y **cuándo una
estrategia destruye la tarea**.

> **Consulta solo las secciones relacionadas con el problema responsive que tienes delante.** No
> es un catálogo de recetas obligatorias: es material para decidir, y la decisión depende de la
> tarea que la pantalla sirve. Ninguna estrategia listada aquí es correcta por defecto.

Lo que ya está en [`SKILL.md`](../SKILL.md) no se repite: frontera con `interface-craft`,
precedencia de fuentes, preservación de capacidades, prioridad por viewport, breakpoints guiados
por contenido, DOM y focus, validación visual y formato de entrega.

| Área | Cuándo abrirla |
|---|---|
| [Navegación](#navegación) | El acceso a los destinos deja de caber |
| [Sidebars](#sidebars) | El panel lateral se come la pantalla |
| [Headers](#headers) | La barra superior envuelve o crece demasiado |
| [Toolbars](#toolbars) | Muchos controles en una fila que ya no entra |
| [Acciones](#acciones) | Botones que compiten, se apilan o desaparecen |
| [Grids](#grids) | Columnas que se estrechan hasta dejar de servir |
| [Tablas](#tablas) | La tabla no cabe; hay que decidir estrategia |
| [Formularios](#formularios) | Varias columnas, pasos, campos largos |
| [Dashboards](#dashboards) | KPI, gráfico y tabla en una columna infinita |
| [Gráficos](#gráficos) | Ejes, leyendas y etiquetas ilegibles |
| [Master / detail](#master--detail) | Listado y detalle simultáneos que ya no caben |
| [Filtros](#filtros) | Filtros laterales o en fila sin espacio |
| [Búsqueda](#búsqueda) | El campo de búsqueda compite con todo lo demás |
| [Modales, drawers y sheets](#modales-drawers-y-sheets) | Overlays más grandes que el viewport |
| [Imágenes y media](#imágenes-y-media) | Crop, proporción y orden respecto del contenido |
| [Sticky y fixed](#sticky-y-fixed) | Barras que tapan contenido en pantallas bajas |
| [Empty, loading y error](#empty-loading-y-error) | Estados que solo se probaron en desktop |
| [Contenido extremo](#contenido-extremo) | Nombres larguísimos, listas enormes, cifras grandes |

---

## Navegación

**Qué se rompe.** Los destinos dejan de caber en el espacio que los mostraba, y la tentación es
recortar la arquitectura de información para que entren.

**Qué se preserva.** Todos los destinos siguen existiendo y siendo alcanzables. La jerarquía
entre primarios y secundarios se mantiene, aunque cambie el mecanismo.

**Estrategias.** Destinos primarios persistentes con los secundarios en menú · navegación
horizontal a menú compacto · agrupación por sección con disclosure · navegación contextual
dentro de la vista en lugar de global.

**Cuándo destruye la tarea.** Cuando reduce diez destinos a cuatro "porque no caben"; cuando
esconde detrás de dos toques algo que se usa en cada sesión; cuando inventa una jerarquía nueva
que no existe en el producto. La estructura funcional permanece: cambia el acceso, no el mapa.

---

## Sidebars

**Qué se rompe.** Un panel lateral fijo consume una fracción del ancho que en pantallas
estrechas ya no sobra, y a menudo empuja el contenido principal a una franja inusable.

**Qué se preserva.** Lo que el sidebar contiene: navegación, filtros, contexto o herramientas.
Si es la única forma de llegar a algo, no puede desaparecer.

**Estrategias.** Drawer u off-canvas invocado desde un control visible · colapso a iconos con
etiquetas al abrir · promoción de los ítems frecuentes a una barra persistente y el resto al
drawer · conversión a navegación superior cuando hay pocos destinos.

**Cuándo destruye la tarea.** Cuando el sidebar contenía **contexto que se consulta mientras se
trabaja** —un árbol de carpetas, filtros activos, una lista de conversaciones— y pasa a un
overlay que se cierra cada vez. Ahí conviene un colapso parcial o una vista de dos paneles
conmutables, no un drawer modal.

---

## Headers

**Qué se rompe.** Logo, navegación, búsqueda, notificaciones, selector de contexto y avatar
compiten por una fila que ya no da; la barra envuelve en dos o tres líneas y se come el primer
viewport.

**Qué se preserva.** La identificación de dónde está el usuario, el acceso a la navegación y las
acciones globales realmente frecuentes.

**Estrategias.** Dividir en dos niveles —identidad y contexto arriba, acciones abajo— · mover la
búsqueda a un control que la expande · agrupar notificaciones y cuenta en un solo menú ·
prescindir del texto del logo conservando la marca · header que se retrae al hacer scroll.

**Cuándo destruye la tarea.** Cuando el selector de contexto —proyecto, empresa, sucursal,
periodo— se esconde en un menú y el usuario deja de saber sobre qué está operando. Ese control
es contexto, no una acción secundaria.

---

## Toolbars

**Qué se rompe.** Una fila de controles heterogéneos —vistas, orden, filtros, exportación,
acciones masivas— empieza a envolver antes de mobile, típicamente en el punto intermedio.

**Qué se preserva.** El control primario de la vista y la posibilidad de ejecutar las acciones
frecuentes sin abrir tres menús.

**Estrategias.** Separar por naturaleza —controles de vista en una fila, acciones en otra— ·
overflow menu para la cola de secundarias · iconos con etiqueta accesible para los controles
universalmente reconocibles · scroll horizontal contenido cuando los controles son una serie
homogénea, como pestañas o chips de filtro.

**Cuándo destruye la tarea.** Cuando todo se colapsa en un único menú "⋯" y una operación
habitual pasa a costar dos toques cada vez. Y cuando los iconos sustituyen etiquetas que nadie
reconoce sin texto.

---

## Acciones

**Qué se rompe.** Un grupo de botones que en desktop se lee de un vistazo pasa a apilarse,
igualando el peso de todos o dejando una acción destructiva sola y protagonista.

**Qué se preserva.** La acción primaria visible y distinguible; la jerarquía entre primaria,
secundarias y destructiva.

**Estrategias.** Primaria visible y secundarias en menú · barra de acción fija al pie para la
primaria de la pantalla · acciones por fila movidas a un menú contextual o a la vista de detalle
· acciones masivas que aparecen solo al haber selección.

**Cuándo destruye la tarea.** Cuando una acción destructiva queda con el mismo peso —o más— que
la primaria por accidente de apilamiento. Y cuando una acción que se ejecuta decenas de veces al
día se manda al menú por ahorrar ancho.

---

## Grids

**Qué se rompe.** Las columnas se estrechan hasta que su contenido deja de ser legible o
comparable, mucho antes de que el layout "se rompa" técnicamente.

**Qué se preserva.** La relación entre los elementos: si la grilla existía para comparar, la
comparación; si existía para navegar, el escaneo.

**Estrategias.** Reducción escalonada de columnas guiada por el ancho mínimo útil de la celda ·
promoción de un elemento a ancho completo cuando domina · scroll horizontal contenido para
series homogéneas · agrupación de secundarios en un bloque compacto · reordenamiento por
prioridad.

**Cuándo destruye la tarea.** Cuando pasar a una columna convierte una comparación en una
secuencia de lecturas separadas. Si el usuario tenía que ver cuatro cosas a la vez y ahora las
ve de a una, la grilla no se adaptó: se eliminó.

---

## Tablas

**Qué se rompe.** El ancho total supera el viewport. La tabla empuja la página, se corta, o
alguien la convierte en cards y desaparece la comparación.

**Qué se preserva.** Los datos necesarios para identificar y decidir, las acciones por registro y
—cuando la tarea es comparar— la estructura tabular.

**Estrategias.** Ver la tabla de decisión en [`SKILL.md`](../SKILL.md). Al implementarla:

- **Scroll contenido**: el contenedor de la tabla desplaza, no la página. Compruébalo con el
  viewport más estrecho y con el contenido más largo, no con el ejemplo que cabe.
- **Columna clave fija**: fija la que identifica el registro; si la columna fija consume tanto
  espacio que el resto pierde ancho útil para comparar, la fijación estorba más de lo que ayuda.
- **Columnas prioritarias**: la selección se decide por la tarea —qué necesita el usuario para
  identificar la fila y decidir qué hacer con ella—, no por cuáles son más angostas.
- **Resumen → detalle**: la fila resumida sigue mostrando lo que permite elegir cuál abrir.
- **Cards**: cada card conserva identificación, los datos que se leen juntos y las acciones.

**Cuándo destruye la tarea.** Cards cuando el trabajo es comparar registros; ocultar columnas sin
darles otra vía de acceso; scroll que se propaga a la página entera; paginación agresiva que
impide ver el conjunto que había que revisar.

---

## Formularios

**Qué se rompe.** Una retícula de varias columnas se vuelve ilegible, los campos relacionados se
separan, las ayudas y los errores compiten con los campos, y el orden de teclado deja de
corresponder al visual.

**Qué se preserva.** Campos, obligatoriedad, validaciones, reglas y flujo. Las agrupaciones
semánticas: lo que pertenece junto se sigue leyendo junto.

**Estrategias.** Secuencia vertical respetando los grupos · campos cortos relacionados en pareja
cuando el ancho lo permite —día/mes, código/número— · ayudas contextuales bajo el campo en vez de
al lado · acciones del formulario fijas al pie en formularios largos · uso de los pasos que ya
existan, sin inventar un asistente nuevo.

**Cuándo destruye la tarea.** Cuando el reordenamiento visual rompe la correspondencia con el
orden de tabulación. Cuando un formulario largo pierde su resumen o su indicador de progreso.
Cuando dividir en pasos convierte una entrada rápida en un trámite.

---

## Dashboards

**Qué se rompe.** KPI, gráfico y tabla apilados producen una columna interminable donde nada
tiene prioridad y todo exige scroll.

**Qué se preserva.** La respuesta que el panel da de un vistazo, y el acceso al resto del
contenido.

**Estrategias.** Promoción de la métrica que responde la pregunta principal · KPI secundarios en
una fila compacta o con scroll contenido · gráfico dimensionado a su tarea en vez de a ancho
completo por defecto · tabla movida a una sección o vista propia · pestañas o secciones para
separar contexto de detalle.

**Cuándo destruye la tarea.** Cuando la comparación entre métricas era el punto y quedan
separadas por scroll. Cuando el panel de vigilancia —el que se mira cada mañana— exige recorrer
la pantalla entera para saber si algo va mal.

---

## Gráficos

**Qué se rompe.** Comprimir el ancho vuelve ilegibles las etiquetas, la leyenda ocupa más que el
gráfico, los puntos pierden separación y la interacción se hace impracticable.

**Qué se preserva.** La pregunta que el gráfico responde y el significado de lo que muestra.

**Estrategias.** Cambiar la proporción antes que el tamaño · mover la leyenda arriba o abajo, o
integrarla en las series · reducir la densidad de marcas del eje sin perder referencia · scroll
horizontal contenido para series temporales largas · separar contexto y gráfico · **reutilizar la
librería de gráficos del proyecto**, que casi siempre ya tiene opciones responsive.

**Cuándo destruye la tarea.** Cuando se eliminan series o datos solo porque no caben —salvo que
la tarea establezca una prioridad que lo justifique—. Y cuando se reconstruye el gráfico a mano
para hacerlo responsive: eso es reimplementar peor algo ya resuelto.

---

## Master / detail

**Qué se rompe.** Listado y detalle simultáneos dejan de caber; cada panel queda demasiado
angosto para servir.

**Qué se preserva.** La capacidad de recorrer el listado y de volver a él sin perder posición ni
filtros.

**Estrategias.** Navegación en dos pasos —listado → detalle— con retorno explícito · detalle en
sheet sobre el listado cuando la consulta es breve · navegación entre registros desde el propio
detalle, para no obligar a volver · conservación del scroll y del estado del listado al regresar.

**Cuándo destruye la tarea.** Cuando el trabajo consistía en revisar muchos registros seguidos y
cada uno ahora cuesta ir y volver perdiendo la posición. Ahí lo que falta no es el layout de dos
paneles: es la navegación entre registros dentro del detalle.

---

## Filtros

**Qué se rompe.** Un panel de filtros lateral o una fila de controles no caben, y los filtros
activos dejan de ser visibles.

**Qué se preserva.** Saber **qué filtros están aplicados** y poder quitarlos. Eso es tan
importante como poder aplicarlos.

**Estrategias.** Botón Filtros que abre un sheet, con contador de filtros activos · chips de
filtros aplicados visibles sobre los resultados · los uno o dos filtros más usados en línea y el
resto en el sheet · aplicación diferida con un botón de confirmar cuando cada cambio recarga.

**Cuándo destruye la tarea.** Cuando los filtros aplicados quedan invisibles dentro del overlay y
el usuario ve un conjunto de resultados sin entender por qué está incompleto.

---

## Búsqueda

**Qué se rompe.** El campo de búsqueda compite con la navegación y las acciones por el mismo
ancho, o desaparece detrás de un icono en una interfaz donde buscar es la operación central.

**Qué se preserva.** La proporción entre la importancia real de buscar en ese producto y el
espacio que se le da.

**Estrategias.** Icono que expande a campo completo · campo persistente bajo el header cuando la
búsqueda es la entrada principal · búsqueda dentro de la vista en lugar de global · sugerencias
en pantalla completa en pantallas estrechas.

**Cuándo destruye la tarea.** Cuando en un producto donde todo el mundo empieza buscando, la
búsqueda pasa a costar un toque adicional para ganar el ancho de un botón que se usa poco.

---

## Modales, drawers y sheets

**Qué se rompe.** Un modal dimensionado para desktop excede el viewport; el contenido se corta,
las acciones quedan fuera de alcance o el fondo desplaza en lugar del overlay.

**Qué se preserva.** Que las acciones de confirmar y cancelar siempre sean alcanzables, y que se
entienda sobre qué se está actuando.

**Estrategias.** Sheet a ancho completo desde el borde inferior · pantalla completa para
contenido extenso o formularios · cabecera y acciones fijas con el cuerpo desplazable ·
conversión a página propia cuando el contenido justifica una URL.

**Cuándo destruye la tarea.** Cuando el overlay tapa el contexto que hacía falta para decidir, y
el usuario tiene que cerrarlo para recordar sobre qué estaba confirmando.

---

## Imágenes y media

**Qué se rompe.** Una imagen dimensionada para desktop ocupa casi todo el viewport, empuja el
mensaje y el CTA fuera de la primera pantalla, o se recorta perdiendo su punto focal.

**Qué se preserva.** La intención visual y el carácter de marca. La proporción puede cambiar; la
presencia de la imagen no es negociable solo porque estorba.

**Estrategias.** Cambio de aspect ratio por viewport · punto focal declarado para que el crop
conserve lo importante · reordenamiento de imagen y texto · texto superpuesto que pasa a bloque
adyacente cuando el contraste ya no aguanta · escala reducida conservando el gesto.

**Cuándo destruye la tarea.** Reducir toda imagen grande a una miniatura decorativa, o conservar
un hero enorme en mobile solo porque así funciona en desktop.

En un hero, **conserva la prioridad aprobada**. Si mensaje y acción son el objetivo dominante,
deben seguir siendo alcanzables y visibles sin que la imagen los desplace; si la referencia hace
de la imagen el elemento principal —editorial, inmobiliario, producto, lujo—, adapta crop y
proporción sin quitarle ese rol. En ningún caso **eliminarla es adaptarla**.

---

## Sticky y fixed

**Qué se rompe.** Header fijo, barra de acciones fija y teclado abierto suman altura sobre un
viewport bajo, hasta que el contenido útil es una franja.

**Qué se preserva.** Que lo fijo siga justificando el espacio que ocupa en el tamaño en el que
está.

**Estrategias.** Un solo elemento fijo por eje · header que se retrae al bajar y reaparece al
subir · acciones fijas solo mientras hacen falta · uso de las unidades de viewport dinámicas del
proyecto para no pelear con las barras del navegador.

**Cuándo destruye la tarea.** Cuando dos o tres elementos fijos dejan al contenido menos de la
mitad de la pantalla, o cuando la barra fija tapa el último campo de un formulario y nadie lo
nota porque solo se probó con el formulario corto.

---

## Empty, loading y error

**Qué se rompe.** Los estados se diseñaron y se probaron en desktop. En pantallas estrechas el
esqueleto de carga no corresponde al layout adaptado, el estado vacío ocupa una altura absurda o
el mensaje de error empuja el contenido.

**Qué se preserva.** Que cada estado siga explicando qué pasa y qué se puede hacer, y que la
acción de salida del estado vacío sea alcanzable.

**Estrategias.** Esqueletos que reflejan la composición **de ese tamaño**, no la de desktop ·
estados vacíos compactos sin ilustración desproporcionada · errores en línea junto a lo que
falló, en vez de un bloque que desplaza la vista.

**Cuándo destruye la tarea.** Un esqueleto de tres columnas sobre un layout de una: anuncia una
composición que no va a llegar y produce un salto al cargar.

---

## Contenido extremo

**Qué se rompe.** Lo que cabía con el dato de ejemplo deja de caber con el real: nombres muy
largos, cifras grandes, listas enormes, textos traducidos, ausencia de imagen.

**Qué se preserva.** Que el layout no se rompa y que la información siga siendo recuperable
—truncar es válido si hay forma de ver el valor completo.

**Estrategias.** Truncado con acceso al valor completo · ajuste en dos líneas para lo que se
identifica leyendo · anchos mínimos y máximos en lugar de fijos · formato compacto para cifras
grandes conservando el valor exacto a la vista o a un toque · virtualización o paginación para
listas muy largas, con la del proyecto si ya existe.

**Cuándo destruye la tarea.** Truncar el único dato que distingue dos registros entre sí. Si dos
filas se leen igual después de truncar, el truncado eligió mal qué recortar.
