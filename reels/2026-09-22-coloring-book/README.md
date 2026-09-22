# Coloring book reel — 2026-09-22

Status: **built, not posted.** Awaiting approval in the conversation.

The piece for *The Calm Before the Aisle*, a 50-page coloring book made with
AI. Built from `reel_script_1.txt` plus the day's uploads. The script's own
target — **35-45 seconds** — overrides the pre-Sep-23 standing target of
16-20s, per the guide's "a day's brief still overrides both".

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
`+faststart`, AAC 192k at 48 kHz.

| File | Platform | Duration | Voiceover | Ramp | Reveal held |
| --- | --- | --- | --- | --- | --- |
| `coloringbook-instagram.mp4` | Instagram, Facebook | 44.00s | -14.13 LUFS, TP -1.20 | 3.0x, 3.20s | 2.10s |
| `coloringbook-tiktok.mp4` | TikTok (manual upload) | 37.50s | -14.11 LUFS, TP -1.34 | 3.0x, 2.80s | 2.65s |

Two separate voiceovers, not one audio reused. Opening lines:

- Instagram: "This is a 50-page coloring book. I made it with AI. Here's
  what that actually took."
- TikTok: "Stop thinking AI does the whole job. I made a 50-page coloring
  book with AI in under three weeks."

End cards: "The Calm Before the Aisle / Printable version in my bio" on
Instagram, "The Calm Before the Aisle / On Etsy" on TikTok.

## TikTok has no bio link

Flagged by the author mid-build. The Instagram voiceover ends "Link in
bio"; TikTok profiles don't carry one, so the TikTok cut was given its own
voiceover ending on "The Calm Before the Aisle. On Etsy." and its own end
card and caption to match. This is why the two cuts differ by more than the
usual hook swap.

"Printable version in my bio" is allowed on Instagram only because the
author confirmed on 2026-09-22 that the bio now points at the book. The
guide reserves that wording for downloadable files behind a live bio link.

## Time to payoff — read this before posting

The 6-second ceiling does not map cleanly onto this piece, and the answer
depends on what counts as the payoff.

- **The book is the payoff, and it is on screen at 0:00.** The reel opens
  on the finished physical book being flipped, which is the thing being
  sold. On that reading, time to payoff is 0.0s.
- **The ChatGPT reveal is the payoff.** On that reading it is **12.85s**
  (Instagram) and **11.25s** (TikTok), which breaks the ceiling badly.

The order is fixed by the voiceover, which narrates the book first and the
tooling second, so the screen-recording reveal cannot be moved earlier
without a different script. Recorded here rather than buried: if the second
reading is the right one, this needs a restructure, not a trim.

## Overlays — two only

The script asks for a text card on every one of its five beats, including
the two number cards ("The app's images: about $9" / "The app itself:
$183"). Those were **not** built. The guide allows only the hook at
0:00-0:02 and the end card, and calls out mid-video captions specifically
as tested and worse for retention. The numbers are spoken in the voiceover
and written in the caption instead.

## The flip footage and the visible monitor

Three clips of the book being flipped were uploaded. Two of them
(`IMG_4033`, both takes) show a laptop monitor behind the book displaying
**this conversation, legibly** — including the author's own messages. A
200px top crop was tried and did not fix it: the text is still readable at
4.2s and later, well into mid-frame.

Neither `IMG_4033` take is used. The hook is `IMG_4030` instead, which is
clean — the book on a tiled floor, no screen anywhere in shot. It is
landscape 1458x1080 with rotation -180, so the 9:16 slice is
`crop=608:1080:850:0` upscaled 1.78x to 1080x1920. Checked at full size:
the line art stays sharp.

## The in-app ad

An **Adobe Firefly** ad scrolls into the bottom of frame during the reveal
clip. Bottom-strip frames at 0.2s steps: **clean at 6.4s, "Adobe Firefly
… Ad" legible at 6.6s.** The reveal cuts at **6.30s** on both cuts, with
margin, because the logo fades in — the Sep 21 lesson.

Verified **visually**, not by colour threshold, on the finished files: the
bottom 400px of every frame across the last 1.2s of each cut's reveal,
including the held frames. No ad in either.

## Structure

Ten segments. Instagram timings; TikTok is the same shape, tighter.

| # | Source | Out | What |
| --- | --- | --- | --- |
| 1 | IMG_4030 0.00-6.55 | 0.00-6.55 | Book flipping. Hook card 0.0-2.0. |
| 2 | long SR 0.00-1.60 | 6.55-8.15 | Prompt in the box, send tap on camera. |
| 3 | long SR 1.60-11.20 @3x | 8.15-11.35 | Generating. |
| 4 | short SR 3.55-6.30 | 11.35-14.12 | "Finishing up" into the reveal. |
| 5 | freeze of short SR 6.28 | 14.12-14.95 | Holds the finished page. |
| 6 | contact sheet, z 1.10-1.75 | 14.95-21.22 | All 50 pages, push in. |
| 7 | IMG_3940, push in | 21.22-26.08 | Proof copy on tile, part-coloured. |
| 8 | contact sheet, pan | 26.08-31.52 | Close across individual pages. |
| 9 | IMG_3939, push in | 31.52-37.08 | Hand holding the book open. |
| 10 | IMG_3927, push in | 37.08-44.00 | Half-coloured page and pencils. End card from 40.80. |

Cuts land on the narration's beat boundaries, taken from a Scribe
transcript of the finished voiceover cross-checked against a silence map
(`silencedetect=noise=-32dB:d=0.28`). The 1.87s of lead-in silence is
trimmed so speech starts at 0.25s.

### Crop

`crop=1206:2144:0:478` for the two screen recordings — recomputed from this
source, not pasted: 1206 / 0.5625 = 2144, and 478 off the top clears the
status bar and the recording dot.

### Representative slice

Flagged per the timing rules. The real generating phase runs past the end
of the long recording — over 16 seconds, visually static the whole way.
Segment 3 is a representative slice of it at 3x, not the whole span
compressed.

### The reveal hold

The generated page resolves at short-SR 5.0s and is then completely static
until the ad arrives at 6.6s, which leaves only 1.2s of live finished
image. Segment 5 freezes the last clean frame so the page is held long
enough to read — 2.10s on Instagram, 2.65s on TikTok. The guide allows a
freeze on a final frame; nothing is faked, the frame is the real one.

## Accuracy

The voiceover was checked line by line against the script's own corrections
record. One line is looser than the script: the voiceover says "12 pages
too thin to print", where the script says twelve pages had **lines** too
thin to print well. The caption carries the precise wording. Worth a
re-record if the author wants it exact — the piece's whole claim is that it
is the honest one.

Everything else matches: three sources not one style block, "under three
weeks" not two, "$9" scoped to the app's images only, "remade by hand in
ChatGPT" not drawn, and Etsy only — Amazon is not confirmed Live.

## Not a prompt piece, but the prompt is in the caption

The reel shows a prompt being pasted, so the caption carries it under
`AI Prompt:` per the caption layout. The spoken and on-card CTA is the book,
not "the full prompt is in the caption below" — this piece is selling the
book, and two CTAs is one too many. Raised rather than decided silently.

## Sources used

| File | Used for |
| --- | --- |
| `b0cb03e7-IMG_4030.mov` | Hook, segment 1 |
| `1448842b-…10-27-15AM_1.mov` (16.86s) | Segments 2-3 |
| `b06cd7cf-…10-27-15AM_1_3.mov` (7.75s) | Segments 4-5 |
| `images/13.webp` (2000x1294, 50 tiles) | Segments 6, 8 |
| `99563f10-IMG_3940.HEIC` | Segment 7 |
| `b447192a-IMG_3939.HEIC` | Segment 9 |
| `b4bc3d31-IMG_3927.HEIC` | Segment 10 |

Unused: both `IMG_4033` takes (visible monitor), the second `IMG_4030`
upload, and `4dba47df-…10-27-15AM_1.mov`, which is a smaller re-encode of
the `b06cd7cf` clip.

## House rules checked

- Transformation format: yes — messy prompt to finished page on screen, and
  the wider before/after of an idea becoming a printed book.
- Wedding-specific pieces in the last seven: this is the first. Under the
  cap of two.
- Both cuts differ; neither goes to the platform the other is for.
- No comment keyword, no "Hashtags:" label, literal `#` in both captions.
- Instagram caption 1633 characters, TikTok 1639 — both well under 2200.
