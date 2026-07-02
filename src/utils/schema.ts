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
    address: {
      '@type': 'PostalAddress',
      addressLocality: 'Srinagar',
      addressRegion: 'Jammu & Kashmir',
      addressCountry: 'IN',
      streetAddress: site.address,
    },
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
    potentialAction: {
      '@type': 'SearchAction',
      target: `${siteUrl('/services')}?q={search_term_string}`,
      'query-input': 'required name=search_term_string',
    },
  };
}

export function localBusinessSchema(
  site: SiteForSchema,
  areas: AreaEntry[],
  services: ServiceEntry[],
  testimonials: TestimonialForSchema[]
) {
  const avgRating =
    testimonials.length > 0
      ? testimonials.reduce((sum, t) => sum + t.rating, 0) / testimonials.length
      : null;

  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'HomeAndConstructionBusiness',
    name: site.businessName,
    url: siteUrl('/'),
    description: site.description,
    telephone: site.phone,
    email: site.email,
    priceRange: '₹₹',
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

  if (avgRating && testimonials.length > 0) {
    schema.aggregateRating = {
      '@type': 'AggregateRating',
      ratingValue: avgRating.toFixed(1),
      reviewCount: testimonials.length,
      bestRating: 5,
      worstRating: 1,
    };
  }

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
      name: `${site.businessName} — Provider App`,
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

export function serviceSchema(service: ServiceEntry, site: SiteForSchema) {
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
    areaServed: {
      '@type': 'City',
      name: 'Srinagar',
    },
    url: siteUrl(`/services/${service.slug}`),
  };
}

export function serviceAreaPageSchema(
  service: ServiceEntry,
  area: AreaEntry,
  site: SiteForSchema,
  pageUrl: string
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: `${service.shortName} in ${area.displayName}`,
    description: `${service.shortName} services in ${area.displayName} by ${site.businessName}.`,
    provider: {
      '@type': 'LocalBusiness',
      name: site.businessName,
      telephone: site.phone,
      url: siteUrl('/'),
    },
    areaServed: {
      '@type': 'City',
      name: area.displayName,
    },
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

export function articleSchema(post: {
  title: string;
  description: string;
  slug: string;
  publishedAt: string;
}) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: post.title,
    description: post.description,
    datePublished: post.publishedAt,
    url: siteUrl(`/blog/${post.slug}`),
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
