# Fuentes de evidencia — detalle operativo

Comandos y métodos de inspección en **solo lectura**, agrupados por categoría. Adapta las herramientas, gestores de paquetes y extensiones al stack real detectado en el triage. Ninguno de estos comandos modifica el repositorio ni altera el working tree.

---

## Principio: Herramientas especializadas como evidencia, nunca como oráculo

Para proyectos JavaScript / TypeScript modernos, herramientas como **`Knip`** (o analizadores equivalentes ya configurados en el proyecto) aportan evidencia valiosa para detectar:
- archivos sin uso;
- exports sin uso;
- dependencias y devDependencies huérfanas;
- binarios no utilizados;
- scripts o archivos de configuración obsoletos.

Reglas indispensables:
1. **Preferir herramientas que el proyecto ya tenga configuradas** en sus scripts o dependencias de desarrollo.
2. **La salida de un analizador es evidencia analítica, jamás autorización automática de borrado.**
3. **Validar falsos positivos** confrontando los resultados contra convenciones de framework, plugins dinámicos y configuración de runtime.
4. **No agregar dependencias persistentes al proyecto** exclusivamente para correr la auditoría. Si se ejecuta mediante npx/dlx, verificar que no altere `package.json` ni el lockfile.
5. **Si la herramienta no está disponible o falla en el entorno**, continuar con las demás fuentes de evidencia y declarar esa comprobación como no realizada.
6. **`depcheck`** puede utilizarse como alternativa o fallback secundario, pero no debe presentarse como la referencia principal universal para JS/TS moderno.

```bash
# Ejecución no invasiva de analizadores si el entorno lo soporta (ejemplo JS/TS):
npx knip --no-exit-code 2>/dev/null || npx depcheck 2>/dev/null || true
```

---

## Rutas y arquitectura

```bash
# imports estáticos de un archivo/símbolo en todo el repo (no solo src/)
grep -rInE "from ['\"].*NOMBRE|require\(['\"].*NOMBRE|import\(['\"].*NOMBRE" .

# imports dinámicos y lazy loading
grep -rInE "import\(|React\.lazy|dynamic\(" --include=*.{js,jsx,ts,tsx} .

# archivos que el router resuelve por convención (App/Pages Router, Remix, Astro, etc.)
find . -path '*/app/*' -o -path '*/pages/*' -o -path '*/routes/*' | grep -v node_modules

# route handlers y API routes
find . -iname 'route.ts' -o -iname 'route.js' -o -path '*/api/*' | grep -v node_modules
```

**Protección de convenciones de framework (file-based routing)**:
Antes de marcar un archivo de ruta como sin uso, confirma si corresponde a un archivo especial que el router invoca por convención sin import explícito:
- `page`, `layout`, `template`, `loading`, `error`, `global-error`, `not-found`, `default`, `route`;
- `middleware`, proxy de rutas o `instrumentation`;
- `manifest`, `sitemap`, `robots`, `favicon`/`icon`, `opengraph-image`, `twitter-image`.

Estos archivos **no dependen de imports en el código** y son consumidos directamente por el framework.

---

## Componentes, hooks y estilos

```bash
# referencias a un componente/hook por nombre en todo el repo
grep -rInE "\bNOMBRE\b" --include=*.{js,jsx,ts,tsx,vue,svelte} .

# clases CSS o tokens usados dinámicamente (template strings, clsx, cva, classnames)
grep -rInE "clsx\(|cva\(|classnames\(|className=\{" --include=*.{js,jsx,ts,tsx} .

# uso de una clase o variable CSS específica
grep -rInE "NOMBRE-CLASE" --include=*.{css,scss,js,jsx,ts,tsx} .
```

*Distinción temporal*: Distingue entre código muerto real y componentes recientemente incorporados para features en curso. Revisa `git log -n 5 -- ruta/archivo` antes de asumir abandono.

---

## Imágenes y assets

Nunca marques como seguro de borrar un asset únicamente porque su nombre no aparezca en una búsqueda textual simple. Inspecciona referencias directas, dinámicas e indirectas:

```bash
# 1. Referencia directa por nombre de archivo
grep -rInE "NOMBRE-ARCHIVO" .

# 2. Uso en metadata, Open Graph, Twitter cards, JSON-LD o sitemaps
grep -rInE "og:image|twitter:image|NOMBRE-ARCHIVO" --include=*.{ts,tsx,js,jsx,json,xml,html} .

# 3. Uso en plantillas de email transaccional
grep -rInE "NOMBRE-ARCHIVO" --include=*.{html,mjml,tsx} .

# 4. Referencias dinámicas mediante template strings (ej: `/images/${slug}.webp` o `/assets/${id}.png`)
grep -rInE '\`.*images.*\$\{' --include=*.{js,jsx,ts,tsx} .

# 5. Duplicados visuales por hash MD5 (mismo contenido con distinto nombre)
find public -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.webp' \) -exec md5sum {} \; 2>/dev/null | sort | uniq -w32 -d

# 6. Assets de gran peso (candidatos a optimización, no necesariamente a eliminación)
find public -type f -size +500k -exec du -h {} \; 2>/dev/null | sort -rh
```

**Regla de assets dinámicos**:
Si en el proyecto existe un patrón como:
```javascript
const imageSrc = `/images/${slug}.webp`;
```
o una tabla de datos/CMS que referencia recursos por ID o slug, **los archivos correspondientes NO pueden clasificarse como Categoría A** por el solo hecho de no encontrarse su nombre literal en el código fuente. Se clasifican como Categoría B o D según la certeza de los identificadores activos.

---

## Dependencias, scripts y configuración

```bash
# uso de una dependencia en scripts, build, configs o CI (no solo en imports de código)
grep -rInE "NOMBRE-PAQUETE" package.json *.config.* .github/ vercel.json netlify.toml Dockerfile Makefile 2>/dev/null

# scripts de package manager invocados desde flujos de CI o tareas automatizadas
grep -rInE "npm run|pnpm run|yarn |bun " .github/ package.json Makefile 2>/dev/null

# variables de entorno declaradas en .env.example vs. usadas en código (solo nombres, nunca valores)
grep -oE '^[A-Z_]+=' .env.example 2>/dev/null | sed 's/=//' | while read v; do
  grep -rq "$v" --include=*.{js,ts,jsx,tsx,py,go,php} . || echo "sin uso aparente: $v"
done
```

**Uso indirecto de dependencias**:
Una dependencia sin import directo en código puede seguir siendo crítica como:
- peer dependency exigida por otra librería instalada;
- plugin de compilación o transpilación (PostCSS, Tailwind, Babel, Vite, Next plugins);
- preset o configuración de linter / formateador (ESLint plugins/configs, Prettier plugins);
- adapter de despliegue o runtime (Vercel, Netlify, Cloudflare);
- comando ejecutado exclusivamente en scripts de `package.json` o pipelines de CI/CD.

Verifica exhaustivamente estos casos antes de clasificar una dependencia como Categoría A.

---

## Tests, documentación y QA

```bash
# tests o mocks que referencian módulos eliminados
grep -rlnE "import .* from ['\"]\./NOMBRE" --include=*.test.* --include=*.spec.* .

# snapshots huérfanos o desactualizados
find . -path '*__snapshots__*' | grep -v node_modules

# documentación operativa desactualizada
grep -rlnE "TODO|DEPRECATED|desactualizado" docs/ 2>/dev/null
```

Separa la documentación técnica vigente del material histórico (informes de auditorías anteriores fechadas, minutas de QA, especificaciones de versiones pasadas). Lo histórico tiene valor de trazabilidad y corresponde a **Categoría E (archivar)**, no a eliminación destructiva.

---

## Validación transversal stack-aware

No ejecutar una suite universal rígida. Utilizar los comandos reales disponibles según el gestor y stack detectado en el proyecto:

```bash
# Node / TypeScript (ejecutar las herramientas configuradas en package.json):
# npm test / pnpm test / yarn test / bun test
# npm run build / pnpm build / yarn build / bun run build
# npm run lint / npm run typecheck (si existen en scripts)

# Python:
# pytest / python -m unittest
# mypy / ruff check / flake8

# Go:
# go test ./...
# go vet ./...
# go build ./...
```

Si el proyecto cuenta con análisis de bundle configurado (`next build` con `@next/bundle-analyzer`, `vite-bundle-visualizer`, etc.), utilízalo como evidencia fuerte para comprobar qué módulos terminan efectivamente en los chunks de producción.
