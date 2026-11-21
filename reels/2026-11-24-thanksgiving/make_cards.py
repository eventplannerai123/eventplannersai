"""The single held overlay for the Tue 24 Nov Thanksgiving Reel.

The Oct 29 food-quantities format, which the Tue 24 brief points at: one
piece of her own footage, ONE overlay held for the whole clip, a short Eryn
voiceover, no screen recording and no demo file. So there is one card here,
not a hook and an end card.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.

**IT HAS TO WORK OVER THREE DIFFERENT SHOTS**, because it never leaves the
screen: a steaming pan on a dark hob, a pan across a laid table, and a roast
turkey on a white platter. Opaque, and in the lower third — the food is in
the middle of all three frames, and the bottom 25% is where TikTok's caption
and buttons sit, so y=1140 is the band that is busy in none of them.
`preview()` in render.py composites it onto all three before anything is
exported.

NO CTA. The caption ends on a question; the frame does not ask for anything.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "cards")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
P600 = os.path.join(FONTS, "Poppins-600.ttf")

# Two cuts, and on this format the held overlay IS the hook, so the overlay
# is the only thing that differs. Instagram takes the brief's line; TikTok
# takes a command-style one, as the structure rules require.
TEXTS = {
    "instagram": "Thanksgiving for 20.\nThe headcount is the easy part.",
    "tiktok": "Thanksgiving for 20.\nStop starting with the headcount.",
}
TOP, PX = 1140, 50
PAD_X, PAD_Y = 44, 34
FLOOR = 1440


def card(text, px):
    f = ImageFont.truetype(P600, px)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines = text.split("\n")
    lw = max(probe.textlength(l, font=f) for l in lines)
    lh = int(px * 1.30)
    w, h = int(lw) + PAD_X * 2, lh * len(lines) + PAD_Y * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=LAVENDER + (255,))
    y = PAD_Y
    for l in lines:
        d.text(((w - d.textlength(l, font=f)) / 2, y), l, font=f, fill=PURPLE)
        y += lh
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    # One overlay per cut, held. The brief says so, and a second card on an
    # 8-second clip would be on screen for about three seconds each.
    assert TEXTS["instagram"] != TEXTS["tiktok"], "the two cuts must differ"
    for name, text in TEXTS.items():
        assert text.count("\n") == 1, f"{name}: two lines"
        assert "BUDGET" not in text and "Comment" not in text, f"{name}: no CTA"
        c = card(text, PX)
        bottom = TOP + c.size[1]
        assert TOP >= 240, f"{name} starts at {TOP}, inside the top 12%"
        assert bottom <= FLOOR, f"{name} ends at {bottom}, past {FLOOR}"
        assert c.size[0] <= W - 40, f"{name} is wider than the frame ({c.size[0]})"
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, TOP), c)
        frame.save(os.path.join(OUT, f"held-{name}.png"))
        print(f"held-{name} {c.size[0]}x{c.size[1]} at y={TOP}, bottom {bottom}")


if __name__ == "__main__":
    main()
