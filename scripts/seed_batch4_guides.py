#!/usr/bin/env python3
"""Seed Batch 4 platform/trust guides into content/guides + public/images/guides."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from batch4_guide_content import GUIDES, TITLE_SUBJECTS
from guide_image_utils import (
    PROMPT_STYLE,
    apply_brand_to_guide,
    collect_image_jobs,
    write_prompts_file,
)
from seed_batch1_guides import yq

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "guides"
IMG = ROOT / "public" / "images" / "guides"
BATCH4_ASSETS = ROOT / "blog-batch-4" / "assets"
GENERATED = BATCH4_ASSETS / "generated"
PROMPTS_DIR = BATCH4_ASSETS / "prompts"
PUBLISHED_AT = "2026-08-03"

NO_LOGO = (
    " CRITICAL: No logos, watermarks, brand marks, gear-logo icons, letter monograms, "
    "company names, or PANUN text anywhere in the artwork — illustration content only."
)

HERO_PROMPT_TEMPLATES = {
    "cover": "Hero cover for Kashmir home-services guide about {subject}. Calm trustworthy mood.",
    "title": "Square title card icon for Kashmir home-services guide about {subject}. Professional calm mood.",
    "methods": "Infographic showing 5 numbered points for {subject}. Simple icons connected by gold arrows.",
    "diagram": "Flow diagram for {subject}: customer request to verified partner completion.",
    "tip": "Practical tip scene for {subject}, calm professional mood.",
}


def hero_prompts(slug: str, guide: dict | None = None) -> dict[str, str]:
    if guide and guide.get("hero_prompt_overrides"):
        return guide["hero_prompt_overrides"]
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
        "hero": hero_prompts(slug, g),
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

    related = "\n".join(f"  - {r}" for r in g.get("relatedGuideSlugs", []))
    trending = "true" if g.get("isTrending") else "false"
    related_service = g.get("relatedServiceSlug", "")
    related_service_line = f"relatedServiceSlug: {related_service}\n" if related_service else ""
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
{related_service_line}relatedGuideSlugs:
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
    """Copy PNG/WebP from blog-batch-4/assets/generated/{slug}/ into public guide images."""
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

    if not use_generated or not (GENERATED / slug).exists() or not any((GENERATED / slug).iterdir()):
        print(
            f"SKIP images for {slug}: place AI-generated PNGs in "
            f"blog-batch-4/assets/generated/{slug}/ then re-run seed."
        )
        return

    # Remove stale pre-brand backups so old placeholder art is not re-applied.
    guide_backup = BATCH4_ASSETS / "pre-brand-backup" / slug
    if guide_backup.exists():
        try:
            shutil.rmtree(guide_backup)
        except OSError:
            print(f"WARN: could not remove stale backup {guide_backup} — delete manually if images look wrong.")

    import_generated_images(slug)


def seed_one(slug: str, *, content_only: bool = False, skip_brand: bool = False) -> None:
    guide = next((g for g in GUIDES if g["slug"] == slug), None)
    if not guide:
        raise SystemExit(f"Unknown Batch 4 slug: {slug}")

    write_guide(guide)
    manifest = write_image_manifest(guide)
    write_prompts_file(guide, TITLE_SUBJECTS.get(slug))
    print(f"Wrote content -> content/guides/{slug}/")
    print(f"Wrote manifest -> {manifest}")

    if not content_only:
        prepare_images(guide, use_generated=(GENERATED / slug).exists())
        if not skip_brand:
            n = apply_brand_to_guide(slug, IMG, backup_dir=BATCH4_ASSETS / "pre-brand-backup")
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
