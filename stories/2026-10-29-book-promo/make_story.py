"""The book-promo Instagram Story frame — her Tue 27 / Thu 29 / Fri 30 line.

HER OWN PHOTO, taken Oct 28: the open book in her hand at the half-coloured
walkie-talkie page, which is the first option the guide names. Nothing was
staged or substituted, and the source stays out of the repo (it is gitignored
like every raw file of hers); this script reads it from the Fri 30 reel folder.

Two frames, because the Story carries two link stickers and the guide says to
split them if the app allows only one. Frame 1 carries the approved line and
takes the Paperback sticker; frame 2 is the same picture with no words at all,
for the Printable PDF sticker.

FRAME 2 IS DELIBERATELY TEXTLESS. The obvious thing was to put Friday's line
("Made with AI. Coloured by hand.") on it, and that is wrong: that line belongs
to the Fri 30 Story in the guide, and spending it here would leave Friday
repeating itself two days later. The sticker is the content on that frame.

Safe zones: nothing that matters goes in the top 12% or the bottom 25%. The
line sits just under the top band, over the plain ceiling the photo happens to
carry, which is the only large empty area in the frame. The first build put it
across the middle and the panel covered the coloured clipboard — the one part
of the page she has actually finished, which is the whole point of the picture.
That leaves the bottom quarter clear for the two link stickers.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "reels", "2026-10-30-coloring-book",
                   "source", "book-planners-kit-page.jpg")
FONTS = os.path.join(HERE, "build", "fonts")
OUT = HERE

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)

P600 = os.path.join(FONTS, "Poppins-600.ttf")
P400 = os.path.join(FONTS, "Poppins-400.ttf")

# Crop chosen off the source: keeps her hand at the lower left and the whole
# coloured right-hand page. Computed to 9:16 from the width so nothing is
# stretched — height = width / 0.5625.
CX, CY, CW = 560, 60, 1372
CH = int(CW / 0.5625)

LINE = "For the planner,\nafter the last wedding\nof the season."


def base():
    im = Image.open(SRC).convert("RGB")
    im = im.crop((CX, CY, CX + CW, CY + CH)).resize((W, H), Image.LANCZOS)
    return im


PANEL_X = 56


def scrim(img, top, bottom):
    """Lavender panel behind the text, inset from the edges and rounded."""
    box = (PANEL_X, top, W - PANEL_X, bottom)
    band = img.crop(box).filter(ImageFilter.GaussianBlur(30))
    band = Image.blend(band, Image.new("RGB", band.size, LAVENDER), 0.88)
    mask = Image.new("L", band.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, band.size[0] - 1, band.size[1] - 1], radius=36, fill=255)
    img.paste(band, (PANEL_X, top), mask)
    return img


def frame_one():
    img = base()
    img = scrim(img, 236, 556)
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(P600, 64)
    y = 282
    for ln in LINE.split("\n"):
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=PURPLE)
        y += 86
    return img


def frame_two():
    return base()


def main():
    for name, fn in (("1-paperback", frame_one), ("2-printable", frame_two)):
        img = fn()
        assert img.size == (W, H)
        p = os.path.join(OUT, f"2026-10-29-book-promo-story-{name}.jpg")
        img.save(p, quality=95)
        print(f"{name} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
