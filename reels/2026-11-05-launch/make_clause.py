"""The contract beat: the clause lifted onto its own panel, the page blurred.

She asked for a zoom on "ten (10) business days" and "May 3, 2027". A straight
crop cannot do it: the clause is three full-width lines of a letter-size page
rendered on a phone, so cropping tight enough to enlarge the type clips the
ends of the lines, and a crop wide enough to keep them is barely a zoom at all.

So this uses the house technique instead — isolate rather than magnify: lift
the passage onto its own panel and throw the rest of the frame out of focus
hard. At a light blur the same sentence stays legible behind the panel and the
frame reads as two copies of itself, so the blur is heavy on purpose.

The band coordinates are measured off the frame, not guessed, and asserted
against what the OCR-free check can see: the panel must land inside the frame
and clear the bottom 25%.
"""
import os
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
BEATS = os.path.join(HERE, "build", "beats")
SRC = os.environ.get(
    "LAUNCH_SRC",
    "/tmp/claude-0/-home-user-eventplannersai/"
    "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/nov5")

W, H = 1080, 1920

# In the 1206x2144 cropped source frame: the three lines of clause 4 that carry
# "...is due no later than ten (10) business days before the event date."
BAND = (146, 968, 1064, 1072)
PANEL_Y = 840


def main():
    full = Image.open(os.path.join(SRC, "full6.png")).convert("RGB")
    assert full.size == (1206, 2144), f"unexpected source frame {full.size}"
    base = full.resize((W, H), Image.LANCZOS)

    blurred = base.filter(ImageFilter.GaussianBlur(14))

    sx, sy = W / 1206, H / 2144
    box = (int(BAND[0] * sx), int(BAND[1] * sy), int(BAND[2] * sx), int(BAND[3] * sy))
    band = base.crop(box)
    scale = (W - 64) / band.size[0]
    band = band.resize((int(band.size[0] * scale), int(band.size[1] * scale)),
                       Image.LANCZOS)

    pad = 26
    panel = Image.new("RGB", (band.size[0] + pad * 2, band.size[1] + pad * 2), "white")
    panel.paste(band, (pad, pad))

    x = (W - panel.size[0]) // 2
    assert x >= 0, "panel wider than the frame"
    assert PANEL_Y + panel.size[1] <= 1440, (
        f"panel runs into the bottom 25%: ends at {PANEL_Y + panel.size[1]}")

    out = blurred.copy()
    shadow = Image.new("RGB", (panel.size[0] + 12, panel.size[1] + 12), (90, 86, 120))
    out.paste(shadow, (x - 6, PANEL_Y - 6))
    out.paste(panel, (x, PANEL_Y))
    out.save(os.path.join(BEATS, "b6-clause.png"))
    print(f"b6-clause.png  panel {panel.size[0]}x{panel.size[1]} at y={PANEL_Y}, "
          f"band scaled {scale:.2f}x")


if __name__ == "__main__":
    main()
