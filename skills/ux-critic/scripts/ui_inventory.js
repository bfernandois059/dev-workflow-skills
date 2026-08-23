/*
 * ui_inventory.js — inventario objetivo de una interfaz viva.
 *
 * Parte de la skill `ux-critic` (Fase 1 — Captura). Se ejecuta sobre la página ya
 * renderizada y devuelve HECHOS MEDIDOS, no juicios: escala tipográfica en uso, paleta
 * real, espaciados, contrastes bajo el umbral, tamaños de toque, esquema de encabezados,
 * ancho de línea y ritmo vertical.
 *
 * El inventario no dice qué está mal. Dice qué hay. El juicio es de la Fase 2.
 *
 * Cómo correrlo:
 *   - MCP de navegador: pasar el contenido de este archivo a la herramienta de ejecución
 *     de JavaScript de la página.
 *   - DevTools: pegar en la consola. Devuelve un objeto; `copy($_)` lo lleva al portapapeles.
 *   - Playwright/Puppeteer: page.evaluate(fs.readFileSync('ui_inventory.js', 'utf8'))
 *
 * Solo lectura: no modifica el DOM ni dispara eventos.
 */
(() => {
  const LIMIT = 25;              // tope de ítems por lista, para que el reporte sea legible
  const TAP_MIN = 44;            // px mínimos de objetivo táctil
  const LINE_MAX = 85;           // caracteres por línea antes de que cueste volver
  const LINE_MIN = 40;
  const CONTRAST_TEXT = 4.5;
  const CONTRAST_LARGE = 3.0;

  const vw = window.innerWidth;
  const vh = window.innerHeight;

  // ---------- utilidades ----------

  const clip = (arr, n = LIMIT) => arr.slice(0, n);

  const byCountDesc = (map) =>
    [...map.entries()].sort((a, b) => b[1] - a[1]).map(([value, count]) => ({ value, count }));

  const path = (el) => {
    const parts = [];
    let node = el;
    for (let i = 0; node && node.nodeType === 1 && i < 4; i++) {
      let part = node.tagName.toLowerCase();
      if (node.id) { parts.unshift(`${part}#${node.id}`); break; }
      const cls = (node.getAttribute('class') || '').trim().split(/\s+/).filter(Boolean)[0];
      if (cls) part += `.${cls}`;
      parts.unshift(part);
      node = node.parentElement;
    }
    return parts.join(' > ');
  };

  const textOf = (el, max = 60) => (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, max);

  const parseColor = (str) => {
    if (!str) return null;
    const m = str.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map((v) => parseFloat(v.trim()));
    if (p.length < 3 || p.some(Number.isNaN)) return null;
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };

  const over = (fg, bg) => ({
    r: fg.r * fg.a + bg.r * (1 - fg.a),
    g: fg.g * fg.a + bg.g * (1 - fg.a),
    b: fg.b * fg.a + bg.b * (1 - fg.a),
    a: 1,
  });

  const hex = (c) =>
    '#' + [c.r, c.g, c.b].map((v) => Math.round(v).toString(16).padStart(2, '0')).join('');

  const luminance = (c) => {
    const ch = [c.r, c.g, c.b].map((v) => {
      const s = v / 255;
      return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2];
  };

  const contrast = (a, b) => {
    const l1 = luminance(a);
    const l2 = luminance(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  };

  // fondo efectivo: sube por ancestros hasta encontrar uno opaco
  const effectiveBg = (el) => {
    let node = el;
    let acc = null;
    while (node && node.nodeType === 1) {
      const bg = parseColor(getComputedStyle(node).backgroundColor);
      if (bg && bg.a > 0) {
        acc = acc ? over(acc, bg) : bg;
        if (acc.a >= 0.99) return acc;
      }
      node = node.parentElement;
    }
    const white = { r: 255, g: 255, b: 255, a: 1 };
    return acc ? over(acc, white) : white;
  };

  const isVisible = (el, cs, rect) =>
    rect.width > 0 && rect.height > 0 &&
    cs.display !== 'none' && cs.visibility !== 'hidden' && parseFloat(cs.opacity || '1') > 0.05;

  const hasOwnText = (el) => {
    for (const n of el.childNodes) {
      if (n.nodeType === 3 && n.nodeValue.trim().length > 1) return true;
    }
    return false;
  };

  const accessibleName = (el) => {
    const aria = el.getAttribute('aria-label');
    if (aria && aria.trim()) return aria.trim();
    const labelledby = el.getAttribute('aria-labelledby');
    if (labelledby) {
      const ref = document.getElementById(labelledby.split(/\s+/)[0]);
      if (ref && textOf(ref)) return textOf(ref);
    }
    if (el.id) {
      const label = document.querySelector(`label[for="${CSS.escape(el.id)}"]`);
      if (label && textOf(label)) return textOf(label);
    }
    if (el.closest('label') && textOf(el.closest('label'))) return textOf(el.closest('label'));
    const title = el.getAttribute('title');
    if (title && title.trim()) return title.trim();
    const alt = el.querySelector && el.querySelector('img[alt]:not([alt=""])');
    if (alt) return alt.getAttribute('alt');
    if (el.tagName === 'INPUT' && el.value && el.type !== 'text') return el.value;
    return textOf(el);
  };

  // ---------- recolección ----------

  const sizes = new Map();
  const weights = new Map();
  const families = new Map();
  const lineHeights = new Map();
  const textColors = new Map();
  const bgColors = new Map();
  const borderColors = new Map();
  const spacing = new Map();
  const radii = new Map();
  const shadows = new Map();
  const zIndexes = new Map();

  const contrastFailures = [];
  const smallTaps = [];
  const unnamed = [];
  const longLines = [];
  const shortLines = [];
  const imagesNoAlt = [];
  const oversizedImages = [];

  const bump = (map, key) => { if (key) map.set(key, (map.get(key) || 0) + 1); };

  const all = document.querySelectorAll('body *:not(script):not(style):not(noscript)');

  for (const el of all) {
    const cs = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    if (!isVisible(el, cs, rect)) continue;

    // caja: espaciados, radios, sombras, z-index
    for (const prop of ['paddingTop', 'paddingBottom', 'paddingLeft', 'paddingRight',
                        'marginTop', 'marginBottom', 'rowGap', 'columnGap']) {
      const v = parseFloat(cs[prop]);
      if (v > 0) bump(spacing, `${Math.round(v)}px`);
    }
    if (cs.borderRadius && cs.borderRadius !== '0px') bump(radii, cs.borderRadius);
    if (cs.boxShadow && cs.boxShadow !== 'none') bump(shadows, cs.boxShadow.slice(0, 60));
    if (cs.zIndex && cs.zIndex !== 'auto') bump(zIndexes, cs.zIndex);

    const bg = parseColor(cs.backgroundColor);
    if (bg && bg.a > 0.05) bump(bgColors, hex(bg));
    if (parseFloat(cs.borderTopWidth) > 0) {
      const bc = parseColor(cs.borderTopColor);
      if (bc && bc.a > 0.05) bump(borderColors, hex(bc));
    }

    // tipografía y contraste: solo elementos con texto propio
    if (hasOwnText(el)) {
      const size = Math.round(parseFloat(cs.fontSize));
      const weight = cs.fontWeight;
      const family = (cs.fontFamily || '').split(',')[0].replace(/["']/g, '').trim();
      bump(sizes, `${size}px`);
      bump(weights, weight);
      bump(families, family);
      bump(lineHeights, cs.lineHeight);

      const fg0 = parseColor(cs.color);
      if (fg0) {
        const bgEff = effectiveBg(el);
        const fg = fg0.a < 1 ? over(fg0, bgEff) : fg0;
        bump(textColors, hex(fg));
        const ratio = contrast(fg, bgEff);
        const bold = parseInt(weight, 10) >= 700;
        const isLarge = size >= 24 || (bold && size >= 18.66);
        const min = isLarge ? CONTRAST_LARGE : CONTRAST_TEXT;
        if (ratio < min) {
          contrastFailures.push({
            path: path(el),
            text: textOf(el, 45),
            fg: hex(fg),
            bg: hex(bgEff),
            ratio: Math.round(ratio * 100) / 100,
            required: min,
            fontSize: `${size}px`,
          });
        }
      }

      // ancho de línea en bloques de texto corrido
      if (/^(P|LI|BLOCKQUOTE|DD)$/.test(el.tagName) && rect.width > 0) {
        const chars = Math.round(rect.width / (size * 0.5));
        const len = (el.textContent || '').trim().length;
        if (len > 120) {
          if (chars > LINE_MAX) longLines.push({ path: path(el), chars, width: Math.round(rect.width) });
          else if (chars < LINE_MIN) shortLines.push({ path: path(el), chars, width: Math.round(rect.width) });
        }
      }
    }

    // objetivos táctiles y nombre accesible
    const interactive =
      /^(A|BUTTON|INPUT|SELECT|TEXTAREA|SUMMARY)$/.test(el.tagName) ||
      ['button', 'link', 'checkbox', 'radio', 'switch', 'tab'].includes(el.getAttribute('role'));
    if (interactive) {
      if (rect.width < TAP_MIN || rect.height < TAP_MIN) {
        smallTaps.push({
          path: path(el),
          text: textOf(el, 30),
          size: `${Math.round(rect.width)}×${Math.round(rect.height)}`,
        });
      }
      const hidden = el.getAttribute('aria-hidden') === 'true';
      if (!hidden && !accessibleName(el)) {
        unnamed.push({ path: path(el), tag: el.tagName.toLowerCase(), type: el.getAttribute('type') || '' });
      }
    }

    if (el.tagName === 'IMG') {
      if (!el.hasAttribute('alt')) imagesNoAlt.push({ path: path(el), src: (el.currentSrc || el.src || '').slice(-60) });
      const nw = el.naturalWidth || 0;
      if (nw && rect.width && nw > rect.width * 2.5) {
        oversizedImages.push({
          path: path(el),
          natural: `${nw}px`,
          displayed: `${Math.round(rect.width)}px`,
        });
      }
    }
  }

  // encabezados
  const headings = [];
  let lastLevel = 0;
  const skips = [];
  for (const h of document.querySelectorAll('h1,h2,h3,h4,h5,h6')) {
    const cs = getComputedStyle(h);
    const rect = h.getBoundingClientRect();
    if (!isVisible(h, cs, rect)) continue;
    const level = parseInt(h.tagName[1], 10);
    const entry = {
      level,
      text: textOf(h, 60),
      fontSize: `${Math.round(parseFloat(cs.fontSize))}px`,
      weight: cs.fontWeight,
    };
    headings.push(entry);
    if (lastLevel && level > lastLevel + 1) skips.push(`h${lastLevel} → h${level}: "${entry.text}"`);
    lastLevel = level;
  }
  const h1Count = headings.filter((h) => h.level === 1).length;

  // ritmo vertical: secciones de primer nivel
  const container = document.querySelector('main') || document.body;
  const sections = [];
  for (const el of container.children) {
    const cs = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    if (!isVisible(el, cs, rect) || rect.height < 40) continue;
    const chars = (el.textContent || '').replace(/\s+/g, ' ').trim().length;
    const area = Math.max(rect.width * rect.height, 1);
    sections.push({
      path: path(el),
      height: Math.round(rect.height),
      screens: Math.round((rect.height / vh) * 100) / 100,
      paddingY: `${Math.round(parseFloat(cs.paddingTop))}/${Math.round(parseFloat(cs.paddingBottom))}`,
      textChars: chars,
      density: Math.round((chars / area) * 10000) / 100, // caracteres por 100×100 px
      children: el.children.length,
    });
  }

  const fixed = [...document.querySelectorAll('body *')]
    .filter((el) => {
      const cs = getComputedStyle(el);
      return (cs.position === 'fixed' || cs.position === 'sticky') && el.getBoundingClientRect().height > 0;
    })
    .map((el) => ({ path: path(el), position: getComputedStyle(el).position, text: textOf(el, 40) }));

  const sizeList = byCountDesc(sizes);
  const spacingList = byCountDesc(spacing);
  const offGrid = spacingList.filter(({ value }) => {
    const n = parseFloat(value);
    return n % 4 !== 0;
  });

  return {
    meta: {
      url: location.href.slice(0, 200),
      viewport: `${vw}×${vh}`,
      pageHeight: Math.round(document.documentElement.scrollHeight),
      screens: Math.round((document.documentElement.scrollHeight / vh) * 10) / 10,
      elementsScanned: all.length,
      generatedAt: new Date().toISOString(),
      note: 'Datos medidos. El juicio corresponde a la Fase 2 de ux-critic.',
    },
    typography: {
      distinctSizes: sizeList.length,
      sizes: clip(sizeList),
      distinctWeights: weights.size,
      weights: byCountDesc(weights),
      distinctFamilies: families.size,
      families: byCountDesc(families),
      lineHeights: clip(byCountDesc(lineHeights), 12),
    },
    colors: {
      distinctText: textColors.size,
      text: clip(byCountDesc(textColors)),
      distinctBackground: bgColors.size,
      background: clip(byCountDesc(bgColors)),
      borders: clip(byCountDesc(borderColors), 12),
    },
    spacing: {
      distinctValues: spacingList.length,
      values: clip(spacingList),
      offFourGrid: clip(offGrid, 15),
    },
    surfaces: {
      radii: clip(byCountDesc(radii), 12),
      shadows: clip(byCountDesc(shadows), 10),
      zIndexes: clip(byCountDesc(zIndexes), 12),
      fixedOrSticky: clip(fixed, 10),
    },
    contrast: {
      failures: contrastFailures.length,
      worst: clip(contrastFailures.sort((a, b) => a.ratio - b.ratio), 20),
    },
    tapTargets: {
      belowMinimum: smallTaps.length,
      minimum: `${TAP_MIN}×${TAP_MIN}`,
      items: clip(smallTaps, 20),
    },
    headings: {
      h1Count,
      levelSkips: skips,
      outline: clip(headings, 40),
    },
    lineLength: {
      tooLong: clip(longLines, 10),
      tooShort: clip(shortLines, 10),
      thresholds: `${LINE_MIN}–${LINE_MAX} caracteres`,
    },
    rhythm: { sections: clip(sections, 30) },
    interactive: {
      unnamed: clip(unnamed, 20),
      unnamedCount: unnamed.length,
    },
    images: {
      missingAlt: clip(imagesNoAlt, 15),
      oversized: clip(oversizedImages, 15),
    },
  };
})();
