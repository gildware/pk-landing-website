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

function addStylesheetPreload(html) {
  const match = html.match(/<link[^>]+rel="stylesheet"[^>]+href="(\/_astro\/[^"]+\.css)"[^>]*>/);
  if (!match) return html;

  const href = match[1];
  const preload = `<link rel="preload" href="${href}" as="style">`;
  if (html.includes(preload)) return html;

  return html.replace(match[0], `${preload}${match[0]}`);
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
  optimized = addStylesheetPreload(optimized);
  await writeFile(fullPath, optimized);
}

console.log(`Critters: optimized ${htmlFiles.length} HTML files in ${distDir}`);
