# Sistema visual — <proyecto>

**Contrato visual operativo del proyecto.** Es la fuente de verdad mínima, semántica, aplicable y trazable que aplica cualquier agente o persona al construir interfaz aquí. Lo mantiene `visual-foundation`.

> **Principio rector:** Documentar el conjunto mínimo de reglas visuales suficiente para que las decisiones futuras sean consistentes. No convertir detalles locales de implementación en leyes globales.

> **Ninguna sección es obligatoria. Borra las que el proyecto no tenga decididas.** Una sección rellenada por completitud enseña reglas que nadie aprobó y debilita la autoridad del documento.

Cada regla lleva uno de estos tres estados:

- `Confirmado` — hay fuente aprobada, instrucción explícita o dirección formalmente aceptada. Se aplica sin preguntar.
- `Derivado` — no hay especificación formal, pero la evidencia del código es consistente en rol, contexto y función visual. Se aplica y se ajusta si aparece una fuente aprobada.
- `Pendiente de validar` — hay contradicción o evidencia insuficiente. **No se aplica.** La incertidumbre queda localizada y no bloquea decisiones independientes.

---

## 1. Contexto y fuentes

**Estado del documento:** Inicial | En uso | Desactualizado  
**Última actualización:** AAAA-MM-DD  

### Referencias aprobadas

| Referencia | Tipo | Dónde vive | Fecha |
|---|---|---|---|
| <Brand Master, mockup aprobado, dirección acordada> | <Marca / UI / Dirección> | <path, Figma, enlace> | <AAAA-MM-DD> |

### Fuentes usadas para este documento

| Fuente | Tipo de evidencia | Qué aportó |
|---|---|---|
| <archivo, doc o código inspeccionado> | <Aprobada / Evidencia de código / Render> | <roles, escala, tokens existentes> |

### Decisiones pendientes de validar

> La incertidumbre es local: un pendiente aquí no suspende las reglas confirmadas de otras áreas.

| # | Pregunta concreta respondible | Qué decisión bloquea | Estado |
|---|---|---|---|
| 1 | <pregunta clara, no "revisar spacing"> | <regla específica que no puede cerrarse> | Abierta |

---

## 2. Dirección visual e invariantes transferibles

<Dos o tres frases sobre el carácter o tesis que gobierna la interfaz, respaldadas por una referencia aprobada o por el handoff de `design-directions`. Borra esta sección si no hay referencia formal: no inventes adjetivos genéricos.>

- **Tesis rectora:** <ej. Evidencia y datos mandan sobre discurso comercial>
- **Invariantes aprobadas:** <ej. Jerarquía de acciones estricta; tratamiento sobrio de superficies; densidad operativa conservada>
- **Fuente de aprobación:** <ej. Dirección B aprobada en PR #XX / Brand Master>
- **Estado:** Confirmado — <fuente>

---

## 3. Tipografía

Roles semánticos antes que escala cruda de píxeles. Incluye solo los niveles con función confirmada o derivada.

> **Regla de jerarquía:** `PageTitle > SectionHeading > Body > Meta`. La jerarquía se sostiene por escala, peso, posición y contraste relativo.

| Rol semántico | Intención y uso | Mapeo técnico actual | Relación / Jerarquía | Estado |
|---|---|---|---|---|
| PageTitle | Título principal de la pantalla o vista | text-3xl / font-bold / leading-tight | Dominante en la página | |
| SectionHeading | Cabecera de bloque o tarjeta principal | text-xl / font-semibold | Claramente subordinado a PageTitle | |
| SubsectionHeading | Subtítulo interno o grupo de campos | text-base / font-semibold | Subordinado a SectionHeading | |
| Body | Texto de lectura, descripciones, contenido | text-sm / font-normal / leading-normal | Nivel base de legibilidad | |
| Meta / Caption | Metadatos, etiquetas auxiliares, marcas temporales | text-xs / text-muted / font-medium | Subordinado al Body | |

---

## 4. Spacing y relaciones de ritmo

Roles semánticos antes que catálogo exhaustivo de utilidades.

> **Relación fundamental:** `distancia interna de control < separación entre bloques relacionados < separación entre secciones`.

| Rol semántico | Uso funcional | Mapeo técnico / Valor | Relación | Estado |
|---|---|---|---|---|
| ControlGap | Espacio interno de botones, inputs, badges | gap-2 (8px) / px-3 py-1.5 | Unidad mínima de interacción | |
| ItemGap | Separación entre elementos de un mismo grupo | gap-3 (12px) | Proximidad perceptiva fuerte | |
| BlockGap | Separación entre grupos de datos o tarjetas | gap-6 (24px) | Delimita bloques temáticos | |
| SectionGap | Separación entre secciones principales de la vista | gap-12 (48px) | Separación estructural evidente | |

---

## 5. Layout, container y estructura

Principios estructurales globales. No define el layout particular de cada pantalla individual.

| Decisión | Valor / Regla | Intención | Estado |
|---|---|---|---|
| Container principal | max-w-7xl / mx-auto | Ancho máximo de contenido central | |
| Gutters globales | px-4 (mobile) / px-8 (desktop) | Margen de seguridad respecto al viewport | |
| Grid base | 12 columnas / gap-6 | Estructura para vistas de contenido | |
| Densidad general | <Cómoda / Estándar / Compacta> | Adecuada a la tarea (editorial vs operativa) | |

---

## 6. Color por función

Roles semánticos de interfaz, no muestrario de marca. Distingue colores de marca de los roles de UI.

| Rol semántico | Uso en interfaz | Mapeo técnico (Token / Hex) | ¿Color de marca? | Estado |
|---|---|---|---|---|
| background | Fondo general de la aplicación | bg-slate-50 / --bg-app | No | |
| surface | Superficie de tarjetas, paneles y modales | bg-white / --surface | No | |
| surface-subtle | Fondo alterno o filas cebradas | bg-slate-100 / --surface-subtle | No | |
| text | Texto principal de lectura y títulos | text-slate-900 / --text-main | No | |
| text-muted | Texto secundario, ayuda, metadata | text-slate-500 / --text-muted | No | |
| primary | Acción principal o estado seleccionado | bg-indigo-600 / --primary | Sí | |
| primary-contrast | Texto o icono sobre color primary | text-white | No | |
| border | Bordes estructurales y divisiones | border-slate-200 / --border | No | |
| focus-ring | Anillo de accesibilidad y foco | ring-indigo-500 / ring-2 | No | |

---

## 7. Superficies, radio y profundidad

Valores respaldados por función. No crees variantes adicionales (`sm/md/lg/xl`) si el proyecto solo usa dos.

| Rol | Uso | Mapeo técnico / Valor | Estado |
|---|---|---|---|
| Radius de control | Botones, inputs, badges | rounded-md (6px) | |
| Radius de contenedor | Tarjetas, modales, paneles | rounded-xl (12px) | |
| Elevación plana | Superficies sin superposición | shadow-none / border | |
| Elevación flotante | Menús desplegables, modales, tooltips | shadow-lg / border | |

---

## 8. Contratos de componentes recurrentes

Solo patrones recurrentes con contrato visual estable que otros agentes necesiten respetar. No es un inventario exhaustivo de componentes.

### PrimaryAction
- **Rol:** Acción más importante del contexto o vista actual.
- **Tratamiento:** Superficie primary con alto contraste; prominente y visualmente diferenciada de acciones secundarias.
- **Estado:** Confirmado / Derivado

### PageHeader
- **Rol:** Apertura de vistas operacionales o de contenido.
- **Tratamiento:** Título y acciones primarias/secundarias alineadas en el mismo eje; acciones secundarias subordinadas en peso; sin cards envolventes innecesarias.
- **Estado:** Confirmado / Derivado

---

## 9. Responsive global

Principios y reglas del sistema que se repiten. La adaptación de cada pantalla o tabla particular corresponde a `adaptive-layout`.

- **Breakpoints globales:** sm (640px), md (768px), lg (1024px), xl (1280px).
- **Gutters por viewport:** 16px en pantallas estrechas; 32px en escritorio.
- **Regla de prioridad general:** En anchos reducidos, el contenido primario y la acción principal conservan visibilidad; los paneles auxiliares colapsan bajo o tras acción de apertura.
- **Estado:** Confirmado / Derivado

---

## 10. Patrones aprobados

Soluciones que sirven de referencia por la decisión que demuestran, no por sus píxeles incidentales.

| Patrón / Pantalla de referencia | Decisión transferible que demuestra | Contexto de aplicación | Estado |
|---|---|---|---|
| <ej. PageHeader de /clientes> | Título y acciones comparten eje; secundarios subordinados; densidad operativa | Vistas principales de gestión | Confirmado |

---

## 11. Patrones a evitar (con evidencia)

Desviaciones que explícitamente no deben repetirse. Solo con evidencia documentada (instrucción, contradicción formal, deriva reiterada o decisión descartada).

| Práctica a evitar | Razón y evidencia | Qué hacer en su lugar |
|---|---|---|
| <ej. Cards anidadas para datos simples> | Rompe la jerarquía y satura con bordes redundantes; el patrón aprobado agrupa por espaciado | Agrupar por proximidad (gap-3) sobre la superficie base |

---

## 12. Excepciones acotadas autorizadas

Desviaciones funcionales justificadas que no constituyen una regla global.

| Ámbito delimitado | Regla que modifica | Razón funcional | Estado |
|---|---|---|---|
| <ej. Tablas operacionales densas> | Spacing vertical de fila (py-1.5 en vez de py-3.5) | Permitir comparación de 50+ filas sin scroll excesivo | Confirmado |

---

## 13. Mapeo técnico a tokens existentes

Cómo se expresan las decisiones en el código actual (Tailwind, variables CSS o tema). No inventes nuevos tokens sin sincronización técnica aprobada.

| Decisión semántica | Expresión técnica existente | Archivo / Ubicación |
|---|---|---|
| PageTitle | text-3xl font-bold tracking-tight | Clases de utilidad Tailwind |
| PrimaryAction | bg-primary text-primary-foreground | CSS variables / tailwind theme |
| ControlGap | gap-2 (0.5rem) | Tailwind default spacing |

---

## Historial de cambios

Trazabilidad de decisiones. La regla activa es única y vigente; las decisiones anteriores pasan aquí y no compiten como alternativas válidas.

| Fecha | Decisión actualizada | Valor anterior (superseded) | Regla nueva activa | Fuente que justifica el cambio |
|---|---|---|---|---|
| AAAA-MM-DD | Documento creado | N/A | Versión inicial | Inspección de fuentes iniciales |
