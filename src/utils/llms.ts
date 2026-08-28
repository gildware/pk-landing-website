import type { AreaEntry, NearMePage, ServiceEntry } from './reader';
import { areaPath } from './areaPaths';
import { siteUrl } from './reader';
import { BOOK_PATH } from './booking';

interface SiteForLlms {
  businessName: string;
  tagline: string;
  description: string;
  phone: string;
  whatsapp: string;
  email: string;
  bookingUrl: string;
  userPlayStoreUrl: string;
  userAppStoreUrl: string;
  providerPlayStoreUrl: string;
  providerAppStoreUrl: string;
  facebookUrl?: string;
  instagramUrl?: string;
  youtubeUrl?: string;
  twitterUrl?: string;
  googleMapsUrl?: string | null;
}

export function buildLlmsTxt(
  site: SiteForLlms,
  services: ServiceEntry[],
  areas: AreaEntry[],
  extended = false,
  nearMePages: NearMePage[] = []
): string {
  const areaNames = areas.map((a) => a.displayName).join(', ');

  const lines: string[] = [
    `# ${site.businessName}`,
    `> ${site.tagline}`,
    '',
    site.description,
    '',
    '## Book & contact',
    `- [Book a service](${siteUrl(BOOK_PATH)}): Online booking form for home services across Kashmir.`,
    `- [Contact us](${siteUrl('/contact')}): Phone ${site.phone}, WhatsApp, and email ${site.email}.`,
    `- [Customer app (Android)](${site.userPlayStoreUrl}): Book, track, and pay from the Panun Kaergar app.`,
    `- [Customer app (iOS)](${site.userAppStoreUrl}): iPhone and iPad app for home service bookings.`,
    `- [Partner app (Android)](${site.providerPlayStoreUrl}): Provider app for Panun Kaergar partners.`,
    `- [Partner app (iOS)](${site.providerAppStoreUrl}): iPhone partner app for Panun Kaergar.`,
    '',
    '## Official profiles',
    `- [Website](${siteUrl('/')}): Official Panun Kaergar website.`,
    site.facebookUrl ? `- [Facebook](${site.facebookUrl}): Official Facebook page.` : '',
    site.instagramUrl ? `- [Instagram](${site.instagramUrl}): Official Instagram.` : '',
    site.youtubeUrl ? `- [YouTube](${site.youtubeUrl}): Official YouTube channel.` : '',
    site.twitterUrl ? `- [X / Twitter](${site.twitterUrl}): Official X account.` : '',
    site.googleMapsUrl ? `- [Google Maps](${site.googleMapsUrl}): Panun Kaergar Private Limited, Srinagar.` : '',
    '',
    '## Services',
    ...services.map((s) => `- [${s.shortName}](${siteUrl(`/services/${s.slug}`)}): ${s.description.trim()}`),
    '',
    '## Service areas',
    ...areas.map(
      (a) =>
        `- [${a.displayName}](${siteUrl(areaPath(a.slug))}): Home services in ${a.displayName}, ${a.region}.`
    ),
  ];

  if (nearMePages.length > 0) {
    lines.push(
      '',
      '## Near me pages',
      ...nearMePages.map(
        (p) =>
          `- [${p.primaryKeyword}](${siteUrl(`/near-me/${p.slug}`)}): High-intent local booking page for ${p.primaryKeyword}.`
      )
    );
  }

  lines.push(
    '',
    '## Help & company',
    `- [Guides & tips](${siteUrl('/guides')}): Practical home-service advice for Kashmir homes.`,
    `- [FAQ](${siteUrl('/faq')}): Full questions and answers on booking, pricing, payment, coverage across Kashmir, and joining as a partner.`,
    `- [Features](${siteUrl('/features')}): Platform features including multi-channel booking, app chat, custom jobs, loyalty rewards, and job tracking.`,
    `- [Why choose Panun Kaergar](${siteUrl('/why-choose-panun-kaergar')}): Clear prices, easy booking, and a company that stays responsible after the visit.`,
    `- [Why choose Panun Kaergar — guide](${siteUrl('/guides/why-choose-panun-kaergar-kashmir')}): In-depth blog on booking home and commercial services from small repairs to large projects in Kashmir.`,
    `- [Become a partner](${siteUrl('/become-a-partner')}): Join as a verified service partner in Kashmir.`,
    '',
    '## Optional',
    `- [Privacy policy](${siteUrl('/privacy')}): How we handle customer data.`,
    `- [Terms of service](${siteUrl('/terms')}): Platform terms for customers and partners.`,
    `- [Extended LLM index](${siteUrl('/llms-full.txt')}): Full service-area page list for AI systems.`,
    `- [Sitemap](${siteUrl('/sitemap.xml')}): Complete URL list (${areaNames}).`
  );

  if (extended) {
    lines.push('', '## Service × area pages');
    for (const service of services) {
      for (const area of areas) {
        lines.push(
          `- [${service.shortName} in ${area.displayName}](${siteUrl(`/services/${service.slug}/${area.slug}`)}): Local SEO page for ${service.shortName.toLowerCase()} in ${area.displayName}.`
        );
      }
    }
  }

  return lines.join('\n');
}
