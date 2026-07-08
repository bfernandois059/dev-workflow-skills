# Mantenimiento, poda de ramas y gotchas — MarcoZen

Detalle operativo para el **Modo 5 (mantenimiento)** y las cadencias mensual/trimestral/
anual, más las **lecciones aprendidas** que evitan romper cosas al ordenar.

## Cómo correr una revisión de mantenimiento

Solo lectura salvo que el usuario apruebe cambios. Reúne evidencia y reporta con severidad
P0–P3.

```bash
git fetch --prune origin
git branch -r --merged origin/main | grep -v HEAD      # ramas fusionadas (candidatas a cerrar)
git branch -r --no-merged origin/main | grep -v HEAD   # con trabajo sin integrar
npm audit --omit=dev          # vulnerabilidades (o pnpm audit)
npm outdated                  # dependencias atrasadas (o pnpm outdated)
npm run typecheck && npm run build && npm run test:run  # que siga verde
npm run lint                  # si existe
```

Revisa además: PRs antiguos abiertos, secretos, formularios, logs básicos, y estado de la
documentación crítica (README, runbook de deploy, security-checklist).

## Poda de ramas — procedimiento seguro (aprendido en uso real)

Ordenar ramas es de las tareas de mayor valor y mayor riesgo. **Nunca borres sin confirmar.**
Procedimiento por fases:

1. **`git fetch --prune`** antes de clasificar (referencias frescas).
2. **Clasifica en tres grupos** contra `main`:
   - **Fusionadas** (`git branch -r --merged origin/main`): candidatas seguras. Verifica
     además `git rev-list --count origin/main..origin/<rama>` (== 0) y diff vacío.
   - **No fusionadas** (`--no-merged`): revisión humana; pueden tener trabajo pendiente.
   - **Dudosas**: relacionadas con deploy/infra, o cuyo contenido ya está en `main` pero por
     re-implementación (no por ancestría). No borrar sin certeza.
3. **Cuidado con lo re-implementado:** una rama puede tener su funcionalidad ya en `main`
   (vía otra rama/PR posterior) sin estar fusionada por ancestría. Confírmalo mirando si los
   archivos/funciones clave existen en `main` antes de recomendar descartarla.
4. **Muestra la lista clasificada y pide confirmación** antes de borrar nada.
5. **Antes de borrar ramas no fusionadas**, muestra `git log` y `git diff --stat` vs `main`,
   y **captura los SHAs** (`git rev-parse origin/<rama>`) — son recuperables un tiempo vía
   reflog/API de GitHub si hiciera falta.
6. Borra solo lo confirmado: `git push origin --delete <rama>`, luego `git fetch --prune`.
7. **Preserva ramas de deploy/infra** (p. ej. Hostinger/Vercel config) hasta revisarlas
   aparte: pueden ser la única fuente del proceso de despliegue.

## Gotchas conocidos (para no romper el repo al ordenar)

- **Lockfile cross-platform (`@emnapi` / `sharp` / lightningcss / oxide):** en macOS/arm64
  `npm ci` puede pasar localmente pero **fallar en CI Linux** con "Missing `@emnapi/...` from
  lock file". Causa: el lock quedó incompleto para las deps nativas opcionales de otra
  plataforma. **Fix:** `rm -rf node_modules package-lock.json && npm install` (regenera el
  lock completo); verifica que `package.json` y sus dependencias **no cambien**. Reaparece si
  luego instalas algo con `npm i` — vuelve a regenerar. No edites el lock a mano.
- **No rompas enlaces históricos:** antes de **renombrar o consolidar documentos**, busca
  referencias (`grep -rn <nombre-archivo>`). Si un archivo está enlazado desde `CHANGELOG.md`
  u otro registro histórico, **no lo renombres** (reescribir historial es mala práctica):
  crea un **índice** que fije la convención en su lugar.
- **`ignoreBuildErrors` / `ignoreDuringBuilds`:** si `next.config` los tiene, el `build`
  **no** atrapa errores de tipo/lint. Asegúrate de que `typecheck` (y `lint`) corran aparte
  en el CI; no confíes solo en que el build pase.

## Cambios masivos: reporta antes de tocar

Si al introducir una herramienta (ESLint, typecheck estricto, formatter) aparecen **muchos**
hallazgos:

- **No los corrijas en masa** en la misma pasada. Reporta el desglose (por regla y archivo)
  y pide prioridad.
- **No metas la herramienta al gate del CI si dejaría el pipeline en rojo** con deuda
  heredada. Añádela al CI recién cuando esté en verde.
- **Documenta la deuda como issue** de seguimiento (título, desglose, bloques sugeridos de
  menor a mayor riesgo), no solo como texto en el reporte — así queda accionable.
- Corrige **por bloques** en PRs separados, de menor a mayor riesgo.

## Upgrades mayores (semestral/anual)

Planifícalos como tarea dedicada, uno a uno, con verificación entre cada uno: Next.js, React,
Node, Prisma/Supabase, Tailwind, CMS, y librerías de pago, email, auth y formularios/validación.
Nunca varios upgrades mayores en el mismo PR.
