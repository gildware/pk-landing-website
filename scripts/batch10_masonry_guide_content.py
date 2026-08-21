"""Batch 10 — Masonry category DIY guide."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "MSN-D05",
        "bathroom-grout-crumbling-kashmir",
        "Bathroom grout crumbling? Rake the joint before water reaches the wall",
        "Masonry",
        "masonry",
        "After a week of showers the floor joints look sandy, a dark line runs along the wall skirting, and someone squeezes silicone over the crumbling grout — trapping moisture behind a shiny seal.",
        "Dry the area, rake out loose grout, clean and dry the joints fully, then regrout with a bathroom-grade mix and seal only after it has cured. Hollow tiles, soft plaster behind the wall, or mould that returns after regrouting need a mason for proper tile and waterproofing repair.",
        "Sandy, cracked, or missing grout lines in a wet bathroom",
        "Failed joint that lets water sit against the tile bed or wall",
        [
            "Old cement grout worn by daily washing, hard water, and cleaning acids.",
            "Movement or hollow tiles flexing the joint until it powders and drops out.",
            "Water left standing on floors after showers, working into open joints.",
        ],
        [
            (
                "Dry and map the failed joints",
                "any sandy or missing line",
                "Wipe the floor and wall dry, then mark every joint that powders, cracks, or shows a dark damp edge so you know the full repair length.",
            ),
            (
                "Rake out loose grout only",
                "crumbling joints",
                "Use a grout rake or a narrow tool to remove loose material to a sound depth — do not dig into soft plaster or the tile bed.",
            ),
            (
                "Clean and dry the open joint",
                "before any new fill",
                "Vacuum dust, wipe with a barely damp cloth, and let the joint dry fully. Wet joints make new grout weak and patchy.",
            ),
            (
                "Regrout and cure before sealing",
                "sound empty joints",
                "Press bathroom-grade grout firmly into the joint, tool it smooth, clean haze carefully, and wait for full cure before any silicone on corners.",
            ),
            (
                "Book a mason",
                "hollow tiles, soft wall, or repeat mould",
                "A pro can lift failed tiles, redo waterproofing, and replace a run of joints that will not hold after DIY regrouting.",
            ),
        ],
        "Raking the sandy joints and letting them dry overnight before regrouting stopped the dark line along the wall.",
        "Nusrat",
        "Kashmir bathrooms often mix hard water, closed winter ventilation, and cold floors that stay wet after showers. Grout fails first at floor edges and shower corners — the same paths seepage uses to reach plaster.",
        "Do not seal silicone over wet crumbling grout, dig aggressively into a soft wall, or ignore mould and hollowness behind failed joints.",
        "Book a mason when tiles sound hollow, plaster behind the wall feels soft, mould returns after cleaning, waterproofing has failed, or a large bathroom needs a full joint and tile reset.",
        hero="Crumbling grout is an open door for water — rake and dry before you seal.",
        excerpt=(
            "Bathroom grout crumbling in Kashmir? Dry and map failed joints, rake loose grout, "
            "regrout after a full dry, and know when a mason should fix hollow tiles or waterproofing."
        ),
    ),
]

_BATCH_SIBLINGS = {
    "MSN-D05": (
        "floor-tile-hollow-loose-kashmir",
        "wall-seepage-plaster-damage-kashmir",
        "loose-plaster-falling-kashmir",
        "wall-cracks-cosmetic-structural",
    ),
}

TITLE_SUBJECTS = {
    "bathroom-grout-crumbling-kashmir": (
        "bathroom floor tile grout crumbling, grout rake, dry joint and bathroom-grade regrout"
    ),
}

_SEO = {
    "bathroom-grout-crumbling-kashmir": {
        "seoTitle": "Bathroom grout crumbling? Rake joints first | Panun Kaergar",
        "seoDescription": (
            "Bathroom grout crumbling in Kashmir? Dry and map joints, rake loose grout, regrout after a full dry, "
            "and know when to book a mason."
        ),
    },
}

_DONT = {
    "bathroom-grout-crumbling-kashmir": [
        (
            "Silicone over wet crumbling grout",
            "Traps moisture behind the seal",
            "A shiny bead over sandy joints locks water against the tile bed and often worsens mould and seepage.",
            "Silicone sealant squeezed over wet crumbling bathroom floor grout",
            "Rake and dry before any seal",
        ),
        (
            "Dig deep into a soft wall or bed",
            "Damages plaster and tile bond",
            "Forcing a tool past failed grout into soft plaster or adhesive can loosen sound tiles around the repair.",
            "Tool digging aggressively under bathroom tile into soft plaster bed",
            "Remove only loose grout to sound depth",
        ),
        (
            "Ignore mould or a hollow clack",
            "Water is already behind the finish",
            "Black mould at joints or hollow-sounding tiles means the problem is past surface grout — DIY fill alone will not last.",
            "Black mould along bathroom wall tile joint with hollow tile tap test",
            "Book a mason for hollow or mouldy areas",
        ),
    ],
}

_FAQS = {
    "bathroom-grout-crumbling-kashmir": [
        (
            "Why is bathroom grout crumbling in Kashmir homes?",
            "Daily washing, hard water, cleaning acids, and boards that stay wet after showers wear cement grout. "
            "Movement or hollow tiles also flex joints until they powder and drop out.",
        ),
        (
            "Can I regrout bathroom tiles myself?",
            "Yes for short runs of failed joints if tiles are still solid. Dry and rake loose grout, clean the joint, "
            "regrout with a bathroom-grade mix, and cure fully before sealing corners.",
        ),
        (
            "Should I put silicone over crumbling grout?",
            "No. Silicone over wet or sandy grout traps moisture behind the seal. Rake out the failure, dry the joint, "
            "regrout, then use silicone only where a flexible corner joint is needed after curing.",
        ),
        (
            "How long should I wait before using the bathroom after regrouting?",
            "Follow the product cure time — often a day or more before heavy wetting. Walking carefully may be fine sooner; "
            "showers and standing water should wait until the grout has set.",
        ),
        (
            "When should I book a mason for bathroom grout problems?",
            "Book when tiles sound hollow, plaster feels soft, mould returns after cleaning, waterproofing has failed, "
            "or a large area needs joints and tiles reset properly.",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 89 + index
    guide["relatedGuideSlugs"] = list(_BATCH_SIBLINGS.get(guide["id"], ()))
    guide["isTrending"] = True
    seo = _SEO.get(guide["slug"], {})
    if seo.get("seoTitle"):
        guide["seoTitle"] = seo["seoTitle"]
    if seo.get("seoDescription"):
        guide["seoDescription"] = seo["seoDescription"]
    if guide["slug"] in _DONT:
        guide["dont_blocks"] = _DONT[guide["slug"]]
    if guide["slug"] in _FAQS:
        guide["faqs"] = _FAQS[guide["slug"]]
    guide["prevention"] = (
        "Squeegee standing water after showers, keep the exhaust or window working, "
        "and touch up a short failed joint early before water reaches the wall."
    )
    guide["prevention_caption"] = "Dry joints last longer than sealed wet ones."
    guide["pro_tip"] = (
        "If a joint powders under a fingernail, map the whole run before you buy grout. "
        "A two-metre dark edge usually means more failure than the one sandy spot you noticed."
    )
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
