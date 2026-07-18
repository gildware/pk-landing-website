/**
 * Shared presentation for service categories.
 * Marketing slugs are the URL source of truth; adminSlug maps to panun-admin parents.
 * Categories + subcategories mirror the live panun-admin `categories` table only.
 */

import { getServicePageMeta } from '@/utils/servicePageMeta';

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
    sub('carpentry-installation', 'Carpentry Installation', 'carpentry-installation/2026-07-08-6a4e20e363690.webp'),
    sub('carpentry-repairs', 'Carpentry Repairs', 'carpentry-repairs/2026-07-08-6a4e20ebdfb4c.webp'),
    sub('roofing-works', 'Roofing Works', 'roofing-works/2026-07-17-6a59b0fa66e93.webp'),
  ],
  plumbing: [
    sub('plumbing-fixtures', 'Plumbing Fixtures', 'plumbing-fixtures/2026-07-08-6a4e2c3455733.webp'),
    sub('plumbing-installs', 'Plumbing Installs', 'plumbing-installs/2026-07-08-6a4e2c3a3a5ab.webp'),
  ],
  masonry: [
    sub('masonry-installs', 'Masonry Installs', 'masonry-installs/2026-07-08-6a4e2c0dd2475.webp'),
    sub('masonry-repairs', 'Masonry Repairs', 'masonry-repairs/2026-07-08-6a4e2c1434738.webp'),
  ],
  electrician: [
    sub('installation-services', 'Electricity Installation', 'installation-services/2026-07-08-6a4e2bd98ecb0.webp'),
    sub('repairing-services', 'Electricity Repair Services', 'repairing-services/2026-07-08-6a4e2be0eb8c9.webp'),
  ],
  'professional-cleaning': [
    sub('home-cleaning', 'Home Cleaning', 'home-cleaning/2026-07-08-6a4e2bfb04c94.webp'),
    sub('office-commercial-cleaning', 'Office & Commercial Cleaning', 'office-commercial-cleaning/2026-07-08-6a4e2c2ec105d.webp'),
    sub('post-construction-cleaning', 'Post-Construction Cleaning', 'post-construction-cleaning/2026-07-08-6a4e2c3fcc8c1.webp'),
  ],
  'dry-clean-laundry': [
    sub('dry-clean', 'Dry Clean', 'dry-clean/2026-07-11-6a521bf5f10ed.webp'),
    sub('wash-laundry', 'Laundry', 'wash-laundry/2026-07-11-6a521bff58f89.webp'),
  ],
  painting: [
    sub('exterior-painting', 'Exterior Painting', 'exterior-painting/2026-07-08-6a4e2be6bdabd.webp'),
    sub('interior-painting', 'Interior Painting', 'interior-painting/2026-07-08-6a4e2c0718699.webp'),
  ],
  'home-appliances': [
    sub('air-conditioners', 'Air Conditioners', 'air-conditioners/2026-07-08-6a4e25915f04e.webp'),
    sub('battery-inverters', 'Battery & Inverters', 'battery-inverters/2026-07-08-6a4e259af2536.webp'),
    sub('cctv', 'CCTV', 'cctv/2026-07-08-6a4e25a47c2de.webp'),
    sub('geysers', 'Geysers', 'geysers/2026-07-08-6a4e25ae60556.webp'),
    sub('led-smart-tv', 'LED / Smart TV', 'led-smart-tv/2026-07-08-6a4e25b843be1.webp'),
    sub('refrigerators', 'Refrigerators', 'refrigerators/2026-07-08-6a4e25c1c96a5.webp'),
    sub('induction-heaters', 'Small Appliances', 'induction-heaters/2026-07-08-6a4e25cad58b5.webp'),
    sub('washing-machine', 'Washing Machine', 'washing-machine/2026-07-08-6a4e25d468714.webp'),
    sub('ro-purifier', 'Water Purifier', 'ro-purifier/2026-07-08-6a4e25dda37f4.webp'),
  ],
  'mens-salon': [
    sub('mens-beard-shaving', "Men's Beard & Shaving", 'mens-beard-shaving/2026-07-08-6a4e2c1a70c7f.webp'),
    sub('mens-hair-services', "Men's Hair Services", 'mens-hair-services/2026-07-08-6a4e2c21000da.webp'),
    sub('mens-skin-grooming-care', "Men's Skin & Grooming Care", 'mens-skin-grooming-care/2026-07-08-6a4e2c2789744.webp'),
  ],
  'womens-salon': [
    sub('beauty-grooming', 'Beauty & Grooming', 'beauty-grooming/2026-07-08-6a4e2bd193c90.webp'),
    sub('hair-care-services', 'Hair Care Services', 'hair-care-services/2026-07-08-6a4e2bf40f2dd.webp'),
    sub('skin-facial-care', 'Skin & Facial Care', 'skin-facial-care/2026-07-08-6a4e2c4cd1cc9.webp'),
  ],
  'pest-control': [
    sub('home-pest-control', 'Home Pest Control', 'home-pest-control/2026-07-11-6a52331934e04.webp'),
    sub('office-pest-control', 'Office Pest Control', 'office-pest-control/2026-07-11-6a52331dc0094.webp'),
    sub('restaurant-pest-control', 'Restaurant Pest Control', 'restaurant-pest-control/2026-07-11-6a523322b9e01.webp'),
  ],
  gardening: [
    sub('lawn-grass-care', 'Lawn & Grass Care', 'lawn-grass-care/2026-07-13-6a54a2fbe537d.webp'),
    sub('planting-soil-care', 'Planting & Soil Care', 'planting-soil-care/2026-07-13-6a54a303ba776.webp'),
    sub('pruning-trimming', 'Pruning & Trimming', 'pruning-trimming/2026-07-13-6a54a30b0555b.webp'),
    sub('garden-cleanup-maintenance', 'Garden Cleanup & Maintenance', 'garden-cleanup-maintenance/2026-07-13-6a54a2f40d8c0.webp'),
  ],
  'aluminium-steel-works': [
    sub('metal-works-installation', 'Metal Works Installation', 'metal-works-installation/2026-07-12-6a5297813acf4.webp'),
    sub('metal-works-repairs', 'Metal Works Repairs', 'metal-works-repairs/2026-07-12-6a52978525ea0.webp'),
    sub('metal-works-fabrication', 'Metal Works Fabrication', 'metal-works-fabrication/2026-07-12-6a52977d58e7b.webp'),
  ],
  'interior-decor': [
    sub('home-decor-consultation', 'Home Decor Consultation', 'home-decor-consultation/2026-07-13-6a549f7d3cec4.webp'),
    sub('commercial-decor-styling', 'Commercial Decor Styling', 'commercial-decor-styling/2026-07-13-6a549f7628491.webp'),
  ],
  'pet-grooming': [
    sub('dog-grooming', 'Dog Grooming', 'dog-grooming/2026-07-12-6a528e24df4d0.webp'),
    sub('cat-grooming', 'Cat Grooming', 'cat-grooming/2026-07-12-6a528e21de347.webp'),
  ],
  'vehicle-services': [
    sub('car-wash-detailing', 'Car Wash & Detailing', 'car-wash-detailing/2026-07-13-6a54a29fda874.webp'),
    sub('car-repair-maintenance', 'Car Repair & Maintenance', 'car-repair-maintenance/2026-07-13-6a54a2992013a.webp'),
    sub('bike-scooter-service', 'Bike & Scooter Service', 'bike-scooter-service/2026-07-13-6a54a29233240.webp'),
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
    icon: '/images/categories/icons/carpentry.webp',
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
    icon: '/images/categories/icons/plumbing.webp',
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
    icon: '/images/categories/icons/masonry.webp',
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
    meta: 'Safety-first partners',
    prompt: 'Wiring, switches, fans, and safe electrical repairs at home.',
    icon: '/images/categories/icons/electrician.webp',
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
    icon: '/images/categories/icons/cleaning.webp',
    soft: '#99f6e4',
    mid: '#2dd4bf',
    accent: '#0f766e',
    scatter: { top: '36%', left: '8%' },
  },
  'pest-control': {
    slug: 'pest-control',
    adminSlug: 'pest-control',
    label: 'Pest control',
    heading: 'Pests in the house?',
    blurb:
      'Book safe pest control for cockroaches, ants, rodents, and more. Mention pets or children when you book, then schedule a visit with clear prep steps.',
    title: 'Safe home treatments',
    meta: 'Follow-up when needed',
    prompt: 'Safe treatments for homes — cockroaches, ants, and more.',
    icon: '/images/categories/icons/pest-control.webp',
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
      'Book care for suits, sarees, everyday wash & iron, and delicate fabrics. Ask about pickup in your area, and share fabric details so the right partner handles your clothes.',
    title: 'Wash, iron & dry clean',
    meta: 'Pickup where available',
    prompt: 'Dry cleaning and laundry for suits, sarees, and everyday clothes.',
    icon: '/images/categories/icons/dry-clean.webp',
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
    icon: '/images/categories/icons/painting.webp',
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
    icon: '/images/categories/icons/home-appliances.webp',
    soft: '#e2e8f0',
    mid: '#94a3b8',
    accent: '#334155',
    scatter: { top: '54%', right: '12%' },
  },
  gardening: {
    slug: 'gardening',
    adminSlug: 'gardening',
    label: 'Gardening',
    heading: 'Garden looking overgrown?',
    blurb:
      'Book lawn trimming, pruning, planting, and seasonal cleanup for homes and offices. Choose a one-time visit or recurring care to keep outdoor spaces tidy.',
    title: 'Lawn, plants & trim',
    meta: 'One-time or recurring',
    prompt: 'Lawn mowing, pruning, planting, and garden cleanup near you.',
    icon: '/images/categories/icons/gardening.webp',
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
    icon: '/images/categories/icons/mens-salon.webp',
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
    icon: '/images/categories/icons/womens-salon.webp',
    soft: '#fbcfe8',
    mid: '#f472b6',
    accent: '#9d174d',
    scatter: { top: '3%', left: '42%' },
  },
  'interior-decor': {
    slug: 'interior-decor',
    adminSlug: 'interior-decor',
    label: 'Interior decor',
    heading: 'Refreshing a room?',
    blurb:
      'Book layout, styling, and colour advice for rooms, homes, and small shops. Start with a consultation, share your goals, and get practical guidance before you refresh or renovate.',
    title: 'Styling & space planning',
    meta: 'Consultation first',
    prompt: 'Space planning, styling, and home makeover support.',
    icon: '/images/categories/icons/interior-decor.webp',
    soft: '#fde68a',
    mid: '#fbbf24',
    accent: '#202048',
    scatter: { top: '44%', right: '1%' },
  },
  'aluminium-steel-works': {
    slug: 'aluminium-steel-works',
    adminSlug: 'aluminium-steel-works',
    label: 'Aluminium & steel',
    heading: 'Need metal work done?',
    blurb:
      'Book aluminium and steel installation, repairs, and fabrication for windows, doors, grills, and custom metal work. Describe the job and schedule a verified fabricator.',
    title: 'Install, repair & fabricate',
    meta: 'Windows, doors & grills',
    prompt: 'Aluminium and steel installation, repairs, and custom fabrication.',
    icon: '/images/categories/icons/aluminium-steel-works.webp',
    soft: '#cbd5e1',
    mid: '#64748b',
    accent: '#1e293b',
    scatter: { bottom: '18%', right: '24%' },
  },
  'pet-grooming': {
    slug: 'pet-grooming',
    adminSlug: 'pet-grooming',
    label: 'Pet grooming',
    heading: 'Pet need a groom?',
    blurb:
      'Book dog or cat grooming at home — baths, trims, and coat care with gentle handling. Share your pet’s breed and needs when you book.',
    title: 'Dog & cat grooming',
    meta: 'Gentle home visits',
    prompt: 'Dog and cat grooming with verified local pet care partners.',
    icon: '/images/categories/icons/pet-grooming.webp',
    soft: '#fde68a',
    mid: '#f59e0b',
    accent: '#b45309',
    scatter: { bottom: '22%', left: '30%' },
  },
  'vehicle-services': {
    slug: 'vehicle-services',
    adminSlug: 'vehicle-services',
    label: 'Vehicle services',
    heading: 'Car or bike need care?',
    blurb:
      'Book car wash & detailing, car repair & maintenance, or bike & scooter service. Share the vehicle type and issue, then pick a convenient slot.',
    title: 'Wash, repair & bike care',
    meta: 'Cars, bikes & scooters',
    prompt: 'Car wash, car repair, and bike & scooter service near you.',
    icon: '/images/categories/icons/vehicle-services.webp',
    soft: '#bfdbfe',
    mid: '#60a5fa',
    accent: '#1d4ed8',
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
  const pageMeta = getServicePageMeta(service.slug);
  const parentSlug = pageMeta?.parentSlug ?? service.slug;
  const visual = categoryCatalog[service.slug] ?? categoryCatalog[parentSlug];
  const label = service.shortName || visual?.label || service.slug;
  const parentIcon =
    pageMeta?.icon ?? visual?.icon ?? categoryCatalog[parentSlug]?.icon ?? '/images/categories/icons/plumbing.webp';

  const fromAdmin = categorySubcategories[service.slug] ?? categorySubcategories[parentSlug];
  const filteredSubs =
    pageMeta?.liveSubSlugs?.length && fromAdmin
      ? fromAdmin.filter((s) => pageMeta.liveSubSlugs!.includes(s.slug))
      : fromAdmin;

  const subcategories: SubCategoryPill[] =
    filteredSubs ??
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
      `Book verified ${service.shortName.toLowerCase()} partners across ${areaName}. Share what you need, pick a time that works, and get clear next steps by phone, WhatsApp, website, or the app.`,
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
    parentSlug: pageMeta?.parentSlug,
    subcategories,
  };
}

export function enrichCategories(services: ServiceLike[] | undefined, areaName = 'Srinagar') {
  return (services ?? []).map((s) => enrichCategory(s, areaName));
}

export function categoryIcon(slug: string) {
  const pageMeta = getServicePageMeta(slug);
  if (pageMeta?.icon) return pageMeta.icon;
  const parent = pageMeta?.parentSlug;
  return (
    categoryCatalog[slug]?.icon ??
    (parent ? categoryCatalog[parent]?.icon : undefined) ??
    '/images/categories/icons/plumbing.webp'
  );
}
