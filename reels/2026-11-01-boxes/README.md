# Sun 1 Nov — boxes shipped to the venue (Reel)

Two cuts, 18.0s each, 1080x1920. Instagram and Facebook at 6:30pm Eastern after
her go-ahead; TikTok hers, handed over the moment she approves the Instagram
cut.

**First post on the far side of the clock change.** Eastern goes to UTC−5 that
morning, so 6:30pm Eastern is **23:30 UTC**, not 22:30.

## The source

One file, hers, filmed Fri 30 Oct and dropped into Drive: a 1206x2622, 62.3s,
60fps HEVC screen recording. She pastes the packing list prompt into ChatGPT
with the list inline, and the answer runs to a box-by-box manifest, a tracking
and sign-off table, a note to the hotel's receiving team, and three things
still needed before shipping. It is not in this repo; raw media never is.

She was sent the prompt and the packing list as one pasteable block, so the
Google Sheet never had to be opened on the phone.

## There is no twist, and that is her call

The guide's Oct 14 twist note predicted the model would build a tidy manifest
and miss the question that actually stops boxes going missing — the earliest
date the hotel accepts deliveries, and whether it charges to hold them.

It did not play out that way. The answer's own opening line reads: *"I've
organized the shipment into six boxes by destination room so the hotel can
distribute them easily. I've also flagged the missing tracking numbers,
delivery dates, and receiving contact rather than inventing details."* It then
leaves every sign-off as TBD and every tracking number as Pending, and closes
with "Three things still needed before shipping".

Asked what she would still change, she said: **"Nothing"**. So this ships as a
straight demo — the brief's voiceover, the brief's takeaway, the brief's
caption, with no "genuinely good, except…" paragraph bolted on to a piece that
does not have one.

## The ninth advertiser is in this recording

**Amazon Business**, at ~58.5s: *"For bulk conference supplies, here's one
Amazon Business option."* — then the logo and a small Ad marker.

It is the second on-topic ad after TicketSpice and the harder of the two to
catch, because the sentence that introduces it is in the answer's own voice and
the answer's own type, sitting directly under a genuine recommendation about
labelling boxes. **The ad starts at that sentence, not at the logo.** Added to
CLAUDE.md's list.

Both cuts end well clear of it: Instagram at 47.3s of source, TikTok at 56.3s.

## Build

    python3 make_cards.py
    python3 render.py

| | Instagram | TikTok |
| --- | --- | --- |
| Hook, 0:00–0:02 | "Six boxes shipped to the venue. Here's how all six make it to the room." | "Stop shipping boxes without a manifest." |
| Time to payoff | **3.40s** | **3.00s** |
| Ends on | the note to the receiving team | "Three things still needed before shipping" |
| Voiceover | Eryn, 46 words, 14.21s | Eryn, 47 words, 14.45s |

Crop `1206:2144:0:478`, computed from the source: 1206 / 0.5625 = 2144. The
standard y-offset applies here — nothing the cut needs sits in the top band.

**The prompt beat starts at 5.8s of source, not 4.4s.** She scrolls up to the
top of her own prompt and then back down, so the *earlier* frames are further
into it: at 4.4s the opening line is already above the crop and the cut would
open mid-sentence. 5.8s is where the first line is back in frame.

**Every overlay card's bottom clears y=1440**, the top of the bottom 25% that
the platform's caption and buttons cover. That sets the three y values
(1070, 1198, 1118), not taste — a first build put all three at 1240–1300 and
each ran 200px or more into the covered band.

Every beat runs at 1x. She scrolled at a readable pace, so there is nothing to
compress and nothing to slow down.

## Audio

Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), both scripts generated here. The
Instagram script is the guide's as written; TikTok's opens command-style, as
the house rules require.

Measured source: Instagram −24.3 LUFS / −1.9 dBTP, TikTok −24.4 / −1.7. Gain is
applied explicitly with `alimiter=limit=0.841:level=0` catching the peaks —
`level` defaults to auto and renormalises everything back to full scale, which
looks exactly like the limiter not working. The figures are tuned against the
export rather than computed: 11.5 dB landed at −15.1 and −14.7.

## Caption

`build/caption.txt`, md5 `eedf79b3`. The guide's, with the house layout: body,
blank line, `AI Prompt: "…"`, blank line, save line, four hashtags. No employer
and no client is named.
