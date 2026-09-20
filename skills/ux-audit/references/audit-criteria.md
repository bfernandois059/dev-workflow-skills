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
- [Fricción y protección](#fricción-y-protección)
- [Contexto y memoria](#contexto-y-memoria)
- [Automatización y control](#automatización-y-control)
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

**Qué observar.** Cuál es la acción principal y si se distingue con claridad de las demás. Si las
decisiones se solicitan en el momento oportuno, cuando la persona ya dispone de información suficiente
para decidir (*Ask for a decision when the person has enough information to make it*). Acciones ambiguas
por su etiqueta. Acciones equivalentes ofrecidas en lugares distintos con nombres divergentes. Opciones
múltiples: si están jerarquizadas o si compiten dispersando la atención (*Reduce decision ambiguity,
not necessarily the number of choices*).

**Qué cuesta.** Decisión incorrecta, desinformada o prematura; retrocesos continuos; parálisis ante
ambigüedad; clics de prueba y error; acciones ejecutadas por descarte o sin comprender consecuencias.

**Qué lo confirma.** Dos o más botones con idéntico peso visual compitiendo por ser el principal; exigir
seleccionar un plan o confirmar una suscripción antes de mostrar el precio o las restricciones; una
etiqueta que no anticipa el efecto de la acción (`Continuar` cuando bifurca caminos); la acción más
frecuente escondida entre secundarias.

**Falsos positivos.** Que dos acciones se vean parecidas no basta: hay que demostrar que inducen a error o
impiden encontrar la correcta. Múltiples opciones visibles no son un defecto si son necesarias,
pertenecen a un entorno operacional, permiten comparar o están organizadas con claridad. No ocultes
opciones útiles solo para vaciar la pantalla. La sola presencia de un dropdown o menú no es un
defecto si no genera costo demostrado (*Audit the cost to the task, not the presence of a pattern*).

**Corrección a.** `interface-craft`. Si la elección de qué debe dominar sigue abierta,
`design-directions`.

---

## Fricción y protección

**Qué observar.** Si cada paso o interacción adicional es fricción accidental (pedir datos dos veces,
reconstruir filtros al volver, menús anidados innecesarios) o fricción protectora/necesaria (confirmar
acciones destructivas, verificar montos y destinatarios antes de transferir, advertir sobre cambios de
permisos a terceros, pasos regulatorios). Si se eliminaron avisos críticos para "hacer el flujo más corto"
o si se interrumpen acciones seguras con confirmaciones innecesarias.

**Qué cuesta.** La fricción accidental produce fatiga, demoras, errores por frustración y abandono. La
falta de fricción protectora induce errores graves, pérdidas de datos irreparables y acciones
involuntarias. El exceso de confirmaciones inocuas entrena el clic reflejo ignorando los avisos.

**Qué lo confirma.** Pasos redundantes sin valor para la tarea; eliminación de resguardos en acciones
irreversibles bajo el pretexto de simplificar; interrupciones modales innecesarias en operaciones reversibles
de bajo impacto donde un mecanismo de deshacer (`undo`) visible y confiable ya ofrece recuperación suficiente.

**Falsos positivos.** Un flujo con más pasos o clics no es automáticamente peor (*Interaction count is
evidence of effort, not a quality score*). Un paso de verificación o confirmación antes de una acción de alto
impacto no es un defecto: es fricción protectora deseable (*Friction is a cost to evaluate, not automatically a
defect to remove*). Tampoco asumas que toda acción reversible prescinde de resguardos ni que toda acción
irreversible exige dogmáticamente un diálogo modal. No evalúes con reglas ciegas de "menos pasos siempre es mejor".

**Corrección a.** `interface-craft` para rediseño del diálogo o secuencia; `engineering-workflow` si exige
implementar reversibilidad (`undo`) o modificar validaciones del dominio.

---

## Contexto y memoria

**Qué observar.** Si para decidir o continuar la persona debe recordar información de pantallas previas
(dirección, montos, restricciones, datos de clientes). Si el sistema oculta información que ya conoce
(*Do not make the user remember information the interface already knows when that memory is required to
continue the task*). Si al navegar o volver al listado se preservan filtros, scroll, selección y
borradores en curso (*Keep decision-relevant context available where the decision is made*).

**Qué cuesta.** Pérdida de contexto, relecturas, necesidad de retroceder para consultar datos, trabajo
repetido reconstruyendo filtros o selecciones, decisiones a ciegas por suposición.

**Qué lo confirma.** La persona debe memorizar cifras o selecciones del paso 1 para operar en el paso 4;
volver al listado resetea filtros y posición; abandonar temporalmente un formulario borra lo ingresado;
la entidad activa no se indica en el encabezado.

**Falsos positivos.** No se requiere duplicar toda la pantalla previa: basta con mantener accesible el
contexto relevante para la decisión (resumen persistente, etiqueta, breadcrumb). Tampoco se exige
persistencia infinita en caché para datos efímeros.

**Corrección a.** `interface-craft` para resúmenes contextuales y etiquetas persistentes;
`engineering-workflow` para persistencia de estado en URL o almacenamiento.

---

## Automatización y control

**Qué observar.** Defaults aplicados, autocompletados, selecciones sugeridas y guardados automáticos. Si la
automatización ahorra trabajo sin ocultar decisiones consecuentes (*Automation is helpful when it removes
work without hiding consequential decisions*). Si la persona puede ver con claridad qué ocurrió y
corregirlo fácilmente.

**Qué cuesta.** Sorpresas operativas, envíos no deseados, cobros accidentales o dificultad para corregir
selecciones impuestas por el sistema.

**Qué lo confirma.** Opciones preseleccionadas que generan cobros o permisos adicionales sin aviso
visible; guardado automático de cambios destructivos sin historial ni undo; automatizaciones que no
permiten override manual.

**Falsos positivos.** Preseleccionar una opción habitual inocua (como la moneda local o el método de envío
estándar) es una buena práctica de eficiencia si es visible y editable. No todo default es manipulación.

**Corrección a.** `interface-craft` para visibilidad del estado y controles de corrección;
`engineering-workflow` para lógica de defaults y reversibilidad.

---

## Feedback y system status

**Qué observar.** Si toda acción produce respuesta visible, si las esperas perceptibles tienen
indicador proporcional a la incertidumbre (*Add feedback when uncertainty has a cost; do not add
feedback as decoration*), si el resultado se confirma de forma que se pueda creer, y si el sistema
comunica en qué estado está un proceso cuando eso condiciona el siguiente paso.

**Qué cuesta.** Doble envío, duplicados en base de datos, reintentos innecesarios, incertidumbre
sobre si el trabajo se guardó o si la transacción sigue en curso.

**Qué lo confirma.** El botón no cambia al pulsarse; tras guardar no aparece nada o aparece algo
que desaparece antes de leerse; una operación asíncrona larga no informa progreso; el estado del
registro no coincide con lo que la interfaz sugiere.

**Falsos positivos.** No toda acción necesita un mensaje o spinner: un cambio visible inmediato **es**
feedback suficiente. Un toast o modal adicional sobre un cambio ya evidente es ruido y adorno. No
impongas umbrales temporales universales para exigir feedback.

**Corrección a.** `interface-craft` para el tratamiento visual; `engineering-workflow` si falta el
estado o el manejo asíncrono.

---

## Errores y recuperación

**Qué observar.** Qué se hace para que el error no ocurra, qué pasa cuando ocurre y qué tan caro
es recuperarse. Sigue el orden: evitar el error cuando sea razonable → detectar → explicar con claridad
→ preservar trabajo ingresado → ofrecer camino de recuperación. Pregunta central: **¿qué cuesta
equivocarse y qué tan fácil es recuperarse?**

**Qué cuesta.** Trabajo perdido, retrabajo completo, abandono en el punto más caro del flujo,
desconfianza duradera.

**Qué lo confirma.** El error aparece solo al enviar; el formulario vuelve arriba sin indicar el
campo; los datos ingresados se borran; el texto es genérico (*"Ocurrió un error"*) o técnico; no hay
forma de reintentar sin empezar de nuevo.

**Falsos positivos.** Validar demasiado temprano —marcar en rojo un campo mientras se está
escribiendo— es un defecto propio, no prevención. Y un error de servidor legítimo no siempre puede
explicarse en detalle: el criterio es si la persona comprende qué hacer a continuación.

**Corrección a.** `interface-craft` para mensajes y ubicación; `engineering-workflow` para
persistencia, validación y manejo real del error.

---

## Confirmaciones

**Qué observar.** Qué se confirma y qué no. Si la confirmación dice **qué** se va a hacer, sobre qué
objeto concreto y qué consecuencias tendrá. Si se evalúa qué resguardo o fricción protectora proporcional
necesita la decisión ante acciones irreversibles o de alto impacto, o si hay confirmaciones redundantes en
acciones inocuas.

**Qué cuesta.** Confirmar por reflejo anula la protección; confirmar todo entrena a ignorar los
diálogos; no resguardar acciones irreversibles o de alto impacto produce pérdidas reales de datos o dinero.

**Qué lo confirma.** Un diálogo genérico (*"¿Estás seguro?"*) sin nombrar el objeto ni sus efectos;
acciones reversibles de bajo impacto que interrumpen con modales innecesarios cuando un deshacer confiable
alcanza; acciones destructivas o irreversibles que se ejecutan al primer clic sin ningún resguardo proporcional.

**Falsos positivos.** En acciones reversibles, un mecanismo de deshacer visible y confiable puede reducir
o reemplazar la necesidad de confirmación previa cuando el costo del error y la recuperación lo permiten;
pero si el error produce consecuencias operacionales graves o la recuperación es costosa, la protección previa
puede seguir justificada. En acciones irreversibles o de alto impacto, evalúa qué fricción protectora
proporcional necesita la decisión: una confirmación explícita es una estrategia posible, no una solución
universal (pudiendo existir pasos deliberados, separación física de acciones, ventanas de recuperación, papelera
o selección explícita del objeto). La pregunta clave sigue siendo: **¿qué cuesta equivocarse y qué tan fácil es
recuperarse?**

**Corrección a.** `interface-craft` para diseño del diálogo, resguardo o notificación; `engineering-workflow`
si hay que implementar deshacer, ventanas de recuperación o cambiar el comportamiento.

---

## Acciones destructivas

**Qué observar.** Si se distinguen claramente de las seguras antes del clic, si están separadas de
las frecuentes, si su alcance es evidente (si afecta a otros usuarios o a datos permanentes) y si
existe reversión. Evalúa: **¿qué cuesta equivocarse y qué tan fácil es recuperarse?**

**Qué cuesta.** Pérdida de datos permanente, trabajo irrecuperable, incidentes operativos críticos.

**Qué lo confirma.** Una acción destructiva con el mismo tratamiento que una segura o adyacente
a ella; el texto no dice qué se elimina ni si afecta a otros; no hay deshacer, papelera ni aviso de
irreversibilidad.

**Falsos positivos.** Que una acción destructiva sea visible no es el problema: en herramientas
operacionales muchas veces debe serlo. El problema es que **no se distinga**, que esté ubicada donde
se cometen clics erróneos o que su alcance real permanezca invisible.

**Corrección a.** `ux-audit` mantiene el hallazgo —es prevención de error y costo real, no estética—;
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

**Qué observar.** Qué se pide y por qué; agrupación semántica; labels visibles; ayuda contextual;
obligatoriedad; defaults razonables; momento de la validación; mensajes de error; persistencia tras
fallo; prevención de pérdida al salir; submit; loading; éxito y recuperación.

**Qué cuesta.** Abandono proporcional al esfuerzo y a la sensación de intrusión; retrabajo
completo cuando el error borra lo escrito o el formulario vuelve arriba sin indicar qué falló.

**Qué lo confirma.** Campos cuyo uso no se explica y no es obvio; labels solo en `placeholder`
—que desaparecen al escribir—; validación únicamente al enviar; mensaje lejos del campo; salida
accidental sin aviso con trabajo dentro.

**Falsos positivos.** Muchos campos no es automáticamente un defecto: un trámite administrativo o
legal legítimo puede necesitarlos. El hallazgo es pedir datos **que no se usan**, pedirlos **antes
de tiempo** o no agrupar lo que conceptualmente va junto. No elimines campos necesarios del dominio
solo por "hacer el formulario más corto". **No cambies reglas de obligatoriedad ni reglas
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

**Qué cuesta.** Tiempo acumulado, errores por fatiga operativa, rechazo de la herramienta.

**Qué lo confirma.** Volver al listado obliga a reconstruir el contexto; una acción diaria exige
tres navegaciones; hay que salir de la pantalla para ver algo que se necesita junto; lo que
se hace en lote solo puede hacerse de a uno.

**Falsos positivos.** Un flujo largo para una tarea **ocasional** no es un problema de
eficiencia. **La frecuencia debe estar respaldada por evidencia** (contexto del usuario,
telemetría, manuales operativos); no asumas que "los usuarios hacen esto todo el día" sin datos. Si
no hay certeza de la frecuencia, plantéalo explícitamente como hipótesis.

**Corrección a.** `interface-craft`; `component-architecture` si el patrón compartido lo causa;
`engineering-workflow` para persistencia de estado y operaciones en lote.

---

## CRM, intranets y sistemas operacionales

**Qué observar.** Densidad útil, escaneabilidad, comparación entre registros, información
contextual disponible sin cambiar de pantalla, jerarquía de acciones frecuentes, continuidad al
navegar, disclosure de lo secundario. Recuerda: **Operational simplicity means less work, not
necessarily less information.**

**Qué cuesta.** El trabajo acumulado por sesión, que es la métrica real de estas herramientas.

**Qué lo confirma.** Se ven menos registros de los que la tarea necesita comparar; datos que
siempre se consultan juntos están en pestañas distintas; la acción más frecuente está escondida;
cada operación exige reconstruir el contexto.

**Falsos positivos.** **No recomiendes "más aire", "menos información" ni "una acción por
pantalla" por estética.** Una pantalla densa no es un defecto: el defecto es densidad **sin
jerarquía**. Antes de proponer eliminar información o acciones necesarias, el orden es: jerarquía
→ agrupación semántica → disclosure progresivo → densidad.

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
veces; momento en que aparecen costos de envío e impuestos; recuperación cuando un pago falla. Ten
presente: **A shorter flow is not better if it makes the decision less informed.**

**Qué cuesta.** Abandono en el punto de mayor intención, y en el peor momento del embudo.

**Qué lo confirma.** El costo total solo se conoce al final; hay que registrarse antes de saber
si conviene; la dirección se pide dos veces; un error de pago vacía el carrito o el formulario;
no se sabe qué pasa después de pagar.

**Falsos positivos.** **No inventes impacto en conversión, lift ni benchmarks.** Describe la
fricción y su costo, no un número. Y no alteres el flujo comercial real —pasos legales, medios
de pago, políticas de seguridad o confirmación obligatoria— para simplificar de forma irresponsable.

**Corrección a.** `interface-craft`; `engineering-workflow` para el flujo, la persistencia y los
estados de pago.

---

## Sitios comerciales

**Qué observar.** Claridad de la oferta, objeciones previsibles sin responder, información
suficiente para dar el siguiente paso, coherencia entre la promesa y lo que ocurre al hacer
clic, y cuánta fricción hay antes de la acción principal. Recuerda: **A business outcome does not
replace user-task evidence.** Si observas manipulación o presión (opciones de rechazo camufladas,
costos tardíos forzados, falsa urgencia observable, suscripciones difíciles de cancelar), registra
el costo para la autonomía del usuario sin atribuir intención maliciosa.

**Qué cuesta.** Contactos que no ocurren, consultas mal calificadas, decisiones involuntarias o
arrepentimiento comercial que se pagan después.

**Qué lo confirma.** No se entiende qué se ofrece sin leer tres secciones; el formulario pide más
de lo necesario para un primer contacto; el CTA promete algo distinto de lo que abre; no hay
forma de saber si el servicio aplica al caso de quien mira.

**Falsos positivos.** La cantidad de secciones o el largo de la página no son hallazgos por sí
mismos, y **tampoco inventes cifras comerciales**. No asumas que más conversión equivale a mejor
experiencia si se logra ocultando condiciones.

**Corrección a.** `interface-craft`; `design-directions` cuando lo que falta decidir es el
enfoque de la página.

---

## Móvil cuando afecta la tarea

**Qué observar.** Solo lo que cambia la capacidad de completar la tarea: acciones que
desaparecen o quedan a dos menús de distancia, contenido que exige comparación y ya no cabe,
teclado que tapa el campo o el botón de envío, elementos fijos que ocupan la pantalla, objetivos
táctiles inalcanzables. Principio rector: **Device or viewport does not prove user intent.** No
asumas que el usuario en móvil tiene menos intención, requiere menos datos o está siempre apurado.

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
