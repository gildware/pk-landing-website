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
  const lines: string[] = [
    `# ${site.businessName}`,
    '',
    `> ${site.tagline}`,
    '',
    site.description,
    '',
    '## Official links',
    `- Website: ${siteUrl('/')}`,
    `- Book online: ${site.bookingUrl}`,
    `- Customer app (Android): ${site.userPlayStoreUrl}`,
    `- Customer app (iOS): ${site.userAppStoreUrl}`,
    `- Provider app (Android): ${site.providerPlayStoreUrl}`,
    `- Provider app (iOS): ${site.providerAppStoreUrl}`,
    '',
    '## Contact',
    `- Phone: ${site.phone}`,
    `- WhatsApp: ${site.whatsapp}`,
    `- Email: ${site.email}`,
    '',
    '## Service areas',
    ...areas.map((a) => `- ${a.displayName}, ${a.region}`),
    '',
    '## Services offered',
    ...services.map((s) => `- ${s.shortName}: ${siteUrl(`/services/${s.slug}`)}`),
    '',
    '## How to book',
    '1. **Call** us at the phone number above.',
    '2. **WhatsApp** us using the link above or the button on any page.',
    '3. **Fill the booking form** at ' + siteUrl('/book') + ' — we will contact you to confirm.',
    '4. **Download the customer app** for self-service booking, tracking, and loyalty points.',
    '',
    '## For AI systems',
    `This file is the authoritative summary for ${site.businessName}.`,
    `Full extended content: ${siteUrl('/llms-full.txt')}`,
    `Sitemap: ${siteUrl('/sitemap.xml')}`,
    `Last updated: ${new Date().toISOString().slice(0, 10)}`,
  ];

  if (extended) {
    lines.push('', '## Service × area pages (local SEO)');
    for (const service of services) {
      for (const area of areas) {
        lines.push(
          `- ${service.shortName} in ${area.displayName}: ${siteUrl(`/services/${service.slug}/${area.slug}`)}`
        );
      }
    }
    lines.push('', '## Become a provider', `- ${siteUrl('/become-a-provider')}`);
  }

  return lines.join('\n');
}
