# 2026-10-27 — Rebuild 1: the Sep 1 post-event ROI report

Tue 27 Oct's 6:30pm Instagram Reel. The first of the four rebuilds by number,
the last to actually get built, because its master went missing for a week.

## The hook

Approved by Sahiba on 2026-10-16 ("2 is good"):

> **If you didn't define success before the event, you can't prove it after.**

It replaces *"A $85,000 corporate summit just wrapped, and leadership wants
proof it was worth it."* The brief's own diagnosis: that opening is a
hypothetical, which breaks the true-moment rule, and "proof it was worth it" is
abstract for a first line. The new one is her own sentence, from her answer to
the rebuild question.

**NO EMPLOYER, anywhere.** Her answer named one and she asked in the same breath
for it kept out — of the piece, the caption and the overlay.

## Where the master came from, after two dead ends

| Source | What it is | Verdict |
| --- | --- | --- |
| This repo | — | The Sep 1 piece predates it |
| Drive `October 27` | the packing list only | Not there |
| Instagram's own CDN | **720x1280**, 19.5s, 871 kbps | **Rejected** |
| **Her upload, 2026-10-26** | **1206x2144, 60fps, 19.5s, 4.76 MB** | **Used** |

The CDN route does work — `INSTAGRAM_GET_IG_USER_MEDIA` for the `media_url`,
then `GOOGLEDRIVE_UPLOAD_FROM_URL` to pull it server-side past the egress
block — and the file it returns is in `October 27` as
`2026-09-01-roi-report-INSTAGRAM-CDN-720.mp4`. It is two-thirds the resolution
and a second-generation encode, and this piece is a **screen recording**, so an
upscale would soften every letter in it. A rebuild exists to measure whether a
new hook moves skip rate; a softer picture moves watch time on its own and
ruins the only number the experiment is for.

**The URL announces the resolution before you download it.** Its `vencode_tag`
reads `xpv_progressive.INSTAGRAM.CLIPS.C3.720`. Read that and skip the fetch.

**Her file is better than the posted version, not worse.** 1206x2144 is the
native crop of the screen recording — one step before the export that went out
— and it is the exact 0.5625 ratio, so 1080x1920 comes out of it by a clean
downscale. 60fps halves to 30 without resampling.

## The edit

| | |
| --- | --- |
| Splice | **3.03s**, inside the master's own 2.864–3.204 silence, so the opening sentence is replaced whole rather than cut mid-word |
| Opening frame | **t=10.00s** — the cost-breakdown table, with the $85,000 total and the $567 cost per attendee on screen. The rebuild rules say open on the finished result, not the typing |
| Opening length | VO + 0.30s |
| Card | cy=560, where the original's sat, so the one visible change is the words |
| Everything after 3.03s | the original edit, rescaled to 1080x1920 and 30fps and nothing else |

**The opening frame is frozen, and the first build got that wrong.** It fed
`-ss 10 -i SRC` straight into `tpad`, which does not freeze anything — it plays
the master from 10.00s, and the body replays that same stretch seconds later.
The viewer would have watched one scroll twice. The frame is now extracted to a
PNG and looped.

## Loudness is matched to the master, not to −14 LUFS

The master runs **−21.45 LUFS** and the body has to stay as it was or the
control is gone, so the new opening line is brought to the master's level
instead of the house target. The Oct 15 rebuild did the same and shipped at
−21.2 against its master's −21.3.

## Two cuts, and the reason is the voice change

The voice changed to Eryn on Oct 25, mid-rebuild. A rebuild replaces only the
opening line, so an Eryn opening on a Vanessa body means the voice changes three
seconds in — audible, and not something the experiment is testing.

- `roi-report-rebuild-eryn.mp4` — her standing instruction, which named this
  piece explicitly.
- `roi-report-rebuild-vanessa.mp4` — matches the body, one voice throughout.

Hers to pick. Nothing else differs between them.

## Caption

`build/caption.txt`. Per the rebuild rules it is the original caption with its
first line swapped for the new hook, and `#theeventplannerai` — a dead handle —
replaced by `#aiforeventplanners`. The prompt block and the closing question are
untouched.
