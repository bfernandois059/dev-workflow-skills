# Modo multiagente y revisión crítica — detalle operativo

El modo multiagente es una **optimización opcional** para auditorías en repositorios extensos, monorepos o proyectos con múltiples subsistemas desacoplados.

En repositorios pequeños o medianos, un único agente aplicando metódicamente las fuentes de evidencia es **100% válido, suficiente y preferido**.

---

## 1. Principios de operación

- **Opcional, no obligatorio**: se activa únicamente cuando la escala del proyecto y la independencia de sus áreas justifique la paralelización.
- **Sin bloqueos de routing ni hard gates de modelo**: la skill se adapta a las capacidades del entorno de ejecución. No se interrumpe la auditoría ni se exige autorización interactiva para alternar perfiles de modelo. Si una limitación técnica impide comprobar un aspecto, se declara transparentemente como no verificado.
- **Unidad de criterio**: todos los agentes operan en modo estrictamente de solo lectura, no generan archivos en el working tree sin solicitud expresa y aplican el principio *"Prove unused before deleting. Absence of a direct reference is evidence, not proof"*.

---

## 2. Dominios de especialización (cuando se divide el trabajo)

Si se opta por paralelizar la inspección entre agentes o tareas concurrentes, los dominios naturales son:

1. **Rutas y arquitectura**:
   - Inspecciona file-based routing, route handlers, layouts y componentes de página.
   - Protege los archivos especiales de convención del framework (`loading`, `error`, `not-found`, `middleware`, `sitemap`, etc.).
2. **Componentes y estilos**:
   - Componentes UI, hooks, utilidades compartidas, clases dinámicas y tokens CSS.
   - Distingue código abandonado de código recién creado para features en desarrollo.
3. **Assets y multimedia**:
   - Imágenes, iconos, fuentes y documentos en carpetas estáticas (`public/`, `assets/`).
   - Rastrea referencias dinámicas (template literals como `/images/${slug}.webp`), Open Graph, emails transaccionales y JSON-LD.
4. **Dependencias, scripts y configuración**:
   - Manifests de dependencias, scripts de package manager, linters, transpiladores, adapters de despliegue y workflows de CI/CD.
   - Emplea herramientas como `Knip` como evidencia complementaria, validando falsos positivos.
5. **Tests y documentación**:
   - Tests o mocks obsoletos y snapshots huérfanos.
   - Separa documentación activa de material histórico con valor de trazabilidad (Categoría E).

---

## 3. Disciplina de refutación (Revisión Crítica)

El rol de revisión crítica es **indispensable en toda auditoría de Tech Cleanup**, independientemente de si se ejecuta con un solo agente o mediante agentes concurrentes:

- **En modo multiagente**: puede asignarse a un subagente revisor que recibe la consolidación de candidatos y desafía activamente las propuestas de Categoría A antes de emitir el informe.
- **En modo de agente único**: el agente ejecuta una fase reflexiva obligatoria de refutación antes de presentar los hallazgos al usuario.

### Preguntas obligatorias de la revisión crítica:
1. *¿Existe alguna convención de framework que cargue este archivo sin un import explícito?*
2. *¿Se referencia este archivo o asset mediante variables, template strings, slugs o IDs de base de datos?*
3. *¿Es esta dependencia necesaria como peer dependency, plugin de build o herramienta en pipelines de CI/CD?*
4. *¿Podría este componente ser código nuevo en desarrollo en lugar de código muerto?*
5. *¿Existe evidencia concluyente de desuso en todo el ciclo de vida, o solo ausencia de resultados en una búsqueda simple?*

Si la respuesta a cualquiera de estas preguntas arroja dudas o incertidumbre no resuelta, el hallazgo se degrada de inmediato a Categoría B o C, o se mantiene (D).
