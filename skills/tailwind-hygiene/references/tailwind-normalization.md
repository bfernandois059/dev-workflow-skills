# Tailwind Normalization

Material de consulta de `tailwind-hygiene`. Cada sección responde cinco cosas: **qué parece
sucio**, **qué puede normalizarse sin cambiar el render**, **qué evidencia confirma la
equivalencia**, **qué debe dejarse quieto** y **qué indicaría que la tarea pertenece a otra
skill**.

> **Consulta solo las secciones relacionadas con las clases o la configuración que tienes en
> alcance.** No es un manual general de Tailwind: es material para decidir si una transformación
> concreta preserva el resultado. Ninguna normalización listada aquí es obligatoria.

Lo que ya está en [`SKILL.md`](../SKILL.md) no se repite: frontera con las demás skills, regla de
equivalencia exacta, arbitrary values como no-defecto, tokens por repetición, orden de clases,
qué significa preservar exactamente, validación antes/después y formato de entrega.

| Sección | Cuándo abrirla |
|---|---|
| [Arbitrary values](#arbitrary-values) | Hay corchetes y hay que decidir si se tocan |
| [Spacing](#spacing) | `p-`, `m-`, `gap-`, `space-` arbitrarios o mezclados |
| [Tipografía](#tipografía) | Tamaños, line-height, tracking y peso dispersos |
| [Color](#color) | Hex, `rgb()`, tokens y variables conviviendo |
| [Radius y sombras](#radius-y-sombras) | `rounded-*` y `shadow-*` fuera de escala |
| [Duplicados y conflictos](#duplicados-y-conflictos) | Dos utilidades sobre la misma propiedad |
| [Variantes responsive](#variantes-responsive) | Prefijos `sm:`, `md:`, `lg:` en el alcance |
| [Variantes de estado](#variantes-de-estado) | `hover:`, `data-*`, `group-*`, `peer-*` |
| [CSS variables](#css-variables) | `var(--…)` dentro o fuera de corchetes |
| [`cn` y `clsx`](#cn-y-clsx) | El `className` se arma con un helper |
| [`cva`](#cva) | El componente define variantes con `cva` |
| [`tailwind-merge`](#tailwind-merge) | Hay merge de clases en runtime |
| [Clases condicionales](#clases-condicionales) | Estilos que dependen de props o estado |
| [Generación dinámica](#generación-dinámica) | Clases construidas con interpolación |
| [`!important`](#important) | Aparece el prefijo `!` |
| [Interop con CSS](#interop-con-css) | Conviven utilities con CSS Modules o global |
| [Tailwind v3](#tailwind-v3) | El proyecto usa `tailwind.config.*` |
| [Tailwind v4 y `@theme`](#tailwind-v4-y-theme) | El proyecto define el theme en CSS |
| [Utilities custom](#utilities-custom) | Hay utilidades propias del proyecto |
| [Plugins](#plugins) | El theme llega desde un plugin o preset |
| [Dark mode](#dark-mode) | Hay `dark:` o theming por clase o atributo |
| [Transiciones y animación](#transiciones-y-animación) | `transition-*`, `animate-*`, `duration-*` |
| [Sincronizar theme y config](#sincronizar-theme-y-config) | El theme y el uso real divergieron |

---

## Arbitrary values

**Qué parece sucio.** Cualquier `[...]`, tratado como deuda por el solo hecho de llevar corchetes.

**Qué puede normalizarse.** El valor arbitrario que **duplica una decisión que el sistema ya
expone** con un token exactamente igual: `mt-[24px] → mt-6` cuando el theme resuelve `6` a 24px.

**Qué evidencia confirma equivalencia.** El valor resuelto del token en el theme real del
proyecto —`tailwind.config.*`, `@theme`, preset o plugin—, no una escala recordada de memoria.

**Qué dejar quieto.** `calc()`, variables CSS, grid templates, geometría del layout, valores
derivados de otro elemento, `env()`, integraciones con primitives y todo valor que exprese una
relación que no pertenece a una escala.

**Cuándo es de otra skill.** Si el valor arbitrario es correcto pero nadie lo formalizó y
conviene que exista como token, la decisión es de `visual-foundation`. Si el valor es simplemente
el equivocado, es un cambio visual: `interface-craft`.

---

## Spacing

**Qué parece sucio.** `p-[24px]` junto a `p-6`; `px-[24px] py-[24px]` donde bastaría `p-6`;
`mt-*` y `space-y-*` resolviendo lo mismo en el mismo contenedor.

**Qué puede normalizarse.** La escritura equivalente: `px-4 py-4 → p-4`, `px-[24px] → px-6` con
equivalencia confirmada, y la utilidad redundante cuando está demostrado cuál aplica.

**Qué evidencia confirma equivalencia.** El valor del step en el theme y el cálculo completo de
la caja: `p-4` no equivale a `px-4 py-4` si algo más define `padding-top` después.

**Qué dejar quieto.** La diferencia entre `gap`, `space-*` y márgenes cuando afecta a hijos
distintos —`space-y-*` no aplica al primer hijo, `gap` sí cambia el comportamiento con `flex-wrap`—.
Valores fuera de escala que no tienen token equivalente.

**Cuándo es de otra skill.** Si el spacing está mal elegido, no mal escrito: `interface-craft`.
Si el mismo valor fuera de escala se repite y merecería un step propio: `visual-foundation`.

---

## Tipografía

**Qué parece sucio.** `text-[15px]`, `leading-[1.4]`, `tracking-[-0.01em]` conviviendo con los
roles del sistema; tamaño y line-height declarados por separado donde el token trae ambos.

**Qué puede normalizarse.** El arbitrario que coincide exactamente con un role existente, en
tamaño **y** en las propiedades que ese role arrastra.

**Qué evidencia confirma equivalencia.** La definición completa del `fontSize` en el theme: en
Tailwind un role puede traer `line-height`, `letter-spacing` y `font-weight` asociados, así que
`text-[15px] → text-base` puede cambiar el interlineado aunque el tamaño coincida.

**Qué dejar quieto.** Tamaños que no coinciden exactamente, ajustes ópticos deliberados de
`tracking` en titulares, y `leading` calculado sobre una altura concreta.

**Cuándo es de otra skill.** «Debería verse en `text-base`» cuando hoy no lo es, es un cambio
visual: `interface-craft`. Si falta el role en el sistema: `visual-foundation`.

---

## Color

**Qué parece sucio.** Hex crudos, `rgb()` inline, `bg-[#1e1e1f]` junto a tokens semánticos, y
opacidades expresadas de dos formas.

**Qué puede normalizarse.** El hex que corresponde **exactamente** al valor de un token del
proyecto, y solo si ese token representa el mismo rol.

**Qué evidencia confirma equivalencia.** El valor exacto del token, incluida la forma en que la
versión de Tailwind aplica la opacidad —`bg-black/50` y `bg-[rgba(0,0,0,.5)]` pueden diferir
cuando el color pasa por `color-mix()` o por un canal alfa de variable—.

**Qué dejar quieto.** Colores cercanos pero distintos: `#1e1e1f` no es `neutral-900`. Colores que
vienen de una variable con semántica o theming. Colores de un primitive o de una marca externa.

**Cuándo es de otra skill.** Unificar colores parecidos cambia el render: `interface-craft`, o
`visual-foundation` si lo que falta es la regla que diga cuál es el correcto.

---

## Radius y sombras

**Qué parece sucio.** `rounded-[8px]` junto a `rounded-lg`; sombras arbitrarias largas repetidas
en varios componentes; `shadow` y `ring` combinados sin criterio aparente.

**Qué puede normalizarse.** El arbitrario idéntico al token, y la sombra arbitraria que coincide
carácter por carácter con la definida en el theme.

**Qué evidencia confirma equivalencia.** El valor del token y el orden de capas: dos sombras con
los mismos números pero distinto orden de capas no renderizan igual, y `ring` participa del mismo
apilado que `shadow`.

**Qué dejar quieto.** Radios que dependen de la geometría —`rounded-full` sobre un elemento no
cuadrado, radios anidados calculados respecto del contenedor— y sombras que expresan una
elevación que el sistema no tokenizó.

**Cuándo es de otra skill.** Homogeneizar radios o elevaciones «para que combinen» es diseño:
`interface-craft`.

---

## Duplicados y conflictos

**Qué parece sucio.** `flex flex`, `rounded-md rounded-lg`, `hidden flex`, `px-4 px-6`, y strings
donde ya no se sabe qué gana.

**Qué puede normalizarse.** La utilidad exactamente repetida, y la contradicción **una vez
demostrado** cuál produce el estilo observable — conservando ese resultado, no el que parezca más
razonable.

**Qué evidencia confirma equivalencia.** El estilo computado en el render, no la posición en el
string: el orden lo decide el CSS generado, no el atributo. Cuando hay `tailwind-merge`, manda su
resolución; cuando hay variantes, `!`, CSS externo o composición en runtime, hay que mirar el
resultado real.

**Qué dejar quieto.** La utilidad que parece redundante pero actúa como fallback, o que aplica en
un breakpoint, un estado o un tema en el que la otra no está activa.

**Cuándo es de otra skill.** Si la contradicción viene de que dos componentes se pisan por
arquitectura, la corrección estructural es `component-architecture`.

---

## Variantes responsive

**Qué parece sucio.** Muchos prefijos por elemento, breakpoints arbitrarios `min-[832px]:`, y
valores arbitrarios repetidos por breakpoint.

**Qué puede normalizarse.** El valor dentro de la variante: `md:gap-[24px] → md:gap-6` con
equivalencia confirmada. Y la utilidad base que un breakpoint ya sobrescribe **en todos** los
anchos posibles.

**Qué evidencia confirma equivalencia.** Que el breakpoint arbitrario coincida exactamente con
uno del theme antes de sustituirlo, y el render en los viewports afectados.

**Qué dejar quieto.** Qué breakpoint usa cada regla, el orden de las variantes, la visibilidad
por tamaño y la composición. Tailwind aplica `min-width` acumulativo: mover una regla de `md:` a
`lg:` cambia el comportamiento entre ambos.

**Cuándo es de otra skill.** Cualquier ajuste que cambie cómo responde la interfaz —incluido
«en tablet queda estrecho»— es `adaptive-layout`.

---

## Variantes de estado

**Qué parece sucio.** Cadenas largas de `hover:`, `focus-visible:`, `disabled:`, `group-*`,
`peer-*`, `data-*` y `aria-*` que hacen ilegible el `className`.

**Qué puede normalizarse.** El valor dentro de la variante, los duplicados exactos y el
agrupamiento cuando el proyecto ya usa esa sintaxis y el resultado se conserva.

**Qué evidencia confirma equivalencia.** El render de cada estado afectado: hover, foco de
teclado, deshabilitado, y los estados `data`/`aria` que el componente realmente emite.

**Qué dejar quieto.** `focus-visible:` no es `focus:`. `group-hover:` depende de un ancestro con
`group` y `peer-*` del orden de hermanos: quitar o mover esas marcas rompe la relación. Y una
variante que no se ve en una captura estática sigue existiendo.

**Cuándo es de otra skill.** Si falta un estado —no hay foco visible, no hay estado
deshabilitado—, eso es un defecto de interfaz: `interface-craft` o `ux-audit`.

---

## CSS variables

**Qué parece sucio.** `bg-[var(--surface-muted)]` repetido, variables que conviven con tokens
equivalentes y `style={{ '--x': … }}` mezclado con utilities.

**Qué puede normalizarse.** La sustitución por la utility semántica **basada en esa misma
variable** —`bg-[var(--surface)] → bg-surface`— cuando el theme la expone y la equivalencia está
confirmada.

**Qué evidencia confirma equivalencia.** Que la utility resuelva a la misma variable, no a una
copia de su valor: si la utility congela el valor actual, el theming en runtime deja de
funcionar.

**Qué dejar quieto.** La variable que expresa semántica, theming, valor calculado en runtime o
contrato con un primitive. **Nunca se sustituye por un color hardcodeado** aunque hoy coincidan.

**Cuándo es de otra skill.** Crear la variable o el rol que falta: `visual-foundation`.

---

## `cn` y `clsx`

**Qué parece sucio.** `className={"base " + (x ? "a" : "") + " " + props.className}`, plantillas
con saltos de línea dentro del string y espacios dobles.

**Qué puede normalizarse.** Pasar esa concatenación al helper que el proyecto **ya usa**,
preservando el orden de los argumentos y la precedencia resultante.

**Qué evidencia confirma equivalencia.** Las combinaciones relevantes de props y estado, no solo
el caso por defecto — y que `props.className` siga llegando en la misma posición.

**Qué dejar quieto.** El helper vigente: no cambies `clsx` por `cn` ni al revés en toda la
aplicación. Si no hay helper, una concatenación simple y legible es una respuesta válida.

**Cuándo es de otra skill.** Rehacer la API de clases del componente para toda la familia:
`component-architecture`.

---

## `cva`

**Qué parece sucio.** Condicionales de estilo repartidos por el JSX en un componente que ya
define variantes con `cva`, o `cva` con `compoundVariants` difíciles de seguir.

**Qué puede normalizarse.** Mover al `cva` existente un estilo que **ya** corresponde a una
variante declarada, y limpiar duplicados dentro de sus listas.

**Qué evidencia confirma equivalencia.** Cada combinación declarada, incluidas las
`compoundVariants` y los `defaultVariants`: cambiar el orden de las claves puede cambiar qué gana.

**Qué dejar quieto.** `cva` no se introduce para una limpieza puntual si el proyecto no lo usa, y
no se inventan variantes nuevas para acomodar estilos sueltos.

**Cuándo es de otra skill.** Definir qué variantes **debería** tener el componente:
`component-architecture`, o `visual-foundation` si falta el vocabulario del sistema.

---

## `tailwind-merge`

**Qué parece sucio.** Clases aparentemente contradictorias en un componente que hace merge, o
`twMerge` envolviendo cadenas que no lo necesitan.

**Qué puede normalizarse.** Los duplicados que el merge ya resuelve igual, con el mismo resultado
observable.

**Qué evidencia confirma equivalencia.** La semántica real del merge: agrupa por propiedad y gana
el último de cada grupo, salvo configuración propia. Con utilities custom o prefijos, la
configuración del proyecto puede alterar esa agrupación.

**Qué dejar quieto.** No lo introduzcas para evitar razonar una colisión local, y no elimines el
merge de un componente que expone `className` al consumidor: eso cambia quién gana.

**Cuándo es de otra skill.** Si la colisión existe porque dos capas de componentes se disputan el
mismo estilo, el arreglo estructural es `component-architecture`.

---

## Clases condicionales

**Qué parece sucio.** Ternarios anidados, condiciones negadas dos veces y ramas que aplican la
misma clase.

**Qué puede normalizarse.** Reescribir la condición conservando **exactamente** el resultado en
todas las combinaciones: cada flag por separado, combinados y ninguno.

**Qué evidencia confirma equivalencia.** Recorrer esas combinaciones en el render, no razonar
solo sobre el código. Una condición «imposible» según los tipos puede darse con datos reales.

**Qué dejar quieto.** La ubicación de la decisión: no muevas lógica a CSS —`peer`, `group`,
`data-*`— ni CSS a lógica por preferencia. No conviertas un ternario en `&&` si eso elimina la
rama que restablecía el estilo por defecto.

**Cuándo es de otra skill.** Si la condición codifica una regla de negocio mal ubicada:
`component-architecture`.

---

## Generación dinámica

**Qué parece sucio.** `` `bg-${color}-500` ``, `` `grid-cols-${n}` `` y strings compuestos en
runtime.

**Qué puede normalizarse.** Sustituirlos por el patrón que el proyecto ya emplea —mapa explícito,
variantes, la safelist existente— **cuando las clases resultantes sean las mismas que hoy se
generan**.

**Qué evidencia confirma equivalencia.** Qué clases produce hoy el build: si la interpolación
nunca llegó al CSS, el elemento no tiene ese estilo, y «arreglarlo» lo agrega.

**Qué dejar quieto.** No crees una safelist grande para sostener una abstracción deficiente, y no
introduzcas interpolación nueva en un proyecto que necesita clases estáticamente descubribles.

**Cuándo es de otra skill.** Si al corregirlo aparece un estilo que antes no se aplicaba, hay un
defecto visual real: decláralo y deriva a `interface-craft`. **No lo presentes como higiene
invisible.**

---

## `!important`

**Qué parece sucio.** `!mt-0`, `!hidden` y cadenas con varios `!` en el mismo componente.

**Qué puede normalizarse.** Nada por defecto. Solo puede quitarse cuando esté demostrado que la
regla gana igual sin él.

**Qué evidencia confirma equivalencia.** El estilo computado con y sin el prefijo, en los estados
y breakpoints donde esa clase participa.

**Qué dejar quieto.** El `!` que actúa como override legítimo sobre un primitive o sobre CSS
externo. Tampoco lo sustituyas por más specificity ni por una cadena más compleja solo para
eliminarlo.

**Cuándo es de otra skill.** Si la única forma de quitarlo es cambiar cómo el primitive o el
componente reciben estilos, eso es `component-architecture`; si cambia el resultado,
`interface-craft`.

---

## Interop con CSS

**Qué parece sucio.** Utilities conviviendo con CSS Modules, hoja global, estilos inline y
estilos del primitive sobre el mismo elemento.

**Qué puede normalizarse.** La utility que esté demostradamente inerte, y los duplicados internos
de Tailwind que no participan de ninguna cascada externa.

**Qué evidencia confirma equivalencia.** El estilo computado del elemento, con el CSS externo
cargado. Una utility que parece redundante puede ser el fallback cuando la regla externa no
aplica.

**Qué dejar quieto.** El CSS existente: esta skill **no migra estilos** en ninguna dirección. Y
los inline styles, que ganan a las utilities salvo `!`.

**Cuándo es de otra skill.** Convertir CSS Modules a Tailwind o al revés es una tarea de
migración aparte, no higiene.

---

## Tailwind v3

**Qué parece sucio.** `tailwind.config.*` con `extend` creciendo sin orden, valores repetidos
entre config y uso, y `theme` conviviendo con variables CSS.

**Qué puede normalizarse.** El uso que ya tiene token equivalente en la config real, y la
exposición coherente de un valor que la config ya define.

**Qué evidencia confirma equivalencia.** La config resuelta, incluidos presets y plugins: lo que
está en `extend` se suma a la escala por defecto, y un plugin puede redefinir lo que parece
estándar.

**Qué dejar quieto.** `content`, prefijos, `corePlugins`, la escala por defecto y cualquier
entrada cuyo consumo no hayas verificado.

**Cuándo es de otra skill.** Migrar a v4 o reorganizar el sistema de tokens no es higiene.

---

## Tailwind v4 y `@theme`

**Qué parece sucio.** `@theme` conviviendo con variables definidas en `:root`, utilities que
parecen faltar y valores duplicados entre CSS y uso.

**Dos familias distintas, y confundirlas lleva a formalizar de más:**

| Familia | Cómo existe la utility |
|---|---|
| **Semántica, por namespace de theme** | Cada variable declarada en `@theme` bajo su namespace —`--color-*`, `--font-*`, `--radius-*`, `--shadow-*`, `--breakpoint-*`— genera su utility: `--color-surface-muted` habilita `bg-surface-muted`. Sin la variable, la utility no existe |
| **Numérica dinámica, derivada de `--spacing`** | Las familias de spacing y sizing se calculan del estilo `calc(var(--spacing) * <número>)`. La utility **no necesita un token individual con ese nombre**: con `--spacing: 0.25rem`, `gap-4.5` resuelve a 18px |

**Qué puede normalizarse.** El arbitrario que coincide con una variable de theme ya declarada; la
expresión coherente de un rol que `@theme` ya define; y el arbitrario numérico que una utility
dinámica ya expresa exactamente —`gap-[18px] → gap-4.5`— sin tocar el theme.

**Qué evidencia confirma equivalencia.** Para la familia semántica, que la variable esté en
`@theme` —y no solo en `:root`—, porque solo la primera genera utility. Para la numérica, el valor
real de `--spacing` y la multiplicación completa, no el supuesto de que la escala sea la de
fábrica: un proyecto puede redefinir `--spacing` y mover todas las utilities a la vez. En ambos
casos, el valor resuelto tras todos los `@import`.

**Qué dejar quieto.** La diferencia entre una variable de theme y una variable de aplicación: no
todas las variables deben generar utilities, y moverlas cambia la superficie del sistema. Y el
valor numérico que **no** cae exactamente en un múltiplo de `--spacing`: ahí la utility dinámica
no existe y el arbitrario sigue siendo correcto.

**Cuándo es de otra skill.** Decidir qué roles existen en `@theme` o cambiar `--spacing`:
`visual-foundation`. Que una utility dinámica ya exprese el valor **no** es crear un token, así
que no hay nada que derivar en ese caso.

---

## Utilities custom

**Qué parece sucio.** Utilidades propias que se solapan con las de Tailwind, o clases de
componente definidas con `@apply` que nadie recuerda.

**Qué puede normalizarse.** El uso que duplica exactamente una utility custom existente, y los
duplicados dentro de su definición.

**Qué evidencia confirma equivalencia.** La definición completa de la utility —incluido su
comportamiento en variantes— y su render, no su nombre.

**Qué dejar quieto.** Las utilities custom que parecen sin uso: pueden consumirse
dinámicamente, desde stories, templates o paquetes compartidos. No se borran aquí.

**Cuándo es de otra skill.** La eliminación de utilities realmente sin uso es `tech-cleanup`;
decidir cuáles deberían existir, `visual-foundation`.

---

## Plugins

**Qué parece sucio.** Clases que no aparecen en la config y parecen inventadas, o valores que
contradicen el theme visible.

**Qué puede normalizarse.** El uso que el plugin ya cubre con una utility equivalente confirmada.

**Qué evidencia confirma equivalencia.** La config **resuelta**, no el archivo: un plugin o un
preset puede añadir escalas, variantes y utilities que no están escritas en el proyecto.

**Qué dejar quieto.** Los plugins instalados y su configuración. No se agregan ni se quitan
plugins como parte de una limpieza.

**Cuándo es de otra skill.** Introducir un plugin es una decisión de dependencia:
`engineering-workflow` según su riesgo, y la decisión visual, de `visual-foundation`.

---

## Dark mode

**Qué parece sucio.** `dark:` repetido en cada elemento donde un token semántico bastaría, o
colores duplicados por tema.

**Qué puede normalizarse.** La sustitución por el token semántico **cuando resuelve a los mismos
valores en ambos temas**.

**Qué evidencia confirma equivalencia.** El render en los dos temas. Es el caso donde «se ve
igual» en una sola captura engaña con más facilidad.

**Qué dejar quieto.** La estrategia de dark mode del proyecto —clase, atributo, `media`— y las
excepciones deliberadas por tema.

**Cuándo es de otra skill.** Si falta el token semántico o el tema está incompleto:
`visual-foundation`.

---

## Transiciones y animación

**Qué parece sucio.** `duration-[200ms]` junto a `duration-200`, `transition-all` en todas
partes, y `animate-*` custom repetidos.

**Qué puede normalizarse.** Duraciones y curvas arbitrarias idénticas a un token existente.

**Qué evidencia confirma equivalencia.** La duración, la curva, el delay y **qué propiedades**
transicionan: `transition-all → transition-colors` reduce el alcance y puede eliminar una
transición que sí se percibía.

**Qué dejar quieto.** `transition-all` cuando algo más que el color está transicionando,
`prefers-reduced-motion` y sus variantes, y las animaciones definidas en keyframes propios.

**Cuándo es de otra skill.** Ajustar cómo se siente una transición es diseño de movimiento:
`interface-craft`.

---

## Sincronizar theme y config

**Qué parece sucio.** El theme define un rol que el código no usa, o el código usa un valor que
el theme ya declara sin exponerlo como utility.

**Qué puede normalizarse.** Exponer de forma coherente una decisión **que ya existe** —variable
declarada, rol definido en `ui-system.md`— para que los consumidores dejen de escribirla a mano,
sin cambiar el valor ni la semántica.

**Qué evidencia confirma equivalencia.** El valor antes y después en cada consumidor afectado, y
que ningún otro uso del token cambie de resultado.

**Qué dejar quieto.** Escalas, breakpoints, colores, radios y spacing existentes. Redefinirlos
—aunque «mejore» el sistema— no es sincronizar: es decidir de nuevo.

**Cuándo es de otra skill.** Si la decisión no está tomada, formalizarla es `visual-foundation`;
si el cambio altera el render de algún consumidor, es `interface-craft`.
