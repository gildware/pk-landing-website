import { siteUrl } from './reader';

const SITE_NAME = 'Panun Kaergar';
/** Share card: navy+gold gear mark on white */
const DEFAULT_OG_IMAGE = '/og-image.png';
const DEFAULT_OG_IMAGE_WIDTH = 1200;
const DEFAULT_OG_IMAGE_HEIGHT = 630;

export interface PageMeta {
  title: string;
  description: string;
  path: string;
  ogType?: string;
  noindex?: boolean;
  ogImage?: string;
  ogImageAlt?: string;
  ogImageWidth?: number;
  ogImageHeight?: number;
}

export interface BuiltPageMeta {
  title: string;
  description: string;
  canonical: string;
  ogType: string;
  noindex: boolean;
  ogImage: string;
  ogImageAlt: string;
  ogImageWidth: number;
  ogImageHeight: number;
}

/** Bing/Google SERP titles truncate around ~60 characters. */
const TITLE_MAX = 60;

/** Keep brand when possible; drop middle “| …” segments before hard-truncating. */
export function fitTitle(title: string, max = TITLE_MAX): string {
  if (title.length <= max) return title;

  const suffix = ` | ${SITE_NAME}`;
  let base = title.endsWith(suffix) ? title.slice(0, -suffix.length) : title;
  const keepBrand = title.endsWith(suffix) || title.includes(SITE_NAME);

  while (base.includes(' | ')) {
    const next = base.split(' | ').slice(0, -1).join(' | ');
    const candidate = keepBrand && !next.includes(SITE_NAME) ? `${next}${suffix}` : next;
    if (candidate.length <= max) return candidate;
    base = next;
  }

  if (keepBrand && !base.includes(SITE_NAME)) {
    const room = max - suffix.length;
    if (room >= 24) {
      let trimmed = base.slice(0, room).trim();
      const sp = trimmed.lastIndexOf(' ');
      if (sp > room * 0.55) trimmed = trimmed.slice(0, sp);
      return `${trimmed.replace(/[|,\-–—:]+$/u, '').trim()}${suffix}`;
    }
  }

  let hard = title.slice(0, max - 1).trim();
  const sp = hard.lastIndexOf(' ');
  if (sp > max * 0.55) hard = hard.slice(0, sp);
  return `${hard}…`;
}

export function buildMeta({
  title,
  description,
  path,
  ogType = 'website',
  noindex = false,
  ogImage = DEFAULT_OG_IMAGE,
  ogImageAlt,
  ogImageWidth,
  ogImageHeight,
}: PageMeta): BuiltPageMeta {
  const url = siteUrl(path);
  const fullTitle = fitTitle(title.includes(SITE_NAME) ? title : `${title} | ${SITE_NAME}`);
  const isDefaultOg =
    ogImage === DEFAULT_OG_IMAGE ||
    ogImage === '/og-image.svg' ||
    ogImage === '/logo-square.png';

  return {
    title: fullTitle,
    description,
    canonical: url,
    ogType,
    noindex,
    ogImage: siteUrl(isDefaultOg ? DEFAULT_OG_IMAGE : ogImage),
    ogImageAlt: ogImageAlt || `${SITE_NAME} — home services in Kashmir`,
    ogImageWidth: ogImageWidth ?? (isDefaultOg ? DEFAULT_OG_IMAGE_WIDTH : 1200),
    ogImageHeight: ogImageHeight ?? (isDefaultOg ? DEFAULT_OG_IMAGE_HEIGHT : 630),
  };
}

export function truncate(text: string, max = 160) {
  if (text.length <= max) return text;
  return `${text.slice(0, max - 1).trim()}…`;
}
