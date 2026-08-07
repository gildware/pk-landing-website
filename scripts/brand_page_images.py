#!/usr/bin/env python3
"""Composite transparent official logo onto page hero images (no backing plate)."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageFilter, ImageStat

from guide_image_utils import (
    LOGO_COLOR,
    LOGO_WHITE,
    _clamp_box,
    _region_emptiness_score,
    load_logo,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "public" / "images" / "why-choose"

# Page heroes need a larger wordmark than guide thumbnails.
PAGE_LOGO_HEIGHT_RATIO = 0.165


def _page_margins(w: int, h: int) -> tuple[int, int]:
    return max(28, int(w * 0.04)), max(28, int(h * 0.04))


def _corner_positions(w: int, h: int, logo_w: int, logo_h: int) -> list[tuple[str, int, int]]:
    mx, my = _page_margins(w, h)
    max_x = max(mx, w - logo_w - mx)
    max_y = max(my, h - logo_h - my)
    return [
        ("top-left", mx, my),
        ("top-right", max_x, my),
        ("bottom-left", mx, max_y),
        ("bottom-right", max_x, max_y),
    ]


def _region_luminance(img: Image.Image, box: tuple[int, int, int, int]) -> float:
    sample = img.convert("RGB").crop(box)
    stat = ImageStat.Stat(sample)
    return sum(stat.mean) / 3.0


def pick_best_corner(
    img: Image.Image,
    logo_w: int,
    logo_h: int,
) -> tuple[str, int, int, Path]:
    """Pick the corner with best emptiness + logo contrast (no solid backing)."""
    w, h = img.size
    best: tuple[str, int, int, Path, float] | None = None

    for corner, x, y in _corner_positions(w, h, logo_w, logo_h):
        box = _clamp_box(w, h, x, y, logo_w, logo_h)
        emptiness = _region_emptiness_score(img, box)
        luminance = _region_luminance(img, box)
        logo_path = LOGO_COLOR if luminance >= 128 else LOGO_WHITE
        # Reward corners where the chosen variant will read clearly.
        if logo_path == LOGO_COLOR:
            contrast = min(luminance, 255.0) / 255.0
        else:
            contrast = (255.0 - luminance) / 255.0
        score = emptiness + contrast * 120.0
        if best is None or score > best[4]:
            best = (corner, box[0], box[1], logo_path, score)

    assert best is not None
    return best[0], best[1], best[2], best[3]


def _shadow_from_logo(logo: Image.Image, *, rgba: tuple[int, int, int, int]) -> Image.Image:
    alpha = logo.split()[3]
    shadow = Image.new("RGBA", logo.size, rgba)
    shadow.putalpha(alpha.point(lambda a: int(a * rgba[3] / 255)))
    return shadow.filter(ImageFilter.GaussianBlur(radius=2))


def composite_logo(
    base: Image.Image,
    logo: Image.Image,
    x: int,
    y: int,
    *,
    logo_path: Path,
) -> Image.Image:
    """Transparent logo with a soft shadow for legibility — no solid plate."""
    out = base.copy()
    if logo_path == LOGO_COLOR:
        shadow_rgba = (32, 32, 72, 110)
    else:
        shadow_rgba = (0, 0, 0, 130)

    for dx, dy, alpha_scale in ((4, 5, 1.0), (2, 2, 0.55)):
        shadow = _shadow_from_logo(logo, rgba=(*shadow_rgba[:3], int(shadow_rgba[3] * alpha_scale)))
        layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        layer.alpha_composite(shadow, (x + dx, y + dy))
        out = Image.alpha_composite(out, layer)

    out.alpha_composite(logo, (x, y))
    return out


def brand_page_image(
    src: Path,
    dst: Path,
    *,
    width: int = 1920,
    height: int = 1280,
    quality: int = 92,
) -> str:
    img = Image.open(src).convert("RGBA")
    img = img.resize((width, height), Image.Resampling.LANCZOS)

    h = img.height
    target_h = max(56, int(h * PAGE_LOGO_HEIGHT_RATIO))
    probe = load_logo(LOGO_COLOR)
    target_w = max(72, int(probe.width * (target_h / probe.height)))

    corner, x, y, logo_path = pick_best_corner(img, target_w, target_h)
    logo = load_logo(logo_path)
    logo = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    branded = composite_logo(img, logo, x, y, logo_path=logo_path)

    dst.parent.mkdir(parents=True, exist_ok=True)
    branded.convert("RGB").save(dst, "WEBP", quality=quality, method=6)
    return corner


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    jobs = [
        ("why-choose-hero-v4.png", "why-choose-hero.webp"),
        ("why-choose-verified-v6.png", "why-choose-verified.webp"),
        ("why-choose-booking-v4.png", "why-choose-booking.webp"),
        ("why-choose-local-v4.png", "why-choose-local.webp"),
        ("features-hero-src.png", "features-hero.webp"),
        ("features-app-src.png", "features-app.webp"),
        ("features-booking-src.png", "features-booking.webp"),
        ("features-custom-jobs-src.png", "features-custom-jobs.webp"),
    ]

    for src_name, dst_name in jobs:
        src = args.src_dir / src_name
        dst = args.out_dir / dst_name
        corner = brand_page_image(src, dst)
        print(f"{dst_name}: {dst.stat().st_size // 1024} KB ({corner})")


if __name__ == "__main__":
    main()
