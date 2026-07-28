#!/usr/bin/env python3
"""Composite official Panun Kaergar logos onto guide images."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from guide_image_utils import (
    BATCH2_ASSETS,
    apply_brand_to_guide,
    apply_brand_to_image_path,
)
from seed_batch1_guides import IMG

DEFAULT_SLUGS = (
    "drain-smell-causes-kashmir",
    "aluminium-door-not-sliding-smoothly",
    "flickering-lights-causes-kashmir",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="Guide slugs (default: Batch 2 AI-pass guides)")
    parser.add_argument("--all-rich", action="store_true", help="Brand every guide with rich images")
    args = parser.parse_args()

    if args.all_rich:
        slugs = sorted({p.name.rsplit("-", 2)[0] for p in IMG.glob("*-cover.webp")})
    elif args.slugs:
        slugs = args.slugs
    else:
        slugs = list(DEFAULT_SLUGS)

    total = 0
    for slug in slugs:
        backup = BATCH2_ASSETS / "pre-brand-backup" / slug
        n = apply_brand_to_guide(slug, IMG, backup_dir=BATCH2_ASSETS / "pre-brand-backup", pristine_dir=backup)
        if n:
            print(f"{slug}: branded {n} images")
            for role_path in sorted(IMG.glob(f"{slug}-*.webp")):
                bak = BATCH2_ASSETS / role_path.name
                if role_path.exists():
                    shutil.copy2(role_path, bak)
            total += n
        else:
            print(f"{slug}: no images found")
    print(f"Done — {total} images branded with official logos.")


if __name__ == "__main__":
    main()
