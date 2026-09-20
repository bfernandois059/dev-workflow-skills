# Sistema visual — <proyecto>

**Contrato visual operativo del proyecto.** Es la fuente de verdad mínima, semántica, aplicable y trazable que aplica cualquier agente o persona al construir interfaz aquí. Lo mantiene `visual-foundation`.

> **Principio rector:** Documentar el conjunto mínimo de reglas visuales suficiente para que las decisiones futuras sean consistentes. No convertir detalles locales de implementación en leyes globales.

> **Estructura, no preset visual:** Esta plantilla define la estructura documental y el tipo de evidencia a registrar. No contiene valores visuales por defecto, temas ni decisiones predeterminadas. No copies clases, colores, breakpoints, spacing o radios como si fueran reglas del proyecto si no están respaldados por evidencia real.

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

- **Tesis rectora:** <tesis funcional o de producto respaldada por referencia>
- **Invariantes aprobadas:** <invariantes transferibles confirmadas en referencia o dirección>
- **Fuente de aprobación:** <referencia formal, PR o acuerdo>
- **Estado:** <Confirmado / Derivado>

---

## 3. Tipografía

Roles semánticos antes que escala cruda de píxeles. Incluye solo los niveles con función confirmada o derivada en el proyecto.

> **Principio de jerarquía:** Roles como PageTitle, SectionHeading, Body o Meta expresan niveles claros de lectura. La jerarquía se sostiene por escala, peso, posición y contraste relativo según la evidencia del proyecto.

| Rol semántico | Intención y uso | Mapeo técnico existente | Relación / Jerarquía | Estado |
|---|---|---|---|---|
| <rol (ej. PageTitle)> | <intención funcional y contexto de uso> | <expresión en código o tokens existentes> | <nivel dominante en la pantalla> | <Confirmado / Derivado> |
| <rol (ej. SectionHeading)> | <cabecera de sección, módulo o bloque> | <expresión en código o tokens existentes> | <subordinado al título principal> | <Confirmado / Derivado> |
| <rol (ej. Body)> | <texto base de lectura, descripciones> | <expresión en código o tokens existentes> | <nivel base de legibilidad> | <Confirmado / Derivado> |
| <rol (ej. Meta / Caption)> | <metadatos, etiquetas auxiliares, marcas> | <expresión en código o tokens existentes> | <subordinado al cuerpo de texto> | <Confirmado / Derivado> |

---

## 4. Spacing y relaciones de ritmo

Roles semánticos y relaciones de distancia antes que catálogo de utilidades o números fijos.

> **Relación fundamental:** `distancia dentro de grupo < separación entre bloques relacionados < separación entre secciones`.

| Rol semántico | Uso funcional | Mapeo técnico existente | Relación | Estado |
|---|---|---|---|---|
| <espaciado interno de control> | <botones, inputs, badges respaldados> | <evidencia o tokens del proyecto> | <distancia mínima de interacción> | <Confirmado / Derivado> |
| <separación entre elementos> | <elementos de un mismo grupo o lista> | <evidencia o tokens del proyecto> | <proximidad perceptiva fuerte> | <Confirmado / Derivado> |
| <separación entre bloques> | <grupos de datos o módulos relacionados> | <evidencia o tokens del proyecto> | <delimita bloques temáticos> | <Confirmado / Derivado> |
| <separación entre secciones> | <secciones estructurales de la vista> | <evidencia o tokens del proyecto> | <separación estructural evidente> | <Confirmado / Derivado> |

---

## 5. Layout, container y estructura

Principios estructurales globales respaldados por fuentes. No define el layout particular de cada pantalla individual.

| Decisión | Regla / Mapeo respaldado | Intención funcional | Estado |
|---|---|---|---|
| Container principal | <ancho máximo o container respaldado en fuentes> | <intención y centrado según evidencia> | <Confirmado / Derivado> |
| Gutters globales | <margen lateral respecto al viewport según fuentes> | <margen de seguridad y respiración lateral> | <Confirmado / Derivado> |
| Grid global | <solo si existe una regla de columnas global documentada> | <alineación estructural del proyecto> | <Confirmado / Derivado> |
| Densidad general | <principio de densidad derivado de la tarea o fuentes> | <adecuación al contexto de uso del producto> | <Confirmado / Derivado> |

---

## 6. Color por función

Roles semánticos de interfaz respaldados por el proyecto. Distingue colores de marca de los roles de UI y no asumas que primary es color de marca.

| Rol semántico | Uso en interfaz | Mapeo técnico (Token / Hex / Clase) | ¿Color de marca? | Estado |
|---|---|---|---|---|
| background | <fondo general según evidencia del proyecto> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |
| surface | <superficie de contenedores, paneles, modales> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |
| text | <texto principal de lectura y títulos> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |
| text-muted | <texto secundario, metadatos, ayuda> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |
| primary | <acción principal o estado interactivo destacado> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |
| border | <bordes estructurales y divisiones> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |
| <rol adicional (ej. focus, feedback)> | <uso funcional específico justificado> | <mapeo respaldado en fuentes> | <Sí / No> | <Confirmado / Derivado> |

---

## 7. Superficies, radio y profundidad

Valores respaldados por función real en el proyecto. No inventes escalas artificiales si el proyecto usa un solo radio o ninguno, ni introduzcas sombras no respaldadas.

| Rol funcional | Uso en interfaz | Mapeo respaldado (Radio / Sombra / Borde) | Estado |
|---|---|---|---|
| <radio / superficie de control> | <botones, inputs, chips según evidencia> | <valor o token respaldado> | <Confirmado / Derivado> |
| <radio / superficie de contenedor> | <tarjetas, paneles, modales según evidencia> | <valor o token respaldado> | <Confirmado / Derivado> |
| <delimitación plana> | <superficies delimitadas por borde o contraste> | <mapeo respaldado (ej. border, sin sombra)> | <Confirmado / Derivado> |
| <elevación flotante> | <solo si existen overlays, modales o menús con elevación> | <mapeo respaldado si existe> | <Confirmado / Derivado> |

---

## 8. Contratos de componentes recurrentes

Solo patrones recurrentes con contrato visual estable que otros agentes necesiten respetar. No es un inventario exhaustivo de componentes ni prescribe diseños prefabricados.

### <Nombre del patrón recurrente (ej. PrimaryAction o PageHeader)>
- **Rol:** <función visual e interactiva recurrente>
- **Contexto:** <dónde y cuándo aplica en el producto>
- **Invariantes visuales:** <decisiones visuales estables respaldadas por evidencia o fuentes>
- **Variantes autorizadas:** <solo las variantes justificadas formalmente>
- **Estado:** <Confirmado / Derivado>
- **Fuente:** <referencia, pantalla o archivo de origen>

---

## 9. Responsive global

Principios y reglas del sistema que se repiten. La adaptación de cada pantalla, flujo o tabla particular corresponde a `adaptive-layout`.

- **Breakpoints globales:** <solo si el proyecto tiene breakpoints formales establecidos en config o tema>
- **Gutters por viewport:** <regla de márgenes laterales existente según evidencia>
- **Principios repetibles:** <solo reglas estructurales confirmadas o derivadas que se repitan en el producto>
- **Estado:** <Confirmado / Derivado>

---

## 10. Patrones aprobados

Soluciones que sirven de referencia por la decisión que demuestran, no por sus píxeles incidentales.

| Patrón o pantalla de referencia | Decisión transferible que demuestra | Contexto de aplicación | Estado |
|---|---|---|---|
| <referencia de pantalla o patrón aprobado> | <decisión visual transferible que sirve de guía> | <contexto de uso donde debe replicarse> | <Confirmado> |

---

## 11. Patrones a evitar (con evidencia)

Desviaciones que explícitamente no deben repetirse. Solo con evidencia documentada (instrucción explícita, contradicción formal, deriva reiterada observada o decisión descartada).

| Práctica a evitar | Razón y evidencia | Qué hacer en su lugar |
|---|---|---|
| <desviación o anti-patrón documentado> | <evidencia concreta: instrucción explícita, deriva observada o decisión descartada> | <alternativa conforme a las reglas activas del sistema> |

---

## 12. Excepciones acotadas autorizadas

Desviaciones funcionales justificadas que no constituyen una regla global.

| Ámbito delimitado | Regla que modifica | Razón funcional | Estado |
|---|---|---|---|
| <ámbito acotado (ej. vista de tabla densa)> | <regla de spacing o superficie afectada> | <necesidad funcional justificada (ej. comparación de alta densidad)> | <Confirmado / Derivado> |

---

## 13. Mapeo técnico a tokens existentes

Cómo se expresan las decisiones en el código actual (Tailwind, variables CSS o tema). No inventes nuevos tokens sin sincronización técnica aprobada.

| Decisión semántica | Expresión técnica existente | Archivo / Ubicación |
|---|---|---|
| <rol semántico confirmado o derivado> | <token, variable CSS o clase existente en el proyecto> | <archivo de configuración, CSS o componente> |
| <rol semántico confirmado o derivado> | <token, variable CSS o clase existente en el proyecto> | <archivo de configuración, CSS o componente> |

---

## Historial de cambios

Trazabilidad de decisiones. La regla activa es única y vigente; las decisiones anteriores pasan aquí y no compiten como alternativas válidas.

| Fecha | Decisión actualizada | Valor anterior (superseded) | Regla nueva activa | Fuente que justifica el cambio |
|---|---|---|---|---|
| <AAAA-MM-DD> | <decisión actualizada> | <valor o regla anterior> | <regla nueva activa> | <fuente aprobada o justificación> |
