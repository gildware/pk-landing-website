"""Batch 12 — Pest Control category DIY guide (PST-D04)."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "PST-D04",
        "ants-in-kitchen-kashmir",
        "Ants in the kitchen? Follow the trail before you spray everywhere",
        "Pest Control",
        "pest-control",
        "A thin line of ants crosses the counter toward a sugar jar left open after morning tea. Someone sprays the visible ones, but by evening a new column appears from the same gap behind the skirting.",
        "Wipe the counter, remove open food and sticky spills, follow the ant trail to the entry gap, clean the route with soapy water, and use bait only where the label allows — not over food surfaces. Ants in wiring, inside wall voids, or returning after a full kitchen clean need pest control.",
        "A steady line of ants to sugar, honey, or crumbs",
        "Food source plus a crack, pipe gap, or window frame entry point",
        [
            "Open sugar, honey, fruit, or crumbs left on counters overnight.",
            "Sticky spills around the stove, kettle tray, or bin rim.",
            "Gaps under skirting, around pipes, or loose window frames giving entry.",
        ],
        [
            (
                "Remove the food source first",
                "any active trail",
                "Seal sugar and dry goods, wipe sticky spills, empty the bin, and lift pet bowls off the floor before tracing the line.",
            ),
            (
                "Follow the trail to the entry",
                "finding the route",
                "Watch where ants leave the counter — often a skirting gap, pipe collar, or window frame — and mark the spot without blocking it yet.",
            ),
            (
                "Wipe the trail with soapy water",
                "breaking the scent line",
                "Use warm water and dish soap on the counter route and along the skirting to erase the pheromone trail other ants follow.",
            ),
            (
                "Use bait correctly if needed",
                "persistent columns",
                "Place ant bait stations in hidden spots along the wall route per label instructions — never on food prep surfaces or where children and pets can reach.",
            ),
            (
                "Book pest control",
                "ants in walls or wiring",
                "A professional can treat nest routes, seal entry points safely, and handle species that need targeted treatment beyond surface spraying.",
            ),
        ],
        "Removing the open honey jar and wiping the trail stopped the line within a day — the gap by the pipe was sealed after that.",
        "Shabnam",
        "Spring thaws and damp kitchen corners in Kashmir can push ants toward warm indoor food stores. A trail to the sugar tin after wazwan prep is common — spray alone rarely reaches the nest behind the skirting.",
        "Do not spray repellent over bait stations, seal a gap while ants are still active inside, or leave open jaggery and grain sacks on the floor overnight.",
        "Book pest control when ants appear in multiple rooms, nest inside walls or electrical boxes, return within days of a full clean, or you see winged ants indoors in large numbers.",
        hero="Ants follow food and scent — remove both before you spray.",
        excerpt=(
            "Ants in the kitchen in Kashmir? Remove open food, follow the trail to the entry gap, "
            "wipe the scent line, use bait safely, and know when to book pest control."
        ),
    ),
]

_BATCH_SIBLINGS = {
    "PST-D04": (
        "cockroach-control-home-kashmir",
        "rat-signs-home-kashmir",
        "termite-signs-home-kashmir",
    ),
}

TITLE_SUBJECTS = {
    "ants-in-kitchen-kashmir": (
        "ant trail on kitchen counter to sugar jar, follow entry gap, soapy wipe and bait station placement"
    ),
}

_SEO = {
    "ants-in-kitchen-kashmir": {
        "seoTitle": "Ants in the kitchen? Follow the trail first | Panun Kaergar",
        "seoDescription": (
            "Ants in the kitchen in Kashmir? Remove food sources, trace the entry gap, wipe the scent trail, "
            "use bait safely, and know when to book pest control."
        ),
    },
}

_DONT = {
    "ants-in-kitchen-kashmir": [
        (
            "Spray repellent over bait stations",
            "Ants avoid the bait",
            "Repellent sprays drive ants away from gel or bait you placed — they scatter instead of carrying poison back to the nest.",
            "Insecticide spray applied directly over ant bait gel on kitchen skirting",
            "Use bait alone or spray elsewhere",
        ),
        (
            "Seal gaps while ants are still inside",
            "Traps them indoors",
            "Closing a pipe gap or skirting crack before activity drops can push ants into wall voids or along new routes through the kitchen.",
            "Silicone sealant applied to skirting gap while ant trail still active",
            "Clean and bait first, then seal",
        ),
        (
            "Leave open sugar and jaggery out",
            "Feeds the colony daily",
            "Ants need a steady food source — open tins, sticky honey jars, and grain sacks on the floor keep the trail alive no matter how much you spray.",
            "Open sugar tin and jaggery block on kitchen floor with ant trail",
            "Store food sealed overnight",
        ),
    ],
}

_FAQS = {
    "ants-in-kitchen-kashmir": [
        (
            "Why do ants appear in the kitchen in Kashmir homes?",
            "Ants follow food and water — open sugar, honey, crumbs, sticky spills, and damp corners near sinks attract them. "
            "Warm indoor kitchens after cold outdoor nights make entry gaps worth checking.",
        ),
        (
            "Should I spray ants I see on the counter?",
            "Spraying visible ants kills only the workers on the surface. Remove the food source, wipe the trail with soapy water, "
            "and use bait along the route if activity continues.",
        ),
        (
            "Where do kitchen ants usually enter?",
            "Common entry points include gaps under skirting, pipe collars under the sink, loose window frames, "
            "and cracks where tiles meet the wall.",
        ),
        (
            "Are ant baits safe in a home kitchen?",
            "Use labelled bait stations in hidden spots along walls — never on food prep surfaces or where children and pets can reach. "
            "Follow the product instructions and keep food stored sealed.",
        ),
        (
            "When should I book pest control for ants?",
            "Book when ants spread to several rooms, appear inside walls or electrical boxes, return within days of a thorough clean, "
            "or you see large numbers of winged ants indoors.",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 91 + index
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
        "Store sugar, honey, and dry goods in sealed containers, wipe stove splatter the same evening, "
        "and check skirting gaps after monsoon dampness swells wood trim."
    )
    guide["prevention_caption"] = "No open food overnight — ants have nothing to march toward."
    guide["pro_tip"] = (
        "If ants reappear at the same spot after wiping, the nest is likely behind the skirting or under the sink cabinet — "
        "bait and professional help beat repeated surface spraying."
    )
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
