"""Batch 6 — Carpentry DIY guide (wooden drawer stuck) with SEO-focused meta."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "CRP-D04",
        "wooden-drawer-stuck-kashmir",
        "Wooden drawer stuck? Ease the rub before you yank the handle",
        "Carpentry",
        "carpentry",
        "The kitchen drawer stops halfway with a soft scrape, someone pulls harder until the front flexes, and a bag of utensils nearly tips onto the floor.",
        "Empty the drawer, find where wood rubs on the runner or carcass, clean grit from the channel, and tighten loose runner screws. Swollen particleboard, a bent metal runner, or a drawer that will not open past a few centimetres needs a carpenter.",
        "Drawer sticks, scrapes, or will not open fully",
        "Swollen board, dirty runner, misaligned slides, or loose fixings",
        [
            "Damp seasons swelling the drawer box or carcass so edges rub.",
            "Grit, sugar, or crumbs packed into wooden or metal runners.",
            "Loose runner screws letting the drawer sag and catch on one side.",
        ],
        [
            (
                "Empty and support the drawer",
                "any stuck drawer",
                "Remove contents so weight is not fighting you, then pull gently while watching both sides for the catch point.",
            ),
            (
                "Find the rub mark",
                "a scrape or hang-up",
                "Look for shiny worn wood, pencil a mark on the rubbing edge, and note whether the catch is bottom, side, or rear.",
            ),
            (
                "Clean the runners",
                "grit in the channel",
                "Vacuum and wipe wooden grooves or metal slides; avoid thick oil that holds more dust in a Kashmir kitchen.",
            ),
            (
                "Tighten runner and front screws",
                "a sagging or crooked pull",
                "Snug visible screws on the slide and drawer front — stop if a screw spins in stripped particleboard.",
            ),
            (
                "Book a carpenter",
                "swollen box, bent slide, or stripped holes",
                "A pro can plane a marked edge, replace runners, or rebuild a delaminating drawer without wrecking the cabinet face.",
            ),
        ],
        "Sugar grit in the runner was the whole problem; a clean and a snug screw freed the drawer.",
        "Sameera",
        "Kashmir kitchens swing from damp monsoon air to dry winter heating. Particleboard drawers swell and shrink, so a tight summer fit often becomes a winter scrape — or the reverse after rain.",
        "Do not yank a stuck drawer until the front cracks, flood wooden runners with thick grease, or plane wood while the drawer is still loaded and misaligned.",
        "Book a carpenter for a drawer that will not open, cracked or delaminating fronts, bent metal slides, stripped screw holes, or a soft-close runner that has jumped the track.",
        hero="A stuck drawer usually needs a clean runner and a calm look at the rub — not a harder pull.",
        excerpt=(
            "Wooden drawer stuck in Kashmir? Empty it, find the rub mark, clean the runner, "
            "tighten loose screws, and know when a carpenter should ease swollen particleboard."
        ),
    ),
]

_BATCH_SIBLINGS = {
    "CRP-D04": (
        "kitchen-cabinet-door-sagging-kashmir",
        "wardrobe-door-slider-problems",
        "door-not-closing-properly",
    ),
}

TITLE_SUBJECTS = {
    "wooden-drawer-stuck-kashmir": "wooden kitchen drawer stuck on runner with rub mark and clean channel",
}

_SEO = {
    "wooden-drawer-stuck-kashmir": {
        "seoTitle": "Stuck Wooden Drawer in Kashmir? Fix the Rub First | Panun Kaergar",
        "seoDescription": (
            "Wooden kitchen drawer stuck in Kashmir? Empty it, mark the rub, clean runners, "
            "tighten screws, and know when to book a carpenter."
        ),
    },
}

_DONT = {
    "wooden-drawer-stuck-kashmir": [
        (
            "Yank until the front flexes",
            "Cracks the drawer face",
            "Hard pulls split particleboard fronts and tear runner screws out of soft carcass wood.",
            "Person yanking stuck kitchen drawer until front panel flexes",
            "Find the rub first",
        ),
        (
            "Flood the runner with thick oil",
            "Holds kitchen grit",
            "Heavy oil catches sugar and dust so the drawer sticks again within days in a busy Kashmir kitchen.",
            "Thick oil poured into wooden kitchen drawer runner channel",
            "Clean dry, then light care",
        ),
        (
            "Plane while it is still loaded",
            "Cuts the wrong edge",
            "Shaving wood without emptying and marking the true rub often creates a permanent summer gap.",
            "Hand plane on wooden drawer still full of utensils",
            "Empty, mark, then ease",
        ),
    ],
}

_FAQS = {
    "wooden-drawer-stuck-kashmir": [
        (
            "Why is my wooden kitchen drawer stuck in Kashmir?",
            "Most stuck drawers rub because of swollen particleboard after damp weather, grit packed in the runner, "
            "or loose slide screws that let one side sag. Start by emptying the drawer and finding the rub mark before you force it.",
        ),
        (
            "How do I free a stuck wooden drawer without breaking it?",
            "Empty it, support both sides, pull gently to locate the catch, clean the runners, and tighten visible screws. "
            "Do not yank the front or plane wet wood while the drawer is still loaded.",
        ),
        (
            "Can damp weather make a drawer stick?",
            "Yes. Kashmir kitchens swing between monsoon humidity and dry heated winter air, so particleboard drawers swell and shrink. "
            "A drawer that sticks after rain often needs drying and a marked rub check, not a harder pull.",
        ),
        (
            "Should I oil a sticky wooden drawer runner?",
            "Avoid flooding wooden runners with thick oil — it holds sugar and kitchen dust so the drawer sticks again. "
            "Clean grit first; use only a light dry lubricant on metal slides if needed.",
        ),
        (
            "When should I book a carpenter for a stuck drawer?",
            "Book when the drawer will not open, the front is cracked or delaminating, metal slides are bent, "
            "screws spin in stripped holes, or a soft-close runner has jumped the track.",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 76 + index
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
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
