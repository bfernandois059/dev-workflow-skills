# Plan de corrección de interfaz — <alcance>

> Generado por `ux-critic` el <fecha>. Cada tarea es autocontenida: se puede tomar suelta,
> pasar a `engineering-workflow` o entregar a otro agente sin volver a leer el informe.

**Contexto** — Producto: … · Usuario: … · Tarea principal: … · Etapa: … · Exigencia: nivel N
**Origen** — Informe: `<ruta o fecha>` · Hallazgos cubiertos: <ids>

## Orden de ejecución

| Ola | Tareas | Por qué en este orden |
|---|---|---|
| 1 · Estructura | UX-01, UX-02 | Colapsar contenedores antes de tocar nada más: mueve todo lo demás |
| 2 · Jerarquía y acciones | UX-03, UX-04 | Con la estructura fija, se decide qué domina y qué acción manda |
| 3 · Contenido y estados | UX-05 | Copy y estados sobre la estructura ya definida |
| 4 · Detalle | UX-06 | Último: pulir lo que ya no se va a mover |

**Reglas**: no empezar una ola sin cerrar la anterior — pulir antes de reestructurar es
trabajo que se tira. Y una tarea sin `Dónde` y sin criterio de aceptación verificable no entra
al plan: se queda como hallazgo hasta que alguien pueda localizarla.

---

## UX-01 — <título imperativo, una línea>

| | |
|---|---|
| **Capa** | 2 · Jerarquía |
| **Severidad** | P1 |
| **Intervención** | Rediseño de bloque |
| **Esfuerzo** | Bajo |
| **Riesgo** | Bajo — solo presentación, sin cambio de comportamiento |
| **Depende de** | — |

**Problema** — <una o dos frases, con la evidencia medida u observada>

**Dónde** — `<componente / archivo / ruta>`

**Qué cambia**
- <cambio concreto 1>
- <cambio concreto 2>

**Estructura objetivo**

```
❌ Antes                         ✅ Después
<árbol de contenedores>          <árbol de contenedores>
```

**Criterio de aceptación**
- [ ] <verificable a ojo o medible: "ninguna superficie anidada a más de 2 niveles">
- [ ] <verificable: "un solo título en la pestaña, sin repetir el nombre de la pestaña">
- [ ] Sin regresión: <lo que debe seguir funcionando igual>

**Fuera de alcance** — <lo que esta tarea NO toca, para que no crezca>

---

## UX-02 — …

<repetir la ficha>

---

## Tareas de sistema (transversales)

Cuando el mismo problema aparece en varias pantallas, se corrige una vez en el componente
compartido y se lista dónde se verifica.

## UX-0N — <título>

| | |
|---|---|
| **Alcance** | Componente compartido `<nombre>` |
| **Aparece en** | `<pantalla 1>`, `<pantalla 2>`, `<pantalla 3>` |

**Qué cambia** — <la regla que pasa a aplicar el componente>

**Criterio de aceptación**
- [ ] Verificado en cada pantalla listada
- [ ] Ninguna pantalla mantiene la variante antigua

---

## Decisiones que necesitas tomar

Lo que no se puede corregir sin una definición de producto o de negocio. No son tareas: son
preguntas que bloquean tareas. **Van redactadas como preguntas**, no como diagnóstico en
tercera persona, y con opciones que se puedan responder con una letra.

| # | Pregunta | Bloquea | Opciones |
|---|---|---|---|
| D1 | ¿…? | UX-0X | A: … · B: … |

Una tarea bloqueada por una decisión se marca `Bloqueada por D<n>` en su ficha y **no arranca**
hasta que la decisión exista. Dejar la pregunta enterrada en el campo `Depende de` es
disfrazarla de tarea: ahí no la ve nadie.

## Verificación final

Al cerrar todas las olas, repetir sobre la interfaz corregida:

- [ ] Inventario objetivo (`scripts/ui_inventory.js`) en los mismos viewports que la auditoría
- [ ] Recorrido limpio de la tarea principal, sin mirar el plan
- [ ] Comparación antes/después de las capturas de las pantallas tocadas
