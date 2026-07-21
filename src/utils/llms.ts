import type { AreaEntry, ServiceEntry } from './reader';
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
    `- [Book a service](${siteUrl(BOOK_PATH)}): Online booking form for home services across Kashmir.`,
    `- [Contact us](${siteUrl('/contact')}): Phone ${site.phone}, WhatsApp, and email ${site.email}.`,
    `- [Customer app (Android)](${site.userPlayStoreUrl}): Book, track, and pay from the Panun Kaergar app.`,
    `- [Customer app (iOS)](${site.userAppStoreUrl}): iPhone and iPad app for home service bookings.`,
    '',
    '## Services',
    ...services.map((s) => `- [${s.shortName}](${siteUrl(`/services/${s.slug}`)}): ${s.description.trim()}`),
    '',
    '## Service areas',
    ...areas.map(
      (a) =>
        `- [${a.displayName}](${siteUrl(areaPath(a.slug))}): Home services in ${a.displayName}, ${a.region}.`
    ),
    '',
    '## Help & company',
    `- [FAQ](${siteUrl('/faq')}): Common questions about booking and partners.`,
    `- [Become a partner](${siteUrl('/become-a-partner')}): Join as a verified service partner in Kashmir.`,
    '',
    '## Optional',
    `- [Privacy policy](${siteUrl('/privacy')}): How we handle customer data.`,
    `- [Terms of service](${siteUrl('/terms')}): Platform terms for customers and partners.`,
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
