"""Batch 4 — Panun Kaergar platform & trust guides (Why Choose Us topics)."""

from html import escape

from guide_image_utils import PROMPT_STYLE, enrich_guide_images

_NO_LOGO = (
    " CRITICAL: No logos, watermarks, brand marks, gear-logo icons, letter monograms, "
    "company names, or PANUN text anywhere in the artwork — illustration content only."
)
_STYLE_LAND = PROMPT_STYLE
_STYLE_SQ = PROMPT_STYLE.replace("16:9 landscape", "1:1 square")

_STYLE_REF = (
    " Match Panun Kaergar Kashmir home troubleshooting guide style exactly: detailed flat vector instructional "
    "diagram with gold callout circles and connecting lines, cream #faf8f4 background, navy #202048 and gold "
    "#FF9900 palette, professional home-service diagram — not cartoon, not stick figures."
)

WHY_CHOOSE_HERO_PROMPTS = {
    "cover": (
        _STYLE_LAND
        + "Hero cover for Kashmir home-services platform: split scene showing small domestic repair on one side "
        "(ceiling fan and dripping tap with gold callout detail) and larger home project on the other "
        "(carpenter on roof timbers, mason with bricks). Calm trustworthy mood."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "title": (
        _STYLE_SQ
        + "Square title card icon for Kashmir home-services platform — house with wrench and shield symbolising "
        "verified trusted local help. Professional calm mood."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "methods": (
        _STYLE_LAND
        + "Infographic showing 6 numbered points for choosing a home-services platform: small jobs, large projects, "
        "verified partners, pricing, booking channels, support. Simple icons connected by gold arrows."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "diagram": (
        _STYLE_LAND
        + "Flow diagram: customer request through verified partner matching to completed job with support backup. "
        "Gold arrows and callout circles."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "tip": (
        _STYLE_LAND
        + "Prevention tip scene: homeowner booking a small tap repair on phone before drip becomes flood damage. "
        "Calm practical mood with instructional callout."
        + _STYLE_REF
        + _NO_LOGO
    ),
}

WHY_CHOOSE_IMAGE_PROMPTS = {
    "method-1": (
        _STYLE_LAND
        + "Method 1: electrician on step ladder repairing ceiling fan in home living room with gold callout on fan motor. "
        "Small everyday repair scene. Helpful, calm, practical."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "method-2": (
        _STYLE_LAND
        + "Method 2: carpenter working on house roof timbers beside mason stacking bricks for home construction repair. "
        "Larger renovation project scene with instructional callouts."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "method-3": (
        _STYLE_LAND
        + "Method 3: home-service partner in navy uniform and cap showing ID badge to homeowner at front door before entering. "
        "Verified professional visit with gold callout on ID card."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "method-4": (
        _STYLE_LAND
        + "Method 4: happy homeowner reading service estimate on smartphone with relaxed smile before work starts. "
        "Transparent pricing scene with gold callout on phone screen."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "method-5": (
        _STYLE_LAND
        + "Method 5: four booking channels as detailed icons — telephone handset, WhatsApp chat bubble, website form on laptop, "
        "mobile app on phone — arranged in a row with gold connecting lines."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "method-6": (
        _STYLE_LAND
        + "Method 6: customer support team — one woman and one man with headsets at desks helping with home-service booking "
        "issue on computers. Friendly professional support scene."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "dont-1": (
        _STYLE_LAND
        + "'What not to do' step 1: ignored small kitchen tap dripping onto cabinet floor. "
        "Show why delaying small repairs fails. Subtle warning feeling — no gore."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "dont-2": (
        _STYLE_LAND
        + "'What not to do' step 2: large renovation quote document beside unanswered ringing phone for small tap repair. "
        "Only big contractors matter myth. Subtle warning feeling."
        + _STYLE_REF
        + _NO_LOGO
    ),
    "dont-3": (
        _STYLE_LAND
        + "'What not to do' step 3: contrast scene — unknown number on phone vs structured booking with verified checkmark "
        "beside home. Platforms cannot be trusted myth debunked."
        + _STYLE_REF
        + _NO_LOGO
    ),
}

_ALL_SLUGS = [
    "why-choose-panun-kaergar-kashmir",
    "home-services-panun-kaergar-handles-kashmir",
    "verified-home-service-partners-kashmir",
    "transparent-pricing-home-services-kashmir",
    "home-service-quality-standards-panun-kaergar",
    "how-to-book-home-services-panun-kaergar-kashmir",
    "panun-kaergar-customer-support-kashmir",
    "panun-kaergar-vs-traditional-booking-kashmir",
]


def _platform_article(item: dict) -> str:
    """SEO-rich article fragment for platform/trust guides."""
    slug = item["slug"]
    enrich_guide_images(item)
    method_imgs = item.get("method_images", [])

    method_parts = []
    for number, ((heading, best_for, detail), img) in enumerate(
        zip(item["methods"], method_imgs), 1
    ):
        alt = img.get("alt", heading)
        cap = img.get("caption", heading)
        method_parts.append(
            f"""<div class="method" id="point-{number}">
  <span class="method-num">Point {number}</span>
  <h3>{escape(heading)}</h3>
  <p class="best-for">Relevant when: {escape(best_for)}</p>
  <p>{escape(detail)}</p>
  <figure class="figure"><img src="/images/guides/{slug}-method-{number}.webp" width="1200" height="675" alt="{escape(alt)}" loading="lazy" />
    <figcaption><strong>{escape(cap)}:</strong> {escape(detail.split('.')[0].strip())}</figcaption>
  </figure>
</div>"""
        )
    methods = "".join(method_parts)

    faqs = "".join(
        f"""<details><summary>{escape(q)}</summary>
  <p>{escape(a)}</p>
</details>"""
        for q, a in item["faqs"]
    )

    causes = "".join(f"<li>{escape(c)}</li>" for c in item["causes"])
    dont_blocks = item.get("dont_blocks")
    if dont_blocks:
        dont_html = "".join(
            f"""<div class="method dont" id="dont-{n}">
  <span class="method-num">Myth {n}</span>
  <h3>{escape(title)}</h3>
  <p class="best-for">{escape(sub)}</p>
  <p>{escape(body)}</p>
  <figure class="figure"><img src="/images/guides/{slug}-dont-{n}.webp" width="1200" height="675" alt="{escape(alt)}" loading="lazy" />
    <figcaption><strong>{escape(cap)}:</strong> {escape(body.split('.')[0].strip())}</figcaption>
  </figure>
</div>"""
            for n, block in enumerate(dont_blocks, 1)
            for title, sub, body, alt, cap in [block[:5]]
        )
    else:
        dont_html = "<ul>" + "".join(f"<li>{escape(d)}</li>" for d in item["donts"]) + "</ul>"

    comparison = item.get("comparison_rows")
    if comparison:
        comp_rows = "".join(
            f"<tr><th scope=\"row\">{escape(row[0])}</th><td>{escape(row[1])}</td><td>{escape(row[2])}</td></tr>"
            for row in comparison
        )
        comparison_html = f"""<h2 id="compare">At a glance</h2>
<p>{escape(item.get("comparison_intro", ""))}</p>
<div class="table-wrap"><table><thead><tr><th>Topic</th><th>Without a platform</th><th>With Panun Kaergar</th></tr></thead><tbody>{comp_rows}</tbody></table></div>"""
    else:
        comparison_html = ""

    overview_rows = item.get("overview_rows", [])
    overview_table = ""
    if overview_rows:
        overview_table = "<div class=\"table-wrap\"><table><thead><tr><th>Job size</th><th>Examples</th><th>How Panun Kaergar helps</th></tr></thead><tbody>"
        overview_table += "".join(
            f"<tr><td><strong>{escape(r[0])}</strong></td><td>{escape(r[1])}</td><td>{escape(r[2])}</td></tr>"
            for r in overview_rows
        )
        overview_table += "</tbody></table></div>"

    return f"""<p class="scene">{escape(item["scene"])}</p>
<div class="answer-box"><span class="label">Quick answer</span><p>{escape(item["quickAnswer"])}</p></div>
<nav class="toc" aria-label="Table of contents"><p class="label">In this guide</p><ol>
  <li><a href="#overview">{escape(item.get("overview_heading", "What this means for you"))}</a></li>
  <li><a href="#problem">{escape(item.get("problem_heading", "The real problem in Kashmir"))}</a></li>
  <li><a href="#how">{escape(item.get("how_heading", "How Panun Kaergar works"))}</a></li>
  {"<li><a href=\"#compare\">At a glance</a></li>" if comparison else ""}
  <li><a href="#kashmir">Kashmir home note</a></li>
  <li><a href="#dont">{escape(item.get("dont_heading", "Common misconceptions"))}</a></li>
  <li><a href="#book">When to book</a></li>
  <li><a href="#faq">FAQs</a></li>
</ol></nav>
<h2 id="overview">{escape(item.get("overview_heading", "What this means for you"))}</h2>
<p>{escape(item["overview_lead"])}</p>
{overview_table}
<h2 id="problem">{escape(item.get("problem_heading", "The real problem in Kashmir"))}</h2>
<p>{escape(item["problem_lead"])}</p><ul>{causes}</ul>
<div class="callout warning"><span class="label">Worth knowing</span><p>{escape(item["warning"])}</p></div>
<h2 id="how">{escape(item.get("how_heading", "How Panun Kaergar works"))}</h2>
<p>{escape(item["how_lead"])}</p>
<figure class="figure"><img src="/images/guides/{slug}-methods.webp" alt="{escape(item['methods_alt'])}" loading="lazy" /><figcaption><strong>Overview:</strong> {escape(item.get("methods_caption", "How Panun Kaergar addresses this for Kashmir households."))}</figcaption></figure>
{methods}
<figure class="figure"><img src="/images/guides/{slug}-diagram.webp" alt="{escape(item['diagram_alt'])}" loading="lazy" /><figcaption><strong>How it fits together:</strong> {escape(item.get("diagram_caption", "The flow from your request to a completed job."))}</figcaption></figure>
<div class="callout pro"><span class="label">Why customers choose us</span><p>{escape(item["pro_tip"])}</p></div>
<div class="review">"{escape(item["review"])}"<cite>— {escape(item["review_by"])}</cite></div>
{comparison_html}
<h2 id="kashmir">Kashmir home note</h2><p>{escape(item["kashmir_note"])}</p>
<h2 id="dont">{escape(item.get("dont_heading", "Common misconceptions"))}</h2>
<p>{escape(item.get("dont_intro", "These assumptions often stop people from getting help — or from choosing a safer option."))}</p>
{dont_html}
<figure class="figure"><img src="/images/guides/{slug}-tip.webp" alt="{escape(item['tip_alt'])}" loading="lazy" /><figcaption><strong>Practical tip:</strong> {escape(item["prevention_caption"])}</figcaption></figure>
<p>{escape(item["prevention"])}</p>
<h2 id="book">When to book through Panun Kaergar</h2><p>{escape(item["book"])}</p>
<p>Ready now? <a href="/book-a-home-service">Book a home service</a> · <a href="/why-choose-panun-kaergar">Why choose Panun Kaergar</a> · <a href="/services">Browse all services</a></p>
<h2 id="faq">FAQs</h2><div class="faq">{faqs}</div>"""


def _spec(
    ident: str,
    slug: str,
    title: str,
    scene: str,
    answer: str,
    overview_lead: str,
    problem_lead: str,
    causes: list[str],
    how_lead: str,
    methods: list[tuple[str, str, str]],
    quote: str,
    person: str,
    kashmir: str,
    warning: str,
    book: str,
    faqs: list[tuple[str, str]],
    *,
    overview_rows: list[tuple[str, str, str]] | None = None,
    comparison_rows: list[tuple[str, str, str]] | None = None,
    comparison_intro: str = "",
    dont_blocks: list[tuple[str, str, str, str, str]] | None = None,
    overview_heading: str = "What this means for you",
    problem_heading: str = "The real problem in Kashmir",
    how_heading: str = "How Panun Kaergar works",
    is_trending: bool = False,
    related_service: str = "",
    reading_minutes: int = 11,
    seo_desc: str = "",
) -> dict:
    subject = title.split("?")[0].lower()
    return dict(
        id=ident,
        slug=slug,
        title=title,
        heroSub=answer.split(".")[0] + ".",
        excerpt=f"{scene.split('.')[0]}. {answer.split('.')[0]}.",
        seoTitle=f"{title} | Panun Kaergar",
        seoDescription=seo_desc or (
            f"{answer.split('.')[0]}. Practical guide for Kashmir households booking verified home services through Panun Kaergar."
        ),
        category="General",
        relatedServiceSlug=related_service,
        readingMinutes=reading_minutes,
        scene=scene,
        quickAnswer=answer,
        overview_lead=overview_lead,
        overview_heading=overview_heading,
        problem_lead=problem_lead,
        problem_heading=problem_heading,
        how_lead=how_lead,
        how_heading=how_heading,
        causes=causes,
        methods=methods,
        methods_alt=f"Panun Kaergar guide illustration for {subject}",
        methods_caption="What Panun Kaergar does differently for customers in Kashmir.",
        diagram_alt=f"How {subject} works with Panun Kaergar",
        diagram_caption="From your request to a verified partner at your door.",
        pro_tip=(
            "Panun Kaergar is built in Kashmir for Kashmir — not a generic listing copied from another city. "
            "That local focus is why small jobs get attention here."
        ),
        review=quote,
        review_by=person.split(",")[0].strip(),
        kashmir_note=kashmir,
        warning=warning,
        dont_heading="Common misconceptions",
        dont_intro="These assumptions often stop people from getting help — or from choosing a safer option.",
        donts=[
            "Assuming every home-service platform works the same in every city.",
            "Waiting until a small repair becomes an expensive emergency.",
            "Booking without asking for a clear estimate when the job allows it.",
        ],
        prevention=(
            "Save Panun Kaergar's booking channels before you need them. "
            "When a tap drips or a switch fails, one message is faster than searching contacts at midnight."
        ),
        prevention_caption="Keep one trusted booking path for every job size.",
        book=book,
        faqs=faqs,
        tip_alt=f"Practical tip for {subject} in Kashmir",
        overview_rows=overview_rows or [],
        comparison_rows=comparison_rows,
        comparison_intro=comparison_intro,
        dont_blocks=dont_blocks,
        isTrending=is_trending,
    )


_SPECS = [
    _spec(
        "PK-G00",
        "why-choose-panun-kaergar-kashmir",
        "Why choose Panun Kaergar for home and commercial services in Kashmir?",
        "A shop owner in Srinagar gets three contractors to quote for a full storefront renovation. The same week, a family cannot find anyone to fix a bathroom tap that has dripped for ten days. Big work attracts proposals; small domestic jobs are left waiting. That imbalance is exactly why Panun Kaergar exists.",
        "Choose Panun Kaergar for verified local professionals, transparent pricing, and simple booking across every home and commercial domestic need in Kashmir — from a twenty-minute tap repair or switch install to multi-day painting, renovation, salon, cleaning, pest control, and appliance work. Small jobs get the same respect as large projects.",
        "Panun Kaergar is Kashmir's trusted home-services platform — built for households, rented flats, guesthouses, small offices, and commercial spaces that need reliable help without chasing contacts. One booking path covers plumbing, electrical, cleaning, salon, appliances, carpentry, masonry, painting, pest control, gardening, pet care, vehicle help, and more.",
        "Kashmir's informal service market rewards size. Renovation contractors, painters, and builders compete to send proposals for work worth lakhs. But when a geyser stops heating, a drain blocks, a salon appointment is needed at home, or a shop needs a quick electrical fix — the same network often goes silent. Families and business owners are left calling numbers that do not answer, waiting days for a five-minute job, or paying emergency rates because they had no alternative.",
        [
            "Large projects get multiple quotes; small repairs get ignored.",
            "No verification when you hire through personal contacts alone.",
            "Pricing agreed verbally — disputes when the bill arrives.",
            "No one to call when a worker no-shows or does poor work.",
            "Commercial and domestic needs treated as separate worlds with no single place to book.",
        ],
        "Panun Kaergar brings structure without losing local skill. We verify partners, share pricing guidance upfront, match by neighbourhood, and stand behind every booking with a support team. Whether you manage a home, a shop, or a small commercial space, you get the same process — describe the job, get a verified partner, confirm the cost, and reach us if anything goes wrong.",
        [
            (
                "Small jobs get done",
                "a ceiling fan, tap drip, or switch fix",
                "A Panun Kaergar technician repairs a ceiling fan, fixes a dripping tap, or replaces a faulty switch — everyday jobs that other workers often ignore as 'not worth the visit.'",
            ),
            (
                "Large projects welcome",
                "renovation, roofing, and masonry",
                "Book carpenters for roofing work, masons for house construction or repairs, and painters for full-home projects. Site visits and written proposals are available for bigger scopes.",
            ),
            (
                "Verified local partners",
                "before anyone enters your space",
                "Every partner wears a Panun Kaergar uniform and ID card, passes identity and trade checks, and is reviewed through ongoing customer ratings.",
            ),
            (
                "Transparent pricing guidance",
                "before work starts",
                "Receive an estimate or rate range on your phone before the visit. Material and labour additions should be explained upfront — not sprung on you when the job is half done.",
            ),
            (
                "Book your way — four channels",
                "phone, WhatsApp, web, or app",
                "Call our support line, send a WhatsApp message, fill the online booking form, or use the free Panun Kaergar app — whichever suits you.",
            ),
            (
                "Real support when it matters",
                "no-shows, complaints, reschedules",
                "Our Srinagar-based support team — men and women handling calls and messages — helps with reschedules, billing questions, and complaints.",
            ),
        ],
        "We had given up on the tap. Panun Kaergar sent someone the same evening — for a job every plumber we knew called 'too small.'",
        "Nighat, Rajbagh",
        "Kashmir mixes old timber homes, modern apartments, guesthouses, and small commercial units — often in the same neighbourhood. A platform built here understands that a geyser failure in winter, a shop wiring check before Eid rush, and a salon visit at home are all real daily needs, not 'small enough to ignore.'",
        "Do not delay small repairs until they become expensive emergencies. A drip, a spark, or a pest sign today is cheaper to fix than a flooded cabinet, a short circuit, or an infestation next month.",
        "Choose Panun Kaergar for your next home or commercial domestic service in Kashmir — especially when local contacts have stopped responding to small requests. Call, WhatsApp, book online, or use the app.",
        [
            (
                "Why should I choose Panun Kaergar over calling a local technician?",
                "You get a verified partner, upfront pricing guidance, a booking record, and a support team — while still hiring local skilled professionals.",
            ),
            (
                "Does Panun Kaergar handle small repairs?",
                "Yes. Small repairs and quick installs are a core reason the platform exists. Jobs others call 'not worth the visit' are booked every day through Panun Kaergar.",
            ),
            (
                "Can I book commercial or domestic work?",
                "Yes. Panun Kaergar serves households, rented flats, guesthouses, shops, and small commercial spaces for plumbing, electrical, cleaning, salon, appliances, and more.",
            ),
            (
                "How are partners verified?",
                "Identity and contact checks, trade review, onboarding on quality standards, and ongoing ratings and complaint monitoring.",
            ),
            (
                "Is pricing transparent?",
                "Estimates or rate guidance are shared before most visits. No hidden platform booking fee on standard requests.",
            ),
            (
                "How do I book?",
                "Phone, WhatsApp, the website booking form, or the free Panun Kaergar app. Describe the job — we match a verified partner in your area.",
            ),
            (
                "What areas do you cover?",
                "Srinagar and multiple districts across Kashmir. Mention your neighbourhood when booking.",
            ),
            (
                "What if I am not satisfied?",
                "Contact support by phone or WhatsApp. We investigate and work toward a fair resolution.",
            ),
        ],
        overview_heading="Why Panun Kaergar exists",
        problem_heading="The small-job gap in Kashmir",
        how_heading="What you get when you choose Panun Kaergar",
        overview_rows=[
            (
                "Small domestic (under 1 hr)",
                "Tap drip, switch fix, door adjustment, AC filter, socket repair, minor leak",
                "Same booking path — verified partner, estimate, and support behind every request",
            ),
            (
                "Medium home & shop (half–full day)",
                "Room painting, bathroom repair, deep clean, pest treatment, geyser service, salon at home",
                "Matched specialist with clear scope and pricing guidance",
            ),
            (
                "Large home & commercial",
                "Full flat painting, renovation, masonry packages, aluminium fitting, multi-room work",
                "Site visit, written proposal, and tracked project support",
            ),
        ],
        comparison_rows=[
            ("Finding help", "Ask around, try saved numbers, hope someone answers", "One request; Panun Kaergar matches a verified local partner"),
            ("Small jobs", "Often ignored — 'not worth the visit'", "Booked daily through the same platform as large work"),
            ("Trust", "Word of mouth only", "Identity checks, trade review, and customer ratings"),
            ("Pricing", "Discussed on arrival, disputed later", "Estimate or rate guidance before the visit"),
            ("Accountability", "Resolve alone with the worker", "Support team for complaints, no-shows, and reschedules"),
            ("Home & commercial", "Separate contact lists for each", "One platform for domestic and small commercial needs"),
        ],
        comparison_intro="Choosing Panun Kaergar changes how you find, book, and trust home and commercial domestic services in Kashmir — without replacing local skilled workers.",
        is_trending=True,
        related_service="plumbing",
        reading_minutes=13,
        seo_desc="Why choose Panun Kaergar for home and commercial services in Kashmir? Verified partners, transparent pricing, and booking for every job size — from small tap repairs to full renovation projects.",
        dont_blocks=[
            (
                "Small jobs are not worth booking",
                "They become expensive later",
                "A ignored drip, loose wire, or pest sign often turns a quick fix into a costly emergency repair.",
                "Small kitchen tap dripping onto cabinet floor with ignored repair list",
                "Book early",
            ),
            (
                "Only big contractors matter",
                "Everyday help keeps homes running",
                "Most households need reliable small-job partners more often than a renovation crew.",
                "Large renovation quote beside unanswered phone for small tap repair",
                "All sizes matter",
            ),
            (
                "Platforms cannot be trusted",
                "Structure adds accountability",
                "Panun Kaergar verifies partners, records bookings, and provides support — more protection than an unknown number.",
                "Verified partner badge on phone booking screen beside Kashmir home",
                "Verified and supported",
            ),
        ],
    ),
    _spec(
        "PK-G01",
        "home-services-panun-kaergar-handles-kashmir",
        "What home services does Panun Kaergar handle in Kashmir? From small repairs to full projects",
        "A contractor quotes happily for a full kitchen renovation. The same person does not answer when you need a leaking tap fixed on a Tuesday evening. In Kashmir, that gap between big-project interest and small-job silence is painfully familiar.",
        "Panun Kaergar handles home services of every size in Kashmir — from a single switch replacement or tap repair to full-room painting, pest treatment, salon visits, appliance service, and larger renovation work. Big projects can receive detailed proposals; small repairs and installs get the same booking path, verified partners, and support team behind them.",
        "Panun Kaergar is Kashmir's home-services platform — one place to book verified local professionals across plumbing, electrical, cleaning, salon, appliances, carpentry, masonry, pest control, gardening, pet care, vehicle help, and more. Whether the job takes twenty minutes or twenty days, you describe it once and we route it to a partner who can actually do the work.",
        "In Kashmir's informal service market, large jobs attract attention because they promise bigger earnings. Contractors compete to send proposals for renovations, full painting contracts, and major builds. Small repairs — a loose door hinge, a blocked drain, a geyser that stopped heating, a salon appointment at home — often get ignored because the trip and negotiation do not feel worth it to many workers.",
        [
            "Technicians say a small job is 'not worth the visit' and never call back.",
            "Families keep a list of numbers that worked once — until they do not.",
            "Urgent small fixes get delayed until they become expensive damage.",
            "Big-project contractors are available; everyday household help is not.",
        ],
        "Panun Kaergar was built to close that gap. Small jobs are not afterthoughts — they are why most households need help in the first place. The platform aggregates demand across Srinagar and Kashmir so partners receive steady booking requests, including work that would otherwise be too small for someone to chase individually.",
        [
            (
                "Small repairs and quick installs",
                "a dripping tap, loose handle, or single switch",
                "Book plumbing, electrical, carpentry, or appliance help for jobs that take under an hour. Panun Kaergar matches a verified partner in your area instead of you calling five numbers.",
            ),
            (
                "Routine home maintenance",
                "seasonal checks and preventive work",
                "Geyser descaling before winter, AC filter cleaning before summer, drain checks, and minor masonry touch-ups — maintenance that prevents bigger bills later.",
            ),
            (
                "Medium household services",
                "half-day or full-day jobs",
                "Bathroom leak repair, room painting, deep kitchen cleaning, pest treatment, sofa cleaning, salon at home, and multi-point electrical checks.",
            ),
            (
                "Larger projects with proposals",
                "renovation and multi-room work",
                "For bigger scopes — full flat painting, carpentry packages, masonry repairs, aluminium work — partners can assess on site and share a detailed proposal before work begins.",
            ),
            (
                "Lifestyle and vehicle services",
                "beyond walls and wires",
                "Men's and women's salon, pet grooming, dry cleaning pickup, garden care, and car AC or battery help — everyday services Kashmir households book through the same platform.",
            ),
        ],
        "I finally got someone for a tap that had dripped for three weeks. Every plumber I knew was 'busy with a big site.'",
        "Nighat, Rajbagh",
        "Kashmir homes mix old timber construction, modern fittings, harsh winters, and busy festival seasons. A platform that only chases large contracts misses what most families actually need on a random Wednesday — someone reliable for the small thing that is ruining the week.",
        "Do not assume a small job is too minor to book properly. Delaying a drip, spark, or pest sign often turns a ₹500 fix into a ₹5,000 repair.",
        "Book through Panun Kaergar for any home, garden, salon, pet, or vehicle service in Kashmir — especially when local contacts have stopped responding to small requests. Call, WhatsApp, use the website form, or the free app.",
        [
            (
                "What types of home services does Panun Kaergar offer in Kashmir?",
                "Panun Kaergar covers plumbing, electrical, cleaning, salon (men's and women's), home appliances, carpentry, masonry, painting, pest control, gardening, interior repair, aluminium and glass work, dry cleaning, pet care, vehicle care, and hiring help — across Srinagar and districts in Kashmir.",
            ),
            (
                "Does Panun Kaergar handle small repairs?",
                "Yes. Small repairs and quick installs are a core reason the platform exists. Jobs like tap fixes, switch replacement, door adjustment, and single-appliance checks are booked every day — not treated as too small to matter.",
            ),
            (
                "Can I book large renovation projects through Panun Kaergar?",
                "Yes. For larger scopes, a verified partner can visit, assess the work, and share a proposal. You get the same support and verification whether the job is small or spans multiple rooms.",
            ),
            (
                "Why is it hard to find help for small jobs in Kashmir?",
                "Many skilled workers prioritise larger contracts with higher payouts. Without a platform aggregating small requests, individual households struggle to make a twenty-minute job worth a technician's trip.",
            ),
            (
                "Is Panun Kaergar only for Srinagar?",
                "Panun Kaergar serves Srinagar and multiple districts across Kashmir. Mention your area when booking — partners are matched by neighbourhood and service type.",
            ),
            (
                "How do I book?",
                "Call, WhatsApp, fill the form at panunkaergar.com/book-a-home-service, or use the free Panun Kaergar app. Describe the job size honestly — small or large — and we route it appropriately.",
            ),
        ],
        overview_rows=[
            (
                "Small (under 1 hour)",
                "Tap drip, switch replacement, door adjustment, AC filter, single socket, minor leak",
                "Same booking path as any job — verified partner, estimate, and support",
            ),
            (
                "Medium (half to full day)",
                "Room painting, bathroom repair, deep clean, pest treatment, geyser service",
                "Matched specialist with clear scope and pricing guidance",
            ),
            (
                "Large (multi-day / proposal)",
                "Full flat painting, renovation packages, major masonry, aluminium fitting",
                "Site visit, written proposal, and tracked project support",
            ),
        ],
        is_trending=True,
        related_service="plumbing",
        seo_desc="Panun Kaergar handles every home service in Kashmir — small tap repairs, installs, cleaning, salon, appliances, and large renovation projects. Book verified local partners for jobs others ignore.",
        dont_blocks=[
            (
                "Small jobs are not worth booking",
                "They become big problems",
                "A ignored drip damages cabinets; a loose wire risks a short. Panun Kaergar exists so you do not wait until the job grows.",
                "Small dripping kitchen tap with water pooling under sink",
                "Book early",
            ),
            (
                "Only contractors handle real work",
                "Everyday help matters more",
                "Most households need reliable small-job partners more often than a renovation crew.",
                "Homeowner comparing large renovation quote with ignored small repair call list",
                "All sizes welcome",
            ),
            (
                "You must know the right contact",
                "One platform replaces the hunt",
                "Panun Kaergar routes your request to a verified partner — you do not need the 'right uncle's number.'",
                "Phone contact list with many unanswered service numbers",
                "One booking path",
            ),
        ],
    ),
    _spec(
        "PK-G02",
        "verified-home-service-partners-kashmir",
        "How does Panun Kaergar verify home service partners in Kashmir?",
        "A stranger arrives to fix the geyser. The family asks who sent him; he says a neighbour recommended him. That answer was enough for generations — until it was not.",
        "Panun Kaergar verifies every service partner before they receive live bookings: identity and contact checks, trade and experience review, onboarding on quality standards, and ongoing monitoring through customer ratings and support feedback.",
        "Verification on Panun Kaergar means more than a profile photo. Partners complete a structured onboarding process before they are assigned customer jobs. You book someone our team has checked — not a random name from a forwarded contact.",
        "In Kashmir, trust in home services has traditionally depended on family recommendations. That works until you move neighbourhoods, need a new trade, or the recommended person is unavailable. Unverified workers create real risk: incomplete work, no accountability, and no one to call when something goes wrong.",
        [
            "No standard check on who enters your home.",
            "Skills claimed on a card may not match actual experience.",
            "No record if the same worker causes problems at multiple homes.",
            "Customers have no platform to escalate complaints.",
        ],
        "Panun Kaergar's verification process is designed for households that want local skilled workers with accountability attached. Partners are onboarded, monitored, and managed — so verification is not a one-time stamp but an ongoing standard.",
        [
            (
                "Identity and contact verification",
                "before any live booking",
                "Partners submit valid ID and reachable phone numbers. Our team confirms details before activating a profile.",
            ),
            (
                "Trade and experience review",
                "matching skills to categories",
                "We review which services a partner claims — plumbing, electrical, cleaning, salon, and more — against their experience and chosen work areas.",
            ),
            (
                "Onboarding and guidelines",
                "setting expectations early",
                "New partners learn how bookings work, how to communicate with customers, and what quality standards apply before receiving requests.",
            ),
            (
                "Customer ratings and reviews",
                "after every completed job",
                "Completed jobs can be rated. Strong performance builds reputation; repeated poor experiences trigger investigation.",
            ),
            (
                "Ongoing performance management",
                "keeping standards high",
                "Support tickets, completion rates, and complaint patterns feed into partner management. Serious or repeat issues can lead to suspension.",
            ),
        ],
        "Knowing he was verified made a difference — we let him in without the usual twenty questions.",
        "Sajad, Bemina",
        "Kashmir has deep networks of skilled tradespeople. Panun Kaergar does not replace that talent — it makes it visible, checkable, and accountable to customers who may not have a family connection to every trade.",
        "Verification reduces risk; it does not remove the need for clear communication. Always confirm the job scope and estimate before work begins.",
        "Book through Panun Kaergar when you want a verified local partner for any home service in Kashmir — especially when you do not have a trusted personal contact for that trade.",
        [
            ("How are Panun Kaergar partners verified?", "Through identity checks, trade review, onboarding, and ongoing rating and complaint monitoring."),
            ("Can anyone join as a partner?", "Partners apply and are reviewed before going live. Not every application is approved."),
            ("What if a verified partner does poor work?", "Contact Panun Kaergar support. We investigate complaints and can take action on repeat issues."),
            ("Are partners employees of Panun Kaergar?", "Partners are independent skilled professionals who use the platform to receive bookings. Panun Kaergar verifies and manages them."),
            ("Why does verification matter for small jobs?", "Small jobs still let someone into your home. Verification matters regardless of job size."),
        ],
        related_service="electrician",
        seo_desc="How Panun Kaergar verifies home service partners in Kashmir — identity checks, trade review, onboarding, ratings, and ongoing quality monitoring before they enter your home.",
    ),
    _spec(
        "PK-G03",
        "transparent-pricing-home-services-kashmir",
        "Are Panun Kaergar home service prices transparent? What to expect before you pay",
        "The plumber finishes in forty minutes. The bill is twice what was discussed on the phone — because 'parts were extra' and 'it was more complicated.' The family pays, annoyed, and tells everyone the story.",
        "Panun Kaergar aims for transparent pricing: estimates or rate guidance before work begins, no hidden platform booking fee for standard requests, clear explanation of material costs, and a booking record in the app.",
        "Transparent pricing means you understand what a job is likely to cost before a partner starts — not only when the work is finished. Panun Kaergar shares estimates or rate ranges upfront for most services.",
        "Home-service pricing in Kashmir is often informal. A worker quotes on the phone, adds items on site, and the customer has little recourse. Without a written estimate or platform record, disputes become he-said-she-said.",
        [
            "Phone quotes that change after the visit.",
            "Material costs added without prior discussion.",
            "No record of what was agreed.",
            "Customers afraid to question the final bill.",
        ],
        "Panun Kaergar structures pricing communication so surprises are less common. Partners are expected to explain scope and cost before proceeding — especially when materials or extra labour are needed.",
        [
            (
                "Estimate before the visit",
                "most standard services",
                "When you book, you receive price guidance or an estimate range. Complex jobs may need an on-site inspection first — that is explained upfront.",
            ),
            (
                "No hidden booking fee",
                "standard customer requests",
                "Panun Kaergar does not add a separate platform booking fee on top of the service charge for typical home-service bookings.",
            ),
            (
                "Material costs explained first",
                "repairs needing parts",
                "If a pipe, switch, filter, or consumable is required, the partner should explain the additional cost before installing it.",
            ),
            (
                "App booking history",
                "tracking what was agreed",
                "App users keep a record of requests, assigned partners, and job status — useful if you need to follow up on pricing.",
            ),
            (
                "Support for billing questions",
                "when something does not match",
                "If the final charge differs significantly from what was discussed, contact Panun Kaergar support with your booking details.",
            ),
        ],
        "They told me the part cost before fitting it. That alone felt new.",
        "Imtiyaz, Hyderpora",
        "Winter repairs often need extra parts — geyser elements, pipe insulation, heating components. In Kashmir, a clear parts breakdown before installation prevents the arguments that happen when a bill arrives in the cold.",
        "An estimate is guidance, not a guarantee for every unforeseen fault found on site. Honest partners explain new findings before expanding scope.",
        "Book through Panun Kaergar when you want pricing discussed clearly before work begins — for taps, wiring, cleaning, salon, appliances, and every other service category.",
        [
            ("Is Panun Kaergar pricing transparent?", "Yes — estimates or rate guidance are shared before most visits, and material additions should be explained upfront."),
            ("Are there hidden fees?", "Panun Kaergar does not add a separate booking fee for standard customer requests."),
            ("What if the price changes on site?", "The partner should explain why before proceeding. Contact support if the final bill differs significantly without explanation."),
            ("Do all services have fixed prices?", "Some jobs need on-site assessment first. You will be told when that applies."),
            ("Can I get a written estimate?", "For larger jobs, partners can provide a detailed proposal after assessment."),
        ],
        related_service="plumbing",
        seo_desc="Transparent home service pricing in Kashmir — estimates before work, no hidden booking fees, clear material costs, and support if your bill does not match what was agreed.",
    ),
    _spec(
        "PK-G04",
        "home-service-quality-standards-panun-kaergar",
        "What quality standards does Panun Kaergar expect from every home service visit?",
        "The electrician leaves the switch plate loose. The cleaner misses the corner behind the fridge. Small slips add up — and customers wonder whether anyone actually cares.",
        "Panun Kaergar expects every partner to arrive prepared, respect appointment times, care for your home, give honest recommendations, and complete work to a professional standard — with ratings and support backing those expectations.",
        "Quality on Panun Kaergar is not abstract. We define what a good visit looks like — and customers can rate partners so standards are visible to the next household booking.",
        "Without standards, home services become a lottery. One visit is excellent; the next is careless. Customers in Kashmir deserve consistency — especially when they are paying and letting someone into their home.",
        [
            "Partners arriving without proper tools.",
            "Missed appointment windows with no communication.",
            "Work areas left messy after the job.",
            "Unnecessary upselling of repairs that are not needed.",
        ],
        "Panun Kaergar sets clear expectations for partners and tracks performance. Quality is enforced through onboarding, customer ratings, and support intervention when standards slip.",
        [
            (
                "Arrive prepared",
                "every accepted job",
                "Partners should bring the right tools and materials for the service category they accepted.",
            ),
            (
                "Respect your time",
                "confirmed appointments",
                "Visit windows should be honoured. Delays should be communicated to you and to support when possible.",
            ),
            (
                "Care for your home",
                "during and after work",
                "Work areas should be left tidy. Your property should be treated with care.",
            ),
            (
                "Honest recommendations",
                "when advising on repairs",
                "If a cheaper fix exists or a repair is not worth doing, partners should say so.",
            ),
            (
                "Rate your experience",
                "after completion",
                "Your rating helps the next customer choose confidently and helps Panun Kaergar maintain standards.",
            ),
        ],
        "The partner cleaned up after the repair — that sounds basic, but it is rare.",
        "Farah, Lal Chowk",
        "In Kashmir's winter, wet boots, tool bags, and work materials cross clean floors daily. Partners who protect surfaces and clean up stand out — and earn repeat bookings.",
        "Quality standards apply to every job size. A small switch fix deserves the same professionalism as a full-day renovation visit.",
        "Book through Panun Kaergar when you want accountable, rated professionals — and rate your experience so the platform stays trustworthy for everyone.",
        [
            ("What quality standards does Panun Kaergar enforce?", "Prepared arrival, punctuality, home care, honest advice, and professional completion — backed by ratings and support."),
            ("Can I report poor quality?", "Yes. Contact support by phone or WhatsApp with your booking details."),
            ("Do ratings matter?", "Yes. They help future customers and inform partner management."),
            ("What if a partner no-shows?", "Contact support immediately. We help reschedule or assign another partner."),
        ],
        related_service="professional-cleaning",
        seo_desc="Panun Kaergar quality standards for every home service visit — prepared arrival, punctuality, home care, honest advice, and customer ratings that keep partners accountable.",
    ),
    _spec(
        "PK-G05",
        "how-to-book-home-services-panun-kaergar-kashmir",
        "How to book home services through Panun Kaergar in Kashmir",
        "The geyser fails on a Sunday. The family's contact list has three plumbers — one does not answer, one is out of town, one says 'call tomorrow.' They need a path that works today.",
        "Book Panun Kaergar home services by phone, WhatsApp, the website booking form, or the free mobile app. Describe the service, your area, and preferred time — we match a verified local partner and confirm details before the visit.",
        "Booking through Panun Kaergar takes minutes. You do not need to know which specific technician is free — you describe the job and the platform handles matching.",
        "Traditional booking in Kashmir depends on personal networks and luck. If your contact is busy, you start again. Panun Kaergar gives every household the same structured path — regardless of who they know.",
        [
            "Searching for the right phone number for each trade.",
            "No confirmation that anyone is actually coming.",
            "No record of what was requested.",
            "Different process for every type of service.",
        ],
        "One booking flow covers every service category. The channel you choose — call, chat, form, or app — feeds the same system and support team.",
        [
            (
                "Call to book",
                "urgent or complex jobs",
                "Phone our support line during business hours. Tell us the service, area, and preferred time.",
            ),
            (
                "WhatsApp",
                "quick requests with details",
                "Message us with the service type, your neighbourhood, and photos if helpful. We reply quickly during support hours.",
            ),
            (
                "Website booking form",
                "planned services",
                "Fill the form at panunkaergar.com/book-a-home-service with service, area, date, and notes.",
            ),
            (
                "Panun Kaergar mobile app",
                "tracking and rebooking",
                "Download the free app to book, track status, view history, and rebook familiar services.",
            ),
            (
                "Confirmation before the visit",
                "every booking",
                "A partner or our team confirms the visit window and expected cost before anyone arrives.",
            ),
        ],
        "I booked on WhatsApp during lunch break. Someone confirmed by evening.",
        "Aqsa, Zakura",
        "Winter evenings are when geysers, heaters, and electrical loads fail together. Having one booking number — instead of five silent contacts — matters most when it is cold and dark.",
        "Describe the job accurately when booking. A small tap drip and a major pipe burst need different partners and pricing — honesty upfront saves time.",
        "Book now for any home service in Kashmir — especially when your usual contacts are not responding.",
        [
            ("How do I book a home service in Kashmir?", "Call, WhatsApp, use the website form, or the Panun Kaergar app."),
            ("Do I need the app?", "No. Phone, WhatsApp, and the website work for all customers."),
            ("How fast can someone come?", "Depends on service and availability. Urgent requests are prioritised when possible."),
            ("Can I book for a specific area?", "Yes. Mention your neighbourhood or district when booking."),
            ("What information should I provide?", "Service type, location, preferred time, and a short description of the problem."),
        ],
        related_service="home-appliances",
        seo_desc="How to book home services in Kashmir through Panun Kaergar — by phone, WhatsApp, website form, or free app. One path for every service from small repairs to large projects.",
    ),
    _spec(
        "PK-G06",
        "panun-kaergar-customer-support-kashmir",
        "Panun Kaergar customer support: who helps when a home service goes wrong?",
        "The technician never showed. The family called his personal number twice; it went to voicemail. With no office to call, the afternoon was wasted.",
        "Panun Kaergar provides real customer support by phone, WhatsApp, and email — for reschedules, billing questions, complaints, and follow-up when a job does not go as planned.",
        "When you book through Panun Kaergar, you are not alone with a worker's personal number. Our Srinagar-based support team helps when something goes wrong.",
        "Informal booking means informal resolution. If a worker no-shows or overcharges, the customer often has no one to escalate to. That is the problem a platform with support is designed to solve.",
        [
            "No-shows with no one to call except the worker.",
            "Billing disputes with no neutral party.",
            "Reschedule chaos when plans change.",
            "No record of what was promised.",
        ],
        "Panun Kaergar support exists for the moments booking apps ignore — when the partner is late, the scope changes, or you need a human to intervene.",
        [
            (
                "Phone support",
                "active bookings and urgent issues",
                "Call during support hours for booking help, reschedules, and complaints about active jobs.",
            ),
            (
                "WhatsApp support",
                "quick follow-up",
                "Message with your booking details, area, and issue. Most queries get a reply within minutes during hours.",
            ),
            (
                "Email for documentation",
                "non-urgent queries",
                "Email for feedback, documentation requests, or detailed complaints you want in writing.",
            ),
            (
                "Complaint investigation",
                "unsatisfactory work",
                "Support reviews the complaint, speaks with the partner when needed, and works toward fair resolution.",
            ),
            (
                "Reschedule and reassignment",
                "when plans change",
                "If a partner cannot make it or you need a different time, support helps rebook rather than leaving you stranded.",
            ),
        ],
        "Support called the partner when he was late. They rescheduled within the hour.",
        "Rukhsar, Nowgam",
        "Snow, curfews, and traffic in Srinagar affect appointment timing. A support team that knows the city can reschedule realistically — not just promise 'soon.'",
        "Support helps resolve issues — it does not do the technical repair itself. For the actual fix, a qualified partner still completes the work.",
        "Book through Panun Kaergar when you want backup behind every booking — not just a phone number that may not answer.",
        [
            ("How do I contact Panun Kaergar support?", "By phone, WhatsApp, or email — details on the Contact page and in your booking confirmation."),
            ("What can support help with?", "Reschedules, billing questions, complaints, no-shows, and general booking help."),
            ("What are support hours?", "Office Monday–Saturday 10:00–18:00; call centre daily 10:00–22:00."),
            ("What if I am not satisfied with the service?", "Contact support with booking details. We investigate and work toward resolution."),
        ],
        related_service="carpentry",
        seo_desc="Panun Kaergar customer support in Kashmir — phone, WhatsApp, and email help for reschedules, billing questions, no-shows, and complaints when a home service does not go as planned.",
    ),
    _spec(
        "PK-G08",
        "panun-kaergar-vs-traditional-booking-kashmir",
        "Panun Kaergar vs traditional local booking: what actually changes for customers?",
        "Two neighbours need a plumber. One calls a cousin's contact; the other books through Panun Kaergar. Same city, same week — very different experiences when something goes wrong.",
        "Compared to traditional local booking, Panun Kaergar offers verified partners, transparent pricing guidance, multiple booking channels, a support team for complaints, and a record of every request — without replacing Kashmir's skilled local workforce.",
        "Traditional booking relies on personal contacts. Panun Kaergar adds verification, pricing clarity, structured booking, and accountability — while still using local skilled partners.",
        "Traditional booking worked when everyone knew everyone. Urban Kashmir moves faster now — new neighbourhoods, rented flats, young families without decades of contacts. The gap is structure, not talent.",
        [
            "Finding the right contact takes time every time.",
            "No verification beyond word of mouth.",
            "Pricing agreed verbally with no record.",
            "No one to call when the worker no-shows.",
        ],
        "Panun Kaergar does not replace local craftsmen — it gives them a platform and gives customers protection. The comparison is about process and accountability, not foreign vs local.",
        [
            (
                "Finding a provider",
                "every new job",
                "Traditional: ask around, search groups, try saved numbers. Panun Kaergar: one request, matched partner.",
            ),
            (
                "Trust and verification",
                "letting someone in",
                "Traditional: word of mouth only. Panun Kaergar: identity and trade checks plus visible ratings.",
            ),
            (
                "Pricing clarity",
                "before and after the job",
                "Traditional: often discussed only on arrival. Panun Kaergar: estimate or rate guidance upfront.",
            ),
            (
                "Booking channels",
                "convenience",
                "Traditional: usually one phone call. Panun Kaergar: phone, WhatsApp, website, and app.",
            ),
            (
                "When things go wrong",
                "accountability",
                "Traditional: resolve alone with the worker. Panun Kaergar: support team investigates and helps resolve.",
            ),
        ],
        "I still get local workers — but now there is someone to call if they do not show.",
        "Feroz, Batamaloo",
        "Kashmir's skilled trades are a strength. Panun Kaergar's role is to make that strength reachable for every household — especially for small jobs that contacts often ignore.",
        "A platform does not guarantee perfection on every visit. It guarantees a process, a record, and someone to call — which traditional booking often lacks.",
        "Try Panun Kaergar for your next home service — especially a small repair your usual contacts have been ignoring.",
        [
            ("Is Panun Kaergar better than calling a local technician?", "It adds verification, pricing guidance, booking records, and support — while still using local partners."),
            ("Does Panun Kaergar replace local workers?", "No. It connects local skilled partners with customers who need them."),
            ("What is the main advantage?", "Accountability — someone to call when the job does not go as planned."),
            ("Is it only for people without contacts?", "No. Many customers use it for convenience, small jobs, and backup even when they have contacts."),
        ],
        comparison_rows=[
            ("Finding a provider", "Ask neighbours, search groups, call saved numbers", "One request; Panun Kaergar matches a verified partner"),
            ("Trust", "Word of mouth only", "Identity checks, trade review, and customer ratings"),
            ("Pricing", "Often agreed only on arrival", "Estimate or rate guidance before the visit"),
            ("Booking", "Usually one phone call", "Phone, WhatsApp, website form, and mobile app"),
            ("Problems", "Resolve directly with the worker", "Panun Kaergar support investigates and helps resolve"),
            ("Small jobs", "Often ignored or deprioritised", "Same booking path as larger work"),
            ("Record", "No central history", "App and platform keep booking records"),
        ],
        comparison_intro="This table compares the experience of booking home services the traditional way in Kashmir versus through Panun Kaergar. No competitor names — just what changes for you as a customer.",
        related_service="painting",
        seo_desc="Panun Kaergar vs traditional local booking in Kashmir — verified partners, transparent pricing, multiple booking channels, support for complaints, and a record of every request.",
    ),
]


GUIDES: list[dict] = []
for index, spec in enumerate(_SPECS, 1):
    guide = dict(spec)
    if guide["slug"] == "why-choose-panun-kaergar-kashmir":
        guide["sortOrder"] = 50
        guide["hero_prompt_overrides"] = WHY_CHOOSE_HERO_PROMPTS
        guide["image_prompt_overrides"] = WHY_CHOOSE_IMAGE_PROMPTS
        guide["heroSub"] = (
            "Verified partners, upfront pricing, and one booking path for every job size in Kashmir."
        )
        guide["excerpt"] = (
            "Big renovations get quotes fast — small repairs often wait weeks. "
            "Panun Kaergar gives both the same attention."
        )
    else:
        guide["sortOrder"] = 40 + index
    siblings = [s for s in _ALL_SLUGS if s != guide["slug"]]
    guide["relatedGuideSlugs"] = siblings[:4]
    guide["articleHtml"] = _platform_article(guide)
    GUIDES.append(guide)

TITLE_SUBJECTS = {
    "why-choose-panun-kaergar-kashmir": "why choose Panun Kaergar for home and commercial services small to large jobs Kashmir",
    "home-services-panun-kaergar-handles-kashmir": "Kashmir home services from small tap repair to large renovation project",
    "verified-home-service-partners-kashmir": "verified home service partner ID check and onboarding",
    "transparent-pricing-home-services-kashmir": "transparent home service pricing estimate before work",
    "home-service-quality-standards-panun-kaergar": "home service quality standards checklist for partner visit",
    "how-to-book-home-services-panun-kaergar-kashmir": "booking home services by phone WhatsApp app and website",
    "panun-kaergar-customer-support-kashmir": "customer support team helping with home service booking issue",
    "panun-kaergar-vs-traditional-booking-kashmir": "comparison traditional local booking vs structured home service platform",
}
