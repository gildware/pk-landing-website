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

export const servicePageMeta: Record<string, ServicePageMeta> = {
  'masonry-installs': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-installs'],
    icon: subIcon('masonry-installs', '2026-07-08-6a4e2c0dd2475.webp'),
  },
  'masonry-repairs': {
    parentSlug: 'masonry',
    liveSubSlugs: ['masonry-repairs'],
    icon: subIcon('masonry-repairs', '2026-07-08-6a4e2c1434738.webp'),
  },
  'carpentry-installation': {
    parentSlug: 'carpentry',
    liveSubSlugs: ['carpentry-installation'],
    icon: subIcon('carpentry-installation', '2026-07-08-6a4e20e363690.webp'),
  },
  'carpentry-repairs': {
    parentSlug: 'carpentry',
    liveSubSlugs: ['carpentry-repairs'],
    icon: subIcon('carpentry-repairs', '2026-07-08-6a4e20ebdfb4c.webp'),
  },
  'plumbing-installs': {
    parentSlug: 'plumbing',
    liveSubSlugs: ['plumbing-installs'],
    icon: subIcon('plumbing-installs', '2026-07-08-6a4e2c3a3a5ab.webp'),
  },
  'plumbing-repairs': {
    parentSlug: 'plumbing',
    // No dedicated admin sub — curated repair-focused page
    icon: subIcon('plumbing-fixtures', '2026-07-08-6a4e2c3455733.webp'),
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
    icon: '/images/categories/home-appliances.png',
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
    icon: subIcon('dog-grooming', '2026-07-12-6a528e24df4d0.webp'),
  },
  'cat-grooming': {
    parentSlug: 'pet-grooming',
    liveSubSlugs: ['cat-grooming'],
    icon: subIcon('cat-grooming', '2026-07-12-6a528e21de347.webp'),
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
