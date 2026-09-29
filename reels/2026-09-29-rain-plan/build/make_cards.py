import os
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cards0929"); os.makedirs(OUT,exist_ok=True)
def card(lines,fs,cy,name,px=54,py=46,r=34,bg=(0,0,0,215),fg=(255,255,255,255)):
    img=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(img)
    f=ImageFont.truetype(FONT,fs); lh=int(fs*1.30)
    w=[d.textbbox((0,0),l,font=f)[2]-d.textbbox((0,0),l,font=f)[0] for l in lines]
    bw=max(w)+px*2; bh=lh*(len(lines)-1)+fs+py*2
    x0,y0=(W-bw)//2, cy-bh//2
    d.rounded_rectangle([x0,y0,x0+bw,y0+bh],radius=r,fill=bg)
    ty=y0+py
    for l in lines:
        bb=d.textbbox((0,0),l,font=f)
        d.text(((W-(bb[2]-bb[0]))//2-bb[0], ty-bb[1]),l,font=f,fill=fg); ty+=lh
    img.save(os.path.join(OUT,name)); print(f"{name}: y {y0}-{y0+bh}")
# Instagram's hook is verbatim from the guide; TikTok's is the command-style
# counterpart, naming the square footage because the transformation is a
# 14,250 sq ft lawn collapsing into a 3,800 sq ft hall.
card(["Rained out at 9am.","Doors at 6."],66,620,"hook_ig.png")
card(["Stop winging the rain plan.","14,250 sq ft into 3,800."],56,620,"hook_tt.png")
