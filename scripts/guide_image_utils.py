"""Shared image prompts and step illustration helpers for Panun Kaergar guides."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "blog-batch-3" / "assets" / "prompts"
ASSETS_GEN = ROOT / "blog-batch-3" / "assets" / "generated"
BATCH_ASSETS = ROOT / "blog-batch-1" / "assets"
BATCH2_ASSETS = ROOT / "blog-batch-2" / "assets"
BATCH3_ASSETS = ROOT / "blog-batch-3" / "assets"
DEMO_ASSETS = ROOT / "blog-demo-assets"
BRAND_DIR = ROOT / "public" / "images" / "brand"

# Official Panun Kaergar logos only — full wordmarks, never small marks or AI-drawn logos.
LOGO_WHITE = BRAND_DIR / "logo-white.png"
LOGO_COLOR = BRAND_DIR / "logo-color.png"
LOGO_SQUARE = ROOT / "public" / "logo-square.png"
OFFICIAL_LOGOS = (LOGO_WHITE, LOGO_COLOR)

GUIDE_IMAGE_ROLES = (
    "cover",
    "title",
    "methods",
    "diagram",
    "tip",
    *(f"method-{n}" for n in range(1, 7)),
    *(f"dont-{n}" for n in range(1, 4)),
)

RICH_IMAGE_MIN_BYTES = 100_000

NAVY = (32, 32, 72, 255)
GOLD = (255, 153, 0, 255)
CREAM = (250, 248, 244, 255)
PAPER = (243, 241, 236, 255)
MUTED = (92, 95, 114, 255)
WHITE = (255, 255, 255, 255)
LINE = (32, 32, 72, 40)
RED = (180, 48, 48, 255)


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


PROMPT_STYLE = (
    "Flat vector illustration, 16:9 landscape. Cream #faf8f4 background. "
    "Palette only navy #202048, gold #FF9900, cream. Clean home-service diagram style. "
    "No photorealism, no text labels in the image, no locality names. "
    "CRITICAL — zero branding in the artwork: no logos, no watermarks, no brand marks, "
    "no gear icons used as logos, no letter monograms, no company names, no PANUN text. "
    "Pure instructional illustration only; margins stay empty for a post-process overlay."
)

# Official wordmark size on guide images (Logo Color / Logo White only).
LOGO_HEIGHT_RATIO_LANDSCAPE = 0.102
LOGO_HEIGHT_RATIO_SQUARE = 0.092

LOGO_CORNERS = ("top-left", "top-right", "bottom-left", "bottom-right")
CREAM_TARGET = (250, 248, 244)


def _logo_margins(w: int, h: int) -> tuple[int, int]:
    return max(16, int(w * 0.025)), max(16, int(h * 0.03))


def _clamp_box(
    w: int, h: int, x: int, y: int, logo_w: int, logo_h: int
) -> tuple[int, int, int, int]:
    x = max(0, min(x, w - logo_w))
    y = max(0, min(y, h - logo_h))
    return (x, y, x + logo_w, y + logo_h)


def _cream_ratio(rgb: Image.Image) -> float:
    pixels = rgb.getdata()
    if not pixels:
        return 0.0
    close = 0
    for r, g, b in pixels:
        if abs(r - CREAM_TARGET[0]) + abs(g - CREAM_TARGET[1]) + abs(b - CREAM_TARGET[2]) < 48:
            close += 1
    return close / len(pixels)


def _navy_ratio(rgb: Image.Image) -> float:
    pixels = rgb.getdata()
    if not pixels:
        return 0.0
    hits = 0
    for r, g, b in pixels:
        if r < 70 and g < 70 and b < 100:
            hits += 1
    return hits / len(pixels)


def _region_emptiness_score(img: Image.Image, box: tuple[int, int, int, int]) -> float:
    """Higher score = emptier / safer for logo placement (no content overlap)."""
    w, h = img.size
    x0, y0, x1, y1 = box
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    if x1 <= x0 or y1 <= y0:
        return -9999.0

    rgb = img.convert("RGB").crop((x0, y0, x1, y1))
    gray = rgb.convert("L")
    edges = gray.filter(ImageFilter.FIND_EDGES)
    gstat = ImageStat.Stat(gray)
    estat = ImageStat.Stat(edges)
    mean = gstat.mean[0]
    variance = gstat.var[0]
    edge_mean = estat.mean[0]
    edge_max = estat.extrema[0][1]
    cream = _cream_ratio(rgb)
    navy = _navy_ratio(rgb)

    score = cream * 150.0
    score -= navy * 250.0  # avoid banners, headings, dark UI blocks
    if mean >= 215:
        score += 40.0
    elif mean >= 165:
        score += 18.0
    elif mean < 90 and variance < 600:
        score += 28.0

    # Penalise detail/text — lower edge & variance wins among candidates
    score -= edge_mean * 22.0
    score -= variance * 0.06
    score -= edge_max * 0.2
    return score


def _iter_logo_positions(w: int, h: int, logo_w: int, logo_h: int) -> list[tuple[int, int]]:
    """Candidate (x, y) anchors — four corners only, never mid-frame."""
    mx, my = _logo_margins(w, h)
    max_x = max(mx, w - logo_w - mx)
    max_y = max(my, h - logo_h - my)
    return [(mx, my), (max_x, my), (mx, max_y), (max_x, max_y)]


def pick_best_logo_position(img: Image.Image, logo_w: int, logo_h: int) -> tuple[int, int, float]:
    """Return (x, y) for logo placement in the best corner only."""
    w, h = img.size
    best_xy = (_logo_margins(w, h)[0], _logo_margins(w, h)[1])
    best_score = float("-inf")

    for x, y in _iter_logo_positions(w, h, logo_w, logo_h):
        box = _clamp_box(w, h, x, y, logo_w, logo_h)
        score = _region_emptiness_score(img, box)
        if score > best_score:
            best_score = score
            best_xy = (box[0], box[1])

    return best_xy[0], best_xy[1], best_score


def pick_best_logo_corner(img: Image.Image, logo_w: int, logo_h: int) -> str:
    """Legacy helper — maps best position to nearest corner name."""
    x, y, _ = pick_best_logo_position(img, logo_w, logo_h)
    w, h = img.size
    mx, my = _logo_margins(w, h)
    right = x >= w // 2
    bottom = y >= h // 2
    if bottom and not right:
        return "bottom-left"
    if bottom and right:
        return "bottom-right"
    if not bottom and right:
        return "top-right"
    return "top-left"


def pick_logo_wordmark(
    img: Image.Image,
    *,
    box: tuple[int, int, int, int] | None = None,
    corner: str = "top-left",
    logo_w: int = 0,
    logo_h: int = 0,
) -> Path:
    """Logo_Color on light backgrounds; Logo White on dark backgrounds."""
    if box:
        sample = img.convert("RGB").crop(box)
    elif logo_w > 0 and logo_h > 0:
        w, h = img.size
        mx, my = _logo_margins(w, h)
        if corner == "top-right":
            box = (w - logo_w - mx, my, w - mx, my + logo_h)
        elif corner == "bottom-left":
            box = (mx, h - logo_h - my, mx + logo_w, h - my)
        elif corner == "bottom-right":
            box = (w - logo_w - mx, h - logo_h - my, w - mx, h - my)
        else:
            box = (mx, my, mx + logo_w, my + logo_h)
        sample = img.convert("RGB").crop(box)
    else:
        fw = max(1, int(img.width * 0.12))
        fh = max(1, int(img.height * 0.12))
        sample = img.convert("RGB").crop((0, 0, fw, fh))
    pixels = sample.getdata()
    mean = sum(sum(px) / 3 for px in pixels) / max(len(pixels), 1)
    return LOGO_COLOR if LOGO_COLOR.exists() and mean >= 165 else (
        LOGO_WHITE if LOGO_WHITE.exists() else LOGO_SQUARE
    )


def load_logo(path: Path) -> Image.Image:
    if path.exists():
        return Image.open(path).convert("RGBA")
    if LOGO_SQUARE.exists():
        return Image.open(LOGO_SQUARE).convert("RGBA")
    raise FileNotFoundError(f"Official logo missing: {path}")


def composite_brand_mark(
    base: Image.Image,
    *,
    corner: str | None = None,
    height_ratio: float | None = None,
) -> Image.Image:
    """Overlay official Panun Kaergar wordmark (Logo White or Logo Color only)."""
    for logo_path in OFFICIAL_LOGOS:
        if logo_path.exists():
            break
    else:
        if not LOGO_SQUARE.exists():
            raise FileNotFoundError(
                f"Missing official logo in {BRAND_DIR} or {LOGO_SQUARE}."
            )

    img = base.convert("RGBA")

    if height_ratio is None:
        height_ratio = (
            LOGO_HEIGHT_RATIO_LANDSCAPE if img.width >= img.height else LOGO_HEIGHT_RATIO_SQUARE
        )
    target_h = max(28, int(img.height * height_ratio))
    probe = load_logo(LOGO_COLOR)
    scale = target_h / probe.height
    target_w = max(40, int(probe.width * scale))

    if corner is None:
        x, y, score = pick_best_logo_position(img, target_w, target_h)
        # If no good empty slot, shrink slightly and retry once
        if score < 10:
            target_h = max(24, int(target_h * 0.85))
            target_w = max(36, int(probe.width * (target_h / probe.height)))
            x, y, _ = pick_best_logo_position(img, target_w, target_h)
    else:
        w, h = img.size
        mx, my = _logo_margins(w, h)
        if corner == "top-right":
            x, y = w - target_w - mx, my
        elif corner == "bottom-left":
            x, y = mx, h - target_h - my
        elif corner == "bottom-right":
            x, y = w - target_w - mx, h - target_h - my
        else:
            x, y = mx, my

    box = _clamp_box(img.width, img.height, x, y, target_w, target_h)
    logo_path = pick_logo_wordmark(img, box=box)
    logo = load_logo(logo_path)
    logo = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    out = img.copy()
    out.alpha_composite(logo, (box[0], box[1]))
    return out


def apply_brand_to_image_path(
    path: Path,
    *,
    backup_dir: Path | None = None,
    pristine_dir: Path | None = None,
) -> bool:
    """Composite official logo onto one guide image file."""
    if not path.exists() or path.suffix.lower() not in {".webp", ".png", ".jpg", ".jpeg"}:
        return False

    source = path
    if pristine_dir and (pristine_dir / path.name).exists():
        source = pristine_dir / path.name
    elif backup_dir and (backup_dir / path.name).exists():
        source = backup_dir / path.name
    else:
        png = ASSETS_GEN / path.name.replace(".webp", ".png")
        if png.exists():
            source = png

    img = Image.open(source)
    branded = composite_brand_mark(img)
    if backup_dir:
        backup_dir.mkdir(parents=True, exist_ok=True)
        if not (backup_dir / path.name).exists() and source == path:
            shutil.copy2(path, backup_dir / path.name)
    branded.convert("RGB").save(path, "WEBP", quality=95, method=6)
    return True


def apply_brand_to_guide(
    slug: str,
    img_dir: Path,
    *,
    backup_dir: Path | None = None,
    pristine_dir: Path | None = None,
) -> int:
    """Apply official logos to all standard guide image slots for one slug."""
    count = 0
    guide_backup = backup_dir / slug if backup_dir else None
    guide_pristine = pristine_dir / slug if pristine_dir else None
    for role in GUIDE_IMAGE_ROLES:
        path = img_dir / f"{slug}-{role}.webp"
        if apply_brand_to_image_path(path, backup_dir=guide_backup, pristine_dir=guide_pristine):
            count += 1
    return count


def _split_dont(dont: str) -> tuple[str, str]:
    """Split a dont line into (title, body)."""
    if ";" in dont:
        title, body = dont.split(";", 1)
        return title.strip(), body.strip()
    if "." in dont:
        title, body = dont.split(".", 1)
        return title.strip(), body.strip()
    words = dont.split()
    if len(words) <= 8:
        return dont.strip(), dont.strip()
    return " ".join(words[:6]).strip(), dont.strip()


def method_alt(heading: str, detail: str, subject: str) -> str:
    detail_bit = detail.split(".")[0].strip()
    if len(detail_bit) > 90:
        detail_bit = detail_bit[:87] + "..."
    return f"{heading} — {detail_bit}" if detail_bit else f"{heading} for {subject}"


def dont_alt(title: str, body: str, subject: str) -> str:
    bit = body.split(".")[0].strip() or title
    if len(bit) > 100:
        bit = bit[:97] + "..."
    return f"Unsafe {subject} habit: {title.lower()} — {bit.lower()}"


def method_prompt(heading: str, detail: str, subject: str, category: str, number: int) -> str:
    return (
        f"{PROMPT_STYLE} Method {number} for a Kashmir home guide about {subject}. "
        f"Show: {heading}. Scene detail: {detail.split('.')[0]}. "
        f"Category: {category}. Helpful, calm, practical — not cartoonish."
    )


def dont_prompt(title: str, body: str, subject: str, category: str, number: int) -> str:
    return (
        f"{PROMPT_STYLE} 'What not to do' step {number} for a Kashmir home guide about {subject}. "
        f"Show the unsafe habit: {title}. Why it fails: {body.split('.')[0]}. "
        f"Category: {category}. Include a subtle stop/warning feeling — no gore, no shock imagery."
    )


def enrich_guide_images(guide: dict, subject: str | None = None) -> dict:
    """Attach method_images and dont_blocks (if missing) for HTML + image generation."""
    subject = subject or guide.get("title", "").split("?")[0].lower()
    category = guide.get("category", "Home")

    overrides = guide.get("image_prompt_overrides", {})
    method_images = []
    for i, (heading, best_for, detail) in enumerate(guide.get("methods", []), 1):
        alt = method_alt(heading, detail, subject)
        cap = heading
        prompt = overrides.get(f"method-{i}") or method_prompt(heading, detail, subject, category, i)
        method_images.append(
            {"num": i, "alt": alt, "caption": cap, "prompt": prompt, "best_for": best_for}
        )
    guide["method_images"] = method_images

    if not guide.get("dont_blocks"):
        blocks = []
        for i, dont in enumerate(guide.get("donts", []), 1):
            title, body = _split_dont(dont)
            alt = dont_alt(title, body, subject)
            prompt = dont_prompt(title, body, subject, category, i)
            blocks.append((title, "Common mistake", body, alt, "Avoid this", prompt))
        guide["dont_blocks"] = blocks

    return guide


def collect_image_jobs(guide: dict, subject: str | None = None) -> list[dict]:
    """All per-step image jobs for a guide (methods + donts)."""
    enrich_guide_images(guide, subject)
    slug = guide["slug"]
    overrides = guide.get("image_prompt_overrides", {})
    jobs: list[dict] = []

    for m in guide["method_images"]:
        jobs.append(
            {
                "slug": slug,
                "kind": "method",
                "num": m["num"],
                "file": f"{slug}-method-{m['num']}.webp",
                "alt": m["alt"],
                "prompt": m["prompt"],
                "label": m["caption"],
            }
        )

    for i, block in enumerate(guide.get("dont_blocks", []), 1):
        if len(block) >= 6:
            title, _sub, body, alt, cap, prompt = block[:6]
        else:
            title, _sub, body, alt, cap = block[:5]
            prompt = overrides.get(f"dont-{i}") or dont_prompt(
                title, body, subject or slug, guide.get("category", "Home"), i
            )
        jobs.append(
            {
                "slug": slug,
                "kind": "dont",
                "num": i,
                "file": f"{slug}-dont-{i}.webp",
                "alt": alt,
                "prompt": prompt,
                "label": title,
            }
        )
    return jobs


def write_prompts_file(guide: dict, subject: str | None = None) -> Path:
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    jobs = collect_image_jobs(guide, subject)
    payload = {
        "slug": guide["slug"],
        "title": guide.get("title", ""),
        "category": guide.get("category", ""),
        "jobs": jobs,
    }
    path = PROMPTS_DIR / f"{guide['slug']}-prompts.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def is_rich_image(path: Path) -> bool:
    try:
        return path.is_file() and path.stat().st_size >= RICH_IMAGE_MIN_BYTES
    except OSError:
        return False


def find_step_asset(filename: str) -> Path | None:
    for base in (ASSETS_GEN, BATCH2_ASSETS, BATCH_ASSETS, DEMO_ASSETS, PROMPTS_DIR.parent):
        if base is None or not base.exists():
            continue
        p = base / filename
        if p.exists():
            return p
    matches = list(ASSETS_GEN.glob(f"*{filename}*")) if ASSETS_GEN.exists() else []
    return matches[0] if matches else None


def find_guide_asset(slug: str, role: str) -> Path | None:
    """Find cover/title/methods/diagram/tip assets for a guide slug."""
    name = f"{slug}-{role}.webp"
    return find_step_asset(name)


def draw_step_illustration(
    path: Path,
    *,
    kind: str,
    number: int,
    title: str,
    subtitle: str = "",
    accent: tuple[int, int, int, int] = GOLD,
) -> None:
    """PIL fallback when AI art is not yet generated."""
    w, h = 1200, 675
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    draw.rectangle((40, 40, w - 40, h - 40), outline=LINE, width=2)

    badge_label = f"Method {number}" if kind == "method" else f"Don't {number}"
    badge_color = accent if kind == "method" else RED
    draw.rounded_rectangle((70, 60, 260, 110), radius=8, fill=badge_color)
    draw.text((95, 72), badge_label, fill=WHITE, font=font(24, True))

    # wrap title
    words = title.split()
    lines, cur = [], ""
    for word in words:
        test = f"{cur} {word}".strip()
        if font(34, True).getlength(test) < w - 160:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    ty = 150
    for line in lines[:3]:
        draw.text((70, ty), line, fill=NAVY, font=font(34, True))
        ty += 46

    if subtitle:
        words = subtitle.split()
        sub_lines, cur = [], ""
        for word in words:
            test = f"{cur} {word}".strip()
            if font(24).getlength(test) < w - 160:
                cur = test
            else:
                sub_lines.append(cur)
                cur = word
        if cur:
            sub_lines.append(cur)
        for line in sub_lines[:4]:
            draw.text((70, ty), line, fill=MUTED, font=font(24))
            ty += 34

    # simple icon panel
    draw.rounded_rectangle((w - 340, 180, w - 80, h - 120), radius=12, fill=PAPER, outline=LINE, width=2)
    draw.ellipse((w - 270, 240, w - 150, 360), fill=NAVY)
    draw.ellipse((w - 235, 275, w - 185, 325), fill=GOLD)
    leaf(draw, 70, h - 110, 1.2)
    leaf(draw, w - 120, h - 100, 1.1, flip=True)
    grain(img).convert("RGB").save(path, "WEBP", quality=88)


def prepare_step_images(guide: dict, img_dir: Path, subject: str | None = None) -> int:
    """Generate or copy method/dont step images; write prompts JSON. Returns job count."""
    jobs = collect_image_jobs(guide, subject)
    write_prompts_file(guide, subject)
    img_dir.mkdir(parents=True, exist_ok=True)

    for job in jobs:
        dst = img_dir / job["file"]
        src = find_step_asset(job["file"])
        if src and src.resolve() != dst.resolve():
            if not is_rich_image(dst) or is_rich_image(src):
                shutil.copy2(src, dst)
        elif not dst.exists() or not is_rich_image(dst):
            detail = guide["methods"][job["num"] - 1][2] if job["kind"] == "method" else ""
            draw_step_illustration(
                dst,
                kind=job["kind"],
                number=job["num"],
                title=job["label"],
                subtitle=detail[:120] if detail else job["alt"][:120],
                accent=GOLD if job["kind"] == "method" else RED,
            )
    return len(jobs)
