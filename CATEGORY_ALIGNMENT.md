# Marketing ↔ Admin category alignment

Website categories in `content/services/` should match parent categories in **panun-admin** (`categories` table, `position = 1`).

Live admin parents (queried from production MySQL):

| Admin name | Admin slug | Marketing slug |
|------------|------------|----------------|
| Carpentry Services | `carpentary` | `carpentry` |
| Cleaning Services | `cleaning` | `professional-cleaning` |
| Dry Cleaning & Laundry | `laundry` | `dry-clean-laundry` |
| Electrician Services | `electrical` | `electrician` |
| Home Appliances | `home-appliance` | `home-appliances` |
| Masonary Services | `masonry` | `masonry` |
| Men's Salon | `mens-salon` | `mens-salon` |
| Pest Control | `pest-control` | `pest-control` |
| Painting Services | `painting` | `painting` |
| Plumbing Services | `plumbing` | `plumbing` |
| Women's Salon | `womens-salon` | `womens-salon` |
| Gardening Services | `gardening` | `gardening` |
| Aluminium & Steel Works | `aluminium-steel-works` | `aluminium-steel-works` |
| Pet Grooming | `pet-grooming` | `pet-grooming` |
| Interior Decor | `interior-decor` | `interior-decor` |
| Vehicle Services | `vehicle-services` | `vehicle-services` |

Subcategory pills (admin `position = 2`) live in `src/utils/categoryCatalog.ts` → `categorySubcategories`. Keep them in sync with live admin only.

Presentation colors/icons live in `src/utils/categoryCatalog.ts`. Homepage stack, showcase, marquee, work-in-context, header nav, and services grid all pull from `getServices()`.

**Action for ops:** When adding categories in admin, update matching YAML in `content/services/{slug}/`, `categoryCatalog.ts` (`categoryCatalog` + `categorySubcategories`), `serviceGroups.ts`, and create `content/service-area-pages/{slug}-srinagar/` if serving Srinagar.
