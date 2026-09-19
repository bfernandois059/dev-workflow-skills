# Visual Review Criteria

Criterios de consulta de `visual-consistency`. Cada sección dice **qué mirar**, **cómo distinguir
una desviación real de una diferencia justificada** y **qué señales delatan deriva**.

> **Consulta únicamente las secciones relacionadas con los posibles defectos que ya observaste.**
> Esto es una guía perceptual, no una checklist obligatoria. Recorrerla entera convierte una
> revisión de diez minutos en la auditoría de cumplimiento que esta skill existe para evitar.

> **Relaciones antes que mediciones.**
> *Visual consistency is consistency of intent and role, not mechanical equality of values.*
> *A numerical difference matters when it creates, hides or contradicts a perceptual relationship.*
> Un desvío numérico o de token (ej. 23px vs 24px) importa únicamente si genera, oculta o contradice una relación visible. Si la relación perceptual se mantiene intacta, una variación microscópica casi nunca es un defecto por sí misma.

> **Lentes perceptuales acotados y sin recitar teoría.**
> Utiliza como apoyo interno únicamente: **proximidad**, **semejanza**, **región común** y **énfasis perceptual**. No importes leyes de interacción o modelos mentales ajenos (Hick, Fitts, Tesler, memoria de trabajo, journeys). Al redactar la salida al usuario, describe siempre el defecto visible y la relación que se rompe, sin recitar nombres de leyes ni marcos teóricos.

Lo que ya está en [`SKILL.md`](../SKILL.md) no se repite: precedencia de fuentes, obligación de
mirar el render, orden macro→micro, priorización, formato de entrega y fronteras entre skills.

| Área | Cuándo abrirla |
|---|---|
| [Jerarquía](#jerarquía) | Todo pesa igual; el ojo no sabe dónde ir |
| [Composición](#composición) | Ordenada pero plana; parece una plantilla |
| [Tipografía](#tipografía) | Tamaños vecinos, pesos que cambian, títulos sin distancia |
| [Spacing](#spacing) | Los grupos no se leen como grupos; valores sueltos |
| [Layout y alineación](#layout-y-alineación) | Bordes que no coinciden; anchos que bailan |
| [Color](#color) | Grises nuevos; roles iguales con tonos distintos |
| [Densidad](#densidad) | "Se ve cargado" / "se ve vacío" |
| [Superficies y profundidad](#superficies-y-profundidad) | Cards, bordes, sombras, radius |
| [Consistencia entre componentes](#consistencia-entre-componentes) | El mismo patrón resuelto de dos maneras |
| [Comparación con una referencia](#comparación-con-una-referencia) | Hay mockup, captura o `ui-system.md` |
| [Comparación entre pantallas](#comparación-entre-pantallas) | Varias vistas que deberían parecer del mismo sistema |
| [Señales de diseño genérico](#señales-de-diseño-genérico) | Sospecha de fórmula por defecto |

---

## Jerarquía

**Cómo mirar**

1. **Desenfoca.** Entrecierra los ojos o mira la pantalla en miniatura. Lo que sigue destacando
   es la jerarquía real, no la que dice el código.
2. **Nombra el ancla visual.** ¿A dónde se dirige el ojo en el primer tercio de segundo? ¿Coincide
   con lo más importante de la pantalla para la tarea del usuario? Si el ojo va a un badge de
   color decorativo, a una ilustración o a un botón secundario, el peso visual está distorsionado.
3. **Clasifica en tres niveles.** Primario, secundario, terciario. Si muchos bloques compiten
   como primarios, no hay jerarquía: hay competencia visual y fatiga cognitiva.
4. **Quita el color.** En escala de grises, ¿sigue percibiéndose qué es prioritario? Si desaparece,
   la jerarquía estaba sostenida exclusivamente por color y fallará bajo condiciones reales.
5. **Comprueba el énfasis como recurso escaso.** El tratamiento visual distintivo (color de acento,
   badge, sombra pronunciada, tamaño de display) solo funciona cuando la mayoría de los elementos
   se mantienen neutros. Si todo intenta destacar, nada destaca. Sin embargo, **no impongas la
   regla dogmática de que solo un elemento puede destacar**: en situaciones reales pueden existir
   legítimamente dos alertas críticas simultáneas o varias métricas fuera de rango. La pregunta es:
   *¿El tratamiento excepcional coincide con lo que realmente demanda atención en este contexto?*

**Diferencia justificada**: una vista de comparación donde varios elementos *deben* pesar igual
—una tabla de datos, una grilla de resultados equivalentes— no es una jerarquía rota. La pregunta
es si la igualdad responde a la naturaleza del contenido o a la falta de una decisión de diseño.

**Señales de deriva**:
- Dos o tres acciones primarias (botones de acento) compitiendo en el mismo encabezado o sección;
- Metadata secundaria (fechas, IDs, estados neutrales) con el mismo tamaño, contraste o peso que el dato central;
- Jerarquía construida únicamente subiendo micro-niveles de `font-weight` o agregando bordes;
- Pérdida de intención de diseño: un KPI dominante en el mockup que en la implementación quedó diluido en una fila de cuatro tarjetas idénticas;
- El encabezado de la página o una barra de navegación robando más protagonismo visual que el contenido principal de la tarea.

---

## Composición

**Cómo mirar**

1. **Dibuja los bloques como siluetas**, sin texto. ¿Esa distribución dice algo sobre lo que
   contiene y la tarea del producto, o serviría exactamente igual para cualquier otra pantalla genérica?
2. **Contenido dominante.** ¿Hay un elemento estructural que merece gobernar la vista —una tabla
   operacional densa, un gráfico comparativo, un formulario principal— y quedó atrapado en una
   grilla simétrica de elementos iguales?
3. **Asimetría justificada vs simetría forzada.** Una distribución asimétrica guiada por el peso
   del contenido suele reflejar intención; forzar columnas idénticas cuando el contenido es dispar
   rompe el ritmo y aplana la jerarquía.
4. **Proximidad antes que contenedores.** Pregúntate: *¿La cercanía física y la alineación ya
   agrupan estos elementos con suficiente claridad?* Si la respuesta es afirmativa, una card o panel
   adicional añade ruido visual y profundidad innecesaria.
5. **Cuenta las superficies.** ¿Cada bloque menor tiene su propia card, borde o fondo? Eso delata
   agrupación suplida con decoración superficial en lugar de estructura.

**Señales de deriva**:
- Estructura predecible de plantilla —badge → título → párrafo → dos botones → tres tarjetas simétricas— aplicada sin justificación funcional;
- Superficies o cards anidadas dentro de otras cards sin que el contenedor interior represente una unidad interactiva autónoma o un cambio de contexto;
- Grilla estricta donde elementos de importancia radicalmente distinta ocupan exactamente el mismo ancho y alto;
- Falta de anclaje visual: la vista carece de un bloque dominante que guíe la lectura.

---

## Tipografía

**Cómo mirar**

1. **Lista los tamaños en uso y agrúpalos por rol, no por valor.** `PageTitle`, `SectionHeading`,
   `Body`, `Meta`, `ActionLabel`. Dos tamaños o pesos distintos para el mismo rol son deriva;
   roles distintos pueden y deben usar soluciones tipográficas distintas.
2. **Distancia perceptible entre niveles.** `H1`, `H2` y `H3` deben distinguirse a simple vista.
   Si hay que medir píxeles para notar el salto, los niveles no comunican jerarquía.
3. **Tamaños vecinos.** Valores muy próximos (14, 15, 16px) conviviendo en el mismo contexto casi
   nunca representan roles intencionales: son accidentes de maquetación que ensucian el sistema.
4. **Pesos por función.** La metadata con peso excesivo (`font-semibold`) compite con el dato; el
   texto secundario demasiado débil (`font-light` o contraste insuficiente) deja de leerse.
5. **Line-height e interlineado según rol.** Títulos compactos para evitar que se desarmen al hacer
   wrap; texto corrido con aire suficiente para guiar la lectura.
6. **Ancho de línea.** Entre 45 y 75 caracteres como rango orientativo; lo que se juzga es la
   comodidad visual de la lectura en pantalla, no el conteo de caracteres.

**Diferencia justificada por rol**: una escala más compacta en una tabla operacional densa o en un
sidebar es legítima si responde a su función y el sistema la contempla. No reportes inconsistencia
solo porque un título de tabla use `14px` mientras el título de sección use `20px`.

**Señales de deriva**:
- Micro-ajustes cosméticos (`font-medium` a `font-semibold` o de `16px` a `18px`) para disimular una jerarquía que no está resuelta estructuralmente;
- El mismo rol tipográfico variando de tamaño o peso entre pantallas del mismo tipo;
- Título con line-height de párrafo que separa las líneas como si fueran bloques independientes.

---

## Spacing

El spacing expresa **relaciones de proximidad**: lo que está cerca pertenece conceptualmente junto;
lo que está lejos pertenece a otro grupo o sección. Se revisa por **relación perceptual**, no por
comparación numérica aislada.

> *A numerical difference matters when it creates, hides or contradicts a perceptual relationship.*

**Cómo mirar**

1. **¿Los grupos se perciben como grupos?** Verifica la regla relacional:
   `distancia dentro del grupo < distancia entre grupos < distancia entre secciones`.
   Si el espacio entre un label y su valor es igual al espacio entre ese valor y el campo siguiente,
   la agrupación se lee cruzada y ambigua, aunque ambos usen un token válido del sistema.
2. **Diferencias numéricas inocuas vs destructivas.** Dos cards con padding interno de `23px` y
   `24px` pueden no generar ningún problema visual visible. En cambio, separar un título de su
   párrafo por `24px` y de la sección siguiente por `24px` destruye por completo la relación de
   bloque.
3. **Espacio uniforme como defecto.** Si todas las capas de la pantalla usan exactamente el mismo
   gap (ej. `gap-6` en todo contenedor), el espaciado deja de comunicar estructura y solo separa
   mecánicamente.
4. **Valores arbitrarios desconectados.** `gap-[22px]` conviviendo con la escala estándar suele ser
   un parche local que enmascara una composición débil.

**Diferencia justificada**: una densidad más compacta en un formulario denso o tabla operacional es
completamente válida frente a un layout de presentación. La regla es que **el mismo tipo de relación
se resuelva de forma consistente**, no que toda la aplicación comparta el mismo valor en píxeles.

**Señales de deriva**:
- Agrupación cruzada: labels más cercanos al control inferior que a su propio campo;
- Padding interno excesivo en cards pequeñas que estrangula el contenido útil;
- Padding o márgenes inconsistentes entre componentes con el mismo rol en vistas paralelas.

---

## Layout y alineación

**Cómo mirar**

1. **Alineación óptica sobre igualdad matemática.**
   > *If mathematically aligned looks visually misaligned, the rendered result wins.*
   Iconos asimétricos (ej. el triángulo de un botón "Play"), comillas decorativas o texto en
   mayúsculas suelen requerir una compensación visual (offset de 1–2px) para *verse* alineados. Lo
   que se juzga es lo que se percibe en pantalla, nunca las coordenadas en el inspector.
   **Nunca inventes un defecto de alineación desde el código sin ver el render.**
2. **Ejes verticales dominantes.** Traza con la mirada los bordes izquierdos y derechos de la vista.
   ¿Los elementos que deberían compartir eje —encabezados, filtros, tablas, totales— descansan
   sobre la misma línea de referencia?
3. **Ancho del container.** Verifica si secciones hermanas o vistas equivalentes respetan el mismo
   ancho máximo de contenido o si saltan arbitrariamente entre vistas.
4. **Alineación por tipo de dato.** En tablas y listas: texto a la izquierda, importes y cantidades
   alineados a la derecha (o por el separador decimal), estados centrados o a la izquierda según su
   formato.

**Diferencia justificada**: un elemento con sangría visual deliberada para indicar subordinación o
jerarquía secundaria (ej. filas anidadas) no es un desalineado.

**Señales de deriva**:
- Iconos o badges descentrados ópticamente respecto a su texto adyacente por aplicar centrado matemático rígido sin compensación;
- Dos secciones contiguas con containers de ancho dispar sin motivo funcional;
- Columnas de datos numéricos alineadas a la izquierda que impiden comparar magnitudes de un vistazo.

---

## Color

**Cómo mirar**

1. **Agrupa por rol, no por tono.** Fondo, superficie, borde, texto principal, texto secundario,
   acento, estados. Dos tonos distintos para el mismo rol son una desviación.
2. **Grises nuevos.** Si dos grises son prácticamente indistinguibles en pantalla y cumplen el
   mismo rol, no son dos niveles del sistema: es uno mal copiado. El criterio es perceptual y
   funcional: ¿alguien nota la diferencia, y significa algo distinto?
3. **Contraste.** Repórtalo cuando sea **evidente a la vista** o cuando puedas **medirlo con las
   herramientas del entorno**. No estimes ratios de memoria ni conviertas esto en una auditoría
   de accesibilidad.
4. **Color de marca en el rol correcto.** El acento pierde su función cuando aparece en
   decoración, en bordes neutros o en cada elemento de una lista.
5. **Estados solo por color.** Si el único indicador de éxito, error o selección es el tono, el
   estado desaparece en escala de grises y para parte de los usuarios.

**No inventes paleta.** La corrección propuesta se enuncia por **rol visual** —"usa el color de
texto secundario del sistema"—, no como "usa otro azul".

---

## Densidad

**Cómo mirar**

1. **Identifica el tipo de producto** antes de juzgar. Un sistema operacional y una landing
   tienen densidades correctas distintas.
2. **¿Cuánto trabajo cabe sin desplazarse?** En una herramienta de uso intensivo, ver poco por
   pantalla es un defecto, no limpieza. Cuántos elementos son "pocos" depende de si la tarea es
   leer uno o comparar varios.
3. **"Se ve cargado" casi nunca significa "sobra información".** Revisa en orden: jerarquía →
   agrupación → disclosure → densidad. Eliminar contenido es la última opción y normalmente es
   una decisión de producto, no de revisión visual.
4. **En un sitio comercial**, la falla simétrica: todo denso, plano y sin ritmo, sin ningún
   momento de descanso.

---

## Superficies y profundidad

**Cómo mirar**

1. **Proximidad vs superficies.** Pregúntate: *¿La proximidad y la alineación ya comunican
   suficientemente la relación?* Si la respuesta es sí, agregar una card, borde, fondo o sombra
   suele introducir ruido visual, profundidad ficticia y jerarquías inexistentes.
2. **Superficie justificada por límite real.** Una card o panel se justifica cuando su límite
   comunica una función concreta:
   - una unidad interactiva autónoma (ej. item clickeable);
   - un cambio de elevación o contexto funcional (ej. un popover o panel de configuración);
   - un estado activo, seleccionado o diferenciado.
3. **No concluyas "card = defecto".** El hallazgo no es que exista una card; el hallazgo es qué
   relación quedó distorsionada, asfixiada o duplicada por el contenedor innecesario.
4. **Cards dentro de cards.** Anidar contenedores decorativos casi siempre es agrupar dos veces lo
   mismo sin agregar claridad.
5. **Radius, bordes y sombras por rol.** El mismo tipo de elemento con radios dispares entre vistas
   es deriva. Pero elementos con roles distintos (ej. modal flotante vs card de tabla) pueden usar
   niveles de elevación y radios distintos de forma justificada.
6. **Escala de elevación.** La profundidad comunica jerarquía espacial: si hay demasiados niveles
   de sombra y ninguno distingue un plano funcional, la sombra solo decora.

---

## Consistencia entre componentes

**Cómo mirar**

1. **Toma un patrón y búscalo en todas partes**: `PageHeader`, `Card`, `Panel`, `Table`,
   `EmptyState`, `FormSection`, `Modal`, `PrimaryAction`, `SectionHeading`, `Filters`, `KPI`.
2. **Consistencia por rol, no por propiedad aislada.**
   *Misma apariencia despierta expectativa de mismo rol.*
   Preguntas clave:
   - ¿Dos elementos visualmente equivalentes cumplen realmente el mismo rol?
   - ¿Dos acciones con el mismo rol cambiaron de estilo sin justificación?
   - ¿Un elemento informativo parece botón porque comparte exactamente su tratamiento?
3. **Distingue con rigor:**
   - **Deriva:** Mismo rol + tratamiento diferente sin justificación.
   - **Diferencia válida:** Roles diferentes + tratamientos diferentes (ej. un modal y una card
     de lista tienen diferente radio y sombra porque sus roles y planos en el sistema difieren;
     una tabla operacional y una landing tienen densidades distintas).
   - **Problema semántico visual:** Roles diferentes + tratamiento idéntico que oculta la
     diferencia funcional.
4. **Nombra el divergente.** Cuando cuatro apariciones coinciden y una no, el hallazgo es esa
   una, no "el patrón es inconsistente".

Aquí se **detecta**. La consolidación estructural es `component-architecture`.

---

## Comparación con una referencia

**Cómo mirar**

1. **Normaliza las condiciones antes de juzgar.**
   > *Normalize what can materially change the visual result before attributing the difference to inconsistency.*
   Comprueba si las condiciones de comparación son razonablemente equivalentes:
   - **Viewport y breakpoint:** no reportes diferencias de layout o container si una captura está en
     `1440px` y la otra en `1280px`;
   - **Zoom y densidad de píxeles (DPR);**
   - **Estado y datos:** menús abiertos/cerrados, longitud de textos dinámicos reales vs mockups,
     scroll vertical.
   Si no se puede normalizar: compara las relaciones que sigan siendo válidas, marca lo incierto
   como `No verificado`, y **nunca bloquees toda la revisión**.
2. **Paridad visual ≠ pixel perfect.**
   > *Preserve visual intent before chasing pixel equality.*
   No busques una réplica matemática inflexible.
   - **Debe conservarse:** jerarquía, anclas visuales, proporciones dominantes, agrupaciones, ritmo,
     roles tipográficos, tratamiento de acciones, intención de densidad y color por rol.
   - **Puede variar legítimamente:** contenido dinámico, wrapping de texto, renderizado de fuentes
     del sistema operativo, adaptaciones fluidas previstas del navegador.
3. **Prueba de pérdida de intención:** no preguntes solo *"¿se parece?"*, sino:
   > ¿La decisión de diseño que hacía funcionar la referencia sobrevivió en la implementación?
   Si un KPI gobernaba la vista por tamaño y posición, y en la implementación quedó atrapado en una
   grilla simétrica donde todos los datos pesan igual, hay una pérdida de intención grave.
4. **Si la referencia es más reciente que `ui-system.md`** y ambos se contradicen, la
   implementación que sigue la referencia **no está incumpliendo**. Declara la discrepancia y
   recomienda sincronizar la foundation con `visual-foundation`.

**Señales de deriva**: proporciones estructurales alteradas; ancla visual disuelta entre elementos
secundarios; espaciados relacionales uniformados mecánicamente.

---

## Comparación entre pantallas

**Cómo mirar**

1. **Ponlas lado a lado**, en miniatura si es posible. Las diferencias de sistema se perciben
   rápidamente en miniatura.
2. **Empieza por lo compartido**: encabezado de página, container, ritmo vertical, tratamiento de
   acciones primarias y secundarias, tratamiento de metadata.
3. **La frecuencia es evidencia, nunca autoridad (*Frequency is evidence, not authority*).**
   Si cuatro pantallas aplican un tratamiento incorrecto según el diseño aprobado o `ui-system.md`
   y una quinta pantalla es la correcta, las cuatro son las desviadas. No acuses a la quinta por
   ser minoría. La mayoría solo ayuda a orientar hipótesis cuando no existe una fuente superior.
4. **Clasifica la inconsistencia encontrada:**
   - **Local:** Una vista o componente puntual se desvió de un patrón claro. → Derivar a `interface-craft`.
   - **Repetida:** Varias pantallas presentan la misma divergencia por un componente común. → Resolver diseño y derivar a `component-architecture`.
   - **Sistémica:** Muchas pantallas contradicen `ui-system.md` de forma deliberada y uniforme. → Comprobar referencia más reciente y sincronizar con `visual-foundation`.

**Señales de deriva**: la misma acción con distinto peso según la pantalla; el mismo rol tipográfico
con tamaños arbitrarios; una vista que inventa una escala de spacing propia; iconografía con estilos
visuales discordantes conviviendo en el mismo producto.

---

## Señales de diseño genérico

No son defectos por definición. Son **indicios** de que una decisión no se tomó, y solo se
reportan cuando el problema es visible y relevante para esta pantalla.

Todo convertido en cards · cards dentro de cards · el hero de siempre · fila estándar de KPI sin
jerarquía · exceso de pills · gradientes arbitrarios · radius excesivo · superficies flotantes
innecesarias · icono + título + descripción repetido mecánicamente · simetría artificial · una
landing muy aireada aplicada a una herramienta operacional.

**La prueba**: ¿este patrón está aquí porque sirve al contenido y al producto, o porque era la
solución más fácil de generar? Si sirve, se queda —aunque sea común. Si no, el hallazgo no es "usa
cards": es qué relación del contenido quedó sin expresar.

**No recomiendes creatividad gratuita.** El reemplazo propuesto tiene que resolver algo concreto:
comprensión, prioridad, carácter del producto o facilidad de uso.
