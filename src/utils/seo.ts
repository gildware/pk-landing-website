import { siteUrl } from './reader';

export interface PageMeta {
  title: string;
  description: string;
  path: string;
  ogType?: string;
  noindex?: boolean;
  ogImage?: string;
}

export function buildMeta({
  title,
  description,
  path,
  ogType = 'website',
  noindex = false,
  ogImage = '/og-image.svg',
}: PageMeta & { ogImage?: string }) {
  const url = siteUrl(path);
  const fullTitle = title.includes('Panun Kaergar') ? title : `${title} | Panun Kaergar`;

  return {
    title: fullTitle,
    description,
    canonical: url,
    ogType,
    noindex,
    ogImage: siteUrl(ogImage),
  };
}

export function truncate(text: string, max = 160) {
  if (text.length <= max) return text;
  return `${text.slice(0, max - 1).trim()}…`;
}
