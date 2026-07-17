# Marketing ↔ Admin category alignment

Website categories in `content/services/` should match parent categories in **panun-admin** (`categories` table, `position = 1`).

Live admin parents (queried from `pk_mar_ts_l`):

| Admin name | Admin slug | Marketing slug |
|------------|------------|----------------|
| Carpentry Services | `carpentary` | `carpentry` |
| Cleaning Services | `cleaning` | `professional-cleaning` |
| Dry Cleaning & Laundry | `laundry` | `dry-clean-laundry` |
| Electrician Services | `electrical` | `electrician` |
| Home Appliances | `home-appliance` | `home-appliances` |
| Masonary Services | `masonry` | `masonry` |
| Men's Salon | `mens-salon` | `mens-salon` |
| Painting Services | `painting` | `painting` |
| Plumbing Services | `plumbing` | `plumbing` |
| Tankey cleaning | `tamkey-cleaning` | `tank-cleaning` |
| Women's Salon | `womens-salon` | `womens-salon` |

Marketing also publishes (not always present as admin parents):

| Marketing slug | Notes |
|----------------|-------|
| `pest-control` | Marketing catalog |
| `gardening` | Marketing catalog |
| `interior-decor` | Marketing catalog |

Presentation colors/icons live in `src/utils/categoryCatalog.ts`. Homepage stack, showcase, marquee, work-in-context, header nav, and services grid all pull from `getServices()`.

**Action for ops:** When adding categories in admin, update matching YAML in `content/services/{slug}/`, `categoryCatalog.ts`, and create `content/service-area-pages/{slug}-srinagar/` if serving Srinagar.
