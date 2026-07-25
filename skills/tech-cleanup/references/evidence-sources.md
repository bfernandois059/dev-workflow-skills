# Fuentes de evidencia — detalle operativo

Comandos de solo lectura, agrupados por categoría. Adapta el gestor de paquetes, el
framework y las extensiones de archivo al stack real detectado en la Fase 0. Ninguno de
estos comandos modifica el repositorio.

---

## Rutas y arquitectura

```bash
# imports estáticos de un archivo/símbolo en todo el repo (no solo src/)
grep -rInE "from ['\"].*NOMBRE|require\(['\"].*NOMBRE|import\(['\"].*NOMBRE" .

# imports dinámicos (lazy, code-splitting)
grep -rInE "import\(|React\.lazy|dynamic\(" --include=*.{js,jsx,ts,tsx} .

# archivos que el router resuelve por convención (Next.js App/Pages Router,
# Remix, file-based routing) — no aparecen como import explícito
find . -path '*/app/*' -o -path '*/pages/*' -o -path '*/routes/*' | grep -v node_modules

# route handlers / API routes
find . -iname 'route.ts' -o -iname 'route.js' -o -path '*/api/*' | grep -v node_modules
```

Antes de marcar un archivo de ruta como sin uso, confirma que no es un archivo especial del
framework (`layout`, `loading`, `error`, `not-found`, middleware, archivos de configuración
por convención) que el router usa sin que aparezca ningún import.

---

## Componentes, hooks, estilos

```bash
# referencias a un componente/hook por nombre en todo el repo
grep -rInE "\bNOMBRE\b" --include=*.{js,jsx,ts,tsx} .

# clases CSS o tokens usados dinámicamente (template strings, clsx, cva)
grep -rInE "clsx\(|cva\(|classnames\(|className=\{" --include=*.{js,jsx,ts,tsx} .

# uso de una clase/token específico
grep -rInE "NOMBRE-CLASE" --include=*.{css,scss,js,jsx,ts,tsx} .
```

Distingue entre código realmente muerto y código reutilizable pendiente de uso (por ejemplo,
un componente recién creado para una feature en curso). Revisa el historial reciente de
commits antes de asumir abandono.

---

## Imágenes y assets

No marques como seguro de borrar un asset solo porque no aparezca en una búsqueda de texto
simple. Revisa referencias directas, dinámicas y externas al código:

```bash
# referencia directa por nombre de archivo
grep -rInE "NOMBRE-ARCHIVO" .

# uso en metadata / Open Graph / JSON-LD / sitemap
grep -rInE "og:image|twitter:image|NOMBRE-ARCHIVO" --include=*.{ts,tsx,js,jsx,json,xml} .

# uso en plantillas de email
grep -rInE "NOMBRE-ARCHIVO" --include=*.{html,mjml,tsx} .

# referencias dinámicas construidas por template string (ej: `/images/${slug}.jpg`)
grep -rInE '\`.*images.*\$\{' --include=*.{js,jsx,ts,tsx} .

# duplicados visuales / mismo contenido con distinto nombre
find public -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.webp' \) -exec md5sum {} \; | sort | uniq -w32 -d

# assets pesados (candidatos a optimizar, no necesariamente a borrar)
find public -type f -size +500k -exec du -h {} \; 2>/dev/null | sort -rh
```

Revisa también `public/` completo contra: CMS/contenido dinámico que referencia assets por
ID o slug, capturas de QA que quedaron versionadas, logos duplicados en distintos formatos
usados por distintos consumidores (favicon vs. Open Graph vs. app icon).

---

## Dependencias, scripts y configuración

```bash
# dependencias sin import directo (revisar salida manualmente, no borrar automático)
npx depcheck 2>/dev/null || true

# uso de una dependencia en scripts/build/CI, no solo en código
grep -rInE "NOMBRE-PAQUETE" package.json *.config.* .github/ vercel.json netlify.toml 2>/dev/null

# scripts npm invocados desde CI o desde otros scripts
grep -rInE "npm run|pnpm run|yarn " .github/ package.json 2>/dev/null

# variables de entorno declaradas vs. usadas
grep -oE '^[A-Z_]+=' .env.example 2>/dev/null | sed 's/=//' | while read v; do
  grep -rq "$v" --include=*.{js,ts,jsx,tsx} . || echo "sin uso aparente: $v"
done
```

Una dependencia sin import directo puede seguir siendo necesaria como peer dependency,
plugin de build, o requisito de otra herramienta (ESLint config, Tailwind plugin, adapter de
despliegue). Verifica antes de clasificarla en Categoría A.

---

## Tests, documentación y QA

```bash
# tests que referencian archivos/componentes que ya no existen
grep -rlnE "import .* from ['\"]\./NOMBRE" --include=*.test.* --include=*.spec.* .

# snapshots huérfanos
find . -path '*__snapshots__*' | grep -v node_modules

# documentación con fecha vieja o que contradice el estado actual del código
grep -rlnE "TODO|DEPRECATED|desactualizado" docs/ 2>/dev/null
```

Separa documentación operativa vigente de material histórico (auditorías anteriores,
reportes de QA fechados): lo histórico es Categoría E (archivar), no Categoría A.

---

## Build, bundle y validación transversal

Ejecuta sin corregir automáticamente lo que encuentres — solo diagnóstico:

```bash
npm ci
npm run lint
npm run typecheck
npm test -- --reporter=dot
npm run build
```

Si el proyecto tiene análisis de bundle disponible (`next build` con `ANALYZE=true`, `vite
build --report`, etc.), úsalo para confirmar qué realmente termina en el bundle final — es
la evidencia más fuerte de que algo participa en producción.
