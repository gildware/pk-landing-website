import categoryServices from '@/data/categoryServices.json';
import { categoryCatalog } from '@/utils/categoryCatalog';

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
    title: 'Confirm Time & Details',
    description:
      'We match a verified local partner. You get clear next steps before anyone visits.',
  },
  {
    title: 'Partner Arrives & Completes Work',
    description:
      'Your partner shows up with the right tools, finishes the job, and you can rate the experience afterward.',
  },
] as const;

const SHARED_BENEFITS = [
  {
    title: 'Verified Local Partners',
    description: 'Partners are onboarded and rated by real customers after every job.',
  },
  {
    title: 'Book Your Way',
    description: 'Call, WhatsApp, website form, or the free Panun Kaergar app — same network either way.',
  },
  {
    title: 'Clear Next Steps',
    description: 'Know what happens before the visit — no surprise runaround.',
  },
  {
    title: 'Kashmir Coverage',
    description: 'Serving homes and workplaces across Kashmir districts with local professionals.',
  },
] as const;

export function getBookingSteps() {
  return BOOKING_STEPS;
}

export function getCategoryBenefits(categoryLabel: string) {
  return [
    {
      title: `Skilled ${categoryLabel} Pros`,
      description: `Book partners who focus on ${categoryLabel.toLowerCase()} — matched to the job you describe.`,
    },
    ...SHARED_BENEFITS,
  ];
}
