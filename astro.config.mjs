import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import markdoc from '@astrojs/markdoc';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';
import vercel from '@astrojs/vercel/serverless';

/** When true, enable Keystatic admin at /keystatic (dev or CMS deploy only). */
const isCms = process.env.KEYSTATIC_CMS === '1';
/** Vercel adapter is only needed for CMS production build — not local dev. */
const isCmsBuild = isCms && process.argv.includes('build');

const site = process.env.PUBLIC_SITE_URL || 'https://panunkaergar.com';

const viteConfig = {
  server: {
    // Allow ngrok (and similar) tunnels — subdomain changes each session.
    allowedHosts: ['.ngrok-free.app', '.ngrok.io', 'localhost'],
    host: true,
  },
  ...(isCms
    ? {
        optimizeDeps: {
          include: ['react', 'react-dom', 'react/jsx-runtime', '@keystatic/core/ui'],
        },
        ssr: {
          noExternal: ['@keystatic/core', '@keystatic/astro'],
        },
      }
    : {}),
};

export default defineConfig({
  site,
  output: isCms ? 'hybrid' : 'static',
  adapter: isCmsBuild ? vercel() : undefined,
  integrations: [tailwind(), markdoc(), ...(isCms ? [react(), keystatic()] : [])],
  vite: viteConfig,
  redirects: {
    '/become-a-provider': '/become-a-partner',
    '/book': '/book-a-home-service',
    '/areas': '/service-areas',
    '/areas/srinagar': '/service-areas/home-services-in-srinagar',
    '/areas/budgam': '/service-areas/home-services-in-budgam',
    '/areas/ganderbal': '/service-areas/home-services-in-ganderbal',
    '/areas/baramulla': '/service-areas/home-services-in-baramulla',
    '/areas/bandipora': '/service-areas/home-services-in-bandipora',
    '/areas/kupwara': '/service-areas/home-services-in-kupwara',
    '/areas/anantnag': '/service-areas/home-services-in-anantnag',
    '/areas/kulgam': '/service-areas/home-services-in-kulgam',
    '/areas/pulwama': '/service-areas/home-services-in-pulwama',
    '/areas/shopian': '/service-areas/home-services-in-shopian',
  },
});
