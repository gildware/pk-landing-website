import type { AreaEntry, ServiceEntry } from './reader';
import { siteUrl } from './reader';

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
}

export function buildLlmsTxt(
  site: SiteForLlms,
  services: ServiceEntry[],
  areas: AreaEntry[],
  extended = false
): string {
  const areaNames = areas.map((a) => a.displayName).join(', ');

  const lines: string[] = [
    `# ${site.businessName}`,
    `> ${site.tagline}`,
    '',
    site.description,
    '',
    '## Book & contact',
    `- [Book a service](${siteUrl('/book')}): Online booking form for home services in Srinagar.`,
    `- [Contact us](${siteUrl('/contact')}): Phone ${site.phone}, WhatsApp, and email ${site.email}.`,
    `- [Customer app (Android)](${site.userPlayStoreUrl}): Book, track, and pay from the Panun Kaergar app.`,
    `- [Customer app (iOS)](${site.userAppStoreUrl}): iPhone and iPad app for home service bookings.`,
    '',
    '## Services',
    ...services.map(
      (s) =>
        `- [${s.shortName}](${siteUrl(`/services/${s.slug}`)}): ${s.description.slice(0, 110).trim()}…`
    ),
    '',
    '## Service areas',
    ...areas.map(
      (a) =>
        `- [${a.displayName}](${siteUrl(`/areas/${a.slug}`)}): Home services in ${a.displayName}, ${a.region}.`
    ),
    '',
    '## Help & company',
    `- [How it works](${siteUrl('/how-it-works')}): Book by phone, WhatsApp, website form, or app.`,
    `- [FAQ](${siteUrl('/faq')}): Common questions about booking and providers.`,
    `- [Become a provider](${siteUrl('/become-a-provider')}): Join as a verified service provider in Kashmir.`,
    '',
    '## Optional',
    `- [Blog](${siteUrl('/blog')}): Guides for homeowners in Srinagar.`,
    `- [Privacy policy](${siteUrl('/privacy')}): How we handle customer data.`,
    `- [Terms of service](${siteUrl('/terms')}): Platform terms for customers and providers.`,
    `- [Extended LLM index](${siteUrl('/llms-full.txt')}): Full service-area page list for AI systems.`,
    `- [Sitemap](${siteUrl('/sitemap.xml')}): Complete URL list (${areaNames}).`,
  ];

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
