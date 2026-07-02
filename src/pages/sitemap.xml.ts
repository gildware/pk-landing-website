import type { APIRoute } from 'astro';
import { siteUrl, getServices, getAreas, getBlogPosts } from '@/utils/reader';

const staticPaths = [
  '/',
  '/book',
  '/services',
  '/areas',
  '/about',
  '/contact',
  '/download',
  '/become-a-provider',
  '/how-it-works',
  '/faq',
  '/blog',
  '/privacy',
  '/terms',
  '/refund',
  '/cancellation',
  '/llms.txt',
  '/llms-full.txt',
];

export const GET: APIRoute = async () => {
  const services = await getServices();
  const areas = await getAreas();
  const posts = await getBlogPosts();

  const urls = [
    ...staticPaths,
    ...services.map((s) => `/services/${s.slug}`),
    ...areas.map((a) => `/areas/${a.slug}`),
    ...services.flatMap((s) => areas.map((a) => `/services/${s.slug}/${a.slug}`)),
    ...posts.map((p) => `/blog/${p.slug}`),
  ];

  const today = new Date().toISOString().slice(0, 10);
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    (path) => `  <url>
    <loc>${siteUrl(path)}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${path.includes('/services/') ? 'weekly' : 'monthly'}</changefreq>
    <priority>${path === '/' ? '1.0' : path.split('/').length <= 2 ? '0.8' : '0.7'}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(body, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
