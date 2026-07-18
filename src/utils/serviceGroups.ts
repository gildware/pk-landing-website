/**
 * SEO-friendly service groupings for /services (duplicates across groups are intentional).
 * `pageSlug` is the dedicated URL (often a subcategory page); `slug` is the parent category.
 */

export interface ServiceGroupEntry {
  /** Parent category slug (for grouping / fallbacks) */
  slug: string;
  /** Dedicated page under /services/{pageSlug} */
  pageSlug: string;
  displayName: string;
}

export interface ServiceGroupDef {
  label: string;
  keywords: readonly string[];
  entries: readonly ServiceGroupEntry[];
  /** Highlighted / high-intent entries within the group (by pageSlug) */
  featured?: readonly string[];
  /**
   * Parent slugs to expand into subcategory cards on /services
   * (e.g. Vehicle → Car wash, Car repair, Bike & scooter).
   */
  expandSubcategories?: readonly string[];
}

export const serviceGroupDefs: readonly ServiceGroupDef[] = [
  {
    label: 'Construction & Renovation',
    keywords: [
      'construction services',
      'home renovation',
      'renovation contractors',
      'remodeling',
      'interior renovation',
      'home improvement',
    ],
    entries: [
      { slug: 'masonry', pageSlug: 'masonry-installs', displayName: 'Masonry Installs' },
      {
        slug: 'carpentry',
        pageSlug: 'carpentry-installation',
        displayName: 'Carpentry Installation',
      },
      { slug: 'plumbing', pageSlug: 'plumbing-installs', displayName: 'Plumbing Installs' },
      {
        slug: 'electrician',
        pageSlug: 'electrical-installation',
        displayName: 'Electrical Installation',
      },
      {
        slug: 'aluminium-steel-works',
        pageSlug: 'metal-works-fabrication',
        displayName: 'Aluminium & Steel Fabrication',
      },
      { slug: 'painting', pageSlug: 'renovation-painting', displayName: 'Renovation Painting' },
      { slug: 'interior-decor', pageSlug: 'interior-decor', displayName: 'Interior Decor' },
    ],
    featured: ['plumbing-installs', 'electrical-installation'],
  },
  {
    label: 'Repairs & Maintenance',
    keywords: [
      'repair services',
      'maintenance services',
      'emergency repair',
      'home maintenance',
      'appliance repair',
    ],
    entries: [
      { slug: 'plumbing', pageSlug: 'plumbing-repairs', displayName: 'Plumbing Repairs' },
      {
        slug: 'electrician',
        pageSlug: 'electrical-repairs',
        displayName: 'Electrical Repairs',
      },
      { slug: 'carpentry', pageSlug: 'carpentry-repairs', displayName: 'Carpentry Repairs' },
      {
        slug: 'home-appliances',
        pageSlug: 'appliance-repair',
        displayName: 'Appliance Repair',
      },
      { slug: 'painting', pageSlug: 'painting-repairs', displayName: 'Painting Repairs' },
      { slug: 'masonry', pageSlug: 'masonry-repairs', displayName: 'Masonry Repairs' },
      {
        slug: 'aluminium-steel-works',
        pageSlug: 'metal-works-repairs',
        displayName: 'Aluminium & Steel Repairs',
      },
      {
        slug: 'vehicle-services',
        pageSlug: 'vehicle-repair-maintenance',
        displayName: 'Vehicle Repair & Maintenance',
      },
    ],
    featured: [
      'plumbing-repairs',
      'electrical-repairs',
      'carpentry-repairs',
      'painting-repairs',
      'masonry-repairs',
      'metal-works-repairs',
    ],
  },
  {
    label: 'Cleaning & Hygiene',
    keywords: [
      'house cleaning',
      'deep cleaning',
      'office cleaning',
      'pest control',
      'laundry service',
    ],
    entries: [
      {
        slug: 'professional-cleaning',
        pageSlug: 'professional-cleaning',
        displayName: 'Professional Cleaning',
      },
      {
        slug: 'dry-clean-laundry',
        pageSlug: 'dry-clean-laundry',
        displayName: 'Dry Clean & Laundry',
      },
      {
        slug: 'pest-control',
        pageSlug: 'home-pest-control',
        displayName: 'Home Pest Control',
      },
    ],
    featured: ['home-pest-control'],
  },
  {
    label: 'Beauty & Wellness',
    keywords: ['men salon at home', 'women salon at home', 'beauty services'],
    entries: [
      { slug: 'mens-salon', pageSlug: 'mens-salon', displayName: "Men's Salon" },
      { slug: 'womens-salon', pageSlug: 'womens-salon', displayName: "Women's Salon" },
    ],
  },
  {
    label: 'Outdoor Services',
    keywords: ['gardening services', 'lawn care', 'outdoor pest control'],
    entries: [
      { slug: 'gardening', pageSlug: 'gardening', displayName: 'Gardening' },
      {
        slug: 'pest-control',
        pageSlug: 'outdoor-pest-control',
        displayName: 'Outdoor Pest Control',
      },
    ],
    featured: ['outdoor-pest-control'],
  },
  {
    label: 'Pet Care',
    keywords: ['pet grooming', 'dog grooming', 'cat grooming'],
    entries: [{ slug: 'pet-grooming', pageSlug: 'pet-grooming', displayName: 'Pet Grooming' }],
    expandSubcategories: ['pet-grooming'],
  },
  {
    label: 'Vehicle Services',
    keywords: ['car wash', 'car repair', 'bike service', 'scooter service', 'vehicle detailing'],
    entries: [
      { slug: 'vehicle-services', pageSlug: 'vehicle-services', displayName: 'Vehicle Services' },
    ],
    expandSubcategories: ['vehicle-services'],
  },
] as const;

export interface ServiceOption {
  slug: string;
  shortName: string;
}

export function groupServices(_services: ServiceOption[]) {
  const groups: Array<{ label: string; services: ServiceOption[] }> = serviceGroupDefs
    .map((def) => ({
      label: def.label,
      services: def.entries.map((entry) => ({
        slug: entry.pageSlug,
        shortName: entry.displayName,
      })),
    }))
    .filter((g) => g.services.length > 0);

  return groups;
}
