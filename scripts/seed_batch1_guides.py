#!/usr/bin/env python3
"""Seed Batch 1 guides into panun-marketing (content + images)."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

from batch1_guide_content import GUIDES, TITLE_SUBJECTS
from guide_image_utils import prepare_step_images

ROOT = Path(__file__).resolve().parents[2]
MKT = ROOT / "panun-marketing"
CONTENT = MKT / "content" / "guides"
IMG = MKT / "public" / "images" / "guides"
ASSETS_GEN = Path("/Users/kamran/.cursor/projects/Users-kamran-Desktop-panun-kaergar/assets")
BATCH_ASSETS = ROOT / "blog-batch-1" / "assets"
DEMO_ASSETS = ROOT / "blog-demo-assets"
MASTER = ROOT / "docs" / "seo" / "blog-master-list.json"
TRACKER = ROOT / "blog-tracker.html"

NAVY = (32, 32, 72, 255)
NAVY_DEEP = (22, 22, 50, 255)
GOLD = (255, 153, 0, 255)
CREAM = (250, 248, 244, 255)
PAPER = (243, 241, 236, 255)
MUTED = (92, 95, 114, 255)
WHITE = (255, 255, 255, 255)
LINE = (32, 32, 72, 40)


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def grain(img: Image.Image, amount: int = 12) -> Image.Image:
    noise = Image.effect_noise(img.size, amount).convert("L")
    noise = noise.point(lambda p: 128 + (p - 128) // 3)
    overlay = Image.merge("RGBA", (noise, noise, noise, Image.new("L", img.size, 28)))
    return Image.alpha_composite(img.convert("RGBA"), overlay)


def leaf(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0, flip: bool = False):
    s = scale
    pts = [(x, y), (x + int(18 * s) * (-1 if flip else 1), y + int(8 * s)), (x + int(6 * s) * (-1 if flip else 1), y + int(22 * s))]
    draw.polygon(pts, fill=NAVY)
    pts2 = [(x + int(8 * s) * (-1 if flip else 1), y + int(4 * s)), (x + int(22 * s) * (-1 if flip else 1), y + int(14 * s)), (x + int(10 * s) * (-1 if flip else 1), y + int(28 * s))]
    draw.polygon(pts2, fill=GOLD)


def draw_methods_ladder(path: Path, steps: list[str]):
    w, h = 1200, 900
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    draw.rectangle((40, 40, w - 40, h - 40), outline=LINE, width=2)
    title_f = font(36, True)
    step_f = font(28, True)
    body_f = font(24)
    draw.text((70, 60), "Method ladder", fill=NAVY, font=title_f)
    draw.text((70, 110), "Start shallow. Go deeper only if needed.", fill=MUTED, font=body_f)
    y = 170
    for i, label in enumerate(steps[:6], 1):
        box = (70, y, w - 70, y + 95)
        draw.rounded_rectangle(box, radius=8, fill=WHITE, outline=LINE, width=2)
        draw.rectangle((70, y, 78, y + 95), fill=NAVY if i < 5 else GOLD)
        badge = (95, y + 28, 145, y + 68)
        draw.ellipse(badge, fill=GOLD)
        draw.text((112, y + 34), str(i), fill=NAVY_DEEP, font=step_f)
        draw.text((170, y + 34), label, fill=NAVY, font=step_f)
        y += 110
    leaf(draw, 70, h - 90, 1.2)
    leaf(draw, w - 110, h - 95, 1.1, flip=True)
    grain(img).convert("RGB").save(path, "WEBP", quality=88)


def draw_diagram(path: Path, title: str, boxes: list[str]):
    w, h = 1200, 675
    img = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(img)
    draw.rectangle((36, 36, w - 36, h - 36), fill=WHITE, outline=LINE, width=2)
    draw.text((70, 60), title, fill=NAVY, font=font(34, True))
    cols = min(3, len(boxes))
    gap = 28
    bw = (w - 140 - gap * (cols - 1)) // cols
    for i, label in enumerate(boxes[:3]):
        x = 70 + i * (bw + gap)
        y = 160
        draw.rounded_rectangle((x, y, x + bw, y + 360), radius=10, fill=CREAM, outline=LINE, width=2)
        draw.ellipse((x + bw // 2 - 28, y + 40, x + bw // 2 + 28, y + 96), fill=NAVY)
        draw.text((x + bw // 2 - 8, y + 54), str(i + 1), fill=GOLD, font=font(28, True))
        # wrap label
        words = label.split()
        lines, cur = [], ""
        for word in words:
            test = f"{cur} {word}".strip()
            if font(22).getlength(test) < bw - 40:
                cur = test
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        ty = y + 140
        for line in lines[:5]:
            draw.text((x + 20, ty), line, fill=NAVY, font=font(22))
            ty += 32
    leaf(draw, 48, h - 80)
    leaf(draw, w - 100, 48, flip=True)
    grain(img).convert("RGB").save(path, "WEBP", quality=88)


def draw_tip(path: Path, title: str, line: str):
    w, h = 1200, 675
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((50, 50, w - 50, h - 50), radius=12, fill=WHITE, outline=LINE, width=2)
    draw.rectangle((50, 50, 62, h - 50), fill=GOLD)
    draw.text((100, 90), "Prevention tip", fill=GOLD, font=font(22, True))
    draw.text((100, 140), title, fill=NAVY, font=font(40, True))
    # wrap body
    words = line.split()
    lines, cur = [], ""
    for word in words:
        test = f"{cur} {word}".strip()
        if font(28).getlength(test) < w - 220:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    ty = 230
    for ln in lines[:6]:
        draw.text((100, ty), ln, fill=MUTED, font=font(28))
        ty += 42
    # simple icon circle
    draw.ellipse((w - 260, h - 260, w - 100, h - 100), fill=NAVY)
    draw.ellipse((w - 230, h - 230, w - 130, h - 130), fill=GOLD)
    leaf(draw, 90, h - 120, 1.3)
    grain(img).convert("RGB").save(path, "WEBP", quality=88)


def draw_simple_cover(path: Path, subject: str):
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), NAVY_DEEP)
    draw = ImageDraw.Draw(img)
    # soft gold glow
    for r, a in ((520, 40), (360, 55), (220, 70)):
        overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse((w // 2 - r, h // 2 - r + 40, w // 2 + r, h // 2 + r + 40), fill=(255, 153, 0, a))
        img = Image.alpha_composite(img, overlay)
        draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((w // 2 - 220, h // 2 - 160, w // 2 + 220, h // 2 + 160), radius=24, fill=CREAM)
    draw.ellipse((w // 2 - 70, h // 2 - 70, w // 2 + 70, h // 2 + 70), fill=NAVY)
    draw.ellipse((w // 2 - 40, h // 2 - 40, w // 2 + 40, h // 2 + 40), fill=GOLD)
    # subject caption for uniqueness (small, bottom)
    words = subject.split()[:6]
    label = " ".join(words)
    draw.text((70, h - 90), label[:48], fill=(255, 255, 255, 180), font=font(28))
    leaf(draw, 60, 60, 1.4)
    leaf(draw, w - 130, 70, 1.3, flip=True)
    grain(img, 18).convert("RGB").save(path, "WEBP", quality=86)


def yq(s: str) -> str:
    """Single-quoted YAML scalar (safe for colons / apostrophes)."""
    return "'" + s.replace("'", "''") + "'"


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
publishedAt: 2026-07-25
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


def find_title_source(slug: str) -> Path | None:
    for base in (ASSETS_GEN, DEMO_ASSETS, BATCH_ASSETS):
        for name in (f"{slug}-title.webp", "title-card.webp" if "drain" in slug else None):
            if not name:
                continue
            p = base / name
            if p.exists():
                return p
    # any generated match
    matches = list(ASSETS_GEN.glob(f"*{slug}*title*.webp"))
    return matches[0] if matches else None


def prepare_images(g: dict):
    slug = g["slug"]
    subject = TITLE_SUBJECTS.get(slug, slug.replace("-", " "))

    # title
    title_dst = IMG / f"{slug}-title.webp"
    src = find_title_source(slug)
    if src:
        shutil.copy2(src, title_dst)
    else:
        # minimal fallback title
        img = Image.new("RGBA", (900, 900), CREAM)
        d = ImageDraw.Draw(img)
        d.ellipse((300, 280, 600, 580), fill=NAVY)
        d.ellipse((360, 340, 540, 520), fill=GOLD)
        leaf(d, 60, 60, 1.5)
        leaf(d, 780, 70, 1.4, flip=True)
        grain(img).convert("RGB").save(title_dst, "WEBP", quality=88)

    # cover
    cover_dst = IMG / f"{slug}-cover.webp"
    if slug.startswith("how-to-unblock") and (DEMO_ASSETS / "cover-hero.webp").exists():
        shutil.copy2(DEMO_ASSETS / "cover-hero.webp", cover_dst)
    else:
        batch_cover = BATCH_ASSETS / f"{slug}-cover.webp"
        # Prefer newly drawn simple covers over busy AI batch covers
        draw_simple_cover(cover_dst, subject)

    # illustrations
    steps_map = {
        "how-to-unblock-kitchen-sink-drain-kashmir": [
            "Bail + hot water & soap",
            "Plunge with cup plunger",
            "Baking soda + vinegar",
            "Skip harsh chemicals",
            "Clean the P-trap",
            "Hand snake / book help",
        ],
        "mcb-keeps-tripping-kashmir": [
            "Make the board area safe",
            "Unplug the heavy load",
            "Reset once, circuit clear",
            "Find the trigger appliance",
            "Book insulation / wiring test",
        ],
        "ac-not-cooling-kashmir": [
            "Check Cool mode & setpoint",
            "Clean dry filters",
            "Clear outdoor airflow",
            "Stop if iced",
            "Diagnose before gas",
        ],
    }
    steps = steps_map.get(
        slug,
        [
            "Make it safe",
            "Do the smallest test",
            "Note what changes",
            "Stop if risk rises",
            "Book the right trade",
        ],
    )
    draw_methods_ladder(IMG / f"{slug}-methods.webp", steps)
    draw_diagram(
        IMG / f"{slug}-diagram.webp",
        "Diagnosis map",
        ["What you notice", "Likely cause", "First move"],
    )
    tip_lines = {
        "how-to-unblock-kitchen-sink-drain-kashmir": ("Bin the ghee", "Cool oil and fat go in the bin — not the pipe — even if hot water is chasing them."),
        "mcb-keeps-tripping-kashmir": ("One reset is enough", "If it trips instantly again, stop resetting. The board is doing its job."),
        "ac-not-cooling-kashmir": ("Dry filters only", "Never run the indoor unit with a dripping filter after washing."),
    }
    tip_title, tip_body = tip_lines.get(
        slug,
        ("Small habits win", "A five-minute check done early usually beats an emergency visit later."),
    )
    draw_tip(IMG / f"{slug}-tip.webp", tip_title, tip_body)

    prepare_step_images(g, IMG, subject)

    # plumbing demo extras if available
    if slug.startswith("how-to-unblock"):
        for name, dest in (
            ("methods-ladder.webp", f"{slug}-methods.webp"),
            ("diagram-p-trap.webp", f"{slug}-diagram.webp"),
            ("prevention-tips.webp", f"{slug}-tip.webp"),
        ):
            src = DEMO_ASSETS / name
            if src.exists():
                shutil.copy2(src, IMG / dest)


def update_master_list():
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    by_slug = {g["slug"]: g for g in GUIDES}
    by_id = {g["id"]: g for g in GUIDES}
    updated = 0
    for blog in data.get("blogs", []):
        g = by_id.get(blog.get("id")) or by_slug.get(blog.get("slug"))
        if not g:
            continue
        blog["status"] = "in-marketing"
        blog["demoFile"] = ""
        blog["marketingPath"] = f"/guides/{g['slug']}"
        blog["marketingSlug"] = g["slug"]
        updated += 1
    meta = data.setdefault("meta", {})
    meta["updated"] = "2026-07-25"
    meta["marketingBlogStatus"] = "batch1_in_marketing"
    meta["marketingNote"] = "Batch 1 guides live under panun-marketing content/guides and /guides/[slug]."
    MASTER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return updated


def refresh_tracker_embed():
    """Replace the embedded DATA JSON in blog-tracker.html from master list."""
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
    """Replace demo batch index with pointer to live marketing guides."""
    batch = ROOT / "blog-batch-1"
    batch.mkdir(exist_ok=True)
    links = "\n".join(
        f'    <li><a href="../panun-marketing/content/guides/{g["slug"]}/">{g["title"]}</a> → live at <code>/guides/{g["slug"]}</code></li>'
        for g in GUIDES
    )
    (batch / "README.md").write_text(
        f"""# Batch 1 moved into panun-marketing

These guides are no longer demo HTML.

- Content: `panun-marketing/content/guides/`
- Images: `panun-marketing/public/images/guides/`
- Live routes: `/guides/[slug]` in the marketing site

## Guides

{chr(10).join(f'- `{g["slug"]}` ({g["id"]})' for g in GUIDES)}
""",
        encoding="utf-8",
    )
    # Keep a tiny index for local convenience
    (batch / "index.html").write_text(
        f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Batch 1 → panun-marketing</title>
<style>body{{font:16px/1.6 system-ui;max-width:720px;margin:40px auto;padding:0 20px;color:#202048}}
a{{color:#202048;font-weight:700}}</style></head>
<body>
<h1>Batch 1 is in panun-marketing</h1>
<p>Demo HTML was retired. Open the marketing site guides:</p>
<ul>
{links}
</ul>
<p><a href="../blog-tracker.html">Back to tracker</a></p>
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

    for html in (ROOT / "blog-batch-1").glob("*.html"):
        if html.name == "index.html":
            continue
        html.unlink(missing_ok=True)

    print(f"\nSeeded {len(GUIDES)} guides")
    print(f"Updated {n} master-list rows → in-marketing")
    print(f"Images → {IMG}")
    print(f"Content → {CONTENT}")


if __name__ == "__main__":
    main()
