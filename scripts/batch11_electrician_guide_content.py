"""Batch 11 — Electrical category DIY guide (ELC-D04)."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "ELC-D04",
        "lights-dim-when-geyser-on-kashmir",
        "Lights dim when the geyser starts? Check load and voltage before rewiring",
        "Electrical",
        "electrician",
        "The bathroom geyser clicks on and the kitchen bulbs drop to a dull orange for a few seconds. Someone blames the wiring, but the real answer may be a shared circuit, a weak supply, or a heater drawing more than the line can carry.",
        "Note whether dimming happens only when the geyser, heater, or AC starts, check if other rooms flicker too, unplug non-essential loads on that circuit, and test whether the supply voltage is stable. Persistent dimming with a hot board, buzzing, or a tripping MCB needs an electrician to check wiring size, earthing, and load balance.",
        "Bulbs or tube lights dip when a high-watt appliance starts",
        "Voltage drop from overload, shared circuit, or weak supply",
        [
            "Geyser, immersion rod, or heater on the same circuit as lights and sockets.",
            "Undersized wiring or a loose connection at the board or a junction box.",
            "Weak incoming supply or long cable runs that cannot hold voltage under load.",
        ],
        [
            (
                "Confirm the pattern",
                "first triage",
                "Switch the geyser or heater on and off while watching lights in the same room and nearby rooms — note whether dimming is brief or lasts the whole heat-up.",
            ),
            (
                "Unplug other loads on that circuit",
                "overload check",
                "Remove heaters, kettles, and irons from sockets on the same line, then start the geyser again and see if dimming eases.",
            ),
            (
                "Check labels and breaker grouping",
                "shared circuit",
                "Look at the distribution board labels to see whether lights and the geyser share one MCB — a common setup in older flats.",
            ),
            (
                "Test voltage at a simple socket",
                "supply stability",
                "If you have a basic multimeter and feel confident, compare socket voltage with the geyser off and on — a large drop suggests load or supply strain. Otherwise note the pattern for the electrician.",
            ),
            (
                "Book an electrician",
                "persistent dimming or danger signs",
                "A pro can measure load, split circuits, tighten connections, and confirm cable size and earthing are safe for a geyser.",
            ),
        ],
        "Splitting the geyser onto its own circuit stopped the kitchen lights dipping every morning.",
        "Imtiyaz",
        "Kashmir winters push geysers, blowers, and bukhari-adjacent heaters onto the same evening load. Older flats often run lights and a bathroom geyser from one line that was never sized for both.",
        "Do not ignore buzzing, a hot distribution board, scorch marks, or dimming that worsens each week — voltage drop under load can damage appliances and loosen connections over time.",
        "Book an electrician when dimming is constant, the MCB trips with the geyser, you smell burning, the board feels hot, or several rooms flicker whenever one appliance starts.",
        hero="Dim lights when the geyser starts usually mean load — not bad bulbs.",
        excerpt=(
            "Lights dim when the geyser starts in Kashmir? Map the pattern, reduce shared circuit load, "
            "check breaker grouping, and know when an electrician should split circuits or test supply voltage."
        ),
    ),
]

_BATCH_SIBLINGS = {
    "ELC-D04": (
        "mcb-keeps-tripping-kashmir",
        "flickering-lights-causes-kashmir",
        "no-power-one-room-kashmir",
        "wall-socket-sparking-kashmir",
    ),
}

TITLE_SUBJECTS = {
    "lights-dim-when-geyser-on-kashmir": (
        "lights dimming when geyser or heater starts, voltage drop, circuit load check and electrician split"
    ),
}

_SEO = {
    "lights-dim-when-geyser-on-kashmir": {
        "seoTitle": "Lights dim when geyser starts? Check load first | Panun Kaergar",
        "seoDescription": (
            "Lights dim when the geyser starts in Kashmir? Map the pattern, reduce shared circuit load, "
            "and know when to book an electrician for wiring and voltage checks."
        ),
    },
}

_DONT = {
    "lights-dim-when-geyser-on-kashmir": [
        (
            "Swap to higher-watt bulbs",
            "Masks a supply problem",
            "Brighter bulbs draw more current and can worsen voltage drop or overheat fittings on an already strained circuit.",
            "Higher watt bulb installed in ceiling fitting while lights still dim when geyser starts",
            "Fix load and wiring, not bulb size",
        ),
        (
            "Run geyser and heater on one multi-plug",
            "Overloads one socket line",
            "Stacking high-watt appliances on a single socket or extension multiplies heat and voltage drop at weak connections.",
            "Geyser plug and room heater sharing one multi-plug adapter on same socket",
            "Spread loads across proper circuits",
        ),
        (
            "Open the board without isolating mains",
            "Shock and fire risk",
            "Loose terminals cause many dimming faults — but the distribution board must be worked on dead by someone qualified.",
            "Homeowner opening live distribution board with screwdriver to tighten wires",
            "Book an electrician for board work",
        ),
    ],
}

_FAQS = {
    "lights-dim-when-geyser-on-kashmir": [
        (
            "Why do lights dim when the geyser starts in Kashmir homes?",
            "High-watt geysers and heaters draw a surge of current when they switch on. If lights share that circuit "
            "or the wiring is undersized, voltage drops briefly and bulbs appear dimmer.",
        ),
        (
            "Is dimming always dangerous?",
            "Brief dimming on an old shared circuit is common, but constant dimming, buzzing, hot boards, or tripping "
            "MCBs are warning signs that need an electrician.",
        ),
        (
            "Can I fix this by changing the MCB to a bigger one?",
            "No. A larger breaker without thicker cable increases fire risk. The fix is usually splitting circuits or "
            "upgrading wiring to match the load.",
        ),
        (
            "Should I use a voltage stabilizer?",
            "A stabilizer may help sensitive appliances on an unstable supply, but it does not replace proper "
            "circuit design for a geyser. An electrician should assess whether load splitting is the real fix.",
        ),
        (
            "When should I book an electrician for dimming lights?",
            "Book when dimming is persistent, worsens over time, affects several rooms, comes with a hot board, "
            "tripping breakers, or burning smells.",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 90 + index
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
        "Keep geysers and room heaters on dedicated circuits where possible, avoid stacking high-watt loads on one "
        "multi-plug, and have the board labelled before winter heating season."
    )
    guide["prevention_caption"] = "Separate heavy loads before cold weather stacks them on one line."
    guide["pro_tip"] = (
        "If dimming lasts the whole geyser heat-up and not just the first second, suspect a shared circuit or loose "
        "connection — not a failing bulb."
    )
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
