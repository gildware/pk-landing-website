#!/usr/bin/env python3
"""Seed Batch 5 DIY guides into content/guides + public/images/guides."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from batch5_guide_content import GUIDES, TITLE_SUBJECTS
from guide_image_utils import (
    PROMPT_STYLE,
    apply_brand_to_guide,
    collect_image_jobs,
    prepare_step_images,
    write_prompts_file,
)
from seed_batch1_guides import draw_diagram, draw_methods_ladder, draw_simple_cover, draw_tip, yq

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "guides"
IMG = ROOT / "public" / "images" / "guides"
BATCH5_ASSETS = ROOT / "blog-batch-5" / "assets"
GENERATED = BATCH5_ASSETS / "generated"
PROMPTS_DIR = BATCH5_ASSETS / "prompts"
PUBLISHED_AT = "2026-08-14"

NO_LOGO = (
    " CRITICAL: No logos, watermarks, brand marks, gear-logo icons, letter monograms, "
    "company names, or PANUN text anywhere in the artwork — illustration content only."
)

HERO_PROMPT_TEMPLATES = {
    "cover": "Hero cover for Kashmir home guide about {subject}. Calm practical mood.",
    "title": "Square title card icon for Kashmir home guide about {subject}. Helpful calm mood.",
    "methods": "Method ladder infographic showing 5 numbered steps for {subject}. Simple icons connected by gold arrows.",
    "diagram": "Diagnosis flowchart for {subject}: symptoms branching to causes with first-check icons.",
    "tip": "Prevention tip scene for {subject}, calm practical mood.",
}


def hero_prompts(slug: str) -> dict[str, str]:
    subject = TITLE_SUBJECTS.get(slug, slug.replace("-", " "))
    out = {}
    for role, tmpl in HERO_PROMPT_TEMPLATES.items():
        base = PROMPT_STYLE if role != "title" else PROMPT_STYLE.replace("16:9 landscape", "1:1 square")
        out[role] = base + tmpl.format(subject=subject) + NO_LOGO
    return out


def write_image_manifest(g: dict) -> Path:
    slug = g["slug"]
    subject = TITLE_SUBJECTS.get(slug, slug.replace("-", " "))
    jobs = collect_image_jobs(g, subject)
    payload = {
        "slug": slug,
        "title": g.get("title", ""),
        "category": g.get("category", ""),
        "hero": hero_prompts(slug),
        "steps": jobs,
    }
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    path = PROMPTS_DIR / f"{slug}-manifest.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def write_guide(g: dict) -> None:
    slug = g["slug"]
    folder = CONTENT / slug
    folder.mkdir(parents=True, exist_ok=True)

    related = "\n".join(f"  - {r}" for r in g["relatedGuideSlugs"])
    trending = "true" if g.get("isTrending") else "false"
    yaml = f"""title: {slug}
headline: {yq(g['title'])}
excerpt: |-
  {g['excerpt']}
seoTitle: {yq(g['seoTitle'])}
seoDescription: |-
  {g['seoDescription']}
category: {yq(g['category'])}
publishedAt: {PUBLISHED_AT}
readingMinutes: {g['readingMinutes']}
isNew: true
isTrending: {trending}
heroSub: {yq(g['heroSub'])}
scene: |-
  {g['scene']}
quickAnswer: |-
  {g['quickAnswer']}
coverImage: {slug}-cover.webp
titleImage: {slug}-title.webp
relatedServiceSlug: {g['relatedServiceSlug']}
relatedGuideSlugs:
{related}
published: true
sortOrder: {g['sortOrder']}
"""
    (folder / "index.yaml").write_text(yaml, encoding="utf-8")
    (folder / "article.html").write_text(g["articleHtml"].strip() + "\n", encoding="utf-8")
    (folder / "body.mdoc").write_text(
        f"<!-- Fallback summary; live article is article.html -->\n\n{g['excerpt']}\n",
        encoding="utf-8",
    )


def import_generated_images(slug: str) -> int:
    from PIL import Image

    src_dir = GENERATED / slug
    if not src_dir.exists():
        raise FileNotFoundError(f"No generated assets at {src_dir}")

    IMG.mkdir(parents=True, exist_ok=True)
    count = 0
    for src in sorted(src_dir.iterdir()):
        if src.suffix.lower() not in {".png", ".webp", ".jpg", ".jpeg"}:
            continue
        if not src.name.startswith(slug):
            continue
        dst = IMG / f"{src.stem}.webp"
        img = Image.open(src).convert("RGB")
        if "title" in src.name:
            img = img.resize((900, 900), Image.Resampling.LANCZOS)
        elif img.width > 1600 or (img.width > img.height and img.width > 1200):
            ratio = 1200 / img.width
            img = img.resize((1200, max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)
        q = 100 if "title" in src.name else 95
        img.save(dst, "WEBP", quality=q, method=6)
        count += 1
    return count


def prepare_images(g: dict, *, use_generated: bool = True) -> None:
    slug = g["slug"]
    subject = TITLE_SUBJECTS.get(slug, slug.replace("-", " "))

    if use_generated and (GENERATED / slug).exists() and any((GENERATED / slug).iterdir()):
        import_generated_images(slug)
    else:
        from PIL import Image, ImageDraw

        from seed_batch1_guides import grain, leaf

        steps = [m[0] for m in g.get("methods", [])][:5] or [
            "Make it safe",
            "Check airflow",
            "Test the seal",
            "Clear space",
            "Book help",
        ]
        draw_methods_ladder(IMG / f"{slug}-methods.webp", steps)
        draw_diagram(
            IMG / f"{slug}-diagram.webp",
            "Diagnosis map",
            ["What you notice", "Likely cause", "First move"],
        )
        draw_tip(
            IMG / f"{slug}-tip.webp",
            "Leave breathing room",
            g.get("prevention_caption", "Keep vents clear and the door seal clean."),
        )
        draw_simple_cover(IMG / f"{slug}-cover.webp", subject)

        title_dst = IMG / f"{slug}-title.webp"
        img = Image.new("RGBA", (900, 900), (250, 248, 244, 255))
        d = ImageDraw.Draw(img)
        d.ellipse((300, 280, 600, 580), fill=(32, 32, 72, 255))
        d.ellipse((360, 340, 540, 520), fill=(255, 153, 0, 255))
        leaf(d, 60, 60, 1.5)
        leaf(d, 780, 70, 1.4, flip=True)
        grain(img).convert("RGB").save(title_dst, "WEBP", quality=88)
        prepare_step_images(g, IMG, subject)

    apply_brand_to_guide(slug, IMG, backup_dir=BATCH5_ASSETS / "pre-brand-backup")


def seed_one(slug: str, *, content_only: bool = False, skip_brand: bool = False) -> None:
    guide = next((g for g in GUIDES if g["slug"] == slug), None)
    if not guide:
        raise SystemExit(f"Unknown Batch 5 slug: {slug}")

    write_guide(guide)
    manifest = write_image_manifest(guide)
    write_prompts_file(guide, TITLE_SUBJECTS.get(slug))
    print(f"Wrote content -> content/guides/{slug}/")
    print(f"Wrote manifest -> {manifest}")

    if not content_only:
        prepare_images(guide, use_generated=(GENERATED / slug).exists())
        if not skip_brand:
            n = apply_brand_to_guide(slug, IMG, backup_dir=BATCH5_ASSETS / "pre-brand-backup")
            print(f"Branded {n} images")


def main() -> None:
    slugs = sys.argv[1:] or [g["slug"] for g in GUIDES]
    content_only = "--content-only" in slugs
    skip_brand = "--skip-brand" in slugs
    slugs = [s for s in slugs if not s.startswith("--")]

    for slug in slugs:
        seed_one(slug, content_only=content_only, skip_brand=skip_brand)
        print(f"OK {slug}")


if __name__ == "__main__":
    main()
