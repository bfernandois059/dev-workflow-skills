# Guía de selección de skills

Fuente principal para decidir **qué skill usar para el problema actual**, cuándo no usarla y
quién toma el relevo después. No reemplaza a los `SKILL.md`: cada skill documenta su propio
método. Este documento solo resuelve el enrutamiento.

Para el contrato interno de la familia visual —qué reglas comparten las siete skills de
interfaz y por qué están separadas así— ver
**[docs/visual-skills-architecture.md](visual-skills-architecture.md)**.

Hoy existen **doce skills**, todas independientes e instalables por separado.

---

## Las tres reglas de selección

### 1. No hay pipeline obligatorio

Las skills son **herramientas especializadas**, no etapas de un proceso. No existe un recorrido
del tipo `project-blueprint → visual-foundation → design-directions → … → tech-cleanup` que haya
que completar. Encadenar todas por costumbre es el error más caro: cuesta tokens, tiempo y
produce entregas infladas con trabajo que nadie pidió.

> **Usa la skill que corresponde al problema actual, y agrega otra solo cuando aparezca una
> responsabilidad distinta.**

### 2. Una skill principal, y solo los apoyos necesarios

Una tarea normalmente tiene **una** skill principal. Los apoyos se suman de a uno, cuando el
problema los exige — no porque pertenezcan a la misma familia.

```text
Problema: la ficha móvil perdió la acción principal.

Principal:        adaptive-layout
Apoyo posible:    ux-audit, solo si primero hay que demostrar el costo sobre la tarea

No necesarios:    visual-foundation · design-directions
                  component-architecture · tailwind-hygiene
```

Que `tailwind-hygiene` sea una skill visual no la convierte en paso obligatorio de todo trabajo
visual.

### 3. Una tarea pequeña no necesita una skill

> **No invoques una skill compleja si la tarea se resuelve correctamente con una respuesta
> puntual.**

```text
"¿este padding se ve grande?"        → responde puntualmente
                                       (no abras visual-consistency)

"¿qué texto pondrías en este botón?" → responde puntualmente
                                       (no abras ux-audit)

"cambia este texto"                  → hazlo
                                       (no abras project-blueprint)
```

Las skills existen para subir la calidad donde hay **una clase de problema real**, no para
añadir proceso a cada interacción.

---

## Matriz de selección

| Necesidad real | Skill principal | No usar cuando… |
|---|---|---|
| Definir un producto o proyecto nuevo: arquitectura, stack y documentación inicial | `project-blueprint` | El proyecto ya tiene las decisiones que el cambio necesita, o la tarea es una implementación acotada |
| Implementar una tarea de desarrollo con alcance, rama, validación y PR | `engineering-workflow` | Es una consulta conceptual, un diagnóstico sin modificaciones o un ajuste local trivial y reversible |
| Definir o mantener la verdad visual del proyecto | `visual-foundation` | El problema es una pantalla concreta y las reglas ya existen: eso es `interface-craft` |
| Explorar caminos visuales antes de elegir uno | `design-directions` | La dirección ya está decidida —mockup aprobado, patrón fijado— o solo cambiaría color, radius o sombras |
| Diseñar, rediseñar o implementar una interfaz concreta | `interface-craft` | La interfaz ya está resuelta y solo falla por espacio o dispositivo: eso es `adaptive-layout` |
| Revisar si lo renderizado pertenece visualmente al producto | `visual-consistency` | El problema es que la persona no puede entender o completar la tarea: eso es `ux-audit` |
| Resolver cómo una interfaz se adapta entre tamaños | `adaptive-layout` | El mismo problema existe también en el viewport de origen: primero `interface-craft` |
| Consolidar responsabilidades y patrones compartidos en componentes | `component-architecture` | Todavía no está decidido cómo debe verse el patrón, o el problema es solo cómo están escritas las clases |
| Normalizar Tailwind sin cambiar la interfaz | `tailwind-hygiene` | El cambio alteraría el render, el responsive o un estado — deja de ser higiene |
| Auditar si una persona puede entender y completar una tarea | `ux-audit` | Solo hay deriva visual sin costo sobre la tarea, o lo que se busca es salud técnica del repo |
| Auditar salud general del repositorio: seguridad, SEO técnico y deuda amplia | `marcozen` | Lo que se audita es la experiencia de una persona, o ya está confirmado qué sobra y solo falta retirarlo |
| Eliminar código, dependencias, assets y archivos realmente sin uso | `tech-cleanup` | Todavía no está determinado qué sobra: eso es `marcozen` |

---

## Fronteras que más se confunden

### `visual-consistency` vs `ux-audit`

```text
visual-consistency → ¿se ve como este producto decidió verse?
ux-audit           → ¿la persona puede entender, decidir y completar la tarea?
```

| Caso | Skill |
|---|---|
| Gap distinto entre cards equivalentes | `visual-consistency` |
| `H1` de 38 px donde `ui-system.md` dice 40 | `visual-consistency` |
| Dos acciones visualmente iguales inducen una decisión incorrecta | `ux-audit` |
| El botón destructivo no se distingue de uno seguro | `ux-audit` |

Un defecto visual pasa a `ux-audit` **solo cuando tiene costo demostrable sobre la tarea**.

### `design-directions` vs `interface-craft`

```text
todavía no sabemos qué dirección tomar → design-directions
la dirección ya está decidida          → interface-craft
```

No uses `design-directions` para generar opciones falsas cuando hay mockup aprobado. Que exista
un sistema visual cerrado tampoco significa que cada pantalla esté diseñada: si queda una
decisión estructural abierta dentro de ese sistema, `design-directions` sigue aplicando.

### `interface-craft` vs `adaptive-layout`

```text
el problema existe también en desktop/origen        → interface-craft
la solución es correcta en origen pero falla
por espacio o dispositivo                           → adaptive-layout
```

Adaptar una pantalla mal resuelta produce dos pantallas mal resueltas.

### `interface-craft` vs `component-architecture`

```text
hay que diseñar o corregir el patrón            → interface-craft
el patrón ya está resuelto y debe existir
una sola vez                                    → component-architecture
```

`component-architecture` consolida decisiones resueltas; no las toma.

### `component-architecture` vs `tailwind-hygiene`

```text
la responsabilidad está duplicada               → component-architecture
la responsabilidad es correcta pero las clases
expresan la misma decisión de forma
innecesariamente inconsistente                  → tailwind-hygiene
```

### `ux-audit` vs `marcozen`

```text
experiencia de una persona completando una tarea → ux-audit
salud transversal del repositorio o del producto → marcozen
```

`marcozen` no es una auditoría de UX, y `ux-audit` no es una auditoría técnica general.

### `marcozen` vs `tech-cleanup`

```text
determinar qué deuda o riesgo existe            → marcozen
retirar elementos confirmados como innecesarios → tech-cleanup
```

`tech-cleanup` también tiene su propia fase de detección con evidencia: no exige una auditoría
previa de `marcozen` para empezar. La diferencia es el objeto — `marcozen` juzga orden,
gobernanza y riesgo; `tech-cleanup` demuestra que algo no se usa y lo elimina por etapas.

---

## Auditoría no es corrección

Tres skills son principalmente de **diagnóstico**:

```text
visual-consistency   revisión visual de lo renderizado   solo lectura
ux-audit             experiencia sobre la tarea real     solo lectura
marcozen             salud del repositorio y del producto
```

Entregan hallazgos y dirección de corrección. **La implementación pasa a quien corresponda.**

Una auditoría no tiene que terminar inmediatamente en implementación: un informe leído y
priorizado es un resultado completo.

---

## Flujos recomendados

Son ejemplos de composición, **no pipelines obligatorios**. Cada flecha es una decisión que
alguien toma, no un paso automático.

### Proyecto nuevo

```text
project-blueprint
→ visual-foundation        cuando existe trabajo visual real
→ design-directions        solo si la dirección sigue abierta
→ interface-craft
```

`engineering-workflow` gobierna la implementación cuando corresponda.

### Feature funcional nueva

```text
engineering-workflow
```

Y se suma `interface-craft`, `adaptive-layout` o `component-architecture` **solo si el problema
realmente los requiere**.

### Rediseño con dirección abierta

```text
visual-foundation
→ design-directions
→ dirección aprobada
→ interface-craft
→ adaptive-layout          si corresponde
→ visual-consistency
```

### Implementación desde mockup aprobado

```text
interface-craft
→ adaptive-layout          si hace falta
→ visual-consistency
```

No pasa por `design-directions`: la dirección ya está decidida.

### Auditoría UX

```text
ux-audit
→ hallazgo
→ skill de corrección correspondiente
```

| Hallazgo | Recibe |
|---|---|
| Corrección visual clara | `interface-craft` |
| Dirección estructural abierta | `design-directions` |
| Fallo entre tamaños | `adaptive-layout` |
| Patrón compartido | `component-architecture` |
| Cambio de comportamiento o datos | `engineering-workflow` |

### Limpieza de un proyecto maduro

No hay secuencia fija. Cada una resuelve un problema distinto y pueden coexistir:

```text
responsabilidades compartidas mal resueltas → component-architecture
clases Tailwind equivalentes e inconsistentes → tailwind-hygiene
elementos confirmados sin uso                → tech-cleanup
```

Correr las tres por costumbre sobre un repo que solo tiene uno de los tres problemas es
trabajo inventado.

---

## Handoffs

Un handoff es una **decisión**, no una obligación. Si la tarea termina correctamente en la
skill actual, ahí termina.

```text
design-directions      → una dirección queda aprobada
                       → interface-craft

ux-audit               → identifica un problema entre tamaños
                       → adaptive-layout

visual-consistency     → identifica un problema visual
                       → interface-craft

visual-consistency     → identifica divergencia repetida de un patrón
                       → component-architecture

component-architecture → deja una estructura correcta, con Tailwind
                         innecesariamente inconsistente
                       → tailwind-hygiene

interface-craft        → la dirección visual no estaba decidida
                       → design-directions

interface-craft        → falta la regla en el sistema
                       → visual-foundation

marcozen               → confirma elementos sin uso
                       → tech-cleanup

cualquiera             → el cambio requiere rama, validaciones y PR
                       → engineering-workflow
```

---

## Versionado

**Una modificación del repositorio no implica que todas las skills deban cambiar de versión.**
Cada skill se versiona según su propio contrato, con su `VERSION` y su tag independiente.

Cambiar el README, esta guía o la documentación compartida no cambia la versión de ninguna
skill. Solo se sube la versión de una skill cuando cambia **su** contrato: su método, sus
fronteras, sus salidas o sus reglas.

Detalle de archivos y tags en el [README](../README.md#versionado).
