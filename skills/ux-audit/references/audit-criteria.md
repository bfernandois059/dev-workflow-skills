# Criterios de auditoría

Referencia de consulta de `ux-audit`. **No se recorre entera.** Se abren las secciones
relevantes para la tarea auditada: auditar un formulario de postulación no obliga a pasar por
e-commerce ni por dashboards.

No es un catálogo universal de heurísticas ni repite el `SKILL.md`. Cada sección responde lo
mismo, de forma práctica:

```text
qué observar · qué costo puede producir · qué evidencia confirma el problema
· qué falsos positivos evitar · qué skill recibe la corrección
```

**Índice**

- [Orientación y propósito](#orientación-y-propósito)
- [Navegación y arquitectura de información](#navegación-y-arquitectura-de-información)
- [Acciones y decisiones](#acciones-y-decisiones)
- [Feedback y system status](#feedback-y-system-status)
- [Errores y recuperación](#errores-y-recuperación)
- [Confirmaciones](#confirmaciones)
- [Acciones destructivas](#acciones-destructivas)
- [Estados](#estados)
- [Formularios](#formularios)
- [Contenido y copy](#contenido-y-copy)
- [Confianza](#confianza)
- [Eficiencia y usuarios frecuentes](#eficiencia-y-usuarios-frecuentes)
- [CRM, intranets y sistemas operacionales](#crm-intranets-y-sistemas-operacionales)
- [Dashboards](#dashboards)
- [E-commerce](#e-commerce)
- [Sitios comerciales](#sitios-comerciales)
- [Móvil cuando afecta la tarea](#móvil-cuando-afecta-la-tarea)
- [Accesibilidad observable](#accesibilidad-observable)

---

## Orientación y propósito

**Qué observar.** Si en los primeros segundos se entiende qué es esto, para quién y qué se puede
hacer aquí. Si la pantalla se abre con la tarea o con material que la antecede. Si quien llega
por primera vez y quien vuelve a diario necesitan cosas distintas y solo una está resuelta.

**Qué cuesta.** Quien no entiende dónde está no decide: relee, retrocede, prueba o abandona. En
herramientas internas el costo no es abandono, es tiempo perdido en cada entrada.

**Qué lo confirma.** El primer bloque útil aparece después de material decorativo o
introductorio; la acción principal no está en el primer pantallazo; el título no dice qué se
hace aquí; hay que leer dos veces para saber qué mira uno.

**Falsos positivos.** Una pantalla puede ser deliberadamente introductoria; un panel para
usuarios entrenados no necesita explicarse como una landing. Confirma quién entra y con qué
frecuencia antes de pedir contexto en pantalla.

**Corrección a.** `interface-craft` si la jerarquía o el orden de bloques está resuelto;
`design-directions` si no está decidido qué debe dominar la pantalla.

---

## Navegación y arquitectura de información

**Qué observar.** Si se sabe dónde se está, cómo se llegó y cómo se vuelve. Si las etiquetas
anticipan lo que hay detrás (*information scent*). Si el agrupamiento corresponde a cómo la
persona piensa la tarea o al organigrama de quien lo construyó. Si volver conserva filtros,
posición y trabajo en curso.

**Qué cuesta.** Búsqueda a ciegas, recorridos de ida y vuelta, trabajo repetido, sensación de
pérdida de control.

**Qué lo confirma.** Volver al listado reinicia filtros o scroll; el botón atrás del navegador
hace algo inesperado; dos secciones podrían contener lo mismo y hay que probar; la ruta actual
no está indicada en ninguna parte.

**Falsos positivos.** Una jerarquía profunda no es un defecto si cada nivel es predecible.
Etiquetas del dominio del negocio pueden ser correctas aunque suenen técnicas para alguien
externo: el criterio es si **este** usuario las entiende.

**Corrección a.** `interface-craft`; `component-architecture` si el problema vive en la
navegación o el layout compartido; `engineering-workflow` si exige cambiar estado o rutas.

---

## Acciones y decisiones

**Qué observar.** Cuál es la acción principal y si se distingue de las demás. Cuántas decisiones
se piden y si llegan cuando la persona tiene con qué decidir. Acciones ambiguas por su etiqueta.
Acciones equivalentes ofrecidas en dos lugares con nombres distintos.

**Qué cuesta.** Decisión incorrecta, parálisis, clics de prueba y error, acciones ejecutadas sin
intención.

**Qué lo confirma.** Dos o más botones con el mismo peso visual compitiendo por ser el
principal; una etiqueta que no dice qué pasará (`Continuar` cuando hay dos caminos posibles); la
acción que la mayoría necesita escondida entre secundarias.

**Falsos positivos.** Que dos acciones se vean parecidas no basta: hay que mostrar que la persona
puede elegir la equivocada o no encontrar la correcta. Y en herramientas densas, varias acciones
visibles suelen ser correctas — el problema es que **ninguna** destaque cuando una domina la
tarea.

**Corrección a.** `interface-craft`. Si la elección de qué debe dominar sigue abierta,
`design-directions`.

---

## Feedback y system status

**Qué observar.** Si toda acción produce respuesta visible, si las esperas perceptibles tienen
indicador, si el resultado se confirma de forma que se pueda creer, y si el sistema dice en qué
estado está algo cuando eso condiciona el siguiente paso.

**Qué cuesta.** Doble envío, duplicados en base de datos, reintentos innecesarios, incertidumbre
sobre si el trabajo se guardó.

**Qué lo confirma.** El botón no cambia al pulsarse; tras guardar no aparece nada o aparece algo
que desaparece antes de leerse; una operación larga no informa progreso; el estado del registro
no coincide con lo que la interfaz sugiere.

**Falsos positivos.** No toda acción necesita un mensaje: un cambio visible inmediato **es**
feedback. Un toast adicional sobre un cambio ya evidente es ruido, no una mejora.

**Corrección a.** `interface-craft` para el tratamiento; `engineering-workflow` si falta el
estado o el manejo asíncrono.

---

## Errores y recuperación

**Qué observar.** Qué se hace para que el error no ocurra, qué pasa cuando ocurre y qué tan caro
es recuperarse. Si el mensaje dice qué pasó, dónde y qué hacer. Si lo ingresado sobrevive. Si
existe camino de salida o el error es un callejón.

**Qué cuesta.** Trabajo perdido, abandono en el punto más caro del flujo, desconfianza duradera.

**Qué lo confirma.** El error aparece solo al enviar; el formulario vuelve arriba sin indicar el
campo; los datos se borran; el texto es genérico (*"Ocurrió un error"*) o técnico; no hay forma
de reintentar sin empezar de nuevo.

**Falsos positivos.** Validar demasiado temprano —marcar en rojo un campo que se está
escribiendo— es un defecto propio, no la solución. Y un error de servidor legítimo no siempre
puede explicarse en detalle: el criterio es si la persona sabe qué hacer a continuación.

**Corrección a.** `interface-craft` para mensajes y ubicación; `engineering-workflow` para
persistencia, validación y manejo real del error.

---

## Confirmaciones

**Qué observar.** Qué se confirma y qué no. Si la confirmación dice **qué** se va a hacer y
sobre qué objeto concreto. Si hay confirmaciones donde no hacen falta.

**Qué cuesta.** Confirmar por reflejo anula la protección; confirmar todo entrena a ignorar los
diálogos; no confirmar lo irreversible produce pérdidas reales.

**Qué lo confirma.** Un diálogo genérico (*"¿Estás seguro?"*) sin nombrar el objeto; acciones
reversibles que interrumpen con un modal; acciones irreversibles que se ejecutan al primer clic.

**Falsos positivos.** Una acción reversible con deshacer visible **no necesita** confirmación —
proponerla es agregar fricción. Confirmar no es siempre mejor que poder deshacer.

**Corrección a.** `interface-craft`; `engineering-workflow` si hay que implementar deshacer o
cambiar el comportamiento.

---

## Acciones destructivas

**Qué observar.** Si se distinguen de las seguras antes del clic, si están lejos de las
frecuentes, si su alcance es evidente y si existe reversión.

**Qué cuesta.** Pérdida de datos, trabajo irrecuperable, incidentes que llegan a soporte.

**Qué lo confirma.** Una acción destructiva con el mismo tratamiento que una segura o adyacente
a ella; el texto no dice qué se elimina ni si afecta a otros; no hay deshacer ni papelera.

**Falsos positivos.** Que una acción destructiva sea visible no es el problema: en herramientas
operacionales muchas veces debe serlo. El problema es que **no se distinga** o que su alcance
sea invisible.

**Corrección a.** `ux-audit` mantiene el hallazgo —es prevención de error, no estética—;
la corrección visual va a `interface-craft` y la reversibilidad a `engineering-workflow`.

---

## Estados

**Qué observar.** Vacío, cargando, error, éxito, parcial y deshabilitado: cuáles existen, cuáles
faltan y cuáles mienten.

- **Vacío:** ¿ofrece la acción que lo llena o solo explica por qué está vacío?
- **Cargando:** ¿se distingue de "no hay nada"?
- **Deshabilitado:** ¿se entiende por qué y qué haría falta para habilitarlo?
- **Éxito:** ¿confirma lo que ocurrió y deja claro el paso siguiente?

**Qué cuesta.** Quedarse esperando algo que no va a pasar; creer que no hay datos cuando están
cargando; no saber cómo desbloquear un control.

**Qué lo confirma.** Un estado faltante es hallazgo, no pendiente. Un control deshabilitado sin
explicación; un vacío que solo describe; una tabla que pasa de nada a lleno sin transición.

**Falsos positivos.** No todo estado deshabilitado necesita texto: si la condición es evidente
en pantalla, basta. Y un vacío puede ser correcto sin acción cuando la acción no corresponde a
ese rol.

**Corrección a.** `interface-craft`; `engineering-workflow` si el estado no existe en el
producto.

---

## Formularios

**Qué observar.** Qué se pide y por qué; agrupación; labels visibles; ayuda contextual;
obligatoriedad; defaults; validación y su momento; mensajes; persistencia tras error; prevención
de pérdida al salir; submit; loading; éxito; recuperación.

**Qué cuesta.** Abandono proporcional al esfuerzo y a la sensación de intrusión; retrabajo
completo cuando el error borra lo escrito.

**Qué lo confirma.** Campos cuyo uso no se explica y no es obvio; labels solo en `placeholder`
—que desaparecen al escribir—; validación únicamente al enviar; mensaje lejos del campo; salida
accidental sin aviso con trabajo dentro.

**Falsos positivos.** Muchos campos no es automáticamente un defecto: un trámite legítimo puede
necesitarlos. El hallazgo es pedir datos **que no se usan**, pedirlos **antes de tiempo** o no
agrupar lo que conceptualmente va junto. **No cambies reglas de obligatoriedad ni reglas
comerciales**: si no se entiende por qué un dato es obligatorio, eso es un hallazgo UX o una
pregunta de producto, no una decisión tuya.

**Nota de alcance.** No conviertas esto en una auditoría WCAG completa.

**Corrección a.** `interface-craft` para estructura y mensajes; `engineering-workflow` para
validación, persistencia y reglas.

---

## Contenido y copy

**Qué observar.** Solo el copy que afecta comprensión, decisión o acción: etiquetas de botones,
títulos que orientan, ayudas, mensajes de error, textos que explican consecuencias.

**Qué cuesta.** Decisiones equivocadas, dudas, relecturas, soporte innecesario.

**Qué lo confirma.** Una etiqueta que no anticipa el resultado; jerga interna en una pantalla de
cara al cliente; un texto que explica la interfaz en vez de la tarea; instrucciones que llegan
después del campo que describen.

**Falsos positivos.** El estilo, el tono de marca y las preferencias de redacción **no son**
hallazgos de esta skill salvo que produzcan un costo demostrable. Reescribir copy correcto
porque suena mejor es opinión.

**Corrección a.** `interface-craft`, o quien sea dueño del contenido en el proyecto.

---

## Confianza

**Qué observar.** Si la persona tiene lo necesario para creer lo que se le pide creer antes de
comprometerse: identidad clara, información verificable, coherencia entre lo prometido y el paso
siguiente, transparencia sobre costos, plazos y uso de sus datos.

**Qué cuesta.** Abandono justo antes de convertir; datos falsos ingresados por precaución;
llamadas para confirmar lo que la interfaz debería decir.

**Qué lo confirma.** El precio o las condiciones aparecen recién al final; se pide información
sensible sin explicar para qué; no hay forma de saber quién está detrás; el siguiente paso
contradice lo que prometía el anterior.

**Falsos positivos.** Ausencia de testimonios o sellos no es un hallazgo por sí misma, y **no
inventes prueba social que no existe**. El hallazgo es la falta de información necesaria para
decidir, no la falta de material persuasivo.

**Corrección a.** `interface-craft`; producto o negocio cuando falta la información misma.

---

## Eficiencia y usuarios frecuentes

**Qué observar.** El costo por repetición: clics, navegaciones, esperas y decisiones que se
repiten decenas de veces por sesión. Continuidad entre registros. Filtros que persisten. Atajos
existentes. Acciones frecuentes al alcance.

**Qué cuesta.** Tiempo acumulado, errores por fatiga, rechazo de la herramienta.

**Qué lo confirma.** Volver al listado obliga a reconstruir el contexto; una acción diaria exige
tres navegaciones; hay que salir de la pantalla para ver algo que se necesita junto; lo que
se hace en lote solo puede hacerse de a uno.

**Falsos positivos.** Un flujo largo para una tarea **ocasional** no es un problema de
eficiencia. Confirma la frecuencia real antes de priorizar aquí.

**Corrección a.** `interface-craft`; `component-architecture` si el patrón compartido lo causa;
`engineering-workflow` para persistencia de estado y operaciones en lote.

---

## CRM, intranets y sistemas operacionales

**Qué observar.** Densidad útil, escaneabilidad, comparación entre registros, información
contextual disponible sin cambiar de pantalla, jerarquía de acciones frecuentes, continuidad al
navegar, disclosure de lo secundario.

**Qué cuesta.** El trabajo acumulado por sesión, que es la métrica real de estas herramientas.

**Qué lo confirma.** Se ven menos registros de los que la tarea necesita comparar; datos que
siempre se consultan juntos están en pestañas distintas; la acción más frecuente está escondida;
cada operación exige reconstruir el contexto.

**Falsos positivos.** **No recomiendes "más aire", "menos información" ni "una acción por
pantalla" por estética.** Una pantalla densa no es un defecto: el defecto es densidad **sin
jerarquía**. Antes de proponer eliminar información, el orden es jerarquía → agrupación →
disclosure → densidad.

**Corrección a.** `interface-craft`; `adaptive-layout` si el problema aparece al cambiar el
tamaño; `component-architecture` si se repite por un componente compartido.

---

## Dashboards

**Qué observar.** Qué pregunta responde el panel y si esa es la pregunta que la persona tiene.
Si se distingue lo normal de lo que requiere atención. Si hay comparación cuando la decisión la
necesita. Si desde el dato se puede llegar a la acción.

**Qué cuesta.** Paneles que se miran pero no se usan; problemas que pasan desapercibidos;
decisiones tomadas sobre una cifra sin contexto.

**Qué lo confirma.** Todas las métricas con el mismo peso; un número sin referencia contra la
cual leerlo; nada indica qué está fuera de rango; ver el detalle exige salir y buscar.

**Falsos positivos.** Un panel de monitoreo continuo y uno de análisis puntual no tienen el
mismo objetivo. Y **no propongas métricas nuevas**: eso es producto, no auditoría.

**Corrección a.** `interface-craft`; `design-directions` si lo que está abierto es qué debe
responder el panel.

---

## E-commerce

**Qué observar.** Costo de encontrar precio, disponibilidad y condiciones; información suficiente
para elegir entre variantes; claridad del carrito; secuencia del checkout; datos pedidos dos
veces; momento en que aparecen costos de envío e impuestos; recuperación cuando un pago falla.

**Qué cuesta.** Abandono en el punto de mayor intención, y en el peor momento del embudo.

**Qué lo confirma.** El costo total solo se conoce al final; hay que registrarse antes de saber
si conviene; la dirección se pide dos veces; un error de pago vacía el carrito o el formulario;
no se sabe qué pasa después de pagar.

**Falsos positivos.** **No inventes impacto en conversión, lift ni benchmarks.** Describe la
fricción y su costo, no un número. Y no alteres el flujo comercial real —pasos legales, medios
de pago, políticas— para simplificar.

**Corrección a.** `interface-craft`; `engineering-workflow` para el flujo, la persistencia y los
estados de pago.

---

## Sitios comerciales

**Qué observar.** Claridad de la oferta, objeciones previsibles sin responder, información
suficiente para dar el siguiente paso, coherencia entre la promesa y lo que ocurre al hacer
clic, y cuánta fricción hay antes de la acción principal.

**Qué cuesta.** Contactos que no ocurren, consultas mal calificadas, expectativas equivocadas
que se pagan después.

**Qué lo confirma.** No se entiende qué se ofrece sin leer tres secciones; el formulario pide más
de lo necesario para un primer contacto; el CTA promete algo distinto de lo que abre; no hay
forma de saber si el servicio aplica al caso de quien mira.

**Falsos positivos.** La cantidad de secciones o el largo de la página no son hallazgos por sí
mismos, y **tampoco inventes cifras comerciales**.

**Corrección a.** `interface-craft`; `design-directions` cuando lo que falta decidir es el
enfoque de la página.

---

## Móvil cuando afecta la tarea

**Qué observar.** Solo lo que cambia la capacidad de completar la tarea: acciones que
desaparecen o quedan a dos menús de distancia, contenido que exige comparación y ya no cabe,
teclado que tapa el campo o el botón de envío, elementos fijos que ocupan la pantalla, objetivos
táctiles inalcanzables.

**Qué cuesta.** La tarea se vuelve imposible o mucho más cara en el dispositivo donde realmente
ocurre.

**Qué lo confirma.** La acción principal no está disponible sin abrir dos niveles de menú; hay
que hacer scroll horizontal para leer datos esenciales; el envío queda bajo el teclado.

**Falsos positivos.** **No audites breakpoints por sí mismos** ni reportes diferencias de
composición que no cambian lo que se puede hacer. Eso es `visual-consistency` o `adaptive-layout`
según el caso.

**Corrección a.** `adaptive-layout`. `ux-audit` registra el hallazgo y su costo; no rediseña el
responsive.

---

## Accesibilidad observable

**Qué observar.** Lo que se puede comprobar mirando y usando: contraste insuficiente para leer,
controles sin nombre accesible, foco invisible o perdido, orden de tabulación ilógico, elementos
inalcanzables por teclado, información comunicada solo por color, objetivos táctiles demasiado
pequeños, texto que no soporta zoom.

**Qué cuesta.** Parte de las personas simplemente no puede completar la tarea.

**Qué lo confirma.** Medición o interacción directa. Sin ella, se declara `No verificado`.

**Falsos positivos.** Una auditoría WCAG completa es otro trabajo y no se simula aquí. **No
declares conformidad**: se reportan barreras observadas, no niveles de cumplimiento.

**Corrección a.** `interface-craft` para tratamiento visual y foco; `engineering-workflow` para
semántica, nombres accesibles y teclado.
