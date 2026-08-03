"""Batch 3 practical guides — third high-intent problem post per category."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "PLB-D03",
        "geyser-not-heating-kashmir",
        "Geyser not heating? Check power and the reset before you replace it",
        "Plumbing",
        "plumbing",
        "On a cold winter morning, the geyser indicator glows but the shower stays stubbornly lukewarm. Someone reaches for the thermostat dial and cranks it to maximum — which is rarely the first fix.",
        "Confirm the geyser switch and MCB are on, check the indicator or heating light, verify thermostat setting, and look for leaks or a dripping safety valve. Lukewarm water after these checks, burning smell, or repeated tripping needs a geyser technician.",
        "Geyser runs but water stays cold or lukewarm",
        "Tripped power, failed element, thermostat fault, or scale buildup",
        [
            "MCB tripped or wall switch turned off after an overload.",
            "Heating element failed after years of hard-water scaling.",
            "Thermostat stuck low, faulty, or accidentally set to vacation mode.",
        ],
        [
            (
                "Confirm power is actually on",
                "any no-heat complaint",
                "Check the dedicated geyser switch, the bathroom MCB, and whether other loads on that circuit work.",
            ),
            (
                "Read the indicator lights",
                "a glowing panel but cold water",
                "Note whether the heating LED stays on, flickers, or never activates when hot water is drawn.",
            ),
            (
                "Check thermostat setting",
                "lukewarm not cold",
                "Set a sensible temperature and wait fifteen minutes; avoid maxing the dial to compensate.",
            ),
            (
                "Look for leaks and valve drip",
                "safety and pressure issues",
                "Inspect the tank base, pipe joints, and pressure relief valve for active dripping or rust streaks.",
            ),
            (
                "Book element or thermostat service",
                "no improvement after checks",
                "A technician can test the element, descale if needed, and replace a faulty thermostat safely.",
            ),
        ],
        "The element had scaled up; a proper descale fixed it without replacing the whole tank.",
        "Imtiyaz",
        "Hard water and a cold inlet in winter make geysers work harder in Kashmir. Scaling often shows up as longer heat-up times long before the tank stops completely.",
        "Do not bypass the thermostat, open the tank cover yourself, or ignore a burning smell or hot outer shell.",
        "Book a geyser technician for no heat after power checks, a tripping MCB, leaking tank, dripping relief valve, or water that suddenly runs very hot then cold.",
    ),
    _compact(
        "ELC-D03",
        "no-power-one-room-kashmir",
        "One room has no power? Find the right breaker before blaming the whole house",
        "Electrical",
        "electrician",
        "The bedroom goes dark after a heater runs all evening, but the kitchen still hums. Someone checks the main meter outside while the answer is probably one switch down the hall.",
        "Check whether only one room is affected, reset the matching MCB once with loads unplugged, test a socket with a simple lamp or charger, and look for a tripped RCCB or loose switch plate. Burning smell, heat, scorch marks, or a breaker that trips again need an electrician.",
        "Lights and sockets dead in one room only",
        "Tripped MCB, overloaded circuit, loose connection, or RCCB trip",
        [
            "A heater, geyser, or kettle overloaded that room's circuit.",
            "Loose wire at a socket or switch on the affected line.",
            "RCCB or combined MCB protecting multiple points has tripped.",
        ],
        [
            (
                "Confirm it is one room only",
                "first triage",
                "Switch on lights in other rooms and note whether the whole flat is dark or just one area.",
            ),
            (
                "Unplug and reset the MCB once",
                "a likely trip",
                "Remove heaters and kettles on that circuit, push the matching breaker fully off, then on once.",
            ),
            (
                "Test a socket simply",
                "checking supply",
                "Plug a phone charger or table lamp into a socket in the dark room and see if it gets power.",
            ),
            (
                "Check RCCB and labelled breakers",
                "partial or recurring loss",
                "Look for a wider trip affecting several rooms or a breaker label that matches the bedroom or bathroom.",
            ),
            (
                "Book an electrician",
                "trip returns or danger signs",
                "A pro can test the circuit, tighten connections, and find faults behind the board safely.",
            ),
        ],
        "It was the bedroom circuit breaker, not the meter. One reset after unplugging the heater fixed it.",
        "Sajad",
        "Winter evenings load bedroom circuits with heaters and blowers while other rooms stay lighter. A single-room blackout often traces to that one overloaded line.",
        "Do not hold a tripping MCB up, touch a wet switch, or open the distribution board without isolating mains.",
        "Book an electrician if the breaker trips again, you smell burning, see scorch marks, hear buzzing, or multiple rooms stay dead after one reset.",
    ),
    _compact(
        "APP-WM-D03",
        "washing-machine-not-draining-kashmir",
        "Washing machine not draining? Check the filter before you call it dead",
        "Home Appliances",
        "home-appliances",
        "After a heavy winter wash, the machine stops mid-cycle with water sitting in the drum. Someone tries to restart it three times; the pump hums but the level does not drop.",
        "Stop the cycle, unplug the machine, check the drain hose for kinks, clean the front filter or pump trap, and run a spin-only empty cycle. Standing water after a clean filter, burning smell, or error codes need appliance repair.",
        "Water left in drum after wash or spin",
        "Blocked filter, kinked drain hose, clogged pump, or failed drain motor",
        [
            "Lint, coins, or fabric trapped in the pump filter.",
            "Drain hose kinked, too high, or pushed behind the machine.",
            "Pump impeller blocked or motor failing after years of use.",
        ],
        [
            (
                "Stop and unplug the machine",
                "any standing water",
                "Cancel the cycle, switch off, and unplug before opening filters or hoses.",
            ),
            (
                "Check the drain hose run",
                "slow or partial drain",
                "Pull the machine forward slightly and look for kinks, pinches, or a hose loop above the recommended height.",
            ),
            (
                "Clean the pump filter trap",
                "water after every wash",
                "Place a shallow tray, open the front filter cover, and clear lint, coins, and debris from the trap.",
            ),
            (
                "Run spin-only empty",
                "after cleaning",
                "With the filter reseated, run a short spin cycle with an empty drum to confirm drainage.",
            ),
            (
                "Book appliance repair",
                "pump hums but no drain",
                "A technician can test the drain pump, clear internal blockages, and replace a failed motor safely.",
            ),
        ],
        "A sock was wedged in the filter; the pump had been working against it for weeks.",
        "Nighat",
        "Heavy pherans and thick blankets in winter loads shed more lint in Kashmir homes. A filter clean every few weeks prevents many mid-cycle stops.",
        "Do not tip the machine to force water out, ignore burning smells from the pump, or poke the impeller while plugged in.",
        "Book appliance repair if water remains after filter cleaning, the pump makes grinding noise, error codes return, or the machine leaks when draining.",
    ),
    _compact(
        "PST-D03",
        "rat-signs-home-kashmir",
        "Rats in the kitchen or ceiling? Spot the signs before they multiply",
        "Pest Control",
        "pest-control",
        "At 1 am, something skitters above the false ceiling while the kitchen smells faintly musky in the morning. One dropping behind the fridge is rarely the whole story.",
        "Look for droppings, grease rub marks, gnawed packets, and night scratching. Remove food overnight, seal entry gaps after inspection, and use traps correctly. Daytime sightings, ceiling damage, or repeat activity after DIY steps need pest control.",
        "Scratching at night, droppings, or chewed food packets",
        "Food and shelter route through kitchen gaps, pipes, or ceiling voids",
        [
            "Open food, pet bowls, and crumbs left out overnight.",
            "Gaps around pipes, doors, and false-ceiling access panels.",
            "Stored cardboard, firewood, or clutter giving hiding routes.",
        ],
        [
            (
                "Inspect with a torch after dark",
                "first suspicion",
                "Check behind the fridge, under the sink, along skirting, and near ceiling access panels for droppings or grease marks.",
            ),
            (
                "Remove food and rubbish overnight",
                "every kitchen",
                "Store dry food sealed, empty bins, wipe stove grease, and lift pet food off the floor before bed.",
            ),
            (
                "Find entry gaps calmly",
                "repeat activity",
                "Look for holes around pipes, door bottoms, and broken vent covers; note size and location before sealing.",
            ),
            (
                "Set traps in the right places",
                "low-level activity",
                "Place traps along walls where droppings appear, not in the open middle of the room.",
            ),
            (
                "Book pest control",
                "ceiling noise or daytime rats",
                "A professional can map routes, treat safely, and seal entry points after the population drops.",
            ),
        ],
        "They found the route behind the sink pipe cover; sealing after treatment stopped the night runs.",
        "Rafiq",
        "Winter stores, firewood stacks, and closed windows can push rats toward warm kitchen voids in Kashmir homes. Night scratching in a false ceiling deserves early action, not waiting for chewed wiring.",
        "Do not scatter poison without a plan, seal holes while rats are still inside, or leave pet food and open grain sacks out overnight.",
        "Book pest control for daytime sightings, ceiling damage, gnawed wires, smell that persists after cleaning, or rats returning within two weeks of DIY trapping.",
    ),
    _compact(
        "CLN-D05",
        "kitchen-grease-cleaning-kashmir",
        "Kitchen grease and chimney buildup? Cut the film before it turns sticky",
        "Cleaning",
        "professional-cleaning",
        "After a week of heavy cooking, the stove knobs feel tacky, the chimney mesh looks tar-black, and the cabinet above the hob has a faint yellow haze. A quick wipe with plain water only spreads it.",
        "Degrease the hob and backsplash while warm-not-hot, soak and scrub the chimney filter mesh, wipe cabinet fronts with the right cleaner, and improve ventilation. Thick carbon, smoke back-draft, or grease dripping onto food prep areas needs professional kitchen cleaning.",
        "Sticky hob, dark chimney filter, yellow grease film on tiles",
        "Oil vapour settling on cool surfaces and an overdue filter clean",
        [
            "Daily frying and boiling without wiping splatter while it is fresh.",
            "Chimney filter mesh clogged with trapped oil and dust.",
            "Poor ventilation in a closed winter kitchen letting grease condense on cabinets.",
        ],
        [
            (
                "Wipe splatter while warm",
                "after each cook session",
                "Switch off the flame, let surfaces cool slightly, then wipe the hob and backsplash with hot water and dish soap.",
            ),
            (
                "Remove and soak the chimney filter",
                "a weak suction smell",
                "Take out the mesh or baffle, soak in hot water with degreaser, then scrub gently and dry fully before refitting.",
            ),
            (
                "Degrease cabinet fronts and tiles",
                "yellow sticky film",
                "Use a kitchen degreaser on a cloth, test a hidden spot first, and wipe vertically to avoid streaks.",
            ),
            (
                "Check ventilation and hood airflow",
                "smoke while frying",
                "Run the chimney on high while cooking and confirm air is drawing up, not leaking around the hood.",
            ),
            (
                "Book a kitchen deep clean",
                "heavy carbon or repeat buildup",
                "A pro can clean hood ducts, behind appliances, and stubborn grease safely.",
            ),
        ],
        "Soaking the filter overnight did more than a month of surface wipes.", "Shazia",
        "Closed Kashmir kitchens in winter trap steam and oil vapour against cold upper cabinets. A filter clean before the festive cooking season prevents sticky buildup and weak chimney suction.",
        "Do not mix bleach with degreaser, spray flammable cleaner near a lit hob, or ignore a chimney that smells of hot grease.",
        "Book kitchen cleaning for carbonized hood parts, grease dripping near food areas, persistent smoke in the room, or a chimney that no longer pulls air after filter cleaning.",
    ),
]

_BATCH12_SIBLINGS = {
    "PLB-D03": ("how-to-unblock-kitchen-sink-drain-kashmir", "drain-smell-causes-kashmir"),
    "ELC-D03": ("mcb-keeps-tripping-kashmir", "flickering-lights-causes-kashmir"),
    "APP-WM-D03": ("ac-not-cooling-kashmir", "ac-leaking-water-kashmir"),
    "PST-D03": ("cockroach-control-home-kashmir", "termite-signs-home-kashmir"),
    "CLN-D05": ("sofa-smells-stains-cleaning", "bathroom-mould-hard-water-stains"),
}

TITLE_SUBJECTS = {
    "geyser-not-heating-kashmir": "wall-mounted geyser with indicator light, thermostat dial and MCB switch",
    "no-power-one-room-kashmir": "MCB board with one tripped breaker and dark room light fitting",
    "washing-machine-not-draining-kashmir": "front-load washing machine drain filter trap and drain hose",
    "rat-signs-home-kashmir": "kitchen rat droppings grease marks and ceiling void entry gap",
    "kitchen-grease-cleaning-kashmir": "kitchen chimney hood filter mesh and greasy stove backsplash",
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 32 + index
    b1, b2 = _BATCH12_SIBLINGS.get(guide["id"], (None, None))
    related = [s for s in (b1, b2) if s]
    guide["relatedGuideSlugs"] = related
    if guide["slug"] == "kitchen-grease-cleaning-kashmir":
        guide["dont_blocks"] = [
            (
                "Mix bleach with degreaser",
                "Toxic fumes in small kitchen",
                "Combining bleach-based cleaners with degreasers releases dangerous gas in enclosed spaces.",
                "Bleach bottle and degreaser spray mixed in kitchen sink",
                "One product at a time",
            ),
            (
                "Spray cleaner near lit hob",
                "Flammable vapour risk",
                "Aerosol degreasers near an open flame or hot plate can ignite suddenly.",
                "Degreaser spray aimed at greasy hob with flame still on",
                "Switch off and cool first",
            ),
            (
                "Ignore a smoking chimney hood",
                "Fire and carbon buildup",
                "A hood that smells hot or drips grease may have blocked ducts or a failing filter.",
                "Kitchen chimney hood with smoke escaping around edges and black filter",
                "Clean or book service",
            ),
        ]
    elif guide["slug"] == "rat-signs-home-kashmir":
        guide["dont_blocks"] = [
            (
                "Scatter poison without a plan",
                "Rats die in hidden voids",
                "Random poison can leave rodents decaying in ceilings or walls, causing smell and fly problems.",
                "Loose rat poison pellets scattered across kitchen floor",
                "Targeted professional treatment",
            ),
            (
                "Seal holes while rats are inside",
                "Traps them in the home",
                "Blocking entry points before the population is reduced can force rats into living areas.",
                "Foam sealant blocking pipe gap while rat route still active",
                "Treat and trap first",
            ),
            (
                "Leave pet food out overnight",
                "Feeds the problem nightly",
                "A full pet bowl on the floor is a reliable midnight meal for rats and mice.",
                "Pet food bowl on kitchen floor beside open grain sack at night",
                "Store food sealed",
            ),
        ]
    elif guide["slug"] == "washing-machine-not-draining-kashmir":
        guide["dont_blocks"] = [
            (
                "Tip the machine to pour water out",
                "Damages drum suspension and leaks",
                "Tipping a washer stresses mounts and hoses; water can flood electrical parts underneath.",
                "Washing machine tipped on its side with water spilling onto floor",
                "Use the drain filter instead",
            ),
            (
                "Keep restarting with a full drum",
                "Burns out the drain pump",
                "Running the pump against a solid blockage overheats the motor and can ruin it.",
                "Washing machine display showing error while drum still full of water",
                "Stop and clean filter",
            ),
            (
                "Poke the pump while plugged in",
                "Shock and injury risk",
                "The pump area is near live parts; always unplug before opening the filter or rear panel.",
                "Metal tool reaching into washing machine pump opening while cord plugged in",
                "Unplug first",
            ),
        ]
    elif guide["slug"] == "no-power-one-room-kashmir":
        guide["dont_blocks"] = [
            (
                "Hold the MCB up with tape",
                "Bypasses safety protection",
                "Forcing a tripping breaker to stay on can overheat wiring and hide a serious fault.",
                "MCB lever taped in ON position on electrical board",
                "Find the cause first",
            ),
            (
                "Touch switches when hands are wet",
                "Shock risk in bathrooms",
                "Wet hands and metal switch plates are a dangerous mix when a circuit is faulting.",
                "Wet bathroom light switch beside steaming mirror",
                "Dry hands and isolate",
            ),
            (
                "Open the board without isolating mains",
                "Live parts inside",
                "Distribution boards contain live busbars; opening the cover without proper isolation is unsafe.",
                "Distribution board cover removed exposing live busbars",
                "Book an electrician",
            ),
        ]
    elif guide["slug"] == "geyser-not-heating-kashmir":
        guide["isTrending"] = True
        guide["dont_blocks"] = [
            (
                "Crank thermostat to maximum",
                "Masks a fault and risks scalding",
                "Turning the dial to max does not fix a failed element; it can overheat water and stress safety parts.",
                "Hand turning geyser thermostat dial to maximum on lukewarm shower morning",
                "Check power and element first",
            ),
            (
                "Open the tank cover yourself",
                "Live wiring and pressure risk",
                "Geyser internals carry mains voltage and hot water under pressure; DIY opening is dangerous.",
                "Screwdriver opening electric geyser cover panel in bathroom",
                "Book a technician",
            ),
            (
                "Ignore a dripping safety valve",
                "Pressure or heating fault",
                "A relief valve that drips constantly can signal over-pressure, failed thermostat, or scaling.",
                "Pressure relief valve dripping onto geyser pipe with rust stain below",
                "Get it checked promptly",
            ),
        ]
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
