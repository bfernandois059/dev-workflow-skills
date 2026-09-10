# Component Boundaries

Material de consulta de `component-architecture`. Cada sección responde cuatro cosas: **qué
evidencia justifica abstraer**, **qué debe compartir el componente**, **qué debe permanecer en el
consumidor** y **qué señales indican que la abstracción empeoró el código**.

> **Consulta solo las secciones relacionadas con el patrón que tienes delante.** No es una
> doctrina general de React ni un manual de clean code: es material para decidir un límite
> concreto. Ninguna forma listada aquí es correcta por defecto, y una preferencia estilística no
> se convierte en regla por aparecer en este archivo.

Lo que ya está en [`SKILL.md`](../SKILL.md) no se repite: frontera con las demás skills,
precedencia de fuentes, responsabilidad antes que repetición, el tamaño como no-criterio,
variantes contra flags de página, preservación visual y funcional, y formato de entrega.

| Sección | Cuándo abrirla |
|---|---|
| [Responsabilidad y cohesión](#responsabilidad-y-cohesión) | No está claro qué comparten realmente dos bloques |
| [Repetición o coincidencia](#repetición-o-coincidencia) | Se repite algo y hay que decidir si importa |
| [Extracción](#extracción) | Un archivo grande o un bloque candidato a salir |
| [Composición](#composición) | La variación empieza a resolverse con props |
| [Variantes](#variantes) | Diferencias legítimas que hay que modelar |
| [Slots y children](#slots-y-children) | El contenido central varía y el marco no |
| [Controlled y uncontrolled](#controlled-y-uncontrolled) | El componente compartido tiene estado |
| [Presentación y comportamiento](#presentación-y-comportamiento) | Se ven iguales pero no hacen lo mismo |
| [Local, feature o global](#local-feature-o-global) | Hay que decidir dónde vive el componente |
| [Wrappers sobre primitives](#wrappers-sobre-primitives) | El proyecto ya tiene una base adecuada |
| [Tablas](#tablas) | Varias tablas resueltas por separado |
| [Formularios](#formularios) | Campos, validación y layout repetidos |
| [Dialogs y overlays](#dialogs-y-overlays) | Modales, drawers y sheets hechos a mano |
| [Sistemas operacionales](#sistemas-operacionales) | CRM, intranet, panel de administración |
| [Patrones de marketing](#patrones-de-marketing) | Hero, secciones y bloques de landing |
| [Señales de mega-componente](#señales-de-mega-componente) | La API creció y ya nadie la entiende |
| [Señales de microcomponentización](#señales-de-microcomponentización) | Muchos archivos triviales |
| [Migración de consumidores](#migración-de-consumidores) | Hay que mover las pantallas al patrón |
| [Eliminación segura de duplicados](#eliminación-segura-de-duplicados) | Queda código reemplazado |

---

## Responsabilidad y cohesión

**Qué evidencia justifica abstraer.** Las implementaciones representan el mismo concepto del
producto y responden a la misma pregunta —"así se presenta un cliente", "así se encabeza una
página"—. La prueba práctica: si esa decisión cambia, todas deben cambiar juntas.

**Qué debe compartir el componente.** Exactamente la decisión común: la estructura, el
tratamiento y el contrato que define el concepto. Un componente cohesivo se puede describir en
una frase sin conjunciones.

**Qué debe permanecer en el consumidor.** El contenido, los datos, la conexión con el dominio y
las diferencias que pertenecen a esa pantalla y no al concepto.

**Señales de que empeoró.** El nombre necesita "y" para explicarse (`CardAndFilters`). Dos
consumidores piden cambios que se contradicen. Cada nueva pantalla obliga a tocar el componente
compartido en vez de usarlo.

---

## Repetición o coincidencia

**Qué evidencia justifica abstraer.** Que la estructura coincida **porque cumple la misma
función**. Dos bloques con el mismo `flex` y el mismo `gap` no comparten nada si uno muestra un
resumen de facturación y el otro una lista de adjuntos.

**Qué debe compartir el componente.** Solo la parte que evoluciona junta. A veces es un primitive
inferior —`Surface`, `Stack`, `Field`— y no el bloque entero.

**Qué debe permanecer en el consumidor.** Todo lo que coincide hoy por casualidad. Congelar una
coincidencia crea un acoplamiento que después obliga a añadir flags para deshacerlo.

**Señales de que empeoró.** El primer cambio posterior necesita una prop nueva para separar
consumidores que "eran iguales". Aparecen `if` sobre el tipo de página dentro del componente.

---

## Extracción

**Qué evidencia justifica abstraer.** Una responsabilidad visual clara, un comportamiento
independiente, un ciclo de estado propio o una frontera conceptual reconocible dentro de un
archivo mayor. **Nunca la cantidad de líneas.**

**Qué debe compartir el componente.** La pieza extraída completa: su marcado, su estado y su
contrato. Una extracción que deja la mitad del estado en el padre y la otra mitad dentro produce
dos lugares donde antes había uno.

**Qué debe permanecer en el consumidor.** La orquestación, la obtención de datos y la
coordinación entre piezas, salvo que la pieza extraída sea justamente esa.

**Señales de que empeoró.** El padre y el hijo se pasan diez props para reconstruir lo que antes
era una función local. Seguir el flujo exige abrir tres archivos. Un bloque cohesivo quedó
partido por la mitad para bajar el tamaño del archivo.

---

## Composición

**Qué evidencia justifica abstraer.** Lo compartido es el **marco** —contenedor, header, spacing,
tratamiento, zona de acciones— y el contenido central varía entre consumidores.

**Qué debe compartir el componente.** El marco y sus reglas. Los subcomponentes exponen las zonas
donde el consumidor pone lo suyo.

**Qué debe permanecer en el consumidor.** El contenido de cada zona y las decisiones que dependen
de su dominio.

**Señales de que empeoró.** La composición exige memorizar un orden implícito de subcomponentes
que nada verifica. Cada zona termina aceptando props de configuración y se pierde la ventaja de
componer. Una variación pequeña y controlada —dos tamaños, un tono— se convirtió en cinco
subcomponentes donde una prop bastaba.

---

## Variantes

**Qué evidencia justifica abstraer.** Las diferencias son **formas legítimas conocidas por el
sistema**: densidad, tono, tamaño, énfasis, layout. El sistema visual o la referencia aprobada las
nombra, o pueden nombrarse sin mencionar una página.

**Qué debe compartir el componente.** El conjunto cerrado de variantes y su traducción a estilo.
Una variante es un valor semántico —`tone="critical"`—, no una lista de utilidades.

**Qué debe permanecer en el consumidor.** La elección de la variante, no su definición.

**Señales de que empeoró.** La variante se llama como el consumidor (`variant="dashboard"`). Las
combinaciones válidas ya no caben en la cabeza y algunas producen resultados absurdos. Se agrega
una variante por cada pantalla nueva: eso ya no es un conjunto cerrado.

> Los boolean props siguen siendo correctos para estados genuinamente binarios: `disabled`,
> `required`, `loading`, `selected`. El problema no es el tipo, es codificar excepciones
> estructurales con ellos.

---

## Slots y children

**Qué evidencia justifica abstraer.** El consumidor necesita insertar marcado arbitrario —un
badge propio, una acción específica, un fragmento de contenido— en un punto conocido del patrón.

**Qué debe compartir el componente.** La posición, el espaciado y el tratamiento del slot; es
decir, dónde va y cómo se relaciona con el resto.

**Qué debe permanecer en el consumidor.** Qué se pone dentro.

**Señales de que empeoró.** Hay tantos slots que el componente ya no decide nada y solo aporta un
`div`. El mismo contenido se pasa a veces por slot y a veces por prop, sin criterio. Un slot
opcional cambia el layout de formas que nadie previó.

---

## Controlled y uncontrolled

**Qué evidencia justifica abstraer.** El patrón tiene estado propio —abierto/cerrado,
seleccionado, expandido, pestaña activa— y varios consumidores lo repiten igual.

**Qué debe compartir el componente.** El comportamiento y sus transiciones, con un contrato
explícito: o gestiona su estado internamente, o lo recibe con su `onChange`, o soporta ambos con
la misma semántica que ya use el proyecto.

**Qué debe permanecer en el consumidor.** La sincronización con URL, store, formulario o servidor
cuando ese estado pertenece a la aplicación y no al componente.

**Señales de que empeoró.** El componente tiene estado interno **y** una prop de valor que no se
sincronizan. Los consumidores duplican el estado para poder leerlo. Un `useEffect` copia una prop
a estado interno en cada render.

---

## Presentación y comportamiento

**Qué evidencia justifica abstraer.** Está demostrado **qué** comparten: presentación, o
comportamiento, o ambos. Verse igual no prueba que hagan lo mismo, y hacer lo mismo no obliga a
verse igual.

**Qué debe compartir el componente.** Solo la capa demostrada. Cuando coinciden en presentación
pero no en lógica, lo compartido es un componente de presentación que recibe lo que necesita
resuelto desde fuera.

**Qué debe permanecer en el consumidor.** Permisos, reglas comerciales, consultas, mutaciones y
cualquier decisión que pertenezca a otra capa. El componente recibe `canEdit`, `status` o
`actions`; no los calcula.

**Señales de que empeoró.** El componente genérico importa hooks de dominio o consulta datos
propios. Aparece lógica de rol dentro de un componente presentacional. Un cambio de regla
comercial obliga a tocar un componente que se usa en pantallas que esa regla no afecta.

---

## Local, feature o global

**Qué evidencia justifica abstraer.** El concepto cruza realmente la frontera donde vas a
ponerlo. Un patrón usado por tres pantallas de la misma feature es un componente de esa feature.

**Qué debe compartir el componente.** Lo que corresponde a su nivel: un primitive global no sabe
de entidades del producto; un componente de feature sí puede saberlas.

**Qué debe permanecer en el consumidor.** El vocabulario de dominio que no pertenece al nivel
elegido.

**Señales de que empeoró.** `components/shared/` contiene piezas que usa una sola feature. Un
primitive global importa tipos de una feature. La consolidación creó una taxonomía de carpetas
nueva que convive con la anterior sin reemplazarla.

---

## Wrappers sobre primitives

**Qué evidencia justifica abstraer.** El proyecto ya tiene una base competente —shadcn, Radix,
Headless UI, una librería de tablas o formularios, primitives internos— y varias pantallas la
usan de formas distintas, o la esquivaron reimplementándola.

**Qué debe compartir el componente.** La **decisión de producto** sobre el primitive: qué tamaño,
qué tono, qué estructura de acciones, qué copy por defecto, qué comportamiento estándar.

**Qué debe permanecer en el consumidor.** El contenido, las acciones específicas y los casos que
el wrapper no debe conocer.

**Señales de que empeoró.** El wrapper reimplementa focus trap, portal, navegación por teclado,
dismiss, sorting o filtering en vez de delegarlos. Bloquea capacidades del primitive que algún
consumidor necesita. Añade una capa que no decide nada y solo reenvía props.

---

## Tablas

**Qué evidencia justifica abstraer.** Varias tablas repiten las mismas decisiones de producto:
tratamiento de cabecera, densidad, estados vacío y de carga, paginación, alineación por tipo de
dato, columna de acciones.

**Qué debe compartir el componente.** Esas decisiones y la integración con la librería de tablas
que el proyecto use.

**Qué debe permanecer en el consumidor.** La definición de columnas, los datos, el orden y las
acciones por fila. Cada tabla muestra otra cosa: eso no se centraliza.

**Señales de que empeoró.** El componente acepta una configuración tan expresiva que
reimplementar la tabla resulta más corto. Las columnas se declaran con strings que nadie tipa. El
comportamiento responsive decidido por `adaptive-layout` se perdió al unificar.

---

## Formularios

**Qué evidencia justifica abstraer.** Se repite la estructura de campo —label, control, ayuda,
error, estados— o el layout del formulario, no las reglas.

**Qué debe compartir el componente.** El `FormField` y su tratamiento, la asociación accesible
entre label, control, ayuda y error, y la disposición.

**Qué debe permanecer en el consumidor.** Esquema, validaciones, obligatoriedad, valores por
defecto, envío y flujo. **Consolidar presentación no autoriza a cambiar reglas de validación.**

**Señales de que empeoró.** El componente compartido decide qué campos son obligatorios. La
validación quedó repartida entre el campo y el formulario. Se perdió la relación
`label`/`aria-describedby` que cada implementación sí tenía.

---

## Dialogs y overlays

**Qué evidencia justifica abstraer.** Hay varios overlays hechos a mano y el proyecto ya tiene un
primitive accesible, o las decisiones de producto —tamaños, zona de acciones, tratamiento del
título, confirmaciones destructivas— se repiten.

**Qué debe compartir el componente.** El primitive y esas decisiones: estructura de header,
cuerpo y acciones, y el patrón de confirmación cuando existe.

**Qué debe permanecer en el consumidor.** El contenido, las acciones concretas y su lógica.

**Señales de que empeoró.** El wrapper impide componer un caso legítimo y obliga a saltárselo. El
foco, el `Escape` o el scroll lock dejaron de funcionar en algún consumidor. Un diálogo de
confirmación genérico terminó ejecutando lógica de negocio que era del llamador.

---

## Sistemas operacionales

**Qué evidencia justifica abstraer.** En un CRM, una intranet o un panel de administración se
repiten patrones densos con comportamiento real: filas con acciones, filtros, selección múltiple,
estados por registro, cabeceras de sección con acciones.

**Qué debe compartir el componente.** La densidad, el ritmo de escaneo, la posición de las
acciones frecuentes y el tratamiento de estados operacionales.

**Qué debe permanecer en el consumidor.** Los permisos, las capacidades por rol y la información
específica de cada entidad.

**Señales de que empeoró.** La consolidación redujo información que el operador usaba. Una acción
frecuente pasó a un menú y agregó fricción diaria. El componente compartido decide qué ve cada
rol.

---

## Patrones de marketing

**Qué evidencia justifica abstraer.** Las secciones de una landing comparten un **ritmo** —ancho
de contenedor, espaciado entre secciones, escala de encabezado, tratamiento de fondo— más que un
bloque.

**Qué debe compartir el componente.** Ese ritmo: `Section`, `Container`, la escala tipográfica y
la relación entre título, bajada y acción.

**Qué debe permanecer en el consumidor.** La composición de cada sección. Un hero, una prueba
social y una comparativa no son el mismo componente con props distintas.

**Señales de que empeoró.** Todas las secciones pasaron a ser el mismo bloque configurable y la
página perdió variedad —el fallo que `interface-craft` llama diseño genérico—. La consolidación
cambió el tratamiento aprobado de un hero "de paso".

---

## Señales de mega-componente

**Qué evidencia justifica abstraer.** Ninguna: aquí la abstracción **ya existe** y hay que
decidir si se divide, se convierte en composición o se separa en responsabilidades distintas.

**Qué observar.** Booleanos que se combinan entre sí sin combinaciones válidas definidas · props
que nombran páginas o roles · ramas `if` sobre el tipo de consumidor · props que solo usa un
consumidor · una API más larga que cualquiera de las implementaciones que reemplazó · cambios que
obligan a probar pantallas sin relación entre sí.

**Cómo salir.** Separa por responsabilidad, no por tamaño: extrae la capa realmente común
—primitive o marco—, modela como variantes lo que es semántico, pasa a composición lo que es
estructural, y devuelve a componentes separados lo que nunca perteneció junto.

**Señales de que empeoró.** La división produjo dos mega-componentes en vez de uno. Se agregó una
prop más para resolver el caso nuevo mientras se discutía cómo dividirlo.

---

## Señales de microcomponentización

**Qué evidencia justifica abstraer.** Tampoco aquí: la decisión es si **reincorporar**.

**Qué observar.** Componentes que envuelven una etiqueta sin aportar semántica · archivos que
reenvían las mismas props sin transformarlas · nombres que describen posición (`TopLeftBox`,
`RightSection`) · componentes de un solo uso sin estado ni contrato · árboles donde entender una
pantalla exige abrir muchos archivos triviales.

**Qué conservar.** Todo componente con un contrato real: estado propio, reutilización efectiva,
semántica de dominio, accesibilidad o una frontera que se cruza en más de un lugar. **Un solo uso
no es motivo suficiente para eliminarlo** si encapsula una responsabilidad independiente.

**Señales de que empeoró.** La reincorporación produjo un archivo ilegible. Se perdió una
frontera útil y ahora dos responsabilidades comparten estado sin necesidad. "Menos archivos" se
volvió el objetivo.

---

## Migración de consumidores

**Qué evidencia justifica abstraer.** El componente destino ya existe o acaba de crearse y
representa la misma responsabilidad que la copia local.

**Qué debe compartir el componente.** Lo que el consumidor deja de declarar por su cuenta.

**Qué debe permanecer en el consumidor.** Las diferencias legítimas, expresadas como variante,
composición o contenido — **nunca borradas por parecerse**.

**Cómo migrar.** Un consumidor a la vez, comparando su render antes y después. Antes de cerrar,
compara diferencias funcionales reales: acciones, eventos, navegación, estados, accesibilidad y
comportamiento responsive. Si una diferencia no cabe como variante y no es deriva, es evidencia
de que ese consumidor no pertenece al mismo componente.

**Señales de que empeoró.** Una pantalla perdió una acción, un estado o un dato en la migración.
El consumidor necesitó una prop inventada para volver a verse igual. La migración quedó a medias
y ahora conviven dos patrones sin plan.

---

## Eliminación segura de duplicados

**Qué evidencia justifica abstraer.** Aquí la pregunta es de borrado, no de abstracción: todos los
consumidores de la implementación antigua están migrados y no quedan otros usos.

**Qué comprobar antes.** Usos reales en el repositorio, incluidos imports indirectos,
reexportaciones desde archivos índice, referencias dinámicas, rutas y convenciones del framework,
tests y stories. **Sin import** no equivale a **sin uso**.

**Qué eliminar.** La implementación reemplazada, sus imports muertos y los estilos exclusivamente
suyos que quedaron sin uso.

**Qué no eliminar.** Código muerto no relacionado con esta consolidación: eso es `tech-cleanup`.
Tampoco implementaciones que "parecen" reemplazadas sin haberlo comprobado.

**Señales de que empeoró.** Quedaron `OldCard`, `NewCard` y `SharedCard` conviviendo. Se borró
algo que un test, una ruta o una referencia dinámica seguía usando. Se aprovechó el PR para
limpiar media aplicación.
