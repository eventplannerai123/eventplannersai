# Catering invoice vs BEO reel — 2026-09-23

Status: **published 2026-09-23.** Approved in conversation ("go ahead and
post"), then posted to Instagram and Facebook.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DdocwZkkyBY/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1761765678094827/ |

Both captions were read back live and diffed against `build/caption.txt` with
`cmp` rather than by eye — **identical byte for byte on both**, md5
`c5f84ae5245eef756e23a709ac06f893`, 697 bytes. Four literal `#`, no
"Hashtags:" label, no comment keyword, no link-in-bio, and none of the retired
`#theeventplannerai`.

The Instagram container (`18092095340367131`) reached FINISHED after 18.9s
over 7 status checks and published first try as media `17863972956680133`.

**Facebook's read-back needed the feed, not the id.** `FACEBOOK_CREATE_VIDEO_POST`
returned `1761765678094827`, and `FACEBOOK_GET_POST` rejected both
`1233196746554445_1761765678094827` (object does not exist) and the bare id
(wrong format). That returned value is the *reel* id, which appears in the
permalink but is not the post id. The actual post id is
`1233196746554445_122111214693449533`, found via `FACEBOOK_GET_PAGE_POSTS` —
which is the duplicate-check path the runbook already specifies. Nothing was
re-posted; the feed shows exactly one copy.

TikTok is not posted from here. `invoice-tiktok.mp4` was handed to the author
for manual upload, per the guide.

Wednesday of Round 6 — a short day in the Sep 23–30 length test (15–20s).
Corporate, not wedding, so the cap of two wedding pieces per seven is
untouched.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
`+faststart`, AAC 192k at 48 kHz. **TikTok was built first**, per the brief —
it is the primary discovery platform now.

| File | Platform | Duration | Voiceover | Ramp | Time to payoff |
| --- | --- | --- | --- | --- | --- |
| `invoice-tiktok.mp4` | TikTok (manual upload) | 15.13s | -13.84 LUFS, TP -1.23 | 2.50x, 2.52s | 4.42s |
| `invoice-instagram.mp4` | Instagram, Facebook | 15.43s | -13.91 LUFS, TP -1.45 | 2.30x, 2.78s | 4.53s |

Opening lines, two separate voiceovers:

- Instagram (author's upload): "Final catering invoice just came in."
- TikTok (generated to match): "Stop paying the final catering invoice on
  trust."

Both then run "Before I pay a cent, I'm checking it line by line against what
we actually signed for. Here's what AI found."

## Overlays — hook only

`Check this before you pay the caterer.` at 0:00–2:00, verbatim from the
brief. **No end card:** Round 6 briefs say "end on the output itself, not an
end card asking for a comment", which overrides the standing two-overlay
default. Both cuts finish on the reconciliation still scrolling.

The hook card sits at y 620, in the gap between the attachment chips and the
input box. At y 880 it covered the prompt and the send button during the tap —
caught on the first render and moved.

## The opening

The recording finally starts the way the guide asks: prompt already typed in
the input box, both PDFs attached, and the **send tap on camera at 0.2s**.
Verified frame by frame on the finished file, not assumed.

## The in-app ad

Not Adobe Acrobat this time — a **Rillion "AI for Accounts Payable"** card,
with the line "For invoice line checks and AP automation, here's one software
option." In clip B it is clean at **9.1s** and legible at **9.4s**. The reveal
cuts at **9.00s**, with margin, because these fade in.

Verified visually on the finished files across the last 1.2s of each cut —
bottom 420px, no ad in either. Clip C is clean to its end; nothing had loaded.

## Structure

Instagram timings; TikTok is the same shape, tighter.

| # | Source | On screen | Out |
| --- | --- | --- | --- |
| 1 | A 0.00–1.75 | Prompt in the box, both PDFs attached, send tap | 0.00–1.75 |
| 2 | A 1.85–8.25 @2.3x | Generating | 1.75–4.53 |
| 3 | C 2.00–6.20 | Bottom line — $87,521.70 → $83,165.11, **$4,356.59** | 4.53–8.73 |
| 4 | C 6.20–9.80 | Itemised BEO mismatches, corn dog billed twice | 8.73–12.33 |
| 5 | B 5.90–9.00 | Final reconciliation, credit due | 12.33–15.43 |

### Crop

`crop=1206:2144:0:478` — recomputed from this source as the brief specifies:
1206 / 0.5625 = 2144, and 478 off the top clears the status bar and the
recording dot. All three clips are 1206x2622 at 60fps.

### The silent tail

The voiceover is 8.67s of speech against a 15.43s cut. As on Sep 20 and 21,
the tail is the answer **scrolling at normal speed** rather than a freeze —
which is also exactly what "end on the output itself" asks for. The cut is
held to the low end of the 15–20s window because the voiceover is short.

## Accuracy — every flagged item checked against the source PDFs

The standing caveat from the vendor contract piece. Both reference documents
are in `build/`. Checked, not taken on trust:

| Flagged | BEO says | Invoice bills | Verdict |
| --- | --- | --- | --- |
| Service charge | **24%**, stated on all 18 BEO pages | **26%** of Subtotal A | Real |
| Andouille Corn Dog | **once**, 6 dozen @ $108 (10/27) | **twice**, both 10/27 — $648 duplicated | Real |
| Italian Sweets Station | **40** @ $28 = $1,120 | **65** @ $28 = $1,820 → $700 over | Real |
| Lowcountry Boil Buffet | **65** @ $120 | **72** @ $120 → $840 over | Real |
| Riverside Deli Buffet | 23 @ $55 = $1,265 | QTY 23, RATE $55, **AMOUNT $1,365** | Real — $100 arithmetic error |

The reconciliation was rebuilt from the raw PDFs rather than read off the
screen. Section A's 39 line items sum to $61,723.00 exactly as stated and
Section B's 6 to $4,025.00, so the invoice's own arithmetic is sound — it is
the rates and quantities that are wrong. Food overcharges 648 + 700 + 840 +
100 = **$2,288.00**; corrected A of $59,435 x 24% = $14,264.40, so the excess
service charge is **$1,783.58**; corrected tax $5,440.71, a **$285.01**
difference. Corrected total **$83,165.11**, credit due **$4,356.59**. Every
figure on screen reproduces to the cent.

**One caveat worth knowing.** The 10/27 Hospitality function header shows an
expected count of 65, while the priced menu line inside it says 40 @ $28.
ChatGPT used the priced line, and the invoice bills the fruit station from
that same function at 40, so the venue clearly had the 40 figure. But the
header gives a hotel something to argue, and the BEO's guarantee clause says
that absent a final guarantee "the above attendance will be the basis for the
billing charges" — the Gtd column is blank throughout. The $700 is the one
line of the five a venue could push back on. The other four are clean, and
the reel's headline number holds.

## Privacy

Both PDFs were scanned before anything went on screen: no email addresses, no
phone numbers, every contact field a bracketed placeholder
(`[Client Contact]`, `[Catering Manager]`, `[Acct]`), and dietary notes
attributed to "Guest A" through "Guest F". The caption says so outright —
"Demo documents — names changed, and the invoice was built with deliberate
errors."

## Not used

The BEO itself never appears on screen. The author wanted to scroll it during
the recording but an iOS autofill prompt kept firing over the top of frame.
It is not needed for time — 27.4s of usable footage against a 15–20s target —
and Sep 25 reuses the same BEO on a day with room for it.
