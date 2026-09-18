# RSVP meal counts reel — 2026-09-18 (built 09-17)

Comment-to-unlock keyword: **CATERER**. Not on the guide's assignment list,
so nothing to clash with; worth adding to that list.

Status: **published 2026-09-18.** Live on Instagram and Facebook, captions
verified against the approved text character for character.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DdbftmjgmIB/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1672652570949483/ |

Posted by the scheduled routine at 9am ET, approved by the author the day
before. The publish call returned an MCP client timeout at 60s while
`max_wait_seconds` was set to 300; both posts had in fact succeeded
server-side. State was checked before doing anything else rather than
retrying, which would have duplicated the Facebook post. **Next time keep
`max_wait_seconds` under the 60s client timeout, or publish Instagram and
Facebook in separate calls.**

TikTok was not posted from here; that cut is uploaded by hand per the guide.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, voiceover at -14 LUFS.

| File | Platform | Duration | Ramp | Time to payoff | Opening line |
| --- | --- | --- | --- | --- | --- |
| `rsvp-instagram.mp4` | Instagram, Facebook | 16.48s | 3.0x | 5.38s | "Thirty RSVPs, four meal types, nine different dietary restrictions — and the caterer needs this two weeks out." |
| `rsvp-tiktok.mp4` | TikTok (manual post) | 16.93s | 2.7x | 5.63s | "Stop hand-counting your RSVP meal choices." |

End card on both: "Save this before your next final count."

## Source handling

First single-file recording of the week: 23.67s at 20.9 MiB, under the
upload limit, no splitting or seam matching needed. The send tap lands at
0.30s, so the opening follows the standing rule.

Generation ends at 11.0s. Nothing is cut: the whole span from 2.05s runs at
3.0x, and the reveal plays start to finish at normal speed, ending on the
footage's own static tail rather than a synthesised freeze. The reveal
carries the payoff the hook promises — the total of 30, the nine-guest
dietary table, and the allergy alerts.

Both voiceover uploads are byte-identical (same md5); either works.

16 frames sampled across the recording at 1.5s intervals; no in-app ads.

## Silent tail

The voiceover is 12.54s against 16.48s, leaving 3.9s. That is the shortest
tail since Sep 13 and comes from holding the total to the low end of the
range, as the timing rules ask when the voiceover is short.
