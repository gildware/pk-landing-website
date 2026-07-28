#!/usr/bin/env python3
"""Seed Batch 2 guides into panun-marketing (content + images)."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from PIL import Image, ImageDraw

from batch2_guide_content import GUIDES, TITLE_SUBJECTS
from seed_batch1_guides import (
    CONTENT,
    DEMO_ASSETS,
    IMG,
    MASTER,
    ROOT,
    TRACKER,
    draw_diagram,
    draw_methods_ladder,
    draw_simple_cover,
    draw_tip,
    font,
    grain,
    leaf,
    yq,
)
from guide_image_utils import find_guide_asset, is_rich_image, prepare_step_images, apply_brand_to_guide

BATCH_DIR = ROOT / "blog-batch-2"
PUBLISHED_AT = "2026-07-27"


def write_guide(g: dict):
    slug = g["slug"]
    folder = CONTENT / slug
    folder.mkdir(parents=True, exist_ok=True)

    related = "\n".join(f"  - {r}" for r in g["relatedGuideSlugs"])
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
isTrending: false
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


def prepare_images(g: dict):
    slug = g["slug"]
    subject = TITLE_SUBJECTS.get(slug, slug.replace("-", " "))

    for role, draw_fn, draw_args in (
        ("title", None, None),
        ("cover", draw_simple_cover, (subject,)),
        ("methods", draw_methods_ladder, ([m[0] for m in g.get("methods", [])][:6] or ["Make it safe", "Do the smallest test", "Note what changes", "Stop if risk rises", "Book the right trade"],)),
        ("diagram", draw_diagram, ("Diagnosis map", ["What you notice", "Likely cause", "First move"])),
        ("tip", draw_tip, ("Small habits win", g.get("prevention_caption", "A five-minute check done early usually beats an emergency visit later."))),
    ):
        dst = IMG / f"{slug}-{role}.webp"
        src = find_guide_asset(slug, role)
        if src and (not dst.exists() or not is_rich_image(dst) or is_rich_image(src)):
            shutil.copy2(src, dst)
            continue
        if role == "title" and not is_rich_image(dst):
            img = Image.new("RGBA", (900, 900), (250, 248, 244, 255))
            d = ImageDraw.Draw(img)
            d.ellipse((300, 280, 600, 580), fill=(32, 32, 72, 255))
            d.ellipse((360, 340, 540, 520), fill=(255, 153, 0, 255))
            leaf(d, 60, 60, 1.5)
            leaf(d, 780, 70, 1.4, flip=True)
            grain(img).convert("RGB").save(dst, "WEBP", quality=88)
        elif draw_fn and not is_rich_image(dst):
            if role == "cover":
                draw_fn(dst, draw_args[0])
            elif role == "methods":
                draw_fn(dst, draw_args[0])
            elif role == "diagram":
                draw_fn(dst, draw_args[0], draw_args[1])
            elif role == "tip":
                draw_fn(dst, draw_args[0], draw_args[1])

    prepare_step_images(g, IMG, subject)
    apply_brand_to_guide(slug, IMG)


def update_master_list():
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    by_id = {g["id"]: g for g in GUIDES}
    updated = 0
    for blog in data.get("blogs", []):
        g = by_id.get(blog.get("id"))
        if not g:
            continue
        blog["status"] = "in-marketing"
        blog["demoFile"] = ""
        blog["marketingPath"] = f"/guides/{g['slug']}"
        blog["marketingSlug"] = g["slug"]
        blog["batch"] = "batch-2"
        updated += 1
    meta = data.setdefault("meta", {})
    meta["updated"] = PUBLISHED_AT
    meta["marketingBlogStatus"] = "batch1_and_2_in_marketing"
    meta["marketingNote"] = (
        "Batch 1 (16) + Batch 2 (16) guides live under panun-marketing content/guides and /guides/[slug]."
    )
    if "batch2" not in meta:
        meta["batch2"] = {}
    meta["batch2"].update(
        {
            "status": "in_marketing",
            "count": len(GUIDES),
            "index": "blog-batch-2/index.html",
            "note": "Second common-problem guide per category.",
        }
    )
    MASTER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return updated


def refresh_tracker_embed():
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    html = TRACKER.read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    new_html, n = re.subn(
        r"const DATA = \{.*?\};",
        f"const DATA = {payload};",
        html,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit(f"Failed to refresh tracker DATA embed (replacements={n})")
    TRACKER.write_text(new_html, encoding="utf-8")


def rewrite_batch_index():
    BATCH_DIR.mkdir(exist_ok=True)
    links = "\n".join(
        f'    <li><a href="../panun-marketing/content/guides/{g["slug"]}/">{g["title"]}</a> → <code>/guides/{g["slug"]}</code></li>'
        for g in GUIDES
    )
    (BATCH_DIR / "README.md").write_text(
        f"""# Batch 2 — in panun-marketing

Second high-intent problem guide per category (16 total).

- Content: `panun-marketing/content/guides/`
- Images: `panun-marketing/public/images/guides/`
- Live routes: `/guides/[slug]` in the marketing site

## Guides

{chr(10).join(f'- `{g["slug"]}` ({g["id"]})' for g in GUIDES)}
""",
        encoding="utf-8",
    )
    (BATCH_DIR / "index.html").write_text(
        f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Batch 2 → panun-marketing</title>
<style>body{{font:16px/1.6 system-ui;max-width:720px;margin:40px auto;padding:0 20px;color:#202048}}
a{{color:#202048;font-weight:700}}</style></head>
<body>
<h1>Batch 2 is in panun-marketing</h1>
<p>Open the marketing site guides:</p>
<ul>
{links}
</ul>
<p><a href="../blog-tracker.html">Back to tracker</a> · <a href="../blog-batch-1/">Batch 1</a></p>
</body></html>
""",
        encoding="utf-8",
    )


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    CONTENT.mkdir(parents=True, exist_ok=True)

    skip_images = "--content-only" in __import__("sys").argv

    for g in GUIDES:
        write_guide(g)
        if not skip_images:
            prepare_images(g)
        print(f"✓ {g['slug']}")

    n = update_master_list()
    refresh_tracker_embed()
    rewrite_batch_index()

    print(f"\nSeeded {len(GUIDES)} Batch 2 guides")
    print(f"Updated {n} master-list rows → in-marketing")
    print(f"Images → {IMG}")
    print(f"Content → {CONTENT}")


if __name__ == "__main__":
    main()
