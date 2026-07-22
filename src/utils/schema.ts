import { siteUrl, type AreaEntry, type ServiceEntry } from './reader';

interface FaqItem {
  question: string;
  answer: string;
}

interface SiteForSchema {
  businessName: string;
  phone: string;
  email: string;
  address: string;
  description: string;
  bookingUrl: string;
  userPlayStoreUrl: string;
  userAppStoreUrl: string;
  providerPlayStoreUrl?: string;
  facebookUrl?: string;
  instagramUrl?: string;
  postalCode?: string | null;
  latitude?: string | null;
  longitude?: string | null;
  googleMapsUrl?: string | null;
  businessHours?: string | null;
}

const WEEKDAYS = [
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
] as const;

const EVERY_DAY = [...WEEKDAYS, 'Sunday'] as const;

function postalAddress(site: SiteForSchema) {
  return {
    '@type': 'PostalAddress',
    streetAddress: site.address,
    addressLocality: 'Srinagar',
    addressRegion: 'Jammu and Kashmir',
    postalCode: site.postalCode || '190008',
    addressCountry: 'IN',
  };
}

function openingHoursSpecs() {
  return [
    {
      '@type': 'OpeningHoursSpecification',
      name: 'Office',
      dayOfWeek: [...WEEKDAYS],
      opens: '10:00',
      closes: '18:00',
    },
    {
      '@type': 'OpeningHoursSpecification',
      name: 'Call center support',
      dayOfWeek: [...EVERY_DAY],
      opens: '10:00',
      closes: '22:00',
    },
  ];
}

interface TestimonialForSchema {
  customerName: string;
  quote: string;
  rating: number;
  location: string;
}

export function organizationSchema(site: SiteForSchema) {
  const sameAs = [
    site.userPlayStoreUrl,
    site.userAppStoreUrl,
    site.providerPlayStoreUrl,
    site.facebookUrl,
    site.instagramUrl,
  ].filter(Boolean);

  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: site.businessName,
    url: siteUrl('/'),
    description: site.description,
    telephone: site.phone,
    email: site.email,
    address: postalAddress(site),
    ...(site.googleMapsUrl ? { hasMap: site.googleMapsUrl } : {}),
    sameAs,
  };
}

export function websiteSchema(site: SiteForSchema) {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: site.businessName,
    url: siteUrl('/'),
    description: site.description,
  };
}

export function localBusinessSchema(
  site: SiteForSchema,
  areas: AreaEntry[],
  services: ServiceEntry[]
) {
  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'HomeAndConstructionBusiness',
    name: site.businessName,
    url: siteUrl('/'),
    description: site.description,
    telephone: site.phone,
    email: site.email,
    priceRange: '₹₹',
    image: siteUrl('/logo-square.png'),
    address: postalAddress(site),
    openingHoursSpecification: openingHoursSpecs(),
    areaServed: areas.map((area) => ({
      '@type': 'City',
      name: area.displayName,
    })),
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: 'Home Services',
      itemListElement: services.map((service, index) => ({
        '@type': 'Offer',
        position: index + 1,
        itemOffered: {
          '@type': 'Service',
          name: service.shortName,
          url: siteUrl(`/services/${service.slug}`),
        },
      })),
    },
  };

  if (site.latitude && site.longitude) {
    schema.geo = {
      '@type': 'GeoCoordinates',
      latitude: site.latitude,
      longitude: site.longitude,
    };
  }

  if (site.googleMapsUrl) {
    schema.hasMap = site.googleMapsUrl;
  }

  // AggregateRating omitted until backed by a verified source (e.g. Google Business Profile).
  // On-page testimonials remain for users; do not derive schema ratings from marketing quotes.

  return schema;
}

export function mobileApplicationsSchema(site: SiteForSchema) {
  return [
    {
      '@context': 'https://schema.org',
      '@type': 'MobileApplication',
      name: `${site.businessName} — Customer App`,
      operatingSystem: 'Android, iOS',
      applicationCategory: 'BusinessApplication',
      offers: { '@type': 'Offer', price: '0', priceCurrency: 'INR' },
      url: site.userPlayStoreUrl,
    },
    {
      '@context': 'https://schema.org',
      '@type': 'MobileApplication',
      name: `${site.businessName} — Partner App`,
      operatingSystem: 'Android, iOS',
      applicationCategory: 'BusinessApplication',
      offers: { '@type': 'Offer', price: '0', priceCurrency: 'INR' },
      url: site.providerPlayStoreUrl,
    },
  ];
}

export function reviewSchemas(testimonials: TestimonialForSchema[], site: SiteForSchema) {
  return testimonials.slice(0, 5).map((t) => ({
    '@context': 'https://schema.org',
    '@type': 'Review',
    author: { '@type': 'Person', name: t.customerName },
    reviewRating: {
      '@type': 'Rating',
      ratingValue: t.rating,
      bestRating: 5,
    },
    reviewBody: t.quote,
    itemReviewed: {
      '@type': 'LocalBusiness',
      name: site.businessName,
      address: t.location,
    },
  }));
}

export function serviceSchema(service: ServiceEntry, site: SiteForSchema, areas?: AreaEntry[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: service.shortName,
    description: service.description,
    provider: {
      '@type': 'Organization',
      name: site.businessName,
      url: siteUrl('/'),
    },
    areaServed: areas?.length
      ? areas.map((area) => ({
          '@type': 'City',
          name: area.displayName,
        }))
      : {
          '@type': 'AdministrativeArea',
          name: 'Kashmir',
        },
    url: siteUrl(`/services/${service.slug}`),
  };
}

export function nearMeServiceSchema(
  page: {
    h1: string;
    intro: string;
    primaryKeyword: string;
    parentServiceSlug: string;
  },
  service: ServiceEntry,
  site: SiteForSchema,
  areas: AreaEntry[],
  pageUrl: string
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: page.h1,
    alternateName: page.primaryKeyword,
    description: page.intro,
    provider: {
      '@type': 'LocalBusiness',
      name: site.businessName,
      telephone: site.phone,
      url: siteUrl('/'),
    },
    serviceType: service.shortName,
    areaServed: areas.length
      ? areas.map((area) => ({
          '@type': 'AdministrativeArea',
          name: area.displayName,
        }))
      : {
          '@type': 'AdministrativeArea',
          name: 'Kashmir',
        },
    url: pageUrl,
    isRelatedTo: {
      '@type': 'Service',
      name: service.shortName,
      url: siteUrl(`/services/${service.slug}`),
    },
  };
}

export function serviceAreaPageSchema(
  service: ServiceEntry,
  area: AreaEntry,
  site: SiteForSchema,
  pageUrl: string,
  description?: string
) {
  const neighborhoods = area.neighborhoods || [];
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: `${service.shortName} in ${area.displayName}`,
    description:
      description ||
      `${service.shortName} services in ${area.displayName} by ${site.businessName}.`,
    provider: {
      '@type': 'LocalBusiness',
      name: site.businessName,
      telephone: site.phone,
      url: siteUrl('/'),
    },
    areaServed: [
      {
        '@type': 'AdministrativeArea',
        name: area.displayName,
      },
      ...neighborhoods.slice(0, 20).map((name) => ({
        '@type': 'Place',
        name,
        containedInPlace: {
          '@type': 'AdministrativeArea',
          name: area.displayName,
        },
      })),
    ],
    serviceType: service.shortName,
    url: pageUrl,
  };
}

export function faqSchema(faqs: FaqItem[]) {
  if (!faqs.length) return null;
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  };
}

export function breadcrumbSchema(items: { name: string; path: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: siteUrl(item.path),
    })),
  };
}

export function itemListSchema(
  items: { name: string; url: string; description?: string }[],
  listName: string
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: listName,
    numberOfItems: items.length,
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      url: item.url,
      ...(item.description ? { description: item.description } : {}),
    })),
  };
}

/** LocalBusiness + Place markup for a district service-area page. */
export function areaLocalBusinessSchema(
  site: SiteForSchema,
  area: AreaEntry,
  pagePath: string,
  services: ServiceEntry[]
) {
  const neighborhoods = area.neighborhoods || [];

  return {
    '@context': 'https://schema.org',
    '@type': 'HomeAndConstructionBusiness',
    name: `${site.businessName} — ${area.displayName}`,
    url: siteUrl(pagePath),
    description: area.seoDescription || area.description,
    telephone: site.phone,
    email: site.email,
    priceRange: '₹₹',
    image: siteUrl(`/images/areas/${area.slug}.webp`),
    address: {
      '@type': 'PostalAddress',
      addressLocality: area.displayName,
      addressRegion: 'Jammu & Kashmir',
      addressCountry: 'IN',
    },
    areaServed: [
      {
        '@type': 'AdministrativeArea',
        name: area.displayName,
        containedInPlace: {
          '@type': 'AdministrativeArea',
          name: 'Kashmir',
          containedInPlace: {
            '@type': 'State',
            name: 'Jammu & Kashmir',
          },
        },
      },
      ...neighborhoods.map((name) => ({
        '@type': 'Place',
        name,
        containedInPlace: {
          '@type': 'City',
          name: area.displayName,
        },
      })),
    ],
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: `Home services in ${area.displayName}`,
      itemListElement: services.map((service, index) => ({
        '@type': 'Offer',
        position: index + 1,
        itemOffered: {
          '@type': 'Service',
          name: `${service.shortName} in ${area.displayName}`,
          url: siteUrl(`/services/${service.slug}/${area.slug}`),
        },
      })),
    },
    parentOrganization: {
      '@type': 'Organization',
      name: site.businessName,
      url: siteUrl('/'),
    },
  };
}
