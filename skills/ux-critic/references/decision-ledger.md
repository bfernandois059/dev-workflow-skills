# Decision Ledger

**La memoria del crítico sobre sus propias soluciones ya validadas.** No es un reglamento del
proyecto, ni una carta fundacional, ni un resumen del PRD.

## Los dos problemas que resuelve

**Re-litigar lo resuelto.** Una crítica sin memoria juzga desde cero cada vez. Como el resto de
la pantalla mejoró, el estándar se movió, y el mismo bloque —con el mismo código— recibe un
veredicto contrario al de la pasada anterior. Lo que se corrigió en la ola 1 se "corrige" otra
vez en la ola 3, en dirección opuesta.

**El arreglo que no se propaga.** Se corrige un elemento en una pantalla y el mismo elemento
sigue viejo en las otras cinco donde aparece. El sistema queda más incoherente que antes, y el
único que lo descubre es quien hace QA a mano.

## Lo que NO es

Este registro **no congela nada**. El error opuesto —una definición tomada al principio que
queda escrita e intocable para siempre— es exactamente lo que vuelve tímidas a las auditorías,
y es lo que esta skill existe para evitar. Aquí **el listón solo sube**.

Tampoco es documentación de producto. Si una regla ya vive en el `PRD`, en `AGENTS.md` o en la
documentación funcional, **ahí se queda**: se referencia, no se copia. Un registro que resume
el PRD no es un registro, es un duplicado que va a divergir.

---

## Cómo nace y qué entra

**Nace vacío.** No se siembra desde ninguna fuente. Una entrada aparece cuando el crítico
propone una solución, el usuario la acepta, y funciona. Si estás creando el registro en un
proyecto que ya tuvo correcciones, las primeras entradas son **las convenciones que
establecieron esas correcciones**, no un inventario de principios.

Cada entrada se anota **al nivel del elemento**, no de la pantalla — es lo que permite que se
herede y se propague.

### Las dos pruebas

**Prueba de la inversa.** Escribe lo contrario de la entrada. Si el contrario es absurdo, no es
una convención: es un principio, y no restringe nada.

| Entrada | Su contrario | ¿Entra? |
|---|---|---|
| "La interfaz usa un lenguaje sobrio y claro" | "usa un lenguaje confuso y denso" | ❌ Nadie defiende el contrario |
| "Los bloques de contexto usan borde completo, radio y `p-4`" | "van sin borde, solo separados por espacio" | ✅ Alternativa legítima; se eligió una |

**Prueba de aplicabilidad.** ¿Alguien a punto de escribir el componente puede comprobar si la
cumple, sin interpretar? Si hace falta interpretar, no entra.

**Regla de tamaño.** Si una entrada solo aplica en un lugar y nada la va a heredar, es un
detalle de implementación y no entra. La regla limita la **cantidad**, no la especificidad: la
forma de quedarse en pocas entradas es ser específico sobre pocas cosas, no vago sobre todas.

---

## Las dos reglas de uso

### El listón solo sube

Una solución registrada **no es un techo**. Si lo que estaba `Sólido` puede llegar a
`Referencia`, adelante — eso es el trabajo del crítico. Nada en este registro impide mejorar.

### Cambiar de lado exige motivo

Lo que sí se prohíbe es el movimiento **lateral**: sustituir una solución que funciona por otra
equivalente. No es una mejora, es churn — deshace trabajo aceptado, obliga a revisar lo que ya
estaba cerrado y deja el sistema donde estaba.

Motivos válidos para cambiar de lado: un requisito nuevo, evidencia observada de que la
solución falla, o un caso real que no encaja y se repite. **No es motivo** que el resto de la
pantalla haya mejorado y el bloque ahora "se vea" peor: el estándar se movió, el bloque no.

Cuando un hallazgo propone un cambio lateral sin motivo, no se reporta como hallazgo. Se
descarta en la refutación, y se anota en el informe que se descartó.

Y si el caso simplemente no encaja en el vocabulario existente, la salida no es cambiar una
entrada: es **extender** — proponer la pieza que falta como `Pieza nueva de sistema`. Los
átomos cerrados no frenan la composición, la abaratan.

---

## Propagación

Es la mitad del valor del registro, y la que ahorra QA manual.

**Antes de proponer la corrección de un elemento, busca dónde más aparece ese elemento.** Si
aparece en más de un lugar, la corrección **no es de pantalla: es de sistema**. La tarea nombra
todas las apariciones y su criterio de verificación cubre cada una.

Aplica en **todos los modos**, no solo en modo sitio. Auditar una sola pantalla no autoriza a
corregir un componente compartido dejándolo distinto en el resto: eso produce la incoherencia
que después alguien encuentra a mano.

La entrada del registro anota el ámbito y las apariciones conocidas, para que la próxima vez la
búsqueda empiece hecha.

---

## Cómo se usa en el flujo

**Fase 0 — se lee.** Antes de juzgar. Las soluciones registradas son contexto: no se
re-inventan, se elevan si hay margen.

**Fase 2 — se contrasta.** Cada hallazgo se cruza con el registro. Si propone un cambio lateral
sin motivo, se descarta. Si propone subir el nivel, sigue siendo un hallazgo válido.

**Fase 5 — se declara.** El informe dice qué entradas tocó, cuáles propone elevar y qué piezas
nuevas propone.

**Fase 6 — se escribe.** Cuando el usuario acepta una corrección, entra al registro con su
elemento, su ámbito y sus apariciones. Una corrección aceptada que no se anota es una decisión
que se va a volver a discutir.

---

## Reglas de alcance en la corrección

- **Una corrección no toca lo ya corregido y aceptado en una ola anterior.** Si al implementar
  aparece la tentación de ajustar un bloque vecino que ya está resuelto, no es parte de la
  tarea: es una tarea nueva y se declara.
- **Una tarea que modifica una entrada del registro avisa antes de implementar**, nombrándola:
  *"esta tarea modifica `UXD-01` — ¿confirmas?"*. El usuario no debería descubrirlo leyendo el
  diff.
- El campo `Fuera de alcance` de la ficha **nombra explícitamente** los bloques vecinos que no
  se tocan cuando hay riesgo de arrastre.
