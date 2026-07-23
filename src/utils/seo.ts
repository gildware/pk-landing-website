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
  const fullTitle = title.includes(SITE_NAME) ? title : `${title} | ${SITE_NAME}`;
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
