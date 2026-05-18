#!/usr/bin/env python3
"""Generate assets/icon.ico for the Notes app.

Run once before building:  python create_icon.py
Requires Pillow:           pip install pillow
"""
import os
from PIL import Image, ImageDraw


def make_icon(dest: str = "assets/icon.ico") -> None:
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    # Draw at 256x256 then let Pillow downscale for smaller ICO frames.
    size = 256
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d    = ImageDraw.Draw(img)

    # Rounded-rectangle background in the app's muted purple
    pad, radius = 16, 40
    d.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=radius,
        fill=(155, 127, 189, 255),
    )

    # Three white horizontal lines  ── notepad metaphor
    lx0, lx1 = 72, 184
    lh        = 14
    for y in (90, 124, 158):
        d.rectangle([lx0, y, lx1, y + lh], fill=(255, 255, 255, 220))

    # Shorter fourth line (suggests more content)
    d.rectangle([lx0, 192, lx0 + 60, 192 + lh], fill=(255, 255, 255, 140))

    img.save(
        dest,
        format="ICO",
        sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)],
    )
    print(f"Icon written to {dest}")


if __name__ == "__main__":
    make_icon()
