import type { APIRoute } from 'astro';
import { siteUrl, getServices, getAllServices, getAreas, getNearMePages } from '@/utils/reader';
import { SERVICE_AREAS_PATH, areaPath } from '@/utils/areaPaths';

const staticPaths = [
  '/',
  '/book-a-home-service',
  '/services',
  '/near-me',
  SERVICE_AREAS_PATH,
  '/about',
  '/contact',
  '/download',
  '/become-a-partner',
  '/faq',
  '/privacy',
  '/terms',
  '/refund',
  '/cancellation',
  '/llms.txt',
  '/llms-full.txt',
];

export const GET: APIRoute = async () => {
  const services = await getServices();
  const allServicePages = await getAllServices();
  const areas = await getAreas();
  const nearMePages = await getNearMePages();

  const urls = [
    ...staticPaths,
    ...allServicePages.map((s) => `/services/${s.slug}`),
    ...areas.map((a) => areaPath(a.slug)),
    ...services.flatMap((s) => areas.map((a) => `/services/${s.slug}/${a.slug}`)),
    ...nearMePages.map((p) => `/near-me/${p.slug}`),
  ];

  const today = new Date().toISOString().slice(0, 10);
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    (path) => `  <url>
    <loc>${siteUrl(path)}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${path.includes('/services/') || path.includes('/near-me/') ? 'weekly' : 'monthly'}</changefreq>
    <priority>${path === '/' ? '1.0' : path.split('/').length <= 2 ? '0.8' : '0.7'}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(body, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
