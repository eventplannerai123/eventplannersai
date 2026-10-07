# AI makes mistakes, just like us — moved to Fri 9 Oct

The format test: the build-story format rather than a demo. No screen recording
and no ChatGPT prompt — Sahiba off camera over b-roll of real work. Content bank
item 10.

**Status: voiceovers and overlays ready, waiting on footage she films at home.**

## Why it moved off Wed 7

It was built on Wed 7 from her conference b-roll and she rejected it: *"No this
isn't good content."* She was right, and the reason is worth keeping, because
nothing was wrong with the execution.

The guide specs this piece as "over b-roll of real work". At a conference, the
b-roll available is an empty ballroom, a corridor and a drinks table. The piece
is a personal, honest account of checking AI's work on **VIP seating** — and
generic room footage is the opposite of personal. A seating chart on a screen is
what the story is about; a hotel foyer is not. Two cuts were built, both
technically clean, and neither carried the story.

**The lesson is about the spec, not the shoot.** "B-roll of real work" was
written assuming she would be somewhere her real work was visible. When the
piece is about a specific artefact — a seating chart, a floor plan, a budget —
the footage has to show that artefact. Check what the voiceover is actually
about before accepting whatever footage is to hand.

Both cuts were deleted rather than kept, so nobody posts them later by mistake,
and the two copies uploaded to her Drive `October 7` folder were trashed the
same day — a cut sitting in a day folder reads as a day that shipped.

**Wed 7 Oct therefore has no Instagram post.** Her decision, taken knowingly: it
costs one of three Instagram posts that week, which weakens the Oct 14 reach
comparison slightly. Fri 9's Headcount piece moves to the following week.

## What survives, and is still correct

Nothing here depends on the footage.

- `voiceover/vo-instagram-raw.mp3` — 15.49s, 47 words, the guide's script verbatim
- `voiceover/vo-tiktok-raw.mp3` — 15.18s, 46 words, opening line only changed
- `build/cards1007/` — both hook overlays
- `build/caption.txt` — the guide's caption, no `AI Prompt:` line, because this
  piece is not a demo
- `build/render.py` — beats, dissolves, loudness handling

Only the beat list's sources change when the new footage arrives.

## What the new footage needs to show

Vertical, 1080p/30, shot at home. Roughly 25 seconds of usable material, sent
through Drive at Actual/Original size.

- A seating chart or table plan open on screen, names legible
- A hand moving a name, or scrolling the chart — the checking itself
- A wide of the desk with the chart on screen

Her off camera throughout. No faces, no client names, no company names visible
on the chart — use a dummy or an old anonymised one.

## Render notes worth keeping from the Wed 7 build

- **`ffprobe` width/height lies about phone clips.** Both her .mov files
  reported 1920x1080 and read as landscape, which would have meant a 608-wide
  centre slice upscaled 1.78x. They carry `rotation=-90` and decode as
  1080x1920 — already the output frame. Check `stream_side_data=rotation`.
- **Loudness needed two corrections found only by measuring the export.** The
  export read about 1 dB below the voiceover's own first-pass figure, because
  the cut carries its lead-in and tail; `TRIM = 1.10` in `render.py` is that
  measured difference. And at `limit=-1.5dB` the ceiling bound before the gain
  landed, so the limiter sits at **−1.0 dB**.
- **Her raw footage is gitignored.** This repo is public — the
  `raw.githubusercontent.com` URLs Meta and Pinterest fetch from only work
  because it is — so source media with faces, a named venue or third-party
  branding in it does not belong here. A first attempt to commit it was blocked
  as an out-of-place publication, correctly.
