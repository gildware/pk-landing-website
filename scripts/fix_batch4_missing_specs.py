from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "scripts" / "batch4_guide_content.py"
text = path.read_text(encoding="utf-8")
src = subprocess.check_output(
    ["git", "show", "HEAD:scripts/batch4_guide_content.py"],
    cwd=ROOT,
    text=True,
    encoding="utf-8",
)


def extract_spec(slug: str) -> str:
    marker = f'"{slug}"'
    idx = src.find(marker)
    if idx == -1:
        raise SystemExit(f"Could not find {slug} in git source")
    start = src.rfind("    _spec(", 0, idx)
    end = src.find("\n    _spec(", idx)
    if end == -1:
        end = src.find("\n]\n\n\nGUIDES", idx)
    block = src[start:end].rstrip()
    if not block.endswith(","):
        block += ","
    return block


def clean_localities(block: str) -> str:
    replacements = [
        ("A shop owner in Srinagar gets", "A shop owner gets"),
        ("Our Srinagar-based support team", "Our support team"),
        ("Nighat, Rajbagh", "Nighat"),
        ("Srinagar and multiple districts across Kashmir. Mention your neighbourhood when booking.", "Across Kashmir. Mention your area when booking."),
        ("across Srinagar and Kashmir so partners", "across Kashmir so partners"),
        ("across Srinagar and districts in Kashmir.", "across Kashmir."),
        ("Is Panun Kaergar only for Srinagar?", "Where does Panun Kaergar operate?"),
        ("Panun Kaergar serves Srinagar and multiple districts across Kashmir.", "Panun Kaergar serves households across Kashmir."),
        ("Sajad, Bemina", "Sajad"),
    ]
    for old, new in replacements:
        block = block.replace(old, new)
    return block


home_spec = clean_localities(extract_spec("home-services-panun-kaergar-handles-kashmir"))
verified_spec = clean_localities(extract_spec("verified-home-service-partners-kashmir"))

home_spec = home_spec.replace(
    '"What home services does Panun Kaergar handle in Kashmir? From small repairs to full projects"',
    '"What jobs can you book through Panun Kaergar in Kashmir?"',
).replace(
    'seo_desc="Panun Kaergar handles every home service in Kashmir — small tap repairs, installs, cleaning, salon, appliances, and large renovation projects. Book verified local partners for jobs others ignore.",',
    'seo_desc="What jobs can you book through Panun Kaergar in Kashmir? From plumbing and electrical work to cleaning, salon, appliances, pest control, and larger projects.",',
)

verified_spec = verified_spec.replace(
    '"How does Panun Kaergar verify home service partners in Kashmir?"',
    '"How Panun Kaergar verifies home service partners before they visit"',
).replace(
    'seo_desc="How Panun Kaergar verifies home service partners in Kashmir — identity checks, trade review, onboarding, ratings, and ongoing quality monitoring before they enter your home.",',
    'seo_desc="How Panun Kaergar verifies home service partners before they visit — ID checks, trade review, onboarding, ratings, and complaint monitoring.",',
)

if '"home-services-panun-kaergar-handles-kashmir"' not in text:
    text = text.replace(
        '    "why-choose-panun-kaergar-kashmir",\n'
        '    "transparent-pricing-home-services-kashmir",',
        '    "why-choose-panun-kaergar-kashmir",\n'
        '    "home-services-panun-kaergar-handles-kashmir",\n'
        '    "verified-home-service-partners-kashmir",\n'
        '    "transparent-pricing-home-services-kashmir",',
    )

if 'PK-G01' not in text:
    insert_marker = '    _spec(\n        "PK-G03",\n        "transparent-pricing-home-services-kashmir",'
    text = text.replace(insert_marker, home_spec + "\n" + verified_spec + "\n" + insert_marker)

if '"home-services-panun-kaergar-handles-kashmir":' not in text.split("TITLE_SUBJECTS", 1)[1]:
    text = text.replace(
        '    "why-choose-panun-kaergar-kashmir": "why choose Panun Kaergar for home and commercial services small to large jobs Kashmir",\n'
        '    "transparent-pricing-home-services-kashmir": "transparent home service pricing estimate before work",',
        '    "why-choose-panun-kaergar-kashmir": "why choose Panun Kaergar for home and commercial services small to large jobs Kashmir",\n'
        '    "home-services-panun-kaergar-handles-kashmir": "Kashmir home services from small tap repair to large renovation project",\n'
        '    "verified-home-service-partners-kashmir": "verified home service partner ID check and onboarding",\n'
        '    "transparent-pricing-home-services-kashmir": "transparent home service pricing estimate before work",',
    )

path.write_text(text, encoding="utf-8")
print("Restored missing batch4 specs")
