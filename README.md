# Panun Kaergar — Marketing Website

SEO-focused static marketing site. **Build status: development complete** — ready for content review and deploy.

## Quick start

```bash
cd panun-marketing
npm install
npm run dev      # preview at http://localhost:4321
npm run build    # static output in dist/
npm run preview  # preview production build
```

## What's included

### Pages (25 built)
| Section | Routes |
|---------|--------|
| Home | `/` — hero, services, how it works, testimonials, app download |
| Services | `/services`, `/services/[slug]` |
| **SEO local pages** | `/services/[slug]/srinagar` × 6 (full custom copy each) |
| Areas | `/areas`, `/areas/srinagar` |
| Company | `/about`, `/contact`, `/how-it-works`, `/faq` |
| Apps | `/download`, `/become-a-provider` |
| Legal | `/privacy`, `/terms` |
| AI/SEO | `/llms.txt`, `/llms-full.txt`, `/sitemap.xml`, `/robots.txt` |

### Features
- Mobile navigation menu
- WhatsApp floating button (all pages)
- JSON-LD schema (Organization, LocalBusiness, Service, FAQ, Breadcrumb)
- Open Graph + Twitter cards + default OG image
- CMS-editable content in `content/` (YAML + Markdoc)
- Testimonials section
- App download promo section

## Edit content

### Option A — Visual CMS (for your team)

Run locally:

```bash
npm run cms
# Open http://localhost:4321/keystatic
```

For non-technical staff, deploy the admin to Vercel — see **[CMS.md](./CMS.md)** for full setup (`cms.panunkaergar.com` → GitHub → Cloudflare auto-rebuild).

### Option B — Edit files directly (developers)

| File / folder | Edit this |
|---------------|-----------|
| `content/site/index.yaml` | Phone, WhatsApp, email, app URLs, hero |
| `content/services/*/` | Service categories |
| `content/areas/*/` | Cities/zones |
| `content/service-area-pages/*/` | SEO pages (e.g. plumbing in Srinagar) |
| `content/testimonials/*/` | Customer quotes |
| `content/faqs/*/` | Global FAQs |
| `content/blog/*/` | Blog posts |

After editing: `npm run build`

**Public site build (fast static):** `npm run build`  
**CMS admin deploy (Vercel only):** `npm run build:cms`

## Before launch — update these placeholders

In `content/site/index.yaml`:

- [x] **phone / whatsapp / email** — synced from [panunkaergar.com](https://panunkaergar.com/)
- [x] **userAppStoreUrl** — [App Store](https://apps.apple.com/in/app/panun-kaergar/id6504860745)
- [x] **facebookUrl / instagramUrl** — synced

Legal:
- [ ] Review `/privacy`, `/terms`, `/refund`, and `/cancellation` with your lawyer

## Deploy

See deploy steps in previous plan:
1. Push to GitHub
2. Cloudflare Pages → build `npm run build` → output `dist`
3. Env: `PUBLIC_SITE_URL=https://panunkaergar.com`
4. Point DNS

## Project structure

```
panun-marketing/
  content/              ← all editable content
  public/               ← logo, favicon, og-image, robots.txt
  src/
    components/         ← Header, Footer, Hero, Testimonials, etc.
    layouts/            ← SEO shell
    pages/              ← routes
    utils/              ← CMS reader, schema, llms.txt
  keystatic.config.ts   ← content schema
```
