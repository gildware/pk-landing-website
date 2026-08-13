"""Batch 7 — Pet Care / grooming DIY guide content."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "PET-D06",
        "dog-smelly-bath-home-kashmir",
        "Dog smells or needs a bath? Wash safely without skin flare-ups",
        "Pet Care",
        "dog-grooming",
        "After a muddy Srinagar walk the dog rolls on the carpet, the living room smells like wet fur by evening, and someone reaches for kitchen dish soap before anyone checks the skin.",
        "Brush out dirt first, bathe with lukewarm water and pet-safe shampoo, rinse thoroughly, and dry the coat completely — especially ears, paws, and folds. Open sores, heavy mats, fear aggression, or smell that returns within a day needs a groomer or vet check.",
        "Wet-dog smell, greasy coat, or muddy fur after walks",
        "Damp undercoat, wrong shampoo, or incomplete drying",
        [
            "Mud, pollen, and damp undercoat after walks that never fully dried.",
            "Too many baths or the wrong shampoo stripping oils and leaving a greasy rebound smell.",
            "Ears, paws, and skin folds trapping moisture in heated winter rooms.",
        ],
        [
            (
                "Check skin and coat before water",
                "any smelly or dirty dog",
                "Part the fur in good light. Look for redness, fleas, scabs, hot spots, or mats close to skin before you wet anything.",
            ),
            (
                "Brush out dirt and loose hair first",
                "muddy or shedding coats",
                "A dry brush removes grit that would otherwise turn into paste in the bath and shortens wash time.",
            ),
            (
                "Bathe with lukewarm water and pet shampoo",
                "routine odour and dirt",
                "Wet the coat thoroughly, massage a small amount of dog shampoo, keep soap out of eyes and ears, and work calmly from neck toward the tail.",
            ),
            (
                "Rinse thoroughly and dry completely",
                "smell that comes back after washing",
                "Leftover shampoo and damp undercoat cause rebound odour. Towel well, then use a pet-safe dryer on low or warm indoor airflow until the coat is dry to the skin.",
            ),
            (
                "Book pet grooming",
                "heavy odour, mats, fear, or skin issues",
                "A trained groomer can bathe, deshed, and dry safely at home — especially when the dog panics, the coat is matted, or smell returns despite careful washing.",
            ),
        ],
        "We stopped using kitchen soap; one proper pet shampoo bath and a full dry fixed the living-room smell.",
        "Amina",
        "Muddy spring walks, rainy days, and heated winter rooms all trap damp undercoat. A dog that smells fine outdoors can fill a closed flat with wet-fur odour by evening if the coat never dries to the skin.",
        "Do not use human shampoo or dish soap, bathe a dog with open sores without advice, or leave a wet coat to air-dry on a cold Kashmir floor overnight.",
        "Book pet grooming for heavy odour, dense undercoat, mats, fear during bathing, or a coat that will not dry well at home. See a veterinarian for sores, ear pain, hair loss, or smell that returns with redness.",
        hero="A smelly coat usually needs a careful bath plan — not human shampoo or a rushed winter soak.",
        excerpt=(
            "Dog smells or needs a bath in Kashmir? Brush first, use pet shampoo and lukewarm water, "
            "rinse and dry fully, and know when to book a groomer."
        ),
    ),
]

_BATCH_SIBLINGS = {
    "PET-D06": (
        "dog-itching-scratching",
        "matted-fur-dog-cat",
    ),
}

TITLE_SUBJECTS = {
    "dog-smelly-bath-home-kashmir": "dog with damp muddy coat needing pet-safe bath and full dry at home",
}

_SEO = {
    "dog-smelly-bath-home-kashmir": {
        "seoTitle": "Dog Smells or Needs a Bath? Safe Wash Guide | Panun Kaergar",
        "seoDescription": (
            "Dog smells or needs a bath in Kashmir? Brush first, use pet shampoo, rinse well, "
            "dry fully, and know when to book pet grooming help."
        ),
    },
}

_DONT = {
    "dog-smelly-bath-home-kashmir": [
        (
            "Use human shampoo or dish soap",
            "Strips skin and worsens smell",
            "Human products are the wrong pH for dog skin and often leave a greasy rebound odour within days.",
            "Human shampoo bottle being used on a dog in a bathtub",
            "Pet shampoo only",
        ),
        (
            "Bathe too often out of panic",
            "Dries skin and invites itch",
            "Weekly emergency washes strip oils. Most dogs need baths only when dirty or smelly — plus brushing between washes.",
            "Dog being bathed too frequently with irritated dry skin",
            "Bathe when needed",
        ),
        (
            "Leave the coat damp overnight",
            "Locks in smell and chill",
            "A half-dry undercoat smells stronger the next morning and risks chill on cold Kashmir floors.",
            "Damp dog lying on a cold floor overnight after an incomplete dry",
            "Dry to the skin",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 77 + index
    guide["relatedGuideSlugs"] = list(_BATCH_SIBLINGS.get(guide["id"], ()))
    guide["isTrending"] = True
    seo = _SEO.get(guide["slug"], {})
    if seo.get("seoTitle"):
        guide["seoTitle"] = seo["seoTitle"]
    if seo.get("seoDescription"):
        guide["seoDescription"] = seo["seoDescription"]
    if guide["slug"] in _DONT:
        guide["dont_blocks"] = _DONT[guide["slug"]]
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
