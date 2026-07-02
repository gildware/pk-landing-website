import Critters from 'critters';
import { readFile, readdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

async function collectHtmlFiles(dir, files = []) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const fullPath = join(dir, entry.name);
    if (entry.isDirectory()) {
      await collectHtmlFiles(fullPath, files);
    } else if (entry.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }
  return files;
}

/** Convert remaining Astro stylesheets to non-render-blocking preload pattern. */
function makeStylesheetsAsync(html) {
  const hrefs = [...new Set([...html.matchAll(/href="(\/_astro\/[^"]+\.css)"/g)].map((m) => m[1]))];
  if (hrefs.length === 0) return html;

  let out = html;
  for (const href of hrefs) {
    const escaped = href.replace(/\//g, '\\/');
    out = out.replace(new RegExp(`<link rel="preload" href="${escaped}" as="style"[^>]*>\\s*`, 'g'), '');
    out = out.replace(new RegExp(`<link rel="stylesheet" href="${escaped}"[^>]*>\\s*`, 'g'), '');
    out = out.replace(
      new RegExp(`<noscript><link rel="stylesheet" href="${escaped}"[^>]*><\\/noscript>\\s*`, 'g'),
      ''
    );
  }

  const asyncTags = hrefs
    .map(
      (href) =>
        `<link rel="preload" href="${href}" as="style" onload="this.onload=null;this.rel='stylesheet'">` +
        `<noscript><link rel="stylesheet" href="${href}"></noscript>`
    )
    .join('');

  return out.replace('</head>', `${asyncTags}</head>`);
}

const distDir = fileURLToPath(new URL('../dist', import.meta.url));

const critters = new Critters({
  path: distDir,
  publicPath: '/',
  preload: 'swap',
  inlineFonts: false,
  pruneSource: false,
});

const htmlFiles = await collectHtmlFiles(distDir);

for (const fullPath of htmlFiles) {
  const html = await readFile(fullPath, 'utf8');
  let optimized = await critters.process(html);
  optimized = makeStylesheetsAsync(optimized);
  await writeFile(fullPath, optimized);
}

console.log(`Critters: optimized ${htmlFiles.length} HTML files in ${distDir}`);
