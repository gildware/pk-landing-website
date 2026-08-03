"""Regenerate favicon PNG/ICO assets from logo-square.png (navy + gold gears on white)."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
SRC = PUBLIC / "logo-square.png"


def main() -> None:
    src = Image.open(SRC).convert("RGBA")

    def save_resized(size: int, name: str) -> None:
        out = PUBLIC / name
        resized = src.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(out, format="PNG", optimize=True)
        print(f"saved {name} ({size}x{size})")

    save_resized(48, "favicon-48x48.png")
    save_resized(96, "favicon-96x96.png")
    save_resized(32, "favicon-light-32x32.png")
    save_resized(500, "favicon-light.png")
    save_resized(180, "apple-touch-icon.png")

    ico_sizes = [16, 32, 48]
    ico_images = [src.resize((s, s), Image.Resampling.LANCZOS) for s in ico_sizes]
    ico_images[0].save(
        PUBLIC / "favicon.ico",
        format="ICO",
        sizes=[(s, s) for s in ico_sizes],
        append_images=ico_images[1:],
    )
    print("saved favicon.ico")


if __name__ == "__main__":
    main()
