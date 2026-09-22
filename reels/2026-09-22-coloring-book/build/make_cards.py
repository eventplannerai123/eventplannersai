import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards0922r")
os.makedirs(OUT, exist_ok=True)

def card(lines, fontsize, center_y, name, pad_x=54, pad_y=46, radius=34,
         bg=(0,0,0,210), fg=(255,255,255,255)):
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
    print(f"{name}: {box_w}x{box_h}  y {y0}-{y0+box_h}  widest {max(widths)}px")

# Instagram hook - narrative, concrete number + timeframe
card(["I made a 50-page","coloring book with AI","in under 3 weeks."], 62, 900, "hook_ig.png")
# TikTok hook - command style, same concrete numbers
card(["Stop thinking AI does","the whole job.","50 pages. Under 3 weeks."], 56, 900, "hook_tt.png")
# End cards - opaque enough to read over the line art
card(["The Calm Before the Aisle","Printable version in my bio"], 54, 1320, "end_ig.png", bg=(0,0,0,240))
card(["The Calm Before the Aisle","On Etsy"], 58, 1320, "end_tt.png", bg=(0,0,0,240))
