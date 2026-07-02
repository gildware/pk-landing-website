# Content management for your team

The public website (`panunkaergar.com`) stays **100% static HTML** — fast on Cloudflare CDN.

Your team edits content in a **separate admin panel** (Keystatic). Saves go to GitHub → Cloudflare rebuilds the site automatically.

```
Team browser  →  cms.panunkaergar.com  →  GitHub (content/ files)  →  Cloudflare Pages  →  panunkaergar.com
     ↑                    ↑                         ↑                              ↑
  non-technical      visual editor            version history              static, super fast
```

---

## What your team can edit (no code)

Open the CMS and use the sidebar:

| Section | Examples |
|---------|----------|
| **Site Settings** | Phone, WhatsApp, email, app store links, hero text |
| **Homepage Sections** | How it works steps, platform features |
| **Services** | Plumbing, electrician, AC, cleaning, etc. |
| **Service Areas** | Srinagar neighborhoods |
| **Service × Area Pages** | SEO pages like “Plumbing in Srinagar” |
| **Testimonials** | Customer quotes |
| **Blog Posts** | Articles |
| **FAQs** | Questions & answers |

After saving, wait 1–2 minutes for the live site to update (automatic rebuild).

---

## For developers — run CMS locally

```bash
cd panun-marketing
npm install
npm run cms
```

Open **http://localhost:4321/keystatic**

Edits save to the `content/` folder on your machine. Run `npm run build` to preview the static site.

Preview the marketing site only (no admin):

```bash
npm run dev
```

---

## For your team — hosted CMS (recommended)

Deploy the admin once to **Vercel** (free tier is enough). The marketing site stays on **Cloudflare Pages**.

### Step 1 — Push code to GitHub

The repo must be on GitHub (private is fine). Your team needs **write access** to the repo.

### Step 2 — Deploy CMS to Vercel

1. Go to [vercel.com](https://vercel.com) → **Add New Project** → import the same GitHub repo.
2. Project name: e.g. `panun-marketing-cms`
3. **Build command:** `npm run build:cms`
4. **Environment variables:**
   - `KEYSTATIC_CMS` = `1`
   - `KEYSTATIC_GITHUB_REPO` = `your-github-username/panun-marketing` (your actual repo)
   - `PUBLIC_SITE_URL` = `https://panunkaergar.com`
5. Deploy.

### Step 3 — Connect Keystatic to GitHub

1. Visit `https://your-cms-project.vercel.app/keystatic`
2. Click **Login with GitHub** and follow the setup (create GitHub App, grant repo access).
3. Copy the env vars Keystatic generates into Vercel → Project → Settings → Environment Variables:
   - `KEYSTATIC_GITHUB_CLIENT_ID`
   - `KEYSTATIC_GITHUB_CLIENT_SECRET`
   - `KEYSTATIC_SECRET`
   - `PUBLIC_KEYSTATIC_GITHUB_APP_SLUG`
4. Redeploy the Vercel project.

### Step 4 — Custom domain (optional)

In Vercel → Domains → add `cms.panunkaergar.com`.

In your GitHub App settings, add callback URL:
`https://cms.panunkaergar.com/api/keystatic/github/oauth/callback`

### Step 5 — Auto-publish to live site

On **Cloudflare Pages** (marketing site):

1. Connect the same GitHub repo
2. Build command: `npm run build`
3. Output directory: `dist`
4. Enable **Build on push** — when your team saves in the CMS, GitHub gets new commits and Cloudflare rebuilds automatically.

---

## Team instructions (share this)

1. Go to **https://cms.panunkaergar.com/keystatic** (or your Vercel URL)
2. Sign in with GitHub (account must have repo access)
3. Pick a section (e.g. **Site Settings** or **Services**)
4. Edit fields in the form — same as filling a Google Form
5. Click **Save**
6. Live site updates in ~1–2 minutes

**Do not** edit YAML files in GitHub directly unless you know what you're doing — use the CMS instead.

---

## Why two deploys?

| | Marketing site | CMS admin |
|--|----------------|-----------|
| **URL** | panunkaergar.com | cms.panunkaergar.com |
| **Host** | Cloudflare Pages | Vercel |
| **Output** | Static HTML (fast) | Server for saving edits |
| **Visitors** | Everyone | Your team only |

The CMS never runs on the public site, so performance stays maximum.

---

## Troubleshooting

**Blank `/keystatic` page** — Stop the server, clear cache, restart:

```bash
rm -rf node_modules/.vite .astro
npm run cms
```

Open **http://127.0.0.1:4321/keystatic** (use `127.0.0.1`, not `localhost`). If still blank, hard-refresh (Cmd+Shift+R).

**“Can't log in to CMS”** — GitHub account needs write access to the repo. Check GitHub App is installed on the repo.

**“Saved but site didn't update”** — Check Cloudflare Pages build logs. Ensure CMS commits are on the branch Cloudflare watches (usually `main`).

**“Blog post not showing”** — Ensure **Published** is checked and click Save again.
