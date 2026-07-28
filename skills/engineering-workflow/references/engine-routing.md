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
  empezado arriba.
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

## Cómo se aplica realmente

Tres mecanismos, con alcances distintos. Sé honesto sobre cuál corresponde:

1. **Sesión principal — solo sugerencia.** Una skill no puede cambiar el modelo en el que
   corre. Emite la recomendación en una línea y **sigue trabajando**; el usuario cambia de
   modelo si quiere. Nunca bloquees esperando respuesta.
   - Excepción: si el cambio es `HIGH`/`CRITICAL` y el modelo actual está claramente por
     debajo del perfil, dilo explícitamente **una vez** antes de editar, y continúa solo si
     el usuario lo confirma o insiste.
2. **Subagentes — enrutamiento real.** El `Agent` tool acepta `model`, y las definiciones
   en `.claude/agents/*.md` fijan modelo y esfuerzo. Aquí sí se aplica sin intervención:
   delega las subtareas de perfil MEDIO/BAJO y quédate con las de perfil ALTO.
3. **Otras herramientas (Codex, Antigravity, etc.) — solo mención.** Puedes recomendar
   mover la tarea a otra herramienta cuando encaja mejor, pero no la invoques desde la
   skill: mete autenticación, costo y salidas no verificables dentro de un flujo que se
   supone trazable.

## Formato de salida

Un bloque corto, después de asignar el riesgo. Sin párrafos.

```markdown
Motor sugerido: ALTO — causa raíz desconocida + toca RLS (riesgo HIGH)
Delegable a MEDIO: tests, CHANGELOG y redacción de PR una vez cerrado el plan
```

Si el perfil sugerido coincide con lo que ya está corriendo, una línea basta o se omite.
No conviertas esto en una sección con justificación larga: el valor está en la decisión,
no en el informe sobre la decisión.

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
