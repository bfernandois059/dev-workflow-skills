# Container Antipatterns

Catálogo de anti-patrones de **estructura y superficie**: cajas, títulos, mensajes y
acciones. Es la parte prescriptiva de `ux-critic` — cada entrada dice **qué no va, por qué, y
cómo debe hacerse**, con la estructura antes/después.

Se aplica en la Capa 2 (jerarquía) y la Capa 6 (sistema visual) del juicio. Son los hallazgos
que las auditorías genéricas nunca reportan, porque ningún checklist pregunta "¿esta caja
para qué está?".

**Advertencia de uso**: son reglas con excepciones nombradas, no dogma. Una regla se rompe
cuando el contexto de la Fase 0 lo justifica y **se dice explícitamente por qué**.

---

## Las siete reglas

| # | Regla | En una línea |
|---|---|---|
| R1 | **Dos superficies como máximo** | Una tarjeta dentro de un panel. Un tercer nivel resta jerarquía en vez de darla |
| R2 | **Un título por superficie** | Ninguna caja contiene otra caja cuyo título sea variación del suyo |
| R3 | **El estado se dice una vez** | Y se dice donde el usuario decide, no en tres lugares |
| R4 | **Una acción primaria por zona visible** | El resto son secundarias o terciarias |
| R5 | **El peso lo fija frecuencia × deseabilidad** | No la novedad de la acción ni lo orgulloso que esté el equipo de ella |
| R6 | **El espacio agrupa antes que el borde** | Se recurre al borde solo cuando el espacio ya no alcanza |
| R7 | **El vacío ofrece, no se explica** | Un estado vacío entrega la acción que lo llena; no justifica su vacío |

---

## A1 · Cajas anidadas sin función

**Qué se ve.** Tres o más superficies encajadas: panel → tarjeta → tabla → fila-tarjeta.
Cada una con su propio borde, su propio fondo y su propio padding.

**Por qué falla.** Una superficie comunica "esto es una unidad separada del resto". Cuando
todo está separado de todo, nada está separado: el usuario deja de leer los bordes como
información y empieza a leerlos como ruido. Además cada nivel roba entre 16 y 32 px de ancho
útil, que en móvil se paga en scroll.

**Prueba.** Por cada superficie: *¿qué separa esta caja que el espacio en blanco no podría
separar?* Si no hay respuesta en una frase, la caja sobra.

**Cómo debe hacerse.** Máximo dos niveles de superficie (R1). El tercer nivel se resuelve con
espacio, un separador de 1 px o un cambio de peso tipográfico.

```
❌ Antes                                  ✅ Después
Panel [borde + fondo]                     Título de sección (texto, sin caja)
  Tarjeta [borde + fondo]                   Bajada de una línea
    Tabla [borde + encabezado]              ── una superficie con filas ──
      Fila [borde + fondo]                  fila · fila · fila
      Fila [borde + fondo]
```

**Excepción nombrada.** Un tercer nivel se justifica cuando el contenido interno es
seleccionable, arrastrable o tiene estado propio que hay que distinguir del contenedor.

---

## A2 · Título en eco

**Qué se ve.** "Documentos técnicos" contiene "Documentos técnicos obligatorios", que
contiene una tabla con la columna "DOCUMENTO". Tres veces la misma palabra en 200 px de
alto.

**Por qué falla.** El usuario lee tres títulos y no recibe tres informaciones. La repetición
le hace sospechar que se perdió algo — vuelve a leer para encontrar la diferencia que no
existe. Es costo de atención sin retorno.

**Prueba.** Lee en voz alta los títulos anidados en secuencia. Si suenan a la misma frase con
un adjetivo agregado, sobra uno.

**Cómo debe hacerse.** Un solo título, el más específico (R2). El nivel externo, si de verdad
hace falta, se identifica por posición o por la pestaña, no por otro título.

```
❌ Pestaña "Documentos" → panel "Documentos técnicos" → tarjeta "Documentos técnicos obligatorios"
✅ Pestaña "Documentos" → "Obligatorios" (o directamente la lista, si no hay otra categoría)
```

**Regla derivada.** Si una pestaña ya se llama X, ninguna caja dentro de esa pestaña se llama
X. La pestaña ya lo dijo.

---

## A3 · Estado repetido

**Qué se ve.** El mismo hecho comunicado tres o cuatro veces: una etiqueta "Documentación
completa" en el encabezado, un "Cargado" por fila, un pie que dice "Documentación técnica
lista para finalizar" y, en otra pantalla, "Documentos técnicos completos".

**Por qué falla.** La repetición no tranquiliza: genera duda. Si el sistema necesita decirlo
cuatro veces, el usuario asume que hay una diferencia entre las cuatro. Y cuando algo falle,
el usuario no sabrá cuál de los cuatro indicadores es el que manda.

**Prueba.** Lista todos los lugares donde aparece el mismo estado. Más de dos —el detalle por
ítem y el resumen en el punto de decisión— es redundancia.

**Cómo debe hacerse.** El estado por ítem se queda donde está el ítem. El estado agregado se
dice **una vez**, pegado a la acción que ese estado habilita o bloquea (R3).

```
❌ encabezado: "Documentación completa"
   por fila:   "Cargado" ×2
   pie:        "Documentación técnica lista para finalizar."
   otra vista: "Documentos técnicos completos"

✅ por fila:   "Cargado" ×2
   junto al botón Finalizar: "Documentación completa" (o el botón deshabilitado con la razón)
```

---

## A4 · Todo es una tarjeta

**Qué se ve.** Un mensaje informativo dentro de un banner con borde y fondo; un input dentro
de su propia tarjeta; un aviso de estado dentro de otra caja. La pantalla es una pila de seis
u ocho superficies del mismo peso.

**Por qué falla.** Cuando cada bloque pesa lo mismo, la página no tiene ritmo: es una lista
de cajas equivalentes y el usuario tiene que leerlas todas para saber cuál importa. Es el
mecanismo exacto por el que una pantalla "ordenada" se siente plana y agotadora.

**Prueba.** Cuenta las superficies apiladas en una pantalla. Más de cuatro del mismo peso
visual es hallazgo. Después pregunta cuál es la más importante: si la respuesta necesita
justificación, ninguna lo es.

**Cómo debe hacerse.**

- Un mensaje que **solo informa** va como texto, con su icono si hace falta. Sin caja (R6).
- Se reserva la caja para lo que se puede **accionar, descartar o que interrumpe**.
- Un input suelto no necesita tarjeta propia: necesita una etiqueta y espacio arriba.
- Si de verdad hay cuatro secciones, se diferencian por peso —una dominante, el resto
  planas— no por repetir el mismo tratamiento cuatro veces.

```
❌ [caja] Continúa con el registro técnico y la evidencia de esta visita.
❌ [caja] Fecha de ejecución del servicio  [input]
✅ Continúa con el registro técnico y la evidencia de esta visita.   ← texto, con icono
✅ Fecha de ejecución del servicio *                                  ← label + input, sin caja
```

---

## A5 · Acciones sin jerarquía

**Qué se ve.** En una fila, "Abrir" con borde y "Reemplazar" en sólido. Arriba, "Volver al
trabajo" con el mismo tratamiento que una acción del flujo. Todos los botones pesan parecido,
o pesa más el que menos se usa.

**Por qué falla.** El peso visual es una instrucción: dice "haz esto". Si la acción más
pesada de la pantalla es la más rara y la más destructiva —reemplazar un documento ya
cargado—, la interfaz está empujando al usuario hacia el error. Y si todos pesan igual, el
usuario decide antes de entender.

**Prueba.** Ordena las acciones visibles por frecuencia esperada y por deseabilidad. Compara
ese orden con el orden de peso visual. Si no coinciden, es hallazgo — y en acciones
destructivas es `P0` o `P1`.

**Cómo debe hacerse.** Una primaria por zona (R4); el peso se asigna por frecuencia ×
deseabilidad (R5); la navegación no es una acción del flujo y no compite con él.

```
❌ [Abrir (outline)] [Reemplazar (sólido)]
✅ Abrir (primaria, la que se usa siempre) · Reemplazar (texto o menú "⋯", rara y riesgosa)

❌ [Volver al trabajo (botón, arriba a la derecha)]
✅ ← Volver al trabajo (enlace, arriba a la izquierda, donde se busca volver)
```

---

## A6 · Input que parece deshabilitado

**Qué se ve.** Campos con relleno gris, borde tenue o ausente y placeholder de bajo contraste.
El usuario no sabe si puede escribir ahí.

**Por qué falla.** El relleno gris es la convención de "campo inactivo" en casi todos los
sistemas. Usarlo para campos activos gasta la única señal disponible para decir "esto no se
puede tocar": cuando después haya un campo realmente deshabilitado, no habrá cómo mostrarlo.

**Prueba.** Compara el campo activo con el campo deshabilitado del mismo formulario. Si se
ven parecidos, el sistema perdió la distinción. Mide además el contraste del placeholder y
del borde.

**Cómo debe hacerse.** Elige una convención y sostenla:

- **Campo activo**: fondo del mismo valor que la superficie + borde de contraste ≥ 3:1, o
  fondo apenas distinto + borde definido. Placeholder ≥ 4.5:1 y **no** usado como etiqueta.
- **Campo deshabilitado**: relleno apagado, borde apagado, cursor `not-allowed` y, si el
  motivo importa, el motivo escrito.
- **Foco**: visible, con contraste, nunca `outline: none` sin reemplazo.

---

## A7 · Doble bloque para una sola tarea

**Qué se ve.** Una caja "Equipos pendientes de registrar" con el botón de agregar, y justo
debajo otra caja "Mantención preventiva ejecutada" cuyo contenido completo es "Esta orden no
tiene equipos registrados. Agrega un equipo antes de registrar el trabajo."

**Por qué falla.** Dos bloques para un solo hecho —no hay equipos— y el segundo es un callejón
sin salida: explica el problema y manda al usuario de vuelta al bloque anterior. El usuario
lee dos veces, actúa una.

**Prueba.** Por cada bloque en estado vacío: *¿ofrece la acción que lo llena, o solo explica
por qué está vacío?* Si solo explica, y la acción ya vive en otro bloque, el bloque sobra.

**Cómo debe hacerse.** Un solo bloque con el estado vacío y la acción dentro (R7). Las
secciones que dependen de ese dato no aparecen todavía, o aparecen atenuadas con una línea de
texto, no con una caja propia.

```
❌ [caja] Equipos pendientes de registrar   [+ Agregar equipo en terreno]
   [caja] Mantención preventiva ejecutada
          Esta orden no tiene equipos registrados. Agrega un equipo antes de registrar.

✅ Equipos
   Aún no registras equipos en terreno. El registro de mantención se habilita al agregar
   el primero.
   [+ Agregar equipo en terreno]
```

---

## Cómo reportarlos

Estos hallazgos van en la ficha estándar (`report-format.md`) y **exigen el árbol de
estructura antes/después**: sin él, "simplificar la jerarquía de contenedores" es otra vez
una recomendación tibia. El árbol es la instrucción.

Cuando el mismo anti-patrón aparece en varias pantallas, se reporta **una vez** como patrón
transversal, con la lista de dónde aparece, y entra al plan de corrección como una sola tarea
de sistema — no como seis tareas de pantalla.
