# Criterios de dirección

Referencia de consulta de `design-directions`. **No se recorre entera.** Se abre la sección que
corresponde a la decisión que está abierta: si lo que no se decidió es cómo presentar la
evidencia, no hace falta leer densidad de catálogo ni master/detail.

Nada de lo que sigue es una plantilla. `evidence-first` es un **criterio posible**, no una receta
de `hero + logos + 3 cards + testimonial + CTA`. Cada sección responde lo mismo:

```text
qué decisión cambia · qué problema podría resolver · qué señales indican que aplica
· qué riesgo introduce · cuándo sería una mala elección
```

**Índice**

- [Ejes de divergencia](#ejes-de-divergencia)
- [Jerarquía](#jerarquía)
- [Composición](#composición)
- [Narrativa y secuencia](#narrativa-y-secuencia)
- [Densidad](#densidad)
- [Relación contenido/media](#relación-contenidomedia)
- [Evidence-first](#evidence-first)
- [Product-first](#product-first)
- [Task-first](#task-first)
- [Editorial](#editorial)
- [Discovery](#discovery)
- [Comparison](#comparison)
- [Master/detail](#masterdetail)
- [Sitios comerciales y de servicios](#sitios-comerciales-y-de-servicios)
- [E-commerce](#e-commerce)
- [Dashboards](#dashboards)
- [CRM, intranets y sistemas operacionales](#crm-intranets-y-sistemas-operacionales)
- [Uso de referencias](#uso-de-referencias)
- [Activos y fotografía](#activos-y-fotografía)
- [Motion e interacción](#motion-e-interacción)
- [Comparación de alternativas](#comparación-de-alternativas)
- [Señales de falsa diversidad](#señales-de-falsa-diversidad)
- [Evaluación de trade-offs](#evaluación-de-trade-offs)
- [Criterios de recomendación](#criterios-de-recomendación)

---

## Ejes de divergencia

Un eje es una pregunta cuya respuesta cambia la interfaz de forma perceptible. Sirven para
construir alternativas que se diferencien por decisión y no por tratamiento.

```text
¿qué domina la pantalla?                 evidencia · producto · texto · datos · acción
¿qué se muestra primero?                 demostración · explicación · confianza · oferta
¿cómo se ordena el contenido?            secuencia narrativa · agrupación · comparación · exploración
¿cuánto se muestra a la vez?             denso y simultáneo · progresivo · por pasos
¿quién manda, imagen o contenido?        media dominante · media de apoyo · sin media
¿cómo se navega?                         lineal · contextual · por facetas · master/detail
¿cómo se decide?                         leyendo · comparando · probando · confiando
¿cuánto trabajo hace la interacción?     estática · disclosure · filtrado en vivo · manipulación directa
```

**Úsalos para generar, no para rellenar.** Dos direcciones que responden distinto a un eje
importante divergen de verdad; dos que responden igual a todos son la misma dirección con otro
color.

**Un eje útil no es cualquier eje distinto.** Cambiar la navegación de una landing de una sección
es una diferencia técnica sin consecuencia perceptible. El eje tiene que mover algo que el usuario
note al usar la interfaz.

---

## Jerarquía

**Qué decisión cambia.** Qué elemento gana la pantalla y en qué orden se lee lo demás.

**Qué problema resuelve.** Interfaces donde todo pesa igual y el usuario no sabe dónde mirar; o
donde el elemento dominante no es el que produce valor.

**Señales de que aplica.** Hay más de un candidato legítimo a protagonista —una imagen fuerte, una
cifra decisiva, un formulario, una acción— y la elección cambia el comportamiento del usuario.

**Riesgo.** Una jerarquía muy marcada puede enterrar información que sí se necesita, sobre todo en
sistemas operacionales donde varias cosas compiten por atención de forma legítima.

**Mala elección.** Cuando el contenido no tiene un protagonista real y forzar uno obliga a inventar
importancia —un titular grande sobre un mensaje vacío no crea jerarquía, la simula.

---

## Composición

**Qué decisión cambia.** Cómo se ocupa el espacio: simetría o asimetría, centrado o desplazado,
columnas iguales o desiguales, grid regular o ritmo variable, contenedor cerrado o sangrías a
borde completo.

**Qué problema resuelve.** Interfaces que se ven correctas pero intercambiables, porque todas
resuelven con el mismo bloque centrado.

**Señales de que aplica.** El contenido tiene piezas de peso muy distinto, o hay un activo
—imagen, dato, producto— que soporta ocupar más espacio del que le da una retícula neutra.

**Riesgo.** Una composición asimétrica o de ritmo variable exige más trabajo en breakpoints
intermedios y más disciplina para no romperse cuando el contenido real varía de largo.

**Mala elección.** Cuando el contenido es homogéneo y repetitivo: forzar variación compositiva
sobre veinte elementos equivalentes produce ruido, no interés.

---

## Narrativa y secuencia

**Qué decisión cambia.** El orden en que se presentan los argumentos: demostrar y después
explicar, explicar y después demostrar, establecer confianza antes de la oferta, o ir al grano.

**Qué problema resuelve.** Páginas donde el orden es el heredado —hero, features, testimonios,
CTA— sin relación con cómo decide realmente ese usuario.

**Señales de que aplica.** Hay más de una audiencia con distinto nivel de conocimiento previo, o
el producto requiere una comprensión antes de la conversión.

**Riesgo.** Una secuencia larga pierde a quien ya estaba convencido; una corta no alcanza para lo
que requiere explicación.

**Mala elección.** Cuando la interfaz no es persuasiva sino operativa: un panel de trabajo no
tiene narrativa, tiene tareas.

---

## Densidad

**Qué decisión cambia.** Cuánta información se ve simultáneamente y cuánta se difiere.

**Qué problema resuelve.** Dos fallos opuestos: paneles que ahogan porque muestran todo con el
mismo peso, e interfaces operacionales convertidas en landings espaciosas donde el usuario
necesita cuatro clics para ver lo que antes veía junto.

**Señales de que aplica.** El usuario compara, supervisa o repite la misma acción muchas veces al
día; o al revés, entra una vez y necesita comprender.

**Riesgo.** Bajar densidad puede destruir la capacidad de comparar. Subirla puede volver la
pantalla ilegible para usuarios ocasionales.

**Mala elección.** Tratar la densidad como estética. Densidad es una decisión sobre la tarea:
**antes de eliminar información**, el orden es jerarquía → agrupación → disclosure → densidad.

---

## Relación contenido/media

**Qué decisión cambia.** Si la imagen manda, acompaña, ilustra o no existe; y si el texto organiza
la pantalla o la rellena.

**Qué problema resuelve.** Proyectos con buen material visual que lo usan como decoración, y
proyectos sin material visual que diseñan como si lo tuvieran.

**Señales de que aplica.** Existe —o puede producirse— fotografía, video o visualización con
calidad suficiente para sostener una composición.

**Riesgo.** Una dirección media-dominante queda a merced de la calidad y cantidad de assets, hoy y
en cada actualización futura de contenido.

**Mala elección.** Cuando el valor del producto no es visual y la imagen no aporta información:
fotografía genérica ocupando media pantalla es coste sin beneficio.

---

## Evidence-first

**Qué decisión cambia.** La pantalla se abre con prueba —proyectos, resultados, casos, escala— y
el texto organiza esa evidencia en lugar de precederla.

**Qué problema resuelve.** Credibilidad. Sirve cuando el mercado desconfía del discurso comercial
y responde a lo demostrable.

**Señales de que aplica.** Existen casos, obras, clientes o mediciones **reales y verificables**, y
el material es lo bastante bueno para mostrarse sin maquillaje.

**Riesgo.** Deja menos espacio inicial para explicar servicios complejos, y su fuerza depende
directamente de la calidad del material.

**Mala elección.** Cuando la evidencia no existe. Entonces la dirección solo funciona si alguien
la fabrica, y fabricar métricas, testimonios o certificaciones **no es una opción**: se declara la
dependencia o se elige otro camino.

---

## Product-first

**Qué decisión cambia.** El producto o la interfaz misma es lo primero que se ve; la explicación
viene después y se apoya en lo que ya se mostró.

**Qué problema resuelve.** Productos que se entienden mejor viéndolos que leyéndolos.

**Señales de que aplica.** El producto es visualmente comprensible, tiene una interfaz o una forma
propia reconocible, y su valor se percibe en un vistazo.

**Riesgo.** Un producto que requiere contexto para entenderse queda incomprendido; y la dirección
depende de capturas o renders que envejecen con cada release.

**Mala elección.** Servicios abstractos, consultoría, o productos cuyo valor está en el proceso y
no en el objeto.

---

## Task-first

**Qué decisión cambia.** La pantalla se organiza alrededor de lo que hay que hacer ahora, no
alrededor de todo lo que existe.

**Qué problema resuelve.** Sistemas operacionales donde el usuario entra con una intención
concreta y repetida, y el panel le presenta un resumen que no usa.

**Señales de que aplica.** Hay tareas dominantes identificables, con frecuencia alta y un flujo
estable.

**Riesgo.** Puede reducir la visión de conjunto y dificultar el trabajo de quien supervisa en vez
de ejecutar.

**Mala elección.** Cuando los perfiles de uso son heterogéneos y nadie puede nombrar la tarea
dominante sin inventarla.

---

## Editorial

**Qué decisión cambia.** La composición se organiza como una publicación: tipografía con
protagonismo, ritmo variable, jerarquías fuertes, lectura guiada.

**Qué problema resuelve.** Diferenciación y tono en categorías donde todo se ve igual; también
contenidos que se entienden leyendo.

**Señales de que aplica.** Hay contenido real que merece lectura, y una identidad tipográfica
capaz de sostener escala.

**Riesgo.** Exige buen copy —una dirección editorial sobre texto de relleno se desarma— y suele
implicar más trabajo de composición por sección.

**Mala elección.** Interfaces de trabajo, catálogos extensos y pantallas donde el usuario escanea
en vez de leer.

---

## Discovery

**Qué decisión cambia.** La interfaz está hecha para recorrer y encontrar: exploración por
categorías, facetas, recomendaciones, ritmo de descubrimiento.

**Qué problema resuelve.** Usuarios que no saben exactamente qué buscan.

**Señales de que aplica.** Catálogo amplio, intención difusa, valor en la variedad.

**Riesgo.** Puede alargar el camino de quien ya sabía qué quería, y suele exigir buenos datos de
categorización.

**Mala elección.** Catálogos pequeños o compras de intención muy definida, donde explorar es
fricción.

---

## Comparison

**Qué decisión cambia.** La pantalla existe para poner alternativas lado a lado y hacer evidentes
las diferencias.

**Qué problema resuelve.** Decisiones donde el usuario ya está evaluando y necesita distinguir,
no descubrir.

**Señales de que aplica.** Atributos comparables y completos entre ítems, y una decisión que
realmente depende de esas diferencias.

**Riesgo.** Expone huecos de datos: si faltan atributos, la comparación miente por omisión. Y
empuja al usuario a decidir por lo comparable aunque no sea lo importante.

**Mala elección.** Cuando la diferencia real es cualitativa —tono, ajuste, experiencia— y la tabla
la reduce a casillas.

---

## Master/detail

**Qué decisión cambia.** Si el contexto de la lista permanece visible mientras se trabaja un
elemento, o si cada detalle ocupa la pantalla completa.

**Qué problema resuelve.** Flujos de revisión en serie: bandejas, colas, backlogs, fichas de
clientes.

**Señales de que aplica.** El usuario recorre muchos elementos por sesión y necesita no perder el
lugar.

**Riesgo.** Reduce el espacio para el detalle y complica el responsive; en pantallas chicas obliga
a resolver la navegación en dos pasos sin perder capacidades.

**Mala elección.** Cuando el detalle es rico y el recorrido es raro: pagar el coste de layout por
un patrón que casi nadie usa.

---

## Sitios comerciales y de servicios

**Qué puede divergir.** Narrativa · forma de demostrar · peso de la prueba social · relación
contenido/media · densidad · tratamiento del CTA · arquitectura de secciones.

**Qué no se toca para diferenciar.** El servicio ofrecido, el alcance comercial y los claims. Una
dirección no puede prometer algo que el negocio no hace.

**Riesgo típico.** Que las direcciones se distingan solo por el hero y el resto de la página sea
idéntica en las tres.

**Señal de mala exploración.** Todas terminan en la misma secuencia heredada y solo cambia la
foto.

---

## E-commerce

**Qué puede divergir.** Producto-first · editorial · comparación · descubrimiento · construcción
de confianza · densidad de catálogo · cómo se presentan variantes, precio y disponibilidad.

**Qué no se toca para diferenciar.** El flujo comercial real: pasos de compra, medios de pago,
políticas, impuestos y logística. Una dirección visual no reescribe el checkout.

**Riesgo típico.** Una dirección editorial preciosa que entierra precio, stock o la acción de
compra.

**Señal de mala exploración.** Las tres opciones son la misma ficha con distinta tipografía, o una
de ellas "gana" porque se le dio mejor fotografía de producto.

---

## Dashboards

**Qué puede divergir.** Monitoring-first —estado actual continuo—, exception-first —solo lo que
está fuera de rango—, comparison-first —contra periodo, objetivo o par— y análisis narrativo
—explicar qué pasó.

**Qué no se toca para diferenciar.** Las métricas disponibles y su definición. Inventar un
indicador para que una dirección luzca mejor es inventar producto.

**Riesgo típico.** Exception-first oculta el contexto cuando no hay excepciones; monitoring-first
satura cuando todo es normal; comparison-first exige datos históricos que pueden no existir.

**Señal de mala exploración.** Las alternativas cambian el color de las tarjetas de KPI y
mantienen el mismo orden, las mismas métricas y la misma pregunta implícita.

---

## CRM, intranets y sistemas operacionales

**Qué puede divergir.** Densidad · overview vs. task-first · navegación · master/detail · jerarquía
de acciones · información contextual · progressive disclosure · qué se resuelve sin cambiar de
pantalla.

**Qué no se toca para diferenciar.** Capacidades, permisos, campos obligatorios, estados del
negocio y volumen real de datos. Y no se convierte un CRM en una landing artística para demostrar
creatividad: la ambición aquí se mide en cuánto trabajo ahorra por sesión.

**Riesgo típico.** Bajar densidad en nombre de la limpieza y multiplicar los clics de una tarea
que se repite cincuenta veces al día.

**Señal de mala exploración.** Direcciones que se distinguen por el estilo de las tarjetas y no
por cómo se opera.

---

## Uso de referencias

**Qué decisión cambia.** Qué principio concreto se toma prestado.

**Cómo usarlas.** Nombra la decisión, no la marca: *"de esta referencia interesa que la evidencia
ocupe el primer scroll"* es utilizable; *"hagamos algo como Stripe"* no.

**Riesgo.** Mezclar principios incompatibles de tres referencias produce una interfaz sin criterio
propio; copiar la apariencia sin la estructura produce una imitación que no funciona con este
contenido.

**Mala elección.** Tomar una referencia cuyo contexto no se parece —otro volumen de contenido,
otro tipo de usuario, otros assets— y tratar su resultado como evidencia de que aquí funcionará.

---

## Activos y fotografía

**Qué decisión cambia.** Cuánto peso puede soportar la imagen y qué exige eso del proyecto.

**Cómo evaluarlo.** Qué existe hoy · con qué calidad y en qué formatos · si se puede producir más ·
quién lo mantiene cuando el contenido cambie · si hay suficiente para todas las pantallas de esa
familia, no solo para la maqueta.

**Riesgo.** Una dirección que depende de material que hoy no existe no es inviable, pero **su
dependencia se declara como exigencia**, no se oculta.

**Mala elección.** Presentar una dirección fotográfica maquetada con stock que el proyecto nunca
va a tener. Eso no compara direcciones: compara una realidad contra una ficción.

---

## Motion e interacción

**Qué decisión cambia.** Si la interfaz se comporta de forma estática, progresiva o manipulable, y
si el movimiento comunica algo o solo decora.

**Qué problema resuelve.** Comprensión de relaciones —qué viene de dónde, qué cambió, qué está
cargando— y sensación de respuesta.

**Señales de que aplica.** Hay transiciones de estado con significado, o una demostración que se
entiende mejor en movimiento.

**Riesgo.** Coste de implementación y mantenimiento, rendimiento, accesibilidad —incluido
`prefers-reduced-motion`— y fragilidad cuando el contenido real varía.

**Mala elección.** Usar el motion como el rasgo que diferencia dos direcciones. Si al quitar las
animaciones las dos son la misma interfaz, era una sola dirección.

---

## Comparación de alternativas

Para que la comparación sea honesta, mantén constante todo lo que no es la decisión:

```text
mismo contenido · misma funcionalidad · mismos datos · mismo viewport
· mismos assets aprobados · mismas restricciones · nivel de acabado equivalente
```

Y explicita **qué cambia** en cada una en términos de decisión, no de acabado. Si una alternativa
se ve mejor porque está más terminada, la comparación no mide direcciones: mide esfuerzo de
presentación.

---

## Señales de falsa diversidad

```text
las tres mantienen el mismo orden de bloques
las tres conducen la mirada al mismo punto
la diferencia se explica solo con color, radius, sombra o tipografía
los nombres son "Modern", "Premium", "Bold"
una tiene features que las otras no
una tiene mejor fotografía o más contenido
la descripción de la diferencia usa adjetivos y no decisiones
al describirla sin mencionar estilo, no queda nada que decir
```

Cuando aparezcan, agrupa las propuestas en una sola dirección con tratamientos posibles y busca la
divergencia donde está la decisión real.

---

## Evaluación de trade-offs

Un trade-off pertenece a la decisión, no al gusto. Para cada dirección:

```text
Gana    → qué mejora concretamente y para quién
Pierde  → qué se hace más difícil, menos visible o más lento
Exige   → qué debe tener el producto, el contenido o el equipo para que funcione
```

Adecuación al problema, claridad, diferenciación, coherencia con el producto, mantenibilidad,
activos requeridos y complejidad proporcional son dimensiones distintas: una dirección puede ganar
en diferenciación y perder en mantenibilidad, y decirlo es el trabajo.

**El esfuerzo de implementación es un trade-off más, no un veto.** Tampoco es un mérito: una
dirección compleja necesita beneficio perceptible o funcional que lo justifique.

---

## Criterios de recomendación

Cuando hay información suficiente, se recomienda. En orden:

1. **Adecuación al problema declarado** —qué debe lograr esta pantalla.
2. **Adecuación al usuario real** y a cómo decide o trabaja.
3. **Coherencia con la identidad y el producto** existentes.
4. **Viabilidad con los activos y el contenido reales**, hoy.
5. **Diferenciación**, cuando el mercado lo exige.
6. **Mantenibilidad y complejidad proporcional.**

La recomendación dice qué se elige, por qué, y **qué se acepta perder** frente a las otras.

Cuando falta una decisión de producto o de negocio que no corresponde tomar aquí, la salida es una
recomendación condicionada —*"si el objetivo es X, A; si es Y, B"*— con la decisión pendiente
nombrada explícitamente. No es lo mismo que *"depende de ustedes"*: la condición se identifica y
cada rama queda resuelta.
