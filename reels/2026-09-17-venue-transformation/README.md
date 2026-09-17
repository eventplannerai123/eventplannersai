# Venue transformation reel — 2026-09-17

Comment-to-unlock keyword: **TRANSFORM** (unused; FLORAL went to the Sep 15
post).

Status: **rendered, awaiting approval.** Nothing posted.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, voiceover at -14 LUFS.

| File | Platform | Duration | Ramp | Time to payoff | Opening line |
| --- | --- | --- | --- | --- | --- |
| `transform-instagram.mp4` | Instagram, Facebook | 16.20s | 2.80x | 5.51s | "This is the actual empty room." |
| `transform-tiktok.mp4` | TikTok (manual post) | 16.40s | 3.0x | 5.13s | "Stop showing clients an empty room." |

End card on both: "Save this before your next client meeting."

## Structure

The clips are in the opposite order to their filenames: `1234ea46` is first
(send tap, empty room, generating), `e62ce9e2` is second (generating tail,
decorated reveal).

The opening keeps the send tap at 0.58s, then jumps to the fullscreen empty
room, which runs 4.60-6.40s in clip one. That puts the real empty room full
frame under the hook text and under the voiceover's opening line, which is
the same sentence. The reel ends held on the fullscreen decorated room.

Two stretches are cut rather than compressed, as the brief permits for long
image generation: clip one 1.30-4.60s and clip two 0-3.00s, both static
generating states. What remains of the generating phase runs at 2.80x
inside the 6-second payoff ceiling.

The fullscreen viewer closes at 9.65s in clip two, so the reveal ends at
9.50s. An earlier render froze past that point and ended on the chat view
instead of the decorated room; the final-frame brightness is now asserted
in the render check.

## Netflix notification

The author asked for it to be edited out. It is not present: the top 700px
of both clips were scanned at 5 fps across 122 frames, including a check for
saturated red. The only red is 28 pixels in every frame, which is the
screen-recording dot in the dynamic island.

It could not have survived regardless. The standard y=478 crop removes the
clock, dynamic island and back-to-Claude row, which is where an iOS banner
sits.

No in-app ads appear in either clip.
