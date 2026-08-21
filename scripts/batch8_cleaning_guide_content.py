"""Batch 8 — Cleaning category DIY guide."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "CLN-D07",
        "post-renovation-cleaning-kashmir",
        "Post-renovation dust everywhere? Clear it in layers, not one frantic wipe",
        "Cleaning",
        "professional-cleaning",
        "The painters leave, the sofa is back, and by evening every windowsill wears a grey film. Someone wet-mops the living room first — and the fine cement dust turns into a sticky paste that smears into the skirting.",
        "Protect soft furnishings, dry-dust from ceiling to floor, vacuum corners before any wet mopping, then wipe cabinets and switches once the air settles. Fine dust in ducts, sticky paint residue, or a whole flat after major work needs professional post-renovation cleaning.",
        "Grey film on sills, sticky floors, and dust that returns after one wipe",
        "Construction dust settling in layers — wet-mopping too early turns it into paste",
        [
            "Fine cement, plaster, and sanding dust that stays airborne for days after work finishes.",
            "Wet mopping or wiping before vacuuming, which smears grit into tiles and wood grain.",
            "Dust trapped in curtains, carpets, AC filters, and closed cabinet tops that re-settles overnight.",
        ],
        [
            (
                "Protect and open the room",
                "a freshly finished space",
                "Cover remaining soft furniture, open windows if outdoor air is dry, and keep fans low so you do not blow dust into clean rooms.",
            ),
            (
                "Dry-dust from top to bottom",
                "ceilings, fans, and high shelves",
                "Wipe or vacuum high surfaces first — false ceilings, cornices, fans, curtain rods — so grit falls downward once, not onto a floor you already cleaned.",
            ),
            (
                "Vacuum floors and corners before wet work",
                "tile, wood, or carpet dust",
                "Use a hard-floor or upholstery tool on skirting, corners, and under radiators. Only then damp-mop with clean water changed often.",
            ),
            (
                "Wipe cabinets, switches, and glass last",
                "sticky film after the air settles",
                "Use a barely damp microfibre on doors, handles, and windows once the heavy dust has dropped. Change cloths when they grey out.",
            ),
            (
                "Book post-renovation cleaning",
                "whole-home fine dust or paint residue",
                "Pros can clear ducts, deep-clean carpets and upholstery, and lift sticky emulsion residue that home wiping leaves behind.",
            ),
        ],
        "Vacuuming first, then mopping with fresh water, finally stopped the grey paste on our new tiles.",
        "Lubna",
        "Kashmir renovations often finish just before winter when windows stay shut and bukhari heat keeps fine dust circulating indoors. Carpets, pheran piles, and lined curtains hold grit for weeks unless you work top-down and dry-first.",
        "Do not wet-mop cement dust into a paste, blast rooms with a high-speed blower toward soft furnishings, or ignore leftover paint and solvent smells in a closed bedroom.",
        "Book professional post-renovation or deep cleaning after major painting or masonry, when dust returns daily, carpets and sofas stay gritty, AC filters clog within days, or sticky paint residue will not lift with home wiping.",
        hero="Fine renovation dust needs dry layers first — wet mopping too early makes paste.",
        excerpt="Post-renovation dust in Kashmir? Dry-dust top to bottom, vacuum before mopping, wipe once the air settles, and know when to book post-construction cleaning.",
    ),
]

_BATCH_SIBLINGS = {
    "CLN-D07": (
        "kitchen-grease-cleaning-kashmir",
        "sofa-smells-stains-cleaning",
        "mattress-smell-stains-cleaning-kashmir",
        "bathroom-mould-hard-water-stains",
    ),
}

TITLE_SUBJECTS = {
    "post-renovation-cleaning-kashmir": (
        "renovation dust on windowsill, dry dusting top to bottom, vacuum before mop and microfibre wipe"
    ),
}

_SEO = {
    "post-renovation-cleaning-kashmir": {
        "seoTitle": "Post-renovation dust? Clean in layers first | Panun Kaergar",
        "seoDescription": (
            "Post-renovation dust in Kashmir? Dry-dust top to bottom, vacuum before mopping, "
            "wipe once air settles, and know when to book post-construction cleaning."
        ),
    },
}

_DONT = {
    "post-renovation-cleaning-kashmir": [
        (
            "Wet-mop fine cement dust first",
            "Turns grit into grey paste",
            "Water on unsettled construction dust smears into tile pores, wood grain, and skirting — harder to lift than dry vacuuming.",
            "Wet mop spreading grey cement paste across newly finished tile floor",
            "Vacuum dry dust before any mop",
        ),
        (
            "Blast every room with a high-speed blower",
            "Pushes dust into soft furnishings",
            "Strong airflow drives fine grit into curtains, carpets, and neighbouring rooms instead of removing it.",
            "Leaf blower or strong fan aimed at dusty curtains and sofa after renovation",
            "Controlled top-down dusting only",
        ),
        (
            "Ignore paint and solvent smell in a closed room",
            "Air quality and finish risk",
            "Sealed winter rooms trap fumes from fresh paint and adhesives; air the space and delay soft furnishings until surfaces are fully dry.",
            "Closed bedroom with fresh paint smell and windows shut after renovation",
            "Ventilate before reoccupying",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 85 + index
    guide["relatedGuideSlugs"] = list(_BATCH_SIBLINGS.get(guide["id"], ()))
    guide["isTrending"] = True
    seo = _SEO.get(guide["slug"], {})
    if seo.get("seoTitle"):
        guide["seoTitle"] = seo["seoTitle"]
    if seo.get("seoDescription"):
        guide["seoDescription"] = seo["seoDescription"]
    if guide["slug"] in _DONT:
        guide["dont_blocks"] = _DONT[guide["slug"]]
    guide["prevention"] = (
        "After any sanding or painting day, vacuum high surfaces the same evening, "
        "keep windows cracked when outdoor air is dry, and cover carpets until dust settles."
    )
    guide["prevention_caption"] = "Dry first, top to bottom — wet work comes last."
    guide["pro_tip"] = (
        "Change mop water the moment it turns grey. Dirty water re-lays the same dust as a thin film."
    )
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
