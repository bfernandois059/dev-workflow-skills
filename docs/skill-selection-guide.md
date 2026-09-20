# Guía de selección de skills

Fuente principal para decidir **qué skill usar para el problema actual**, cuándo no usarla,
cómo se combinan y quién toma el relevo después. El repositorio opera en tres niveles documentales:
* **`README.md`**: orienta rápidamente y ofrece un mapa general de entrada.
* **Esta guía (`docs/skill-selection-guide.md`)**: resuelve dudas de selección, fronteras finas, handoffs y composición detallada.
* **`SKILL.md` (en cada carpeta de skill)**: documenta y ejecuta el método operativo concreto.

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
| Definir arquitectura, stack y decisiones clave (Greenfield, Retrofit o Decision Patch) | `project-blueprint` | El proyecto ya tiene las decisiones que el cambio necesita, o la tarea es una implementación acotada directa |
| Implementar una tarea de desarrollo con alcance, rama, validación y PR | `engineering-workflow` | Es una consulta conceptual, un diagnóstico sin modificaciones o un ajuste local trivial y reversible |
| Definir o mantener la verdad visual del proyecto | `visual-foundation` | El problema es una pantalla concreta y las reglas ya existen: eso es `interface-craft` |
| Explorar caminos visuales antes de elegir uno | `design-directions` | La dirección ya está decidida —mockup aprobado, patrón fijado— o solo cambiaría color, radius o sombras |
| Diseñar, rediseñar o implementar una interfaz concreta | `interface-craft` | La interfaz ya está resuelta y solo falla por espacio o dispositivo: eso es `adaptive-layout` |
| Revisar si lo renderizado pertenece visualmente al producto | `visual-consistency` | El problema es que la persona no puede entender o completar la tarea: eso es `ux-audit` |
| Resolver cómo una interfaz se adapta entre tamaños | `adaptive-layout` | El mismo problema existe también en el viewport de origen: primero `interface-craft` |
| Consolidar responsabilidades y patrones compartidos en componentes | `component-architecture` | Todavía no está decidido cómo debe verse el patrón, o el problema es solo cómo están escritas las clases |
| Normalizar Tailwind sin cambiar la interfaz | `tailwind-hygiene` | El cambio alteraría el render, el responsive o un estado — deja de ser higiene |
| Auditar si una persona puede entender y completar una tarea | `ux-audit` | Solo hay deriva visual sin costo sobre la tarea, o lo que se busca es salud técnica del repo |
| Auditar salud general del repositorio: seguridad, SEO técnico y deuda amplia | `marcozen` | Lo que se audita es la experiencia de una persona (`ux-audit`), o el objetivo exclusivo es investigar y podar desuso específico de código/assets (`tech-cleanup`) |
| Eliminar código, dependencias, assets y archivos realmente sin uso | `tech-cleanup` | El objetivo es evaluar la salud transversal, seguridad o gobernanza global del repositorio: eso es `marcozen` |

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
salud transversal, seguridad, gobernanza y readiness → marcozen
demostrar y retirar elementos realmente sin uso     → tech-cleanup
```

`tech-cleanup` no exige una auditoría previa de `marcozen` para operar: incluye su propia
investigación de evidencia de desuso y puede activarse directamente ante sospecha de código muerto,
acumulación técnica o una solicitud directa de limpieza. La diferencia radica en el objeto de
análisis: `marcozen` evalúa salud transversal, gobernanza, seguridad, readiness y deuda amplia del
repositorio; `tech-cleanup` investiga específicamente si componentes, dependencias o assets concretos
carecen de uso real y ejecuta su eliminación segura en lotes proporcionales y reversibles.

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

Son ejemplos de composición en situaciones reales, **no pipelines obligatorios**. Cada flecha representa una decisión contextual que el equipo toma, no un paso automático e inevitable. Si una tarea queda resuelta en la primera skill, el trabajo concluye ahí.

### 1. Proyecto nuevo

```text
project-blueprint
→ visual-foundation          si existe trabajo visual
→ design-directions          solo si la dirección sigue abierta
→ interface-craft
→ adaptive-layout            cuando haya adaptación entre tamaños
→ visual-consistency         antes de entrega visual
```

* **Cuándo usar esta ruta**: Al construir un producto o sitio web desde cero.
* **Gobierno técnico**: `engineering-workflow` no es una etapa visual posterior; gobierna la disciplina técnica transversal (ramas, commits, PRs y validaciones de código) cada vez que se ejecuten cambios en el repositorio.
* **Excepciones**: Si el proyecto parte con un mockup aprobado o diseño cerrado, se salta `design-directions` directamente a `interface-craft`. Si es un servicio puramente backend o CLI sin interfaz, solo aplican `project-blueprint` y `engineering-workflow`.

### 2. Sitio existente que necesita rediseño

```text
ux-audit                     si primero hay que entender fricción de la tarea
+
visual-consistency           si existe deriva visual
↓
visual-foundation            si las reglas no están claras o están desactualizadas
↓
design-directions            solo si la dirección está abierta
↓
interface-craft
↓
adaptive-layout              si corresponde
```

* **Diagnóstico previo no conjunto**: `ux-audit` y `visual-consistency` **no son una obligación conjunta**. Si el dolor reportado es funcional (usuarios que dudan, abandonan o cometen errores en un flujo), se dispara `ux-audit`. Si el problema es estético (pantallas rotas, gaps dispares, estilos desalineados), se dispara `visual-consistency`. Si existen ambos, cada una entrega su diagnóstico de solo lectura antes de tocar código.
* **Reglas**: Antes de rehacer pantallas, `visual-foundation` consolida o actualiza `docs/ui-system.md` para evitar repetir el caos previo.

### 3. CRM / intranet / sistema interno

```text
ux-audit
→ interface-craft
→ adaptive-layout
→ component-architecture     si aparecen responsabilidades realmente compartidas
```

* **Prioridades en herramientas operacionales**: En sistemas internos la densidad de información no es un defecto si reduce clics, scroll y tiempo de trabajo al operador.
* **Foco**: Reducir fricción operativa, proteger contra errores destructivos y acelerar la carga de datos.
* **Cuándo consolidar**: `component-architecture` interviene **solo si** un patrón ya resuelto (ej. tabla con filtros avanzados, selector modal) aparece en múltiples vistas y debe evolucionar de forma idéntica. Si el patrón solo vive en una vista, no se componentiza preventivamente.

### 4. Feature nueva dentro de un producto existente

```text
project-blueprint            Decision Patch, solo si aparecen decisiones nuevas
→ engineering-workflow
→ interface-craft            si tiene UI
→ adaptive-layout            si corresponde
```

* **Alcance proporcional**: No exige regenerar el blueprint completo; el modo **Decision Patch** de `project-blueprint` resuelve únicamente los deltas de arquitectura, datos o permisos necesarios.
* **Flujo puramente técnico**: Para una funcionalidad de backend, lógica o refactor sin interfaz, `engineering-workflow` opera por sí sola de principio a fin, sin invocar skills visuales.

### 5. Implementar un mockup ya aprobado

```text
interface-craft
→ adaptive-layout            si falta resolver tamaños
→ visual-consistency
```

* **Dirección ya fijada**: `design-directions` **no corresponde** porque la decisión estructural y visual ya fue resuelta y aprobada previamente. Fabricar opciones en este escenario es desperdicio de recursos.
* **Verificación**: `visual-consistency` interviene al final únicamente para comprobar que lo renderizado en el navegador respeta fielmente las decisiones aprobadas.

### 6. Proyecto heredado / repo desordenado

Se aborda como una **ramificación según el hallazgo**, no como una secuencia lineal fija:

```text
marcozen
   ↓ según hallazgo
   ├─ tech-cleanup            (código, assets o dependencias sin uso)
   ├─ component-architecture  (patrones duplicados que deberían unificarse)
   ├─ tailwind-hygiene        (clases redundantes o inconsistentes)
   └─ engineering-workflow    (refactors o saneamiento técnico)
```

* **`marcozen` no es un prerrequisito obligatorio**: `tech-cleanup` cuenta con su propia metodología de evidencia de desuso. Si ya se sabe de antemano que el repositorio acumula código muerto o dependencias huérfanas, `tech-cleanup` puede ejecutarse directamente sin pasar por `marcozen`.
* **Criterio**: Activar las skills según el problema real detectado en vez de correr todas por rutina.

### 7. Antes de entregar o publicar (Pre-entrega)

No es un checklist obligatorio ni una cadena secuencial (`todo proyecto → visual-consistency → ux-audit → marcozen`). Cada auditoría responde a una pregunta distinta y se activa según el riesgo o la necesidad del hito:

```text
visual-consistency     → calidad y coherencia visual del render frente al sistema
ux-audit               → tareas y recorridos críticos del usuario
marcozen               → readiness técnico, seguridad, SEO/AEO y gobernanza
```

* Si la entrega es un ajuste o rediseño visual: `visual-consistency`.
* Si se lanza un flujo de checkout o registro sensible: `ux-audit`.
* Si el proyecto sale por primera vez a producción: `marcozen` (modo pre-producción).

### Relevo tras una auditoría UX

Cuando `ux-audit` detecta fricción, entrega hallazgos y deriva a la skill adecuada:

| Hallazgo | Recibe |
|---|---|
| Corrección visual clara | `interface-craft` |
| Dirección estructural abierta | `design-directions` |
| Fallo entre tamaños | `adaptive-layout` |
| Patrón compartido | `component-architecture` |
| Cambio de comportamiento o datos | `engineering-workflow` |

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

**Las versiones son independientes por skill.** Un número mayor no significa que una skill sea “mejor” o más madura que otra: refleja la evolución histórica de su propio contrato.

* **Historiales SemVer independientes**: las skills pioneras del repositorio (`project-blueprint`, `engineering-workflow`, `marcozen`, `tech-cleanup`) atravesaron evoluciones de contrato mayores y se encuentran en `v2.0.0`. Por su parte, la familia visual completa y `ux-audit` nacieron de forma más reciente y se encuentran actualmente en `v0.2.0`.
* **Evolución real sin sincronización forzada**: la serie `0.x` indica que su especificación de contrato todavía se considera en evolución activa. Cuando una skill `0.x` consolide su interfaz y reglas de forma definitiva pasará a `1.0.0`. No se sincronizan versiones artificialmente.
* **Documentación compartida**: modificar el README, esta guía o cualquier documento transversal del repositorio **no cambia la versión de ninguna skill**. Solo se incrementa la versión de una skill cuando cambia **su** propio contrato operativo (fases, reglas, fronteras o formato de salida).

Detalle de versiones actuales, archivos y tags en el [README](../README.md#versionado).
