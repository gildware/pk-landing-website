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
    _compact(
        "CRP-D03",
        "kitchen-cabinet-door-sagging-kashmir",
        "Kitchen cabinet door sagging? Tighten the hinge before it rips the carcass",
        "Carpentry",
        "carpentry",
        "The upper cupboard door hangs crooked after months of heavy spice jars on the shelf, someone props it shut with a tea towel, and the soft-close hinge scrapes the neighbouring door every time it opens.",
        "Support the door, tighten hinge screws into solid carcass wood, adjust the side-to-side and depth screws on a modern cup hinge, and check that the mounting plate is not pulling out. Stripped screw holes, a cracked door, or a ripped particleboard edge needs a carpenter.",
        "Cabinet door hangs low, rubs, or will not stay shut",
        "Loose hinge screws, misadjusted cup hinge, or a failing mounting plate in soft board",
        [
            "Hinge screws worked loose from daily open-close and heavy door weight.",
            "Cup-hinge adjustment screws drifted so the door sits low or out of line.",
            "Particleboard holes stripped or the mounting plate pulling away from the carcass.",
        ],
        [
            (
                "Support the door and snug the screws",
                "a drooping or rattling door",
                "Have someone hold the door level, then tighten the hinge screws into the carcass and door — stop if a screw spins freely in a stripped hole.",
            ),
            (
                "Adjust the cup-hinge screws",
                "a modern soft-close or Euro hinge",
                "Use the side and depth adjustment screws in small turns so the door aligns with its neighbour and clears the frame without forcing.",
            ),
            (
                "Check the mounting plate and cup",
                "a plate lifting from the board",
                "Look for gaps under the plate, cracked laminate around the cup, or screws that no longer bite — those need repair, not more torque.",
            ),
            (
                "Rescue a stripped hole carefully",
                "a spinning screw in soft board",
                "A wood plug, longer screw into solid timber, or a proper repair kit can restore grip; do not keep driving a larger screw into crumbling chipboard.",
            ),
            (
                "Book a carpenter",
                "ripped board, cracked door, or repeat sag",
                "A pro can relocate hinges, reinforce the carcass, replace worn soft-close units, and realign a run of doors properly.",
            ),
        ],
        "Two loose hinge screws and a tiny side adjustment lined the door up; we had nearly ordered a new shutter.",
        "Hina",
        "Kashmir kitchens mix heavy wooden shutters, soft particleboard carcasses, and damp seasons that swell doors. A slight hang after monsoon or winter heating is often a hinge job, not a full cabinet remake.",
        "Do not prop a heavy door with cloth forever, force a misaligned soft-close shut, or drive longer screws blindly into a thin carcass wall near a pipe or sink.",
        "Book a carpenter for stripped hinge holes, a cracked or delaminating door, a mounting plate torn from the board, doors that still sag after careful adjustment, or a full run of cupboards out of line.",
        hero="A crooked cupboard door usually starts with loose hinge screws — not a new kitchen.",
        excerpt="Kitchen cabinet door sagging in Kashmir? Support the door, tighten and adjust the hinges, and know when a carpenter should repair stripped holes or ripped board.",
    ),
    _compact(
        "PNT-D03",
        "paint-looking-patchy-streaky-kashmir",
        "Paint looking patchy or streaky? Fix prep before another coat",
        "Painting",
        "painting",
        "The living-room wall looks mottled the morning after a rushed weekend paint job, roller lines catch every afternoon light, and someone is already opening a third tin hoping more colour will hide the mess.",
        "Stop adding wet coats over a weak base. Sand high ridges lightly, wipe dust, spot-prime bare or patched areas, then roll thin even coats with a quality roller — keeping a wet edge. Active damp, peeling layers, or large colour mismatch needs a painter.",
        "Fresh paint looks blotchy, streaky, or shows roller marks",
        "Poor surface prep, skipped primer, overloaded roller, or coats applied too thick or too fast",
        [
            "Dust, grease, or unsanded putty patches absorbing paint unevenly.",
            "Bare plaster or filler left without primer so colour sinks in patches.",
            "A dripping roller, dried edge lines, or coats stacked before the previous one cured.",
        ],
        [
            (
                "Judge the wall in daylight",
                "any patchy finish",
                "Look across the surface with side light; mark high ridges, missed spots, and areas where old colour still ghosts through.",
            ),
            (
                "Sand and dust the problem zones",
                "roller ridges or rough putty",
                "Lightly sand shiny or raised lines, wipe with a clean dry cloth, and keep the floor free of grit before you open paint again.",
            ),
            (
                "Spot-prime bare and patched areas",
                "absorbent blotches",
                "Prime filler patches and scraped spots so the finish coat sits evenly instead of sinking into thirsty plaster.",
            ),
            (
                "Roll thin coats with a wet edge",
                "streaks and lap marks",
                "Load the roller evenly, work in overlapping W patterns, and finish each section before the edge dries — two thin coats beat one heavy coat.",
            ),
            (
                "Book a painter",
                "still patchy after careful rework",
                "A pro can assess damp, strip failing layers, level large areas, and match sheen across a full room without another wasted tin.",
            ),
        ],
        "Priming the putty patches stopped the blotches; the third full coat was never needed.",
        "Asiya",
        "Kashmir rooms often mix old limewash, modern emulsion, and winter dust from bukhari heat. Skipping primer on patched walls shows up fast once low afternoon sun hits the surface.",
        "Do not keep flooding a wet wall with thicker paint, paint over active damp or peeling film, or sand lead-suspect old coatings without protection.",
        "Book a painter for large patchy rooms after basic sand-and-prime fails, peeling or bubbling paint, suspected damp, ceiling work at height, or a full flat where colour and sheen must match.",
        hero="Patchy paint is usually prep and primer — not a missing third tin.",
        excerpt="Paint looking patchy or streaky in Kashmir? Sand dust, spot-prime patches, roll thin even coats, and know when a painter should take over.",
    ),
    _compact(
        "WMN-D06",
        "frizzy-dry-hair-after-wash-kashmir",
        "Frizzy dry hair after washing? Calm the cuticle before more heat",
        "Women's Salon",
        "womens-salon",
        "By afternoon the wash-day shine is gone, hair lifts into a dry halo in bukhari-heated rooms, and someone reaches for a hotter straightener hoping one more pass will flatten what moisture should have fixed.",
        "Rinse thoroughly, blot — do not rub — with a soft towel, apply leave-in or serum on damp lengths, air-dry or use low heat with protection, and sleep on a smoother pillowcase. Sudden breakage, scalp pain, or chemical damage needs a salon professional.",
        "Hair feels dry, frizzy, or static soon after washing",
        "Cuticle roughened by hard water, overwashing, heat, or dry indoor air",
        [
            "Hard water minerals and leftover shampoo film roughening the cuticle.",
            "Towel rubbing and high heat on dripping wet hair creating frizz.",
            "Dry indoor heating and cold outdoor air stripping moisture from lengths.",
        ],
        [
            (
                "Rinse until water runs clear",
                "product film and hard-water feel",
                "Spend extra time rinsing lengths and the nape; leftover shampoo and minerals make hair feel dry within hours.",
            ),
            (
                "Blot, do not rub",
                "wet hair after the wash",
                "Squeeze water out with a soft cotton or microfibre towel; rubbing lifts the cuticle and sets frizz before you even style.",
            ),
            (
                "Seal damp lengths",
                "frizz starting as hair dries",
                "Apply a light leave-in or serum mid-lengths to ends while hair is still damp — keep heavy oil off an already oily scalp.",
            ),
            (
                "Lower the heat and give it time",
                "daily straightener habit",
                "Air-dry when you can; if you style, use heat protection and a lower setting instead of chasing frizz with more heat.",
            ),
            (
                "Book a salon hair care visit",
                "persistent frizz or breakage",
                "A stylist can assess porosity, trim splitting ends, and plan a moisture treatment without another blind home chemical.",
            ),
        ],
        "Switching to blot-drying and a leave-in on damp lengths calmed the halo; the straightener came out far less often.",
        "Insha",
        "Kashmir winters mix hard water, bukhari-dry rooms, and cold outdoor air. Hair that feels fine after a wash can turn frizzy by evening unless the cuticle is sealed while damp.",
        "Do not blast soaking wet hair on the hottest setting, pile oil on an itchy scalp hoping lengths will soften, or bleach again to 'fix' dryness.",
        "Book women's salon hair care for persistent frizz after gentle routine changes, widespread split ends, chemical damage, painful scalp, or a treatment and trim before a big event.",
        hero="Afternoon frizz usually starts with a rough cuticle — not a hotter iron.",
        excerpt="Frizzy dry hair after washing in Kashmir? Rinse well, blot instead of rubbing, seal damp lengths, lower the heat, and know when to book a salon visit.",
    ),
    _compact(
        "WMN-D07",
        "hairfall-after-wash-kashmir",
        "Hairfall after every wash? Check breakage before blaming the roots",
        "Women's Salon",
        "womens-salon",
        "The bathroom drain holds a dark clump after every wash, someone panics about roots, and a neighbour recommends a stronger oil — before anyone checks whether the strands are snapping mid-length or shedding with a tiny white bulb.",
        "Look at the shed hair: a white bulb often means normal shedding; short snapped ends suggest breakage from heat, tight styles, or chemical stress. Ease rough handling, reduce heat, and strengthen the routine. Patchy bald spots, sudden heavy loss, or scalp pain need medical advice — a salon can help with breakage and gentle care.",
        "Extra hair in the drain, brush, or pillow after washing",
        "Seasonal shedding, breakage from damage, tight styling, or a scalp/medical issue",
        [
            "Normal seasonal or post-stress shedding with bulbs attached.",
            "Breakage from heat, bleach, tight buns, or rough towel drying.",
            "Scalp inflammation, sudden patchy loss, or hormonal/medical triggers needing a doctor.",
        ],
        [
            (
                "Inspect a few strands in good light",
                "any worrying wash-day clump",
                "Check whether hairs end in a small white bulb (shed) or look snapped and uneven (breakage) before changing products randomly.",
            ),
            (
                "Ease handling while wet",
                "snapping during combing",
                "Detangle from ends upward with a wide-tooth comb on wet hair; stop yanking through knots at the crown.",
            ),
            (
                "Cut the heat and tight pull",
                "breakage along the hairline or lengths",
                "Lower straightener temperature, skip daily tight buns for a while, and use heat protection when you do style.",
            ),
            (
                "Simplify scalp products",
                "itch or heavy oil buildup",
                "Wash with a gentle shampoo on a steady schedule; heavy overnight oils will not fix root shedding and can clog an irritated scalp.",
            ),
            (
                "Book salon care — or a doctor if red flags",
                "ongoing loss after gentle changes",
                "A stylist can trim damaged ends and plan restorative care for breakage; sudden patches, bald spots, or rapid thinning need a dermatologist.",
            ),
        ],
        "Most of the 'hairfall' in my brush was snapped mid-length from a tight bun and hot iron — not roots falling out.",
        "Saba",
        "Kashmir wash days often follow hard water, winter dryness, and festival heat styling. Clumps in the drain look alarming, but breakage and normal shedding need different next steps — oil alone rarely settles either.",
        "Do not pull out more hair to 'test' loss, cover patchy spots with harsh dyes, or ignore sudden bald patches while layering random oils.",
        "Book women's salon hair care for breakage, split ends, and gentle restorative routines; see a dermatologist for sudden heavy shedding, round bald patches, scalp sores, or loss with other health symptoms.",
        hero="A drain clump is a clue — bulb vs snap tells you what to fix first.",
        excerpt="Hairfall after every wash in Kashmir? Check whether strands are shedding or snapping, ease heat and tight styles, and know when to book a salon or a doctor.",
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
    "CRP-D03": (
        "door-not-closing-properly",
        "wardrobe-door-slider-problems",
        "curtain-rod-falling-sagging",
    ),
    "PNT-D03": (
        "painting-damp-walls-kashmir",
        "paint-peeling-kashmir-homes",
        "wall-seepage-plaster-damage-kashmir",
    ),
    "WMN-D06": (
        "hair-damage-after-colour",
        "skin-allergy-after-facial",
        "dandruff-itchy-scalp-men",
    ),
    "WMN-D07": (
        "frizzy-dry-hair-after-wash-kashmir",
        "hair-damage-after-colour",
        "skin-allergy-after-facial",
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
    "kitchen-cabinet-door-sagging-kashmir": "kitchen cabinet door, cup hinge screws, mounting plate and sagging shutter",
    "paint-looking-patchy-streaky-kashmir": "patchy painted wall, roller marks, putty patch primer and even emulsion coat",
    "frizzy-dry-hair-after-wash-kashmir": "frizzy dry hair after wash, soft towel blot, leave-in on damp lengths and low heat",
    "hairfall-after-wash-kashmir": "hairfall in brush after wash, shed bulb vs snapped breakage and gentle detangling",
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
    "kitchen-cabinet-door-sagging-kashmir": {
        "seoTitle": "Cabinet door sagging? Tighten hinge first | Panun Kaergar",
        "seoDescription": (
            "Kitchen cabinet door sagging in Kashmir? Support the door, tighten and adjust the hinges, and know when "
            "to book a carpenter for stripped holes."
        ),
    },
    "paint-looking-patchy-streaky-kashmir": {
        "seoTitle": "Patchy paint? Fix prep before another coat | Panun Kaergar",
        "seoDescription": (
            "Paint looking patchy or streaky in Kashmir? Sand dust, spot-prime putty patches, "
            "roll thin even coats with a wet edge, and know when to book a painter."
        ),
    },
    "frizzy-dry-hair-after-wash-kashmir": {
        "seoTitle": "Frizzy dry hair? Calm cuticle first | Panun Kaergar",
        "seoDescription": (
            "Frizzy dry hair after washing in Kashmir? Rinse well, blot instead of rubbing, seal damp lengths, "
            "lower the heat, and know when to book a salon visit."
        ),
    },
    "hairfall-after-wash-kashmir": {
        "seoTitle": "Hairfall after wash? Check breakage first | Panun Kaergar",
        "seoDescription": (
            "Hairfall after every wash in Kashmir? Check whether strands are shedding or snapping, ease heat "
            "and tight styles, and know when to book a salon or a doctor."
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
    "kitchen-cabinet-door-sagging-kashmir": [
        (
            "Force the door shut every time",
            "Rips the hinge plate",
            "Slamming a sagging door tears screw holes wider and can crack the door edge or carcass.",
            "Hand slamming sagging kitchen cabinet door against frame",
            "Support and adjust instead",
        ),
        (
            "Drive a much larger screw into chipboard",
            "Splits the carcass",
            "Oversized screws often split thin particleboard and leave nothing for a proper repair later.",
            "Large screw forced into crumbling kitchen cabinet chipboard hinge hole",
            "Use a proper plug or carpenter fix",
        ),
        (
            "Remove all hinges at once unsupported",
            "Door drops and chips",
            "Take one hinge at a time with the door supported, or the shutter can fall and damage the worktop.",
            "Kitchen cabinet door falling while all hinges removed at once",
            "Support the door first",
        ),
    ],
    "paint-looking-patchy-streaky-kashmir": [
        (
            "Slap on a thicker coat to hide it",
            "Runs, sags, and longer dry time",
            "Heavy wet coats trap marks and drip; thin even coats over a primed surface hide better.",
            "Paint roller overloaded dripping thick paint down wall",
            "Thin coats over proper prep",
        ),
        (
            "Paint over active damp or peeling film",
            "Fails again within days",
            "Moisture and loose old paint will telegraph through any new colour — fix the base first.",
            "Fresh paint brushed over peeling damp wall patch",
            "Dry and sound before colour",
        ),
        (
            "Skip primer on bare putty patches",
            "Blotches return",
            "Unprimed filler absorbs finish unevenly and leaves permanent light and dark zones.",
            "Bare white putty patches on wall before emulsion without primer",
            "Spot-prime every patch",
        ),
    ],
    "frizzy-dry-hair-after-wash-kashmir": [
        (
            "Blast soaking wet hair on max heat",
            "Burns the cuticle open",
            "High heat on dripping hair locks in frizz and dryness; blot first and use a lower setting with protection.",
            "Hair straightener on hottest setting on soaking wet frizzy hair",
            "Dry partly, then lower heat",
        ),
        (
            "Pile oil on an itchy scalp for dry ends",
            "Grease without softness",
            "Lengths need leave-in moisture; a heavy oiled scalp will not fix dry ends and can worsen itch.",
            "Heavy oil poured onto itchy scalp while hair ends stay dry",
            "Treat lengths, not only the scalp",
        ),
        (
            "Bleach again to 'fix' dryness",
            "More breakage",
            "Chemical lightening on already dry hair increases snap and frizz — pause and restore first.",
            "Bleach brush on already dry frizzy hair lengths",
            "Restore before any chemical",
        ),
    ],
    "hairfall-after-wash-kashmir": [
        (
            "Pull more hair to 'count' the loss",
            "Worsens shedding trauma",
            "Tugging clumps to measure hairfall damages follicles and scares you without diagnosing the cause.",
            "Hand yanking large clump of hair from scalp to test hairfall",
            "Inspect shed strands gently",
        ),
        (
            "Layer random oils on patchy spots",
            "Delays real care",
            "Sudden bald patches need medical review; heavy oils can irritate and hide what a doctor needs to see.",
            "Oil bottle poured onto round bald patch on scalp",
            "Seek medical advice for patches",
        ),
        (
            "Keep tight buns and max heat daily",
            "Breakage looks like hairfall",
            "Constant tension and high heat snap lengths into the brush — ease styling while you recover.",
            "Tight bun and hot straightener used daily on stressed hair",
            "Loosen styles and lower heat",
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
