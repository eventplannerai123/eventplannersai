import os
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cards1014"); os.makedirs(OUT,exist_ok=True)

SAFE_TOP, SAFE_BOT = int(H*0.12), int(H*0.75)
AMBER = (255, 206, 74, 125)

def canvas(): return Image.new("RGBA",(W,H),(0,0,0,0))

def highlight(img, box, name=""):
    x0,y0,x1,y1 = box
    assert y0>=SAFE_TOP and y1<=SAFE_BOT, f"{name} highlight outside safe band: {y0}-{y1}"
    ImageDraw.Draw(img,"RGBA").rounded_rectangle([x0,y0,x1,y1],radius=18,fill=AMBER)
    print(f"  highlight {name}: y {y0}-{y1} ({y0/H:.0%}-{y1/H:.0%}), x {x0}-{x1} ({(x1-x0)/W:.0%} wide)")

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

# Beat 1: the hook, over the prompt. The sent bubble runs y 470-1455, so the
# card sits in the gap above it and covers the PDF attachment chip instead -
# not a word of the prompt. The Instagram line is the guide's verbatim; the
# TikTok cut takes a command-style one, per the standing two-cuts rule.
for tag, lines in (("instagram", ["I sent the AV crew to lunch","during the keynote."]),
                   ("tiktok",    ["Stop assuming the AV schedule","matches the run of show."])):
    print(f"beat 1 ({tag})")
    b1=canvas(); card(b1, lines, 52, 350, f"hook-{tag}", py=30)
    b1.save(os.path.join(OUT,f"b1-{tag}.png"))

# Beat 2: the finding, in ChatGPT's own words. Highlighted so the voiceover's
# claim is checkable on screen rather than asserted.
print("beat 2")
b2=canvas(); highlight(b2,(26,815,1055,1045),"the biggest issue is ... swapped")
b2.save(os.path.join(OUT,"b2.png"))

# Beat 3: the diagnosis. Two headings, far apart, so two highlights rather
# than one box that would swallow the body text between them.
print("beat 3")
b3=canvas()
highlight(b3,(180,300,900,440),"Day 2 crew schedule -> Day 3 production")
highlight(b3,(180,995,900,1135),"Day 3 crew schedule -> Day 2 production")
b3.save(os.path.join(OUT,"b3.png"))

# Beat 4: the takeaway, over the bottom line, dimmed.
print("beat 4")
b4=canvas()
ImageDraw.Draw(b4,"RGBA").rectangle([0,0,W,H],fill=(0,0,0,155))
card(b4,["Check the crew schedule","against the run of show.","Day by day."],68,850,"takeaway")
b4.save(os.path.join(OUT,"b4.png"))
