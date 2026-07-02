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

/** Inline critical CSS and defer the rest after Astro static build. */
export function crittersIntegration() {
  return {
    name: 'critters-integration',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        const root = fileURLToPath(dir);
        const critters = new Critters({
          path: root,
          publicPath: '/',
          preload: 'swap',
          inlineFonts: false,
          pruneSource: false,
        });

        const htmlFiles = await collectHtmlFiles(root);

        await Promise.all(
          htmlFiles.map(async (fullPath) => {
            const html = await readFile(fullPath, 'utf8');
            const optimized = await critters.process(html);
            await writeFile(fullPath, optimized);
          })
        );
      },
    },
  };
}
