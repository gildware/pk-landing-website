"""Batch 2 practical guides — second high-intent problem post per category."""

from batch1_guide_content import _article, _compact

_SPECS = [
    _compact(
        "ALU-D02", "aluminium-door-not-sliding-smoothly", "Aluminium door not sliding smoothly? Clean the track before you force it",
        "Aluminium & Glass", "aluminium-steel-works",
        "The balcony door in a flat needs a hip-check every evening. The glass is fine; the bottom track has collected a season of grit.",
        "Vacuum and wipe the track, clear weep holes, check rollers and alignment, then use a dry silicone lubricant sparingly. Do not force a jammed panel or use thick grease.",
        "Door drags, jumps, or sticks halfway", "Grit in the track, worn rollers, or a misaligned frame",
        ["Dust and grit packed into the bottom channel.", "Blocked drainage holes holding water and swelling debris.", "Worn or seized rollers after years of use."],
        [("Vacuum the track", "a dragging panel", "Remove loose grit with a vacuum nozzle, then wipe with a soft brush and dry cloth."), ("Clear weep holes", "water in the frame", "Find small drainage openings and clear them gently without enlarging."), ("Check rollers and alignment", "persistent scraping", "Look for a panel sitting low on one side or a roller that no longer spins."), ("Use dry silicone only", "a clean but sticky track", "Apply a window-safe dry lubricant; avoid oil that catches more dust."), ("Book adjustment", "glass stress or lock failure", "A pro can realign rollers without stressing the glass or frame.")],
        "The track looked clean on top; the grit was packed under the roller.", "Imran",
        "Wind-blown dust and winter grit are hard on sliding doors. A five-minute track clean before the wet season prevents many stuck panels.",
        "Do not force a jammed panel, use heavy grease, or drill new holes in the frame.", "Book a window professional for cracked glass, a loose frame, a door that will not lock, or persistent leakage after cleaning."),
    _compact(
        "CRP-D02", "wardrobe-door-slider-problems", "Wardrobe door or slider stuck? Find the rub before you yank",
        "Carpentry", "carpentry",
        "A mirrored wardrobe in a bedroom refuses to close on a humid morning. The mirror is innocent; the top runner is carrying the whole argument.",
        "Locate where the door catches, clean the track, tighten loose fixings, and check whether the runner is bent or the door has sagged. Do not force a heavy mirrored door.",
        "Sliding wardrobe door jumps, drags, or falls off track", "Dirty track, loose brackets, bent runner, or swollen board",
        ["Dust and clothing fibres packed in the top or bottom track.", "Loose screws letting the door hang at an angle.", "A bent aluminium runner or swollen particleboard edge."],
        [("Stop forcing it", "any stuck slider", "Open slowly and note exactly where it catches or lifts."), ("Clean the track", "grit and lint", "Vacuum the channel and wipe with a dry cloth; do not flood it with oil."), ("Tighten visible brackets", "a sagging door", "Check top guide screws and side fixings with the correct screwdriver."), ("Check the runner", "repeated derailment", "Look for bends, missing wheels, or a door sitting lower on one side."), ("Call a carpenter", "mirrored or heavy doors", "Large doors need proper alignment; a small shave or runner swap beats a broken mirror.")],
        "One loose top bracket was making the whole door ride up.", "Nida",
        "Modular wardrobes in heated winter rooms can dry and shift slightly; damp spells can swell edges. Both feel like a broken slider until you look closely.",
        "Do not yank a mirrored door, spray oil into a full track, or plane wood while the door is hanging crooked.", "Book a carpenter for a derailed heavy door, cracked mirror, broken runner, or a door that will not stay closed."),
    _compact(
        "DRY-D01", "sofa-dry-cleaning-vs-home-clean", "Does your sofa need dry cleaning or a home clean?",
        "Dry Cleaning", "dry-clean-laundry",
        "After a winter of closed windows, the living-room sofa smells faintly stale. Someone suggests vinegar; someone else says dry clean everything.",
        "Read the fabric tag, test in a hidden seam, and choose home spot-clean only for washable, water-safe upholstery. Odour, oil, delicate fabric, or old stains usually need professional extraction or dry cleaning.",
        "Stale smell, visible stain, or unclear fabric care", "Trapped moisture, residue, or a stain type the fabric cannot take wet",
        ["Food, tea, or body oil pushed deeper by rubbing.", "Too much home shampoo left in the foam.", "Silk, wool, velvet, or dry-clean-only blends."],
        [("Find the care tag", "every sofa", "Check whether the cover is removable and whether water is allowed."), ("Test a hidden patch", "unknown fabric", "Dab a tiny amount of your cleaner and let it dry before treating the mark."), ("Blot fresh spills only", "a new stain", "Press from the edge inward with a white cloth; do not scrub."), ("Air and vacuum", "light odour", "Vacuum crevices and give cushions airflow before assuming chemical cleaning."), ("Book extraction or dry clean", "old odour or delicate fabric", "Pros can rinse residue and dry the filling without flooding it.")],
        "The tag said dry clean only; the home remedy would have left a pale ring.", "Saima",
        "Closed Kashmir winters keep sofas damp longer than they feel on top. A heater aimed at wet fabric can bake in a smell; airflow and the right method matter more.",
        "Do not saturate foam, mix cleaners, or iron a stain.", "Book dry cleaning or upholstery extraction for silk, wool, velvet, pet accidents, mould spots, old odour, or a dry-clean-only label."),
    _compact(
        "ELC-D02", "flickering-lights-causes-kashmir", "Lights flickering? Check the bulb before blaming the wiring",
        "Electrical", "electrician",
        "In an older flat, the kitchen tube flickers whenever the geyser clicks on. The family swaps bulbs twice before anyone asks whether the fitting or circuit is talking.",
        "Tighten or replace the bulb or tube, try another lamp on the same point, and note whether flicker matches appliance use. Persistent flicker, buzzing, heat, or one-room-only issues need an electrician.",
        "Light flickers, dims, or pulses", "Loose bulb, failing driver, loose contact, or circuit load",
        ["Loose or incompatible bulb or LED driver.", "Loose holder contact or old starter gear.", "Heavy appliance starting on the same circuit."],
        [("Reseat or replace the bulb", "one flickering point", "Switch off, tighten the bulb, or swap in a known-good lamp."), ("Try another fitting", "isolating bulb vs point", "Move the bulb to a different holder to see whether the flicker travels."), ("Listen and feel", "buzzing or heat", "Warm switches, buzzing holders, or scorch marks are not bulb problems."), ("Note the pattern", "load-related flicker", "Write down whether it happens when the geyser, heater, or motor starts."), ("Book an electrician", "persistent or spreading flicker", "Loose neutrals, damaged wiring, and bad holders need proper testing.")],
        "It was a loose contact in the holder, not the whole flat's wiring.", "Bilal",
        "Winter load from heaters and geysers can make marginal circuits show symptoms that look like a bad bulb. Check the simple things first, but do not ignore heat or smell.",
        "Do not wiggle live fittings, bypass a holder, or ignore flicker that comes with a burning smell.", "Book an electrician for heat, buzzing, scorch marks, whole-room flicker, or flicker that continues with a new bulb."),
    _compact(
        "GRD-D04", "overwatering-garden-plants-kashmir", "Plants looking sad? Overwatering is often the culprit",
        "Gardening", "gardening",
        "A proud balcony garden gets watered twice daily through a hot week indoors. By Friday the leaves look yellow and limp, which feels cruelly like thirst.",
        "Check soil moisture before watering, improve drainage, and look for yellowing lower leaves, soggy soil, and fungus gnats. Wilt from overwatering needs less water, not more.",
        "Yellow leaves, limp stems, or mouldy soil surface", "Roots sitting in wet soil with poor drainage",
        ["Watering on a schedule instead of by soil feel.", "Pots without drainage holes or saucers holding water.", "Heavy soil that stays wet through cool nights."],
        [("Test the soil", "before every pour", "Stick a finger or skewer in; water only if the top few centimetres are dry."), ("Empty saucers", "potted plants", "Drain standing water after watering so roots are not bathing."), ("Check drainage holes", "soggy pots", "Make sure holes are open and not blocked by roots or stones."), ("Improve airflow", "indoor plants", "Space pots and wipe condensation from cold window sills."), ("Repot or refresh soil", "chronic sogginess", "A gardener can add grit, perlite, or move plants to better containers.")],
        "We were drowning them with kindness; less water fixed the yellow leaves.", "Hina",
        "Indoor heat and cold window sills create uneven drying in Kashmir homes. A plant by the glass may stay wet at the roots while the top looks dry.",
        "Do not water because the leaves droop without checking soil, leave pots in full saucers, or repot into dense garden soil alone.", "Book a gardener for repeated plant loss, drainage redesign, balcony beds that never dry, or pest/fungal issues after soggy soil."),
    _compact(
        "APP-AC-D02", "ac-leaking-water-kashmir", "AC leaking water indoors? Check the drain before panicking",
        "Home Appliances", "home-appliances",
        "On a humid July afternoon, a split AC starts dripping from the indoor unit onto the floor. Everyone assumes the refrigerant is escaping; often it is just blocked condensate.",
        "Switch off, check whether water is condensate or oily refrigerant, inspect the drain pipe and filter, and clear blockages gently. Oily marks, no cooling, or electrical smell need appliance service.",
        "Water dripping from indoor unit or wall stain below", "Blocked drain, tilt issue, dirty filter, or frozen coil melting",
        ["Clogged drain hose or full drain tray.", "Dirty filters causing ice that later melts.", "Improper slope letting water pool inside the unit."],
        [("Switch off and observe", "active drip", "Note whether water is clear condensate or oily, and whether cooling has stopped."), ("Check the drain pipe", "blocked condensate", "Look for kinks, clogs, or a disconnected outlet; clear gently."), ("Clean filters", "ice then melt", "Wash and fully dry filters before restarting."), ("Check installation tilt", "pooling water", "The indoor unit should slope slightly toward the drain side."), ("Book service", "repeat leak or oily residue", "A technician can vacuum the drain, test refrigerant, and fix installation.")],
        "The drain pipe was kinked behind the cabinet, not a major gas leak.", "Adnan",
        "Humid summers and dusty filters combine to clog AC drains quickly in Kashmir. A pre-season filter wash and drain check prevents many indoor puddles.",
        "Do not poke the coil with wire, ignore oily stains, or run a leaking unit near electrical points.", "Book appliance repair for oily residue, poor cooling with leak, repeated overflow, electrical tripping, or a ceiling stain spreading below the unit."),
    _compact(
        "INT-D05", "curtain-rod-falling-sagging", "Curtain rod falling or sagging? Fix the anchor, not just the fabric",
        "Interior Repair", "interior-decor",
        "A heavy blackout curtain in a Sopore bedroom pulls the rod down with a soft crack on a windy night. The curtain is not too dramatic; the wall anchor is.",
        "Remove load, inspect brackets and fixings, move anchors to solid material if needed, and distribute weight across enough support points. Do not keep drilling into crumbling plaster.",
        "Rod sags, bracket pulls away, or finial drops", "Weak anchors, too few brackets, or heavy fabric on hollow wall",
        ["Plastic plugs in soft or crumbling plaster.", "Too few brackets for long or heavy curtains.", "Repeated pulling on one end when opening."],
        [("Take the weight off", "a failing bracket", "Remove curtains and check whether brackets are bent or screws are loose."), ("Inspect the wall", "pull-out holes", "Look for crumbling plaster, hollow sound, or previous patch failures."), ("Use proper anchors", "weak original fixings", "Match fixings to wall type; heavy curtains need solid anchors and enough points."), ("Add a centre support", "long spans", "A middle bracket stops sag on wide windows."), ("Rehang evenly", "repeat failure", "Open and close from the middle where possible to reduce side strain.")],
        "They added one centre bracket and proper anchors; the rod stopped creeping down.", "Rubeena",
        "Heavy winter curtains and long damp spells can test old plaster harder than lightweight sheers. Anchor choice matters as much as rod quality.",
        "Do not screw back into the same crumbled hole, use mismatched rawlplugs, or ignore a rod near a sleeping area that keeps falling.", "Book interior repair for repeated pull-out, large heavy drapes, ceiling-mounted tracks, or damage to the window reveal."),
    _compact(
        "MSN-D02", "wall-seepage-plaster-damage-kashmir", "Wall seepage and plaster damage? Find the water path first",
        "Masonry", "masonry",
        "A patch of plaster bubbles in a ground-floor room every spring. Fresh putty lasts one season because the wall is still drinking from somewhere.",
        "Trace whether moisture is rising, leaking from above, or entering from outside. Dry the wall, fix the source, then repair plaster. Painting or skimming over active seepage fails quickly.",
        "Damp patch, flaking plaster, or salty white bloom", "Hidden leak, rain entry, rising damp, or cold-wall condensation",
        ["Bathroom or pipe leak on the other side.", "Cracks or failed pointing on an exterior wall.", "Ground moisture or poor external drainage."],
        [("Map the patch", "any damp zone", "Note height, seasonality, and whether it grows after rain or use upstairs."), ("Check upstairs and outside", "hidden source", "Inspect bathrooms, windows, roof edges, and exterior cracks."), ("Test for active moisture", "before repair", "A foil tape test or moisture meter helps confirm whether the wall is still wet."), ("Fix the source and dry", "confirmed leak", "Repair plumbing or exterior entry and allow real drying time."), ("Repair plaster properly", "a dry wall", "Remove failed material, treat salts if needed, then replaster and paint.")],
        "The bathroom grout line upstairs was the leak; the bedroom wall was innocent.", "Tanveer",
        "Snowmelt, driving rain, and old stone walls make seepage seasonal in Kashmir. The stain location is a clue, not always the leak itself.",
        "Do not skim over active damp, use ordinary paint as a barrier, or hack plaster open near live wires.", "Book a mason urgently for a bulging wall, spreading mould, salt-heavy bloom after repeated repair, or damp near electrics."),
    _compact(
        "MEN-D05", "uneven-beard-growth-shape", "Uneven beard growth? Work with your pattern, not against it",
        "Men's Grooming", "mens-salon",
        "A young man in Anantnag stares at one cheek in the mirror every morning. One side fills in faster; the neckline creeps up unevenly after a rushed trim.",
        "Give growth time, map your natural line, trim gradually with good light, and use a barber for shape rather than chasing perfect symmetry daily. Patchy loss, bald spots, or sudden change needs medical advice.",
        "Patchy density, uneven line, or lopsided shape", "Natural growth pattern, scarring, hormonal change, or a rushed home trim",
        ["Genetic pattern with slower areas on cheeks or neck.", "Over-trimming trying to force symmetry.", "Skin irritation or hair loss from pulling or infection."],
        [("Let it grow a few weeks", "early patchiness", "Many uneven patterns look different after fuller growth."), ("Map in good light", "line problems", "Use a mirror and natural light; mark neckline with a comb before trimming."), ("Trim small amounts", "shape maintenance", "Take less off than you think; you can always remove more."), ("Visit a barber for shape", "special occasions", "A professional line and fade can make uneven growth look intentional."), ("See a doctor if sudden", "new bald patches", "Round patches, pain, or rapid loss are not styling issues.")],
        "He stopped chasing identical cheeks and let a barber set the line once.", "Owais",
        "Dry indoor heat and cap friction can irritate the neck line in winter. Gentle washing and a defined professional shape often beat daily aggressive edging.",
        "Do not shave against irritated skin daily, use random kitchen scissors, or compare your pattern to filtered photos.", "Book men's grooming for shape-ups, special events, or learning a maintainable line; see a doctor for sudden patch loss or painful skin."),
    _compact(
        "PNT-D02", "paint-peeling-kashmir-homes", "Why paint peels in Kashmir homes — and what to do next",
        "Painting", "painting",
        "Fresh emulsion in a Hazratbal bedroom lifts in curls by winter. The colour looked fine in October; the wall underneath had other plans.",
        "Peeling usually means poor adhesion, moisture, or surface prep failure. Scrape loose paint, fix damp, prime correctly, and repaint. Do not roll new colour over lifting flakes.",
        "Paint flakes, blisters, or lifts in sheets", "Moisture, chalky surface, wrong primer, or paint on glossy old coat",
        ["Painting over damp or salty walls.", "Skipping primer on new plaster or glossy old paint.", "Cheap paint on a wet or very cold wall."],
        [("Scrape what lifts easily", "active peeling", "Remove loose flakes back to a firm edge; do not rip good paint."), ("Find moisture or chalk", "repeat peeling", "Check for damp, efflorescence, or powdery plaster."), ("Prepare the surface", "before repaint", "Clean, dry, and use the correct primer for that wall."), ("Repaint in suitable conditions", "finish work", "Avoid very cold, humid, or dusty application days."), ("Use compatible systems", "exterior or wet areas", "Match undercoat and topcoat to the location.")],
        "They primed after fixing a bathroom leak; the peel did not return next winter.", "Manzoor",
        "Freeze-thaw, interior heat, and exterior damp make paint adhesion a seasonal test in Kashmir. Peeling is usually a preparation or moisture story, not bad luck.",
        "Do not glue flakes down with fresh paint, ignore damp behind the wall, or pressure-wash interior peeling areas.", "Book a painter after the moisture source is fixed, or urgently if peeling follows a ceiling leak, mould, or large exterior failure."),
    _compact(
        "PST-D02", "termite-signs-home-kashmir", "Termite signs at home? Catch mud tubes early",
        "Pest Control", "pest-control",
        "A thin muddy line appears up a skirting board in a house after monsoon. The family wipes it once; by autumn the door frame sounds hollow when tapped.",
        "Look for mud tubes, hollow wood, discarded wings, and fine sawdust. Do not break open active tubes or spray randomly. Professional inspection and targeted treatment matter.",
        "Mud lines, hollow-sounding wood, or fine dust", "Subterranean termites using hidden routes to wood",
        ["Mud shelter tubes along walls or foundations.", "Hollow door frames, skirting, or furniture edges.", "Swarmers or discarded wings near windows."],
        [("Inspect quietly", "first suspicion", "Check skirting, door frames, stored cardboard, and damp zones with a torch."), ("Tap and listen", "hidden damage", "Hollow or papery sound suggests eaten wood beneath paint."), ("Photograph", "active tubes", "Document before cleaning; breaking tubes can scatter the colony."), ("Remove food sources", "prevention support", "Lift wood off floors, fix damp, and reduce cardboard clutter."), ("Book termite inspection", "any confirmed sign", "Treatment needs mapping the route and choosing the right method.")],
        "We thought it was dirt on the wall until the inspector traced the tube to the frame.", "Arshid",
        "Damp skirting, stored firewood, and old wooden windows give termites quiet routes in Kashmir homes. Early mud tubes are cheaper than a hollow door frame.",
        "Do not spray household insecticide along the whole house, cover tubes with paint only, or ignore hollow wood.", "Book pest control for mud tubes, hollow timber, swarmers, or repeat activity after DIY treatment."),
    _compact(
        "PET-D05", "matted-fur-dog-cat", "Matted fur on your dog or cat? Do not cut blindly",
        "Pet Care", "dog-grooming",
        "A long-haired cat develops tight knots behind the ears after weeks of indoor heat. The owner reaches for kitchen scissors; the skin under the mat is not visible.",
        "Work slowly with a comb, use detangler made for pets, and stop if the pet reacts in pain. Severe mats, skin redness, or mats near eyes and ears need professional grooming or veterinary help.",
        "Tight knots, dull coat, or skin hidden under fur", "Friction, moisture, shedding, or missed brushing",
        ["Behind ears, armpits, and collar area rubbing together.", "Damp coat that dried into tangles.", "Seasonal undercoat not brushed out."],
        [("Look before you cut", "any mat", "Part the fur and check how close the mat sits to skin."), ("Use a comb, not scissors first", "small tangles", "Hold the base of the hair and work from the tip inward gently."), ("Apply pet-safe detangler", "stubborn knots", "Spray lightly and rest before combing again."), ("Split large mats carefully", "thick knots", "Use a mat splitter or see a groomer; do not yank."), ("Book grooming", "wide or painful mats", "Pros can shave safely where home scissors risk cuts.")],
        "The groomer removed the mats without nicks because we stopped trying at home.", "Saba",
        "Indoor heat and damp outdoor coats can tangle quickly in Kashmir winters. Short, regular brushing beats one painful rescue session.",
        "Do not use human detangler, cut mats you cannot see through, or bathe a severely matted pet without planning drying and combing.", "Book pet grooming for large mats, odour, skin redness, or coat change; see a vet for bald patches, sores, or pain."),
    _compact(
        "PLB-D02", "drain-smell-causes-kashmir", "Bad smell from drains? Find where the trap dried out",
        "Plumbing", "plumbing",
        "Every morning a guest bathroom smells like something forgotten. The basin looks clean; the drain may have lost its water seal overnight.",
        "Run water in little-used drains, clean traps and strainers, check for slow drainage, and inspect overflow holes. Persistent sewage smell, gurgling, or multiple drains affected need a plumber.",
        "Sour or sewage smell from basin, floor, or kitchen drain", "Dry trap, biofilm buildup, partial blockage, or vent issue",
        ["Unused floor or guest drains letting traps dry out.", "Hair and soap scum rotting in the trap.", "Partial clog holding stagnant water."],
        [("Run water in unused drains", "guest bath or floor drain", "Pour water until the trap refills; repeat weekly in little-used rooms."), ("Clean strainers and visible traps", "basin smell", "Remove hair and debris; wash the strainer and flush with hot water."), ("Check for slow drainage", "combined smell and slow sink", "A partial clog can trap waste above the trap."), ("Inspect overflow and gaps", "basin-only smell", "Clean overflow holes and seal gaps around fittings."), ("Book a plumber", "whole-house smell", "Shared venting or main-line issues need proper inspection.")],
        "The guest bathroom trap had dried out all winter; water fixed the smell in a day.", "Khalid",
        "In cold months, guest rooms and floor drains go unused for weeks. A dried trap lets sewer gas in even when the room looks spotless.",
        "Do not mask smell with constant bleach alone, ignore gurgling toilets, or mix drain chemicals.", "Book a plumber for sewage smell with slow drains, gurgling, backup in another fixture, or smell after every trap has water."),
    _compact(
        "CLN-D04", "bathroom-mould-hard-water-stains", "Bathroom mould and hard water stains? Ventilation comes first",
        "Cleaning", "professional-cleaning",
        "White crust and grey spots gather around a Batamaloo showerhead every few weeks. Scrubbing harder makes the tiles look scratched and the mould returns in the grout lines.",
        "Improve airflow, reduce standing moisture, use the right cleaner for mould vs limescale, and protect grout. Widespread mould, ceiling patches, or mould after a leak need professional cleaning and source repair.",
        "Black spots in grout or white crust on fittings", "Trapped humidity plus minerals in water",
        ["Poor ventilation after hot showers.", "Hard water leaving mineral scale that traps soap.", "Slow leaks keeping grout damp."],
        [("Dry and ventilate", "after every shower", "Run the fan, wipe glass, and leave the door ajar when safe."), ("Match cleaner to stain", "scale vs mould", "Use descaler on mineral crust; use mould treatment on organic growth in grout."), ("Test on a tile edge", "strong products", "Check that acids or bleach will not etch your finish."), ("Brush grout gently", "light mould", "A stiff brush and suitable product beat endless bleach fumes."), ("Book deep cleaning", "heavy buildup", "Pros can descale fixtures and treat grout without damaging surfaces.")],
        "Opening the window after showers did more than another bottle of bleach.", "Ayesha",
        "Closed bathroom windows through winter keep humidity high in Kashmir flats. Mould and limescale are often a ventilation problem wearing a cleaning disguise.",
        "Do not mix bleach and acid cleaners, scrub glazed tiles with metal pads, or paint over mould.", "Book professional cleaning for ceiling mould, large areas, persistent smell, or stains after a bathroom leak."),
    _compact(
        "VEH-D04", "car-battery-dead-cold-morning", "Car battery dead on a cold morning? Know when to jump and when to replace",
        "Vehicle Care", "car-repair-maintenance",
        "A driveway at 7 am: clicks, dim cabin light, no start. The car was fine yesterday; cold mornings expose a weak battery fast.",
        "Check terminals for corrosion, try lights and horn, jump-start only with correct procedure if needed, and test the battery and charging system. Repeated slow starts mean replacement, not endless jumps.",
        "Clicking starter, dim lights, or no crank on cold morning", "Weak or old battery, loose terminal, or charging fault",
        ["Battery age and cold reducing available power.", "Loose or corroded terminals.", "Alternator not fully recharging after short trips."],
        [("Check terminals", "intermittent start", "Look for white corrosion and wiggle-test clamp tightness safely."), ("Note age and pattern", "repeat cold failure", "Batteries older than about three to five years fail more often in winter."), ("Try a proper jump-start", "single failure", "Follow a safe jump procedure; do not crank endlessly."), ("Drive long enough to recharge", "after a jump", "Short idling may not restore charge; a test is still wise."), ("Get battery and alternator tested", "second failure", "A workshop can load-test instead of guessing.")],
        "The terminal was loose; we almost bought a battery we did not need.", "Faisal",
        "Cold starts after short city trips are hard on batteries in Kashmir winters. Terminals and age deserve a look before an expensive guess.",
        "Do not jump with reversed polarity, keep cranking a weak battery hot, or ignore a battery that fails twice in one week.", "Book vehicle care for repeated no-start, dim lights while driving, warning light on dash, or a battery that fails load test."),
    _compact(
        "WMN-D05", "skin-allergy-after-facial", "Skin reaction after a facial? Cool it down and stop the next product",
        "Women's Salon", "womens-salon",
        "After a cleanup before a family function, cheeks burn and small bumps appear by evening. More scrub and perfume mask is the wrong kind of comfort.",
        "Stop active products, rinse with cool water, avoid heat and makeup, and note what was used. Swelling, breathing difficulty, blistering, or eye involvement needs urgent medical care.",
        "Redness, bumps, burn, or itch after facial", "Irritation or allergy to product, over-exfoliation, or compromised skin barrier",
        ["Strong acids or scrubs on sensitive skin.", "Fragrance or essential oils you have reacted to before.", "Steam or extraction on already irritated skin."],
        [("Stop the routine", "immediate reaction", "Pause actives, scrubs, and new products on affected skin."), ("Cool and soothe", "mild redness", "Use cool water and a simple fragrance-free moisturiser if tolerated."), ("Do not pick or re-scrub", "bumps after cleanup", "Further abrasion worsens barrier damage."), ("Photograph and list products", "follow-up", "This helps the salon or doctor identify the trigger."), ("Seek medical help urgently", "severe signs", "Swelling of face or lips, breathing trouble, or spreading rash needs emergency care.")],
        "They told us to stop everything for 48 hours; the redness settled without more treatment.", "Nazirah",
        "Winter indoor heat already stresses skin; a strong peel before a heated function can tip sensitive skin over the edge.",
        "Do not apply random kitchen remedies, more perfume, or another facial to fix the first reaction.", "Book a dermatologist for severe or persistent reaction; return to the salon only with product list and photos for a gentle follow-up plan."),
]

# Map batch-2 guides to their batch-1 sibling in the same category for related links
_BATCH1_SIBLINGS = {
    "ALU-D02": "aluminium-sliding-window-problems",
    "CRP-D02": "door-not-closing-properly",
    "DRY-D01": "fabric-stains-dry-clean",
    "ELC-D02": "mcb-keeps-tripping-kashmir",
    "GRD-D04": "lawn-looking-dead-kashmir",
    "APP-AC-D02": "ac-not-cooling-kashmir",
    "INT-D05": "false-ceiling-water-stain",
    "MSN-D02": "wall-cracks-cosmetic-structural",
    "MEN-D05": "dandruff-itchy-scalp-men",
    "PNT-D02": "painting-damp-walls-kashmir",
    "PST-D02": "cockroach-control-home-kashmir",
    "PET-D05": "dog-itching-scratching",
    "PLB-D02": "how-to-unblock-kitchen-sink-drain-kashmir",
    "CLN-D04": "sofa-smells-stains-cleaning",
    "VEH-D04": "car-ac-not-cooling",
    "WMN-D05": "hair-damage-after-colour",
}

TITLE_SUBJECTS = {
    "aluminium-door-not-sliding-smoothly": "aluminium sliding door track with rollers and grit",
    "wardrobe-door-slider-problems": "wardrobe sliding door top runner and bracket",
    "sofa-dry-cleaning-vs-home-clean": "sofa fabric care tag and dry clean vs home clean",
    "flickering-lights-causes-kashmir": "light bulb holder flicker with tube and LED lamp",
    "overwatering-garden-plants-kashmir": "potted plant yellow leaves and soggy soil test",
    "ac-leaking-water-kashmir": "split AC indoor unit with condensate drain hose",
    "curtain-rod-falling-sagging": "curtain rod bracket pulling from wall anchor",
    "wall-seepage-plaster-damage-kashmir": "damp wall with flaking plaster and seepage stain",
    "uneven-beard-growth-shape": "beard neckline trim and uneven cheek growth",
    "paint-peeling-kashmir-homes": "interior wall with peeling paint flakes and primer",
    "termite-signs-home-kashmir": "mud tube termite sign on skirting board",
    "matted-fur-dog-cat": "long-haired pet with matted fur behind ear",
    "drain-smell-causes-kashmir": "bathroom sink drain trap and dry seal",
    "bathroom-mould-hard-water-stains": "shower tile grout mould and limescale crust",
    "car-battery-dead-cold-morning": "car battery terminals corrosion on cold morning",
    "skin-allergy-after-facial": "facial skin redness bumps after salon treatment",
}

GUIDES = []
for index, spec in enumerate(_SPECS, 17):
    guide = dict(spec)
    guide["sortOrder"] = index
    sibling = _BATCH1_SIBLINGS[guide["id"]]
    others = [g["slug"] for g in _SPECS if g["slug"] != guide["slug"]]
    guide["relatedGuideSlugs"] = [sibling, others[(index - 17) % len(others)], others[(index - 14) % len(others)]]
    if guide["slug"] == "flickering-lights-causes-kashmir":
        guide["dont_blocks"] = [
            (
                "Wiggle live fittings",
                "Shock and short-circuit risk",
                "Touching a live holder or twisting wires while power is on can cause a shock or spark. Switch off at the breaker before any check.",
                "Hand wiggling a live light bulb holder with power still on",
                "Switch off first",
            ),
            (
                "Bypass a holder with tape or wire",
                "Creates a fire hazard",
                "Taping wires or bypassing a holder leaves bare connections that can overheat. A proper holder or electrician fix is the safe route.",
                "Electrical tape bypassing a damaged light bulb holder with exposed wires",
                "No DIY bypasses",
            ),
            (
                "Ignore flicker with a burning smell",
                "Often means overheating wiring",
                "A burning smell with flicker usually points to arcing or a hot connection, not a bad bulb. Turn off the circuit and book an electrician.",
                "Flickering light fitting with faint smoke wisps and scorch mark while family ignores it",
                "Stop and call help",
            ),
        ]
    if guide["slug"] == "aluminium-door-not-sliding-smoothly":
        guide["dont_blocks"] = [
            (
                "Force a jammed panel",
                "Can crack glass or bend the frame",
                "Shoulder-checking a stuck door stresses rollers and can shatter tempered glass. Stop and clean the track first.",
                "Person forcing a stuck aluminium sliding balcony door with shoulder instead of cleaning the track",
                "Stop before it breaks",
            ),
            (
                "Use heavy grease on the track",
                "Attracts dust and makes sticking worse",
                "Thick oil or grease turns grit into paste in the channel. Dry silicone is the window-safe option.",
                "Applying thick grease to an aluminium door track that already has dust packed in the channel",
                "Dry lube only",
            ),
            (
                "Drill new holes in the frame",
                "Weakens the profile and voids warranty",
                "New holes let water into the frame and rarely fix alignment. Roller adjustment is the proper fix.",
                "Power drill aimed at aluminium door frame instead of adjusting rollers on a sliding panel",
                "Adjust, do not drill",
            ),
        ]
    if guide["slug"] == "drain-smell-causes-kashmir":
        guide["dont_heading"] = "Please don't do this"
        guide["dont_intro"] = "<p>These shortcuts hide the smell briefly and often make the real fault harder to find.</p>"
        guide["dont_blocks"] = [
            (
                "Mask the smell with bleach alone",
                "Hides the symptom, not the cause",
                "Repeated bleach pours do not refill a dry trap and can corrode fittings. Fix the seal or blockage first.",
                "Pouring bleach down a drain to mask smell instead of fixing the trap",
                "Cover-up, not cure",
            ),
            (
                "Ignore a gurgling toilet or slow drain",
                "Often points to venting or a partial clog",
                "Gurgling with smell usually means air or waste is not moving normally. Running water in one basin may not fix a shared line issue.",
                "Gurgling toilet ignored while drain smell continues in the home",
                "Listen for clues",
            ),
            (
                "Mix different drain chemicals",
                "Dangerous fumes and unpredictable reactions",
                "Combining cleaners — or following one with another — can release harmful gas and leave a chemical soup in the trap for whoever opens it next.",
                "Two drain cleaners mixed under a sink with fumes warning",
                "One product, one plan",
            ),
        ]
    if guide["slug"] == "wardrobe-door-slider-problems":
        guide["dont_blocks"] = [
            (
                "Yank a mirrored door",
                "Can shatter the mirror or bend the runner",
                "Heavy mirrored panels need slow, even pressure. Forcing one corner stresses the glass and top guide.",
                "Person yanking a stuck mirrored wardrobe sliding door by one edge",
                "Stop before it breaks",
            ),
            (
                "Spray oil into a full track",
                "Turns lint and dust into sticky paste",
                "Flooding a dirty top or bottom channel with oil traps grit and makes the door ride worse over time.",
                "Spray can squirting oil into a wardrobe track packed with dust and clothing fibres",
                "Clean first, lube sparingly",
            ),
            (
                "Plane wood while the door hangs crooked",
                "Trims the wrong edge and hides the real fault",
                "Shaving a swollen edge before the door is aligned removes material you may need once brackets are fixed.",
                "Hand plane shaving wardrobe door edge while door still sags on crooked runner",
                "Align before you trim",
            ),
        ]
    if guide["slug"] == "sofa-dry-cleaning-vs-home-clean":
        guide["dont_blocks"] = [
            (
                "Saturate the foam",
                "Traps moisture and bakes in odour",
                "Flooding cushions leaves detergent and water in the filling; indoor heat can turn that into a lasting smell.",
                "Person soaking sofa cushion with bucket of soapy water until foam is drenched",
                "Blot, do not flood",
            ),
            (
                "Mix different cleaners",
                "Unpredictable stains and fabric damage",
                "Combining vinegar, bleach, or shop products can set a stain or weaken fibres in ways one product alone would not.",
                "Two upholstery cleaner bottles mixed in a bowl beside a sofa",
                "One product, one test",
            ),
            (
                "Iron a stain",
                "Sets the mark permanently",
                "Heat locks oil and dye into fabric; what looked like a fresh spill becomes a fixed shadow.",
                "Clothes iron pressed onto wet stain on sofa fabric",
                "Blot and air-dry instead",
            ),
        ]
    if guide["slug"] == "overwatering-garden-plants-kashmir":
        guide["dont_blocks"] = [
            (
                "Water because the leaves droop",
                "Overwatering can look like thirst",
                "Limp yellow leaves with wet soil mean too much water, not too little. Check the soil before adding more.",
                "Watering can pouring onto drooping plant with already soggy soil surface",
                "Test soil first",
            ),
            (
                "Leave pots in full saucers",
                "Roots sit in standing water",
                "Saucers that stay full keep the bottom of the pot wet through cool nights and encourage rot.",
                "Plant pot sitting in saucer brim-full of water on a windowsill",
                "Empty after watering",
            ),
            (
                "Repot into dense garden soil alone",
                "Heavy mix holds moisture too long",
                "Plain garden soil in a pot compacts and stays wet indoors; grit or perlite improves drainage.",
                "Bag of heavy garden soil repotted into indoor plant pot without perlite",
                "Lighten the mix",
            ),
        ]
    if guide["slug"] == "ac-leaking-water-kashmir":
        guide["dont_blocks"] = [
            ("Poke the coil with wire", "Can puncture fins and cause a gas leak", "Wire or sharp tools damage delicate coil fins and rarely clear a drain properly.", "Wire being poked into split AC evaporator coil fins", "Clear drain, not coil"),
            ("Ignore oily stains", "May mean refrigerant leak, not condensate", "Oily residue under the unit with poor cooling needs a technician, not more mopping.", "Oily stain under AC indoor unit with water drip", "Book service"),
            ("Run a leaking unit near electrics", "Water and power do not mix", "Active dripping near sockets or wiring risks shock and short circuits.", "AC dripping water onto floor near electrical socket", "Switch off first"),
        ]
    if guide["slug"] == "curtain-rod-falling-sagging":
        guide["dont_blocks"] = [
            ("Screw back into the same crumbled hole", "The bracket will pull out again", "Soft plaster cannot hold the same rawlplug twice; move the anchor to solid material.", "Curtain bracket screw going back into crumbled plaster hole", "Fresh anchor point"),
            ("Use mismatched rawlplugs", "Wrong fixings fail under curtain weight", "Plastic plugs meant for light loads will not hold heavy blackout curtains.", "Wrong size rawlplugs beside falling curtain rod bracket", "Match fixings to wall"),
            ("Ignore a rod that keeps falling", "Risk of injury near the bed", "A rod that drops repeatedly can hit someone sleeping below.", "Curtain rod fallen onto bed pillow at night", "Fix anchors properly"),
        ]
    if guide["slug"] == "wall-seepage-plaster-damage-kashmir":
        guide["dont_blocks"] = [
            ("Skim over active damp", "Peeling returns within one season", "Fresh putty on a wet wall traps moisture and fails quickly.", "Wet plaster patch being skimmed with new putty over active damp", "Dry and fix source first"),
            ("Use ordinary paint as a barrier", "Paint lifts when moisture moves", "Emulsion alone does not stop water entry; it only hides it briefly.", "Paint roller over damp wall with flaking plaster beneath", "Fix leak, then paint"),
            ("Hack plaster open near live wires", "Shock and damage risk", "Cutting into a damp wall without knowing what is behind it is dangerous.", "Chisel opening damp wall near electrical conduit", "Map and isolate first"),
        ]
    if guide["slug"] == "uneven-beard-growth-shape":
        guide["dont_blocks"] = [
            ("Shave against irritated skin daily", "Worsens bumps and patchiness", "Daily aggressive shaving on already red skin slows recovery and irritates follicles.", "Razor shaving red irritated neck skin every morning", "Give skin rest"),
            ("Use random kitchen scissors", "Uneven lines and nicks", "House scissors are not shaped for beard lines and slip easily on wet hair.", "Kitchen scissors trimming beard neckline unevenly", "Use proper tools"),
            ("Compare to filtered photos", "Unrealistic symmetry goals", "Social media beards are lit and edited; chasing that shape leads to over-trimming.", "Man comparing beard in mirror to filtered phone photo", "Work your pattern"),
        ]
    if guide["slug"] == "paint-peeling-kashmir-homes":
        guide["dont_blocks"] = [
            ("Glue flakes down with fresh paint", "New coat peels with the old", "Rolling over lifting flakes traps air and moisture; adhesion fails again.", "Paint roller going over loose peeling paint flakes", "Scrape to firm edge"),
            ("Ignore damp behind the wall", "Peel returns next winter", "Moisture from a leak or cold wall will push through any new topcoat.", "Fresh paint over wall with hidden damp stain spreading", "Fix moisture first"),
            ("Pressure-wash interior peeling areas", "Soaks room and damages plaster", "High-pressure water indoors floods floors and forces moisture deeper into walls.", "Pressure washer aimed at interior bedroom wall", "Scrape and prep dry"),
        ]
    if guide["slug"] == "termite-signs-home-kashmir":
        guide["dont_blocks"] = [
            ("Spray insecticide along the whole house", "Scatters colony, hides routes", "Random spraying drives termites deeper and makes professional mapping harder.", "Household spray bottle used along entire skirting board", "Targeted inspection"),
            ("Cover tubes with paint only", "Hides active infestation", "Painting over mud tubes does not kill termites; damage continues beneath.", "Paint brush covering termite mud tube on skirting", "Photograph and inspect"),
            ("Ignore hollow wood", "Frame damage spreads quietly", "A papery tap sound means eaten timber; waiting risks door frames and floors.", "Hollow-sounding door frame ignored while mud tube visible", "Book inspection"),
        ]
    if guide["slug"] == "matted-fur-dog-cat":
        guide["dont_blocks"] = [
            ("Use human detangler", "Can irritate pet skin", "Human hair products are not pH-safe for cats and dogs and may cause reactions.", "Human hair detangler spray on long-haired cat mat", "Pet-safe products only"),
            ("Cut mats you cannot see through", "Risk of cutting skin", "Scissors under a tight mat can slice skin that is pulled into the knot.", "Scissors cutting hidden mat behind cat ear close to skin", "Part fur first"),
            ("Bathe a severely matted pet unplanned", "Mats tighten when wet", "Water makes knots worse; drying without combing sets tangles harder.", "Soaking matted dog in tub without detangling plan", "Detangle or groom first"),
        ]
    if guide["slug"] == "bathroom-mould-hard-water-stains":
        guide["dont_blocks"] = [
            ("Mix bleach and acid cleaners", "Toxic fumes in small bathroom", "Combining bleach with descaler releases dangerous gas in enclosed spaces.", "Bleach and acid cleaner bottles mixed in shower", "One product at a time"),
            ("Scrub glazed tiles with metal pads", "Scratches finish permanently", "Steel wool etches tile glaze and makes future staining worse.", "Metal scouring pad scrubbing shower tiles hard", "Soft brush instead"),
            ("Paint over mould", "Mould grows through new coat", "Painting without killing mould in grout traps moisture and spreads spores.", "Paint roller over black mould spots in shower grout", "Treat mould first"),
        ]
    if guide["slug"] == "car-battery-dead-cold-morning":
        guide["dont_blocks"] = [
            ("Jump with reversed polarity", "Can damage electronics", "Wrong cable order risks blown fuses and costly ECU damage on modern cars.", "Jumper cables connected wrong polarity on car battery", "Follow correct order"),
            ("Keep cranking a weak battery", "Overheats starter and battery", "Endless cranking on a flat battery generates heat without starting the engine.", "Driver repeatedly cranking car with dim headlights", "Stop and test"),
            ("Ignore two failures in one week", "Battery or charging fault", "Repeat no-start means replace or test — not another jump each morning.", "Car failing to start twice in same cold week ignored", "Get load test"),
        ]
    if guide["slug"] == "skin-allergy-after-facial":
        guide["dont_blocks"] = [
            ("Apply random kitchen remedies", "Can worsen irritation", "Lemon, toothpaste, or spices on reactive skin often burn and delay healing.", "Kitchen ingredients applied to red cheeks after facial", "Keep it simple"),
            ("Add more perfume or actives", "Layers trigger on sensitized skin", "More products on already inflamed skin increases allergy risk.", "Perfume and scrub applied over red post-facial skin", "Stop all actives"),
            ("Book another facial to fix it", "Re-exposure before skin heals", "Repeating treatment before barrier recovery can deepen the reaction.", "Salon facial booked next day on still-red irritated face", "Wait and soothe"),
        ]
    guide["articleHtml"] = _article(guide)
    GUIDES.append(guide)
