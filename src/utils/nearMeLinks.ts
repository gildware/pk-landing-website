/**
 * Near-me discoverability helpers — featured links + service → near-me mapping.
 */

export interface NearMeLink {
  slug: string;
  href: string;
  label: string;
  /** Parent marketing service slug(s) this near-me page belongs to */
  serviceSlugs: readonly string[];
}

/** Full catalog of near-me landing pages (keep in sync with content/near-me-pages). */
export const NEAR_ME_LINKS: readonly NearMeLink[] = [
  {
    slug: 'plumber-near-me',
    href: '/near-me/plumber-near-me',
    label: 'Plumber near me',
    serviceSlugs: ['plumbing', 'plumbing-installs', 'plumbing-repairs'],
  },
  {
    slug: 'carpenter-near-me',
    href: '/near-me/carpenter-near-me',
    label: 'Carpenter near me',
    serviceSlugs: ['carpentry', 'carpentry-installation', 'carpentry-repairs'],
  },
  {
    slug: 'electrician-near-me',
    href: '/near-me/electrician-near-me',
    label: 'Electrician near me',
    serviceSlugs: ['electrician', 'electrical-installation', 'electrical-repairs'],
  },
  {
    slug: 'ac-repair-near-me',
    href: '/near-me/ac-repair-near-me',
    label: 'AC repair near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'cctv-installation-near-me',
    href: '/near-me/cctv-installation-near-me',
    label: 'CCTV installation near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'washing-machine-repair-near-me',
    href: '/near-me/washing-machine-repair-near-me',
    label: 'Washing machine repair near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'fridge-repair-near-me',
    href: '/near-me/fridge-repair-near-me',
    label: 'Fridge repair near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'painter-near-me',
    href: '/near-me/painter-near-me',
    label: 'Painter near me',
    serviceSlugs: ['painting', 'renovation-painting', 'painting-repairs'],
  },
  {
    slug: 'mason-near-me',
    href: '/near-me/mason-near-me',
    label: 'Mason near me',
    serviceSlugs: ['masonry', 'masonry-installs', 'masonry-repairs'],
  },
  {
    slug: 'pest-control-near-me',
    href: '/near-me/pest-control-near-me',
    label: 'Pest control near me',
    serviceSlugs: ['pest-control', 'home-pest-control', 'outdoor-pest-control'],
  },
  {
    slug: 'emergency-plumber-near-me',
    href: '/near-me/emergency-plumber-near-me',
    label: 'Emergency plumber near me',
    serviceSlugs: ['plumbing', 'plumbing-repairs'],
  },
  {
    slug: 'emergency-electrician-near-me',
    href: '/near-me/emergency-electrician-near-me',
    label: 'Emergency electrician near me',
    serviceSlugs: ['electrician', 'electrical-repairs'],
  },
  {
    slug: 'geyser-repair-near-me',
    href: '/near-me/geyser-repair-near-me',
    label: 'Geyser repair near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'tv-repair-near-me',
    href: '/near-me/tv-repair-near-me',
    label: 'TV repair near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'ro-service-near-me',
    href: '/near-me/ro-service-near-me',
    label: 'RO service near me',
    serviceSlugs: ['home-appliances', 'appliance-repair'],
  },
  {
    slug: 'home-cleaning-near-me',
    href: '/near-me/home-cleaning-near-me',
    label: 'Home cleaning near me',
    serviceSlugs: ['professional-cleaning'],
  },
  {
    slug: 'sofa-cleaning-near-me',
    href: '/near-me/sofa-cleaning-near-me',
    label: 'Sofa cleaning near me',
    serviceSlugs: ['professional-cleaning'],
  },
  {
    slug: 'dry-cleaning-near-me',
    href: '/near-me/dry-cleaning-near-me',
    label: 'Dry cleaning near me',
    serviceSlugs: ['dry-clean-laundry'],
  },
  {
    slug: 'car-wash-near-me',
    href: '/near-me/car-wash-near-me',
    label: 'Car wash near me',
    serviceSlugs: ['vehicle-services', 'car-wash-detailing', 'car-repair-maintenance', 'bike-scooter-service'],
  },
  {
    slug: 'door-repair-near-me',
    href: '/near-me/door-repair-near-me',
    label: 'Door repair near me',
    serviceSlugs: ['carpentry', 'carpentry-repairs'],
  },
] as const;

/** Homepage / footer featured set (high intent, keep short). */
export const FEATURED_NEAR_ME_SLUGS = [
  'plumber-near-me',
  'carpenter-near-me',
  'electrician-near-me',
  'ac-repair-near-me',
  'cctv-installation-near-me',
  'emergency-plumber-near-me',
  'painter-near-me',
  'home-cleaning-near-me',
] as const;

export const NEAR_ME_HUB_PATH = '/near-me';

export function featuredNearMeLinks(): NearMeLink[] {
  const bySlug = new Map(NEAR_ME_LINKS.map((l) => [l.slug, l]));
  return FEATURED_NEAR_ME_SLUGS.map((slug) => bySlug.get(slug)).filter(
    (l): l is NearMeLink => Boolean(l)
  );
}

/** Near-me pages related to a service / subcategory slug. */
export function nearMeLinksForService(serviceSlug: string): NearMeLink[] {
  const key = serviceSlug.trim().toLowerCase();
  return NEAR_ME_LINKS.filter((l) => l.serviceSlugs.includes(key));
}

/** Primary near-me page for a service (first match). */
export function primaryNearMeForService(serviceSlug: string): NearMeLink | null {
  return nearMeLinksForService(serviceSlug)[0] ?? null;
}
