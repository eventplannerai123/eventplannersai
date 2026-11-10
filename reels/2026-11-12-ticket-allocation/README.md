# Thu 12 Nov — 2,000 tickets, 140 seats promised twice

Redo of the Oct 26 ticket allocation Reel, which reached 68; the original
stays up. Instagram + Facebook at 6:30pm Eastern Thursday; TikTok at about
9am, by her hand, from the file sent the evening before.

| | |
| --- | --- |
| Cuts | `ticket-allocation-instagram.mp4`, `ticket-allocation-tiktok.mp4` |
| Length | 18.48s both, inside the brief's 15–20s |
| Export | 1080x1920, ratio 0.5625, 30fps, H.264 high, CRF 19, +faststart |
| Audio | Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), **-14.01 LUFS, -1.20 dBTP** |
| Source | her 1206x2622 iPhone capture, 107.6s, 60fps, no rotation side data |
| Crop | `crop=1206:2144:0:478` then `scale=1080:1920` |
| Fix from last time | the lists are clients and prospects, not departments |

## Two things in the recording that must never reach a frame

Both are asserted in `make_beats.py` rather than remembered, and **neither is
written down anywhere in this repo** — it is public, so recording what to
avoid would publish the thing being avoided.

**An Instagram new-follower notification at about 89–91s.** Sahiba asked for
it cut. It names a private individual and her handle, barred the same way a
client's name is. Measured against the crop: the banner sits at roughly
y 300–470 of the full frame, so `crop=…:478` removes it anyway — but that is
luck rather than a plan, so `NOTIF_WINDOW` keeps every beat clear of it with
two seconds of margin either side.

**The first seconds are the iOS Files app**, listing her own documents — a
résumé among them, and one captioned with someone else's first name.
`START_FLOOR` bars anything that early; in practice the first usable frame is
far later, since the PDF preview runs to about 24s.

## The answer hit every number the brief predicted

| | |
| --- | --- |
| Invitation records | 2,125 |
| People invited twice | 140, each by two different teams |
| Unique invitees | 1,985 |
| Seats left | **15**, at 99.25% utilization |
| On paper | clients 40 over, prospects 85 over, 125 over in total |

It also went one step further than the brief: every duplicate is classified
once as a Client and once as a Prospect, so the total of 1,985 is certain but
the Client-versus-Prospect split cannot be settled without a human. That is
its own "important issue to resolve", and it is why the fifth beat is the
bottom line rather than another table.

## The twist is the brief's predicted one, and the answer admits it

> "I used email addresses as the primary identifier, rather than names alone,
> to avoid incorrectly flagging different people with similar names."

So one person with a work address and a personal address is still two people
to it. That is the last line of the voiceover, and the beat under it is the
duplicate list itself — one name, two account teams — which is exactly what
the caveat is about.

**Not yet confirmed by her.** She sent the recording without the "one thing
you'd still change", so this is the brief's prediction plus the answer's own
words, and it goes to her with the cut.

## Beats

| Beat | t | What it shows |
| --- | --- | --- |
| b0-prompt | 30.00s | the sent prompt, the PDF attached, "Analyzing…" |
| b1-overall | 72.00s | 140 duplicates, still inside the 2,000-seat capacity |
| b2-dupes | 77.50s | 280 records, all 140 between Client and Prospect |
| b3-remaining | 100.50s | 2,125 → 1,985, 15 seats left, 99.25% |
| b4-bottom | 103.00s | "15 seats available, but reconcile the categories" |
| b5-list | 95.00s | the duplicate list: two teams against each name |

**b5 sits 8 seconds earlier in the recording than b4**, because the beats
follow the voiceover rather than the scroll and the twist is the last thing
said.

**The timestamps were checked against the frames, not assumed.** A first pass
put the seats-remaining block at 103s and the email note at 100.5s. On screen
it is the other way round, and by 103s the answer has scrolled on to the
recommendations. Looking at the frames is the only thing that catches that.

Beats are selected by frame number (`eq(n,N)`), never a time window: at 60fps
`between(t,T,T+0.02)` spans one or two frames, and on Nov 10 six such windows
matched eleven frames and every beat after the second was silently wrong.

## Cards

Hook at 0:00–2:30, end card in the last 3s, nothing between.

**No BUDGET line on this one.** The Nov 3 soft mention covers Thu 5, Mon 9,
Tue 10 and Tue 17 only, and Tue 10 came off it on Nov 9, so this Reel ends on
the guide's own takeaway overlay: "Dedupe the lists before you say you're
sold out." The same line on both cuts — nothing here turns on a bio link.

The hook sits at y=1240 over the prompt bubble's last line, the same shape as
Tue 10. The end card sits at y=1020 on the duplicate list: the beat's job is
one person against two account teams, which the header and the first seven
rows already show, so the card covers rows that only repeat it. Both cards
are opaque, as on Tue 10, because every card here lands on a table or a dense
paragraph rather than white space.

## Checks

- **Ad check clean.** The whole 107.6s source at 1fps over the bottom 460px,
  and then the exported mp4's bottom 340px at 1fps through to its final
  frame. No ad in either — worth stating rather than assuming, since nine
  advertisers have turned up in these recordings so far and the last three
  arrived late in the clip.
- Hook verified present on the **exported** frames at 1.0s and 2.0s and gone
  by 2.6s; end card present at 16.0s and on the last frame, absent at 14.0s.
- All six beat frames were looked at whole, which is a stronger check than a
  bottom-strip scan: the 4% push only ever shows less of a beat, never more.
- Loudness measured on the finished exports, not on the voiceover.
- **The gain was swept, not computed.** Eryn came out at -23.74 LUFS with
  peaks at -1.80 dBTP, and it took **+12.4 dB** through
  `alimiter=limit=0.841:level=0` to measure -14.01.
- 52 words in 18.48s is 2.81 w/s, in line with the 2.74 measured on Tue 10 and
  well under the 3.1 planning figure.
