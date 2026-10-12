import os
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cards1012"); os.makedirs(OUT,exist_ok=True)

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

# Beat 1 overlays: the hook, over the prompt. Two versions - the TikTok cut
# takes a command-style line, per the standing rule.
for tag, lines in (("instagram", ["31 things to confirm.","The wifi one won't save you."]),
                   ("tiktok",    ["Stop asking venues","if they have wifi."])):
    print(f"beat 1 ({tag})")
    b1=canvas(); card(b1, lines, 64, 480, f"hook-{tag}")
    b1.save(os.path.join(OUT,f"b1-{tag}.png"))

# Beat 2: the scale of the checklist.
print("beat 2")
b2=canvas(); highlight(b2,(50,660,1020,765),"follow-up tracker, 0 of 31")
b2.save(os.path.join(OUT,"b2.png"))

# Beat 3: the catch. This is the whole piece - the line is on screen, so the
# claim in the voiceover is checkable rather than asserted.
print("beat 3")
b3=canvas(); highlight(b3,(45,885,1010,1105),"power access, internet/Wi-Fi")
b3.save(os.path.join(OUT,"b3.png"))

# Beat 4: the takeaway, over the end of the brief, dimmed.
print("beat 4")
b4=canvas()
ImageDraw.Draw(b4,"RGBA").rectangle([0,0,W,H],fill=(0,0,0,155))
card(b4,["It asked if there's wifi.","Not if your laptops","can get on it."],72,900,"takeaway")
b4.save(os.path.join(OUT,"b4.png"))
