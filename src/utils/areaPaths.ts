/** SEO-friendly public paths for service-area pages. */

const SEO_PREFIX = 'home-services-in-';

/** Listing page — keyword-rich hub URL. */
export const SERVICE_AREAS_PATH = '/service-areas';

/** e.g. srinagar → home-services-in-srinagar */
export function areaSeoSlug(districtSlug: string): string {
  return `${SEO_PREFIX}${districtSlug}`;
}

/** e.g. srinagar → /service-areas/home-services-in-srinagar */
export function areaPath(districtSlug: string): string {
  return `${SERVICE_AREAS_PATH}/${areaSeoSlug(districtSlug)}`;
}

/** Parse URL param back to content slug, or null if invalid. */
export function districtSlugFromSeoParam(seoSlug: string): string | null {
  if (!seoSlug.startsWith(SEO_PREFIX)) return null;
  const district = seoSlug.slice(SEO_PREFIX.length);
  return district.length > 0 ? district : null;
}

export function areaPageTitle(displayName: string): string {
  return `Home Services in ${displayName}, Kashmir | Book Online`;
}

export function areaPageDescription(displayName: string, fallback?: string): string {
  if (fallback?.trim()) return fallback;
  return `Book verified home services in ${displayName}, Kashmir — carpentry, plumbing, electrician, cleaning, salon & more. Call, WhatsApp, or book online with Panun Kaergar.`;
}
