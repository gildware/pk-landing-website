#!/usr/bin/env node
/**
 * Refresh service thumbnail URLs in src/data/categoryServices.json from the live API.
 *
 * Admin re-uploads write a new hashed filename and delete the old R2 object.
 * This snapshot must be refreshed or marketing pages 404 those photos.
 *
 *   npm run sync-catalog
 *   SKIP_CATALOG_SYNC=1 npm run build   # offline / CI without live API
 */

import { readFile, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const servicesPath = join(root, 'src/data/categoryServices.json');
const catalogPath = join(root, 'src/data/catalog.json');

const apiBase = (
  process.env.PUBLIC_ADMIN_API_URL?.trim() || 'https://live.panunkaergar.com'
).replace(/\/$/, '');

if (process.env.SKIP_CATALOG_SYNC === '1') {
  console.log('sync-category-images: skipped (SKIP_CATALOG_SYNC=1)');
  process.exit(0);
}

async function main() {
  const [servicesRaw, catalogRaw] = await Promise.all([
    readFile(servicesPath, 'utf8'),
    readFile(catalogPath, 'utf8'),
  ]);
  const data = JSON.parse(servicesRaw);
  const catalog = JSON.parse(catalogRaw);
  const zoneId = process.env.MARKETING_ZONE_ID || catalog.zoneId;
  if (!zoneId) {
    throw new Error('No zoneId in catalog.json (set MARKETING_ZONE_ID)');
  }

  const subSlugs = [
    ...new Set(
      Object.values(data.categories ?? {}).flatMap((cat) =>
        (cat.subcategories ?? []).map((sub) => sub.slug).filter(Boolean),
      ),
    ),
  ];

  const liveBySlug = new Map();
  const results = await mapPool(subSlugs, 6, (slug) => fetchSubcategory(slug, zoneId));
  let failed = 0;
  for (const result of results) {
    if (!result.ok) {
      failed += 1;
      console.warn(`  warn: ${result.slug}: ${result.error}`);
      continue;
    }
    for (const row of result.rows) {
      if (row.slug && row.thumbnail_full_path) {
        liveBySlug.set(row.slug, row.thumbnail_full_path);
      }
    }
  }

  if (liveBySlug.size === 0) {
    console.warn(
      'sync-category-images: live API returned no thumbnails; leaving catalog unchanged',
    );
    process.exit(0);
  }

  let updated = 0;
  let missing = 0;
  for (const cat of Object.values(data.categories ?? {})) {
    for (const sub of cat.subcategories ?? []) {
      for (const svc of sub.services ?? []) {
        const next = liveBySlug.get(svc.slug);
        if (!next) {
          missing += 1;
          continue;
        }
        if (svc.image !== next) {
          svc.image = next;
          updated += 1;
        }
      }
    }
  }

  if (updated === 0) {
    console.log(
      `sync-category-images: already current (${liveBySlug.size} live thumbs, ${missing} catalog slugs not on live)`,
    );
    process.exit(0);
  }

  data.exportedAt = new Date().toISOString().slice(0, 10);
  await writeFile(servicesPath, `${JSON.stringify(data, null, 4)}\n`);
  console.log(
    `sync-category-images: updated ${updated} image URL(s); ${missing} catalog slugs not returned by live (${failed} subcategory fetch errors)`,
  );
}

async function fetchSubcategory(slug, zoneId) {
  const url = `${apiBase}/api/v1/customer/service/sub-category/${encodeURIComponent(slug)}?limit=200&offset=1`;
  try {
    const res = await fetch(url, {
      headers: {
        zoneId,
        'X-localization': 'en',
        Accept: 'application/json',
        'User-Agent': 'panun-marketing-catalog-sync',
      },
      signal: AbortSignal.timeout(25000),
    });
    if (!res.ok) {
      return { ok: false, slug, error: `HTTP ${res.status}`, rows: [] };
    }
    const payload = await res.json();
    const content = payload?.content;
    const rows = Array.isArray(content?.data)
      ? content.data
      : Array.isArray(content)
        ? content
        : [];
    return { ok: true, slug, error: null, rows };
  } catch (err) {
    return { ok: false, slug, error: err instanceof Error ? err.message : String(err), rows: [] };
  }
}

async function mapPool(items, limit, fn) {
  const out = new Array(items.length);
  let next = 0;
  async function worker() {
    while (next < items.length) {
      const i = next++;
      out[i] = await fn(items[i], i);
    }
  }
  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, () => worker()));
  return out;
}

main().catch((err) => {
  console.warn(`sync-category-images: ${err instanceof Error ? err.message : err}`);
  console.warn('Continuing with the committed catalog snapshot.');
  process.exit(0);
});
