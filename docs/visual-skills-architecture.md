# Arquitectura del sistema visual de skills

Documento canónico de la familia de skills visuales de este repositorio. Define qué resuelve
cada una, dónde termina su responsabilidad y qué reglas comparten. Se escribió antes de que
existiera ninguna implementación y sigue siendo el contrato que cada pieza debe respetar.

Este documento es un contrato operativo, no un manifiesto de diseño. Se escribe para que un
agente —Claude Code, Codex u otro compatible— pueda decidir qué skill corresponde a una tarea
sin adivinar, y para que la implementación posterior de cada pieza no invada a las demás.

> **Estado:** `visual-foundation`, `interface-craft` y `visual-consistency` ya están
> implementadas e instalables (`skills/visual-foundation/`, `skills/interface-craft/`,
> `skills/visual-consistency/`). Las otras cuatro siguen sin existir: este documento define su
> contrato y los siguientes PR implementarán cada pieza.

## Titularidad

Los nombres, la metodología y la arquitectura descritos aquí son propios de este repositorio.
No son un envoltorio de servicios, productos ni skills de terceros, no dependen de ninguna
plataforma externa para funcionar y no replican un sistema ajeno.

Lo que sí usan es el estándar abierto [Agent Skills](https://code.claude.com/docs/en/skills)
como formato de empaquetado, igual que las cinco skills actuales. Una skill visual podrá
**recomendar** una librería de terceros cuando sea la solución correcta —eso es la regla 5 del
contrato común— pero el criterio, las fases y los cortes son de este repositorio.

## Por qué siete y no una

Una sola skill de "diseño" termina siendo monolítica: hace una crítica tímida, un rediseño
parcial y una limpieza a medias, y no hace bien ninguna de las tres. La familia se separa por
**tipo de decisión**, no por tecnología:

| Tipo de decisión | Skill |
|---|---|
| Qué reglas visuales rigen el proyecto | `visual-foundation` |
| Qué camino visual tomar cuando hay más de uno | `design-directions` |
| Cómo se resuelve esta interfaz concreta | `interface-craft` |
| Si lo construido corresponde a lo decidido | `visual-consistency` |
| Cómo sobrevive esa decisión en otros tamaños | `adaptive-layout` |
| Cuándo una decisión repetida se vuelve estructura | `component-architecture` |
| Cómo se expresa todo eso en Tailwind sin ruido | `tailwind-hygiene` |

Cada una es de responsabilidad única y combinable. Ninguna necesita a las otras para dar un
resultado útil, pero encadenadas cubren el ciclo completo de una interfaz.

## Mapa del sistema

```
Producto / arquitectura
        ↓
project-blueprint          define producto, stack, datos y documentos
        ↓
engineering-workflow       controla rama, validaciones, PR e integración
        ↓
┌──────────────────────────────────────────────────────────────┐
│ Sistema visual especializado                                 │
│                                                              │
│   visual-foundation ──────────────→ design-directions        │
│   (reglas: ui-system.md)            (explorar alternativas)   │
│            │                                 │               │
│            └────────────┬────────────────────┘               │
│                         ↓                                    │
│                  interface-craft                             │
│                  (diseñar / rediseñar / implementar)         │
│                         ↓                                    │
│                  adaptive-layout                             │
│                  (mobile · tablet · desktop)                 │
│                         ↓                                    │
│                  visual-consistency                          │
│                  (revisar lo renderizado vs. referencias)    │
│                         ↓                                    │
│                  component-architecture                      │
│                  (lo repetido se vuelve componente)          │
│                         ↓                                    │
│                  tailwind-hygiene                            │
│                  (normalizar sin rediseñar)                  │
└──────────────────────────────────────────────────────────────┘

Auditorías especializadas (transversales, fuera de la cadena):
ux-critic · marcozen · tech-cleanup
```

El orden es la secuencia típica, no una obligación. Una tarea puede entrar directamente por
`interface-craft` o por `tailwind-hygiene` sin pasar por las anteriores. Lo que el mapa fija es
la **dirección de la dependencia**: `visual-foundation` no depende de las demás, y
`tailwind-hygiene` no decide nada que las anteriores no hayan decidido ya.

---

## Las siete skills

### `visual-foundation` — implementada

**Estado.** Disponible en [`skills/visual-foundation/`](../skills/visual-foundation/SKILL.md).

**Propósito.** Establecer y mantener el lenguaje visual del proyecto como reglas operativas, y
ser dueña de `docs/ui-system.md`.

**Cuándo usarla.** Al inicio de un proyecto con referencias aprobadas; cuando existe marca o
mockup pero nadie los tradujo a reglas; cuando el proyecto creció y el sistema visual real ya no
coincide con el declarado; cuando otra skill visual necesita una fuente de verdad que no existe.

**Cuándo no usarla.** Para diseñar una pantalla concreta (`interface-craft`). Para juzgar si una
pantalla cumple el sistema (`visual-consistency`). Para inventar una marca desde cero: si no hay
ninguna decisión visual aprobada, eso es una conversación de producto, no una skill.

**Entrada principal.** Brand Master, mockups, capturas aprobadas, referencias, y el código
existente como evidencia del estado real.

**Salida esperada.** `docs/ui-system.md` creado o actualizado, con las decisiones separadas en
`Confirmado` / `Derivado` / `Pendiente de validar`.

**Qué puede modificar.** `docs/ui-system.md` y los tokens o configuración que ese contrato
declara (variables CSS, `tailwind.config`, tema). Nada más.

**Qué no debe absorber.** El diseño de páginas completas como responsabilidad principal, la
crítica de interfaz, y la definición de arquitectura de información —eso es `project-blueprint`.

---

### `design-directions`

**Propósito.** Explorar alternativas visuales realmente distintas antes de comprometerse con una.

**Cuándo usarla.** Cuando la dirección visual no está decidida; cuando la primera solución
propuesta es la única que se consideró; cuando el cliente pide "opciones" y el riesgo es entregar
tres versiones del mismo layout.

**Cuándo no usarla.** Cuando ya existe una referencia aprobada o un `ui-system.md` que fija la
dirección. Cuando la tarea es implementar, no elegir. Cuando el problema es de detalle y no de
dirección.

**Entrada principal.** El problema de interfaz, el contexto de producto y usuario, y las
referencias disponibles.

**Salida esperada.** Alternativas comparables con su razonamiento, y una recomendación explícita
con lo que se gana y se pierde en cada una.

**Qué puede modificar.** Preferentemente nada del producto: trabaja en exploraciones aisladas. Si
necesita código para mostrar la alternativa, va en archivos de exploración, no en la ruta
productiva.

**Qué no debe absorber.** La implementación definitiva por defecto. Elegir dirección y construirla
en producción son dos decisiones distintas y la segunda pasa por `interface-craft`.

> **Regla dura.** Las alternativas deben divergir en estructura, composición, jerarquía o
> interacción. Tres paletas sobre el mismo layout no son tres direcciones: son una sola con
> variaciones cosméticas, y presentarlas como opciones es simular una decisión que no se tomó.

---

### `interface-craft` — implementada

**Estado.** Disponible en [`skills/interface-craft/`](../skills/interface-craft/SKILL.md).

**Propósito.** Diseñar o rediseñar una interfaz concreta con criterio visual, e implementarla
cuando la tarea lo requiera.

**Cuándo usarla.** Para construir una pantalla, sección o flujo nuevo; para rehacer uno que no
funciona visualmente; cuando hay una referencia aprobada que traducir a interfaz real.

**Cuándo no usarla.** Para revisar sin construir (`visual-consistency` o `ux-critic`). Para
explorar direcciones aún no decididas (`design-directions`). Para normalizar clases sin cambiar
el resultado (`tailwind-hygiene`).

**Entrada principal.** El alcance solicitado, `ui-system.md` si existe, las referencias aprobadas
y la interfaz actual renderizada cuando ya hay algo.

**Salida esperada.** La interfaz diseñada e implementada dentro del alcance, con las decisiones
visuales relevantes explicadas.

**Qué puede modificar.** El código de la interfaz dentro del alcance solicitado: composición,
layout, escala, densidad y estructura visual. Puede replantear —no solo ajustar— cuando la
estructura actual es el problema.

**Qué no debe absorber.** El alcance funcional. Rediseñar una pantalla no autoriza a cambiar
qué hace. Tampoco absorbe la creación de componentes compartidos como objetivo propio: si al
resolver detecta repetición estructural, lo señala y lo deriva a `component-architecture`.

---

### `visual-consistency` — implementada

**Estado.** Disponible en [`skills/visual-consistency/`](../skills/visual-consistency/SKILL.md).

**Propósito.** Revisar una interfaz **renderizada** contra las referencias aprobadas y el sistema
visual, y reportar lo que no corresponde.

**Cuándo usarla.** Después de implementar; antes de mostrar algo a un cliente; cuando "se ve raro"
y no está claro dónde; para comparar pantallas entre sí y detectar deriva.

**Cuándo no usarla.** Como auditoría UX completa —eso es `ux-critic`, que evalúa propósito,
tarea, copy y estados con contexto obligatorio. Para corregir: reporta, no implementa. Para
juzgar sin haber renderizado nada.

**Entrada principal.** La interfaz renderizada (local, URL o captura), más `ui-system.md` y las
referencias aprobadas.

**Salida esperada.** Lista de desviaciones concretas con su ubicación y su corrección propuesta.

**Qué puede modificar.** Nada. Es de revisión.

**Qué no debe absorber.** La profundidad de `ux-critic`. Revisa **macro antes que micro**:

1. jerarquía
2. composición
3. tipografía
4. spacing
5. alineación y layout
6. color
7. densidad
8. forma y profundidad
9. consistencia entre patrones
10. detalle

El orden no obliga a recorrer las diez capas en cada revisión: obliga a no reportar la última
como si fuera la primera. Un `gap` de unos píxeles no encabeza el informe cuando el defecto real
es que dos bloques compiten por el protagonismo.

> **Regla dura.** Es una revisión cotidiana, rápida y repetible. Si empieza a evaluar propósito
> de producto, adecuación al usuario o calidad del copy, dejó de ser `visual-consistency` y está
> duplicando `ux-critic` peor de lo que `ux-critic` ya lo hace.

---

### `adaptive-layout`

**Propósito.** Adaptar una interfaz entre mobile, tablet y desktop conservando intención y
prioridad.

**Cuándo usarla.** Cuando una interfaz existe en un tamaño y hay que resolverla en los otros;
cuando algo se rompe o se degrada en un breakpoint; cuando el diseño mobile es visiblemente el
desktop encogido.

**Cuándo no usarla.** Para el diseño base de la interfaz (`interface-craft`). Para verificar que
el responsive cumple el sistema (`visual-consistency`). Para arreglar clases desordenadas sin
cambiar comportamiento (`tailwind-hygiene`).

**Entrada principal.** La interfaz renderizada en los viewports relevantes y la intención
declarada de la pantalla.

**Salida esperada.** El comportamiento adaptativo resuelto e implementado, con la prioridad de
contenido explícita por tamaño.

**Qué puede modificar.** Layout, orden, densidad, visibilidad y comportamiento por breakpoint.

**Qué no debe absorber.** El rediseño visual de fondo. Si la pantalla está mal en desktop, no se
arregla desde el responsive.

> **Regla dura.** Responsive no es reducir desktop. Lo primero en una pantalla chica puede no ser
> lo primero en una grande, y decidir eso es parte del trabajo, no una consecuencia automática del
> breakpoint.

---

### `component-architecture`

**Propósito.** Identificar cuándo una decisión visual o funcional repetida debe convertirse en un
componente o patrón compartido, y ejecutar esa consolidación.

**Cuándo usarla.** Cuando el mismo patrón aparece resuelto de tres formas distintas; cuando
corregir algo obliga a tocar seis archivos; cuando una revisión detectó que el problema no está en
las páginas sino en lo que comparten.

**Cuándo no usarla.** Para diseñar el patrón por primera vez (`interface-craft`). Para eliminar
componentes sin uso (`tech-cleanup`). Para consolidar cuando todavía no hay repetición real.

**Entrada principal.** El código de la interfaz y la evidencia de repetición.

**Salida esperada.** Componentes o patrones compartidos creados o consolidados, con los puntos de
uso migrados y el resultado visual preservado.

**Qué puede modificar.** La estructura de componentes y sus consumidores dentro del alcance.

**Qué no debe absorber.** La decisión visual en sí. Consolida lo que ya se decidió; no aprovecha
la consolidación para rediseñar.

> **Regla dura.** No se componentiza por número de líneas. Un componente existe porque tiene una
> responsabilidad real y un contrato claro, no porque un bloque se repita dos veces. Crear
> microcomponentes sin responsabilidad propia empeora la mantenibilidad que se quería mejorar.

---

### `tailwind-hygiene`

**Propósito.** Normalizar y limpiar el uso de Tailwind preservando exactamente el resultado
visual.

**Cuándo usarla.** Cuando hay valores arbitrarios que ya existen como token; cuando el orden de
clases es ilegible; cuando conviven utilidades contradictorias; cuando el `tailwind.config` y el
uso real divergieron.

**Cuándo no usarla.** Para cambiar cómo se ve algo. Para arreglar responsive roto
(`adaptive-layout`). Para eliminar clases de componentes sin uso (`tech-cleanup`).

**Entrada principal.** El código con Tailwind y el `ui-system.md` o la configuración vigente.

**Salida esperada.** Clases normalizadas, con el antes/después visual verificado.

**Qué puede modificar.** Clases de utilidad, `tailwind.config` y tokens, siempre que el resultado
renderizado no cambie.

**Qué no debe absorber.** El rediseño, la creación de componentes y la eliminación de código sin
uso.

> **Regla dura.** Si el resultado visual cambió, la tarea dejó de ser higiene. O se revierte, o se
> reclasifica como `interface-craft` y se justifica el cambio.

---

## `docs/ui-system.md` — la fuente de verdad visual del proyecto

`ui-system.md` es el contrato visual **operativo** que podrá existir dentro de cada proyecto que
use estas skills. Vive en el repositorio del proyecto, no en este repositorio.

Este documento lo define conceptualmente. Su dueña es `visual-foundation`, que mantiene la
plantilla en `skills/visual-foundation/assets/templates/ui-system.template.md`.

### Qué podrá contener

Según lo que el proyecto realmente tenga decidido:

- dirección visual
- referencias aprobadas
- tipografía
- escala de spacing
- layout y containers
- colores y semántica
- radius, bordes y sombras
- patrones de componentes
- motion
- comportamiento responsive
- patrones aprobados
- patrones a evitar

Ninguna sección es obligatoria. Un proyecto pequeño puede tener cuatro; uno maduro, las doce. Un
`ui-system.md` con secciones vacías rellenadas por completitud es peor que uno corto.

### Qué no es

- **No reemplaza el Brand Master.** La marca —identidad, logo, uso, voz— es un documento anterior
  y de otra naturaleza. `ui-system.md` la consume, no la sustituye.
- **No inventa branding.** Si no hay decisión de marca, `ui-system.md` no la genera: registra lo
  que falta como `Pendiente de validar`.
- **Traduce decisiones aprobadas a reglas operativas.** Su valor es que un agente pueda mantener
  la coherencia sin interpretar un PDF de marca en cada tarea.
- **No es un inventario del código.** Documentar lo que hay no es lo mismo que declarar lo que
  debe ser.

### El código es evidencia, no fuente de verdad

Esta distinción es el motivo por el que el documento existe:

> El código existente es **evidencia** del estado actual. No es fuente de verdad cuando contradice
> una referencia aprobada o el sistema visual declarado.

Que algo esté implementado de cierta forma prueba que se implementó así, no que sea correcto. Ante
contradicción entre código y referencia aprobada, manda la referencia, y la diferencia se reporta
como desviación —no se adopta el código como norma retroactiva.

---

## Contrato común de las skills visuales

Estas nueve reglas aplican a las siete. Se documentan aquí una vez y **no se repiten dentro de
cada `SKILL.md`**.

**1. Respetar el sistema no significa preservar errores.**
Una inconsistencia existente no se conserva únicamente porque ya esté implementada. "Así estaba"
no es justificación.

**2. La cantidad mínima de código no es un objetivo.**
La meta es la solución más simple, sólida y mantenible que produzca el resultado requerido. Menos
líneas a costa de fragilidad no es simplicidad.

**3. Una dependencia adecuada puede ser la solución mínima correcta.**
No construir manualmente gráficos complejos con SVG, tablas avanzadas desde cero, animaciones
complejas solo con CSS ni primitives accesibles artesanales únicamente para evitar una
dependencia. Reimplementar mal algo resuelto no es austeridad.

**4. Primero reutilizar lo adecuado que ya existe.**
Si el proyecto ya usa una librería competente para gráficos, motion, tablas, primitives o
componentes, se prefiere esa antes que introducir otra.

**5. Si no existe herramienta adecuada, una dependencia estándar y mantenida es válida.**
Válida cuando simplifica realmente la solución. No se agregan dependencias innecesarias ni
exóticas, y la justificación sigue siendo la de `engineering-workflow`: necesidad, mantenimiento,
seguridad y alternativa descartada.

**6. Diseño visual y alcance funcional son dimensiones distintas.**
Mantener un alcance acotado no obliga a producir una solución visual tímida. Se puede resolver algo
pequeño con ambición visual.

**7. La referencia aprobada tiene prioridad visual.**
Cuando existe Brand Master, mockup, captura aprobada o `ui-system.md`, la implementación se evalúa
contra esas referencias y no solamente contra el código existente.

**8. No convertir todas las interfaces en el mismo patrón.**
Evitar resolver sistemáticamente con cards, grids idénticos, hero estándar, gradientes, o
icono + título + descripción. Una fórmula repetida sin relación con el problema es ausencia de
decisión, no consistencia.

**9. El criterio debe ser perceptual y funcional.**
Build, lint o typecheck nunca sustituyen una revisión visual cuando la tarea afecta lo que ve el
usuario. Que compile no es evidencia de que se vea bien.

---

## Fronteras con las skills actuales

Las cinco skills existentes siguen funcionando sin cambios. Estas fronteras se resuelven
**documentalmente**: ninguna skill actual se modifica en este PR.

| Skill actual | Responsabilidad | Frontera con la familia visual |
|---|---|---|
| `project-blueprint` | Producto y arquitectura general | Define qué se construye y con qué stack. La familia visual no define arquitectura de información ni documentos de producto. |
| `engineering-workflow` | Rama, validaciones, PR, integración | Controla **cómo** se integra cualquier cambio, incluidos los visuales. Ninguna skill visual gestiona ramas, PR ni merge. |
| `ux-critic` | Auditoría UX profunda de interfaz renderizada | Sin cambios por ahora. Ver contradicción 1. |
| `marcozen` | Auditoría y gobernanza del repositorio | Orden general, seguridad, SEO, mantenimiento. No juzga calidad visual de una pantalla. |
| `tech-cleanup` | Eliminación segura de código y assets sin uso | Borra lo que no se usa. `tailwind-hygiene` normaliza lo que sí se usa; `component-architecture` consolida lo repetido. Tres operaciones distintas. |

### Contradicciones detectadas y su resolución

Las siguientes son solapamientos **reales** encontrados en las skills actuales, no hipotéticos.

**1. `ux-critic` ya cubre sistema visual y responsive.**
Su Capa 6 (`skills/ux-critic/SKILL.md`, Capa 6) evalúa color, tipografía y espaciado; su Transversal B
(`skills/ux-critic/references/judgment-layers.md`, Transversal B) evalúa responsive real. Eso solapa con `visual-consistency`
y con `adaptive-layout`.

*Resolución documental:* se separan por **profundidad y costo**, no por tema.

- `ux-critic` es una auditoría profunda con contexto de producto y usuario obligatorio y
  bloqueante, siete capas en orden fijo, inventario medido sobre la página viva, pasada de
  refutación y niveles de exigencia. Es cara y se usa en momentos concretos.
- `visual-consistency` es una revisión cotidiana contra referencias y `ui-system.md`. No exige
  contexto de producto, no evalúa propósito ni copy, y está pensada para correrse seguido.
- `adaptive-layout` **implementa** la adaptación; `ux-critic` solo la juzga y no toca código.

`ux-critic` no se renombra, no se recorta y no se modifica en este PR. Más adelante se evaluará
separar su auditoría UX profunda de la revisión visual cotidiana; esa evaluación es un PR propio y
no está autorizada aquí.

**2. `docs/04-ux-content-and-design-system.md` ya existe como documento de producto.**
Lo define `project-blueprint` (`skills/project-blueprint/SKILL.md`) como "arquitectura de información, flujos,
contenido y componentes" y lo lista `engineering-workflow` en su matriz de impacto documental
(`skills/engineering-workflow/SKILL.md`). Introducir `ui-system.md` sin frontera crea dos fuentes de verdad.

*Resolución documental:*

| Documento | Dueño | Naturaleza | Cadencia |
|---|---|---|---|
| `docs/04-ux-content-and-design-system.md` | `project-blueprint` | Decisión de producto: arquitectura de información, flujos, contenido, inventario de componentes | Se define al inicio y cambia poco |
| `docs/ui-system.md` | `visual-foundation` | Contrato visual operativo: tokens, escalas, patrones y reglas que un agente aplica en cada tarea | Se mantiene continuamente |

El primero responde *qué pantallas y qué contenido existen*. El segundo, *con qué reglas visuales
se construyen*. Si un proyecto solo tiene uno de los dos, no se fuerza el otro.

**3. `ux-critic` ya rastrea hallazgos al componente compartido.**
Su modo sitio y su plantilla de plan de corrección (`skills/ux-critic/assets/templates/fix-plan.template.md`)
trabajan con alcance "Componente compartido". Eso roza `component-architecture`.

*Resolución documental:* `ux-critic` **identifica** que el problema vive en un componente
compartido y lo entrega como tarea. `component-architecture` **decide y ejecuta** la
consolidación estructural. Diagnóstico y cirugía, no la misma skill.

**4. `project-blueprint` ya pregunta por marca y referencias.**
Su cuestionario de descubrimiento (`skills/project-blueprint/references/discovery-questionnaire.md`) pregunta si existe
marca, sistema visual, Figma o referencias aprobadas.

*Resolución documental:* no hay conflicto, hay encadenamiento. `project-blueprint` **detecta** qué
material visual existe; `visual-foundation` lo **traduce** a `ui-system.md`. La pregunta se queda
donde está.

---

## Convenciones de autoría de nuevas skills

Toda skill de esta familia se escribe con esta separación:

```text
SKILL.md
→ comportamiento esencial que siempre necesita la skill.

references/
→ conocimiento especializado que solo se consulta cuando corresponde.

scripts/
→ operaciones deterministas que una máquina realiza mejor que el modelo.

evals/
→ validar decisiones y comportamiento, no comprobar que el modelo recite un procedimiento.
```

Reglas de autoría:

- **Responsabilidad única y combinables.** Si una skill necesita "y además" para explicarse,
  probablemente son dos.
- **No repetir lo que ya pertenece a `engineering-workflow`.** Queda fuera de todo `SKILL.md`
  visual: política de ramas, flujo de PR, clasificación general de riesgo, auditorías de
  seguridad y Definition of Done global.
- **No repetir el contrato común.** Las nueve reglas de este documento se citan, no se copian.
- **`SKILL.md` deliberadamente compacto.** No hay límite artificial de líneas, pero si una regla
  no es necesaria en prácticamente todos los usos de la skill, se evalúa moverla a `references/`.
- **Versión SemVer propia**, igual que las cinco actuales.

El costo de una regla que vive en `SKILL.md` se paga en cada invocación. El de una que vive en
`references/` se paga solo cuando hace falta. Esa es la razón de la separación, y es la misma para
la descripción del frontmatter: se lee siempre, aunque la skill no se use.

---

## Estado de implementación

Implementado:

- `visual-foundation` — dueña de `docs/ui-system.md`, con su plantilla y sus evals.
- `interface-craft` — diseño, rediseño e implementación de una interfaz concreta, con sus
  criterios por área en `references/craft-criteria.md` y sus evals.
- `visual-consistency` — revisión visual cotidiana de solo lectura sobre la interfaz renderizada,
  con sus criterios por área en `references/visual-review-criteria.md` y sus evals.

Todavía no existe:

- `design-directions`, `adaptive-layout`, `component-architecture` y `tailwind-hygiene`
- `ux-audit` ni ninguna separación de `ux-critic`
- librerías, scripts o infraestructura compartida entre skills visuales

Las cinco skills previas siguen sin modificarse: cada pieza visual se incorpora sin alterar el
comportamiento de las existentes. La siguiente será `adaptive-layout`.
