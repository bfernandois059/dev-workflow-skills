# Modo multiagente — auditorías profundas

Cuando el triage de la Fase 0 indique que el repo es lo bastante grande, activo o con
capas suficientes (rutas, componentes, assets, dependencias, tests/docs), correr la
auditoría con varios agentes especializados **en paralelo** da un resultado más profundo que
un solo agente repartiendo su atención entre todas las categorías. Cada agente se enfoca
solo en la suya.

**Costo:** este modo consume notablemente más tokens que el modo de un solo agente. Actívalo
quirúrgicamente — cuando el triage lo justifique — no por defecto. En proyectos chicos o con
triage mayormente 🟢, el modo de un solo agente (mismo rigor de evidencia, en secuencia) es
suficiente.

Todos los agentes comparten las mismas reglas: solo lectura, evidencia obligatoria antes de
clasificar, nunca asumir que "sin import directo" es "sin uso". Cada uno entrega su porción
de la tabla maestra (ver formato en `SKILL.md`), no un informe aparte.

---

## Agente 1 — Arquitectura y rutas

Revisa: estructura de rutas del framework (App/Pages Router, Remix, file-based routing u
otro equivalente), layouts, route handlers, imports, componentes compartidos, módulos
duplicados, código abandonado de fases o rediseños anteriores.

Debe detectar archivos sin referencias y rutas que ya no tienen uso real — pero primero
confirmar que no son archivos especiales que el router resuelve por convención de nombre o
ubicación, no por import explícito.

## Agente 2 — Componentes y estilos

Revisa: componentes de UI, hooks, helpers, utilidades, clases CSS, tokens de diseño, estilos
globales, variantes duplicadas, componentes antiguos sustituidos por versiones nuevas.

Debe distinguir entre código realmente muerto y código reutilizable pendiente de uso (por
ejemplo, un componente recién creado para una feature en curso, aunque todavía no tenga
muchas referencias).

## Agente 3 — Assets

Revisa toda carpeta estática del proyecto (`public/`, `static/`, `assets/` o equivalente).

Detecta: imágenes/media sin referencias, duplicados visuales, variantes antiguas, archivos
demasiado pesados, formatos innecesarios, logos repetidos, archivos temporales o capturas de
QA versionadas, assets usados solo en documentación, archivos que podrían estar referenciados
dinámicamente.

**No marca como seguro de borrar un asset solo porque no aparezca en una búsqueda simple.**
Revisa referencias directas, dinámicas (template strings, IDs de CMS), metadata, Open Graph,
plantillas de email, JSON-LD, CSS y scripts antes de clasificar.

## Agente 4 — Dependencias, scripts y configuración

Revisa: manifest de dependencias (`package.json` o equivalente), lockfile, dependencias y
devDependencies, scripts, aliases, configuración de tipado/linting, configuración del
framework, configuración de despliegue, variables de entorno, configuraciones duplicadas.

Debe identificar dependencias sin import directo, pero validar también uso indirecto en
scripts, build, tooling y configuración de despliegue antes de proponer eliminarlas — una
dependencia sin import en código puede seguir siendo un plugin de build o un peer
dependency requerido.

## Agente 5 — Tests, documentación y QA

Revisa: tests, snapshots, documentación, reportes de auditoría previos, carpetas de QA,
capturas, archivos históricos, documentos que ya no reflejan el estado actual del proyecto.

Debe separar: documentación operativa vigente; documentación histórica con valor de
trazabilidad (Categoría E, archivar); archivos duplicados; material seguro de eliminar
(Categoría A, solo si no tiene ningún valor de trazabilidad).

## Agente 6 — Revisor crítico final

No genera hallazgos nuevos. Revisa y cuestiona los de los agentes 1–5:

- detecta falsos positivos;
- busca dependencias ocultas y referencias que los otros agentes no vieron;
- revisa imports dinámicos y uso por convención del framework;
- revisa referencias desde despliegue, SEO, metadata, emails y scripts de build;
- marca cualquier eliminación propuesta que pueda romper producción, y la baja de categoría
  (de A a B, o de B a C) si la evidencia no es concluyente;
- exige evidencia concreta antes de confirmar cualquier hallazgo como Categoría A.

Ningún hallazgo llega a la tabla maestra final sin pasar por este agente. Es el que protege
al usuario de que un falso positivo se ejecute como si fuera seguro.

---

## Cómo lanzarlos

Lanza los agentes 1–5 en paralelo (una sola tanda de llamadas, sin dependencias entre
ellos). El agente 6 corre después, sobre los resultados consolidados de los cinco — depende
de que existan para poder cuestionarlos, así que va en una segunda tanda, no junto a los
demás.

Cada agente recibe: la ruta del repo/proyecto, el stack detectado en el triage, las reglas
de solo lectura y no exponer secretos, y el recordatorio explícito de que debe adjuntar
evidencia (comando o referencia concreta) a cada hallazgo, no solo una afirmación.

Asigna el modelo por rol al lanzarlos, no uno solo para todos: los agentes 1–5 corren en
perfil MEDIO (clasifican con criterios explícitos y verificables) y el agente 6 en perfil
ALTO (su trabajo es sospechar de conclusiones que se ven bien fundamentadas). Perfiles y
nombres de modelo vigentes en `engineering-workflow/references/engine-routing.md`.
