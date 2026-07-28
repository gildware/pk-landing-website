#!/usr/bin/env python3
"""Build deploy + brand commands for guide image regeneration."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from batch2_guide_content import GUIDES, TITLE_SUBJECTS
from guide_image_utils import PROMPT_STYLE, apply_brand_to_guide, collect_image_jobs

ASSETS = Path("/Users/kamran/.cursor/projects/Users-kamran-Desktop-panun-kaergar/assets")
PUBLIC = Path(__file__).resolve().parents[1] / "public" / "images" / "guides"
BACKUP = Path(__file__).resolve().parents[2] / "blog-batch-2" / "assets"

NO_LOGO = (
    " CRITICAL: No logos, watermarks, brand marks, gear-logo icons, letter P or K monograms, "
    "company names, or PANUN text anywhere in the artwork — illustration content only."
)

HERO_PROMPTS = {
    "cover": "Hero cover for Kashmir home guide about {subject}. Calm practical mood.",
    "title": "Square title card icon for Kashmir home guide about {subject}. Helpful calm mood.",
    "methods": "Method ladder infographic showing 5 numbered steps for {subject}. Simple icons connected by gold arrows.",
    "diagram": "Diagnosis flowchart for {subject}: symptoms branching to causes with first-check icons.",
    "tip": "Prevention tip scene for {subject}, calm practical mood.",
}


def hero_prompts(slug: str) -> dict[str, str]:
    subject = TITLE_SUBJECTS.get(slug, slug.replace("-", " "))
    out = {}
    for role, tmpl in HERO_PROMPTS.items():
        base = PROMPT_STYLE if role != "title" else PROMPT_STYLE.replace("16:9 landscape", "1:1 square")
        out[role] = base + tmpl.format(subject=subject) + NO_LOGO
    return out


def deploy_png(slug: str, role: str) -> None:
    src = ASSETS / f"{slug}-{role}.png"
    if not src.exists():
        raise FileNotFoundError(src)
    dst = PUBLIC / f"{slug}-{role}.webp"
    bak = BACKUP / f"{slug}-{role}.webp"
    q = 100 if role == "title" else 95
    subprocess.run(["cwebp", "-q", str(q), str(src), "-o", str(dst)], check=True)
    bak.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["cp", str(dst), str(bak)], check=True)


def main() -> None:
    slugs = sys.argv[1:] or [
        "flickering-lights-causes-kashmir",
        "aluminium-door-not-sliding-smoothly",
        "drain-smell-causes-kashmir",
    ]
    for slug in slugs:
        guide = next(g for g in GUIDES if g["slug"] == slug)
        jobs = collect_image_jobs(guide, TITLE_SUBJECTS.get(slug))
        manifest = {"slug": slug, "hero": hero_prompts(slug), "steps": jobs}
        out = ASSETS / f"{slug}-regen-manifest.json"
        out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"Wrote {out}")
        if len(sys.argv) > 1 and sys.argv[-1] == "--brand":
            n = apply_brand_to_guide(slug, PUBLIC)
            print(f"Branded {n} images for {slug}")


if __name__ == "__main__":
    main()
