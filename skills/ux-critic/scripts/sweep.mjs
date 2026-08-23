#!/usr/bin/env node
/*
 * sweep.mjs — corre el inventario objetivo sobre muchas rutas y guarda un JSON por ruta.
 *
 * Parte de la skill `ux-critic` (modo sitio). Sirve para el barrido previo al muestreo:
 * antes de criticar pantallas una por una, se mide todo el sitio y se deja que los datos
 * digan qué rutas se salen del sistema.
 *
 * Requiere Playwright resuelto desde el proyecto auditado (no desde la skill):
 *
 *   npm i -D playwright && npx playwright install chromium
 *   node <skill>/scripts/sweep.mjs --base http://localhost:3000 --routes rutas.txt --out .ux-sweep
 *
 * Rutas autenticadas: crea el estado de sesión una vez y pásalo con --storage
 *
 *   npx playwright open --save-storage=.ux-sweep/state.json http://localhost:3000
 *   node <skill>/scripts/sweep.mjs ... --storage .ux-sweep/state.json
 *
 * Solo lectura: navega y mide. No envía formularios ni pulsa acciones.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const HERE = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const out = { routes: [], viewport: '1280x800', wait: 600, out: '.ux-sweep', shots: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    const next = () => argv[++i];
    if (a === '--base') out.base = next();
    else if (a === '--routes') out.routesFile = next();
    else if (a === '--route') out.routes.push(next());
    else if (a === '--out') out.out = next();
    else if (a === '--viewport') out.viewport = next();
    else if (a === '--storage') out.storage = next();
    else if (a === '--wait') out.wait = parseInt(next(), 10);
    else if (a === '--shots') out.shots = true;
    else if (a === '--help' || a === '-h') out.help = true;
    else throw new Error(`Opción desconocida: ${a}`);
  }
  return out;
}

const USAGE = `
Uso: node sweep.mjs --base <url> (--routes <archivo> | --route <ruta> ...) [opciones]

  --base <url>          Origen del sitio, ej. http://localhost:3000
  --routes <archivo>    Archivo con una ruta por línea (# comenta, líneas vacías se ignoran)
  --route <ruta>        Ruta suelta; se puede repetir
  --out <dir>           Directorio de salida (por defecto .ux-sweep)
  --viewport <WxH>      Viewport, por defecto 1280x800. Para móvil: 375x812
  --storage <archivo>   storageState de Playwright para rutas autenticadas
  --wait <ms>           Espera extra tras cargar, por defecto 600
  --shots               Guarda además una captura de página completa por ruta
`;

function loadRoutes(opts) {
  const list = [...opts.routes];
  if (opts.routesFile) {
    const raw = fs.readFileSync(opts.routesFile, 'utf8');
    for (const line of raw.split('\n')) {
      const r = line.split('#')[0].trim();
      if (r) list.push(r);
    }
  }
  return [...new Set(list)];
}

const slug = (route) =>
  (route.replace(/^\//, '').replace(/[^a-zA-Z0-9._-]+/g, '_') || 'root').slice(0, 80);

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.help || !opts.base) {
    console.log(USAGE);
    process.exit(opts.help ? 0 : 2);
  }

  const routes = loadRoutes(opts);
  if (!routes.length) {
    console.error('Sin rutas. Usa --routes <archivo> o --route <ruta>.');
    process.exit(2);
  }

  let chromium;
  try {
    const requireFromCwd = createRequire(path.join(process.cwd(), 'package.json'));
    ({ chromium } = requireFromCwd('playwright'));
  } catch {
    console.error(
      'No se pudo resolver Playwright desde este directorio.\n' +
        'Ejecuta el script desde la raíz del proyecto auditado, tras:\n' +
        '  npm i -D playwright && npx playwright install chromium'
    );
    process.exit(2);
  }

  const source = fs.readFileSync(path.join(HERE, 'ui_inventory.js'), 'utf8');
  const expression = `(function(){ return ${source.replace(/;\s*$/, '')}; })()`;

  const [width, height] = opts.viewport.split('x').map(Number);
  fs.mkdirSync(opts.out, { recursive: true });

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width, height },
    ...(opts.storage ? { storageState: opts.storage } : {}),
  });

  const index = { base: opts.base, viewport: opts.viewport, generatedAt: new Date().toISOString(), routes: [] };

  for (const route of routes) {
    const url = new URL(route, opts.base).toString();
    const page = await context.newPage();
    const entry = { route, url, file: null, error: null };
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 }).catch(() =>
        page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 })
      );
      if (opts.wait) await page.waitForTimeout(opts.wait);
      const inventory = await page.evaluate(expression);
      const file = `${slug(route)}.json`;
      fs.writeFileSync(
        path.join(opts.out, file),
        JSON.stringify({ route, url, viewport: opts.viewport, inventory }, null, 2)
      );
      entry.file = file;
      if (opts.shots) {
        await page.screenshot({ path: path.join(opts.out, `${slug(route)}.png`), fullPage: true });
      }
      console.log(
        `✓ ${route}  ` +
          `tipos:${inventory.typography.distinctSizes} ` +
          `contraste:${inventory.contrast.failures} ` +
          `toque:${inventory.tapTargets.belowMinimum} ` +
          `anidamiento:${inventory.surfaces.maxDepth}`
      );
    } catch (err) {
      entry.error = String(err && err.message ? err.message : err);
      console.error(`✗ ${route}  ${entry.error}`);
    } finally {
      index.routes.push(entry);
      await page.close();
    }
  }

  fs.writeFileSync(path.join(opts.out, '_index.json'), JSON.stringify(index, null, 2));
  await context.close();
  await browser.close();

  const ok = index.routes.filter((r) => r.file).length;
  console.log(`\n${ok}/${routes.length} rutas medidas en ${opts.out}`);
  console.log(`Siguiente: python3 ${path.relative(process.cwd(), path.join(HERE, 'compare_inventories.py'))} ${opts.out}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
