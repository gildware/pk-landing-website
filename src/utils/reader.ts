import { createReader } from '@keystatic/core/reader';
import keystaticConfig from '../../keystatic.config';
import { renderMarkdocHtml } from './markdoc';

export const reader = createReader(process.cwd(), keystaticConfig);

export type SiteSettings = Awaited<ReturnType<typeof getSiteSettings>>;
export type ServiceEntry = Awaited<ReturnType<typeof getServices>>[number];
export type AreaEntry = Awaited<ReturnType<typeof getAreas>>[number];
export type ServiceAreaPage = Awaited<ReturnType<typeof getServiceAreaPages>>[number];
export type NearMePage = Awaited<ReturnType<typeof getNearMePages>>[number];
export type FaqEntry = Awaited<ReturnType<typeof getFaqs>>[number];

export async function getSiteSettings() {
  const site = await reader.singletons.site.read();
  if (!site) {
    throw new Error('Site settings missing. Add content/site/index.yaml via Keystatic.');
  }
  return site;
}

export async function getHomepage() {
  return reader.singletons.homepage.read();
}

export async function getHomepageHtml() {
  const entry = await reader.singletons.homepage.read();
  if (!entry) return null;
  return renderMarkdocHtml(() => entry.body());
}

async function readAllPublishedServices() {
  const slugs = await reader.collections.services.list();
  const items = await Promise.all(
    slugs.map(async (slug) => {
      const entry = await reader.collections.services.read(slug);
      if (!entry) return null;
      const bodyHtml = await renderMarkdocHtml(() => entry.body());
      return { slug, ...entry, bodyHtml };
    })
  );
  return items
    .filter((item): item is NonNullable<typeof item> => item !== null && item.published)
    .sort((a, b) => (a.sortOrder ?? 0) - (b.sortOrder ?? 0));
}

/** Top-level categories only (excludes subcategory / focused pages with parentSlug). */
export async function getServices() {
  const items = await readAllPublishedServices();
  return items.filter((item) => !item.parentSlug);
}

/** All published service pages including subcategory-focused variants. */
export async function getAllServices() {
  return readAllPublishedServices();
}

export async function getService(slug: string) {
  const entry = await reader.collections.services.read(slug);
  if (!entry || !entry.published) return null;
  const bodyHtml = await renderMarkdocHtml(() => entry.body());
  return { slug, ...entry, bodyHtml };
}

export async function getAreas() {
  const slugs = await reader.collections.areas.list();
  const items = await Promise.all(
    slugs.map(async (slug) => {
      const entry = await reader.collections.areas.read(slug);
      if (!entry) return null;
      const bodyHtml = await renderMarkdocHtml(() => entry.body());
      return { slug, ...entry, bodyHtml };
    })
  );
  return items
    .filter((item): item is NonNullable<typeof item> => item !== null && item.published)
    .sort((a, b) => (a.sortOrder ?? 0) - (b.sortOrder ?? 0));
}

export async function getArea(slug: string) {
  const entry = await reader.collections.areas.read(slug);
  if (!entry || !entry.published) return null;
  const bodyHtml = await renderMarkdocHtml(() => entry.body());
  return { slug, ...entry, bodyHtml };
}

export async function getServiceAreaPages() {
  const slugs = await reader.collections.serviceAreaPages.list();
  const items = await Promise.all(
    slugs.map(async (slug) => {
      const entry = await reader.collections.serviceAreaPages.read(slug);
      if (!entry) return null;
      const bodyHtml = await renderMarkdocHtml(() => entry.body());
      return { slug, ...entry, bodyHtml };
    })
  );
  return items.filter(
    (item): item is NonNullable<typeof item> => item !== null && item.published
  );
}

export async function getServiceAreaPage(slug: string) {
  const entry = await reader.collections.serviceAreaPages.read(slug);
  if (!entry || !entry.published) return null;
  const bodyHtml = await renderMarkdocHtml(() => entry.body());
  return { slug, ...entry, bodyHtml };
}

export async function getNearMePages() {
  const slugs = await reader.collections.nearMePages.list();
  const items = await Promise.all(
    slugs.map(async (slug) => {
      const entry = await reader.collections.nearMePages.read(slug);
      if (!entry) return null;
      const bodyHtml = await renderMarkdocHtml(() => entry.body());
      return { slug, ...entry, bodyHtml };
    })
  );
  return items
    .filter((item): item is NonNullable<typeof item> => item !== null && item.published)
    .sort((a, b) => (a.sortOrder ?? 0) - (b.sortOrder ?? 0));
}

export async function getNearMePage(slug: string) {
  const entry = await reader.collections.nearMePages.read(slug);
  if (!entry || !entry.published) return null;
  const bodyHtml = await renderMarkdocHtml(() => entry.body());
  return { slug, ...entry, bodyHtml };
}

export async function getFaqs() {
  const slugs = await reader.collections.faqs.list();
  const items = await Promise.all(
    slugs.map(async (slug) => {
      const entry = await reader.collections.faqs.read(slug);
      if (!entry) return null;
      return { slug, ...entry };
    })
  );
  return items
    .filter((item): item is NonNullable<typeof item> => item !== null && item.published)
    .sort((a, b) => (a.sortOrder ?? 0) - (b.sortOrder ?? 0));
}

export async function getTestimonials() {
  const slugs = await reader.collections.testimonials.list();
  const items = await Promise.all(
    slugs.map(async (slug) => {
      const entry = await reader.collections.testimonials.read(slug);
      if (!entry) return null;
      return { slug, ...entry };
    })
  );
  return items
    .filter((item): item is NonNullable<typeof item> => item !== null && item.published)
    .sort((a, b) => (a.sortOrder ?? 0) - (b.sortOrder ?? 0));
}

export function getPrimaryArea(areas: AreaEntry[]) {
  return areas[0] ?? { slug: 'srinagar', displayName: 'Srinagar' };
}

export function siteUrl(path = '') {
  const base = import.meta.env.SITE || 'https://panunkaergar.com';
  return `${base.replace(/\/$/, '')}${path.startsWith('/') ? path : `/${path}`}`;
}
