# Mantenimiento, Poda de Ramas y Gotchas — MarcoZen

Detalle operativo para el **Modo 5 (mantenimiento)** y revisiones periódicas del repositorio.

---

## 1. Revisión de mantenimiento adaptada al stack

La revisión se realiza en **solo lectura** reuniendo evidencia concreta con los comandos reales del stack:

```bash
# Sincronización de referencias remotas
git fetch --prune origin

# Detección dinámica de la rama base real (sin asumir main, master ni develop):
BASE_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || git rev-parse --abbrev-ref HEAD)
# Si no puede determinarse con certeza, reportar como 'No verificado' o solicitar contexto al usuario.

# Inspección de ramas respecto de la base detectada:
git branch -r --merged "origin/$BASE_BRANCH" | grep -v HEAD      # ramas remotas ya fusionadas
git branch -r --no-merged "origin/$BASE_BRANCH" | grep -v HEAD   # ramas con trabajo sin integrar

# Dependencias (ejecutar la herramienta correspondiente al gestor detectado):
# Node (npm/pnpm/yarn/bun):
npm audit --omit=dev 2>/dev/null || pnpm audit --prod
npm outdated || pnpm outdated

# Python (pip/poetry/uv):
pip list --outdated
pip-audit 2>/dev/null

# Verificación de pipeline (solo los comandos existentes en el proyecto):
# npm test / pytest / go test / cargo test / npm run build
```

> **Regla sobre herramientas no disponibles:** Si un comando de auditoría de dependencias no puede ejecutarse por falta de conexión de red o ausencia del CLI en el entorno, **reporta el estado como `No verificado`**. Nunca asumas fallos ni inventes vulnerabilidades.

---

## 2. Poda de ramas — Procedimiento seguro

El orden de ramas aporta gran valor pero conlleva riesgo de pérdida de historial. **Nunca borres una rama remota sin confirmación explícita del usuario.**

> [!IMPORTANT]
> **Frontera de autorización ("audita y corrige"):**  
> Una instrucción previa como *"audita y corrige los problemas seguros que encuentres"* autoriza iniciar la fase de remediación para cambios no destructivos y claramente reversibles (documentación, README, `.env.example`, basura local o archivos temporales). **No constituye autorización implícita para borrar ramas remotas específicas.** La eliminación de ramas remotas es una acción destructiva sobre el historial del repositorio: siempre se debe actualizar referencias (`git fetch --prune`), clasificar cada rama, verificar integración, mostrar el inventario exacto propuesto para eliminación, capturar SHAs y obtener confirmación explícita del usuario sobre esas ramas antes de eliminarlas.

Procedimiento seguro para eliminación de ramas:
1. **`git fetch --prune origin`** para trabajar con el estado remoto actualizado.
2. **Clasificar ramas respecto de la rama base detectada:**
   - **Fusionadas:** Ya integradas en la rama base detectada (diff vacío). Son candidatas a poda.
   - **No fusionadas:** Contienen commits no presentes en la base; requieren revisión humana.
   - **Ramas de infraestructura o despliegue (ej. `production`, `staging`, ramas vinculadas a hosting o webhooks):** Tratarlas como sensibles y dudosas. Preservar mientras exista incertidumbre o dependencia operacional; eliminar solo cuando la obsolescencia esté demostrada con evidencia (ya no participa en ningún despliegue, no está vinculada a hosting/webhooks/procesos externos, su contenido fue integrado o quedó obsoleto, y no contiene configuración única necesaria para recuperación).
3. **Presentar inventario clasificado y solicitar confirmación explícita** para las ramas específicas antes de ejecutar cualquier comando de eliminación.
4. **Capturar SHAs antes de podar:** Registrar `git rev-parse origin/<rama>` para permitir recuperación ante cualquier eventualidad.
5. **Borrado autorizado:** `git push origin --delete <rama>` seguido de `git fetch --prune`.

---

## 3. Gotchas conocidos en mantenimiento

- **Lockfiles cross-platform:** Si un lockfile falla en CI con dependencias nativas faltantes (`@emnapi`, `sharp`, `esbuild`), regenerar el lockfile completo sin alterar versiones de producción en `package.json`.
- **Preservar enlaces históricos:** Antes de renombrar o mover un archivo de documentación, verifica referencias en commits o en `CHANGELOG.md` para evitar romper hipervínculos documentales.
- **Herramientas de linting/formatting:** Si al introducir o actualizar una regla de linter aparecen cientos de advertencias, **no las corrijas masivamente en un solo commit**. Reporta el inventario y planifica una intervención atómica mediante `engineering-workflow`.
