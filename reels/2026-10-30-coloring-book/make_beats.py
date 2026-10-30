"""Beat frames for the Fri 30 Oct coloring book Reel.

NO FILMING, AND NOTHING INVENTED. Two real sources only:

  * her own photo of the paperback, `IMG_3939.HEIC` in Drive October 30 — the
    open book in her hand at the half-coloured planner's-kit page. The author
    copies arrived, so this is the physical book rather than a mockup.
  * `CalmBeforeTheAisle_interior_102pp.pdf` (Drive 1Ner_-szB1ZOCT3RWsiztpXS06VulJK4l),
    rendered at 200 dpi, one page per beat.

The brief's third source, `story_etsy_book/`, does not exist: the `Coloring
book` folder holds the two PDFs, a `pintrest` subfolder and one test PNG, and
Drive has no folder by that name. Checked again on Oct 30 rather than assumed.

WHY THE PAGES SIT ON LAVENDER INSTEAD OF FILLING THE FRAME. A letter page is
0.773 wide-to-tall and the frame is 0.5625, so filling it crops 231px off each
side of the page. Measured ink margins on the seven chosen pages run from 100px
(page 47) to 298px (page 65) at 200 dpi, so a fill would cut into the drawing on
four of them — page 47 by 131px, which is the walkie-talkie her photo shows her
colouring. The brief says "slow pans across pages"; a pan that amputates the art
is not worth the motion. So the whole page sits on the brand lavender and the
motion is a slow push-in instead, which also leaves clean bands top and bottom
for the hook and the takeaway.
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
DL = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/dl"

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
HAIRLINE = (176, 172, 228)

PAGE_W = 984                      # 48px of lavender each side
PAGES = {
    "dress": "hi/pg17-017.jpg",
    "bouquet": "hi/pg25-025.jpg",
    "kit": "hi/pg47-047.jpg",
    "guestbook": "hi/pg61-061.jpg",
    "ring": "hi/pg3-003.jpg",
    "aisle": "hi/pg57-057.jpg",
    "title": "hi/pg1-001.jpg",
}

# Her photo, cropped to 9:16 from the source width so nothing is stretched.
# Same crop as the Oct 29 Story frames: keeps her hand and the whole coloured
# page. Source is 4284x5712, which is the full-size HEIC rather than the
# downscaled copy that came through chat.
PHOTO_CX, PHOTO_CY, PHOTO_CW = 1242, 133, 3042


def page_beat(src):
    img = Image.new("RGB", (W, H), LAVENDER)
    p = Image.open(os.path.join(DL, src)).convert("RGB")
    ph = round(p.size[1] * PAGE_W / p.size[0])
    p = p.resize((PAGE_W, ph), Image.LANCZOS)
    y = (H - ph) // 2
    img.paste(p, ((W - PAGE_W) // 2, y))
    d = ImageDraw.Draw(img)
    d.rectangle([(W - PAGE_W) // 2 - 1, y - 1,
                 (W + PAGE_W) // 2, y + ph], outline=HAIRLINE, width=2)
    return img


def photo_beat():
    import pillow_heif
    pillow_heif.register_heif_opener()
    im = Image.open(os.path.join(DL, "IMG_3939.HEIC")).convert("RGB")
    ch = round(PHOTO_CW / 0.5625)
    im = im.crop((PHOTO_CX, PHOTO_CY, PHOTO_CX + PHOTO_CW, PHOTO_CY + ch))
    return im.resize((W, H), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    photo_beat().save(os.path.join(OUT, "01-photo.jpg"), quality=95)
    for name, src in PAGES.items():
        page_beat(src).save(os.path.join(OUT, f"{name}.jpg"), quality=95)
        print(name, "ok")
    print("photo ok")


if __name__ == "__main__":
    main()
