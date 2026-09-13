# DIY vs florist centerpiece cost reel — 2026-09-13

Comment-to-unlock keyword: **CENTERPIECE** (Sep 13 assignment in the guide's
keyword list; not reused from CONTRACT on Sep 10).

Status: **published 2026-09-13.** Live on Instagram and Facebook, captions
verified against the approved text character for character.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DdOks0FjmRO/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1578909337365274/ |

TikTok was not posted from here: the guide records Composio's TikTok
integration as unable to publish publicly, so that cut is uploaded by hand.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, voiceover at -14 LUFS.

| File | Platform | Duration | Ramp | Time to payoff | Opening line |
| --- | --- | --- | --- | --- | --- |
| `centerpiece-instagram.mp4` | Instagram, Facebook | 17.50s | 2.69x | 5.60s | "DIY centerpieces barely save you anything once you count the hours." |
| `centerpiece-tiktok.mp4` | TikTok (manual post) | 17.90s | 3.0x | 5.18s | "Stop calling DIY centerpieces the cheap option." |

End card on both: "Comment CENTERPIECE for the full cost breakdown."

## Source handling

The raw recording arrived as two clips because the 63-second original
exceeded the upload limit, and Google Drive is blocked by the session's
egress policy. Clip 1 at 15.550s was frame-matched to clip 2 at 0.000s
(mean absolute difference 0.002) and the two were joined into a single
36.45s source at 60 fps.

Cropped 1206x2144 at y=478 and scaled to 1080x1920. That offset drops the
status bar and the red recording dot off the top, which a y=0 crop would
keep. This deviates from the guide's stated `crop=1206:2144:0:0`; it matches
what shipped on Sep 12 and is flagged for the author to settle.

Source 11.60 to 24.55 is cut entirely, to fit 36 seconds of footage into the
target length while holding the generating beat under the 6-second ceiling.
The cut lands on the "Now let's count ALL the DIY labor" heading so it reads
as a section change rather than a skip. Both cuts end on the break-even
frame, held as a freeze so it stays readable.

No in-app ads appear anywhere in the joined footage.

## Standing rules checked

- Footage in motion from frame one, no static title card
- Prompt pre-typed and sitting in the box, send tapped on camera
- Generating beat 3.40s (IG) / 3.08s (TikTok), above the 2.5s minimum
- Time to payoff under the 6-second combined ceiling on both
- No rolling mid-video captions, hook and end card only
- True 9:16 verified with ffprobe

## Rebuilding

    build/make_cards.py
    build/render.sh <joined-source.mp4> <vo.mp3> .
