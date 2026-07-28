#!/usr/bin/env python3
"""Remove specific locality/neighbourhood names from guide content."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "panun-marketing" / "content" / "guides"
SCRIPTS = ROOT / "panun-marketing" / "scripts"

# Neighbourhoods, districts, and named areas — not the word "Kashmir" alone.
LOCALITIES = [
    "Downtown Srinagar",
    "Jawahar Nagar",
    "Lal Chowk",
    "Habba Kadal",
    "Rainawari",
    "Batamaloo",
    "Hyderpora",
    "Srinagar",
    "Zakura",
    "Bemina",
    "Rajbagh",
    "Anantnag",
    "Pampore",
    "Budgam",
    "Baramulla",
    "Sopore",
    "Hazratbal",
    "Nishat",
    "Pulwama",
    "Ganderbal",
    "Downtown",
]

LOCALITY_RE = re.compile(
    r"\b(" + "|".join(re.escape(x) for x in sorted(LOCALITIES, key=len, reverse=True)) + r")\b"
)

PHRASE_FIXES = [
    (r"\bin a Bemina flat\b", "in a flat"),
    (r"\bin an Anantnag kitchen\b", "in the kitchen"),
    (r"\bin an old Lal Chowk flat\b", "in an older flat"),
    (r"\bin a rented Lal Chowk flat\b", "in a rented flat"),
    (r"\bin a Pulwama house\b", "in a house"),
    (r"\bin a Hyderpora flat\b", "in a flat"),
    (r"\bin a Rainawari home\b", "at home"),
    (r"\bin a Srinagar apartment\b", "in an apartment"),
    (r"\bin Ganderbal\b", "at home"),
    (r"\bin Anantnag\b", ""),
    (r"\bin Budgam\b", ""),
    (r"\bin Pampore\b", ""),
    (r"\bin Sopore\b", ""),
    (r"\bin Hazratbal\b", ""),
    (r"\bin Baramulla\b", ""),
    (r"\bground-floor Baramulla room\b", "ground-floor room"),
    (r"\bSopore bedroom\b", "bedroom"),
    (r"\bHazratbal bedroom\b", "bedroom"),
    (r"\bBatamaloo showerhead\b", "showerhead"),
    (r"\ba Zakura bathroom\b", "a guest bathroom"),
    (r"\bOn a cold Srinagar morning\b", "On a cold winter morning"),
    (r"\bIn a top-floor Srinagar room\b", "In a top-floor room"),
    (r"\bIn a rain-swollen old Srinagar house\b", "In a rain-swollen old house"),
    (r"\bIn a quiet Srinagar garden\b", "In a quiet garden"),
    (r"\bA proud Srinagar balcony garden\b", "A proud balcony garden"),
    (r"\bA Srinagar driveway\b", "A driveway"),
    (r"\bA family leaves Srinagar in afternoon traffic\b", "A family sits in afternoon traffic"),
    (r"\bOn a humid July afternoon in Pampore,\s*", "On a humid July afternoon, "),
    (r"\bAfter a cap-heavy week in Srinagar,\s*", "After a cap-heavy week, "),
    (r"\bin a Jawahar Nagar living room\b", "in the living room"),
    (r"\bon a Habba Kadal bedroom wall\b", "on a bedroom wall"),
    (r"\bin downtown Srinagar\b", "at home"),
    (r"\bthe living-room sofa in Hyderpora\b", "the living-room sofa"),
    (r"\bends of a woman's hair in Rajbagh feel\b", "ends of a woman's hair feel"),
    (r"\bBefore a family function in Budgam,\s*", "Before a family function, "),
    (r"\bThe balcony door in a Rajbagh flat\b", "The balcony door in a flat"),
    (r"\bA mirrored wardrobe in a Bemina bedroom\b", "A mirrored wardrobe in a bedroom"),
    (r"\bA window in a Hyderpora flat\b", "A window in a flat"),
    (r"\bA tea-coloured ring appears over the dining table in a Rainawari home\b",
     "A tea-coloured ring appears over the dining table"),
    (r"\bA young man in Anantnag stares\b", "A young man stares"),
    (r"\bA long-haired cat in Ganderbal develops\b", "A long-haired cat develops"),
    (r"\bAt 11:40 pm in an Anantnag kitchen\b", "At 11:40 pm, the kitchen"),
    (r" ,", ","),
    (r"[ \t]+\.", "."),
]


def clean(text: str) -> str:
    for pattern, repl in PHRASE_FIXES:
        text = re.sub(pattern, repl, text)
    # Review cites: — Name, Place → — Name
    text = re.sub(
        r"(<cite>—\s*[^,<]+),\s*[^<]+(</cite>)",
        r"\1\2",
        text,
    )
    # Remaining stray "in Locality" / "at Locality" fragments
    text = re.sub(r"\b(in|at|from|near)\s+" + LOCALITY_RE.pattern + r"\b", r"\1 ", text)
    text = re.sub(r"\b" + LOCALITY_RE.pattern + r"\s+(flat|home|house|room|garden|driveway|bedroom|kitchen|apartment)\b", r"\1", text)
    text = LOCALITY_RE.sub("", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r" \n", "\n", text)
    return text


def assert_no_localities(text: str, context: str = "") -> None:
    """Raise ValueError if guide copy contains banned locality names."""
    if LOCALITY_RE.search(text):
        match = LOCALITY_RE.search(text)
        raise ValueError(f"Banned locality {match.group(0)!r} in {context or 'text'}")


def validate_guides() -> list[str]:
    """Return list of guide files that still contain locality names."""
    bad = []
    for path in GUIDES.rglob("*"):
        if path.suffix not in {".html", ".yaml", ".mdoc"}:
            continue
        text = path.read_text(encoding="utf-8")
        if LOCALITY_RE.search(text):
            bad.append(str(path.relative_to(ROOT)))
    return bad


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = clean(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main():
    bad = validate_guides()
    if bad:
        print("Locality names still present:")
        for p in bad:
            print(f"  {p}")
        raise SystemExit(1)
    changed = []
    for path in GUIDES.rglob("*"):
        if path.suffix not in {".html", ".yaml", ".mdoc"}:
            continue
        if process_file(path):
            changed.append(path.relative_to(ROOT))
    print(f"Updated {len(changed)} files")
    for p in changed:
        print(f"  {p}")


if __name__ == "__main__":
    main()
