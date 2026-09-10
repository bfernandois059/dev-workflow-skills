# Sistema visual — <proyecto>

**Contrato visual operativo del proyecto.** Es la fuente de verdad que aplica cualquier agente o
persona al construir interfaz aquí. Lo mantiene `visual-foundation`.

> **Ninguna sección es obligatoria. Borra las que el proyecto no tiene decididas.** Una sección
> rellenada por completitud enseña reglas que nadie aprobó, y es peor que no tenerla.

Cada regla lleva estado:

- `Confirmado` — hay fuente aprobada o instrucción explícita. Se aplica sin preguntar.
- `Derivado` — no hay especificación, pero la evidencia del producto es consistente. Se aplica, y
  se corrige si aparece una fuente aprobada.
- `Pendiente de validar` — hay contradicción o evidencia insuficiente. **No se aplica.**

---

## 1. Contexto y fuentes

**Estado del documento:** Inicial | En uso | Desactualizado
**Última actualización:** AAAA-MM-DD

### Referencias aprobadas

| Referencia | Tipo | Dónde vive | Fecha |
|---|---|---|---|
| <Brand Master, mockup, captura, design system> | | | |

### Fuentes usadas para este documento

| Fuente | Qué aportó |
|---|---|

### Decisiones pendientes

| # | Pregunta | Bloquea | Estado |
|---|---|---|---|
| 1 | <pregunta respondible, no "revisar spacing"> | <qué no se puede aplicar hasta responderla> | Abierta |

---

## 2. Dirección visual

<Dos o tres frases sobre el carácter que debe mantener la interfaz, respaldadas por una
referencia. Si no hay referencia que lo respalde, borra esta sección: no inventes adjetivos
genéricos.>

**Estado:** <Confirmado / Derivado / Pendiente de validar> — <fuente>

---

## 3. Tipografía

Roles, no páginas. No hace falta tener todos los niveles.

| Rol | Family | Size | Line-height | Weight | Tracking | Responsive | Estado |
|---|---|---|---|---|---|---|---|
| Display | | | | | | | |
| H1 | | | | | | | |
| H2 | | | | | | | |
| H3 | | | | | | | |
| Body | | | | | | | |
| Small | | | | | | | |
| Label / caption | | | | | | | |

**Excepciones autorizadas:** <dónde y por qué. Si no hay, borra la línea.>

---

## 4. Spacing

**Escala operativa:** <valores> — Estado: <>

Usos semánticos, cuando puedan establecerse:

| Uso | Valor | Estado |
|---|---|---|
| Separación entre secciones | | |
| Separación entre bloques | | |
| Gaps internos | | |
| Padding de superficies y componentes | | |
| Spacing de controles | | |

> Objetivo de esta sección: que una pantalla nueva no invente un valor arbitrario.

---

## 5. Layout

| Decisión | Valor | Estado |
|---|---|---|
| Container principal | | |
| Anchos máximos | | |
| Gutters | | |
| Grid y columnas | | |
| Densidad | | |
| Alineaciones estructurales | | |

---

## 6. Color

Por función, no como catálogo. Incluye solo los roles que el proyecto realmente tiene.

| Rol | Valor | ¿Color de marca? | Estado |
|---|---|---|---|
| background | | | |
| surface | | | |
| text | | | |
| muted | | | |
| primary | | | |
| accent | | | |
| border | | | |
| success | | | |
| warning | | | |
| error | | | |

**Distinción marca / interfaz:** <qué colores vienen de la marca y cuáles son roles de UI
derivados. Un color de marca no siempre es un rol de interfaz.>

---

## 7. Forma y profundidad

Solo lo que existe. Si el proyecto necesita dos radios, no declares cinco.

| Decisión | Valores | Uso | Estado |
|---|---|---|---|
| Radius | | | |
| Border | | | |
| Shadow | | | |
| Elevation | | | |

---

## 8. Componentes y patrones

Patrones visuales aprobados que deben mantenerse consistentes. **No documentes cada componente
del repositorio por completitud** — solo aquellos cuya inconsistencia se nota.

### <Botones>

- **Variantes y cuándo usar cada una:**
- **Reglas visuales:** <altura, padding, tipografía, radius, estados>
- **Estado:**

<Repite el bloque solo para los patrones que lo necesiten: inputs, cards, tablas, navegación,
diálogos, badges, bloques de contenido.>

---

## 9. Motion

Borra esta sección si el proyecto no tiene motion decidido. **No inventes animaciones para
llenarla.**

| Decisión | Valor | Estado |
|---|---|---|
| Propósito | | |
| Duración | | |
| Easing | | |
| Comportamiento | | |
| Herramienta / librería | | |

---

## 10. Responsive

Principios visuales ya decididos. No sustituye el trabajo de adaptación de cada pantalla.

- **Prioridad:** <qué manda cuando no cabe todo>
- **Comportamiento general:**
- **Breakpoints relevantes:** <solo si están establecidos>
- **Cambios estructurales conocidos:**

**Estado:** <>

---

## 11. Patrones aprobados

Soluciones que sirven de referencia interna.

| Patrón | Dónde vive | Por qué funciona | Estado |
|---|---|---|---|

---

## 12. Patrones a evitar

Desviaciones y fórmulas que explícitamente no deben repetirse.

| Qué evitar | Por qué | Qué hacer en su lugar |
|---|---|---|

---

## 13. Mapeo técnico

Cómo se expresa cada regla en el código. Útil para encontrar dónde se cambia algo — **no es
documentación exhaustiva del código**.

| Decisión visual | Token / variable / theme / componente |
|---|---|
| <H1> | <`--text-h1` · `text-4xl` · `<Heading level={1}>`> |

---

## Historial

| Fecha | Qué cambió | Fuente que lo justifica |
|---|---|---|
| AAAA-MM-DD | Documento creado | |
