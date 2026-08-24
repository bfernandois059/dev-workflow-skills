# Decision Ledger

El registro de decisiones de interfaz del proyecto. Es lo que hace que dos auditorías separadas
por semanas —o dos agentes distintos— no se contradigan.

## El problema que resuelve

Una crítica sin registro tiene memoria de los problemas y ninguna de las resoluciones. Cada
pasada juzga desde cero, y como el resto de la pantalla mejoró, el estándar se movió: el mismo
bloque, con el mismo código, recibe un veredicto distinto. Lo que se corrigió en la ola 1 se
"corrige" otra vez en la ola 3, en dirección contraria.

Es el mismo mecanismo que hace valioso un sistema de diseño, y por la razón menos obvia: su
valor no es la taxonomía, es que **la decisión tiene un solo lugar y se hereda**. La coherencia
deja de depender del criterio de cada quien.

## Dónde vive

En **el repositorio del proyecto**, no en la skill: `docs/ux-decisions.md`, referenciado desde
`AGENTS.md`. Así lo hereda cualquier agente que trabaje ahí, no solo el que corra `ux-critic`.
Plantilla en [`../assets/templates/ux-decisions.template.md`](../assets/templates/ux-decisions.template.md).

---

## Qué se anota y qué no

La distinción que evita que el registro se convierta en una máquina de timidez:

| Sí entra — **convenciones** | No entra — **respuestas** |
|---|---|
| Vocabulario compartido, arbitrario en sí mismo, valioso porque se comparte | Cómo se resolvió una pantalla concreta |
| "Los bloques de contexto usan patrón tarjeta: borde completo, radio, `p-4`, sin sombra" | "La sección de documentos se resuelve con una lista de seis filas y estado por fila" |
| Se hereda: define cómo se construye lo siguiente | Es una solución, y **una solución se puede superar** |

Una convención re-litigada produce churn sin ganancia. Una respuesta re-examinada es el trabajo
del crítico. El registro guarda lo primero y deja lo segundo abierto.

**Regla de tamaño**: si una entrada solo aplica en un lugar y nada la va a heredar, no es una
decisión — es un detalle de implementación y no entra. Una plataforma mediana debería tener del
orden de diez a veinte entradas. Si crece mucho más, se están anotando respuestas.

Esto **no contradice** el principio de que lo documentado no prueba que esté bien. Ese
principio protege contra tratar una decisión previa como correcta por el hecho de existir. El
registro no dice "esto es correcto": dice "esto ya se decidió, y reabrirlo cuesta".

---

## Las dos operaciones

Un registro con una sola operación —"respetar"— paraliza. Con dos, genera.

### Reabrir — caro, exige motivo

Una decisión cerrada **no se reabre por gusto ni por deriva de estándar**. Que el resto de la
pantalla haya mejorado y el bloque ahora "se vea" peor no es motivo: el estándar se movió, el
bloque no.

Sí son motivos válidos:

- un requisito nuevo que la convención no contemplaba;
- evidencia observada de que la convención falla — medida, no impresión;
- un caso real que no encaja y que se repite.

Un hallazgo que contradice una decisión cerrada **no se reporta como hallazgo**. Se reporta
como **propuesta de cambio de decisión**, en su propia sección, diciendo qué cambió en el
contexto. Decide el usuario, no el crítico.

### Extender — barato, se fomenta

Si el caso no encaja en el vocabulario existente, la respuesta correcta **no es reabrir una
decisión: es proponer una pieza nueva** y anotarla, para que exista la próxima vez.

Este es el punto que evita la parálisis. Los átomos cerrados no frenan la composición: la
abaratan. Se deja de renegociar el botón y se compone más libre.

> **Caso real.** Una corrección destrozó un bloque de aviso aplanándolo a medias porque el
> sistema solo tenía dos piezas: "tarjeta" y "nada". Le faltaba una tercera. Con la entrada
> escrita —*patrón `aviso`: fondo tenue, acento a la izquierda, `p-4`, sin borde completo*— el
> error no ocurre; no porque esté prohibido tocar el bloque, sino porque **existía la pieza
> correcta**.

Proponer una pieza nueva es el nivel de intervención **`Pieza nueva de sistema`**. Se propaga,
así que es un compromiso de producto y no un arreglo de pantalla: va a la sección
*Decisiones que necesitas tomar*, nombrando dónde más aplicaría. El crítico propone
vocabulario; no se lo autoconcede.

---

## Cómo se usa en el flujo

**Fase 0 — se lee.** Antes de juzgar nada. Una decisión cerrada es contexto, no está en
discusión. Si el proyecto no tiene registro, se dice y se ofrece crearlo con las decisiones que
salgan de esta auditoría.

**Fase 2 — se contrasta.** Cada hallazgo se cruza con el registro antes de escribirse. Si lo
contradice, cambia de sección: pasa a propuesta de cambio de decisión.

**Fase 5 — se declara.** El informe lista qué decisiones cerradas tocó, cuáles propone reabrir
y qué piezas nuevas propone. El bloque de verificación lleva la fila correspondiente.

**Fase 6 — se escribe.** Cuando el usuario acepta una corrección, la decisión entra al registro
**en el nivel del componente, no de la pantalla**, con su ámbito. Una corrección aceptada que
no se anota es una decisión que se va a volver a discutir.

---

## Reglas de alcance en la corrección

Derivadas del mismo problema:

- **Una corrección no toca lo ya corregido y aceptado en una ola anterior.** Si al implementar
  aparece la tentación de ajustar un bloque vecino que ya está cerrado, eso no es parte de la
  tarea: es una tarea nueva, y se declara. Deshacer trabajo aceptado obliga al usuario a
  revisar lo que ya había dado por cerrado.
- **Una tarea que toca una decisión cerrada avisa antes de implementar**, nombrando la entrada:
  *"esta tarea modifica `UXD-01`, que está cerrada — ¿confirmas?"*. El usuario no debería tener
  que descubrirlo leyendo el diff.
- El campo `Fuera de alcance` de la ficha de tarea **nombra explícitamente** los bloques
  vecinos que no se tocan cuando hay riesgo de arrastre.
