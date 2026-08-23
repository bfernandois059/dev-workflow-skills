# Report Format

Fase 5 de `ux-critic`. Estructura fija del informe, formato de ficha y reglas de redacción.

El informe se entrega en la conversación. Guárdalo además como archivo
(`docs/ux-audit/<fecha>-<alcance>.md`) solo si el usuario lo pide o si la auditoría es de un
sitio completo.

---

## Estructura

```markdown
# Crítica de interfaz — <alcance>

**Contexto usado**
Producto: … · Usuario: … · Tarea: … · Etapa: … · Exigencia: nivel N
Capturas: <viewports y estados revisados>
Alcance real: <qué se auditó y qué quedó fuera>

## Veredicto
<Una frase. Honesta. Sin colchón.>

## Nivel por capa

| Capa | Nivel | En una línea |
|---|---|---|
| 1 · Propósito y promesa | Roto / Mediocre / Sólido / Referencia | … |
| 2 · Jerarquía | … | … |
| 3 · Ritmo y flujo | … | … |
| 4 · Contenido y copy | … | … |
| 5 · Interacción y estados | … | … |
| 6 · Sistema visual | … | … |
| 7 · Oficio y detalle | … | … |
| Accesibilidad (transversal) | … | … |
| Responsive (transversal) | … | … |

**Global:** <nivel> — <por qué ese y no el siguiente>

## Lo que sí funciona
<Máximo cinco. Cada uno con evidencia. Si hay menos de cinco reales, hay menos.>

## Hallazgos
<Fichas ordenadas por severidad: P0 → P3.>

## Preguntas incómodas
<3 a 5. Observación → hipótesis → qué cambia la respuesta.>

## Lo que replantearía de cero
<Obligatorio en pre-producción. 1 a 3 movimientos estructurales, como alternativa real.>

## Orden de ataque
<Secuencia numerada. Estructura antes que detalle.>

## Lo que no pude verificar
<Lista explícita. Y qué haría falta para verificarlo.>

## Refutación
<Qué se degradó de OK a hallazgo, qué hallazgo se retiró y por qué.>

## Plan de corrección
<Tareas autocontenidas, agrupadas en olas. Ver plantilla.>
```

---

## Ficha de hallazgo

```
### [P1 · Jerarquía · Rediseño de bloque · Esfuerzo medio] Título del hallazgo en una línea

**Qué se ve** — evidencia observada, con valores medidos o referencia a la captura.
**Por qué falla** — para este usuario, en esta tarea. No en abstracto.
**Qué cuesta** — confusión / paso extra / error / abandono / desconfianza.
**Corrección** — concreta, con valores o texto propuesto.
**Certeza** — Hecho observado | Juicio del crítico | Supuesto por confirmar
```

La línea de encabezado lleva siempre los cuatro campos en ese orden:
`severidad · capa · nivel de intervención · esfuerzo`.

**En hallazgos de estructura y superficie** —los del catálogo
[`container-antipatterns.md`](container-antipatterns.md)— la corrección **debe incluir el
árbol antes/después**. Sin el árbol, "simplificar la jerarquía de contenedores" vuelve a ser
una recomendación tibia; el árbol es la instrucción:

```
❌ Antes                                  ✅ Después
Panel "Documentos técnicos"               "Obligatorios" (título de sección, sin caja)
  Tarjeta "Documentos … obligatorios"       Kick Off y OT antes de finalizar.
    Tabla                                   ── una superficie, dos filas ──
      Fila con fondo propio ×2
  Pie "Documentación lista para finalizar"  (estado, una sola vez, junto a Finalizar)
```

### Ejemplo correcto

```
### [P1 · Jerarquía · Ajuste · Esfuerzo bajo] El precio pierde contra el badge de descuento

**Qué se ve** — En la tarjeta de producto, el badge "-30%" está en 20 px / peso 700 sobre
rojo, y el precio final en 16 px / peso 400 en gris #767676. Captura: 375-catalogo.png.
**Por qué falla** — La tarea es comparar productos y decidir. El dato que decide es el precio
final; el que domina la tarjeta es el descuento, que solo tiene sentido después de haber
leído el precio.
**Qué cuesta** — El usuario compara descuentos en vez de precios y vuelve atrás al descubrir
el precio real en la ficha. Paso extra y desconfianza.
**Corrección** — Precio final a 20 px / peso 600 en el color de texto principal; badge a
12 px / peso 600 y contenido dentro del flujo de la tarjeta, no encima de la imagen.
**Certeza** — Hecho observado (valores medidos).
```

### Ejemplo incorrecto

```
Se recomienda revisar la jerarquía visual de las tarjetas de producto, ya que actualmente
podría no ser del todo clara para el usuario. Considerar destacar mejor el precio.
```

Sin evidencia, sin costo, sin valores, sin certeza, y en condicional. No es un hallazgo: es
una sensación con formato de informe.

---

## Niveles

**Por capa y global:**

| Nivel | Qué significa |
|---|---|
| **Roto** | No cumple su función. Un usuario real falla, se confunde o se va |
| **Funciona pero mediocre** | Cumple, se nota que nadie decidió. Se sostiene por inercia |
| **Sólido** | Decidido, consistente, sin fricciones relevantes. No sorprende |
| **Referencia** | Se puede mostrar como ejemplo. Cada decisión tiene intención |

Sin puntajes numéricos. Un "72/100" en una crítica de interfaz es precisión falsa: sugiere
una medición que no existe.

---

## Reglas de redacción

- **Duro con el trabajo, respetuoso con la persona.** Nunca "quien hizo esto no pensó";
  siempre "esta decisión cuesta X".
- **Toda crítica trae propuesta.** Sin propuesta es opinión.
- **Específico o no se dice.** Valores, textos, selectores, capturas.
- **Nada de lenguaje de colchón**: *podría considerarse*, *tal vez sería recomendable*, *en
  general está bien pero*, *no está mal del todo*, *se sugiere evaluar*.
- **Nada de sándwich de elogios.** Lo bueno tiene su sección.
- **Nada de jerga vacía**: *sinergia visual*, *storytelling de marca*, *experiencia
  inmersiva*.
- **Nada de números inventados.** Ni conversión, ni segundos, ni porcentajes de mejora.
- **Separa hecho de juicio** con la línea de certeza. El usuario puede discutir los juicios;
  los hechos no se discuten, se corrigen.
- **El veredicto va primero.** Nadie debería tener que leer treinta hallazgos para saber si
  la pantalla está bien o mal.

---

## Plan de corrección

Última sección del informe y **entregable en sí mismo**: la lista de tareas con la que se
arregla lo encontrado, sin tener que releer el informe. Plantilla completa en
[`../assets/templates/fix-plan.template.md`](../assets/templates/fix-plan.template.md).

Reglas:

1. **Una tarea es autocontenida.** Se puede tomar suelta, pasar a `engineering-workflow` o
   entregar a otro agente sin el resto del informe. Lleva problema, dónde, qué cambia,
   estructura objetivo, criterio de aceptación y fuera de alcance.
2. **Criterio de aceptación verificable.** "Ninguna superficie anidada a más de dos niveles en
   la pestaña" sí; "mejorar la jerarquía" no. Debe poder marcarse hecho o no hecho mirando la
   pantalla.
3. **Agrupadas en olas, no en una lista plana**: estructura → jerarquía y acciones →
   contenido y estados → detalle. No se empieza una ola sin cerrar la anterior, porque pulir
   antes de reestructurar es trabajo que se tira.
4. **Un anti-patrón repetido es una sola tarea de sistema**, con la lista de pantallas donde
   se verifica. Seis tareas de pantalla para el mismo problema es la forma de garantizar que
   quede a medias.
5. **Riesgo declarado.** Marca qué tareas son solo presentación y cuáles tocan comportamiento
   o datos: define si pueden ir por la ruta rápida de `engineering-workflow` o exigen el flujo
   completo.
6. **Lo que no es tarea, es decisión.** Lo que requiere una definición de producto o negocio
   va en una tabla aparte de decisiones pendientes, indicando qué tarea bloquea. No se
   disfraza de tarea.
7. **Verificación final incluida**: repetir el inventario objetivo y el recorrido limpio sobre
   la interfaz corregida, y comparar capturas antes/después.

---

## Longitud

Proporcional al alcance, no al esfuerzo invertido:

| Alcance | Extensión razonable |
|---|---|
| Bloque | Veredicto + 3 a 6 hallazgos |
| Pantalla | Informe completo, 8 a 15 hallazgos |
| Flujo | Informe completo + mapa del recorrido paso a paso |
| Sitio | Informe por pantalla clave + una sección de patrones transversales que se repiten |

En un sitio completo, el hallazgo transversal vale más que el mismo hallazgo repetido en seis
pantallas: repórtalo una vez, lista dónde aparece.
