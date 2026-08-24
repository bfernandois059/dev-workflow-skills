# Decisiones de interfaz — <proyecto>

Registro de las convenciones visuales y de interacción **ya decididas**. Vive en el repositorio
y se referencia desde `AGENTS.md` para que lo herede cualquier agente que trabaje aquí.

**Qué entra**: convenciones — vocabulario compartido que se hereda.
**Qué no entra**: respuestas — cómo se resolvió una pantalla concreta. Eso se puede superar.
**Regla de tamaño**: si una entrada solo aplica en un lugar y nada la va a heredar, no entra.

Una decisión `Cerrada` no significa "correcta para siempre": significa **"ya se decidió, y
reabrirla cuesta"**. Se reabre con un motivo real —requisito nuevo, evidencia medida de que
falla, un caso que no encaja y se repite—, nunca porque el estándar de alrededor haya subido.

Si el caso no encaja en el vocabulario existente, **no reabras: extiende**. Propón una pieza
nueva y anótala aquí.

---

## Registro

| ID | Decisión | Ámbito | Estado | Fecha | Origen |
|---|---|---|---|---|---|
| UXD-01 | <la convención, en una frase que se pueda aplicar sin interpretar> | <componente · familia · global> | Cerrada | AAAA-MM-DD | <tarea o auditoría> |
| UXD-02 | … | … | Cerrada | | |

Estados: `Cerrada` · `Propuesta` (esperando decisión del usuario) · `Reabierta` (con motivo
declarado abajo) · `Reemplazada por UXD-NN`.

---

## Detalle de las entradas

### UXD-01 · <nombre corto de la convención>

**Decisión** — <qué se hace, concreto y con valores>
**Por qué** — <la razón. Es lo que permite saber después si sigue siendo válida>
**Ámbito** — <dónde aplica y qué hereda de ella>
**Excepciones nombradas** — <los casos en que no aplica, si los hay>
**Origen** — <auditoría o tarea de la que salió>

---

## Movimientos

Historial de reaperturas y extensiones. Sirve para ver si una convención se está reabriendo
demasiado, que casi siempre significa que estaba mal planteada.

| Fecha | ID | Movimiento | Motivo |
|---|---|---|---|
| AAAA-MM-DD | UXD-0N | Reabierta / Extendida / Reemplazada | <qué cambió en el contexto> |
