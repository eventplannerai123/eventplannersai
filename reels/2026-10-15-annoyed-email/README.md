# 2026-10-15 — The annoyed email

The Thu 15 Oct quick piece. **One cut, three platforms.** TikTok is hers — the
file was handed over and she posted it on Oct 15. The same file then went out
from here that evening as the day's **second Instagram post**, and to Facebook.

## Published 2026-10-15

| Where | Post | When |
| --- | --- | --- |
| TikTok | hers — confirmed "i posted it, all good" | Oct 15 |
| Instagram | https://www.instagram.com/reel/DeiCY8mDrRr/ | 6:31pm ET |
| Facebook | https://www.facebook.com/reel/1117454167422413/ | 6:32pm ET |

Instagram media id `17913216915284218`, Facebook post id
`1233196746554445_122116025217449533`. **Both live captions compared to
`build/caption-tiktok.txt` and identical** — four literal `#`, hashtags
included per her Oct 15 rule.

Her instruction: "Claude Code posts the annoyed email to Instagram and Facebook
this evening, with hashtags, as a second post after the rebuild." Both feeds
were read first and the piece was on neither; the day's main post, the deposit
tracker rebuild, was already up at 9:30am ET, so this was correctly second.

**The same cut, not a re-cut.** The guide's Thu 15 line says "post the
annoyed-email cut", and a quick piece gets one cut — so TikTok, Instagram and
Facebook all carry the identical file. The never-both-cuts-to-one-platform rule
is about two different cuts on one platform, which is not this.

| | |
| --- | --- |
| TikTok | `annoyed-email-tiktok.mp4` — 15.60s, −14.5 LUFS |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz. Inside the 15–20s quick-piece window, at the low end of it because
the voiceover is short.

## The piece

She pasted a deliberately snippy chase email — third ask for the final AV specs
— and asked for it firm but not rude. What makes it worth 15 seconds is what
the rewrite *keeps*: the end-of-day deadline and the invoice correction both
survive. Only the contempt goes.

That is the takeaway card, and the voiceover, and the reason beats 2 and 3 are
the two frames they are.

## The recording opens right

Prompt sitting in the input box with the send arrow still showing at t=0.3 —
the opening the guide's Oct 5 rule 2 asks for, with nothing faked. Third
recording in a row that opens correctly.

It is only **12.6s** long, which is short, but a freeze-frame piece needs
moments rather than duration and all four are in it: the prompt (0.3), the
whole snippy draft (3–6), the rewrite (9–12.4).

## Beats

Freeze frames, 0.20s dissolves. Clean band 1161x2064 at x=22, y=300.

| | Source | Cut | What it shows |
| --- | --- | --- | --- |
| 1 | t=0.5 | 0.00–2.70 | the prompt in the input box, hook card above it |
| 2 | t=5.5 | 2.70–5.75 | **"I honestly don't understand why this is so hard"**, highlighted |
| 3 | t=9.7 | 5.75–12.10 | the rewrite's whole consequence paragraph, highlighted |
| 4 | t=12.4 | 12.10–15.60 | the end of the rewrite, dimmed, takeaway over it |

**Time to payoff is 5.75s** — the rewrite is on screen before the 6-second
ceiling. That is what sets beat 2's length, not the voiceover.

Beat boundaries are cut to the voiceover's own pauses, measured with
`silencedetect` rather than guessed: it breaks at 2.25, 6.10, 8.85, 10.05 and
11.77, and the last word lands at 14.82.

**Beat 2 is from the prompt, not the answer.** The guide's quick-piece format
says "2–3 key lines of the answer". Here the line that carries the piece is in
the *draft she pasted* — the rewrite is only interesting against it — so beat 2
holds the contempt line and beat 3 the answer. Deliberate, and noted because it
reads as a deviation from the format.

## Beat 3 moved, and why

The first pass put beat 3 at **t=10.5** with a 3-line highlight. `preview()`
showed the box sitting on *"them by then, I'll proceed with sourcing / the
projector independently and will / expect the associated cost to be"* — a
fragment starting mid-sentence. At 10.5 the paragraph is cut by the frame and
**no** slice of it is a whole sentence.

At **t=9.7** all six of its lines sit at y 790–1230, inside the Oct 5 safe
band, so the highlight covers the sentence entire: *"Please send the complete
AV specs by end of day tomorrow. If I don't receive them by then, I'll proceed
with sourcing the projector independently and will expect the associated cost
to be deducted from your invoice."*

**Caught before anything was rendered**, which is the whole point of the
preview step added on Oct 14.

## Overlays

First build to use `tools/cardkit.py` for every box — **no coordinate in this
build was typed by hand**. Each highlight is a seed y plus a line count, snapped
to the frame's real ink.

| | Position | Width |
| --- | --- | --- |
| hook | y 244–456 | — |
| "honestly don't understand / why this is so hard." | y 890–1039 | 60% |
| the consequence paragraph | y 778–1242 | 88% |
| takeaway card | y 695–1005 | — |

All inside the Oct 5 safe band (nothing above y=230 or below y=1440), asserted
by `build/make_cards.py` and then checked again on the exported frames.

Hook (command-style, TikTok): **"Stop sending the email you wrote angry."** It
sits in the white space above the input box, so it covers no part of the
prompt.

Takeaway: **"The deadline stayed. / The invoice line stayed. / Only the sarcasm
went."**

ChatGPT's floating scroll-to-bottom button is left in frame, per Oct 10.

## No ad

**No in-app advertiser anywhere.** The bottom 700px of the raw 12.6s was
scanned at 1s intervals, and then the bottom 340px of the finished mp4 through
to its final frame. Third clean recording in a row.

## Voiceover

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`. 38 words, inside the format's 30–40:

> Stop sending the email you wrote angry. Third time asking, and I nearly sent
> something I'd regret. AI kept every consequence — the deadline, the invoice
> correction — and cut the one line that would have cost me the vendor.

15.09s against a 15.60s cut, so there is a 0.5s hold on the takeaway at the
end. **`-shortest` was removed from the export** — it truncated the video to
the audio length and ate that hold.

Loudness: measured first pass (−21.3 LUFS), explicit gain, `alimiter` with
`level=0` at a −1.0 dB ceiling. `TRIM` is **1.75** here, not the usual 1.10:
at 1.10 the finished file measured −14.8, which is a long way under.

## Caption

`build/caption-tiktok.txt` — the guide's Thu 15 wording verbatim. No "Prompt
below." to strip; it carries none.

One thing left for her to decide: the guide's own quick-piece rule says the
caption's **first line states the takeaway**, and this day's pasted caption
opens with a description instead. Handed over as written.
