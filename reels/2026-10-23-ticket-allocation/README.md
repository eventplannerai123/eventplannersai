# Ticket allocation reel — 2026-10-23

Status: **built, not posted.** Instagram and Facebook run from here after her
go-ahead; the TikTok cut is hers.

| | `ticket-allocation-instagram.mp4` | `ticket-allocation-tiktok.mp4` |
| --- | --- | --- |
| Duration | 19.88s | 19.87s |
| Loudness | −14.31 LUFS, −3.66 dBTP | −14.40 LUFS, −3.78 dBTP |

Both 1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`,
AAC 192k / 48 kHz.

## Three things the first build got wrong

All three were invisible in the filtergraph and only showed up on the exported
frames and a loudness measurement.

**1. A TicketSpice ad on the last frame.** It slides into the bottom of frame
between source 38.0s and 38.5s — "Sell More Tickets Online", "#1 Ticketing
Software" — and the email beat originally ran to 39.18. It is the **eighth**
advertiser seen in these recordings, and the most dangerous so far: a ticketing
ad inside a piece about ticket allocation reads as part of the answer. Every
beat now ends by **37.60**, and both exports were re-checked visually on a
bottom-strip montage through the final frame.

**2. A blank "Loading" frame in the prompt beat.** At source 2.7s she taps the
attachment and the screen goes blank for about 0.7s before the demand sheet
renders. The beat ran to 3.40 and put that on screen. It now takes 0.0–2.60 and
stretches to fill its slot, which on a near-static prompt screen is invisible.

**3. No loudness stage at all.** The voiceover is the only audio, so the first
export measured exactly what ElevenLabs handed over: **−22.3 LUFS** against the
house −14. The two-pass `loudnorm` that replaced it stalled at −16.0 with true
peak at −4.19 — 2.7 dB of headroom it declined to use, so not the documented
true-peak stall. Explicit gain plus `alimiter` (`level=0`) lands it at −14.3.

Content bank **item 4**: the hook and voiceover use only the true story — 2,000
sponsor tickets split across departments, and every department's client was the
most important. **The numbers on screen are demo data**, and the caption says so.

## Her catch is the ending

The Oct 14 review added a twist test to this piece: show the answer, then the
one line she would still change — "genuinely good, except…". That is the shape
of the Oct 12 Reel that reached 83 against a weekly average of 29.

**Her catch, 2026-10-23, verbatim:** "I don't like the answer. It should
highlight clients and prospects as well as internal departments."

She is right, and it is a better catch than the one the brief guessed at. The
brief expected politics — whose guests come off the top, which department head
escalates. What she actually caught is a level above that: the demand sheet is
organised by internal department, the answer allocates the same way, and nobody
in those 2,000 seats is a department. They are clients and prospects, and that
cut never appears anywhere in the output.

It now carries three things, which is what the brief specifies:

| | |
| --- | --- |
| Closing voiceover line | "But it allocated to departments — and those seats are for clients and prospects. That's the split it missed." |
| Takeaway overlay | "Departments don't sit in the seats. Clients do." |
| Caption, second paragraph | the same point in her phrasing |

**The script was held until she said it**, rather than generated to the brief's
guess and rewritten after. That is why no voiceover existed before today.

## Voiceovers

| Cut | File | Length |
| --- | --- | --- |
| Instagram | `voiceover/instagram.mp3` | 19.88s |
| TikTok | `voiceover/tiktok.mp3` | 20.85s |

Vanessa - Beach Girl, `eleven_v4`, two takes each, the shorter of each pair
used. **The TikTok take is 0.85s over the 15-20s target**; it gets a light
`atempo` on the way into the cut rather than a regeneration, the same trick the
Oct 22 rebuild used.

## The demo file is real and checked

`Ticket Demand — Sponsored Arena Event`, built Oct 14, sitting in Drive →
October 23 (file `1aGpioNGMKrgqF2Al7WNShXa928Cp8Wauj3J1kmwEBPY`). Opened and
read here rather than taken on trust:

| Department | Requested | Priority note |
| --- | --- | --- |
| Sales | 700 | "Non-negotiable, these close deals" |
| Marketing | 400 | Need at least 300 for the launch push |
| Partnerships | 350 | Promised to partners last quarter |
| Executive Office | 300 | Must be confirmed first |
| Customer Success | 300 | Retention depends on this |
| HR / People | 250 | Already announced internally |

2,300 requested against 2,000 available — **short by 300**. Every row carries a
priority note that reads as non-negotiable, which is the whole point of the
piece.

## Two hooks and a takeaway

`build/make_cards.py`, all three asserted inside the safe band.

| Cut | Hook |
| --- | --- |
| Instagram | "2,000 tickets. Every department wanted more." — the brief's, verbatim |
| TikTok | "Stop splitting 2,000 tickets by who emails first." — command-style, per the house rule that TikTok's hook is not a derivative of Instagram's |

Plus the takeaway at the end: **"Departments don't sit in the seats. Clients
do."** Two overlays is the written default; the recent briefs cut it to one, and
this piece earns the second back because the twist test needs her line on screen.

**The hook sits at y=1240, not the usual 620.** The cut opens on the finished
allocation table, so a card at 620 would land across the numbers the shot exists
to show. Re-check it against the real opening frames when the recording lands.

## Caption

`build/caption.txt`. The second paragraph is her catch. The brief's "Prompt
below." has been dropped: retired 2026-10-12, and the guide still carries it in
per-day blocks until she edits them.

## Who posts what

| | |
| --- | --- |
| Instagram + Facebook | from here, after her go-ahead |
| TikTok | **hers** — file and caption handed over together, caption pasted into the reply |

## What went out, and when

The slot moved twice. Built for Fri 23, left to lapse when she did not reply,
and then given a date of its own in her 2026-10-25 travel-week calendar: **Mon
26 Oct, 6:30pm Eastern** — "use the existing cut and the Fri 23 caption. It's
on TikTok since Oct 25, never on Instagram." Nothing was re-rendered; the files
are the Oct 23 builds byte for byte.

| | |
| --- | --- |
| TikTok | Sat 25 Oct, by her. Confirmed "tik tok posted". |
| Instagram | Mon 26 Oct 22:32 UTC (6:32pm Eastern), media `18102849353052644`, [reel/De-XKRwGU26](https://www.instagram.com/reel/De-XKRwGU26/), `is_shared_to_feed: true` |
| Facebook | Mon 26 Oct, video post `1129871560001934` |

Posted under the one blanket go-ahead there has ever been — her Oct 25
instruction covering Mon 26 to Wed 28 while she flies — not under the ordinary
ask-and-wait rule, which resumes Thu 29. The 6:30pm slot came from a one-shot
scheduled task firing into the session (`trig_01ScroGDDVUW6oY3FfVLrYVk`), which
read both live accounts before posting: the one thing worse than missing the
slot is filling it twice.

The live Instagram caption was hashed against `build/caption.txt` and matches
character for character, all 811 of them.

**Drive: the piece stays in `October 23`, not `October 26`.** Both cuts, her
screen recording and the demo ticket-demand sheet are already together there
(`2026-10-23-ticket-allocation-instagram.mp4`, Drive id
`1dURHKibAQGHmIUc-Q-sk4uPxp1wgzgFS`, and the TikTok cut beside it), filed on the
day it was built when Oct 23 was still its block. Her rule puts a post's files
on the day the post belongs to, and a second copy in `October 26` would split
one piece across two folders while leaving the source behind — worse than either
folder alone. `October 26` holds the expense-report demo files, which belong to
the Sat 31 piece. Re-parenting cannot run from here in any case:
`mcp__Google_Drive__update_file` takes no `addParents`.
