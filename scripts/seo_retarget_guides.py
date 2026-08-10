from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDES_DIR = ROOT / "content" / "guides"


def truncate_desc(text: str, max_len: int = 158) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rstrip()
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut + "…"


SERVICE_HINTS = {
    "plumbing": "a plumber",
    "electrician": "an electrician",
    "home-appliances": "appliance repair",
    "pest-control": "pest control",
    "professional-cleaning": "a cleaning professional",
    "dry-clean-laundry": "professional cleaning",
    "carpentry": "a carpenter",
    "aluminium-steel-works": "an aluminium professional",
    "gardening": "a gardener",
    "mens-salon": "a barber or grooming professional",
    "womens-salon": "a salon professional",
    "dog-grooming": "a pet grooming professional",
    "vehicle-care": "vehicle care",
    "painting": "a painter",
    "masonry": "a mason",
    "interior-decor": "an interior repair professional",
}


MANUAL_META = {
    "sofa-dry-cleaning-vs-home-clean": (
        "Not every sofa needs dry cleaning. Use this Kashmir guide to decide between home spot-cleaning, upholstery extraction, and professional dry cleaning."
    ),
    "sofa-smells-stains-cleaning": (
        "Tea spill, stale odour, or an old mark on the sofa? Learn how to clean upholstery safely in Kashmir without setting stains deeper."
    ),
    "aluminium-door-not-sliding-smoothly": (
        "Aluminium door dragging or sticking? Clean the track, clear weep holes, and know when the rollers need professional adjustment."
    ),
    "aluminium-sliding-window-problems": (
        "Sliding window stuck or leaking? Check the track, rollers, and drain holes before forcing the frame or booking replacement."
    ),
    "wall-cracks-cosmetic-structural": (
        "Are wall cracks cosmetic or serious? Learn which crack patterns need monitoring, plaster repair, or urgent structural advice in Kashmir."
    ),
    "wall-seepage-plaster-damage-kashmir": (
        "Damp patch or bubbling plaster in Kashmir? Trace seepage to plumbing, rain entry, "
        "or rising damp before repairing the wall — then book the right fix."
    ),
    "painting-damp-walls-kashmir": (
        "Painting a damp wall never lasts. Find the moisture source, dry the surface properly, and know when to call a painter or mason."
    ),
    "paint-peeling-kashmir-homes": (
        "Paint peeling in a Kashmir home usually points to damp, poor prep, or primer failure. "
        "Fix the cause before repainting, and know when to book a painter."
    ),
    "car-battery-dead-cold-morning": (
        "Car battery dead on a cold Kashmir morning? Learn when a jump-start is safe, "
        "when terminals need cleaning, and when to book a battery replacement."
    ),
    "lawn-looking-dead-kashmir": (
        "Lawn looking dead after a Kashmir winter? Check if grass is dormant, rake gently, "
        "water only when soil needs it, and know when to book a gardener."
    ),
    "matted-fur-dog-cat": (
        "Matted fur on a dog or cat? Loosen mats safely without cutting blind spots, "
        "protect the skin, and know when professional pet grooming is safer."
    ),
    "uneven-beard-growth-shape": (
        "Uneven beard growth in Kashmir? Work with your natural pattern, shape carefully "
        "with good light, and know when a barber visit helps more than home trimming."
    ),
    "ac-not-cooling-kashmir": (
        "AC running but not cooling? Check mode, filters, airflow, and the outdoor unit safely before booking appliance repair in Kashmir."
    ),
    "ac-leaking-water-kashmir": (
        "AC leaking water indoors? Check the drain, filters, and indoor-unit slope safely before booking appliance repair in Kashmir."
    ),
    "car-ac-not-cooling": (
        "Car AC not cooling? Check recirculation, airflow, and condenser clearance before paying for a gas refill or leak diagnosis."
    ),
}


BATCH4_TEXT_REPLACEMENTS = {
    '"Why choose Panun Kaergar for home and commercial services in Kashmir?"':
        '"Why Panun Kaergar works for small repairs and large projects in Kashmir"',
    '"What home services does Panun Kaergar handle in Kashmir? From small repairs to full projects"':
        '"What jobs can you book through Panun Kaergar in Kashmir?"',
    '"How does Panun Kaergar verify home service partners in Kashmir?"':
        '"How Panun Kaergar verifies home service partners before they visit"',
    '"Are Panun Kaergar home service prices transparent? What to expect before you pay"':
        '"How Panun Kaergar handles pricing before work starts"',
    '"What quality standards does Panun Kaergar expect from every home service visit?"':
        '"What standards should you expect from a Panun Kaergar home service visit?"',
    '"How to book home services through Panun Kaergar in Kashmir"':
        '"How to book a Panun Kaergar home service in Kashmir"',
    '"Panun Kaergar customer support: who helps when a home service goes wrong?"':
        '"What happens if a Panun Kaergar home service goes wrong?"',
    '"Panun Kaergar vs traditional local booking: what actually changes for customers?"':
        '"Panun Kaergar vs calling a local technician: what changes for customers?"',
    '"Panun Kaergar verified providers: trained, qualified professionals for your home"':
        '"Are Panun Kaergar providers trained and experienced? What verified means"',
    'seo_desc="Why choose Panun Kaergar for home and commercial services in Kashmir? Verified partners, transparent pricing, and booking for every job size — from small tap repairs to full renovation projects.",':
        'seo_desc="Why Panun Kaergar works for small repairs and large projects in Kashmir — verified partners, structured booking, and support across job sizes.",',
    'seo_desc="Panun Kaergar handles every home service in Kashmir — small tap repairs, installs, cleaning, salon, appliances, and large renovation projects. Book verified local partners for jobs others ignore.",':
        'seo_desc="What jobs can you book through Panun Kaergar in Kashmir? From plumbing and electrical work to cleaning, salon, appliances, pest control, and larger projects.",',
    'seo_desc="How Panun Kaergar verifies home service partners in Kashmir — identity checks, trade review, onboarding, ratings, and ongoing quality monitoring before they enter your home.",':
        'seo_desc="How Panun Kaergar verifies home service partners before they visit — ID checks, trade review, onboarding, ratings, and complaint monitoring.",',
    'seo_desc="Transparent home service pricing in Kashmir — estimates before work, no hidden booking fees, clear material costs, and support if your bill does not match what was agreed.",':
        'seo_desc="How Panun Kaergar handles pricing before work starts — estimates, material-cost explanations, booking records, and billing support when charges do not match.",',
    'seo_desc="Panun Kaergar quality standards for every home service visit — prepared arrival, punctuality, home care, honest advice, and customer ratings that keep partners accountable.",':
        'seo_desc="What standards should you expect from a Panun Kaergar visit? Prepared arrival, punctuality, home care, honest advice, cleanup, and ratings-backed accountability.",',
    'seo_desc="How to book home services in Kashmir through Panun Kaergar — by phone, WhatsApp, website form, or free app. One path for every service from small repairs to large projects.",':
        'seo_desc="How to book a Panun Kaergar home service in Kashmir — by phone, WhatsApp, website form, or app, with one booking path for small repairs and larger jobs.",',
    'seo_desc="Panun Kaergar customer support in Kashmir — phone, WhatsApp, and email help for reschedules, billing questions, no-shows, and complaints when a home service does not go as planned.",':
        'seo_desc="What happens if a Panun Kaergar home service goes wrong? Support helps with reschedules, billing questions, no-shows, and complaints.",',
    'seo_desc="Panun Kaergar vs traditional local booking in Kashmir — verified partners, transparent pricing, multiple booking channels, support for complaints, and a record of every request.",':
        'seo_desc="Panun Kaergar vs calling a local technician in Kashmir — what changes in verification, pricing clarity, booking records, and support if a job goes wrong.",',
    'seo_desc=(\n            "Panun Kaergar verified providers in Kashmir are trained, qualified, experienced local professionals — "\n            "identity-checked, trade-reviewed, onboarded on quality standards, and rated after every visit."\n        ),':
        'seo_desc=("Are Panun Kaergar providers trained and experienced? Learn what \'verified\' means, from trade review and onboarding to ratings after each visit."),',
}


def parse_yaml_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    data: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if ": |-" in line:
            key = line.split(":", 1)[0].strip()
            i += 1
            vals = []
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].strip() == ""):
                vals.append(lines[i][2:] if lines[i].startswith("  ") else "")
                i += 1
            data[key] = " ".join(v.strip() for v in vals).strip()
            continue
        if ":" in line and not line.startswith("  - "):
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip().strip("'").strip('"')
        i += 1
    return data


def replace_block(text: str, key: str, new_value: str) -> str:
    pattern = re.compile(rf"(?m)^({re.escape(key)}:\s*\|-\n)(?:^  .*?\n)+")
    replacement = f"{key}: |-\n  {new_value}\n"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)

    single_pattern = re.compile(rf"(?m)^{re.escape(key)}:.*$")
    if single_pattern.search(text):
        return single_pattern.sub(replacement.rstrip("\n"), text, count=1)

    raise ValueError(f"Could not replace field {key} in text")


def update_batch1_source() -> None:
    path = ROOT / "scripts" / "batch1_guide_content.py"
    text = path.read_text(encoding="utf-8")
    if "_seo_from_compact(" not in text:
        helper = """
def _seo_from_compact(title: str, service: str, first_move: str) -> str:
    service_label = SERVICE_HINTS.get(service, "professional help")
    lead = title.strip().rstrip("?")
    step = first_move.split(".")[0].strip()
    return (
        f"{lead} in Kashmir? {step}. Learn the safest first checks, the usual causes, "
        f"and when to book {service_label}."
    )


"""
        anchor = "def _compact(\n"
        text = text.replace(anchor, helper + anchor, 1)
    text = text.replace(
        '        seoDescription=f"Practical Kashmir guide: diagnose {subject}, try safe first steps, and know when to book a verified professional.",',
        '        seoDescription=_seo_from_compact(title, service, method_rows[0][2]),',
    )
    if "SERVICE_HINTS = {" not in text:
        service_map = """
SERVICE_HINTS = {
    "plumbing": "a plumber",
    "electrician": "an electrician",
    "home-appliances": "appliance repair",
    "pest-control": "pest control",
    "professional-cleaning": "a cleaning professional",
    "dry-clean-laundry": "professional cleaning",
    "carpentry": "a carpenter",
    "aluminium-steel-works": "an aluminium professional",
    "gardening": "a gardener",
    "mens-salon": "a barber or grooming professional",
    "womens-salon": "a salon professional",
    "dog-grooming": "a pet grooming professional",
    "vehicle-care": "vehicle care",
    "painting": "a painter",
    "masonry": "a mason",
    "interior-decor": "an interior repair professional",
}


"""
        text = text.replace('GUIDES = [\n', service_map + 'GUIDES = [\n', 1)
    path.write_text(text, encoding="utf-8")


def update_batch4_source() -> None:
    path = ROOT / "scripts" / "batch4_guide_content.py"
    text = path.read_text(encoding="utf-8")
    for old, new in BATCH4_TEXT_REPLACEMENTS.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def generated_meta(slug: str, data: dict[str, str]) -> str:
    if slug in MANUAL_META:
        return truncate_desc(MANUAL_META[slug])

    headline = data.get("headline", "").strip().rstrip("?")
    service = data.get("relatedServiceSlug", "")
    service_label = SERVICE_HINTS.get(service, "professional help")
    excerpt = data.get("excerpt", "")
    first = excerpt.split(".")[0].strip()
    # Avoid "Headline in Kashmir? Scene…" — that reads as a broken template in SERPs.
    if first and len(first) > 40 and not first.lower().startswith(headline.lower()[:24]):
        desc = f"{first}. Practical Kashmir guide — safe first checks and when to book {service_label}."
    else:
        desc = (
            f"{headline} in Kashmir. Practical first checks, usual causes, "
            f"and when to book {service_label}."
        )
    return truncate_desc(desc)


def update_current_guide_metadata() -> list[str]:
    changed: list[str] = []
    platform_overrides = {
        "why-choose-panun-kaergar-kashmir": {
            "headline": "Why Panun Kaergar works for small repairs and large projects in Kashmir",
            "seoTitle": "Why Panun Kaergar for every job size | Panun Kaergar",
            "seoDescription": (
                "Why Panun Kaergar works for small repairs and large projects in Kashmir — "
                "verified partners, structured booking, and support across job sizes."
            ),
        },
        "what-jobs-can-you-book-panun-kaergar-kashmir": {
            "headline": "What jobs can you book through Panun Kaergar in Kashmir?",
            "seoTitle": "Jobs you can book through Panun Kaergar | Panun Kaergar",
            "seoDescription": (
                "Book plumbing, electrical, cleaning, salon, appliances, pest control, painting, "
                "carpentry, and renovation jobs through Panun Kaergar in Kashmir."
            ),
        },
        "verified-home-service-partners-kashmir": {
            "headline": "How Panun Kaergar verifies home service partners before they visit",
            "seoTitle": "How Panun Kaergar verifies service partners | Panun Kaergar",
            "seoDescription": (
                "How Panun Kaergar verifies home service partners before they visit — "
                "ID checks, trade review, onboarding, ratings, and complaint monitoring."
            ),
        },
        "transparent-pricing-home-services-kashmir": {
            "headline": "How Panun Kaergar handles pricing before work starts",
            "seoTitle": "Transparent pricing before work starts | Panun Kaergar",
            "seoDescription": (
                "How Panun Kaergar handles pricing before work starts — estimates, material-cost "
                "explanations, booking records, and billing support when charges do not match."
            ),
        },
        "home-service-quality-standards-panun-kaergar": {
            "headline": "What standards should you expect from a Panun Kaergar home service visit?",
            "seoTitle": "What to expect on every Panun Kaergar visit | Panun Kaergar",
            "seoDescription": (
                "What to expect on a Panun Kaergar visit: prepared arrival, punctuality, home care, "
                "honest advice, cleanup, and ratings-backed accountability."
            ),
        },
        "how-to-book-home-services-panun-kaergar-kashmir": {
            "headline": "How to book a Panun Kaergar home service in Kashmir",
            "seoTitle": "How to book a Panun Kaergar home service | Panun Kaergar",
            "seoDescription": (
                "How to book a Panun Kaergar home service in Kashmir — by phone, WhatsApp, website "
                "form, or app, with one booking path for small repairs and larger jobs."
            ),
        },
        "panun-kaergar-customer-support-kashmir": {
            "headline": "What happens if a Panun Kaergar home service goes wrong?",
            "seoTitle": "If a Panun Kaergar home service goes wrong | Panun Kaergar",
            "seoDescription": (
                "What happens if a Panun Kaergar home service goes wrong? Support helps with "
                "reschedules, billing questions, no-shows, and complaints."
            ),
        },
        "panun-kaergar-vs-traditional-booking-kashmir": {
            "headline": "Panun Kaergar vs calling a local technician: what changes for customers?",
            "seoTitle": "Panun Kaergar vs calling a local technician | Panun Kaergar",
            "seoDescription": (
                "Panun Kaergar vs calling a local technician in Kashmir — what changes in "
                "verification, pricing clarity, booking records, and support if a job goes wrong."
            ),
        },
        "panun-kaergar-verified-providers-kashmir": {
            "headline": "Are Panun Kaergar providers trained and experienced? What verified means",
            "seoTitle": "Are Panun Kaergar providers trained? | Panun Kaergar",
            "seoDescription": (
                "Are Panun Kaergar providers trained and experienced? Learn what verified means, "
                "from trade review and onboarding to ratings after each visit."
            ),
        },
    }

    for path in sorted(GUIDES_DIR.glob("*/index.yaml")):
        text = path.read_text(encoding="utf-8")
        data = parse_yaml_frontmatter(path)
        slug = path.parent.name
        original = text

        if slug in platform_overrides:
            for key, value in platform_overrides[slug].items():
                text = replace_block(text, key, value)
        else:
            seo_desc = data.get("seoDescription", "")
            if seo_desc.startswith("Practical Kashmir guide: diagnose") or slug in MANUAL_META:
                text = replace_block(text, "seoDescription", generated_meta(slug, data))

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(slug)
    return changed


def main() -> None:
    update_batch1_source()
    update_batch4_source()
    changed = update_current_guide_metadata()
    print(f"Updated {len(changed)} guide metadata files")
    for slug in changed:
        print(slug)


if __name__ == "__main__":
    main()
