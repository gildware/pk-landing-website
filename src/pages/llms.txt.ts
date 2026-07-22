import type { APIRoute } from 'astro';
import { buildLlmsTxt } from '@/utils/llms';
import { getSiteSettings, getServices, getAreas, getNearMePages } from '@/utils/reader';

export const GET: APIRoute = async () => {
  const site = await getSiteSettings();
  const services = await getServices();
  const areas = await getAreas();
  const nearMePages = await getNearMePages();
  const body = buildLlmsTxt(site, services, areas, false, nearMePages);

  return new Response(body, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
