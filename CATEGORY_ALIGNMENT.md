# Marketing ↔ Admin category alignment

Website categories in `content/services/` should match parent categories in **panun-admin** (`CategoryManagement` module).

| Marketing slug | Display name | Admin notes |
|----------------|--------------|-------------|
| `carpentry` | Carpentry | Align with admin parent category name |
| `plumbing` | Plumbing | |
| `masonry` | Masonry | |
| `electrician` | Electrician | |
| `professional-cleaning` | Professional Cleaning | Home + office cleaning |
| `pest-control` | Pest Control | |
| `dry-clean-laundry` | Dry Clean & Laundry | |
| `painting` | Painting | |
| `home-appliances` | Home Appliances | Confirmed in admin seeder (`slug: home-appliances`) |
| `gardening` | Gardening | |
| `mens-salon` | Men's Salon | |
| `womens-salon` | Women's Salon | |
| `interior-decor` | Interior Decor | |

**Action for ops:** When adding categories in admin, update matching YAML in `content/services/{slug}/` and create `content/service-area-pages/{slug}-srinagar/` if serving Srinagar.

**Booking form** uses display names (`shortName`) — keep these aligned with what your call center expects.
