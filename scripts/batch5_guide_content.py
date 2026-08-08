"""Batch 5 — daily SEO DIY guides (published from 2026-08-07)."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "APP-RF-D01",
        "refrigerator-not-cooling-kashmir",
        "Refrigerator not cooling? Check vents and the door seal before calling",
        "Home Appliances",
        "home-appliances",
        "The milk feels lukewarm on a warm afternoon, the freezer still has ice, and someone has already turned the dial to the coldest setting — which often makes frost worse, not better.",
        "Clear blocked vents, confirm the fridge is not pushed tight to the wall, check the door gasket for gaps, and set a mid-range temperature. Warm fridge with a silent compressor, heavy frost, water pooling, or food spoiling within a day needs appliance repair.",
        "Fridge section warm while the light still works",
        "Blocked airflow, poor door seal, dirty condenser, or a failing thermostat/compressor",
        [
            "Food packed against the rear vents choking cold air circulation.",
            "Door left ajar or a torn gasket letting warm air in.",
            "Dusty condenser coils or a fridge pushed flush against the wall with no breathing gap.",
        ],
        [
            (
                "Feel the vents and clear the load",
                "uneven cooling",
                "Pull tall bottles and trays away from the rear cold-air vents so air can circulate through both fridge and freezer.",
            ),
            (
                "Check the door seal with a paper strip",
                "a warm edge or condensation",
                "Close the door on a strip of paper; if it slides out easily all around, clean or realign the gasket before assuming a gas refill.",
            ),
            (
                "Give the back and sides breathing room",
                "a hot cabinet or weak cooling",
                "Pull the fridge a few centimetres from the wall, clear dust behind it carefully, and keep the top free of boxes.",
            ),
            (
                "Reset to a mid temperature",
                "dial cranked to maximum",
                "Set a middle setting, wait several hours with doors closed, and avoid packing hot leftovers straight onto shelves.",
            ),
            (
                "Book a cooling diagnosis",
                "still warm after airflow checks",
                "A technician can test the thermostat, fan, condenser, and sealed system — do not demand refrigerant before a leak check.",
            ),
        ],
        "The gasket was cracked at the bottom corner; a seal fix cooled the fridge without a gas refill.",
        "Zahoor",
        "Warm Kashmir afternoons plus a fridge packed after shopping days can overwhelm airflow. Winter load — bottled water and leftover wazwan trays — also blocks vents if shelves are overfilled.",
        "Do not puncture coolant lines, wash the compressor area with water, or keep resetting a fridge that stays silent and warm.",
        "Book appliance repair for a warm fridge after vent and seal checks, loud or silent compressor faults, heavy ice blocking airflow, water under the fridge, or food spoiling within a day.",
        hero="Warm milk is a clue — start with airflow and the door seal.",
        excerpt="Fridge warm but the light still works? Clear vents, check the door gasket, and give the condenser room to breathe before booking appliance repair in Kashmir.",
    ),
    _compact(
        "PLB-D05",
        "low-water-pressure-home-kashmir",
        "Low water pressure at home? Check the aerator and tank before blaming the line",
        "Plumbing",
        "plumbing",
        "The shower turns into a weak spray just as everyone needs to get ready, the kitchen tap coughs air, and someone says the whole colony line is down — even though the neighbour's hose still runs fine.",
        "Unscrew and clean the tap aerator, confirm the rooftop or loft tank has water, open the isolation valve fully, and compare pressure at two taps. Sudden drop in every fixture, muddy water, a silent pump, or a tank that will not fill needs a plumber.",
        "Weak flow from one or more taps",
        "Clogged aerator, half-closed valve, low tank level, or a supply/pump fault",
        [
            "Mineral scale or debris packed inside the tap aerator or shower head.",
            "Rooftop tank empty, half-closed outlet valve, or airlock after a refill.",
            "Failing booster pump, choked inlet strainer, or a partial main-line blockage.",
        ],
        [
            (
                "Clean the aerator or shower head",
                "one weak tap",
                "Unscrew the tip, rinse grit and scale, soak in mild vinegar if needed, then refit without overtightening.",
            ),
            (
                "Check tank level and outlet valve",
                "several upstairs taps weak",
                "Confirm water in the rooftop or loft tank and that the tank outlet valve is fully open.",
            ),
            (
                "Compare two fixtures",
                "deciding if it is local or whole-home",
                "Test the kitchen and bathroom; one weak point suggests a local clog, every point weak suggests tank, valve, or supply.",
            ),
            (
                "Listen for the pump and strainer",
                "a booster-fed flat",
                "Note whether the pump runs, trips, or stays silent when you open a tap; a clogged inlet strainer starves flow.",
            ),
            (
                "Book a pressure diagnosis",
                "no improvement after basics",
                "A plumber can check valves, pump performance, hidden kinks, and municipal or colony supply issues safely.",
            ),
        ],
        "The aerator was packed with grit; cleaning it restored the kitchen tap without touching the main line.",
        "Bilal",
        "Many Kashmir homes mix municipal hours with rooftop storage and a booster pump. After a dry spell or tank clean, air and debris often lodge in aerators before anything is wrong with the street line.",
        "Do not dismantle a pressurised pump while powered, force a seized valve with a long lever, or ignore a sudden total loss of water with a burning pump smell.",
        "Book a plumber for whole-home low pressure after aerator and tank checks, a pump that runs dry or trips, muddy or no water after supply hours, or a tank that will not refill.",
        hero="Weak shower first — clean the tip and check the tank.",
        excerpt="Low water pressure in a Kashmir home? Clean the aerator, check the rooftop tank and valves, then know when a plumber should inspect the pump or line.",
    ),
    _compact(
        "ELC-D05",
        "ceiling-fan-making-noise-kashmir",
        "Ceiling fan making noise? Tighten the canopy before replacing the motor",
        "Electrical",
        "electrician",
        "The bedroom fan starts a metallic tick every night just as the room settles, then a wobble that makes the light kit shiver — and someone reaches for oil without killing the power first.",
        "Switch the fan off at the wall, tighten visible canopy and blade screws, check that blades are not bent or unequal, and test on a medium speed. Burning smell, sparking, a hot switch, or noise that returns after a careful tighten needs an electrician.",
        "Tick, rattle, or hum from a running ceiling fan",
        "Loose canopy screws, unbalanced blades, worn bearings, or a switch/regulator fault",
        [
            "Canopy or downrod screws loosened by vibration over months.",
            "One blade slightly bent, dusty, or fitted with a different pitch.",
            "Dry bearings, a failing capacitor, or a loose wall regulator connection.",
        ],
        [
            (
                "Kill power and tighten the canopy",
                "a tick from the ceiling rose",
                "Switch off the fan and MCB if needed, then snug the canopy and downrod screws without stripping them.",
            ),
            (
                "Check blade screws and balance",
                "a wobble or slap",
                "Confirm each blade screw is firm and blades look even; clean heavy dust that pulls one side off balance.",
            ),
            (
                "Test speeds after a clean tighten",
                "noise only on one setting",
                "Run low and medium first; a regulator that crackles or smells warm is an electrical issue, not a blade issue.",
            ),
            (
                "Note bearing or motor sounds",
                "a grind that survives tightening",
                "A deep grind or squeal that continues after screws are tight often means bearings or motor service.",
            ),
            (
                "Book an electrician",
                "sparking, heat, or repeat noise",
                "A pro can check the capacitor, regulator, earthing, and secure the fan without DIY live work.",
            ),
        ],
        "Two loose canopy screws were the whole tick; no motor replacement needed.",
        "Idrees",
        "Kashmir fans run long hours in summer and sit through damp winters. Screw vibration plus seasonal expansion often sounds like a failing motor when it is only a canopy that needs a safe tighten.",
        "Do not oil a live fan, stand on unstable furniture under a spinning blade, or ignore sparking at the regulator.",
        "Book an electrician for sparking, burning smell, a hot switch, noise after screws are tight, a severe wobble, or a fan that trips the MCB.",
        hero="A tick from the ceiling often starts with loose screws — power off first.",
        excerpt="Ceiling fan ticking or wobbling in Kashmir? Tighten the canopy and blades safely, check balance, and know when noise means an electrician — not more oil.",
    ),
    _compact(
        "PLB-D06",
        "toilet-keeps-running-kashmir",
        "Toilet keeps running? Check the flapper and fill valve before wasting a tank a day",
        "Plumbing",
        "plumbing",
        "At 2 a.m. the cistern refills again with that soft hiss nobody wants to hear, the water bill is climbing, and someone jiggles the handle hoping the phantom flush will stop.",
        "Lift the cistern lid, see if the flapper seals after a flush, adjust or replace a worn flapper, and check that the fill valve shuts off at the right water line. A cracked cistern, stuck fill valve, or leak onto the floor needs a plumber.",
        "Toilet runs, hisses, or refills without being used",
        "Worn flapper, mis-set float, faulty fill valve, or a leaking overflow",
        [
            "Rubber flapper warped, slimy, or no longer sealing the flush valve seat.",
            "Float set too high so water spills into the overflow tube.",
            "Fill valve not shutting off, or a chain tangled so the flapper stays open.",
        ],
        [
            (
                "Listen and watch after a flush",
                "any running cistern",
                "Flush once, wait; if water keeps entering or the level creeps to the overflow, note whether the flapper or fill side is the culprit.",
            ),
            (
                "Seat the flapper and free the chain",
                "a hiss after flush",
                "Make sure the chain has a little slack, the flapper drops centred on the seat, and nothing is trapping it open.",
            ),
            (
                "Set the water line below the overflow",
                "water trickling into the overflow tube",
                "Adjust the float or fill-valve screw so the level stops about a finger below the overflow rim.",
            ),
            (
                "Replace a worn flapper",
                "an old soft seal that never seats",
                "Match the flush-valve size, fit a new flapper, and test a few flushes for a quiet stop.",
            ),
            (
                "Book a plumber",
                "still running or leaking outside",
                "A pro can replace a failing fill valve, reseat a flush valve, or fix a cracked cistern without flooding the bathroom.",
            ),
        ],
        "A new flapper stopped the night hiss; we had been wasting a tank every few hours.",
        "Shaista",
        "Hard water and long idle seasons in Kashmir bathrooms age flapper rubber quickly. A quiet overnight run can waste more water than a busy daytime household notices.",
        "Do not force the cistern lid if it is stuck, add random weights to a float, or ignore water pooling at the toilet base.",
        "Book a plumber for a cistern that will not stop after flapper and float checks, water at the base, a cracked tank, or a fill valve that will not shut off.",
        hero="A night-time hiss usually means the flapper or fill valve — not a mystery leak in the wall.",
        excerpt="Toilet keeps running in Kashmir? Check the flapper seal and fill-valve level safely, stop wasting water overnight, and know when to book a plumber.",
    ),
    _compact(
        "PLB-D07",
        "tap-keeps-dripping-kashmir",
        "Tap keeps dripping? Fix the washer before wasting a bucket overnight",
        "Plumbing",
        "plumbing",
        "After dinner the kitchen tap still ticks into the sink every few seconds, someone has already tightened the handle harder, and the stainless bowl has a chalky ring that was not there last week.",
        "Turn off the isolation valve, open the tap to drain pressure, replace a worn washer or cartridge, and reseat the spindle carefully. A cracked body, seized spindle, or drip from the base needs a plumber.",
        "Steady drip from a closed tap",
        "Worn washer, damaged seat, failing cartridge, or a loose spindle packing",
        [
            "Rubber washer flattened or cracked so the spindle never seals fully.",
            "Mineral scale on the valve seat keeping a tiny gap open.",
            "Cartridge or ceramic disc worn inside a modern mixer tap.",
        ],
        [
            (
                "Isolate and drain the tap",
                "any drip you plan to open",
                "Close the under-sink or wall isolation valve, open the tap to release pressure, and put a plug in the sink so small parts cannot fall down the drain.",
            ),
            (
                "Open the handle and check the washer",
                "a classic two-handle tap",
                "Remove the handle and headgear, lift out the old washer, and note size before fitting a matching replacement.",
            ),
            (
                "Clean the seat and refit snugly",
                "scale under the washer",
                "Wipe grit from the valve seat, fit the new washer flat, and tighten the headgear firmly without crushing the spindle.",
            ),
            (
                "Treat a mixer cartridge differently",
                "a single-lever mixer that drips",
                "Many mixers need a cartridge swap, not a washer — match the brand shape or photograph the old part before buying.",
            ),
            (
                "Book a plumber",
                "still dripping or parts seized",
                "A pro can re-seat a scored valve, free a stuck spindle, or replace a cracked body without flooding the cabinet.",
            ),
        ],
        "A two-rupee washer stopped the night drip; we had been filling a mug every hour.",
        "Firdous",
        "Hard water in many Kashmir homes ages washers and seats faster. A quiet overnight drip also empties rooftop storage and leaves chalky rings that look worse than the leak feels.",
        "Do not force a seized spindle with pliers on chrome, leave the main supply open while the tap is apart, or ignore a drip from the base that may be wetting the cabinet floor.",
        "Book a plumber for a drip that continues after a washer or cartridge change, a seized or stripped spindle, water at the tap base, or a cracked body.",
        hero="A steady drip is usually a washer or cartridge — not a mystery pipe in the wall.",
        excerpt="Tap keeps dripping in Kashmir? Isolate the supply, replace a worn washer or mixer cartridge, and know when a plumber should fix a seized spindle or cracked body.",
    ),
    _compact(
        "APP-WM-D02",
        "washing-machine-not-spinning-kashmir",
        "Washing machine not spinning? Check the load and lid switch before the motor",
        "Home Appliances",
        "home-appliances",
        "The wash cycle finishes, clothes sit heavy and dripping, and someone opens the door early hoping a second spin will magically start — while the drum only hums or stays still.",
        "Redistribute an unbalanced load, confirm the lid or door is fully latched, select a proper spin programme, and drain standing water first if the drum will not turn. Burning smell, repeated error codes, or a silent motor after these checks needs appliance repair.",
        "Washer fills or washes but will not spin dry",
        "Unbalanced load, open lid switch, drain fault, or a failing motor/belt/clutch",
        [
            "Clothes bunched on one side triggering the imbalance sensor.",
            "Lid or door switch not closing, so spin is locked for safety.",
            "Water still in the drum, a blocked pump, or a worn belt/motor that cannot reach spin speed.",
        ],
        [
            (
                "Stop and redistribute the load",
                "a thud-thud then cancel",
                "Pause the cycle, spread wet clothes evenly around the drum, and avoid one heavy blanket alone on a high spin.",
            ),
            (
                "Confirm the lid or door latch",
                "spin locked with a door alert",
                "Close firmly until it clicks; clean lint from the latch area and try again before assuming a motor fault.",
            ),
            (
                "Drain first if water is sitting",
                "a heavy waterlogged drum",
                "Run a drain or spin-only programme; a full drum of water often will not accelerate into spin.",
            ),
            (
                "Check the filter and hose path",
                "slow drain before spin",
                "On front-loaders, clear the pump filter carefully with a towel ready; kinks in the drain hose also stall spin.",
            ),
            (
                "Book appliance repair",
                "humming, burning smell, or repeat faults",
                "A technician can test the lid switch, belt, clutch, motor, and control board without forcing a stuck drum.",
            ),
        ],
        "One soaked quilt on one side was the whole problem; evening the load brought spin back.",
        "Nayeem",
        "Kashmir winter washes often mean heavy blankets and pherans in a single load. That uneven mass trips imbalance protection far more often than a dead motor.",
        "Do not force the drum by hand while powered, bypass a door switch with tape, or keep restarting a machine that smells of burning rubber or plastic.",
        "Book appliance repair for a washer that will not spin after load and latch checks, error codes that return, a burning smell, leaks, or a motor that only hums.",
        hero="Heavy wet clothes and a half-open lid stop spin more often than a failed motor.",
        excerpt="Washing machine not spinning in Kashmir? Redistribute the load, check the lid latch and drain, then know when appliance repair should inspect the motor or belt.",
    ),
    _compact(
        "ELC-D06",
        "wall-socket-sparking-kashmir",
        "Wall socket sparking? Unplug and kill the MCB before it becomes a fire risk",
        "Electrical",
        "electrician",
        "A soft crackle when the heater plug goes in, a warm faceplate by evening, and someone says it has always been like that — until the smell of hot plastic arrives.",
        "Unplug the appliance, switch off the MCB for that circuit, stop using the socket, and check for a loose plug or overloaded multi-plug. Scorch marks, a hot plate, repeated sparks, or a socket in a damp area need an electrician before anyone rewires at home.",
        "Spark, crackle, or heat at a wall socket when plugging in",
        "Loose terminals, damaged plug pins, overloaded strip, or failing socket contacts",
        [
            "Loose live or neutral screws inside the socket box making intermittent contact.",
            "Bent or blackened plug pins arcing every time they enter.",
            "Too many heaters on one multi-plug or a cracked, age-worn socket.",
        ],
        [
            (
                "Unplug and kill the circuit",
                "any spark or warm plate",
                "Pull the plug if safe, switch the socket off, then turn off the MCB for that board before touching the faceplate.",
            ),
            (
                "Inspect the plug and cord",
                "spark only with one appliance",
                "Look for bent pins, cracked plugs, or a frayed cord; try a known-good plug only after the socket has cooled and the MCB is back on briefly for a test.",
            ),
            (
                "Stop using overloaded strips",
                "heaters sharing one outlet",
                "Move high-load appliances off daisy-chained multi-plugs; one socket, one heavy load is safer while you wait for repair.",
            ),
            (
                "Note scorch and smell",
                "brown marks or hot plastic odour",
                "Photograph discolouration for the electrician and do not cover a warm plate with cloth or tape.",
            ),
            (
                "Book an electrician",
                "repeat spark, heat, or trip",
                "A pro can retighten terminals, replace the socket, check earthing, and confirm the circuit can carry the load.",
            ),
        ],
        "The socket screws were loose behind a warm plate; tightening and a new faceplate stopped the crackle.",
        "Iqbal",
        "Kashmir winters push heaters, geysers, and kettles onto the same boards. Loose old sockets plus heavy load is a common spark recipe — not a quirk to ignore.",
        "Do not keep plugging in through sparks, open a live socket with a screwdriver, wrap a warm plate in tape, or ignore a burning smell.",
        "Book an electrician for any repeating spark, hot or discoloured faceplate, socket in a wet area, MCB trips with that outlet, or wiring that smells of burning.",
        hero="A crackle at the plug is a warning — cut power before it becomes smoke.",
        excerpt="Wall socket sparking in Kashmir? Unplug, switch off the MCB, stop using overloaded strips, and know when an electrician must replace the socket.",
    ),
]

_BATCH_SIBLINGS = {
    "APP-RF-D01": (
        "ac-not-cooling-kashmir",
        "washing-machine-not-draining-kashmir",
        "geyser-not-heating-kashmir",
    ),
    "PLB-D05": (
        "how-to-unblock-kitchen-sink-drain-kashmir",
        "geyser-not-heating-kashmir",
        "drain-smell-causes-kashmir",
    ),
    "ELC-D05": (
        "flickering-lights-causes-kashmir",
        "mcb-keeps-tripping-kashmir",
        "no-power-one-room-kashmir",
    ),
    "PLB-D06": (
        "low-water-pressure-home-kashmir",
        "how-to-unblock-kitchen-sink-drain-kashmir",
        "drain-smell-causes-kashmir",
    ),
    "PLB-D07": (
        "toilet-keeps-running-kashmir",
        "low-water-pressure-home-kashmir",
        "how-to-unblock-kitchen-sink-drain-kashmir",
    ),
    "APP-WM-D02": (
        "washing-machine-not-draining-kashmir",
        "refrigerator-not-cooling-kashmir",
        "geyser-not-heating-kashmir",
    ),
    "ELC-D06": (
        "mcb-keeps-tripping-kashmir",
        "flickering-lights-causes-kashmir",
        "ceiling-fan-making-noise-kashmir",
    ),
}

TITLE_SUBJECTS = {
    "refrigerator-not-cooling-kashmir": "refrigerator with rear vents, door gasket seal test and condenser airflow",
    "low-water-pressure-home-kashmir": "tap aerator, rooftop water tank valve and shower with weak spray",
    "ceiling-fan-making-noise-kashmir": "ceiling fan canopy screws, blade balance and wall regulator",
    "toilet-keeps-running-kashmir": "toilet cistern flapper seal, fill valve float and overflow tube",
    "tap-keeps-dripping-kashmir": "kitchen tap drip, worn washer, valve seat and mixer cartridge",
    "washing-machine-not-spinning-kashmir": "washing machine drum, unbalanced wet load, lid latch and spin cycle",
    "wall-socket-sparking-kashmir": "wall socket spark, warm faceplate, plug pins and MCB switch-off",
}

_SEO = {
    "refrigerator-not-cooling-kashmir": {
        "seoTitle": "Fridge not cooling? Check vents first | Panun Kaergar",
        "seoDescription": (
            "Refrigerator not cooling in Kashmir? Clear vents, check the door seal, and give coils airflow "
            "before booking appliance repair."
        ),
    },
    "low-water-pressure-home-kashmir": {
        "seoTitle": "Low water pressure? Check aerator first | Panun Kaergar",
        "seoDescription": (
            "Low water pressure at home in Kashmir? Clean the tap aerator, check the rooftop tank and valves, "
            "then know when to book a plumber."
        ),
    },
    "ceiling-fan-making-noise-kashmir": {
        "seoTitle": "Ceiling fan noise? Tighten canopy first | Panun Kaergar",
        "seoDescription": (
            "Ceiling fan making noise in Kashmir? Switch off, tighten the canopy and blades, check balance, "
            "and know when to book an electrician."
        ),
    },
    "toilet-keeps-running-kashmir": {
        "seoTitle": "Toilet keeps running? Check flapper first | Panun Kaergar",
        "seoDescription": (
            "Toilet keeps running in Kashmir? Check the flapper seal and fill-valve level, stop overnight water "
            "waste, and know when to book a plumber."
        ),
    },
    "tap-keeps-dripping-kashmir": {
        "seoTitle": "Tap dripping? Replace washer first | Panun Kaergar",
        "seoDescription": (
            "Tap keeps dripping in Kashmir? Isolate the supply, replace a worn washer or mixer cartridge, and know "
            "when to book a plumber for a seized spindle."
        ),
    },
    "washing-machine-not-spinning-kashmir": {
        "seoTitle": "Washer not spinning? Check load first | Panun Kaergar",
        "seoDescription": (
            "Washing machine not spinning in Kashmir? Redistribute the load, check the lid latch and drain, then know "
            "when to book appliance repair."
        ),
    },
    "wall-socket-sparking-kashmir": {
        "seoTitle": "Socket sparking? Kill MCB first | Panun Kaergar",
        "seoDescription": (
            "Wall socket sparking in Kashmir? Unplug, switch off the MCB, stop overloaded strips, and know when to "
            "book an electrician."
        ),
    },
}

_DONT = {
    "refrigerator-not-cooling-kashmir": [
        (
            "Crank the dial to maximum",
            "Frost grows; food still spoils",
            "The coldest setting can freeze the rear wall and choke airflow without fixing a warm fridge section.",
            "Refrigerator temperature dial turned to maximum with frost on back wall",
            "Use a mid setting",
        ),
        (
            "Demand a gas refill first",
            "Skip diagnosis",
            "Many warm-fridge jobs are vents, seals, or dust — refrigerant should follow a leak and performance check.",
            "Technician testing fridge cooling before any refrigerant work",
            "Diagnose before refill",
        ),
        (
            "Wash the back with a hose",
            "Electrical risk",
            "Water on the compressor and electrics is dangerous. Dust carefully with the power off if you clean at all.",
            "Water spray near refrigerator compressor and electrical plug",
            "Keep electrics dry",
        ),
    ],
    "low-water-pressure-home-kashmir": [
        (
            "Blame the colony line first",
            "Miss a clogged aerator",
            "A neighbour with strong flow usually means your tip, valve, or tank is the first place to look.",
            "Weak kitchen tap beside neighbour hose running strongly",
            "Compare before calling the line",
        ),
        (
            "Force a stuck valve with a long pipe",
            "Snaps the spindle",
            "A seized isolation valve needs the right tool or a plumber — leverage often breaks it open and floods the area.",
            "Long metal pipe used as lever on small water valve",
            "Do not force seized valves",
        ),
        (
            "Run a dry booster pump",
            "Burns the motor",
            "A pump that runs with an empty tank or closed inlet overheats quickly and can fail permanently.",
            "Booster pump running while rooftop tank gauge shows empty",
            "Confirm water before pumping",
        ),
    ],
    "ceiling-fan-making-noise-kashmir": [
        (
            "Oil a spinning fan",
            "Injury and shock risk",
            "Never reach into blades that are moving, and never work on wiring with the wall switch still on.",
            "Hand reaching toward spinning ceiling fan with oil bottle",
            "Power off first",
        ),
        (
            "Ignore sparking at the regulator",
            "Fire and trip risk",
            "A crackling speed regulator is an electrical fault — stop using that control and book help.",
            "Wall fan regulator with spark icon and warm switch plate",
            "Stop at sparking",
        ),
        (
            "Bend blades by hand to 'fix' wobble",
            "Makes imbalance worse",
            "Forcing a blade changes pitch permanently; clean and tighten first, then let a pro balance it.",
            "Person bending ceiling fan blade by hand",
            "Do not force blades",
        ),
    ],
    "toilet-keeps-running-kashmir": [
        (
            "Ignore the overnight hiss",
            "Wastes tanks of water",
            "A quiet refill every few hours adds up on metered supply and empties rooftop storage faster than you notice.",
            "Toilet cistern quietly refilling at night with water meter icon",
            "Fix the seal early",
        ),
        (
            "Bend the float arm randomly",
            "Can crack old parts",
            "Adjust with the intended screw or clip; forcing brittle plastic often breaks the fill valve.",
            "Hands bending toilet cistern float arm roughly",
            "Use the proper adjustment",
        ),
        (
            "Keep flushing to 'reset' it",
            "Hides a bad flapper",
            "Repeated flushes do not reseat a warped flapper; replace or reseat the seal instead.",
            "Person repeatedly flushing running toilet handle",
            "Fix the seal, do not keep flushing",
        ),
    ],
    "tap-keeps-dripping-kashmir": [
        (
            "Tighten the handle harder",
            "Scores the seat",
            "Over-tightening flattens the washer and can cut a groove in the valve seat, making the drip worse.",
            "Hand forcing kitchen tap handle closed with dripping spout",
            "Replace the seal instead",
        ),
        (
            "Open the tap with supply still on",
            "Cabinet flood risk",
            "Always close the isolation valve and drain pressure before removing headgear or a cartridge.",
            "Tap headgear open while water sprays from under-sink pipe",
            "Isolate first",
        ),
        (
            "Force a stuck spindle with pliers on chrome",
            "Ruins the finish and spindle",
            "A seized spindle needs the right puller or a plumber — pliers on polished chrome often slip and gouge.",
            "Pliers gripping chrome tap spindle roughly",
            "Do not force seized parts",
        ),
    ],
    "washing-machine-not-spinning-kashmir": [
        (
            "Force the drum by hand while powered",
            "Injury and shock risk",
            "Never reach into a drum that may start, and never work inside with the machine plugged in.",
            "Hand inside washing machine drum while power cord is connected",
            "Unplug before any reach-in",
        ),
        (
            "Tape over the lid switch",
            "Safety lock defeated",
            "Bypassing the door or lid switch can let spin run with the door open — a serious injury hazard.",
            "Tape covering washing machine lid safety switch",
            "Fix the latch properly",
        ),
        (
            "Keep restarting through a burning smell",
            "Worsens motor or belt damage",
            "A rubber or electrical burn smell means stop and book repair — more cycles can finish the motor.",
            "Washing machine with heat and smoke hint near motor area",
            "Stop at burning smell",
        ),
    ],
    "wall-socket-sparking-kashmir": [
        (
            "Keep plugging through the spark",
            "Arc and fire risk",
            "Each spark can pit the contacts further. Stop using that outlet until it is repaired.",
            "Hand forcing plug into sparking wall socket",
            "Unplug and cut power",
        ),
        (
            "Open the socket live with a screwdriver",
            "Shock risk",
            "Never remove a faceplate or touch terminals while the MCB is still on.",
            "Screwdriver opening wall socket with power still on",
            "MCB off before any open-up",
        ),
        (
            "Tape over a warm faceplate",
            "Hides heat damage",
            "Covering a hot plate traps heat and hides scorch marks an electrician needs to see.",
            "Tape wrapped over warm discoloured wall socket",
            "Leave it open and book help",
        ),
    ],
}

GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    guide["sortOrder"] = 60 + index
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
