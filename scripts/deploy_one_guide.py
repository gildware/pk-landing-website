#!/usr/bin/env python3
"""Deploy PNG assets for one guide slug, corner-brand, update article."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from batch2_guide_content import GUIDES
from guide_image_utils import GUIDE_IMAGE_ROLES, apply_brand_to_guide
from seed_batch2_guides import write_guide

ASSETS = Path("/Users/kamran/.cursor/projects/Users-kamran-Desktop-panun-kaergar/assets")
PUBLIC = Path(__file__).resolve().parents[1] / "public" / "images" / "guides"
BACKUP_ROOT = Path(__file__).resolve().parents[2] / "blog-batch-2" / "assets" / "pre-brand-backup"


def deploy_slug(slug: str) -> None:
    pristine = BACKUP_ROOT / slug
    pristine.mkdir(parents=True, exist_ok=True)
    for role in GUIDE_IMAGE_ROLES:
        src = ASSETS / f"{slug}-{role}.png"
        if not src.exists():
            raise FileNotFoundError(src)
        dst = PUBLIC / f"{slug}-{role}.webp"
        q = 100 if role == "title" else 95
        subprocess.run(["cwebp", "-q", str(q), str(src), "-o", str(dst)], check=True, capture_output=True)
        subprocess.run(["cp", str(dst), str(pristine / dst.name)], check=True)
    n = apply_brand_to_guide(slug, PUBLIC, backup_dir=BACKUP_ROOT, pristine_dir=pristine)
    write_guide(next(g for g in GUIDES if g["slug"] == slug))
    cover = PUBLIC / f"{slug}-cover.webp"
    print(f"OK {slug}: {n} images, cover={cover.stat().st_size} bytes")


if __name__ == "__main__":
    deploy_slug(sys.argv[1])
