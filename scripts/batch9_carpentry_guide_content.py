"""Batch 9 — Carpentry category DIY guide."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "CRP-D05",
        "squeaky-floorboard-kashmir",
        "Squeaky floorboard? Find the loose board before you nail at random",
        "Carpentry",
        "carpentry",
        "Every evening walk to the kitchen announces itself with a sharp squeak by the bedroom door. Someone grabs a random nail and hammers into the loudest board — and the next week a second squeak answers from two steps away.",
        "Walk slowly and mark the exact board, check for a loose nail or screw, seat the board onto the joist with a proper fixing if you can see the structure, and use a dry lubricant only as a short quieting step. A bouncing span, rotten timber, or squeaks across a whole room need a carpenter.",
        "Sharp squeak or creak when you step on one board",
        "Loose board rubbing on a joist, nail, or neighbouring plank",
        [
            "Floorboards shrinking in dry heated winter rooms so edges rub and nails loosen.",
            "A nail or screw that has worked up and rubs inside the wood.",
            "Joist movement or a board that no longer sits flat on its support.",
        ],
        [
            (
                "Walk and mark the squeak",
                "any night-creak board",
                "Step slowly in socks, mark the loudest plank with tape or pencil, and note whether it squeaks near a wall, mid-span, or over a known joist line.",
            ),
            (
                "Look for a proud nail or screw",
                "a local click underfoot",
                "Check the marked board for a raised head; seat it carefully or replace with a slightly longer screw into solid timber — never force a bent nail sideways.",
            ),
            (
                "Quiet the rub only as a temporary step",
                "a dry seasonal squeak",
                "A light dusting of talc or graphite powder into the gap can reduce friction overnight, but it will not fix a loose board that still moves.",
            ),
            (
                "Screw the board to the joist if accessible",
                "a board that lifts underfoot",
                "Predrill and drive screws into the joist line so the board sits flat; hide heads if the floor is finished timber. Stop if the timber feels soft or crumbly.",
            ),
            (
                "Book a carpenter",
                "bounce, rot, or a whole noisy bay",
                "A pro can work from below, sister a weak joist, replace a cupped board, and quiet a run of boards without guessing nail lines into pipes or cables.",
            ),
        ],
        "Marking the board and one screw into the joist ended the midnight squeak; random nails would have missed it.",
        "Idrees",
        "Kashmir timber floors dry hard under bukhari and room heaters, then take moisture again in damp spells. Boards shrink, nails loosen, and the same path to the kitchen starts announcing every step until the fixing is seated again.",
        "Do not hammer nails at random into an unknown floor bay, flood gaps with thick oil, or ignore a soft bouncing span that may mean a failing joist.",
        "Book a carpenter for squeaks across a whole room, boards that bounce or feel soft, visible rot, access only from a ceiling below, or any floor where pipes and cables may run under the boards.",
        hero="A squeak is usually one loose board — mark it before you nail at random.",
        excerpt=(
            "Squeaky floorboard in Kashmir? Mark the board, check loose fixings, seat it to the joist, "
            "and know when a carpenter should fix bounce or a whole noisy bay."
        ),
    ),
]

_BATCH_SIBLINGS = {
    "CRP-D05": (
        "door-not-closing-properly",
        "wooden-drawer-stuck-kashmir",
        "kitchen-cabinet-door-sagging-kashmir",
        "wardrobe-door-slider-problems",
    ),
}

TITLE_SUBJECTS = {
    "squeaky-floorboard-kashmir": (
        "squeaky timber floorboard, mark the loose plank, nail head and screw into joist"
    ),
}

_SEO = {
    "squeaky-floorboard-kashmir": {
        "seoTitle": "Squeaky floorboard? Mark it before nailing | Panun Kaergar",
        "seoDescription": (
            "Squeaky floorboard in Kashmir? Mark the board, check loose nails, seat it to the joist, "
            "and know when to book a carpenter for bounce or rot."
        ),
    },
}

_DONT = {
    "squeaky-floorboard-kashmir": [
        (
            "Hammer nails at random into the bay",
            "Misses the joist — hits services",
            "Blind nailing can miss the joist entirely and risk pipes or cables running under timber floors.",
            "Person hammering random nails into squeaky floorboard without marking joist",
            "Mark the board and joist line first",
        ),
        (
            "Flood the gap with thick oil",
            "Holds grit and stains timber",
            "Heavy oil darkens boards and catches dust so the rub returns messier than before.",
            "Thick oil poured into gap between squeaky timber floorboards",
            "Dry powder only as a short quieting step",
        ),
        (
            "Ignore a soft bouncing span",
            "Joist or rot risk",
            "A board that dips underfoot is not just noisy — it can mean a weak joist or decaying timber that needs a carpenter, not another nail.",
            "Foot pressing soft bouncing floorboard that dips between joists",
            "Book help for bounce or soft timber",
        ),
    ],
}

_FAQS = {
    "squeaky-floorboard-kashmir": [
        (
            "Why does my wooden floor squeak in Kashmir?",
            "Most squeaks are a loose board rubbing on a joist, a proud nail, or a neighbouring plank. "
            "Dry winter heating shrinks timber so fixings loosen; damp spells can swell boards again.",
        ),
        (
            "How do I find which floorboard is squeaking?",
            "Walk slowly in socks, listen for the loudest step, and mark that plank with tape or pencil. "
            "Note whether the noise is near a wall, mid-span, or over a joist line.",
        ),
        (
            "Will talc or graphite fix a squeaky floor?",
            "A light dry powder in the gap can quiet friction for a while, but it will not secure a board that still lifts. "
            "Seat the board to the joist or book a carpenter if movement remains.",
        ),
        (
            "Is it safe to nail a squeaky floorboard myself?",
            "Only if you can identify the joist line and there is no risk of hidden pipes or cables. "
            "Random nailing is how floors get damaged and services get hit — mark first or book a pro.",
        ),
        (
            "When should I book a carpenter for floor squeaks?",
            "Book when squeaks run across a whole room, boards bounce or feel soft, timber looks rotten, "
            "access is only from a ceiling below, or you are unsure what runs under the floor.",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 87 + index
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
        "Keep indoor humidity steadier where you can, fix drips that wet timber floors, "
        "and reseat a single squeaky board early before neighbouring planks loosen."
    )
    guide["prevention_caption"] = "Mark the board once — random nails create new squeaks."
    guide["pro_tip"] = (
        "Tape a short line on the loudest plank, then check from both directions. "
        "The true rub is often half a board away from where you first heard it."
    )
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
