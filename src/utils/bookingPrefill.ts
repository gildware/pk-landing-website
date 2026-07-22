/**
 * Resolve marketing service slugs → booking form option labels.
 * Form values are display names from serviceGroupDefs (+ parent shortNames).
 */
import { serviceGroupDefs } from './serviceGroups';

/**
 * Phrase after “Book …” on CTAs and book-page titles.
 * Must read as booking a person or a service — never a whole venue/business.
 * Examples:
 *   Carpenter → “Book Carpenter in Budgam”
 *   Men's Salon Services → “Book Men's Salon Services in Kashmir”
 */
const BOOK_CTA_NOUN: Record<string, string> = {
  // Tradespeople (person form)
  carpentry: 'Carpenter',
  plumbing: 'Plumber',
  electrician: 'Electrician',
  painting: 'Painter',
  masonry: 'Mason',
  gardening: 'Gardener',

  // Named services (already service-like)
  'pest-control': 'Pest Control',
  'home-pest-control': 'Pest Control',
  'outdoor-pest-control': 'Pest Control',
  'professional-cleaning': 'Home Cleaning',
  'dry-clean-laundry': 'Dry Cleaning',
  'home-appliances': 'Appliance Repair',
  'appliance-repair': 'Appliance Repair',
  'vehicle-services': 'Vehicle Services',
  'car-wash-detailing': 'Car Wash',
  'car-repair-maintenance': 'Car Repair',
  'bike-scooter-service': 'Bike Service',
  'vehicle-repair-maintenance': 'Vehicle Repair',

  // Venue / category names — add “Services” so CTAs aren’t ambiguous
  'mens-salon': "Men's Salon Services",
  'womens-salon': "Women's Salon Services",
  'pet-grooming': 'Pet Grooming Services',
  'dog-grooming': 'Dog Grooming Services',
  'cat-grooming': 'Cat Grooming Services',
  'interior-decor': 'Interior Decor Services',
  'aluminium-steel-works': 'Aluminium & Steel Services',

  // Focused subcategory pages — already service phrases
  'carpentry-installation': 'Carpentry Installation',
  'carpentry-repairs': 'Carpentry Repairs',
  'plumbing-installs': 'Plumbing Installs',
  'plumbing-repairs': 'Plumbing Repairs',
  'electrical-installation': 'Electrical Installation',
  'electrical-repairs': 'Electrical Repairs',
  'masonry-installs': 'Masonry Installs',
  'masonry-repairs': 'Masonry Repairs',
  'renovation-painting': 'Renovation Painting',
  'painting-repairs': 'Painting Repairs',
  'metal-works-fabrication': 'Metal Fabrication',
  'metal-works-repairs': 'Metal Repairs',
};

/** Parent category → preferred bookable form option when the parent itself isn’t ideal. */
const PARENT_FALLBACK: Record<string, string> = {
  plumbing: 'Plumbing Repairs',
  electrician: 'Electrical Repairs',
  carpentry: 'Carpentry Repairs',
  masonry: 'Masonry Repairs',
  painting: 'Painting Repairs',
  'home-appliances': 'Appliance Repair',
  'aluminium-steel-works': 'Aluminium & Steel Repairs',
  'pest-control': 'Home Pest Control',
  'professional-cleaning': 'Professional Cleaning',
  'dry-clean-laundry': 'Dry Clean & Laundry',
  'vehicle-services': 'Vehicle Services',
  gardening: 'Gardening',
  'mens-salon': "Men's Salon",
  'womens-salon': "Women's Salon",
  'pet-grooming': 'Pet Grooming',
  'interior-decor': 'Interior Decor',
};

/** Near-me / specialty slug → form option. */
const SPECIALTY_MAP: Record<string, string> = {
  'appliance-repair': 'Appliance Repair',
  'carpentry-installation': 'Carpentry Installation',
  'carpentry-repairs': 'Carpentry Repairs',
  'plumbing-installs': 'Plumbing Installs',
  'plumbing-repairs': 'Plumbing Repairs',
  'electrical-installation': 'Electrical Installation',
  'electrical-repairs': 'Electrical Repairs',
  'masonry-installs': 'Masonry Installs',
  'masonry-repairs': 'Masonry Repairs',
  'renovation-painting': 'Renovation Painting',
  'painting-repairs': 'Painting Repairs',
  'metal-works-fabrication': 'Aluminium & Steel Fabrication',
  'metal-works-repairs': 'Aluminium & Steel Repairs',
  'home-pest-control': 'Home Pest Control',
  'outdoor-pest-control': 'Outdoor Pest Control',
  'vehicle-repair-maintenance': 'Vehicle Repair & Maintenance',
  'car-wash-detailing': 'Vehicle Services',
  'car-repair-maintenance': 'Vehicle Repair & Maintenance',
  'bike-scooter-service': 'Vehicle Services',
  'dog-grooming': 'Pet Grooming',
  'cat-grooming': 'Pet Grooming',
};

const DISTRICT_NAMES: Record<string, string> = {
  srinagar: 'Srinagar',
  budgam: 'Budgam',
  ganderbal: 'Ganderbal',
  bandipora: 'Bandipora',
  baramulla: 'Baramulla',
  kupwara: 'Kupwara',
  anantnag: 'Anantnag',
  kulgam: 'Kulgam',
  pulwama: 'Pulwama',
  shopian: 'Shopian',
};

function buildPageSlugMap(): Record<string, string> {
  const map: Record<string, string> = { ...SPECIALTY_MAP };
  for (const group of serviceGroupDefs) {
    for (const entry of group.entries) {
      map[entry.pageSlug] = entry.displayName;
      if (!map[entry.slug] && PARENT_FALLBACK[entry.slug]) {
        map[entry.slug] = PARENT_FALLBACK[entry.slug];
      }
    }
  }
  for (const [slug, label] of Object.entries(PARENT_FALLBACK)) {
    if (!map[slug]) map[slug] = label;
  }
  return map;
}

const SLUG_TO_LABEL = buildPageSlugMap();

/**
 * Make CMS / fallback labels read as a bookable service, not a venue.
 * e.g. “Men's Salon” → “Men's Salon Services”
 */
export function clarifyBookCtaNoun(label: string): string {
  const t = label.trim();
  if (!t) return 'a home service';
  if (/\bservices?\b/i.test(t)) return t;
  // Place / venue sounding names
  if (/\bsalon\b/i.test(t)) return `${t} Services`;
  if (/\b(interior|decor)\b/i.test(t)) return `${t} Services`;
  // Category brand names without a clear service verb
  if (/^(aluminium|aluminum)\b/i.test(t) && !/\b(repair|fabrication|install)/i.test(t)) {
    return `${t} Services`;
  }
  if (/^pet grooming$/i.test(t) || /^dog grooming$/i.test(t) || /^cat grooming$/i.test(t)) {
    return `${t} Services`;
  }
  return t;
}

export function bookingLabelForSlug(slug: string | undefined | null): string | null {
  if (!slug?.trim()) return null;
  const key = slug.trim().toLowerCase();
  return SLUG_TO_LABEL[key] ?? null;
}

/**
 * Noun/phrase for Book CTAs (person or clear service name).
 * Prefer mapped CTA nouns; otherwise clarify the fallback.
 */
export function bookCtaLabel(
  slug: string | undefined | null,
  fallback?: string | null
): string {
  if (!slug?.trim()) {
    return clarifyBookCtaNoun(fallback || 'a home service');
  }
  const key = slug.trim().toLowerCase();
  if (BOOK_CTA_NOUN[key]) return BOOK_CTA_NOUN[key];
  if (fallback?.trim()) return clarifyBookCtaNoun(fallback);
  const formLabel = bookingLabelForSlug(key);
  if (formLabel) return clarifyBookCtaNoun(formLabel);
  return clarifyBookCtaNoun(fallback || 'a home service');
}

/** “Book Carpenter” / “Book Men's Salon Services in Budgam”. */
export function bookCtaText(
  slug: string | undefined | null,
  opts?: { fallback?: string | null; areaName?: string | null }
): string {
  const label = bookCtaLabel(slug, opts?.fallback);
  const area = opts?.areaName?.trim();
  return area ? `Book ${label} in ${area}` : `Book ${label}`;
}

/** All known slug → label pairs for the booking form client script. */
export function bookingSlugLabelEntries(): { slug: string; label: string }[] {
  return Object.entries(SLUG_TO_LABEL).map(([slug, label]) => ({ slug, label }));
}

export function districtDisplayName(areaParam: string | undefined | null): string | null {
  if (!areaParam?.trim()) return null;
  const raw = areaParam.trim();
  const fromSlug = DISTRICT_NAMES[raw.toLowerCase()];
  if (fromSlug) return fromSlug;
  // Already a display name or free text
  return raw;
}

export function isKnownDistrictSlug(value: string | undefined | null): boolean {
  if (!value?.trim()) return false;
  return Boolean(DISTRICT_NAMES[value.trim().toLowerCase()]);
}
