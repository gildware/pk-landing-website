import categoryServices from '@/data/categoryServices.json';
import { categoryCatalog } from '@/utils/categoryCatalog';

/** Snapshot of live service thumbnails. Refresh with `npm run sync-catalog` after admin image uploads. */

export interface LiveServiceItem {
  name: string;
  slug: string;
  shortDescription: string;
  image: string | null;
  avgRating: number | null;
  ratingCount: number;
}

export interface LiveSubcategory {
  slug: string;
  name: string;
  services: LiveServiceItem[];
}

export interface LiveCategoryBundle {
  marketingSlug: string;
  adminSlug: string;
  adminName: string;
  serviceCount: number;
  subcategories: LiveSubcategory[];
}

const catalog = categoryServices as {
  categories: Record<string, LiveCategoryBundle>;
};

export function getLiveCategoryServices(marketingSlug: string): LiveCategoryBundle | null {
  return catalog.categories[marketingSlug] ?? null;
}

/** Live catalog filtered to one or more admin subcategories under a parent. */
export function getLiveSubcategoryBundle(
  parentSlug: string,
  liveSubSlugs?: readonly string[],
): LiveCategoryBundle | null {
  const parent = getLiveCategoryServices(parentSlug);
  if (!parent) return null;
  if (!liveSubSlugs?.length) return parent;

  const subcategories = parent.subcategories.filter((sub) => liveSubSlugs.includes(sub.slug));
  if (subcategories.length === 0) return null;

  return {
    ...parent,
    marketingSlug: parentSlug,
    serviceCount: subcategories.reduce((n, s) => n + s.services.length, 0),
    subcategories,
  };
}

/** Representative work images for a category (service photos from live DB). */
export function getCategoryWorkGallery(marketingSlug: string, limit = 8): LiveServiceItem[] {
  const bundle = getLiveCategoryServices(marketingSlug);
  if (!bundle) return [];
  const withImages = bundle.subcategories
    .flatMap((sub) => sub.services)
    .filter((s) => Boolean(s.image));
  return withImages.slice(0, limit);
}

export function getCategoryHeroImage(
  marketingSlug: string,
  liveSubSlugs?: readonly string[],
): string {
  const bundle = liveSubSlugs?.length
    ? getLiveSubcategoryBundle(marketingSlug, liveSubSlugs)
    : getLiveCategoryServices(marketingSlug);
  const withImage = bundle?.subcategories
    .flatMap((sub) => sub.services)
    .find((s) => Boolean(s.image));
  if (withImage?.image) return withImage.image;
  return categoryCatalog[marketingSlug]?.icon ?? '/images/categories/plumbing.png';
}

const BOOKING_STEPS = [
  {
    title: 'Tell Us What You Need',
    description:
      'Pick this category, describe the job, and share your address — by phone, WhatsApp, website, or the app.',
  },
  {
    title: 'We Take Care of the Rest',
    description:
      'Panun Kaergar confirms price and timing, then assigns who will do the work. You get clear next steps before anyone visits.',
  },
  {
    title: 'We Get It Done',
    description:
      'Our team or a professional partner arrives with the right tools, finishes the job to our standards, and you can rate the experience afterward.',
  },
] as const;

const SHARED_BENEFITS = [
  {
    title: 'We Own the Job',
    description: 'You hire Panun Kaergar. We handle pricing, quality, and support — not a random number.',
  },
  {
    title: 'Book Your Way',
    description: 'Call, WhatsApp, website form, or the free Panun Kaergar app — same company either way.',
  },
  {
    title: 'Clear Next Steps',
    description: 'Know what happens before the visit — no surprise runaround.',
  },
  {
    title: 'Kashmir Coverage',
    description: 'Serving homes and workplaces across Kashmir districts.',
  },
] as const;

export function getBookingSteps() {
  return BOOKING_STEPS;
}

export function getCategoryBenefits(categoryLabel: string) {
  return [
    {
      title: `Skilled ${categoryLabel} Pros`,
      description: `Panun Kaergar handles ${categoryLabel.toLowerCase()} for the job you describe — our team or a professional partner.`,
    },
    ...SHARED_BENEFITS,
  ];
}
