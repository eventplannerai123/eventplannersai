import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards0922s")
os.makedirs(OUT, exist_ok=True)

def card(lines, fontsize, center_y, name, pad_x=54, pad_y=46, radius=34,
         bg=(0,0,0,215), fg=(255,255,255,255)):
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
    print(f"{name}: {box_w}x{box_h}  y {y0}-{y0+box_h}")

# Verbatim from reel_script_1.txt, one card per beat as the script lays them out.
# Script text is "I made this with AI in under three weeks." - the author
# flagged that "this" never names the thing, so the card names it.
card(["I made this 50-page","coloring book with AI","in under three weeks."], 58, 900, "c1_hook.png")
card(["Three tools. One book."],                        62, 900, "c2_tools.png")
card(["The app's images:","about $9"],                  72, 960, "c3_images.png")
card(["The app itself: $183"],                          72, 960, "c4_app.png")
card(["AI got me 90% there."],                          64, 1320, "c5_ninety.png", bg=(0,0,0,235))
card(["The last 10% is still you."],                    60, 1320, "c6_ten.png",    bg=(0,0,0,235))
# Script says: add "+ Amazon" only once it shows Live. The author says the
# print edition is coming shortly, so the card says soon, not available.
# Sits just under "50 PAGES - INSTANT DOWNLOAD" on the cover, clear of the
# bottom strip where Instagram puts the username, caption and audio label.
card(["Now on Etsy","Amazon coming soon"],              58, 1440, "c7_end.png",    bg=(0,0,0,240))
