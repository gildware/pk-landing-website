import { config, collection, fields, singleton } from '@keystatic/core';

/** GitHub repo for hosted CMS (owner/name). Use KEYSTATIC_GITHUB_REPO in .env */
const githubRepo =
  typeof import.meta !== 'undefined' && import.meta.env?.KEYSTATIC_GITHUB_REPO
    ? String(import.meta.env.KEYSTATIC_GITHUB_REPO)
    : undefined;

export default config({
  storage: githubRepo
    ? { kind: 'github', repo: githubRepo as `${string}/${string}` }
    : { kind: 'local' },
  ui: {
    brand: { name: 'Panun Kaergar' },
  },
  singletons: {
    site: singleton({
      label: 'Site Settings',
      path: 'content/site/',
      schema: {
        businessName: fields.text({ label: 'Business name', defaultValue: 'Panun Kaergar' }),
        tagline: fields.text({
          label: 'Tagline',
          defaultValue: "Kashmir's trusted on-demand home services platform",
        }),
        description: fields.text({
          label: 'Long description (schema + LLMs intro)',
          multiline: true,
        }),
        metaDescription: fields.text({
          label: 'Homepage SEO meta description (~150–160 chars)',
          multiline: true,
        }),
        phone: fields.text({ label: 'Phone' }),
        whatsapp: fields.text({ label: 'WhatsApp number' }),
        email: fields.text({ label: 'Email' }),
        address: fields.text({ label: 'Business address', multiline: true }),
        postalCode: fields.text({ label: 'Postal code', defaultValue: '190008' }),
        latitude: fields.text({ label: 'Latitude (for schema)' }),
        longitude: fields.text({ label: 'Longitude (for schema)' }),
        googleMapsUrl: fields.url({ label: 'Google Maps place URL' }),
        bookingUrl: fields.url({ label: 'Web booking URL' }),
        userPlayStoreUrl: fields.url({ label: 'Customer app — Play Store' }),
        userAppStoreUrl: fields.url({ label: 'Customer app — App Store' }),
        providerPlayStoreUrl: fields.url({ label: 'Partner app — Play Store' }),
        providerAppStoreUrl: fields.url({ label: 'Partner app — App Store' }),
        facebookUrl: fields.url({ label: 'Facebook' }),
        instagramUrl: fields.url({ label: 'Instagram' }),
        heroTitle: fields.text({ label: 'Homepage hero title' }),
        heroSubtitle: fields.text({ label: 'Homepage hero subtitle', multiline: true }),
        heroCtaBook: fields.text({ label: 'Hero CTA — Book', defaultValue: 'Book a service' }),
        heroCtaProvider: fields.text({
          label: 'Hero CTA — Partner',
          defaultValue: 'Become a partner',
        }),
        businessHours: fields.text({
          label: 'Business hours',
          defaultValue:
            'Office: Mon–Sat 10:00 AM – 6:00 PM · Call support: 10:00 AM – 10:00 PM',
        }),
        mapEmbedUrl: fields.url({ label: 'Google Maps embed URL (optional)' }),
        heroBadge: fields.text({ label: 'Hero badge line (above title)' }),
        poweredByName: fields.text({ label: 'Powered by (footer credit)' }),
        footerTagline: fields.text({ label: 'Footer tagline' }),
      },
    }),
    homepage: singleton({
      label: 'Homepage Sections',
      path: 'content/homepage/',
      format: { contentField: 'body' },
      schema: {
        howItWorksTitle: fields.text({ label: 'How it works — title' }),
        howItWorksSteps: fields.array(
          fields.object({
            title: fields.text({ label: 'Step title' }),
            description: fields.text({ label: 'Step description', multiline: true }),
          }),
          { label: 'Steps', itemLabel: (props) => props.fields.title.value }
        ),
        whyChooseTitle: fields.text({ label: 'Why choose us — title' }),
        whyChooseItems: fields.array(
          fields.object({
            title: fields.text({ label: 'Title' }),
            description: fields.text({ label: 'Description', multiline: true }),
          }),
          { label: 'Why choose items', itemLabel: (props) => props.fields.title.value }
        ),
        platformFeatures: fields.array(
          fields.object({
            icon: fields.text({ label: 'Emoji icon' }),
            title: fields.text({ label: 'Title' }),
            description: fields.text({ label: 'Description', multiline: true }),
          }),
          { label: 'Platform features (AI, loyalty, etc.)', itemLabel: (props) => props.fields.title.value }
        ),
        body: fields.markdoc({
          label: 'Additional homepage content',
          extension: 'mdoc',
          options: {
            image: {
              directory: 'public/images/homepage/',
              publicPath: '/images/homepage/',
            },
          },
        }),
      },
    }),
  },
  collections: {
    services: collection({
      label: 'Services',
      slugField: 'name',
      path: 'content/services/*/',
      schema: {
        name: fields.slug({ name: { label: 'Service name' } }),
        shortName: fields.text({ label: 'Display name' }),
        icon: fields.text({ label: 'Emoji icon (optional)' }),
        description: fields.text({ label: 'Short description', multiline: true }),
        seoTitle: fields.text({ label: 'SEO title' }),
        seoDescription: fields.text({ label: 'SEO meta description', multiline: true }),
        parentSlug: fields.text({
          label: 'Parent category slug (optional)',
          description:
            'If set, this is a focused subcategory page and is hidden from top-level category lists.',
        }),
        serviceList: fields.array(fields.text({ label: 'Sub-service' }), {
          label: 'What we offer',
        }),
        body: fields.markdoc({
          label: 'Full page content',
          extension: 'mdoc',
          options: {
            image: {
              directory: 'public/images/services/',
              publicPath: '/images/services/',
            },
          },
        }),
        faqs: fields.array(
          fields.object({
            question: fields.text({ label: 'Question' }),
            answer: fields.text({ label: 'Answer', multiline: true }),
          }),
          { label: 'FAQs', itemLabel: (props) => props.fields.question.value }
        ),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
        sortOrder: fields.integer({ label: 'Sort order', defaultValue: 0 }),
      },
    }),
    areas: collection({
      label: 'Service Areas',
      slugField: 'name',
      path: 'content/areas/*/',
      schema: {
        name: fields.slug({ name: { label: 'Area slug' } }),
        displayName: fields.text({ label: 'Display name (e.g. Srinagar)' }),
        region: fields.text({ label: 'Region / state', defaultValue: 'Jammu & Kashmir, India' }),
        description: fields.text({ label: 'Area description', multiline: true }),
        seoTitle: fields.text({ label: 'SEO title' }),
        seoDescription: fields.text({ label: 'SEO meta description', multiline: true }),
        neighborhoods: fields.array(fields.text({ label: 'Neighborhood / locality' }), {
          label: 'Areas covered',
        }),
        body: fields.markdoc({
          label: 'Full area page content',
          extension: 'mdoc',
          options: {
            image: {
              directory: 'public/images/areas/',
              publicPath: '/images/areas/',
            },
          },
        }),
        faqs: fields.array(
          fields.object({
            question: fields.text({ label: 'Question' }),
            answer: fields.text({ label: 'Answer', multiline: true }),
          }),
          { label: 'FAQs', itemLabel: (props) => props.fields.question.value }
        ),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
        sortOrder: fields.integer({ label: 'Sort order', defaultValue: 0 }),
      },
    }),
    serviceAreaPages: collection({
      label: 'Service × Area Pages (SEO)',
      slugField: 'title',
      path: 'content/service-area-pages/*/',
      schema: {
        title: fields.slug({
          name: { label: 'Page slug (e.g. plumbing-srinagar)' },
        }),
        serviceSlug: fields.text({ label: 'Service slug (must match services collection)' }),
        areaSlug: fields.text({ label: 'Area slug (must match areas collection)' }),
        seoTitle: fields.text({ label: 'SEO title' }),
        seoDescription: fields.text({ label: 'SEO meta description', multiline: true }),
        intro: fields.text({ label: 'Intro paragraph', multiline: true }),
        faqs: fields.array(
          fields.object({
            question: fields.text({ label: 'Question' }),
            answer: fields.text({ label: 'Answer', multiline: true }),
          }),
          { label: 'FAQs', itemLabel: (props) => props.fields.question.value }
        ),
        body: fields.markdoc({
          label: 'Additional content',
          extension: 'mdoc',
          options: {
            image: {
              directory: 'public/images/service-area/',
              publicPath: '/images/service-area/',
            },
          },
        }),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
      },
    }),
    nearMePages: collection({
      label: 'Near Me Pages (SEO)',
      slugField: 'title',
      path: 'content/near-me-pages/*/',
      schema: {
        title: fields.slug({
          name: { label: 'Page slug (e.g. plumber-near-me)' },
        }),
        h1: fields.text({ label: 'H1 headline' }),
        primaryKeyword: fields.text({ label: 'Primary keyword' }),
        bookLabel: fields.text({
          label: 'Book CTA label (person / service name)',
          description:
            'Used as “Book {label}” — e.g. Plumber, Carpenter, Men\'s Salon Services (not “Men\'s Salon” alone).',
        }),
        seoTitle: fields.text({ label: 'SEO title' }),
        seoDescription: fields.text({ label: 'SEO meta description', multiline: true }),
        intro: fields.text({ label: 'Intro paragraph', multiline: true }),
        parentServiceSlug: fields.text({
          label: 'Parent service slug',
          description: 'Must match a services collection slug (e.g. plumbing).',
        }),
        catalogSubSlugs: fields.array(fields.text({ label: 'Subcategory slug' }), {
          label: 'Catalog subcategory filter (optional)',
          description: 'If set, only these live catalog subcategories are shown (e.g. air-conditioners).',
        }),
        trustLine: fields.text({
          label: 'Hero trust line',
          defaultValue: 'Verified partners · Across Kashmir · Same-day when available',
        }),
        whoFor: fields.array(fields.text({ label: 'Situation' }), {
          label: 'Who this page is for',
        }),
        commonProblems: fields.array(fields.text({ label: 'Problem' }), {
          label: 'Common problems we handle',
        }),
        diyVsPro: fields.text({ label: 'DIY vs call a pro', multiline: true }),
        costFactors: fields.array(fields.text({ label: 'Cost factor' }), {
          label: 'What affects cost',
        }),
        seasonalNotes: fields.text({ label: 'Kashmir / seasonal notes', multiline: true }),
        coverageNote: fields.text({ label: 'Coverage note', multiline: true }),
        prepareList: fields.array(fields.text({ label: 'Item' }), {
          label: 'What to prepare before booking',
        }),
        relatedNearMeSlugs: fields.array(fields.text({ label: 'Related near-me slug' }), {
          label: 'Related near-me pages (optional)',
        }),
        faqs: fields.array(
          fields.object({
            question: fields.text({ label: 'Question' }),
            answer: fields.text({ label: 'Answer', multiline: true }),
          }),
          { label: 'FAQs', itemLabel: (props) => props.fields.question.value }
        ),
        body: fields.markdoc({
          label: 'Additional content',
          extension: 'mdoc',
          options: {
            image: {
              directory: 'public/images/near-me/',
              publicPath: '/images/near-me/',
            },
          },
        }),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
        sortOrder: fields.integer({ label: 'Sort order', defaultValue: 0 }),
      },
    }),
    faqs: collection({
      label: 'Global FAQs',
      slugField: 'question',
      path: 'content/faqs/*/',
      schema: {
        question: fields.slug({ name: { label: 'Question slug' } }),
        questionText: fields.text({ label: 'Question' }),
        answer: fields.text({ label: 'Answer', multiline: true }),
        category: fields.text({ label: 'Category' }),
        sortOrder: fields.integer({ label: 'Sort order', defaultValue: 0 }),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
      },
    }),
    testimonials: collection({
      label: 'Testimonials',
      slugField: 'name',
      path: 'content/testimonials/*/',
      schema: {
        name: fields.slug({ name: { label: 'Customer name slug' } }),
        customerName: fields.text({ label: 'Customer name' }),
        location: fields.text({ label: 'Location (e.g. Srinagar)' }),
        service: fields.text({ label: 'Service used' }),
        quote: fields.text({ label: 'Testimonial quote', multiline: true }),
        rating: fields.integer({ label: 'Rating (1-5)', defaultValue: 5 }),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
        sortOrder: fields.integer({ label: 'Sort order', defaultValue: 0 }),
      },
    }),
    guides: collection({
      label: 'Guides & Tips',
      slugField: 'title',
      path: 'content/guides/*/',
      schema: {
        title: fields.slug({ name: { label: 'Guide title' } }),
        headline: fields.text({ label: 'Headline (H1)' }),
        excerpt: fields.text({ label: 'Excerpt / list summary', multiline: true }),
        seoTitle: fields.text({ label: 'SEO title' }),
        seoDescription: fields.text({ label: 'SEO meta description', multiline: true }),
        category: fields.select({
          label: 'Category',
          options: [
            { label: 'Plumbing', value: 'Plumbing' },
            { label: 'Electrical', value: 'Electrical' },
            { label: 'Home Appliances', value: 'Home Appliances' },
            { label: 'Pest Control', value: 'Pest Control' },
            { label: 'Cleaning', value: 'Cleaning' },
            { label: 'Painting', value: 'Painting' },
            { label: 'Carpentry', value: 'Carpentry' },
            { label: 'Masonry', value: 'Masonry' },
            { label: 'Dry Cleaning', value: 'Dry Cleaning' },
            { label: "Men's Grooming", value: "Men's Grooming" },
            { label: "Women's Salon", value: "Women's Salon" },
            { label: 'Gardening', value: 'Gardening' },
            { label: 'Aluminium & Glass', value: 'Aluminium & Glass' },
            { label: 'Interior Repair', value: 'Interior Repair' },
            { label: 'Pet Care', value: 'Pet Care' },
            { label: 'Vehicle Care', value: 'Vehicle Care' },
            { label: 'Hiring', value: 'Hiring' },
            { label: 'General', value: 'General' },
          ],
          defaultValue: 'General',
        }),
        publishedAt: fields.date({ label: 'Published date' }),
        readingMinutes: fields.integer({ label: 'Reading time (minutes)', defaultValue: 5 }),
        isNew: fields.checkbox({ label: 'Mark as New', defaultValue: false }),
        isTrending: fields.checkbox({ label: 'Mark as Trending', defaultValue: false }),
        heroSub: fields.text({
          label: 'Hero subline (short)',
          description: 'One line under the H1 — story hook, not SEO fluff',
        }),
        scene: fields.text({
          label: 'Opening scene',
          multiline: true,
          description: 'First story beat shown above the quick answer',
        }),
        quickAnswer: fields.text({
          label: 'Quick answer',
          multiline: true,
        }),
        coverImage: fields.image({
          label: 'Cover / hero (16:9)',
          directory: 'public/images/guides',
          publicPath: '/images/guides/',
        }),
        titleImage: fields.image({
          label: 'Title / share card (1:1)',
          directory: 'public/images/guides',
          publicPath: '/images/guides/',
        }),
        relatedServiceSlug: fields.text({
          label: 'Related service slug (optional)',
          description: 'e.g. plumbing — used for Book CTA prefill',
        }),
        relatedGuideSlugs: fields.array(fields.text({ label: 'Guide slug' }), {
          label: 'Related guides (optional)',
          description: 'Leave empty to auto-pick same category first',
        }),
        body: fields.markdoc({
          label: 'Article body (fallback if article.html missing)',
          extension: 'mdoc',
          options: {
            image: {
              directory: 'public/images/guides/',
              publicPath: '/images/guides/',
            },
          },
        }),
        published: fields.checkbox({ label: 'Published', defaultValue: true }),
        sortOrder: fields.integer({ label: 'Sort order', defaultValue: 0 }),
      },
    }),
  },
});
