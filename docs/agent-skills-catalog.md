# AGENT-SKILLS — Catálogo y Routing

Este documento existe para que ChatGPT sepa **qué Agent Skills reales están disponibles** cuando
genera encargos de desarrollo para Claude, Codex o Antigravity.

Las skills ya están instaladas en los agentes ejecutores. Acá no se explica cómo ejecutarlas.
Solo se define cuáles existen, de qué responde cada una, y las fronteras entre ellas.

> **La sección de skills es generada.** Se construye desde el `description` del frontmatter de
> cada `SKILL.md`, que es el texto de routing autoritativo —el mismo que lee el agente ejecutor
> para decidir si activa la skill. No la edites a mano: corrige el `SKILL.md` y regenera.
>
> ```bash
> python3 scripts/build_skill_catalog.py
> ```
>
> `--check` falla si el catálogo quedó desincronizado. La prosa fuera de los marcadores es
> escrita a mano y el generador no la toca.

---

# 1. Regla dura

**No inventar Agent Skills.** Si un nombre no aparece en el catálogo cerrado de la sección 3,
no es una Agent Skill de este workflow.

---

# 2. Especialidad profesional ≠ Agent Skill

Un proyecto puede contener perfiles, dominios y tecnologías: Analytics, UX/UI, Full-stack,
Arquitectura, SEO, Growth, CRM inmobiliario, e-commerce, Supabase, Next.js, WordPress.

Sirven para **pensar correctamente el problema**. No son Agent Skills.

Nunca escribir `Skill: analytics`, `Skill: CRM inmobiliario`, `Craft: Supabase` ni
`Apoyo: frontend`, salvo que ese nombre esté en el catálogo cerrado.

---

<!-- BEGIN GENERATED: skills -->

# 3. Catálogo cerrado — 12 skills

Un nombre que no aparece en esta lista no es una Agent Skill de este workflow.

```text
adaptive-layout
component-architecture
design-directions
engineering-workflow
interface-craft
marcozen
project-blueprint
tailwind-hygiene
tech-cleanup
ux-audit
visual-consistency
visual-foundation
```

## `adaptive-layout` · v0.2.0

Adapta una interfaz ya resuelta entre mobile, tablet y desktop conservando intención, prioridad y capacidades. Úsala cuando algo se rompe, se corta o se degrada en un tamaño concreto; cuando la versión mobile es visiblemente el desktop encogido; cuando una tabla, un sidebar, una toolbar, un formulario de varias columnas o un dashboard no caben en pantallas estrechas; cuando hay overflow horizontal, breakpoints acumulados como parches, o acciones que se escondieron con `display:none` para que algo cupiera; y cuando el punto intermedio de tablet quedó sin resolver. Dispara con "hazlo responsive", "en mobile se ve mal", "esta tabla no cabe en el teléfono", "el sidebar se come la pantalla", "se rompe en tablet", "hay scroll horizontal en toda la página". No la uses para el diseño base de una pantalla que tampoco funciona en su viewport de origen, para revisar sin implementar, para consolidar componentes repetidos ni para normalizar clases de Tailwind.

## `component-architecture` · v0.2.0

Detecta cuándo una decisión visual o funcional ya resuelta debe existir una sola vez y ejecuta esa consolidación sin rediseñar. Úsala cuando el mismo patrón está implementado de varias formas distintas; cuando corregir un detalle obliga a tocar seis archivos; cuando una pantalla reimplementó localmente un componente que el producto ya tiene; cuando un componente compartido acumuló flags de páginas concretas (`isDashboard`, `showExtraBorder`); cuando hay dialogs, tablas o formularios hechos a mano sobre un proyecto que ya usa primitives; y cuando una pantalla se volvió ilegible por microcomponentes que solo reenvían props. Dispara con "esto está copiado en tres pantallas", "hagamos un componente común", "cada card se ve distinta", "ya tenemos un EmptyState", "este Card tiene diez booleanos". No la uses para decidir cómo debería verse un patrón que aún no está resuelto, para eliminar código sin uso no relacionado ni para normalizar clases de Tailwind.

## `design-directions` · v0.2.0

Explora caminos visuales realmente distintos antes de comprometerse con uno y construirlo. Úsala cuando la dirección visual todavía no está decidida y existen alternativas materialmente diferentes; cuando la primera idea razonable se convirtió en "la dirección" sin haber considerado otras; cuando alguien pide "opciones" y el riesgo es entregar tres versiones del mismo layout con distinto color; y cuando hay que elegir entre resolver una pantalla de forma editorial, producto-first, guiada por evidencia, orientada a comparar o centrada en la tarea. Sirve para sitios comerciales, e-commerce, dashboards, CRM, intranets y sistemas operacionales. Dispara con "exploremos opciones", "dame direcciones para este hero", "no sabemos si debería sentirse editorial o de producto", "muéstrame caminos distintos". Puede trabajar dentro de un sistema visual o de referencias aprobadas mientras siga habiendo una decisión estructural abierta. No la uses cuando ya existe un mockup o una referencia aprobada que fija suficientemente la dirección de esa pantalla, cuando la tarea es implementar la dirección elegida, cuando el problema es de detalle y no de dirección, ni para inventar una marca que no existe.

## `engineering-workflow` · v2.2.0

Ejecuta cambios de desarrollo de forma controlada y trazable en repositorios Git. Úsala obligatoriamente cuando el usuario la nombre, el repositorio la exija o la tarea implemente comportamiento, requiera Pull Request o merge, afecte varios archivos, datos, permisos, autenticación, pagos, documentos formales, dependencias, infraestructura o flujos operacionales. También cuando el cambio amplía la superficie alcanzable del producto —una tabla, un endpoint, una ruta pública, un bucket o un webhook nuevo— o depende de configuración aplicada en la consola de un servicio externo, que no aparece en el diff. Permite una ruta rápida para cambios LOW. Déjala a criterio de la IA para documentación, copy o ajustes locales triviales y reversibles. No la uses por defecto para consultas conceptuales, explicaciones, comandos aislados ni investigación o diagnóstico sin modificaciones.

## `interface-craft` · v0.2.0

Diseña, rediseña e implementa una interfaz concreta —pantalla, sección, flujo o bloque— con criterio visual y dentro del alcance funcional solicitado. Úsala para construir una pantalla o sección nueva; para rehacer una que se ve genérica, plana o desordenada; para traducir un mockup o una referencia aprobada a interfaz real; para resolver jerarquía, composición, densidad, tipografía, spacing, color, estados o visualización de datos de una vista concreta; y para decidir entre construir a mano o usar una librería de gráficos, motion, tablas o primitives accesibles. Sirve tanto para sitios comerciales y e-commerce como para dashboards, intranets, CRM, sistemas internos, herramientas operacionales y paneles de administración. Dispara con "rediseña este hero", "esta pantalla se ve genérica", "todos los KPI pesan igual", "no sé dónde mirar", "agrega un gráfico de evolución", "mejora esta vista del CRM", "implementa esta sección". No la uses para explorar direcciones visuales todavía no decididas, para revisar sin construir, para adaptar responsive una interfaz existente, para consolidar componentes repetidos ni para normalizar clases de Tailwind.

## `marcozen` · v2.2.0

MarcoZen de Proyectos audita, poda y gobierna repositorios web, e-commerce y apps bajo un modelo evidence-first y proporcional. Evalúa salud general, seguridad, preparación para producción, dependencias, ramas, documentación y SEO/AEO basándose en evidencia real y no en checklists dogmáticos ni puntajes artificiales. En sus modos de seguridad y pre-producción audita también la superficie alcanzable del producto en los tres lugares donde vive: el repositorio, la consola del proveedor —registro de cuentas, políticas de acceso efectivas, almacenamiento, entornos y claves emitidas— y el despliegue respondiendo, mediante sondas de solo lectura de cabeceras, métodos, redirecciones, mensajes de autenticación, páginas de error y DNS, todo contra el modelo de acceso declarado. Úsala al auditar o recibir un repositorio, antes de salir a producción o integrar pagos/auth, en mantenimientos periódicos o para evaluar deuda técnica sin modificar archivos salvo autorización expresa.

## `project-blueprint` · v2.1.0

Diseña el blueprint técnico, funcional y de decisiones de un proyecto digital antes de implementar, o resuelve decisiones arquitectónicas específicas. Opera en modo Greenfield, Retrofit o Decision Patch. Clasifica el proyecto, recomienda el stack mínimo suficiente, resuelve arquitectura, datos, seguridad, operación y entrega bajo el principio de que la completitud de decisiones manda sobre la cantidad de documentos. Cuando el producto tiene usuarios, declara el modelo de acceso y registro como decisión explícita y auditable. No construye el producto ni inventa requisitos.

## `tailwind-hygiene` · v0.2.0

Normaliza y limpia el uso de Tailwind preservando exactamente el resultado visual y funcional. Úsala cuando la misma decisión está escrita de varias formas (`p-[24px]`, `p-6`, `px-[24px] py-[24px]`); cuando conviven utilidades redundantes o contradictorias (`rounded-md rounded-lg`, `hidden flex`, `px-4 px-6`) y ya no está claro qué regla produce el resultado; cuando un `className` acumuló concatenaciones ilegibles; y cuando el theme, las CSS variables y el uso real divergieron. Dispara con "normaliza estas clases", "saca los arbitrary values", "estas clases se contradicen", "este className es ilegible". No la uses para cambiar cómo se ve algo, para arreglar responsive roto, para consolidar componentes repetidos, para crear tokens nuevos, para migrar Tailwind de versión ni para eliminar código sin uso: si el render cambia, dejó de ser higiene.

## `tech-cleanup` · v2.0.0

Tech Cleanup detecta código, archivos, dependencias y assets sin uso, y produce un plan de eliminación segura clasificado por riesgo. Úsala SIEMPRE que el usuario quiera limpiar deuda técnica en un sitio, app o repositorio ya en producción o a punto de estarlo: código muerto, componentes sin uso, rutas obsoletas, imágenes/assets duplicados o sin referencias, dependencias innecesarias, scripts sin uso, tests obsoletos, configuraciones duplicadas, variables de entorno abandonadas o documentación desactualizada. Dispara con frases como "limpia el proyecto", "hay código muerto", "elimina lo que no se usa", "reduce el bundle", "poda el repo de basura técnica", "auditoría de código sin uso", "encuentra archivos huérfanos", "dependencias que no se usan" o cuando el sitio lleva tiempo en producción y ha ido acumulando desorden. No la uses para auditar orden general, ramas o gobernanza (usa marcozen) ni para definir arquitectura de un proyecto nuevo (usa project-blueprint).

## `ux-audit` · v0.2.0

Auditoría profunda de experiencia sobre una interfaz real —pantalla, flujo, herramienta o producto completo— centrada en si la persona puede entender, decidir y completar su tarea. Úsala cuando el usuario pida auditar la UX, la usabilidad o un flujo; cuando algo "funciona" pero la gente se pierde, duda, comete errores o abandona; cuando un formulario, un checkout, un onboarding o un panel operacional produce fricción; cuando hay que saber dónde se pierde tiempo en una herramienta de uso diario; y antes de publicar o mostrar un flujo a un cliente. Dispara con "audita la UX", "los clientes se pierden en el checkout", "dónde estamos haciendo perder tiempo", "este formulario da problemas", "revisa este flujo completo". Es de solo lectura: diagnostica y deriva, no implementa. No la uses para revisar consistencia visual —spacing, radius, color, fidelidad al sistema— cuando eso no cambia la capacidad de completar la tarea, ni para diseñar, adaptar entre tamaños o auditar el repositorio.

## `visual-consistency` · v0.2.0

Revisa una interfaz ya renderizada y detecta las desviaciones visuales respecto de lo que este producto decidió ser. Es la revisión visual cotidiana: rápida, perceptual y de solo lectura. Úsala para mirar una pantalla y decir qué está mal; para comparar lo construido contra un mockup, una captura aprobada o `docs/ui-system.md`; para comparar varias pantallas entre sí y encontrar la que se salió del sistema; y para revisar jerarquía, composición, escala tipográfica, pesos, gaps, padding, márgenes, alineación, anchos, color, radius, bordes, sombras y densidad. Dispara con "algo se ve raro acá", "revisa esta pantalla", "esto quedó inconsistente", "compáralo con la referencia", "revisa tipografías y espacios", "¿esto está listo para mostrárselo al cliente?", "estas pantallas no parecen del mismo sistema". No la uses para construir o corregir la interfaz, para auditar en profundidad la experiencia de un usuario en una tarea, para explorar direcciones visuales no decididas ni para escribir las reglas del proyecto.

## `visual-foundation` · v0.2.0

Establece y mantiene la fuente de verdad visual operativa de un proyecto en `docs/ui-system.md`, traduciendo marca, referencias aprobadas y evidencia del código a reglas que otros agentes puedan aplicar. Úsala cuando exista marca, mockup o referencia aprobada que nadie tradujo a reglas; cuando el proyecto creció y aparecieron tamaños tipográficos arbitrarios, gaps inconsistentes, paddings sin sistema, colores casi equivalentes, containers divergentes o radius y sombras sin criterio; cuando otra tarea visual necesita un sistema que no existe; o cuando hay que actualizar el sistema visual tras una nueva referencia aprobada. Dispara con "define el sistema visual", "no hay consistencia de espaciados", "cada pantalla usa un tamaño distinto", "documenta los tokens", "actualiza el ui-system". No la uses para diseñar o rediseñar una pantalla concreta, para auditar la interfaz renderizada, ni para inventar una marca que no existe.

<!-- END GENERATED: skills -->

---

# 4. Cómo se nombran en un encargo

```text
Skill:   [una del catálogo]
Apoyo:   [una del catálogo]   · solo si hay una segunda responsabilidad real
Craft:   [capa de criterio]   · solo si el resultado visual importa
```

Lo habitual es **una skill**. El apoyo se agrega cuando aparece una responsabilidad distinta,
no porque pertenezca a la misma familia. Cero skills es válido para una tarea trivial que se
resuelve con una respuesta puntual.

No existe pipeline obligatorio. No activar una skill porque podría servir, porque normalmente
viene después, o porque quizás encuentre algo.

## La capa de craft

Las doce skills son **contrato de proceso**: cuándo activar, alcance, frontera, riesgo,
profundidad de validación, entrega. Son las dueñas del flujo.

Los agentes ejecutores suelen tener además skills externas de **criterio y oficio** —gusto
visual, guidelines, patrones de componentes. `impeccable` es la habitual. No compiten con el
catálogo: están a otra altura.

```text
interface-craft   decide el alcance, la frontera y la entrega
impeccable        aporta el criterio visual dentro de la construcción
```

El slot `Craft:` existe para declararlo. Sin esa línea, las dos reclaman el flujo y gana la
que tenga la descripción más ancha.

**Dos límites:**

- **No nombrar una skill visual sin brief visual real.** Qué pantalla, qué debe comunicar, qué
  jerarquía. `"Mantener coherencia con el sistema visual existente"` no es un brief: es la
  forma de obtener un resultado genérico. Sin brief, no hay `Apoyo:` visual ni `Craft:`.
- **Las skills externas que producen planes de trabajo** —`improve` y equivalentes— no se
  invocan dentro de un encargo que ya tiene `Skill:` asignada. Son de fase previa, cuando
  todavía no hay encargo. Dentro de uno, compiten con el flujo completo.

Las bibliotecas puras de componentes (`shadcn` y similares) no entran en este cálculo.

---

# 5. Fronteras que más se confunden

```text
¿hay que decidir el camino visual?               → design-directions
¿el camino ya está decidido?                     → interface-craft

¿la interfaz base necesita diseño o rediseño?    → interface-craft
¿funciona en origen y falla al cambiar espacio?  → adaptive-layout

¿corresponde visualmente al producto?            → visual-consistency
¿la persona puede completar la tarea?            → ux-audit

¿la responsabilidad está duplicada?              → component-architecture
¿está correcta pero escrita inconsistentemente?  → tailwind-hygiene

¿salud transversal del repositorio?              → marcozen
¿demostrar y retirar desuso?                     → tech-cleanup

¿decisiones de arquitectura, stack o datos?      → project-blueprint
¿ejecutar un cambio de software?                 → engineering-workflow
```

Una feature de métricas no crea una skill `analytics`:

```text
Problema:        métricas comerciales en un CRM inmobiliario
Para pensarlo:   Analytics + CRM + UX operacional
Skill:           engineering-workflow
Apoyo:           interface-craft, si hay responsabilidad visual real y brief
```

Si el problema ya está demostrado, no uses una auditoría para descubrirlo otra vez. La acción
desaparece en mobile y el fallo está verificado → `adaptive-layout`, no
`ux-audit` → `adaptive-layout`.

---

# 6. Si el routing sigue ambiguo

Consultar el repositorio canónico `bfernandois059/dev-workflow-skills`, en este orden:

1. `docs/skill-selection-guide.md` — fronteras finas, handoffs, composición.
2. `skills/<skill-candidata>/SKILL.md` — solo de las candidatas reales.

No cargar las doce para decidir. No buscar una skill nueva para que coincida con el nombre de
la tarea.

---

# 7. Control antes de devolver un routing

```text
¿Skill y Apoyo pertenecen al catálogo cerrado?
¿Hay como máximo un apoyo?
¿Confundí una profesión, un dominio o una tecnología con una Agent Skill?
¿La skill nombrada posee realmente la decisión dominante?
¿Nombré una skill visual sin brief visual?
```

---

> **Las especialidades ayudan a entender el problema.
> Las Agent Skills definen con qué método trabaja el ejecutor.**
