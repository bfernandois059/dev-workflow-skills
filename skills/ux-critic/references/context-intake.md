# Context Intake

Fase 0 de `ux-critic`. Define contra qué se va a juzgar la interfaz. Sin esto, la crítica se
vuelve un checklist genérico — que es exactamente el fallo que esta skill existe para evitar.

## Regla base: inferir primero, preguntar después

Preguntar siete cosas que estaban a la vista es tan malo como no preguntar nada: quema la
paciencia del usuario y hace que responda rápido y mal.

Antes de preguntar, extrae lo que ya está disponible:

| Fuente | Qué te dice |
|---|---|
| `README`, blueprint, docs del repo | Propósito, alcance, etapa, restricciones |
| Contenido de la propia página | A quién le habla, qué vende, qué tono usa, qué tarea propone |
| Rutas y navegación | Cuántos flujos hay y cuál es el central |
| Presencia de auth, carrito, panel | Si el usuario es visitante, cliente o interno |
| Idioma, moneda, formatos | Mercado y expectativas culturales |
| Lo que el usuario ya dijo en el chat | Casi siempre la mitad del contexto |

Después presenta lo inferido y pide confirmación en una sola pasada. Confirmar es más barato
que responder.

## Las siete entradas obligatorias

### 1. Propósito
Qué es y qué tiene que lograr esa pantalla o ese sitio. Un objetivo, no tres.
**Cambia**: qué se considera éxito y qué elementos merecen dominar la composición.

### 2. Usuario real
No una persona ficticia con nombre y edad. Los ejes que sí cambian el veredicto:

| Eje | Extremos | Qué implica para la crítica |
|---|---|---|
| Familiaridad | Primera vez ↔ lo usa a diario | Primera vez: la pantalla debe explicar. Diario: la pantalla debe ser rápida y densa, y explicar molesta |
| Prisa | Explorando ↔ resolviendo algo urgente | Con prisa, todo texto no esencial es un obstáculo |
| Dispositivo | Móvil dominante ↔ escritorio | Cambia jerarquía, tamaños de toque y cuánto cabe antes del scroll |
| Costo del error | Reversible ↔ irreversible (pago, envío, borrado) | Define cuánta confirmación y cuánta reversibilidad son obligatorias |
| Motivación | Tiene que hacerlo ↔ puede irse | Si puede irse, la fricción se paga con abandono |
| Confianza previa | Marca conocida ↔ desconocida | Sin confianza previa, las señales de credibilidad son funcionales, no decorativas |
| Capacidad técnica | Experta ↔ nula | Define la jerga admisible y cuánto se puede dar por sabido |

### 3. Tarea principal y criterio de éxito
"El usuario llega desde Instagram y tiene que agendar una hora." El criterio de éxito se
escribe como un hecho observable, no como una sensación.
**Cambia**: qué se audita primero y qué se considera un desvío.

### 4. Etapa
- **Pre-producción**: nada es definitivo. El replanteo estructural está sobre la mesa y la
  sección "Lo que replantearía de cero" es obligatoria.
- **Producción**: hay costo de cambio y usuarios acostumbrados. Los replanteos siguen siendo
  válidos, pero se acompañan del costo y de una alternativa incremental.

### 5. Nivel de exigencia
Niveles 1 / 2 / 3 definidos en `SKILL.md`. Pregunta directa cuando no esté claro:
*"¿Esto tiene que funcionar bien, verse profesional, o competir con lo mejor de su
categoría?"*

### 6. Restricciones reales
Marca y paleta cerradas, stack, componentes de terceros, plazos, decisiones comerciales
tomadas, lo que explícitamente no se toca. Una restricción declarada no vuelve correcta a la
interfaz: mueve el hallazgo a "restricción asumida" y se reporta igual, con su costo.

### 7. Alcance
`Sitio completo` · `Flujo` · `Pantalla` · `Bloque`. Si es un bloque, hay que verlo **en su
contexto**: un bloque impecable puede ser un error dentro de la página que lo contiene.

## Formato de la pregunta

Un solo bloque, máximo seis preguntas, cada una con una opción por defecto para que se pueda
responder con una palabra.

```
Antes de criticar necesito seis cosas. Te propongo lo que deduje; corrígeme donde falle.

1. Objetivo de la pantalla: [inferido] — ¿correcto?
2. Quién llega: [inferido]. ¿Primera vez o recurrente? ¿Móvil o escritorio?
3. La tarea que tiene que completar: [inferida]. ¿Es esa?
4. Etapa: ¿pre-producción (puedo proponer replanteos) o ya está en producción?
5. Exigencia: ¿que funcione, que se vea profesional, o nivel de referencia?
6. Qué NO se puede tocar: ¿marca, componentes, plazos?
```

## Cuando el usuario no sabe responder

- **"No sé quién lo usa."** Eso ya es un hallazgo de producto — dilo. Propón el perfil más
  probable a partir del contenido, márcalo `Supuesto por confirmar` y avanza. Un supuesto
  explícito es auditable; un supuesto silencioso contamina todo el informe.
- **"Lo usan todos."** Fuerza la elección: *"¿a quién prefieres perder si tengo que elegir?"*
  Una interfaz optimizada para todos no está optimizada.
- **"Quiero que se vea bonito / moderno / premium."** No es un criterio, es una sensación.
  Tradúcelo: pide dos o tres referencias concretas y usa **esas** como vara. "Como X pero sin
  la sensación de Y" es un criterio utilizable.
- **"Hazme la auditoría completa igual."** Puedes: entrega la parte objetiva y medible
  (contraste, tamaños de toque, escala tipográfica, estados faltantes, semántica) y declara
  al inicio que las capas 1–4 quedan sin juicio hasta tener contexto.

## Preguntas que no hay que hacer

- Demografía que no cambia ninguna decisión de diseño (edad, género, ciudad) — a menos que sí
  la cambie y puedas decir cómo.
- "¿Qué emociones quieres transmitir?" sin traducirlas después a decisiones concretas.
- Preguntas cuya respuesta está en la página que tienes abierta.
- Más de seis preguntas. Si necesitas más, es que no inferiste lo suficiente.
