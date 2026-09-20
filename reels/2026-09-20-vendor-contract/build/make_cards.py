import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards")
os.makedirs(OUT, exist_ok=True)

def card(lines, fontsize, center_y, name, pad_x=54, pad_y=46, radius=34,
         bg=(0,0,0,196), fg=(255,255,255,255)):
    img = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, fontsize); lh = int(fontsize*1.30)
    widths = [d.textbbox((0,0),l,font=f)[2]-d.textbbox((0,0),l,font=f)[0] for l in lines]
    box_w = max(widths)+pad_x*2; box_h = lh*(len(lines)-1)+fontsize+pad_y*2
    x0, y0 = (W-box_w)//2, center_y-box_h//2
    d.rounded_rectangle([x0,y0,x0+box_w,y0+box_h], radius=radius, fill=bg)
    ty = y0+pad_y
    for l in lines:
        bb = d.textbbox((0,0),l,font=f)
        d.text(((W-(bb[2]-bb[0]))//2-bb[0], ty-bb[1]), l, font=f, fill=fg); ty += lh
    img.save(os.path.join(OUT,name))
    print(f"{name}: {box_w}x{box_h}  y {y0}-{y0+box_h}  widest line {max(widths)}px")

# Instagram hook - brief's wording minus the page count (contract is 5 pages,
# not twelve; author chose to drop the number rather than correct it).
# "page one" keeps the concrete detail the hook rule asks for.
card(["This is a real vendor contract.","Most people never read","past page one."], 60, 940, "hook_ig.png")
# TikTok hook - command style, same concrete detail
card(["Stop signing vendor contracts","you haven't read past","page one."], 60, 940, "hook_tt.png")
# End card - verbatim from the brief. Opaque fill: it lands over a dense
# flagged-issues list, and at alpha 196 that text bleeds through (Sep 19).
card(["Save this before your next","contract signing."], 60, 1330, "endcard.png",
     bg=(0,0,0,240))
