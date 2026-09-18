# Limpieza en lotes coherentes y reversibles — detalle operativo

La ejecución de cambios de limpieza sigue la disciplina de `engineering-workflow`: branches dedicadas, commits trazables con Conventional Commits, validaciones pertinentes antes de dar por terminado el trabajo y nunca operar directamente sobre la rama principal (`main`).

Principio rector:
> **Coherent and reversible batches > fixed cleanup stages.**

Se descartan las etapas fijas secuenciales obligatorias (1 a 5) y la imposición de múltiples Pull Requests fragmentados artificialmente. La eliminación se estructura en **lotes coherentes, autónomos y fácilmente reversibles**.

---

## 1. Criterios para estructurar un lote coherente

Agrupar las eliminaciones y modificaciones según su relación técnica y riesgo real, no por una división artificial:

1. **Unidad Funcional**:
   Elementos que pertenecen a un mismo subsistema o funcionalidad abandonada (ej. un módulo de integración descontinuado con sus rutas, componentes y helpers).
2. **Unidad Interdependiente**:
   Elementos vinculados directamente entre sí que carecen de sentido por separado (ej. una dependencia externa en desuso eliminada junto a su archivo de configuración y su script asociado en `package.json`).
3. **Naturaleza del Recurso**:
   Recursos homogéneos de bajo riesgo (ej. un conjunto de 20 imágenes estáticas huérfanas confirmadas) pueden eliminarse conjuntamente en un único lote seguro.
4. **Aislamiento de Riesgo**:
   No mezclar en un mismo lote recursos de bajo impacto (assets estáticos) con modificaciones sensibles (eliminación de dependencias de build, reestructuración de rutas o refactors de código).

---

## 2. Ejecución según el modo de operación

### En modo `AUDIT + EXECUTE SAFE`
Cuando el usuario solicita explícitamente *"limpia el proyecto"*, *"elimina lo que no se usa"* o *"audita y elimina lo seguro"*:
- La instrucción ya constituye la autorización para diagnosticar y ejecutar directamente los lotes de **Categoría A (seguro de borrar)** dentro del alcance indicado.
- **No se formula una segunda pregunta genérica de confirmación** para proceder con Categoría A.
- Se ejecutan las eliminaciones seguras, se corren las comprobaciones pertinentes del proyecto y se informa el resultado.

### Límites estrictos de ejecución segura
Aun en modo `AUDIT + EXECUTE SAFE`, **NO se ejecutan automáticamente**:
- **Categoría B**: requiere la validación específica previa indicada en la auditoría (preview visual en UI, test puntual, compilación específica).
- **Categoría C**: requiere migrar primero los consumidores activos antes de borrar el elemento.
- **Secretos y credenciales**: nunca se tocan ni se eliminan en una sesión de limpieza técnica; se reportan como hallazgo de seguridad independiente.
- **Refactors de diseño o arquitectura**: fuera del alcance de tech-cleanup.

---

## 3. Protocolo operativo por categoría

### Lotes de Categoría A (Seguro de borrar)
- Se eliminan los archivos huérfanos o dependencias confirmadas sin uso.
- Se ejecutan las validaciones del proyecto (build, tests pertinentes, lint).
- Si alguna validación falla, se revierte de inmediato el cambio puntual causante, se reclasifica el elemento (a B o C) y se reporta en el resumen.

### Lotes de Categoría B (Borrable con validación)
- Antes de eliminar, se ejecuta la comprobación estipulada en el informe (inspección de bundle, test específico, confirmación de configuración).
- Para componentes de UI o assets con impacto visual en pantalla, **se requiere comprobación visual en preview local o entorno de pruebas** antes de confirmar el borrado.
- Si la validación deja dudas o no es concluyente, el elemento no se elimina; se reclasifica a C o se mantiene (D).

### Lotes de Categoría C (Requiere refactor previo)
- Se aborda en dos fases trazables:
  1. Migración o actualización de los consumidores que aún dependen del elemento.
  2. Eliminación del elemento original una vez desacoplado.
- Nunca se elimina el elemento en el mismo paso en que sus consumidores siguen apuntando a él.

### Lotes de Categoría E (Archivar material histórico)
- No se elimina: se traslada a una carpeta de histórico (ej. `docs/_archive/`) o se marca formalmente como archivado, preservando su valor de trazabilidad.
- Solo se procede a borrado destructivo si el usuario lo ordena de forma explícita e inequívoca.

---

## 4. Checklist de seguridad y rollback

Antes de dar por concluido un lote de limpieza, verifica que se cumpla cada uno de los siguientes puntos:

- [ ] **Independencia y atomicidad**: el lote es autónomo y puede revertirse mediante `git revert <commit>` sin dejar el repositorio en estado inconsistente.
- [ ] **Validación stack-aware**: las herramientas pertinentes disponibles en el proyecto (build, pruebas automatizadas, linting o typecheck) pasaron exitosamente sobre el estado resultante.
- [ ] **Verificación visual**: los componentes de UI o assets eliminados fueron verificados visualmente en preview para asegurar que no existan huecos visuales ni imágenes rotas.
- [ ] **Secretos intactos**: no se modificaron credenciales, archivos `.env` reales ni tokens de acceso.
- [ ] **Registro de cambios**: se documenta con claridad qué elementos se eliminaron o archivaron y la evidencia que sustentó la decisión.
