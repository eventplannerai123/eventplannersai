# Mon 9 Nov 2026 — The catering invoice, $1,140 over

**Instagram Reel, 6:30pm Eastern (23:30 UTC).** Also to Facebook. TikTok is
hers, and from Mon 9 it goes up **at 9am, before the Instagram post** — her
Sun 8 decision — so this cut had to be approved the evening before.

A redo of the Sep 23 catering invoice Reel (reach 30, morning). The original
stays up.

| | |
| --- | --- |
| Instagram | `catering-invoice-instagram.mp4` — 17.360s, 1080x1920, 1,792,751 bytes |
| TikTok | `catering-invoice-tiktok.mp4` — 17.360s, 1080x1920, 1,791,948 bytes |
| Audio | Eryn only, **-14.0 LUFS / -4.1 dBTP** on the Instagram export |

## The twist came from the answer, not from her

The brief predicted it the other way round: "It will find all three, but it
will probably call the four extra guests an overcharge. The guarantee is a
minimum… That's the likely catch."

It did not need catching. ChatGPT made the distinction itself, in its own
words on screen: *"The $500 additional guest charge is contractually supported
if 124 guests were actually served. The invoice says the count came from the
banquet captain, but the count should be verified."* So its headline figure is
**$530 disputed**, not $1,140 — the $420 cake fee the BEO waives and the $110
bar extension nobody signed for, and nothing else.

Both numbers are true and the piece needs both: the invoice **is** $1,140 over
the signed BEO ($18,300 against $19,440, which its own reconciliation shows),
and **$530** is the part worth arguing about. The hook carries the big number,
the end of the cut carries the real one.

The guide's line says CC rewrites the last voiceover line, the takeaway
overlay and the caption's second paragraph around what she actually caught.
All three are rewritten — around what the answer caught.

## Her recording

Drive `November 9`, `1JkeOVn2IB2cLgCZKF3JZ_H4kW-wykCgi` — 75,072,670 bytes,
1206x2622, 120fps, 41.14s. Read from the scratchpad, never committed: the repo
is public.

`crop=1206:2144:0:478` then scale to 1080x1920, recomputed from the source
rather than pasted.

**Ad check: clean.** Two passes at 2fps over the bottom 420px of the whole
41s, and the bottom strip of the exports to the final frame. Nothing from any
of the nine known advertisers and nothing new — the answer runs straight into
its own email draft with no sponsored line.

## Build

Six freeze frames, no scrolling:

| Beat | Source t | What it shows |
| --- | --- | --- |
| b0-prompt | 2.60s | the sent prompt bubble with both PDFs attached |
| b1-530 | 14.60s | "three billing discrepancies" and **$530.00** |
| b2-table | 19.50s | the discrepancy table, line by line |
| b3-minimum | 25.00s | "the guarantee is a minimum, not a cap" |
| b4-recon | 30.00s | $18,300 / $19,440 / **+$1,140** |
| b5-dispute | 36.50s | "Amount to dispute **$530.00**" |

**Time to payoff is 2.40s** on Instagram and 2.20s on TikTok — beat 1 carries
$530, well inside the 6-second ceiling. A 4% slow push per beat keeps the
frame moving from frame one.

Card placement measured off a y-ruler: the prompt bubble on b0 ends at y=1180
and TikTok's bottom furniture starts at 1440, so the hook sits at 1190, over
the answer's opening line rather than over the prompt. The end card sits at
780 on b5 because "Amount to dispute $530.00" is at y=400 and the push lifts
everything ~77px — it covers only the email draft.

**The end card is the BUDGET line and it substitutes.** The guide's Nov 3 soft
mention says to end this Reel on "Comment BUDGET for the tracker I use"
*instead of* the usual closing line, so the guide's own takeaway overlay is
replaced rather than appended to. TikTok says "on my Instagram" — no bio link
there, and the automation lives on Instagram. It is the second of the four the
free ManyChat plan allows (Thu 5, Mon 9, Tue 10, Tue 17).

## Voiceover

55 words, 17.36s — 3.17 w/s, right on Eryn's planning figure. Raw came out at
**-24.0 LUFS / -1.7 dBTP**; **+12.0 dB** then `alimiter=limit=0.841:level=0`
measured -14.0. Swept across six renders rather than computed.

The mp3 came back through Drive, because `elevenlabsusercontent.com` is
blocked from this session.

## Checks run on the exports

- Prompt readable at 0.5s and 2.0s with the hook below it; hook gone by 2.6s.
- Payoff ($530.00, "three billing discrepancies") on screen at 2.6s.
- End card visible at 14.5s and 17.2s with "Amount to dispute $530.00" still
  readable above it.
- 1080x1920, 30fps, H.264, AAC 192k/48kHz, `+faststart`.

## Still open

Her YOU line asks for **the one thing she would still change** about the
answer. She has not said yet. If it changes the reading, the last voiceover
line and the caption's second paragraph are the two places to redo.

## Live

| | |
| --- | --- |
| Instagram | https://www.instagram.com/reel/DfihO2fGId7/ — 6:32pm Eastern, Mon 9 Nov |
| Facebook | video post `1786931315872496` |
| TikTok | hers, posted 9:20am from the file sent Sun 8 — 123 views by the evening |

Posted from here on the scheduled 6:30pm task. Instagram's media edge was
read first and showed the 12:32pm planner-feelings image as the newest item,
and the Facebook feed showed the same, so nothing was duplicated. The live
Instagram caption was read back and diffed against `build/caption.txt`
character for character — identical.

**No BUDGET comments before the automation went live**: the Reel's comment
edge was empty when it was read straight after publishing, so nobody is owed
a manual DM.

**Automation count, corrected.** This is the second of the four the free
ManyChat plan allows, and the plan was Thu 5, Mon 9, Tue 10, Tue 17. Tue 10
came off that list the same afternoon — Sahiba dropped the BUDGET CTA from
the insurance Reel because the tracker is deposits and balances and that
piece is an insurance certificate — so after tonight it is **Thu 5, Mon 9
and Tue 17, with one slot free**.
