# Coloring book reel — 2026-09-22

Status: **built, not posted.** Awaiting approval in the conversation.

The piece for *The Calm Before the Aisle*, a 50-page coloring book made with
AI.

**Built to `reel_script_1.txt`, not to the master guide.** The author asked
for that explicitly for this post. Where the two disagree, the script wins —
see "What the script overrode" below.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
`+faststart`, AAC 192k at 48 kHz.

| File | Platform | Duration | Voiceover | Ramp | Reveal held |
| --- | --- | --- | --- | --- | --- |
| `coloringbook-instagram.mp4` | Instagram, Facebook | 44.00s | -14.13 LUFS, TP -1.20 | 3.0x, 3.20s | 2.10s |
| `coloringbook-tiktok.mp4` | TikTok (manual upload) | 37.50s | -14.11 LUFS, TP -1.34 | 3.0x, 2.80s | 2.65s |

Two separate voiceovers, not one audio reused.

## What the script overrode

- **Seven text cards, not two.** The script writes a TEXT line into every
  beat and they are all built. The guide allows only a hook and an end card
  and calls mid-video captions out as tested and worse for retention; the
  author set that aside for this post.
- **Length.** The script's 35-45s target, not the pre-Sep-23 16-20s.
- **Time to payoff.** If the payoff is the ChatGPT reveal it lands at 12.85s
  (Instagram) / 11.25s (TikTok), over the 6-second ceiling. The voiceover
  narrates the book first and the tooling second, so the reveal cannot move
  earlier without a different script. If the payoff is the finished book,
  it is on screen at 0:00.
- **Caption.** The script's caption verbatim, with no `AI Prompt:` block —
  the script's caption does not carry one.

The guide's rules on rendering, the ad check and posting approval were kept.

## Cards, verbatim from the script

| Card | Instagram | TikTok |
| --- | --- | --- |
| I made this 50-page coloring book with AI in under three weeks. | 0.00-2.60 | 0.00-2.60 |
| Three tools. One book. | 6.90-10.30 | 5.45-8.60 |
| The app's images: about $9 | 14.95-17.75 | 14.51-17.30 |
| The app itself: $183 | 17.95-23.40 | 17.55-23.30 |
| AI got me 90% there. | 26.15-30.20 | 24.30-26.35 |
| The last 10% is still you. | 33.40-37.00 | 26.55-28.75 |
| Now on Etsy / Amazon coming soon | 40.90-44.00 | 34.80-37.50 |

Two changes to the script's wording, both on the author's instruction:

- The script's beat-1 line is "I made this with AI in under three weeks."
  The author flagged that "this" never names the thing, so the card names it.
- The script says add "+ Amazon" only once it shows Live. The author says
  the print edition is coming shortly, so the card reads **"Amazon coming
  soon"** — true today, and it does not claim a listing that is not there.
  Swap it to "Now on Etsy + Amazon" the day it shows Live.

## TikTok has no bio link

Flagged by the author mid-build. The Instagram voiceover ends "Link in
bio"; TikTok profiles don't carry one, so the TikTok cut was given its own
voiceover ending on "The Calm Before the Aisle. On Etsy." and its own
caption. This is why the two cuts differ by more than a hook swap.

"Printable version in my bio" is on the Instagram caption only, and only
because the author confirmed on 2026-09-22 that the bio now points at the
book.

## The closing shot

The reel ends on the **digital cover** (`build/cover-digital.jpg`), composited
onto a 1080x1920 frame in the cover's own cream (#FBF7EE, sampled from the
file) with a slow push-in. The digital edition is the one that is live and
the one the bio points at, so it is the cover that matches the CTA.

The **print cover wrap** is in `build/CalmBeforeTheAisle_cover_wrap.pdf`
(back cover, spine, front cover, 8.5 x 11 with bleed). Its front panel is the
same bouquet with a different subtitle — "An Adult Coloring Book for Brides,
Bridesmaids & Wedding Planners", "50 INTRICATE PAGES · FOR COLORED PENCIL".
Swap it in once Amazon is Live and the CTA changes.

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

Eleven segments. Instagram timings; TikTok is the same shape, tighter.

| # | Beat | Source | Out |
| --- | --- | --- | --- |
| 1 | 1 | IMG_4030 0.00-6.55 | 0.00-6.55 |
| 2 | 2 | long SR 0.00-1.60 — prompt in the box, send tap on camera | 6.55-8.15 |
| 3 | 2 | long SR 1.60-11.20 @3x — generating | 8.15-11.35 |
| 4 | 2 | short SR 3.55-6.30 — into the reveal | 11.35-14.12 |
| 5 | 2 | freeze of short SR 6.28 | 14.12-14.95 |
| 6 | 3 | contact sheet, z 1.10-1.75 — all 50 pages | 14.95-21.22 |
| 7 | 3 | contact sheet, pan — close across pages | 21.22-26.08 |
| 8 | 4 | IMG_3940, push in — proof copy open | 26.08-31.52 |
| 9 | 4 | IMG_3939, push in — hand on a page | 31.52-37.08 |
| 10 | 5 | IMG_3927, push in — half-coloured page and pencils | 37.08-40.50 |
| 11 | 5 | digital cover, slow push in | 40.50-44.00 |

Shot assignment follows the script's beat list: contact sheet on the money
beat, proof copy open on the 90% beat, pencils page on the payoff. Cuts land
on the narration's beat boundaries, taken from a Scribe transcript of the
finished voiceover cross-checked against a silence map
(`silencedetect=noise=-32dB:d=0.28`). The 1.87s of lead-in silence is
trimmed so speech starts at 0.25s.

### Crop

`crop=1206:2144:0:478` for the two screen recordings — recomputed from this
source, not pasted: 1206 / 0.5625 = 2144, and 478 off the top clears the
status bar and the recording dot.

### Representative slice

The real generating phase runs past the end of the long recording — over 16
seconds, visually static the whole way. Segment 3 is a representative slice
of it at 3x, not the whole span compressed.

### The reveal hold

The generated page resolves at short-SR 5.0s and is then completely static
until the ad arrives at 6.6s, which leaves only 1.2s of live finished
image. Segment 5 freezes the last clean frame so the page is held long
enough to read — 2.10s on Instagram, 2.65s on TikTok. Nothing is faked; the
frame is the real one.

## Accuracy

Checked line by line against the script's own corrections record. One line
is looser than the script: the voiceover says "12 pages too thin to print",
where the script says twelve pages had **lines** too thin to print well. The
caption carries the precise wording. Worth a re-record if the author wants
it exact — the piece's whole claim is that it is the honest one.

Everything else matches: three sources not one style block, "under three
weeks" not two, "$9" scoped to the app's images only, "remade by hand in
ChatGPT" not drawn, and Etsy live with Amazon flagged as coming, not there.

## Sources used

| File | Used for |
| --- | --- |
| `b0cb03e7-IMG_4030.mov` | Beat 1 |
| `1448842b-…10-27-15AM_1.mov` (16.86s) | Beat 2, segments 2-3 |
| `b06cd7cf-…10-27-15AM_1_3.mov` (7.75s) | Beat 2, segments 4-5 |
| `images/13.webp` (2000x1294, 50 tiles) | Beat 3 |
| `99563f10-IMG_3940.HEIC` | Beat 4 |
| `b447192a-IMG_3939.HEIC` | Beat 4 |
| `b4bc3d31-IMG_3927.HEIC` | Beat 5 |
| `images/14.jpg` (2000x2000 digital cover) | Beat 5 close |

Unused: both `IMG_4033` takes (visible monitor), the second `IMG_4030`
upload, `4dba47df-…10-27-15AM_1.mov` (a smaller re-encode of the `b06cd7cf`
clip), and the print cover wrap (held for when Amazon is Live).
