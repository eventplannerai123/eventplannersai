# Handwritten consultation notes reel — 2026-09-19

Comment-to-unlock keyword: **NOTES**. Now on the guide's assignment list
(added in the Sep 19 revision, alongside CATERER).

Status: **published 2026-09-19.** Approved in conversation, then posted to
Instagram and Facebook.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DdeNg6tCTt9/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1748053619796411/ |

Both captions were read back live and compared to the approved text byte
for byte - identical on both platforms, with the four hashtags carrying a
literal `#` rather than `%23`. Facebook reports the video length as
17.166s, matching the cut.

Instagram publish used `max_wait_seconds: 45`, under the 60s MCP client
timeout that bit on Sep 18; the container reached FINISHED after 18.9s.
Facebook did not appear in the page feed on the first read-back - it was
still processing. It was re-read rather than re-posted, since
`FACEBOOK_CREATE_VIDEO_POST` has no duplicate protection.

TikTok is not posted from here; that cut is uploaded by hand per the guide.

## Accuracy check (requested in the brief)

The brief asked for confirmation that the AI-generated organization is
actually accurate to the real notes before proceeding, since a visible
misread would undercut the premise. The handwritten page was transcribed
from the fullscreen frame at native resolution and checked line by line
against ChatGPT's output. The author then sent the original photo, and the
check was re-run against that rather than against a video frame.

**No errors and no fabrications.** Everything on the page is carried
through: event date November 12 2026, 6-8pm; 200 guests, cocktail
reception; coat check with a check-in table that becomes the exit giveaway
table, name tags; in-house stage; A/V needs an outside vendor with a venue
preferred list; the run of show (5:30 / 6:00 / 6:30 / 7-8 / 8); passed
apps; wine and beer only; live music with suggestions needed; minimal,
elegant florals; in-house votives; and the load-in time question.

The sideways margin note — "is there a speaker green room?" — is picked up
and quoted, and appears in the final "Still needs confirmation" list. That
is the detail the voiceover's claim about catching unanswered questions
rests on, so it is worth noting it is genuinely on screen.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
voiceover normalised to -14 LUFS (measured -13.8).

| File | Platform | Duration | Ramp | Time to payoff | Opening line |
| --- | --- | --- | --- | --- | --- |
| `notes-instagram.mp4` | Instagram, Facebook | 17.17s | 2.44x | 5.50s | "This is what my actual consultation notes look like." |
| `notes-tiktok.mp4` | TikTok (manual post) | 17.43s | 2.30x | 5.59s | "Stop retyping your handwritten client notes." |

End card on both: "Save this before your next client meeting."

## Structure

Five segments, because the notes photo and the send tap both have to land
before the generating beat:

1. Send tap — clip A 0.35-1.25. The prompt is already in the input box with
   the photo attached and the tap is on camera at 0.63s, so the standing
   rule holds without faking an opening.
2. Notes fullscreen — clip A 5.10-6.40.
3. Freeze hold on the notes frame — 23 (IG) / 20 (TikTok) extra frames.
4. Generating — clip A 6.40-12.50 sped 2.44x (IG) / 6.40-12.30 at 2.30x.
5. Reveal — clip B 2.65-14.30 (IG) / 2.45-14.30, normal speed throughout.

### Representative slice of the generating phase

Flagging this per the timing rules. The real generating phase runs from
6.4s to the end of clip A and on into clip B — well over the ~4 seconds the
rules ask for, and visually static the whole way (a single "Inspecting
image dimensions" line on an otherwise empty screen). Segment 4 is a
representative slice of it rather than the whole span compressed, and the
cut from it into the reveal skips roughly 5.9s of that static wait.

### The freeze hold

Without it the notes photo is on screen for about 1.3s, most of it under
the hook card, which is not long enough to register what the hook is
pointing at. The hold extends the notes beat to 2.10s (IG) / 2.00s
(TikTok), leaving roughly 0.95s of it unobstructed after the hook fades.

## QC notes

Three problems were found in the first render and fixed before delivery:

- **TikTok video stream ran 0.58s short of its audio.** The `-t` total
  exceeded the concatenated video length, so the cut would have ended on a
  held frame with voiceover still playing. Both files now have video and
  audio within one frame of each other.
- **Time to payoff was over the ceiling.** IG landed at 5.95s and TikTok at
  6.11s, which breaks the 6-second rule outright. Rebalanced by shortening
  the opening and pinning the generating beat to its 2.5s minimum.
- **End card was unreadable.** At the usual alpha 196 the dense "Still
  needs confirmation" list bled straight through it. The end card is now
  filled at alpha 240; the hook cards are unchanged.

Ad check: 21 frames sampled across both raw clips; no in-app ads.

Clips A and B overlap — B's first frame matches A at 15.80s (MAD 0.002) —
but the seam used here is not that overlap. It is a deliberate jump past
the static generating wait, which is why the two clips' timelines do not
run continuously across segments 4 and 5.

## Silent tail

The voiceover is 16.85s against a 17.17s cut, leaving 0.32s. Both totals
are held near the low end of the range, as the timing rules ask when the
voiceover is short.
