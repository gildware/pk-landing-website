/** Matches /services page groups and booking form optgroups. */
export const serviceGroupDefs = [
  {
    label: 'Home repair & construction',
    slugs: ['carpentry', 'plumbing', 'masonry', 'electrician', 'painting', 'interior-decor'],
  },
  {
    label: 'Cleaning & care',
    slugs: ['professional-cleaning', 'pest-control', 'dry-clean-laundry', 'gardening', 'tank-cleaning'],
  },
  {
    label: 'Appliances & lifestyle',
    slugs: ['home-appliances', 'mens-salon', 'womens-salon'],
  },
] as const;

export interface ServiceOption {
  slug: string;
  shortName: string;
}

export function groupServices(services: ServiceOption[]) {
  const groupedSlugs = new Set<string>(serviceGroupDefs.flatMap((g) => [...g.slugs]));
  const groups = serviceGroupDefs
    .map((def) => ({
      label: def.label,
      services: def.slugs
        .map((slug) => services.find((s) => s.slug === slug))
        .filter((s): s is ServiceOption => Boolean(s)),
    }))
    .filter((g) => g.services.length > 0);

  const ungrouped = services.filter((s) => !groupedSlugs.has(s.slug));
  if (ungrouped.length > 0) {
    groups.push({ label: 'More services', services: ungrouped });
  }

  return groups;
}
