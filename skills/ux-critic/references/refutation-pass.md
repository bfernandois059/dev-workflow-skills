# Refutation Pass

Fase 4 de `ux-critic`. Obligatoria. Es el QA manual que las auditorías complacientes se
saltan: el momento en que el crítico intenta destruir su propio informe antes de entregarlo.

El fallo típico no es reportar de más, es **aprobar de menos**: escribir "cumple" sobre algo
que nunca se probó y dejar al usuario descubriéndolo a mano diez minutos después. Después de
eso, todo el informe pierde valor, incluida la parte que sí era correcta.

---

## Pasada 1 — Recorrido limpio

Cierra la lista de hallazgos. Completa la tarea principal de punta a punta **en las
condiciones del usuario real** (su viewport, su nivel de familiaridad, su prisa).

Anota, sin filtrar, cada punto donde:

- dudaste qué hacer;
- releíste algo;
- retrocediste;
- buscaste una información que no estaba donde esperabas;
- tuviste que interpretar en vez de leer.

**Cada duda anotada que no esté ya en tus hallazgos entra ahora.** Ese es el material que el
checklist no ve, porque el checklist pregunta "¿existe X?" y la duda aparece en cómo X se
relaciona con todo lo demás.

Si el recorrido limpio no produjo ninguna anotación, sospecha de ti mismo: o la interfaz es
excelente —y entonces puedes explicar exactamente por qué— o lo recorriste como auditor y no
como usuario.

## Pasada 2 — Ataque a cada `OK`

Por cada cosa que aprobaste, tres preguntas:

1. ¿Qué vería aquí alguien que llega por primera vez, sin el contexto que yo ya tengo?
2. ¿Qué pasa con esto en 375 px, con contenido largo, o con la conexión lenta?
3. ¿Lo aprobé porque lo verifiqué, o porque no encontré nada que objetar?

La tercera es la decisiva. **"No encontré nada" no es `OK`, es `Sin verificar`.** Un informe
que distingue las dos cosas es útil; uno que las mezcla es el que se cae en el QA manual.

Si no puedes defender el `OK` con evidencia concreta, bájalo a hallazgo o a `Sin verificar`.

## Pasada 3 — Ataque a cada hallazgo

Por cada hallazgo:

1. **¿Es un costo real para este usuario en esta tarea, o una regla que recité?** Si la única
   justificación es "las buenas prácticas dicen", bájalo a `criterio` o elimínalo.
2. **¿La corrección que propongo resuelve la causa o mueve el problema de lugar?** Ampliar un
   espaciado para que un bloque respire, cuando el problema es que el bloque no debería estar
   ahí, es desplazar el problema.
3. **¿Está en la capa correcta?** Un hallazgo de detalle que en realidad es un síntoma de
   jerarquía rota debe reportarse en la capa alta, no en la baja.
4. **¿Sobrevive a la restricción declarada?** Si el usuario dijo que la marca no se toca,
   proponer cambiar la paleta no es un hallazgo, es ignorar el contexto. Se reporta el costo
   de la restricción, no se propone violarla en silencio.

Menos hallazgos verdaderos valen más que treinta defendibles en abstracto. Borrar hallazgos
en esta pasada es señal de que la fase funcionó.

## Pasada 4 — Coherencia

- ¿Hay hallazgos que se contradicen entre sí? (pedir más densidad en un bloque y más aire en
  su equivalente).
- ¿Alguno contradice el contexto de la Fase 0? (proponer explicaciones extensas para un
  usuario que entra diez veces al día).
- ¿La severidad es coherente entre hallazgos comparables?
- ¿El veredicto final se sostiene con los hallazgos listados, o es más suave —o más duro— que
  su propia evidencia?

Resuelve las contradicciones antes de entregar. Que las descubra el lector cuesta más que
cualquier hallazgo omitido.

---

## Señales de que la auditoría mintió

Si reconoces alguna de estas en tu informe, no lo entregues todavía:

- Todos los hallazgos son de las capas 6 y 7 (color, espaciado, detalle) y ninguno de las
  capas 1 a 3.
- La sección "lo que funciona" es más larga que la de hallazgos.
- No hay ningún estado (vacío, error, carga) mencionado.
- No hay ninguna medición: ni un contraste, ni un tamaño, ni un conteo.
- El informe podría copiarse a otro sitio distinto cambiando dos nombres.
- No hay ni una pregunta incómoda: siempre hay al menos una decisión que no se explica sola.
- Todo el informe está en condicional.

---

## Registro

En el informe, la Fase 4 deja rastro visible: qué se degradó de `OK` a hallazgo, qué hallazgo
se retiró y por qué. Es lo que le permite al usuario confiar en los `OK` que quedaron — que
es, al final, lo único que una auditoría de UX tiene para ofrecer.
