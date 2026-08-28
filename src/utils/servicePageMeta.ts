/**
 * Dedicated /services/{slug} pages that focus on one subcategory (or a curated slice).
 * parentSlug drives visuals + live catalog; liveSubSlugs filters bookable services.
 */

const CDN = 'https://pub-d94f3aebce9d4036815a281f00dd51b3.r2.dev/prod';

export interface ServicePageMeta {
  parentSlug: string;
  /** Admin subcategory slug(s) to show from categoryServices.json */
  liveSubSlugs?: readonly string[];
  /** When true, show the full parent live catalog (e.g. Appliance Repair). */
  useFullParentCatalog?: boolean;
  /** Corner / nav icon (CDN subcategory art when available) */
  icon?: string;
}

function subIcon(slug: string, file: string) {
  return `${CDN}/subcategory/${slug}/${file}`;
}

/** Local parent icon when CDN subcategory art is unavailable */
function parentIcon(path: string) {
  return path;
}

export const servicePageMeta: Record<string, ServicePageMeta> = {
  'masonry-installation': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-installation', 'masonry-installs'],
    icon: parentIcon('/images/categories/icons/masonry.webp'),
  },
  'masonry-repair': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-repair', 'masonry-repairs'],
    icon: parentIcon('/images/categories/icons/masonry.webp'),
  },
  'masonry-inspection': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-inspection'],
    icon: parentIcon('/images/categories/icons/masonry.webp'),
  },
  // Legacy slugs — URLs redirect; keep meta for lookups and live-catalog aliases
  'masonry-installs': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-installation', 'masonry-installs'],
    icon: parentIcon('/images/categories/icons/masonry.webp'),
  },
  'masonry-repairs': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-repair', 'masonry-repairs'],
    icon: parentIcon('/images/categories/icons/masonry.webp'),
  },
  'carpentry-installation': {
    parentSlug: 'carpentry',
    liveSubSlugs: ['carpentry-installation'],
    icon: parentIcon('/images/categories/icons/carpentry.webp'),
  },
  'carpentry-making': {
    parentSlug: 'carpentry',
    liveSubSlugs: ['carpentry-making'],
    icon: parentIcon('/images/categories/icons/carpentry.webp'),
  },
  'carpentry-repairs': {
    parentSlug: 'carpentry',
    liveSubSlugs: ['carpentry-repairs'],
    icon: parentIcon('/images/categories/icons/carpentry.webp'),
  },
  'roofing-works': {
    parentSlug: 'carpentry',
    liveSubSlugs: ['roofing-works'],
    icon: parentIcon('/images/categories/icons/carpentry.webp'),
  },
  'plumbing-installs': {
    parentSlug: 'plumbing',
    liveSubSlugs: ['plumbing-installation'],
    icon: subIcon('plumbing-installation', '2026-07-24-6a6269ed3bcd2.webp'),
  },
  'plumbing-repairs': {
    parentSlug: 'plumbing',
    liveSubSlugs: ['plumbing-repair'],
    icon: subIcon('plumbing-repair', '2026-07-24-6a6269f058788.webp'),
  },
  'plumbing-inspection': {
    parentSlug: 'plumbing',
    liveSubSlugs: ['plumbing-inspection'],
    icon: subIcon('plumbing-inspection', '2026-07-24-6a6269ea112eb.webp'),
  },
  'electrical-installation': {
    parentSlug: 'electrician',
    liveSubSlugs: ['installation-services'],
    icon: subIcon('installation-services', '2026-07-08-6a4e2bd98ecb0.webp'),
  },
  'electrical-repairs': {
    parentSlug: 'electrician',
    liveSubSlugs: ['repairing-services'],
    icon: subIcon('repairing-services', '2026-07-08-6a4e2be0eb8c9.webp'),
  },
  'metal-works-fabrication': {
    parentSlug: 'aluminium-steel-works',
    liveSubSlugs: ['metal-works-fabrication'],
    icon: subIcon('metal-works-fabrication', '2026-07-12-6a52977d58e7b.webp'),
  },
  'metal-works-repairs': {
    parentSlug: 'aluminium-steel-works',
    liveSubSlugs: ['metal-works-repairs'],
    icon: subIcon('metal-works-repairs', '2026-07-12-6a52978525ea0.webp'),
  },
  'renovation-painting': {
    parentSlug: 'painting',
    liveSubSlugs: ['interior-painting', 'exterior-painting'],
    icon: subIcon('interior-painting', '2026-07-08-6a4e2c0718699.webp'),
  },
  'painting-repairs': {
    parentSlug: 'painting',
    icon: subIcon('exterior-painting', '2026-07-08-6a4e2be6bdabd.webp'),
  },
  'appliance-repair': {
    parentSlug: 'home-appliances',
    useFullParentCatalog: true,
    icon: '/images/categories/icons/home-appliances.webp',
  },
  'home-pest-control': {
    parentSlug: 'pest-control',
    liveSubSlugs: ['home-pest-control'],
    icon: subIcon('home-pest-control', '2026-07-11-6a52331934e04.webp'),
  },
  'outdoor-pest-control': {
    parentSlug: 'pest-control',
    icon: subIcon('home-pest-control', '2026-07-11-6a52331934e04.webp'),
  },
  'vehicle-repair-maintenance': {
    parentSlug: 'vehicle-services',
    liveSubSlugs: ['car-repair-maintenance'],
    icon: subIcon('car-repair-maintenance', '2026-07-13-6a54a2992013a.webp'),
  },
  'car-wash-detailing': {
    parentSlug: 'vehicle-services',
    liveSubSlugs: ['car-wash-detailing'],
    icon: subIcon('car-wash-detailing', '2026-07-13-6a54a29fda874.webp'),
  },
  'car-repair-maintenance': {
    parentSlug: 'vehicle-services',
    liveSubSlugs: ['car-repair-maintenance'],
    icon: subIcon('car-repair-maintenance', '2026-07-13-6a54a2992013a.webp'),
  },
  'bike-scooter-service': {
    parentSlug: 'vehicle-services',
    liveSubSlugs: ['bike-scooter-service'],
    icon: subIcon('bike-scooter-service', '2026-07-13-6a54a29233240.webp'),
  },
  'dog-grooming': {
    parentSlug: 'pet-grooming',
    liveSubSlugs: ['dog-grooming'],
    icon: parentIcon('/images/categories/icons/pet-grooming.webp'),
  },
  'cat-grooming': {
    parentSlug: 'pet-grooming',
    liveSubSlugs: ['cat-grooming'],
    icon: parentIcon('/images/categories/icons/pet-grooming.webp'),
  },
  'home-trades': {
    parentSlug: 'book-kaergar',
    liveSubSlugs: ['home-trades'],
    icon: parentIcon('/images/categories/icons/book-kaergar.webp'),
  },
  'building-site': {
    parentSlug: 'book-kaergar',
    liveSubSlugs: ['building-site'],
    icon: parentIcon('/images/categories/icons/book-kaergar.webp'),
  },
  'home-care': {
    parentSlug: 'book-kaergar',
    liveSubSlugs: ['home-care'],
    icon: parentIcon('/images/categories/icons/book-kaergar.webp'),
  },
  'beauty-artists': {
    parentSlug: 'book-kaergar',
    liveSubSlugs: ['beauty-artists'],
    icon: parentIcon('/images/categories/icons/book-kaergar.webp'),
  },
};

export function isServiceVariant(slug: string) {
  return Boolean(servicePageMeta[slug]);
}

export function getServicePageMeta(slug: string): ServicePageMeta | null {
  return servicePageMeta[slug] ?? null;
}

export function getParentServiceSlug(slug: string) {
  return servicePageMeta[slug]?.parentSlug ?? slug;
}
