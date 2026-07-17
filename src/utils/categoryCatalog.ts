/**
 * Shared presentation for service categories.
 * Marketing slugs are the URL source of truth; adminSlug maps to panun-admin parents.
 */

const CDN = 'https://pub-d94f3aebce9d4036815a281f00dd51b3.r2.dev/prod';

export interface SubCategoryPill {
  slug: string;
  name: string;
  icon: string;
}

export interface CategoryVisual {
  slug: string;
  adminSlug?: string;
  label: string;
  heading: string;
  blurb: string;
  title: string;
  meta: string;
  prompt: string;
  icon: string;
  soft: string;
  mid: string;
  accent: string;
  /** Live admin subcategories (position=2) */
  subcategories?: SubCategoryPill[];
  /** WorkInContext scatter position hints */
  scatter?: {
    top?: string;
    bottom?: string;
    left?: string;
    right?: string;
  };
}

function sub(slug: string, name: string, file: string): SubCategoryPill {
  return { slug, name, icon: `${CDN}/subcategory/${file}` };
}

/** Subcategories from live panun-admin DB, keyed by marketing slug */
export const categorySubcategories: Record<string, SubCategoryPill[]> = {
  carpentry: [
    sub('carpentry-installation', 'Carpentry Installation', 'carpentry-installation/2026-07-08-6a4e20e74ace9.webp'),
    sub('carpentry-repairs', 'Carpentry Repairs', 'carpentry-repairs/2026-07-08-6a4e20f04b517.webp'),
  ],
  plumbing: [
    sub('plumbing-fixtures', 'Plumbing Fixtures', 'plumbing-fixtures/2026-07-08-6a4e2c36c6bbb.webp'),
    sub('plumbing-installs', 'Plumbing Installs', 'plumbing-installs/2026-07-08-6a4e2c3c633b5.webp'),
  ],
  masonry: [
    sub('masonry-installs', 'Masonry Installs', 'masonry-installs/2026-07-08-6a4e2c10bcbbb.webp'),
    sub('masonry-repairs', 'Masonry Repairs', 'masonry-repairs/2026-07-08-6a4e2c16d7ec0.webp'),
  ],
  electrician: [
    sub('installation-services', 'Electricity Installation', 'installation-services/2026-07-08-6a4e2bdd53d96.webp'),
    sub('repairing-services', 'Electricity Repair', 'repairing-services/2026-07-08-6a4e2be386fdb.webp'),
  ],
  'professional-cleaning': [
    sub('home-cleaning', 'Home Cleaning', 'home-cleaning/2026-07-08-6a4e2bfd92933.webp'),
    sub('office-commercial-cleaning', 'Office & Commercial', 'office-commercial-cleaning/2026-07-08-6a4e2c314674f.webp'),
    sub('post-construction-cleaning', 'Post-Construction', 'post-construction-cleaning/2026-07-08-6a4e2c42a8c9c.webp'),
  ],
  'dry-clean-laundry': [
    sub('garment-care', 'Garment Care', 'dry-clean/2026-07-11-6a521bfa82b7f.webp'),
    sub('household-fabric-care', 'Household Fabric Care', 'wash-laundry/2026-07-11-6a521c03e6ecd.webp'),
    sub('premium-fabric-care', 'Premium Fabric Care', 'premium-fabric-care/2026-07-08-6a4e2c48b10f8.webp'),
  ],
  painting: [
    sub('exterior-painting', 'Exterior Painting', 'exterior-painting/2026-07-08-6a4e2be98a76e.webp'),
    sub('interior-painting', 'Interior Painting', 'interior-painting/2026-07-08-6a4e2c0ace82d.webp'),
  ],
  'home-appliances': [
    sub('air-conditioners', 'Air Conditioners', 'air-conditioners/2026-07-08-6a4e25956ace1.webp'),
    sub('refrigerators', 'Refrigerators', 'refrigerators/2026-07-08-6a4e25c605988.webp'),
    sub('washing-machine', 'Washing Machine', 'washing-machine/2026-07-08-6a4e25d94ec98.webp'),
    sub('led-smart-tv', 'LED / Smart TV', 'led-smart-tv/2026-07-08-6a4e25bcaa606.webp'),
    sub('geysers', 'Geysers', 'geysers/2026-07-08-6a4e25b35e02e.webp'),
    sub('battery-inverters', 'Battery & Inverters', 'battery-inverters/2026-07-08-6a4e259f43b8a.webp'),
  ],
  'mens-salon': [
    sub('mens-beard-shaving', "Beard & Shaving", 'mens-beard-shaving/2026-07-08-6a4e2c1cc8b0e.webp'),
    sub('mens-hair-services', 'Hair Services', 'mens-hair-services/2026-07-08-6a4e2c2386126.webp'),
    sub('mens-skin-grooming-care', 'Skin & Grooming', 'mens-skin-grooming-care/2026-07-08-6a4e2c2a749b1.webp'),
  ],
  'womens-salon': [
    sub('beauty-grooming', 'Beauty & Grooming', 'beauty-grooming/2026-07-08-6a4e2bd46b872.webp'),
    sub('hair-care-services', 'Hair Care', 'hair-care-services/2026-07-08-6a4e2bf7c44b9.webp'),
    sub('skin-facial-care', 'Skin & Facial', 'skin-facial-care/2026-07-08-6a4e2c4f3cd88.webp'),
  ],
};

/** Distinct, readable palette — brand navy + warm accents, not purple-default AI look */
export const categoryCatalog: Record<string, CategoryVisual> = {
  carpentry: {
    slug: 'carpentry',
    adminSlug: 'carpentary',
    label: 'Carpentry',
    heading: 'Need a carpenter at home?',
    blurb:
      'Yes — book a verified carpenter for doors, shelves, cabinets, repairs, and polish. Tell us what needs work and we’ll confirm a local pro at a time that suits you.',
    title: 'Doors, shelves & polish',
    meta: 'Clear quotes before work',
    prompt: 'Furniture repair, doors, cabinets — skilled carpenters near you.',
    icon: '/images/categories/carpentry.png',
    soft: '#fde68a',
    mid: '#f59e0b',
    accent: '#92400e',
    scatter: { top: '6%', right: '11%' },
  },
  plumbing: {
    slug: 'plumbing',
    adminSlug: 'plumbing',
    label: 'Plumbing',
    heading: 'Leak or blocked drain?',
    blurb:
      'Book a verified plumber for leaks, drains, taps, and bathroom pipe work. Share the issue, pick a slot, and get clear next steps before the visit.',
    title: 'Leaks, taps & pipes — handled',
    meta: 'Same-day visits when available',
    prompt: 'Book a verified plumber for leaks, taps, and pipe repairs.',
    icon: '/images/categories/plumbing.png',
    soft: '#bae6fd',
    mid: '#38bdf8',
    accent: '#0369a1',
    scatter: { top: '8%', left: '12%' },
  },
  masonry: {
    slug: 'masonry',
    adminSlug: 'masonry',
    label: 'Masonry',
    heading: 'Wall, plaster, or tile work?',
    blurb:
      'Book a verified mason for cracks, plastering, tiling, and small builds. Describe the job, schedule a visit, and get neat work with clear next steps.',
    title: 'Solid work, neat finish',
    meta: 'Repair & new work',
    prompt: 'Brickwork, plastering, tile fitting, and wall repairs by verified masons.',
    icon: '/images/categories/masonry.png',
    soft: '#fed7aa',
    mid: '#fb923c',
    accent: '#c2410c',
    scatter: { top: '32%', right: '7%' },
  },
  electrician: {
    slug: 'electrician',
    adminSlug: 'electrical',
    label: 'Electrician',
    heading: 'Fan, switch, or wiring issue?',
    blurb:
      'Book a verified electrician who puts safety first. Tell us what’s failing, choose a time, and get a technician to your door for installs or repairs.',
    title: 'Wiring, fans & switches',
    meta: 'Safety-first providers',
    prompt: 'Wiring, switches, fans, and safe electrical repairs at home.',
    icon: '/images/categories/electrician.png',
    soft: '#fef08a',
    mid: '#eab308',
    accent: '#a16207',
    scatter: { top: '22%', left: '2%' },
  },
  'professional-cleaning': {
    slug: 'professional-cleaning',
    adminSlug: 'cleaning',
    label: 'Cleaning',
    heading: 'Need a deep clean?',
    blurb:
      'Book verified cleaners for kitchens, bathrooms, full homes, and offices. Choose a one-time deep clean or a regular visit — apartments, houses, and workplaces covered.',
    title: 'Deep clean, kitchen & more',
    meta: 'Book a convenient slot',
    prompt: 'Deep cleaning, kitchen, bathrooms — professional teams on call.',
    icon: '/images/categories/cleaning.png',
    soft: '#99f6e4',
    mid: '#2dd4bf',
    accent: '#0f766e',
    scatter: { top: '36%', left: '8%' },
  },
  'pest-control': {
    slug: 'pest-control',
    label: 'Pest control',
    heading: 'Pests in the house?',
    blurb:
      'Book safe pest control for cockroaches, ants, rodents, and more. Mention pets or children when you book, then schedule a visit with clear prep steps.',
    title: 'Safe home treatments',
    meta: 'Follow-up when needed',
    prompt: 'Safe treatments for homes — cockroaches, ants, and more.',
    icon: '/images/categories/pest-control.png',
    soft: '#bbf7d0',
    mid: '#4ade80',
    accent: '#15803d',
    scatter: { top: '48%', left: '1%' },
  },
  'dry-clean-laundry': {
    slug: 'dry-clean-laundry',
    adminSlug: 'laundry',
    label: 'Dry clean & laundry',
    heading: 'Need dry clean or laundry?',
    blurb:
      'Book care for suits, sarees, everyday wash & iron, and delicate fabrics. Ask about pickup in your area, and share fabric details so the right provider handles your clothes.',
    title: 'Wash, iron & dry clean',
    meta: 'Pickup where available',
    prompt: 'Dry cleaning and laundry for suits, sarees, and everyday clothes.',
    icon: '/images/categories/dry-clean.png',
    soft: '#c7d2fe',
    mid: '#818cf8',
    accent: '#3730a3',
    scatter: { bottom: '10%', left: '22%' },
  },
  painting: {
    slug: 'painting',
    adminSlug: 'painting',
    label: 'Painting',
    heading: 'Ready to repaint?',
    blurb:
      'Book interior or exterior painting for a room or full home. Get neat prep, clear quotes, and tidy finishes — start with an assessment, then schedule verified painters.',
    title: 'Interior & exterior finishes',
    meta: 'Estimate before you book',
    prompt: 'Interior & exterior painting with neat finishes and clear quotes.',
    icon: '/images/categories/painting.png',
    soft: '#fecdd3',
    mid: '#fb7185',
    accent: '#be123c',
    scatter: { top: '18%', right: '3%' },
  },
  'home-appliances': {
    slug: 'home-appliances',
    adminSlug: 'home-appliance',
    label: 'Home appliances',
    heading: 'Appliance not working?',
    blurb:
      'Book repair for AC, fridge, washing machine, TV, geyser, and more. Share the brand and issue so we match the right technician, then pick a time that works for you.',
    title: 'AC, fridge, wash & more',
    meta: 'Brand-aware technicians',
    prompt: 'AC, fridge, washing machine, TV, and geyser repair by verified techs.',
    icon: '/images/categories/home-appliances.png',
    soft: '#e2e8f0',
    mid: '#94a3b8',
    accent: '#334155',
    scatter: { top: '54%', right: '12%' },
  },
  gardening: {
    slug: 'gardening',
    label: 'Gardening',
    heading: 'Garden looking overgrown?',
    blurb:
      'Book lawn trimming, pruning, planting, and seasonal cleanup for homes and offices. Choose a one-time visit or recurring care to keep outdoor spaces tidy.',
    title: 'Lawn, plants & trim',
    meta: 'One-time or recurring',
    prompt: 'Lawn mowing, pruning, planting, and garden cleanup near you.',
    icon: '/images/categories/gardening.png',
    soft: '#d9f99d',
    mid: '#a3e635',
    accent: '#4d7c0f',
    scatter: { top: '58%', left: '14%' },
  },
  'mens-salon': {
    slug: 'mens-salon',
    adminSlug: 'mens-salon',
    label: "Men's salon",
    heading: 'Need a haircut at home?',
    blurb:
      'Book men’s haircuts, beard trim, and grooming at your door — no salon commute. Choose a time, tell us what you need, and get a verified stylist with professional tools.',
    title: 'Hair, beard & styling',
    meta: 'Flexible time slots',
    prompt: "Men's haircut, beard trim, and grooming at your door.",
    icon: '/images/categories/mens-salon.png',
    soft: '#e9d5ff',
    mid: '#c084fc',
    accent: '#6b21a8',
    scatter: { bottom: '8%', right: '20%' },
  },
  'womens-salon': {
    slug: 'womens-salon',
    adminSlug: 'womens-salon',
    label: "Women's salon",
    heading: 'Want salon care at home?',
    blurb:
      'Book hair, facials, manicure, threading, and party prep with a beautician at your door. Choose a single service or a special-occasion package and enjoy salon care at home.',
    title: 'Hair, facial & beauty',
    meta: 'Home beauty visits',
    prompt: "Women's hair, facials, manicure, and party makeup at home.",
    icon: '/images/categories/womens-salon.png',
    soft: '#fbcfe8',
    mid: '#f472b6',
    accent: '#9d174d',
    scatter: { top: '3%', left: '42%' },
  },
  'interior-decor': {
    slug: 'interior-decor',
    label: 'Interior decor',
    heading: 'Refreshing a room?',
    blurb:
      'Book layout, styling, and colour advice for rooms, homes, and small shops. Start with a consultation, share your goals, and get practical guidance before you refresh or renovate.',
    title: 'Styling & space planning',
    meta: 'Consultation first',
    prompt: 'Space planning, styling, and home makeover support.',
    icon: '/images/categories/interior-decor.png',
    soft: '#fde68a',
    mid: '#fbbf24',
    accent: '#202048',
    scatter: { top: '44%', right: '1%' },
  },
  'tank-cleaning': {
    slug: 'tank-cleaning',
    adminSlug: 'tamkey-cleaning',
    label: 'Tank cleaning',
    heading: 'Time to clean the tank?',
    blurb:
      'Book overhead or underground water tank cleaning for safer water at home. Share access details when you request, and keep household water fresher with regular care.',
    title: 'Water tank cleaning',
    meta: 'Home tank service',
    prompt: 'Book water tank cleaning for safer, cleaner household water storage.',
    icon: '/images/categories/cleaning.png',
    soft: '#a5f3fc',
    mid: '#22d3ee',
    accent: '#0e7490',
    scatter: { bottom: '14%', right: '34%' },
  },
};

export interface ServiceLike {
  slug: string;
  shortName: string;
  description?: string;
  serviceList?: string[];
}

export function enrichCategory(service: ServiceLike, areaName = 'Srinagar') {
  const visual = categoryCatalog[service.slug];
  const label = visual?.label ?? service.shortName;
  const parentIcon = visual?.icon ?? '/images/categories/plumbing.png';

  const fromAdmin = categorySubcategories[service.slug];
  const subcategories: SubCategoryPill[] =
    fromAdmin ??
    (service.serviceList ?? []).slice(0, 6).map((name, i) => ({
      slug: `${service.slug}-${i}`,
      name,
      icon: parentIcon,
    }));

  return {
    slug: service.slug,
    shortName: service.shortName,
    description: service.description ?? '',
    label,
    heading: visual?.heading ?? `Need ${service.shortName.toLowerCase()}?`,
    blurb:
      visual?.blurb ??
      `Book verified ${service.shortName.toLowerCase()} providers across ${areaName}. Share what you need, pick a time that works, and get clear next steps by phone, WhatsApp, website, or the app.`,
    /** Card title uses category name */
    title: label,
    meta: visual?.meta ?? 'Verified local pros',
    prompt: visual?.prompt ?? service.description ?? `Book ${service.shortName} in ${areaName}.`,
    icon: parentIcon,
    soft: visual?.soft ?? '#e2e8f0',
    mid: visual?.mid ?? '#94a3b8',
    accent: visual?.accent ?? '#202048',
    scatter: visual?.scatter,
    adminSlug: visual?.adminSlug,
    subcategories,
  };
}

export function enrichCategories(services: ServiceLike[] | undefined, areaName = 'Srinagar') {
  return (services ?? []).map((s) => enrichCategory(s, areaName));
}

export function categoryIcon(slug: string) {
  return categoryCatalog[slug]?.icon ?? '/images/categories/plumbing.png';
}
