# Wedding getting-ready timeline reel — 2026-09-12

CTA experiment: binary/simple choice. The caption closes on a two-option
question (on-site vs. salon), the same shape as Sunday Round 3's
half-day/full-day question.

Status: **published 2026-09-12.** Live on both accounts, captions verified
against the approved text character for character.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DdL-u8jjGJN/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/4629453164047728/ |

Posted as a Reel shared to feed. Hashtags render as `#tag`, not the
`%23tag` the Composio field docs warn about, so pass literal `#` next time.
Meta fetched the video from its raw GitHub URL on this branch, so moving or
renaming the file would break the live posts. The TikTok cut was not posted.

## Cuts

Both 1080x1920, H.264 high, 30 fps, AAC 192k, voiceover at -14 LUFS.

| File | Platform | Duration | Speed ramp | Opening line |
| --- | --- | --- | --- | --- |
| `wedding-timeline-instagram.mp4` | Instagram, Facebook | 16.32s | 3.0x | "A 3pm ceremony means the morning starts way earlier than most people think." |
| `wedding-timeline-tiktok.mp4` | TikTok | 16.51s | 2.6x | "Build your getting-ready timeline backward from 3pm." |

## Structure

The Instagram cut runs: 2.5s at normal speed over the send tap, 4.0s of
sped-up generating, then 9.8s back at normal speed on the finished
timeline, ending on a 2.7s fully static hold. The TikTok cut opens 0.4s
shorter, ramps a little slower, and holds the reveal 0.4s longer.

The voiceover runs 11.2s, so the last ~5s of each cut is a silent hold on
the backward timeline with the save prompt up. That is the read beat.

## Source handling

The raw recording is 1206x2622, taller than 9:16. It is cropped to
1206x2144 at y=478 and scaled to 1080x1920. That offset drops the status
bar and the floating header buttons off the top and keeps the whole
ChatGPT input bar at the bottom, where the platform UI covers it anyway.

No stock footage and no generated visuals. The recording's own audio track
is digital silence, so the uploaded voiceover is the only audio. No in-app
ads appear anywhere in the recording, so the reveal needed no retiming.

## Rebuilding

    build/make_cards.py                       # regenerates the text cards
    build/render.sh <recording.mp4> <vo.mp3> . # rebuilds both cuts

## Caption as approved

A 3pm ceremony means the morning starts way earlier than most people think — here's the full timeline. Hair and makeup on-site or at a salon — which do you always recommend?

AI Prompt: "Create a getting-ready morning timeline for a wedding: ceremony starts at 3pm, hair and makeup for 6 people starting at 8am (45 min each), photographer arrives at 12pm for detail shots, dress goes on at 1:30pm. Build a full timeline working backward from ceremony start."

#aiforeventplanners #weddingplanningtips #eventprofs #eventplanningtips
