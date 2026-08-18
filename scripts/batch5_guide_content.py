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
    _compact(
        "CLN-D06",
        "mattress-smell-stains-cleaning-kashmir",
        "Mattress smells or stains? Air it out before you soak the foam",
        "Cleaning",
        "professional-cleaning",
        "On a warm morning the mattress still smells closed after winter bedding, a faint tea ring sits near the edge, and someone is already pouring a bucket of soapy water onto the foam — which often locks moisture and odour deeper inside.",
        "Strip the bedding, vacuum both sides, blot fresh spills without soaking, air the mattress in dry light, and use a light baking-soda refresh only when fully dry. Deep odour, urine, mould spots, or a mattress that stays damp after cleaning needs professional mattress cleaning.",
        "Stale smell, surface stain, or damp feel in the mattress",
        "Trapped moisture, body oils, spill residue, or dust buildup in the cover and foam",
        [
            "Sweat and body oils building up under closed winter bedding with little airing.",
            "Spills rubbed wider or flooded with water so foam stays wet and smells musty.",
            "Dust, dead skin, and allergen buildup on a mattress never vacuumed or rotated.",
        ],
        [
            (
                "Strip and vacuum both sides",
                "any stale or dusty mattress",
                "Remove all covers, vacuum the top, sides, and underside with an upholstery tool, and empty the canister outside so dust does not settle back in the room.",
            ),
            (
                "Blot spills — never flood the foam",
                "a fresh stain",
                "Press a clean cloth from the edge inward; use minimal moisture on a barely damp cloth, then blot dry. Soaking foam can leave a lasting musty core.",
            ),
            (
                "Air in dry light when weather allows",
                "a closed winter smell",
                "Stand the mattress on its side near an open window or sunny dry spot for a few hours — never leave it in damp air or overnight rain risk.",
            ),
            (
                "Refresh with baking soda only when dry",
                "light odour after vacuuming",
                "Dust a thin layer of baking soda on a fully dry surface, leave briefly, then vacuum thoroughly. Skip this on a damp mattress.",
            ),
            (
                "Book mattress cleaning",
                "deep odour, urine, or mould",
                "Pros can extract residue, treat allergens, and dry the core properly — safer than soaking foam at home.",
            ),
        ],
        "Vacuuming both sides and a dry afternoon airing cleared the closed smell; we never needed to soak the mattress.",
        "Mehak",
        "Kashmir winters mean thick bedding, closed rooms, and bukhari heat that dries the air while moisture still sits in foam. A mattress that never gets stripped and aired often smells 'old' long before it needs replacing.",
        "Do not soak the foam with buckets of water, scrub stains into a wider ring, or put a damp mattress back under heavy covers the same night.",
        "Book professional mattress cleaning for urine or mould, odour that returns after airing and vacuuming, deep set stains, allergy flare-ups tied to the bed, or a mattress too heavy to turn and dry safely at home.",
        hero="A closed mattress smell usually needs air and a vacuum — not a bucket of water.",
        excerpt="Mattress smells or stains in Kashmir? Strip, vacuum both sides, blot spills lightly, air it dry, and know when to book mattress cleaning.",
    ),
    _compact(
        "PNT-D04",
        "paint-touch-up-never-matches-kashmir",
        "Touch-up paint never matches? Feather the edge before you repaint the room",
        "Painting",
        "painting",
        "A small putty patch after moving a shelf looks fine until the roller dries — then a bright rectangle sits in the middle of a faded wall, and someone opens a fresh tin hoping one dab will disappear.",
        "Clean and sand the spot, prime bare filler, tint from leftover paint or a fresh match under the same light, then feather thin coats outward instead of painting a hard square. Large faded walls, sheen mismatch, or many scattered patches need a painter for a full blend or recoat.",
        "Touch-up looks lighter, darker, or glossier than the wall",
        "Faded old paint, different batch/sheen, unprimed filler, or a hard-edged patch",
        [
            "Sun and bukhari heat fading the original wall while leftover paint stayed darker in the tin.",
            "Bare putty or plaster absorbing new colour differently than sealed emulsion.",
            "A hard square of fresh paint with a different sheen catching afternoon light.",
        ],
        [
            (
                "Clean, sand, and dust the patch",
                "any small repair",
                "Wipe grease, sand the filler flush, and remove dust so the new film sits level with the old wall.",
            ),
            (
                "Spot-prime bare filler only",
                "fresh putty or scraped plaster",
                "Prime the absorbent patch so colour does not sink into a pale blotch when you apply finish.",
            ),
            (
                "Match paint and sheen in daylight",
                "leftover tin or a shop match",
                "Shake well, check matt vs silk, and test a coin-sized dab beside the repair under the same window light you live with.",
            ),
            (
                "Feather thin coats outward",
                "a visible rectangle after drying",
                "Roll or brush lightly beyond the repair so the edge blends; two thin passes beat one thick square.",
            ),
            (
                "Book a painter for a proper blend",
                "many patches or a whole faded wall",
                "A pro can recoat a full elevation, match sheen, and hide scattered touch-ups that will never disappear alone.",
            ),
        ],
        "Priming the putty and feathering two thin coats hid the shelf marks; we did not need to repaint the whole room.",
        "Owais",
        "Kashmir walls fade unevenly — sunny sides bleach faster, and winter heating dries rooms while leftover tins stay sealed. A perfect tin match still looks wrong if the wall has aged and the patch is painted as a hard square.",
        "Do not paint a thick hard-edged square on faded walls, skip primer on bare putty, or judge colour under a yellow bulb alone.",
        "Book a painter when touch-ups still flash after careful feathering, the whole wall has faded, sheen is wrong across a room, or many repairs make a full recoat cheaper than chasing patches.",
        hero="A bright patch is usually sheen and edges — not a cursed tin.",
        excerpt="Touch-up paint never matches in Kashmir? Sand, spot-prime, feather thin coats, and know when a painter should recoat the wall.",
    ),
    _compact(
        "MSN-D03",
        "floor-tile-hollow-loose-kashmir",
        "Floor tile hollow or loose? Tap-test before you smash the whole floor",
        "Masonry",
        "masonry",
        "Walking past the bathroom door you hear a dull clack underfoot, then a neighbour says rip every tile out — before anyone maps which ones are hollow and which still ring solid.",
        "Tap-test the floor, mark hollow or rocking tiles, check for water entry at grout lines, and lift only failed tiles carefully for rebedding. Widespread hollowness, cracked screed, or tiles lifting after a leak need a mason for proper floor tile repair.",
        "Hollow sound, rocking tile, or cracked floor tile",
        "Failed adhesive bond, water under tiles, or movement in the screed",
        [
            "Adhesive or mortar bed that never bonded fully, or dried out under winter freeze-thaw.",
            "Water seeping through broken grout and lifting tiles from below.",
            "Heavy impact or furniture drag cracking a tile that then loosens its neighbours.",
        ],
        [
            (
                "Tap-test and mark the hollow ones",
                "any suspicious clack underfoot",
                "Tap with a coin or screwdriver handle; hollow tiles sound dull. Mark them with tape so you know the real area before anyone starts breaking.",
            ),
            (
                "Check grout and wet zones",
                "bathrooms and kitchen floors",
                "Look for missing grout, dark damp lines, or soft edges — water under tiles often explains a cluster of hollow spots.",
            ),
            (
                "Protect neighbours before lifting",
                "a single loose tile",
                "Score grout, protect nearby good tiles, and lift the failed piece carefully instead of hammering randomly across the room.",
            ),
            (
                "Clean and rebed a small repair",
                "one or two loose tiles with sound screed",
                "Clear old adhesive, dry the base, and reset with suitable tile adhesive so the tile sits flush and does not rock.",
            ),
            (
                "Book a mason for floor tile repair",
                "many hollow tiles or cracked base",
                "A pro can assess screed damage, replace a run of tiles, and regrout properly without turning a small hollow into a broken floor.",
            ),
        ],
        "Three hollow bathroom tiles were the whole problem; rebedding them stopped the clack without a full floor redo.",
        "Javed",
        "Kashmir bathrooms and kitchens see freeze-thaw, hard water, and long wet winters that punish weak adhesive beds. A dull tap underfoot is often a small bond failure — not a reason to demolish every tile on day one.",
        "Do not smash random tiles without mapping hollow spots, flood the floor hoping it will 'settle', or ignore water under tiles while only regrouting the surface.",
        "Book a mason for widespread hollowness, rocking tiles near a leak, cracked screed, tiles that lift again after a DIY reset, or a bathroom floor that needs systematic repair.",
        hero="A hollow clack usually means a failed bond — map it before you demolish.",
        excerpt="Floor tile hollow or loose in Kashmir? Tap-test, check grout for water entry, rebed small failures, and know when to book a mason.",
    ),
    _compact(
        "MSN-D04",
        "loose-plaster-falling-kashmir",
        "Loose plaster hollow or peeling? Contain it before a chunk drops",
        "Masonry",
        "masonry",
        "A soft drum sound answers when you tap the bedroom wall, then a palm-sized flake of plaster lands behind the wardrobe — and someone wants to skim the whole room before checking how far the hollow runs.",
        "Tap-test the wall, mark hollow or blistered zones, clear loose flakes safely, and keep people clear of the fall path. Fix damp first if the plaster is wet; large hollow areas, ceiling plaster, or plaster near electrical points need a mason for proper plaster repair.",
        "Hollow drum sound, blistered paint, or plaster flakes on the floor",
        "Failed plaster bond, moisture behind the skim, impact, or old weak render",
        [
            "Plaster skim that never keyed to the masonry, or dried too fast and lost bond.",
            "Damp, salts, or seepage softening the layer until it drums hollow and peels.",
            "Impact, vibration, or old lime plaster that has lost strength after many winters.",
        ],
        [
            (
                "Tap-test and map the hollow zone",
                "any soft or drumming patch",
                "Tap lightly with a knuckle or wooden handle; hollow plaster sounds dull. Mark the boundary with tape so you know the real area before scraping.",
            ),
            (
                "Check for damp and salts",
                "blisters near bathrooms or exterior walls",
                "Look for wet patches, white salt bloom, or stains — active moisture must be fixed before any replaster or the hollow will return.",
            ),
            (
                "Contain loose flakes safely",
                "ceiling edges and walkways",
                "Clear the floor under the patch, wear eye protection, and peel only what already lifts; do not hammer a whole wall open on day one.",
            ),
            (
                "Patch a small dry hollow",
                "a hand-sized dry failure with sound edges",
                "Remove failed skim to a firm edge, dampen lightly, and refill with suitable plaster so the repair keys and sits flush before painting.",
            ),
            (
                "Book a mason for plaster repair",
                "wide hollow areas or ceiling plaster",
                "A pro can chase out failed render, treat the base, and replaster evenly — safer than DIY on ceilings, wet walls, or large living-room faces.",
            ),
        ],
        "The hollow was only above the skirting where damp had softened the skim; local plaster repair stopped the flakes without stripping the whole room.",
        "Bilal",
        "Kashmir freeze-thaw, damp ground-floor walls, and old lime plaster make hollow patches common after winter. A drumming sound is a bond failure — not always a reason to demolish every wall in the house.",
        "Do not hammer open a whole elevation without mapping hollow spots, skim over wet or salty plaster, or leave loose ceiling flakes above beds and walkways.",
        "Book a mason for widespread hollowness, falling ceiling plaster, wet or salt-damaged walls, plaster near electrical points, or a patch that fails again after a DIY refill.",
        hero="A hollow drum under paint usually means lost bond — map it before you strip the room.",
        excerpt="Loose plaster hollow or peeling in Kashmir? Tap-test, check for damp, contain flakes safely, and know when to book plaster repair.",
    ),
    _compact(
        "DRY-D03",
        "winter-woollens-dry-clean-kashmir",
        "Winter woollens smell musty? Dry clean before you fold them away",
        "Dry Cleaning",
        "dry-clean-laundry",
        "When the pheran comes off after months of bukhari heat and closed rooms, the wool still smells faintly damp — and someone is already stuffing it into a plastic carry bag for the summer trunk.",
        "Air woollens in dry daylight, brush off surface dust, and dry clean pherans, shawls, and suits before long storage. Store clean, fully dry garments in breathable cotton with cedar or neem — never in sealed plastic while still holding body moisture or food odour.",
        "Musty smell, flat moths, or stiff wool after winter wear",
        "Body oils, damp storage, or food smoke trapped in fibres before folding",
        [
            "Wool worn all winter without cleaning, trapping sweat, smoke, and skin oils that attract moths.",
            "Garments folded while still slightly damp after rain, snow, or a hurried wash.",
            "Plastic bags or airtight trunks sealing in humidity through Kashmir's damp spring weeks.",
        ],
        [
            (
                "Air and inspect every piece",
                "end-of-season woollens",
                "Hang pherans, shawls, and coats in dry daylight for a few hours; check seams, cuffs, and under collars for stains or tiny holes before storage.",
            ),
            (
                "Brush off dust and lint",
                "surface grime before drop-off",
                "Use a soft clothes brush on dry fabric; do not beat wool against a wall — that can weaken fibres and spread hidden dust mites.",
            ),
            (
                "Dry clean before long storage",
                "pherans, suits, and embellished wool",
                "Take clean, identified items to dry cleaning so oils and food smells do not feed moths over summer. Point out any weak seams or loose buttons.",
            ),
            (
                "Store in breathable cotton",
                "months in a trunk or cupboard",
                "Fold loosely into cotton bags or muslin wraps with cedar blocks or neem leaves; keep away from naphthalene touching fabric directly.",
            ),
            (
                "Book pickup or drop-off dry cleaning",
                "many pieces or delicate embroidery",
                "A laundry partner can collect suits, pherans, and shawls, clean them properly, and return them ready for storage — safer than home washing wool.",
            ),
        ],
        "Dry cleaning the pherans before the trunk went in stopped the musty smell and the moth holes we had the year before.",
        "Naseema",
        "Kashmir winters mean months in wool around bukhari heat, wazwan smoke, and damp shoes tracked indoors. Wool that goes straight from daily wear into a plastic bag often smells fine for a week — then comes out musty or chewed by spring.",
        "Do not home-wash dry-clean-only wool in hot water, seal damp garments in plastic, or skip cleaning because a pheran 'looks clean' after heavy winter wear.",
        "Book dry cleaning for pherans, wool suits, embroidered shawls, and any garment with a dry-clean-only label before long storage; use pickup for a full winter wardrobe refresh or moth-damaged pieces that need professional treatment.",
        hero="Musty wool usually means oils and damp — clean before you fold.",
        excerpt="Winter woollens smell musty in Kashmir? Air them dry, dry clean pherans and shawls before storage, and keep them in breathable cotton — not sealed plastic.",
    ),
    _compact(
        "DRY-D04",
        "curtains-dusty-musty-cleaning-kashmir",
        "Curtains dusty or musty? Clean them without shrinking the lining",
        "Dry Cleaning",
        "dry-clean-laundry",
        "Afternoon light catches a grey cloud when the drawing-room curtains move, and the lining smells closed after months of shut winter windows — but the care label is hidden high behind the pleats.",
        "Vacuum curtains in place with low suction, check the care label and lining, spot-test only a hidden edge, and air the room dry. Dry clean lined, velvet, silk, pleated, blackout, or embellished curtains; careless machine washing can shrink the face fabric differently from the lining.",
        "Dust cloud, closed-room smell, tide mark, or stained curtain hem",
        "Trapped dust and smoke, condensation, fabric-sensitive staining, or a damp lining",
        [
            "Road dust, pollen, bukhari smoke, and cooking residue settling into folds over a long closed season.",
            "Window condensation dampening hems or blackout lining where air cannot circulate.",
            "Face fabric and lining made from different fibres that shrink at different rates in a home wash.",
        ],
        [
            (
                "Vacuum from top to hem",
                "ordinary surface dust",
                "Use a clean upholstery attachment on low suction while the curtain hangs; support delicate pleats instead of pulling them into the nozzle.",
            ),
            (
                "Read the label and inspect the lining",
                "before adding any water",
                "Check the face fabric, blackout backing, embroidery, hooks, and lining — the least washable layer decides how the whole curtain should be cleaned.",
            ),
            (
                "Blot a fresh mark carefully",
                "a small recent splash",
                "Lift solids, then blot from the edge inward with a clean white cloth. Test any fabric-safe solution behind the hem and stop if colour transfers.",
            ),
            (
                "Air the window area dry",
                "musty hems or condensation",
                "Open curtains fully, wipe the sill, and improve airflow; do not fold or rehang fabric that still feels cool and damp at the lining.",
            ),
            (
                "Book curtain dry cleaning",
                "lined, velvet, silk, blackout, or large panels",
                "A fabric-care professional can label each panel, remove hooks safely, treat stains, and clean the face and lining without guessing at shrinkage.",
            ),
        ],
        "The cleaner found a water line only in the blackout backing; the velvet face came back fresh without the shortened lining we feared.",
        "Shazia",
        "Kashmir rooms stay closed through cold months, so curtains collect bukhari smoke, kitchen vapour, road dust, and window condensation together. Heavy lined panels may feel dry on the face while the hem or backing still holds moisture.",
        "Do not machine-wash lined curtains without the care label, soak a stained hem while it hangs, or rehang panels before both face and lining are fully dry.",
        "Book dry cleaning for velvet, silk, wool, blackout, lined, pleated, embroidered, or very large curtains; get prompt help for mould spots, colour bleeding, water damage, or a musty smell that returns after airing.",
        hero="The lining decides the wash — check it before the curtain shrinks unevenly.",
        excerpt="Curtains dusty or musty in Kashmir? Vacuum gently, inspect the lining, blot marks safely, and know when curtain dry cleaning prevents shrinkage.",
    ),
    _compact(
        "GRD-D05",
        "balcony-plants-dying-winter-kashmir",
        "Balcony plants dying in winter? Check frost before you water more",
        "Gardening",
        "gardening",
        "After the first hard frost, balcony geraniums and herbs look wilted and black at the edges — and someone is already pouring warm water on every pot, including the ones sitting in frozen saucers.",
        "Tell frost damage from underwatering by checking soil moisture and stem tissue. Move tender pots to a sheltered wall or bright indoor spot, reduce winter watering, and lift pots off frozen saucers. Widespread loss, poor drainage, or a full terrace reset needs a gardener.",
        "Wilted, blackened, or dropping leaves on balcony pots after cold nights",
        "Frost burn, cold root shock, overwatering in cold soil, or drought on sheltered evergreens",
        [
            "Tender plants left on open railings through hard frost nights.",
            "Cold wet soil suffocating roots while drooping leaves look like thirst.",
            "Pots in saucers freezing and thawing, stressing roots at the base.",
        ],
        [
            (
                "Check soil before you pour",
                "any drooping winter pot",
                "Stick a finger into the top few centimetres; frozen or soggy soil needs less water, not a daily warm top-up.",
            ),
            (
                "Move tender pots to shelter",
                "herbs, geraniums, and soft stems",
                "Group pots against a south-facing wall or bring them to a bright room — away from a direct bukhari blast.",
            ),
            (
                "Lift pots off frozen saucers",
                "balcony rails and floor trays",
                "Empty ice water, use pot feet, and let excess drain so roots are not sitting in a frozen bath.",
            ),
            (
                "Wait before hard pruning",
                "blackened leaves after frost",
                "Scrape a stem for green tissue after a week; light cleanup only until you know what survived.",
            ),
            (
                "Book a gardener",
                "a dead terrace or poor drainage",
                "A pro can redesign drainage, repot large planters, plan frost-hard planting, or set up drip for next season.",
            ),
        ],
        "Moving the herbs to the sheltered wall and stopping daily pours saved what we thought was a dead balcony.",
        "Rafiq",
        "Open Kashmir balconies freeze hard while living rooms run bukhari heat. Plants caught between the two often fail from wrong winter watering — not from one cold night alone.",
        "Do not drown drooping pots in cold weather, hard-prune everything the morning after frost, or leave plastic pots on frozen saucers full of ice water.",
        "Book a gardener for a full balcony reset, drainage redesign, frost-hard planting plans, drip irrigation setup, or large dead planters you cannot move safely.",
        hero="Frost-black leaves are not always thirst — check the soil first.",
        excerpt="Balcony plants dying in winter in Kashmir? Tell frost from thirst, shelter tender pots, cut winter watering, and know when to book a gardener.",
    ),
    _compact(
        "GRD-D06",
        "garden-weeds-taking-over-kashmir",
        "Garden weeds taking over? Pull them before they seed",
        "Gardening",
        "gardening",
        "After a wet August week, the vegetable patch is half mint and half mystery green — and someone is already spraying a shed bottle onto the beds next to the coriander.",
        "Identify weeds versus kitchen herbs, pull after rain when the soil is soft so the root comes with you, cut seed heads first if they are already flowering, and mulch or replant empty patches. Deep-rooted clumps, a neglected plot, or monthly upkeep needs a gardener for garden cleanup and weeding.",
        "Fast-spreading green between beds, lawn edges, or under fruit trees",
        "Missed weeding after rain, seed heads left standing, or bare soil inviting new growth",
        [
            "Warm soil and summer rain letting annual weeds germinate in a few days.",
            "Seed heads left on dandelion, amaranth, or grass weeds after a rushed mow.",
            "Bare soil between vegetable rows with no mulch or competing plants.",
        ],
        [
            (
                "Identify before you pull",
                "beds mixed with kitchen herbs",
                "Walk the plot in daylight and mark mint, haakh, and coriander before yanking lookalikes — a weed is only a weed once you know it is not dinner.",
            ),
            (
                "Pull after rain with the root",
                "young weeds in soft soil",
                "Wet soil lets taproots slide out whole; a dry tug snaps the crown and the same plant returns in a week.",
            ),
            (
                "Cut seed heads first",
                "weeds already flowering or seeding",
                "Bag the heads before you disturb the plant so wind and the next mow do not sow a second crop across the lawn.",
            ),
            (
                "Mulch and fill the gaps",
                "bare patches after weeding",
                "Cover open soil with compost, leaf mulch, or a wanted plant so the next rain does not refill the same holes.",
            ),
            (
                "Book garden cleanup and weeding",
                "a neglected plot or deep-rooted clumps",
                "A gardener can clear large beds, edges, and fruit-tree understories, then set a monthly weeding rhythm before seeds set again.",
            ),
        ],
        "The gardener pulled taproots after rain and mulched the vegetable rows; the same patch did not bounce back in a week.",
        "Nayeem",
        "August rain after a warm spell fills Kashmir kitchen gardens, apple-tree understories, and neglected lawn edges almost overnight. Beds beside mint, haakh, and coriander mix with lookalikes if nobody walks the plot after a wet week.",
        "Do not spray random herbicide near food plants, mow weeds and leave seed heads on the lawn, or dump pulled weeds in a damp pile where they can re-root.",
        "Book a gardener for a whole neglected plot, deep-rooted clumps around fruit trees, steep or large lawn edges, or a monthly garden maintenance plan that includes weeding.",
        hero="Weeds spread from seed heads and bare soil — pull the root, then cover the gap.",
        excerpt="Garden weeds taking over in Kashmir? Identify them, pull with the root after rain, mulch the gaps, and know when to book garden cleanup.",
    ),
    _compact(
        "PET-D07",
        "dog-nails-clicking-too-long-kashmir",
        "Dog nails clicking or too long? Trim without cutting the quick",
        "Pet Care",
        "dog-grooming",
        "Every step on the wooden floor clicks, the dew claw is starting to curve, and someone has already lined up kitchen scissors — before anyone has found the pink quick inside the nail.",
        "Check whether nails click on hard floors or sit past the pad, find the quick in good light, and trim only a sliver at a time with pet nail clippers. File sharp edges and stop if the dog pulls away. Dark nails, wriggly pets, curled dew claws, or a past quick-cut need a groomer for dog nail clipping.",
        "Clicking on tiles or wood, nails past the pad, or a curling dew claw",
        "Nails grown past the wear line, missed dew claws, or a delayed trim",
        [
            "Indoor floors and short winter walks that do not wear nails down.",
            "Dew claws that never touch the ground and curl toward the pad.",
            "A long gap between grooms after rain, mud, or a nervous last trim.",
        ],
        [
            (
                "Listen and look at the pad",
                "clicking on hard floors",
                "Nails that click on wood or tiles, or sit past the pad when the dog stands, are ready for a small trim — not a one-cut shortening.",
            ),
            (
                "Find the quick before you clip",
                "any nail you plan to cut",
                "Hold the paw in daylight. On light nails the quick is the pink core; on dark nails trim millimetres and watch the cut face for a grey-pink centre.",
            ),
            (
                "Trim a sliver, then wait",
                "calm dogs and visible quicks",
                "Use pet clippers, take a thin slice, and stop well short of the quick. Do one nail, praise, then the next — never a deep cut to 'finish faster'.",
            ),
            (
                "File sharp edges and check dew claws",
                "after a careful trim",
                "A pet file smooths snags that catch on carpets. Dew claws hide in fur and curve inward if skipped.",
            ),
            (
                "Book dog nail clipping",
                "dark nails, wriggles, or a past bleed",
                "A groomer can restrain safely, trim dark nails in stages, and handle curled dew claws without guessing at the quick.",
            ),
        ],
        "The groomer took tiny slices on the dark nails and filed the dew claws; the clicking stopped without a single bleed.",
        "Farhana",
        "Kashmir flats make nail click obvious on wood and tiles. Short winter walks, salty ice, and rocky lakeside paths wear nails unevenly, while dew claws keep growing unseen through the cold months.",
        "Do not take a big chunk to shorten nails in one go, use kitchen scissors or human clippers, or ignore a limp or split nail after a walk.",
        "Book pet grooming for dark nails, a wriggly or fearful dog, curled dew claws, a previous quick-cut, or nails so long they change the dog's walk. See a veterinarian for bleeding that will not stop, swelling, or a torn nail.",
        hero="Clicking on the floor means the nail is past the pad — trim a sliver, not a chunk.",
        excerpt="Dog nails clicking or too long in Kashmir? Find the quick, trim a sliver at a time, file edges, and know when to book nail clipping.",
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
    "CLN-D06": (
        "sofa-smells-stains-cleaning",
        "bathroom-mould-hard-water-stains",
        "kitchen-grease-cleaning-kashmir",
    ),
    "PNT-D04": (
        "paint-looking-patchy-streaky-kashmir",
        "painting-damp-walls-kashmir",
        "paint-peeling-kashmir-homes",
    ),
    "MSN-D03": (
        "wall-cracks-cosmetic-structural",
        "wall-seepage-plaster-damage-kashmir",
        "false-ceiling-water-stain",
    ),
    "MSN-D04": (
        "wall-cracks-cosmetic-structural",
        "wall-seepage-plaster-damage-kashmir",
        "floor-tile-hollow-loose-kashmir",
    ),
    "DRY-D03": (
        "fabric-stains-dry-clean",
        "sofa-dry-cleaning-vs-home-clean",
    ),
    "DRY-D04": (
        "fabric-stains-dry-clean",
        "sofa-dry-cleaning-vs-home-clean",
        "winter-woollens-dry-clean-kashmir",
    ),
    "GRD-D05": (
        "lawn-looking-dead-kashmir",
        "overwatering-garden-plants-kashmir",
    ),
    "GRD-D06": (
        "lawn-looking-dead-kashmir",
        "overwatering-garden-plants-kashmir",
        "balcony-plants-dying-winter-kashmir",
    ),
    "PET-D07": (
        "dog-itching-scratching",
        "matted-fur-dog-cat",
        "dog-smelly-bath-home-kashmir",
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
    "mattress-smell-stains-cleaning-kashmir": "mattress with stale smell, vacuum both sides, blot stain and dry airing",
    "paint-touch-up-never-matches-kashmir": "wall touch-up patch lighter than faded paint, feathered roller edge and primer on putty",
    "floor-tile-hollow-loose-kashmir": "hollow floor tile tap test, loose bathroom tile and rebedding adhesive",
    "loose-plaster-falling-kashmir": "hollow plaster wall tap test, peeling skim flakes and plaster repair patch",
    "winter-woollens-dry-clean-kashmir": "wool pheran and shawl aired in daylight, soft brush, dry-clean bag and breathable cotton storage trunk",
    "curtains-dusty-musty-cleaning-kashmir": "lined drawing-room curtains with dust in pleats, damp blackout hem, care label and upholstery vacuum",
    "balcony-plants-dying-winter-kashmir": "balcony potted plants frost damage, sheltered wall grouping and winter soil moisture check",
    "garden-weeds-taking-over-kashmir": "overgrown kitchen garden weeds, taproot pull after rain, seed heads bagged and mulched vegetable rows",
    "dog-nails-clicking-too-long-kashmir": "dog paw on wooden floor, long clicking nails, pink quick inside nail and pet clippers taking a thin slice",
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
    "mattress-smell-stains-cleaning-kashmir": {
        "seoTitle": "Mattress smells or stains? Air it out first | Panun Kaergar",
        "seoDescription": (
            "Mattress smells or stains in Kashmir? Strip bedding, vacuum both sides, blot spills lightly, "
            "air it dry, and know when to book mattress cleaning."
        ),
    },
    "paint-touch-up-never-matches-kashmir": {
        "seoTitle": "Touch-up paint never matches? Feather first | Panun Kaergar",
        "seoDescription": (
            "Touch-up paint never matches in Kashmir? Sand, spot-prime putty, feather thin coats outward, "
            "and know when a painter should recoat the wall."
        ),
    },
    "floor-tile-hollow-loose-kashmir": {
        "seoTitle": "Hollow floor tile? Tap-test first | Panun Kaergar",
        "seoDescription": (
            "Floor tile hollow or loose in Kashmir? Tap-test, check grout for water entry, rebed small "
            "failures carefully, and know when to book a mason."
        ),
    },
    "loose-plaster-falling-kashmir": {
        "seoTitle": "Loose plaster hollow or peeling? | Panun Kaergar",
        "seoDescription": (
            "Loose plaster hollow or peeling in Kashmir? Tap-test, check for damp, contain flakes safely, "
            "and know when to book a mason for plaster repair."
        ),
    },
    "winter-woollens-dry-clean-kashmir": {
        "seoTitle": "Musty woollens? Dry clean before storage | Panun Kaergar",
        "seoDescription": (
            "Winter woollens smell musty in Kashmir? Air them dry, dry clean pherans and shawls before storage, "
            "and keep them in breathable cotton — not sealed plastic."
        ),
    },
    "curtains-dusty-musty-cleaning-kashmir": {
        "seoTitle": "Curtains dusty or musty? Check lining first",
        "seoDescription": (
            "Curtains dusty or musty in Kashmir? Vacuum gently, inspect the lining, blot marks safely, "
            "and know when curtain dry cleaning prevents shrinkage."
        ),
    },
    "balcony-plants-dying-winter-kashmir": {
        "seoTitle": "Balcony plants dying? Check frost first | Panun Kaergar",
        "seoDescription": (
            "Balcony plants dying in winter in Kashmir? Tell frost from thirst, shelter tender pots, "
            "cut winter watering, and know when to book a gardener."
        ),
    },
    "garden-weeds-taking-over-kashmir": {
        "seoTitle": "Weeds taking over? Pull before they seed | Panun Kaergar",
        "seoDescription": (
            "Garden weeds taking over in Kashmir? Identify them, pull with the root after rain, "
            "mulch the gaps, and know when to book garden cleanup."
        ),
    },
    "dog-nails-clicking-too-long-kashmir": {
        "seoTitle": "Dog nails too long? Trim without the quick | Panun Kaergar",
        "seoDescription": (
            "Dog nails clicking or too long in Kashmir? Find the quick, trim a sliver at a time, "
            "file edges, and know when to book nail clipping."
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
    "mattress-smell-stains-cleaning-kashmir": [
        (
            "Soak the foam with a bucket of water",
            "Locks in musty smell",
            "Flooding a mattress drives moisture into the core where it cannot dry — odour often gets worse, not better.",
            "Bucket of soapy water poured onto mattress foam creating wet patch",
            "Blot lightly, never flood",
        ),
        (
            "Scrub a stain in circles hard",
            "Spreads a wider ring",
            "Aggressive scrubbing pushes pigment outward and can damage the cover weave.",
            "Hand scrubbing mattress stain in hard circles spreading the mark",
            "Blot from the edge inward",
        ),
        (
            "Cover a damp mattress the same night",
            "Traps moisture under sheets",
            "Heavy bedding on a still-damp mattress seals in humidity and recreates the closed smell by morning.",
            "Heavy winter quilt put back on damp mattress same evening",
            "Air until fully dry first",
        ),
    ],
    "paint-touch-up-never-matches-kashmir": [
        (
            "Paint a thick hard-edged square",
            "Flashes under daylight",
            "A sharp rectangle of fresh paint sits proud of faded wall colour and shows from across the room.",
            "Hard square of fresh paint on faded wall looking like a bright patch",
            "Feather the edge outward",
        ),
        (
            "Skip primer on bare putty",
            "Colour sinks unevenly",
            "Unprimed filler drinks finish and leaves a permanent light blotch even with the same tin.",
            "Bare white putty patch on wall painted without primer",
            "Spot-prime filler first",
        ),
        (
            "Judge colour only under a yellow bulb",
            "Wrong match by morning",
            "Warm bulbs hide sheen and hue differences that appear harsh in daylight — always check by a window.",
            "Person checking wall paint colour only under yellow room bulb at night",
            "Test in daylight too",
        ),
    ],
    "floor-tile-hollow-loose-kashmir": [
        (
            "Smash tiles without mapping hollow spots",
            "Breaks good floor needlessly",
            "Blind demolition destroys solid tiles and raises dust before you know how small the failed area is.",
            "Hammer smashing random floor tiles without tap-test marks",
            "Tap-test and mark first",
        ),
        (
            "Flood the floor hoping it will settle",
            "Worsens under-tile water",
            "Extra water under hollow tiles softens the bed further and can stain neighbouring rooms.",
            "Bucket of water poured onto hollow bathroom floor tiles",
            "Find water entry, do not flood",
        ),
        (
            "Only regrout and ignore rocking tiles",
            "Hollowness returns quickly",
            "Fresh grout on a floating tile hides the clack briefly but does not restore the bond underneath.",
            "Person regrouting around a visibly rocking floor tile",
            "Rebed or book repair",
        ),
    ],
    "loose-plaster-falling-kashmir": [
        (
            "Hammer open a whole wall without mapping",
            "Destroys sound plaster needlessly",
            "Blind chiselling raises dust and wrecks firm areas before you know how small the hollow zone is.",
            "Hammer chiselling random plaster wall without tape marks on hollow spots",
            "Tap-test and mark first",
        ),
        (
            "Skim over wet or salty plaster",
            "Hollow returns under paint",
            "Fresh putty on active damp or salt bloom looks fine for a week, then blisters and drums hollow again.",
            "Person skimming wet blistered plaster with fresh putty over damp wall",
            "Dry and fix moisture first",
        ),
        (
            "Ignore loose ceiling flakes above beds",
            "Fall hazard overnight",
            "Ceiling plaster that already peels can drop without warning onto beds, cradles, and walkways.",
            "Loose ceiling plaster flakes above bed with no containment below",
            "Contain and book repair",
        ),
    ],
    "winter-woollens-dry-clean-kashmir": [
        (
            "Home-wash a dry-clean-only pheran",
            "Shrinks and felts the wool",
            "Hot water and scrubbing can turn a loose pheran into a stiff, smaller garment with ruined embroidery.",
            "Wool pheran being hand-washed in hot soapy bucket at home",
            "Dry clean labelled wool",
        ),
        (
            "Seal damp wool in plastic",
            "Musty smell and moth risk",
            "Trapped moisture in a carry bag creates the exact damp pocket moths and mildew love over summer.",
            "Slightly damp wool pheran folded into sealed plastic carry bag",
            "Air fully dry first",
        ),
        (
            "Skip cleaning because it looks fine",
            "Oils feed moths all summer",
            "Invisible skin oils and wazwan smoke on 'clean-looking' wool are what draw moths to cuffs and collars.",
            "Unwashed wool pheran folded straight into storage trunk after winter",
            "Dry clean before storage",
        ),
    ],
    "curtains-dusty-musty-cleaning-kashmir": [
        (
            "Machine-wash lined curtains blindly",
            "Face and lining shrink differently",
            "Mixed fibres can pull against each other, leaving a shortened lining, puckered seams, or panels that no longer meet the floor.",
            "Lined curtains emerging uneven and puckered from home washing machine",
            "Check every layer first",
        ),
        (
            "Soak a stained hem while it hangs",
            "Leaves a tide mark and wet wall",
            "Water climbs through the fabric, spreads the stain, and can dampen the sill, wall, and lining behind it.",
            "Bucket soaking bottom hem of hanging curtain beside damp window wall",
            "Remove and treat correctly",
        ),
        (
            "Rehang before the lining is dry",
            "Musty smell returns quickly",
            "A dry-feeling face can hide moisture in blackout backing or stitched hems, sealing the same stale smell against the window.",
            "Heavy curtain rehung with visibly damp blackout lining at window",
            "Dry face and lining fully",
        ),
    ],
    "balcony-plants-dying-winter-kashmir": [
        (
            "Drown drooping pots in cold weather",
            "Roots rot in cold wet soil",
            "Warm daily pours on frozen or soggy soil suffocate roots when plants are already in shock.",
            "Watering can pouring onto frost-damaged balcony plant with soggy cold soil",
            "Check soil first",
        ),
        (
            "Hard-prune everything after one frost",
            "May remove live tissue",
            "Cutting all stems to the ground before you scrape for green can kill plants that would have recovered.",
            "Hand cutting balcony herb pots down to soil level morning after frost",
            "Wait and scrape stems first",
        ),
        (
            "Move pots beside bukhari without light",
            "Leaves scorch; stems weaken",
            "Dry heat without bright window light cooks foliage and leaves recovery weaker than frost alone.",
            "Balcony plant pot placed directly beside bukhari heater in dark corner",
            "Bright sheltered spot instead",
        ),
    ],
    "garden-weeds-taking-over-kashmir": [
        (
            "Spray mystery herbicide on kitchen beds",
            "Poisons food plants and soil",
            "A random shed bottle near coriander, mint, or haakh can kill the crop and leave residue in the soil you eat from.",
            "Person spraying unmarked herbicide bottle onto vegetable bed beside coriander",
            "Pull and mulch instead",
        ),
        (
            "Mow weeds and leave the seed heads",
            "Spreads a second crop",
            "A quick mow scatters ripe seeds across the lawn and into vegetable rows instead of removing them.",
            "Lawn mower cutting flowering weeds and scattering seed heads across grass",
            "Bag seed heads first",
        ),
        (
            "Dump pulled weeds in a damp pile",
            "They re-root on the soil",
            "Moist stems and taproots left on the bed can take again after the next rain, undoing the afternoon's work.",
            "Pile of freshly pulled weeds left on damp garden soil after rain",
            "Bag and remove them",
        ),
    ],
    "dog-nails-clicking-too-long-kashmir": [
        (
            "Take a big chunk to shorten nails fast",
            "Cuts the quick and bleeds",
            "One deep cut hits the pink core, hurts the dog, and makes the next trim a fight.",
            "Large nail clipper taking a deep cut close to the pink quick in a dog nail",
            "Trim a sliver only",
        ),
        (
            "Use kitchen scissors or human clippers",
            "Crushes the nail and slips",
            "Household tools crush instead of slicing, slip toward the pad, and can split the nail.",
            "Kitchen scissors and human nail clippers held toward a dog paw",
            "Use pet nail clippers",
        ),
        (
            "Ignore a limp or split nail after a walk",
            "Pain and infection risk",
            "A snagged or split nail can catch on carpets and ice; delayed care lets it tear further.",
            "Dog lifting a paw with a split long nail after a walk",
            "Stop walks and book help",
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
