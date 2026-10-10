import os
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cards1010"); os.makedirs(OUT,exist_ok=True)

# Oct 5 safe zones: nothing important in the top 12% (y<230) or bottom 25%
# (y>1440). Asserted, not trusted.
SAFE_TOP, SAFE_BOT = int(H*0.12), int(H*0.75)
AMBER = (255, 206, 74, 125)

def canvas(): return Image.new("RGBA",(W,H),(0,0,0,0))

def highlight(img, box, name=""):
    """Amber wash over a line of the answer. Boxes were read off exported
    output-scale frames with a pixel grid, never estimated from the source."""
    x0,y0,x1,y1 = box
    assert y0>=SAFE_TOP and y1<=SAFE_BOT, f"{name} highlight outside safe band: {y0}-{y1}"
    d=ImageDraw.Draw(img,"RGBA")
    d.rounded_rectangle([x0,y0,x1,y1],radius=18,fill=AMBER)
    print(f"  highlight {name}: y {y0}-{y1} ({y0/H:.0%}-{y1/H:.0%} of frame), "
          f"x {x0}-{x1} ({(x1-x0)/W:.0%} of width)")

def card(img,lines,fs,cy,name,px=48,py=40,r=30,bg=(0,0,0,220),fg=(255,255,255,255)):
    d=ImageDraw.Draw(img,"RGBA")
    f=ImageFont.truetype(FONT,fs); lh=int(fs*1.28)
    w=[d.textbbox((0,0),l,font=f)[2]-d.textbbox((0,0),l,font=f)[0] for l in lines]
    bw=max(w)+px*2; bh=lh*(len(lines)-1)+fs+py*2
    x0,y0=(W-bw)//2, cy-bh//2
    assert y0>=SAFE_TOP and y0+bh<=SAFE_BOT, f"{name} card outside safe band: {y0}-{y0+bh}"
    d.rounded_rectangle([x0,y0,x0+bw,y0+bh],radius=r,fill=bg)
    ty=y0+py
    for l in lines:
        bb=d.textbbox((0,0),l,font=f)
        d.text(((W-(bb[2]-bb[0]))//2-bb[0], ty-bb[1]),l,font=f,fill=fg); ty+=lh
    print(f"  card {name}: y {y0}-{y0+bh}")

# --- Beat 1: the prompt, with an overlay saying what was asked -------------
# The bubble fills the frame top to bottom, so there is no empty space to put
# a card in. The card goes over the opening two lines and carries the same
# information they do ("Doors open at 7pm for a 200-person evening event"),
# and the operative sentence - the actual ask - is highlighted instead.
print("beat 1")
b1=canvas()
card(b1,["Doors at 7pm. 200 guests.","Six vendors."],68,355,"setup")
highlight(b1,(240,1135,1020,1300),"the ask")
b1.save(os.path.join(OUT,"b1.png"))

# --- Beat 2: first vendor in -----------------------------------------------
print("beat 2")
b2=canvas()
highlight(b2,(55,930,985,1105),"1:00 PM rentals, first in")
b2.save(os.path.join(OUT,"b2.png"))

# --- Beat 3: the key rule ---------------------------------------------------
print("beat 3")
b3=canvas()
highlight(b3,(20,775,1030,1000),"key rule")
b3.save(os.path.join(OUT,"b3.png"))

# --- Beat 4: the takeaway ---------------------------------------------------
# Sits over the 2:30 bar-team row, dimmed, so the overlay is the biggest thing
# on screen as the format requires.
print("beat 4")
b4=canvas()
ImageDraw.Draw(b4,"RGBA").rectangle([0,0,W,H],fill=(0,0,0,150))
card(b4,["Doors at 7.","First vendor in at 1."],92,830,"takeaway")
b4.save(os.path.join(OUT,"b4.png"))
