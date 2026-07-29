# Engine Routing

Cómo elegir con qué modelo conviene resolver una tarea, y cuándo delegarla a otro.

Este archivo es la fuente única de la política de motor para todas las skills del
repositorio. `marcozen` y `tech-cleanup` referencian los perfiles definidos aquí; los
nombres concretos de modelos solo viven en este archivo para que envejezca un archivo y no
cuatro skills.

## Principio

La métrica no es el costo por token, es el **costo por tarea resuelta, incluyendo las
iteraciones**. Un modelo menor que necesita cuatro intentos, tres correcciones y una
reconstrucción de contexto sale más caro —en tokens, tiempo y riesgo de error silencioso—
que uno mayor que cierra al primero.

La regla inversa también es cierta: usar el modelo más capaz para renombrar un archivo o
listar rutas es desperdicio puro. La decisión es un juicio sobre **cuántas iteraciones
espera la tarea**, no sobre qué tan importante se siente.

## Perfiles

No razones en nombres de modelo, razona en perfiles. Los nombres cambian; los perfiles no.

| Perfil | Qué hace bien | Tareas típicas |
|---|---|---|
| **ALTO** — razonamiento profundo | Sostiene muchas restricciones a la vez, encuentra causa raíz, evalúa trade-offs, detecta lo que falta | Diagnóstico de bugs sin causa evidente, diseño y arquitectura, refactor transversal, cambios `HIGH`/`CRITICAL`, especificación ambigua, revisión crítica final |
| **MEDIO** — ejecución guiada | Aplica un plan ya definido con buen criterio local | Implementar un plan cerrado, seguir un patrón existente del repo, tests focalizados, cambios `MEDIUM` acotados, redacción de documentación y PR |
| **BAJO** — mecánico | Transformaciones deterministas y volumen | Renombres, formato, aplicar una edición ya especificada archivo por archivo, inventarios, extracción y conteo, búsquedas amplias |

## Ejes de decisión

Evalúa los cinco. Si dos o más empujan hacia arriba, sube de perfil.

1. **Ambigüedad de la especificación.** ¿Hay que inferir intención, o está todo dicho? La
   ambigüedad es el mayor predictor de iteraciones perdidas.
2. **Profundidad de razonamiento.** ¿Decidir entre alternativas con trade-offs reales, o
   aplicar un patrón que ya existe en el repositorio?
3. **Amplitud de contexto.** Cuántos archivos, dominios o invariantes hay que sostener
   simultáneamente para no romper algo a distancia.
4. **Costo del error.** El nivel de `references/change-risk-matrix.md` y qué tan reversible
   es. `HIGH`/`CRITICAL` no se optimizan por costo.
5. **Verificabilidad barata.** ¿Existe un oráculo automático —tests, tipos, lint, build—
   que atrape el error en segundos?

El quinto eje es el que más se olvida y el que más ahorra: **cuando la verificación es
automática y barata, un perfil menor es seguro**, porque la iteración la cierra la máquina
y no una revisión humana. Cuando el error solo se detecta en producción, en datos o a los
tres días, sube de perfil aunque la tarea parezca simple.

## Reglas de escalamiento

- **Regla de los dos intentos.** Si el perfil menor no cerró la tarea en dos intentos, no
  hay un tercero: sube de perfil y **reinicia con contexto limpio**, no encima del contexto
  contaminado por los intentos fallidos. Dos iteraciones fallidas ya costaron más que haber
  empezado arriba. Esto dispara el punto de control de abajo — no sigas intentando por tu
  cuenta.
- **Riesgo manda sobre ahorro.** `HIGH` y `CRITICAL` van en perfil ALTO, aunque el cambio
  se vea pequeño. Un cambio de una línea en permisos sigue siendo un cambio de permisos.
- **No subas por importancia percibida.** Una tarea puede ser urgente y visible y aun así
  ser mecánica. Sube por ambigüedad, amplitud, costo del error o falta de oráculo — no por
  ansiedad.
- **Ante empate, sube uno.** Es el mismo criterio que la matriz de riesgo.

## Perfil mixto: la tarea no es una sola pieza

Una tarea rara vez tiene un solo perfil. Lo normal es **decidir en ALTO y ejecutar en
MEDIO**: el plan, la causa raíz y las decisiones de diseño en el perfil alto; los tests, la
documentación, el `CHANGELOG` y la PR en el perfil medio, ya con el plan cerrado.

Divide por fase antes de asumir que toda la tarea necesita el perfil más caro.

## Punto de control de motor — bloqueante

Cuando el perfil requerido es **mayor** que el del modelo que está corriendo, **detente y
pide autorización explícita antes de avanzar**, igual que para un merge o una migración de
producción. No es una sugerencia al pasar: es un punto de control. Un aviso que se emite y
se ignora en la misma respuesta no cambia nada — por eso esto bloquea.

Una skill no puede cambiar el modelo en el que corre; lo único que puede hacer es **no
seguir** hasta que el usuario decida. Eso es exactamente lo que hace falta.

### Cuándo dispara

Dos gatillos, cualquiera de los dos basta:

1. **Desajuste inicial.** El perfil requerido por la tarea es mayor que el del modelo
   actual, y el riesgo es `MEDIUM` o superior (o la auditoría es profunda). Dispara antes
   de editar o de lanzar la auditoría, no después.
2. **Dos intentos fallidos.** La misma subtarea falló dos veces con el modelo actual. No
   hagas un tercer intento: detente y pregunta. Este gatillo es el que más ahorra, porque
   corrige una estimación inicial equivocada antes de que se convierta en cinco iteraciones.

Si no puedes determinar con certeza en qué modelo estás corriendo, trata la incertidumbre
como desajuste cuando el riesgo sea `HIGH`/`CRITICAL`, y pregunta igual.

### Cuándo NO dispara

Que sea bloqueante no significa que sea frecuente. Un punto de control que aparece siempre
se vuelve ruido y se empieza a responder sin leer — ahí muere la utilidad. **No preguntes**
cuando:

- el perfil requerido es igual o menor que el actual;
- el riesgo es `LOW`;
- ya preguntaste por esta tarea (es **una vez por tarea**, no una por fase);
- la tarea es un ahorro posible, no un riesgo: si podrías bajar de perfil, dilo en una línea
  y sigue — bajar de perfil nunca bloquea.

### Cómo se pregunta

Con `AskUserQuestion` si está disponible; si no, en texto plano, y **detén el turno ahí**.
Sin párrafos previos, sin empezar a trabajar "mientras tanto".

```markdown
Punto de control — motor
Tarea: [una línea]  ·  Riesgo: [NIVEL]  ·  Perfil requerido: [ALTO/MEDIO]
Modelo actual: [nombre] (perfil [ALTO/MEDIO/BAJO])
Motivo del desajuste: [media línea: ambigüedad / amplitud / costo del error / sin oráculo]

A) Cambias de modelo y retomo — me detengo hasta que confirmes.
B) Sigo con el modelo actual — registro el desvío y continúo.
C) Delego solo las partes de razonamiento a un subagente de perfil ALTO y ejecuto el resto aquí.
```

Reglas de la espera:

- **No asumas B por silencio.** Sin respuesta no hay avance.
- Si eligen **B**, deja el desvío por escrito en el plan y en la PR: *"Ejecutado en perfil
  MEDIO con riesgo HIGH por decisión explícita del usuario."* La decisión es del usuario;
  esconderla no.
- Si eligen **C**, es la salida que no requiere que el usuario cambie nada: tú enrutas los
  subagentes y sigues.

## Los otros dos mecanismos

Además del punto de control, hay dos formas de aplicar el perfil. Sé honesto sobre cuál
corresponde:

- **Subagentes — enrutamiento real, sin preguntar.** El `Agent` tool acepta `model`, y las
  definiciones en `.claude/agents/*.md` fijan modelo y esfuerzo. Aquí se aplica solo:
  delega las subtareas de perfil MEDIO/BAJO y quédate con las de perfil ALTO. Esto no
  necesita autorización porque no cambia nada del entorno del usuario.
- **Otras herramientas (Codex, Antigravity, etc.) — solo mención.** Puedes recomendar mover
  la tarea a otra herramienta cuando encaja mejor, pero no la invoques desde la skill: mete
  autenticación, costo y salidas no verificables dentro de un flujo que se supone trazable.

## Formato cuando no hay desajuste

Cuando el perfil coincide o podrías bajar, no hay punto de control: una línea junto al
riesgo y sigues.

```markdown
Motor: ALTO (coincide con el modelo actual) — delegable a MEDIO: tests, CHANGELOG y PR
```

No conviertas esto en una sección con justificación larga: el valor está en la decisión, no
en el informe sobre la decisión.

## Modelos vigentes

Tabla de conveniencia, **no** la política. La política son los perfiles de arriba.

Verificada al **2026-07-28**. Los nombres de modelo cambian rápido; si esta fecha quedó
lejos, confirma antes de citarla y actualiza este bloque en la misma PR.

| Perfil | Claude Code (sesión) | `Agent` tool (`model:`) |
|---|---|---|
| ALTO | Opus 5, razonamiento alto | `opus` |
| MEDIO | Sonnet 5 | `sonnet` |
| BAJO | Haiku 4.5 | `haiku` |

Para herramientas fuera de Claude Code (Codex, Antigravity y similares), no fijes nombres
de versión aquí: pide el modelo más capaz disponible en esa herramienta para perfil ALTO, y
su esfuerzo de razonamiento alto cuando exista ese control. Sus catálogos rotan por su
cuenta y una tabla desactualizada es peor que ninguna.
