from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def card(lines, fontsize, center_y, pad_x=54, pad_y=46, radius=34,
         bg=(0, 0, 0, 196), fg=(255, 255, 255, 255), out="card.png",
         accent=None):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, fontsize)
    lh = int(fontsize * 1.30)

    widths, heights = [], []
    for ln in lines:
        bb = d.textbbox((0, 0), ln, font=f)
        widths.append(bb[2] - bb[0])
        heights.append(bb[3] - bb[1])

    block_w = max(widths)
    block_h = lh * (len(lines) - 1) + fontsize
    box_w = block_w + pad_x * 2
    box_h = block_h + pad_y * 2
    x0 = (W - box_w) // 2
    y0 = center_y - box_h // 2
    d.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=radius, fill=bg)

    if accent:
        d.rounded_rectangle([x0, y0, x0 + 10, y0 + box_h], radius=5, fill=accent)

    ty = y0 + pad_y
    for ln in lines:
        bb = d.textbbox((0, 0), ln, font=f)
        tx = (W - (bb[2] - bb[0])) // 2 - bb[0]
        d.text((tx, ty - bb[1]), ln, font=f, fill=fg)
        ty += lh

    img.save(out)
    print(f"{out}: box {box_w}x{box_h} at y {y0}-{y0+box_h}")

import os
SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards")
os.makedirs(SP, exist_ok=True)

# Instagram hook (verbatim from brief)
card(["A 3pm ceremony means", "the morning starts", "way earlier than", "most people think."],
     70, 940, out=f"{SP}/hook_ig.png")

# TikTok hook - command style
card(["Build your getting-ready", "timeline backward", "from 3pm."],
     70, 940, out=f"{SP}/hook_tt.png")

# End card (same text both versions, per brief)
card(["Save this before your next", "getting-ready timeline."],
     62, 1330, out=f"{SP}/endcard.png")
