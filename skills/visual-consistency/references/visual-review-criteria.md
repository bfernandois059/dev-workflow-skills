# Visual Review Criteria

Criterios de consulta de `visual-consistency`. Cada sección dice **qué mirar**, **cómo distinguir
una desviación real de una diferencia justificada** y **qué señales delatan deriva**.

> **Consulta únicamente las secciones relacionadas con los posibles defectos que ya observaste.**
> Esto es una guía perceptual, no una checklist obligatoria. Recorrerla entera convierte una
> revisión de diez minutos en la auditoría de cumplimiento que esta skill existe para evitar.

> **Sobre las cifras.** Donde aparece un valor orientativo está declarado como tal. Ninguno es un
> umbral de aprobación ni una condición automática: el criterio es siempre perceptual y
> funcional —¿se nota?, ¿significa algo distinto?—, y el sistema visual del proyecto manda sobre
> cualquier número escrito aquí.

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
2. **Nombra el primer elemento** que toca el ojo. ¿Coincide con lo más importante de la pantalla?
   Si el ojo va a un badge de color o a una ilustración, el peso está mal repartido.
3. **Clasifica en tres niveles.** Primario, secundario, terciario. Si muchos bloques compiten
   como primarios, no hay jerarquía: hay una lista.
4. **Quita el color.** En escala de grises, ¿sigue habiendo orden? Si desaparece, la jerarquía
   estaba sostenida solo por color.

**Diferencia justificada**: una vista de comparación donde varios elementos *deben* pesar igual
—una tabla, una grilla de resultados equivalentes— no es una jerarquía rota. La pregunta es si la
igualdad es la respuesta al contenido o la ausencia de una decisión.

**Señales de deriva**: jerarquía construida solo subiendo `font-weight`; dos o tres CTA al mismo
nivel; metadata con el mismo tratamiento que el dato principal; el título de la página más
grande que el contenido que importa; un KPI dominante compitiendo con su propio encabezado.

---

## Composición

**Cómo mirar**

1. **Dibuja los bloques como rectángulos**, sin texto. ¿Esa distribución dice algo sobre lo que
   contiene, o serviría igual para cualquier otra pantalla?
2. **Contenido dominante.** ¿Hay un elemento que merece dominar —una tabla, un gráfico, un
   formulario— y quedó atrapado en una grilla de iguales?
3. **Tapa la mitad inferior.** ¿Lo que queda arriba es lo que debía quedar?
4. **Cuenta las superficies.** ¿Cada bloque tiene su propia card, borde o fondo? Eso suele ser
   agrupación suplida con decoración.

**Señales de deriva**: la estructura por defecto —badge → título → párrafo → dos botones → tres
tarjetas, o título → fila de KPI → gráfico → tabla— aplicada sin que el contenido la pida;
simetría perfecta para contenido de importancia desigual; anidamiento que no corresponde a
ninguna relación real.

---

## Tipografía

**Cómo mirar**

1. **Lista los tamaños en uso** y agrúpalos por rol, no por valor. Dos tamaños distintos para el
   mismo rol son una desviación aunque ambos existan hace meses.
2. **Distancia entre niveles.** `H1`, `H2` y `H3` deben distinguirse sin compararlos lado a lado.
   Si hay que medirlos para notar la diferencia, el sistema tiene niveles que no comunican nada.
3. **Tamaños vecinos.** Varios valores muy próximos conviviendo —del tipo 15, 16, 17, 18— casi
   nunca son niveles: son un nivel y sus accidentes.
4. **Pesos.** El mismo rol con pesos distintos entre pantallas es deriva. La metadata con peso
   excesivo compite con el dato; el texto secundario demasiado débil deja de leerse.
5. **Line-height** según el rol: títulos compactos, texto corrido cómodo. Un interlineado de
   párrafo aplicado a un título lo desarma.
6. **Ancho de línea.** El texto corrido incómodo se nota al leerlo: el ojo pierde el inicio de la
   línea siguiente. Como referencia orientativa —no como umbral— suele estar en el orden de 45 a
   75 caracteres; lo que se juzga es la lectura, no el número.

**Diferencia justificada**: una escala distinta en un contexto denso —una tabla, un panel lateral—
puede ser deliberada si el sistema la contempla. Verifícalo contra `ui-system.md` antes de
reportarla.

**No asumas que cada tamaño histórico es un rol legítimo.** Y no impongas cifras universales
cuando el sistema visual del proyecto estableció otra cosa.

---

## Spacing

El spacing expresa **relaciones**: lo que está cerca pertenece junto, lo que está lejos es otra
cosa. Se revisa por relación, no por valor.

**Relaciones a mirar**: sección ↔ sección · bloque ↔ bloque · título ↔ su contenido · label ↔ su
valor · controles relacionados entre sí · padding interno de componentes equivalentes · gutters ·
ritmo vertical general.

**Cómo mirar**

1. **¿Los grupos se leen como grupos?** Si el espacio entre un título y su contenido es igual al
   que lo separa del bloque siguiente, la agrupación no existe visualmente.
2. **Compara componentes equivalentes.** Dos cards con padding distinto, dos secciones con gaps
   distintos: eso es deriva, no variación.
3. **Busca valores sueltos.** Un valor arbitrario donde el sistema tiene escala —del tipo
   `gap-[22px]` conviviendo con la escala del proyecto— casi siempre es un ajuste local que
   nunca volvió al sistema.
4. **Espacio uniforme.** Si todo está separado por lo mismo, el spacing dejó de comunicar
   jerarquía y solo separa.

**Señales de deriva**: márgenes accidentales heredados de otro componente; exceso de espacio
usado para disimular una composición débil; densidad impropia del tipo de producto.

**Consistencia no significa usar el mismo valor en todo.** Significa que el mismo tipo de
relación se resuelve siempre igual.

---

## Layout y alineación

**Cómo mirar**

1. **Traza los bordes verticales** con la mirada o con una regla en pantalla. Los elementos que
   deberían compartir eje —títulos, contenido, acciones— ¿lo comparten?
2. **Ancho del container** entre secciones de la misma pantalla y entre pantallas equivalentes.
   Un ancho que cambia sin motivo se percibe como descuido antes de que nadie sepa por qué.
3. **Alineación óptica frente a matemática.** Iconos, comillas y formas redondas a veces
   necesitan corrección para *verse* alineados. Lo que se juzga es lo que se ve.
4. **Alineación de texto en columnas y tablas**: números a la derecha o por el separador decimal,
   texto a la izquierda. Un desalineado numérico impide comparar de un vistazo.

**Señales de deriva**: dos secciones de la misma página con containers distintos; contenido
centrado en una pantalla y alineado a la izquierda en su equivalente; acciones que cambian de
posición entre vistas del mismo tipo.

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

1. **¿Qué justifica cada superficie?** Una card, un borde o una sombra deberían señalar
   agrupación, elevación o separación real. Si solo decoran, agregan ruido.
2. **Cards dentro de cards.** Casi siempre es agrupación resuelta dos veces.
3. **Radius, bordes y sombras por rol.** El mismo tipo de elemento con radios distintos entre
   pantallas es deriva. Radios muy próximos entre sí no son dos niveles del sistema.
4. **Escala de elevación.** Si hay muchos niveles de sombra y ninguno significa algo distinto, la
   profundidad no está comunicando: está adornando.

---

## Consistencia entre componentes

**Cómo mirar**

1. **Toma un patrón y búscalo en todas partes**: `PageHeader`, `Card`, `Panel`, `Table`,
   `EmptyState`, `FormSection`, `Modal`, `PrimaryAction`, `SectionHeading`, `Filters`, `KPI`.
2. **Compara los mismos atributos** en cada aparición: tipografía, spacing, radius, color,
   layout, iconografía, densidad, jerarquía, comportamiento visual.
3. **Separa variante de deriva.** Pregunta qué función cumple cada aparición. Si cumplen la
   misma, la diferencia es deriva. Si cumplen funciones distintas, la diferencia puede ser
   correcta —y forzar la igualdad empeoraría la pantalla.
4. **Nombra el divergente.** Cuando cuatro apariciones coinciden y una no, el hallazgo es esa
   una, no "el patrón es inconsistente".

Aquí se **detecta**. La consolidación estructural es `component-architecture`.

---

## Comparación con una referencia

**Cómo mirar**

1. **Confirma que la referencia aplica** a esta pantalla y está aprobada. Un mockup de otra vista
   no es la vara.
2. **Compara en el mismo orden macro→micro**, no elemento por elemento. Primero si la estructura
   y el peso relativo coinciden; después los valores.
3. **Distingue tres cosas**: lo que se implementó distinto, lo que la referencia no cubría y hubo
   que resolver, y lo que se implementó distinto **a propósito** y con motivo.
4. **Si la referencia es más reciente que `ui-system.md`** y ambos se contradicen, la
   implementación que sigue la referencia **no está incumpliendo**. Declara la discrepancia y
   recomienda sincronizar la foundation con `visual-foundation`.

**Señales de deriva**: proporciones que cambiaron al implementar; el énfasis del mockup repartido
entre varios elementos; espaciados uniformados que en la referencia eran deliberadamente
desiguales.

---

## Comparación entre pantallas

**Cómo mirar**

1. **Ponlas lado a lado**, en miniatura si es posible. Las diferencias de sistema se ven antes en
   miniatura que a tamaño completo.
2. **Empieza por lo compartido**: encabezado de página, container, ritmo vertical, tratamiento de
   las acciones, tratamiento de la metadata.
3. **Busca la que se salió**, no las diferencias de a pares. Con tres o más pantallas suele haber
   un consenso implícito y una excepción.
4. **Verifica que la excepción no esté justificada** por el tipo de contenido antes de
   reportarla.

**Señales de deriva**: la misma acción con distinto peso según la pantalla; el mismo tipo de
título con distinto tamaño; una vista que usa una escala de spacing propia; iconografía de dos
familias distintas conviviendo.

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
