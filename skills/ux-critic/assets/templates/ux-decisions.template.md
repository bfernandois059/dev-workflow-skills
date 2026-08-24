# Decisiones de interfaz — <proyecto>

**Memoria de las soluciones de interfaz ya validadas**: las que el crítico propuso, se
aceptaron y funcionaron. Vive en el repositorio y se referencia desde `AGENTS.md` para que la
herede cualquier agente que trabaje aquí.

Este registro **no congela nada**. El listón solo sube: si una solución registrada puede
mejorarse, se mejora. Lo que exige un motivo es el movimiento **lateral** —sustituirla por otra
equivalente—, porque eso no mejora nada y deshace trabajo aceptado.

**Nace vacío.** No se siembra desde el `PRD` ni desde la documentación funcional: si una regla
ya vive ahí, ahí se queda y aquí se referencia. Una entrada aparece cuando una corrección
concreta se acepta.

**Dos pruebas antes de anotar:**
- *La inversa* — escribe lo contrario. Si el contrario es absurdo, es un principio y no entra.
- *Aplicabilidad* — ¿alguien puede comprobarla al escribir el componente, sin interpretar?

**Regla de tamaño**: si solo aplica en un lugar y nada la va a heredar, es un detalle de
implementación y no entra.

---

## Registro

| ID | Solución | Elemento y ámbito | Aparece en | Estado | Fecha | Origen |
|---|---|---|---|---|---|---|
| UXD-01 | <la convención, aplicable sin interpretar> | <componente · familia · global> | <rutas o vistas donde vive> | Validada | AAAA-MM-DD | <tarea de la que salió> |

Estados: `Validada` (aceptada y funcionando) · `Propuesta` (esperando decisión del usuario) ·
`Elevada por UXD-NN` (una versión mejor la reemplazó) · `Retirada` (con motivo abajo).

---

## Detalle de las entradas

### UXD-01 · <nombre corto de la convención>

**Solución** — <qué se hace, concreto y con valores>
**Por qué** — <la razón. Es lo que permite saber después si sigue siendo válida>
**Elemento** — <el componente o patrón. Al nivel del elemento, no de la pantalla>
**Aparece en** — <dónde vive hoy. Es el punto de partida de la próxima propagación>
**Excepciones nombradas** — <los casos en que no aplica, si los hay>
**Origen** — <la tarea de corrección de la que salió>

---

## Movimientos

Historial de elevaciones, extensiones y retiros. Sirve para ver si una entrada se está moviendo
demasiado, que casi siempre significa que estaba mal planteada.

| Fecha | ID | Movimiento | Motivo |
|---|---|---|---|
| AAAA-MM-DD | UXD-0N | Elevada / Extendida / Retirada | <qué cambió, o qué mejora la superó> |
