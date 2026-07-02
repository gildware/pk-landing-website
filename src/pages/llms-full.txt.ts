import type { APIRoute } from 'astro';
import { buildLlmsTxt } from '@/utils/llms';
import { getSiteSettings, getServices, getAreas, getFaqs } from '@/utils/reader';

export const GET: APIRoute = async () => {
  const site = await getSiteSettings();
  const services = await getServices();
  const areas = await getAreas();
  const faqs = await getFaqs();

  let body = buildLlmsTxt(site, services, areas, true);

  body += '\n\n## Frequently asked questions\n';
  for (const faq of faqs) {
    body += `\n### ${faq.questionText}\n${faq.answer}\n`;
  }

  return new Response(body, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
