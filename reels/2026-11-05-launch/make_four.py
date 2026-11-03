"""The opening beat: Vendor, Amount, Due date and Flag, all four together.

Her note, Nov 3: "Open on Vendor | Amount | Due date | Flag together, not the
Days/Flag columns alone."

THEY DO NOT FIT ON HER PHONE IN PORTRAIT. Hiding every other column and
narrowing the four still left them wider than the screen — two recordings
proved it, both of which pan across rather than showing the four at once. She
turned the phone sideways, which fits them, and that is the take this beat
comes from: the capture stays 1206x2622 with the content rotated inside it, so
it is rotated back with `transpose=2` and the table lifted out of it.

The result is a wide band rather than a full frame, which is simply what a
four-column table looks like when it has to fit 1080 across. It sits on a
blurred copy of the same frame — the same isolate-rather-than-magnify
treatment as the contract clause, so the two beats look like one piece.

The crop is measured off the frame: the lavender header runs x 370-2143, and
the table's own gridlines put its top at y=207.
"""
import os
import subprocess
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
BEATS = os.path.join(HERE, "build", "beats")
SRC = os.environ.get(
    "LAUNCH_SRC",
    "/tmp/claude-0/-home-user-eventplannersai/"
    "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/nov5")

W, H = 1080, 1920
TABLE = (359, 200, 2140, 800)      # in the rotated 2622x1206 frame
BAND_Y = 620                        # top of the band in the output frame


def frame(t, dst):
    subprocess.run(
        ["ffmpeg", "-v", "error", "-i", os.path.join(SRC, "four2.mp4"),
         "-ss", f"{t}", "-frames:v", "1", "-vf", "transpose=2", dst, "-y"],
        check=True)


def build(t, name):
    tmp = os.path.join(BEATS, f"_rot{name}.png")
    frame(t, tmp)
    rot = Image.open(tmp).convert("RGB")
    assert rot.size == (2622, 1206), f"unexpected rotated size {rot.size}"

    # Background: the same frame, covering the output, blurred hard.
    scale = max(W / rot.size[0], H / rot.size[1])
    big = rot.resize((int(rot.size[0] * scale), int(rot.size[1] * scale)), Image.LANCZOS)
    bx, by = (big.size[0] - W) // 2, (big.size[1] - H) // 2
    bg = big.crop((bx, by, bx + W, by + H)).filter(ImageFilter.GaussianBlur(16))

    band = rot.crop(TABLE)
    s = (W - 40) / band.size[0]
    band = band.resize((int(band.size[0] * s), int(band.size[1] * s)), Image.LANCZOS)
    x = (W - band.size[0]) // 2
    assert BAND_Y + band.size[1] <= 1440, (
        f"band runs into the bottom 25%: ends at {BAND_Y + band.size[1]}")

    out = bg.copy()
    out.paste(Image.new("RGB", (band.size[0] + 12, band.size[1] + 12), (90, 86, 120)),
              (x - 6, BAND_Y - 6))
    out.paste(band, (x, BAND_Y))
    out.save(os.path.join(BEATS, name + ".png"))
    os.remove(tmp)
    print(f"{name}.png  band {band.size[0]}x{band.size[1]} at y={BAND_Y}, {s:.2f}x")


def main():
    build(12.0, "b0-four")     # rows 3-7: Fernwood through Harbor Light
    build(16.0, "b7-four")     # rows 15-18: the tail, for the end card


if __name__ == "__main__":
    main()
