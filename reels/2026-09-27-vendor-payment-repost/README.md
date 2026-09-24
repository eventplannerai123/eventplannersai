# Vendor payment schedule — Instagram repost, 2026-09-27

Status: **blocked on the source file.** Caption is ready; there is nothing to
export yet.

Sunday Sep 27 carries two Instagram posts, which is the only day of the week
that is true:

| Post | Where it is made | Who posts it |
| --- | --- | --- |
| Storage room photo → inventory list | Claude.ai chat, Trial toggle | **the author, by hand** |
| **This repost** — Sep 3 vendor payment schedule | here | this session |

A Trial Reel reaches only non-followers, so on a trial day the 280 followers
see nothing in feed and nothing lands on the grid. The repost reaches a
separate audience and the two do not compete.

## Do not post the trial from here

The Trial toggle is in-app only. Anything published from this session goes out
as a regular feed Reel, which would waste the trial **and** trip Instagram's
duplicate-content detection if the same piece later went up as a trial —
throttling both for up to 30 days. The guide's Sep 27 block says so outright:
"DO NOT POST — planned trial".

## The blocker: the original file

The Sep 3 reel predates this repo (it starts Sep 12), so the source mp4 is not
here.

Two routes were tried and neither works:

| Route | Result |
| --- | --- |
| Download from the live post via the Graph API `media_url` | **Egress-blocked.** `scontent-iad3-1.cdninstagram.com:443` → `connect_rejected` by the proxy's organization policy. |
| Use that copy anyway if it were reachable | **Would be wrong.** The URL's own encode tag reads `CLIPS.C3.720` — Instagram's 720p transcode, not the 1080x1920 original. Re-uploading an upscaled 720p transcode would be visibly soft, which is worse than the reach problem the repost is meant to fix. |

So the original has to come from the author. It is a 16s screen-recording
piece, well inside the ~30 MB chat ceiling, so a single upload at
"Actual"/"Original" size covers it.

The live post, for reference:

| | |
| --- | --- |
| Permalink | https://www.instagram.com/reel/Dc04ivflJtl/ |
| IG media id | `18437908249177797` |
| Published | 2026-09-03T13:08:57Z |
| Original performance | 13 views / 12 reach — the lowest of any post |

That is what makes this a repost worth making: genuinely unseen rather than
genuinely unpopular.

## Re-export, not a byte-for-byte copy

The guide is explicit: **do not re-use the exact original file.** Duplicate
detection can throttle both copies. Once the source arrives, re-encode it
(same 1080x1920 / 30 fps / CRF 19 / AAC 192k spec, fresh encode) so the two
files differ, and verify the md5 is not the original's.

Space it several hours from the author's trial upload.

## Caption

`build/caption.txt`, md5 `363bfca762c4f1c9d4c187b02eae3241`, 756 bytes.

Assembled from the guide as follows:

| Part | Source |
| --- | --- |
| Body | The Sep 27 block's "Repost caption", verbatim. Ends on "The full prompt is in the caption below." |
| AI Prompt | The **original Sep 3 block's** prompt, verbatim, as the guide's repost handling requires. |
| Hashtags | The original Sep 3 four, with `#theeventplannerai` swapped for `#aiforeventplanners` — the old handle points at an account name that no longer exists. |

**The hashtags are the one judgement call.** The guide specifies the body and
the prompt for this repost but says nothing about hashtags, so the original
post's four were carried over with the dead handle replaced. Worth a glance
before it goes out.

The original Sep 3 caption ended "How many deposits are you tracking right
now, honestly? Comment the number." That is dropped — the guide supplies a
fresh body for the repost, and it closes on the prompt line instead.

## A bookkeeping error in guide_6

The Sep 27 block carries **two** "Second post that day — repost" paragraphs:
the Sep 3 vendor payment schedule and the Sep 2 seating chart. The Sep 28
block carries none. The second paragraph is Sep 28's, misfiled one block up.

CLAUDE.md already has the split right — Sep 27 is the vendor payment
schedule, Sep 28 is the seating chart — so nothing here was built from the
wrong one. Flagged so the guide gets fixed rather than the error being
rediscovered on Monday.

## Also Sunday, and not from here

The TikTok back-catalogue upload for the day is the **Sep 2 seating chart
Reel** (instagram.com/reel/DcyeB4dlQck/), a manual TikTok upload. Its caption
is ready in the guide with the handle already swapped. TikTok cannot be
published from here at all.
