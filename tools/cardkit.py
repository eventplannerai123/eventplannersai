"""Shared overlay helpers for the Reels builds.

Why this exists: highlight boxes were being placed by reading a y-ruler off a
contact sheet and typing the numbers in. That is eyeballing, and it has been
wrong more than once — on 2026-10-14 both boxes on one beat landed on body
text because two headings were 700px apart rather than 90, and it was only
caught after a full render. The author asked for them tightened up.

The fix is to stop typing coordinates. `fit_highlight` takes a *seed* — one y
somewhere inside the line you mean — and snaps the box to that line's real ink,
so the edges follow the glyphs instead of a guess. `preview` then composites
every overlay onto its own beat frame so the result is looked at BEFORE the
render, not after.
"""
import os
from PIL import Image, ImageDraw

AMBER = (255, 206, 74, 125)


def _ink_rows(gray, W, thresh, min_frac):
    """Per-row count of dark pixels, as a fraction of width."""
    px = gray.load()
    rows = []
    for y in range(gray.size[1]):
        n = 0
        for x in range(0, W, 2):          # every 2nd column is plenty
            if px[x, y] < thresh:
                n += 1
        rows.append(n * 2 / W)
    return rows


def _lines(frame_path, thresh=140, min_frac=0.004, merge=8):
    """Every text line in the frame, as (top, bottom) row pairs.

    Rows separated by fewer than `merge` blank rows are one line — that bridges
    the split a descender or a dotted i leaves, without joining real lines.
    """
    im = Image.open(frame_path).convert("L")
    W, H = im.size
    px = im.load()
    inked = [sum(1 for x in range(0, W, 2) if px[x, y] < thresh) * 2 / W >= min_frac
             for y in range(H)]
    runs, y = [], 0
    while y < H:
        if inked[y]:
            t = y
            while y < H and inked[y]:
                y += 1
            runs.append([t, y - 1])
        else:
            y += 1
    out = [runs[0]] if runs else []
    for t, b in runs[1:]:
        if t - out[-1][1] - 1 < merge:
            out[-1][1] = b
        else:
            out.append([t, b])
    return im, out


def fit_highlight(frame_path, seed_y, lines=1, up=0, pad_x=16, pad_y=12,
                  thresh=140, name=""):
    """Snap a highlight to whole text lines, counted rather than guessed.

    `seed_y` picks a line; `lines` is how many lines the highlight should cover
    from there, and `up` how many of them sit above the seed. The box is the
    union of those lines' real ink, so its edges follow the glyphs.

    Counting lines replaced an earlier version that grew through blank rows
    until a gap of N. That could not work: on the Oct 14 capture the leading
    inside a heading is 18 rows and inside a body paragraph 33, so any single
    threshold either split a heading or swallowed the next block. The caller
    knows how many lines it means; the frame knows where they are.
    """
    im, runs = _lines(frame_path, thresh=thresh)
    W, H = im.size
    assert runs, f"{name}: no text found in frame"
    i = min(range(len(runs)),
            key=lambda k: 0 if runs[k][0] <= seed_y <= runs[k][1]
            else min(abs(runs[k][0] - seed_y), abs(runs[k][1] - seed_y)))
    lo, hi = i - up, i - up + lines
    assert 0 <= lo and hi <= len(runs), (
        f"{name}: lines={lines}, up={up} from line {i} runs past the frame "
        f"({len(runs)} lines found)")
    top, bot = runs[lo][0], runs[hi - 1][1]

    px = im.load()
    x0, x1 = W, 0
    for y in range(top, bot + 1):
        for x in range(W):
            if px[x, y] < thresh:
                if x < x0: x0 = x
                if x > x1: x1 = x
    assert x1 > x0, f"{name}: no ink between y {top}-{bot}"

    box = (max(0, x0 - pad_x), max(0, top - pad_y),
           min(W - 1, x1 + pad_x), min(H - 1, bot + pad_y))
    print(f"  fit {name}: seed {seed_y} -> line {i}, {lines} line(s), "
          f"y {box[1]}-{box[3]}, x {box[0]}-{box[2]} ({(box[2]-box[0])/W:.0%} wide)")
    return box


def draw_highlight(img, box, safe_top, safe_bot, name=""):
    x0, y0, x1, y1 = box
    assert y0 >= safe_top and y1 <= safe_bot, \
        f"{name} highlight outside safe band: {y0}-{y1}"
    ImageDraw.Draw(img, "RGBA").rounded_rectangle([x0, y0, x1, y1], radius=18, fill=AMBER)


def preview(frames, overlays, out_path, cols=4):
    """Composite each overlay onto its beat frame, side by side.

    Look at this before rendering. It is the step that would have caught the
    Oct 14 beat without burning a full export.
    """
    tiles = []
    for f, o in zip(frames, overlays):
        base = Image.open(f).convert("RGBA")
        base.alpha_composite(Image.open(o).convert("RGBA"))
        tiles.append(base.convert("RGB").resize((320, 569)))
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (320 * min(cols, len(tiles)), 569 * rows), (255, 255, 255))
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % cols) * 320, (i // cols) * 569))
    sheet.save(out_path)
    print(f"  preview -> {out_path}")
    return out_path
